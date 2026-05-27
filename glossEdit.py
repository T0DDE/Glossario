"""
Glossario Acronimi
Salva, cerca, modifica ed elimina acronimi nel file glossario.txt
"""

GLOSSARIO_FILE = "glossario.txt"


def carica_glossario():
    """Legge il file e restituisce un dizionario {ACRONIMO: significato}."""
    glossario = {}
    try:
        with open(GLOSSARIO_FILE, "r", encoding="utf-8") as f:
            for riga in f:
                riga = riga.strip()
                if " = " in riga:
                    acronimo, significato = riga.split(" = ", 1)
                    glossario[acronimo.strip().upper()] = significato.strip()
    except FileNotFoundError:
        pass  # Il file verrà creato al primo salvataggio
    return glossario


def salva_glossario(glossario):
    """Scrive il dizionario nel file, ordinato alfabeticamente."""
    with open(GLOSSARIO_FILE, "w", encoding="utf-8") as f:
        for acronimo in sorted(glossario):
            f.write(f"{acronimo} = {glossario[acronimo]}\n")


def cerca_acronimo(glossario, acronimo):
    """Cerca un acronimo e gestisce inserimento, modifica ed eliminazione."""
    acronimo = acronimo.strip().upper()

    if not acronimo:
        print("  ⚠  Acronimo non valido.")
        return glossario

    if acronimo in glossario:
        # — Acronimo già presente —
        print(f"\n  ✔  '{acronimo}' = {glossario[acronimo]}")
        print("\n  Cosa vuoi fare?")
        print("  [M] Modifica   [E] Elimina   [Invio] Niente")
        scelta = input("  > ").strip().upper()

        if scelta == "M":
            nuovo = input(f"  Nuovo significato per '{acronimo}': ").strip()
            if nuovo:
                glossario[acronimo] = nuovo
                salva_glossario(glossario)
                print(f"  ✔  '{acronimo}' aggiornato.")
            else:
                print("  ⚠  Nessuna modifica effettuata (campo vuoto).")

        elif scelta == "E":
            conferma = input(f"  Sei sicuro di voler eliminare '{acronimo}'? [s/N] ").strip().lower()
            if conferma == "s":
                del glossario[acronimo]
                salva_glossario(glossario)
                print(f"  ✔  '{acronimo}' eliminato.")
            else:
                print("  ↩  Eliminazione annullata.")

    else:
        # — Acronimo nuovo —
        print(f"\n  '{acronimo}' non è nel glossario.")
        significato = input(f"  Per cosa sta '{acronimo}'? ").strip()
        if significato:
            glossario[acronimo] = significato
            salva_glossario(glossario)
            print(f"  ✔  '{acronimo}' salvato.")
        else:
            print("  ⚠  Nessun significato inserito, acronimo non salvato.")

    return glossario


def mostra_tutti(glossario):
    """Stampa tutti gli acronimi salvati."""
    if not glossario:
        print("\n  Il glossario è vuoto.")
        return
    print(f"\n  {'─'*40}")
    print(f"  {'ACRONIMO':<12} SIGNIFICATO")
    print(f"  {'─'*40}")
    for acronimo in sorted(glossario):
        print(f"  {acronimo:<12} {glossario[acronimo]}")
    print(f"  {'─'*40}")
    print(f"  {len(glossario)} acronimo/i trovato/i.\n")


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

        if scelta == "1":
            acronimo = input("\n  Inserisci l'acronimo: ").strip()
            glossario = cerca_acronimo(glossario, acronimo)

        elif scelta == "2":
            mostra_tutti(glossario)

        elif scelta == "0":
            print("\n  Arrivederci! 👋\n")
            break

        else:
            print("  ⚠  Scelta non valida.")


if __name__ == "__main__":
    main()