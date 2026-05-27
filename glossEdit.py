"""
Glossario Acronimi - v4
- Fuzzy finder in tempo reale
- Push unico al ritorno al menu
- Descrizione lunga per ogni acronimo
- Retrocompatibilità col vecchio formato
- glossario.txt sempre nella cartella dello script

Formato file:
ACRONIMO|significato|descrizione

Compatibile anche con:
ACRONIMO = significato
"""

import msvcrt
import os
import sys
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
GLOSSARIO_FILE = SCRIPT_DIR / "glossario.txt"
MAX_RESULTS = 8

# Abilita ANSI su Windows
os.system('')


# ── Git ────────────────────────────────────────────────────────────────────────

def git_commit_push(modifiche: list):
    """Commit + push con messaggio adattato."""

    if not modifiche:
        return

    if len(modifiche) == 1:
        tipo, acronimo, dettaglio = modifiche[0]

        if tipo == 'aggiunta':
            msg = f"Aggiunta acronimo '{acronimo}'"

        elif tipo == 'modifica':
            msg = f"Modifica '{acronimo}': {dettaglio}"

        else:
            msg = f"Eliminazione acronimo '{acronimo}'"

    else:
        n_a = sum(1 for t, _, _ in modifiche if t == 'aggiunta')
        n_m = sum(1 for t, _, _ in modifiche if t == 'modifica')
        n_e = sum(1 for t, _, _ in modifiche if t == 'eliminazione')

        parti = []

        if n_a:
            parti.append(f"{n_a} aggiunta/e")

        if n_m:
            parti.append(f"{n_m} modifica/he")

        if n_e:
            parti.append(f"{n_e} eliminazione/i")

        msg = "Glossario: " + ", ".join(parti)

    try:
        subprocess.run(
            ["git", "add", str(GLOSSARIO_FILE)],
            cwd=SCRIPT_DIR,
            check=True,
            capture_output=True
        )

        subprocess.run(
            ["git", "commit", "-m", msg],
            cwd=SCRIPT_DIR,
            check=True,
            capture_output=True
        )

        subprocess.run(
            ["git", "push"],
            cwd=SCRIPT_DIR,
            check=True,
            capture_output=True
        )

        print(f"\n  ↑ Push completato: {msg}")

    except subprocess.CalledProcessError as e:
        print(f"\n  ⚠ Errore git: {e}")


# ── I/O glossario ──────────────────────────────────────────────────────────────

def carica_glossario():
    """
    Formato nuovo:
    ACRONIMO|significato|descrizione

    Formato vecchio:
    ACRONIMO = significato
    """

    glossario = {}

    try:
        with open(GLOSSARIO_FILE, "r", encoding="utf-8") as f:

            for riga in f:
                riga = riga.rstrip("\n")

                if not riga.strip():
                    continue

                # ── Nuovo formato ────────────────────────────────────────
                if "|" in riga:

                    parti = riga.split("|", 2)

                    acronimo = parti[0].strip().upper()

                    significato = (
                        parti[1].strip()
                        if len(parti) > 1
                        else ""
                    )

                    descrizione = (
                        parti[2].replace("\\n", "\n").strip()
                        if len(parti) > 2
                        else ""
                    )

                    glossario[acronimo] = {
                        "significato": significato,
                        "descrizione": descrizione
                    }

                # ── Vecchio formato ──────────────────────────────────────
                elif " = " in riga:

                    acronimo, significato = riga.split(" = ", 1)

                    glossario[acronimo.strip().upper()] = {
                        "significato": significato.strip(),
                        "descrizione": ""
                    }

    except FileNotFoundError:
        pass

    return glossario


def salva_glossario(glossario):

    with open(GLOSSARIO_FILE, "w", encoding="utf-8") as f:

        for acronimo in sorted(glossario):

            dato = glossario[acronimo]

            significato = dato.get("significato", "").strip()

            descrizione = (
                dato.get("descrizione", "")
                .replace("\n", "\\n")
                .strip()
            )

            f.write(
                f"{acronimo}|{significato}|{descrizione}\n"
            )


# ── Finder rendering ───────────────────────────────────────────────────────────

def build_lines(query: str, glossario: dict) -> list[str]:

    q = query.upper()

    matches = sorted(
        k for k in glossario
        if q in k
    )

    lines = [
        f"  Cerca: {query}\u258c",
        f"  {'─' * 55}",
    ]

    if matches:

        for k in matches[:MAX_RESULTS]:

            marker = "\u25b6 " if k == q else "  "

            significato = glossario[k]["significato"]

            lines.append(
                f"  {marker}{k:<12} {significato}"
            )

        if len(matches) > MAX_RESULTS:
            lines.append(
                f"  ... e altri {len(matches) - MAX_RESULTS}"
            )

    elif query:

        lines.append(
            f"  (nessun risultato — Invio per aggiungere '{q}')"
        )

    else:
        lines.append("  (digita per cercare)")

    while len(lines) < MAX_RESULTS + 2:
        lines.append("")

    lines += [
        f"  {'─' * 55}",
        "  [Invio] conferma   [Esc] torna al menu",
    ]

    return lines


def print_block(lines: list[str]) -> int:

    sys.stdout.write('\n'.join(lines))
    sys.stdout.flush()

    return len(lines)


def clear_block(n: int):

    sys.stdout.write(f'\r\033[{n - 1}A\033[J')
    sys.stdout.flush()


# ── Input ──────────────────────────────────────────────────────────────────────

def read_key():

    ch = msvcrt.getwch()

    if ch in ('\x00', '\xe0'):
        msvcrt.getwch()
        return None

    return ch


# ── Util ───────────────────────────────────────────────────────────────────────

def stampa_descrizione(descrizione: str):

    if not descrizione.strip():
        print("  (nessuna descrizione)")
        return

    print("  Descrizione:")
    print("  ─────────────────────────────────────────")

    for riga in descrizione.splitlines():
        print(f"  {riga}")

    print("  ─────────────────────────────────────────")


def input_multiline(prompt=""):
    """
    Input multilinea.
    Fine input = riga vuota.
    """

    print(prompt)
    print("  (Invio su riga vuota per terminare)\n")

    righe = []

    while True:

        riga = input()

        if riga == "":
            break

        righe.append(riga)

    return "\n".join(righe).strip()


# ── Finder ─────────────────────────────────────────────────────────────────────

def fuzzy_finder(glossario: dict, modifiche: list):

    query = ""

    print()

    n = print_block(
        build_lines(query, glossario)
    )

    while True:

        ch = read_key()

        if ch is None:
            continue

        # ── ESC ──────────────────────────────────────────────────────────
        if ch == '\x1b':

            clear_block(n)

            return modifiche

        # ── INVIO ────────────────────────────────────────────────────────
        elif ch == '\r':

            acronimo = query.strip().upper()

            if not acronimo:
                continue

            clear_block(n)

            # ── Esistente ───────────────────────────────────────────────
            if acronimo in glossario:

                dato = glossario[acronimo]

                print(f"\n  ✔ '{acronimo}'")
                print(f"  Significato: {dato['significato']}\n")

                stampa_descrizione(
                    dato["descrizione"]
                )

                print("\n  [M] Modifica significato")
                print("  [D] Modifica descrizione")
                print("  [E] Elimina")
                print("  [Invio] Niente")

                scelta = input("\n  > ").strip().upper()

                # ── Modifica significato ───────────────────────────────
                if scelta == 'M':

                    nuovo = input(
                        f"\n  Nuovo significato per '{acronimo}': "
                    ).strip()

                    if nuovo:

                        vecchio = dato["significato"]

                        glossario[acronimo]["significato"] = nuovo

                        salva_glossario(glossario)

                        modifiche.append((
                            'modifica',
                            acronimo,
                            f"significato aggiornato"
                        ))

                        print(f"\n  ✔ Significato aggiornato.")
                        print(f"  Vecchio: {vecchio}")
                        print(f"  Nuovo:   {nuovo}")

                    else:
                        print("\n  ⚠ Campo vuoto.")

                # ── Modifica descrizione ───────────────────────────────
                elif scelta == 'D':

                    print("\n  Descrizione attuale:\n")

                    stampa_descrizione(
                        dato["descrizione"]
                    )

                    nuova_descrizione = input_multiline(
                        "\n  Nuova descrizione:"
                    )

                    glossario[acronimo]["descrizione"] = (
                        nuova_descrizione
                    )

                    salva_glossario(glossario)

                    modifiche.append((
                        'modifica',
                        acronimo,
                        'descrizione aggiornata'
                    ))

                    print("\n  ✔ Descrizione aggiornata.")

                # ── Elimina ────────────────────────────────────────────
                elif scelta == 'E':

                    conf = input(
                        f"\n  Eliminare '{acronimo}'? [s/N] "
                    ).strip().lower()

                    if conf == 's':

                        del glossario[acronimo]

                        salva_glossario(glossario)

                        modifiche.append((
                            'eliminazione',
                            acronimo,
                            ''
                        ))

                        print(f"\n  ✔ '{acronimo}' eliminato.")

                    else:
                        print("\n  ↩ Annullato.")

            # ── Nuovo acronimo ──────────────────────────────────────────
            else:

                print(f"\n  '{acronimo}' non è nel glossario.\n")

                significato = input(
                    f"  Significato di '{acronimo}': "
                ).strip()

                if significato:

                    descrizione = input_multiline(
                        "\n  Descrizione dettagliata (opzionale):"
                    )

                    glossario[acronimo] = {
                        "significato": significato,
                        "descrizione": descrizione
                    }

                    salva_glossario(glossario)

                    modifiche.append((
                        'aggiunta',
                        acronimo,
                        significato
                    ))

                    print(f"\n  ✔ '{acronimo}' salvato.")

                else:
                    print("\n  ⚠ Campo vuoto.")

            input(
                "\n  Premi Invio per una nuova ricerca..."
            )

            query = ""

            print()

            n = print_block(
                build_lines(query, glossario)
            )

        # ── Backspace ───────────────────────────────────────────────────
        elif ch == '\x08':

            if query:

                query = query[:-1]

                clear_block(n)

                n = print_block(
                    build_lines(query, glossario)
                )

        # ── Carattere normale ───────────────────────────────────────────
        elif ch.isprintable():

            query += ch

            clear_block(n)

            n = print_block(
                build_lines(query, glossario)
            )


# ── Menu ───────────────────────────────────────────────────────────────────────

def mostra_tutti(glossario):

    if not glossario:

        print("\n  Il glossario è vuoto.")

        return

    print(f"\n  {'─' * 60}")
    print(f"  {'ACRONIMO':<12} SIGNIFICATO")
    print(f"  {'─' * 60}")

    for acronimo in sorted(glossario):

        significato = glossario[acronimo]["significato"]

        print(f"  {acronimo:<12} {significato}")

    print(f"  {'─' * 60}")
    print(f"  {len(glossario)} acronimo/i.\n")


def menu():

    print("\n╔════════════════════════════════╗")
    print("║      GLOSSARIO ACRONIMI        ║")
    print("╠════════════════════════════════╣")
    print("║  [1] Cerca / Inserisci         ║")
    print("║  [2] Mostra tutti              ║")
    print("║  [0] Esci                      ║")
    print("╚════════════════════════════════╝")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():

    glossario = carica_glossario()

    while True:

        menu()

        scelta = input("  Scelta: ").strip()

        if scelta == '1':

            modifiche = []

            modifiche = fuzzy_finder(
                glossario,
                modifiche
            )

            if modifiche:
                git_commit_push(modifiche)

        elif scelta == '2':

            mostra_tutti(glossario)

        elif scelta == '0':

            print("\n  Arrivederci! 👋\n")

            break

        else:

            print("  ⚠ Scelta non valida.")


if __name__ == "__main__":
    main()