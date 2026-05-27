"""
Glossario Acronimi - v3
- Fuzzy finder in tempo reale
- Push unico al ritorno al menu, con commit message intelligente
- glossario.txt sempre nella cartella dello script
"""

import msvcrt
import os
import sys
import subprocess
from pathlib import Path

SCRIPT_DIR    = Path(__file__).resolve().parent
GLOSSARIO_FILE = SCRIPT_DIR / "glossario.txt"
MAX_RESULTS   = 8

# Abilita sequenze ANSI su Windows (necessario per PowerShell / CMD)
os.system('')


# ── Git ────────────────────────────────────────────────────────────────────────

def git_commit_push(modifiche: list):
    """Commit + push con messaggio adattato al numero di modifiche."""
    if not modifiche:
        return

    if len(modifiche) == 1:
        tipo, acronimo, dettaglio = modifiche[0]
        if tipo == 'aggiunta':
            msg = f"Aggiunta acronimo '{acronimo}' = '{dettaglio}'"
        elif tipo == 'modifica':
            msg = f"Modifica '{acronimo}': {dettaglio}"
        else:
            msg = f"Eliminazione acronimo '{acronimo}'"
    else:
        n_a = sum(1 for t, _, _ in modifiche if t == 'aggiunta')
        n_m = sum(1 for t, _, _ in modifiche if t == 'modifica')
        n_e = sum(1 for t, _, _ in modifiche if t == 'eliminazione')
        parti = []
        if n_a: parti.append(f"{n_a} aggiunta/e")
        if n_m: parti.append(f"{n_m} modifica/he")
        if n_e: parti.append(f"{n_e} eliminazione/i")
        msg = "Glossario: " + ", ".join(parti)

    try:
        subprocess.run(["git", "add", str(GLOSSARIO_FILE)],
                       cwd=SCRIPT_DIR, check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", msg],
                       cwd=SCRIPT_DIR, check=True, capture_output=True)
        subprocess.run(["git", "push"],
                       cwd=SCRIPT_DIR, check=True, capture_output=True)
        print(f"\n  ↑  Push completato: {msg}")
    except subprocess.CalledProcessError as e:
        print(f"\n  ⚠  Errore git: {e}")


# ── I/O glossario ──────────────────────────────────────────────────────────────

def carica_glossario():
    glossario = {}
    try:
        with open(GLOSSARIO_FILE, "r", encoding="utf-8") as f:
            for riga in f:
                riga = riga.strip()
                if " = " in riga:
                    acronimo, significato = riga.split(" = ", 1)
                    glossario[acronimo.strip().upper()] = significato.strip()
    except FileNotFoundError:
        pass
    return glossario


def salva_glossario(glossario):
    with open(GLOSSARIO_FILE, "w", encoding="utf-8") as f:
        for acronimo in sorted(glossario):
            f.write(f"{acronimo} = {glossario[acronimo]}\n")


# ── Fuzzy finder – rendering ───────────────────────────────────────────────────

def build_lines(query: str, glossario: dict) -> list[str]:
    """Costruisce le righe da visualizzare nel finder."""
    q = query.upper()
    matches = sorted(k for k in glossario if q in k)

    lines = [
        f"  Cerca: {query}\u258c",          # ▌ come cursore visivo
        f"  {'─' * 45}",
    ]

    if matches:
        for k in matches[:MAX_RESULTS]:
            marker = "\u25b6 " if k == q else "  "   # ▶ se corrispondenza esatta
            lines.append(f"  {marker}{k:<12} {glossario[k]}")
        if len(matches) > MAX_RESULTS:
            lines.append(f"  ... e altri {len(matches) - MAX_RESULTS}")
    elif query:
        lines.append(f"  (nessun risultato — Invio per aggiungere '{q}')")
    else:
        lines.append("  (digita per cercare)")

    # Righe fisse in fondo: sempre stessa altezza → niente sfarfallio
    while len(lines) < MAX_RESULTS + 2:
        lines.append("")

    lines += [
        f"  {'─' * 45}",
        "  [Invio] conferma   [Esc] torna al menu",
    ]
    return lines


def print_block(lines: list[str]) -> int:
    """Stampa il blocco (senza newline finale). Ritorna il numero di righe."""
    sys.stdout.write('\n'.join(lines))
    sys.stdout.flush()
    return len(lines)


def clear_block(n: int):
    """Cancella le n righe del blocco appena stampato."""
    # \r → inizio riga corrente
    # \033[{n-1}A → su di n-1 righe
    # \033[J → cancella da qui in giù
    sys.stdout.write(f'\r\033[{n - 1}A\033[J')
    sys.stdout.flush()


# ── Fuzzy finder – input loop ──────────────────────────────────────────────────

def read_key():
    """Legge un tasto; ignora tasti speciali (frecce, F*, etc.)."""
    ch = msvcrt.getwch()
    if ch in ('\x00', '\xe0'):
        msvcrt.getwch()   # consuma il secondo byte dei tasti speciali
        return None
    return ch


def fuzzy_finder(glossario: dict, modifiche: list) -> list:
    """
    Loop interattivo di ricerca.
    Esce (e ritorna le modifiche) quando l'utente preme Esc.
    """
    query = ""
    print()                                         # riga di separazione dal menu
    n = print_block(build_lines(query, glossario))  # primo render

    while True:
        ch = read_key()
        if ch is None:
            continue

        # ── Esc: torna al menu ──────────────────────────────────────────────
        if ch == '\x1b':
            clear_block(n)
            return modifiche

        # ── Invio: processa acronimo ────────────────────────────────────────
        elif ch == '\r':
            acronimo = query.strip().upper()
            if not acronimo:
                continue

            clear_block(n)

            if acronimo in glossario:
                print(f"\n  \u2714  '{acronimo}' = {glossario[acronimo]}")
                print("  [M] Modifica   [E] Elimina   [Invio] Niente")
                scelta = input("  > ").strip().upper()

                if scelta == 'M':
                    nuovo = input(f"  Nuovo significato per '{acronimo}': ").strip()
                    if nuovo:
                        vecchio = glossario[acronimo]
                        glossario[acronimo] = nuovo
                        salva_glossario(glossario)
                        modifiche.append(('modifica', acronimo, f"'{vecchio}' → '{nuovo}'"))
                        print(f"  \u2714  '{acronimo}' aggiornato.")
                    else:
                        print("  \u26a0  Campo vuoto, nessuna modifica.")

                elif scelta == 'E':
                    conf = input(f"  Eliminare '{acronimo}'? [s/N] ").strip().lower()
                    if conf == 's':
                        del glossario[acronimo]
                        salva_glossario(glossario)
                        modifiche.append(('eliminazione', acronimo, ''))
                        print(f"  \u2714  '{acronimo}' eliminato.")
                    else:
                        print("  \u21a9  Annullato.")

            else:
                print(f"\n  '{acronimo}' non è nel glossario.")
                significato = input(f"  Per cosa sta '{acronimo}'? ").strip()
                if significato:
                    glossario[acronimo] = significato
                    salva_glossario(glossario)
                    modifiche.append(('aggiunta', acronimo, significato))
                    print(f"  \u2714  '{acronimo}' salvato.")
                else:
                    print("  \u26a0  Campo vuoto, nessun salvataggio.")

            input("\n  Premi Invio per una nuova ricerca (Esc nel finder per uscire)...")
            query = ""
            print()
            n = print_block(build_lines(query, glossario))

        # ── Backspace ───────────────────────────────────────────────────────
        elif ch == '\x08':
            if query:
                query = query[:-1]
                clear_block(n)
                n = print_block(build_lines(query, glossario))

        # ── Carattere normale ───────────────────────────────────────────────
        elif ch.isprintable():
            query += ch
            clear_block(n)
            n = print_block(build_lines(query, glossario))


# ── Menu ───────────────────────────────────────────────────────────────────────

def mostra_tutti(glossario):
    if not glossario:
        print("\n  Il glossario è vuoto.")
        return
    print(f"\n  {'─' * 45}")
    print(f"  {'ACRONIMO':<12} SIGNIFICATO")
    print(f"  {'─' * 45}")
    for acronimo in sorted(glossario):
        print(f"  {acronimo:<12} {glossario[acronimo]}")
    print(f"  {'─' * 45}")
    print(f"  {len(glossario)} acronimo/i.\n")


def menu():
    print("\n╔══════════════════════════════╗")
    print("║      GLOSSARIO ACRONIMI      ║")
    print("╠══════════════════════════════╣")
    print("║  [1] Cerca / Inserisci       ║")
    print("║  [2] Mostra tutti            ║")
    print("║  [0] Esci                    ║")
    print("╚══════════════════════════════╝")


def main():
    glossario = carica_glossario()

    while True:
        menu()
        scelta = input("  Scelta: ").strip()

        if scelta == '1':
            modifiche = []
            modifiche = fuzzy_finder(glossario, modifiche)
            if modifiche:
                git_commit_push(modifiche)

        elif scelta == '2':
            mostra_tutti(glossario)

        elif scelta == '0':
            print("\n  Arrivederci! 👋\n")
            break

        else:
            print("  ⚠  Scelta non valida.")


if __name__ == "__main__":
    main()