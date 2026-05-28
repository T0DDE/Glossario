# Glossario Acronimi

Glossario interattivo per la gestione di acronimi tecnici tramite terminale Python.

Il progetto permette di:

* cercare acronimi in tempo reale
* aggiungere nuove voci
* modificare significati e descrizioni
* eliminare acronimi
* mantenere il glossario in un file Markdown leggibile
* effettuare commit e push automatici tramite Git

---

# Struttura del progetto

```text
.
├── glossario.py
├── glossario.md
└── README.md
```

---

# Formato del glossario

Il glossario è salvato nel file:

```text
glossario.md
```

Il file è completamente leggibile anche senza eseguire il programma Python.

Esempio:

```md
## TSO
**Significato:** Transmission System Operator

Il gestore del sistema di trasmissione dell'energia elettrica o del gas.

---
```

---

# Funzionalità principali

## Ricerca realtime

Durante la digitazione il finder aggiorna automaticamente i risultati.

Esempio:

```text
Cerca: TS▌

▶ TSO          Transmission System Operator
```

---

## Inserimento rapido

Se un acronimo non esiste:

1. premi Invio
2. inserisci il significato
3. inserisci una descrizione opzionale multilinea

---

## Descrizioni multilinea

Ogni acronimo può avere:

* significato breve
* descrizione dettagliata multilinea

La descrizione viene mostrata automaticamente quando l'acronimo viene selezionato.

---

## Indice automatico

Il programma genera automaticamente un indice Markdown cliccabile:

```md
## Indice

- [TSO](#tso)
- [RAM](#ram)
```

Compatibile con:

* GitHub
* GitLab
* editor Markdown

---

## Commit e push automatici

Quando si torna al menu principale:

* il file viene salvato
* viene eseguito:

  * `git add`
  * `git commit`
  * `git push`

Il messaggio commit viene generato automaticamente.

Esempi:

```text
Aggiunta acronimo 'TSO'
```

oppure:

```text
Glossario: 2 aggiunta/e, 1 modifica/he
```

---

# Requisiti

* Python 3.10+
* Git installato
* Windows terminal / PowerShell / CMD

Il progetto usa:

```python
msvcrt
```

quindi è attualmente pensato per Windows.

---

# Come usare il programma

## Avvio

Da terminale:

```bash
python glossario.py
```

---

## Menu principale

```text
[1] Cerca / Inserisci
[2] Mostra tutti
[0] Esci
```

---

## Ricerca

Scrivi un acronimo nel finder.

* Invio → seleziona
* Esc → torna al menu

---

## Modifica voce

Quando un acronimo esiste:

```text
[M] Modifica significato
[D] Modifica descrizione
[E] Elimina
```

---

# Tutorial rapido per collaboratori GitHub

## 1. Clonare la repository

```bash
git clone <URL_REPOSITORY>
```

Entrare nella cartella:

```bash
cd <NOME_CARTELLA>
```

---

## 2. Eseguire il programma

```bash
python glossario.py
```

oppure:

```bash
py glossario.py
```

su Windows.

---

## 3. Modificare il glossario

Usare normalmente il programma.

Le modifiche vengono salvate automaticamente in:

```text
glossario.md
```

---

## 4. Push automatico

Quando si esce dal finder tornando al menu principale:

* il programma crea automaticamente il commit
* esegue automaticamente il push

Non è necessario usare Git manualmente.

---

# Modifica manuale del file Markdown

È possibile modificare direttamente:

```text
glossario.md
```

Mantenendo il formato:

```md
## ACRONIMO
**Significato:** Testo

Descrizione multilinea.

---
```

L'indice verrà rigenerato automaticamente dal programma.

---

# Possibili sviluppi futuri

* categorie/tag
* ricerca full-text anche nelle descrizioni
* esportazione HTML/PDF
* supporto Linux/macOS
* ordinamento per categoria
* colori ANSI avanzati
* preview descrizione nel finder
* fuzzy matching avanzato

---

# Licenza

Uso interno / personale.
