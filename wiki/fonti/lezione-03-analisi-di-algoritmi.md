---
tipo: fonte
titolo: "Corso di Algoritmi e Strutture Dati — Analisi di correttezza e di complessità degli algoritmi"
file_raw: "03-Analisi di algoritmi.pdf"
pagine: "1-34"
data_ingest: 2026-09-26
formato: slide-pdf
argomenti: [paradigmi di progettazione, iterazione e ricorsione, correttezza, controesempi, invariante di ciclo, induzione, analisi di complessità, ricorrenze]
---

# Lezione 03 — Analisi di correttezza e di complessità (03-Analisi di algoritmi.pdf)

## Sommario

La lezione ha quattro parti. **Classificazione dei problemi**: tre famiglie di approcci (divide et impera, ricerca combinatoria, metodi euristici) che bilanciano tempo, qualità e scalabilità. **Caratterizzazione degli algoritmi**: iterazione contro ricorsione, con l'esempio della somma dei primi $n$ numeri in entrambe le forme. **Correttezza**: controesempi e testing per dimostrare l'incorrettezza (con cinque suggerimenti pratici), invariante di ciclo per gli algoritmi iterativi, induzione per quelli ricorsivi, applicati alla somma. **Analisi di complessità**: il costo riga per riga della somma iterativa ($2n + 4 = O(n)$) e la ricorrenza $T(n) = T(n-1) + c$ della somma ricorsiva ($1 + cn = O(n)$), con la domanda aperta sulla complessità spaziale.

## Punti chiave

1. Tre famiglie di progettazione ([[03-Analisi di algoritmi.pdf#page=3]]–[[03-Analisi di algoritmi.pdf#page=6]]) → [[paradigmi-di-progettazione]], [[divide-et-impera]], [[ricerca-combinatoria]], [[metodi-euristici]].
2. Iterazione contro ricorsione: stesso potere espressivo, costi e chiarezza diversi ([[03-Analisi di algoritmi.pdf#page=8]], [[03-Analisi di algoritmi.pdf#page=9]]) → [[iterazione-e-ricorsione]].
3. Esempio: somma di $1..n$ iterativa e ricorsiva ([[03-Analisi di algoritmi.pdf#page=10]], [[03-Analisi di algoritmi.pdf#page=11]]) → [[somma-iterativa]], [[somma-ricorsiva]].
4. Incorrettezza: controesempi, testing, tips (think small, think exhaustively, hunt for the weakness, go for a tie, seek extremes); nessun controesempio ≠ correttezza ([[03-Analisi di algoritmi.pdf#page=13]]–[[03-Analisi di algoritmi.pdf#page=15]]) → [[ricerca-di-controesempi]].
5. Invariante di ciclo: inizializzazione, conservazione, conclusione + terminazione con funzione variante ([[03-Analisi di algoritmi.pdf#page=16]], [[03-Analisi di algoritmi.pdf#page=17]]) → [[invariante-di-ciclo]].
6. Ricorsione: specifiche, misura ben fondata, casi base, passo induttivo, terminazione ([[03-Analisi di algoritmi.pdf#page=18]], [[03-Analisi di algoritmi.pdf#page=19]]) → [[correttezza-per-induzione]].
7. Analisi: risorse, modello, dimensione dell'input, costo riga × esecuzioni ([[03-Analisi di algoritmi.pdf#page=21]], [[03-Analisi di algoritmi.pdf#page=22]]) → [[tempo-di-esecuzione]], [[modello-ram]].
8. Somma iterativa: $1 + 1 + (n+1) + n + 1 = 2n + 4 = O(n)$ ([[03-Analisi di algoritmi.pdf#page=23]]–[[03-Analisi di algoritmi.pdf#page=29]]) → [[analisi-del-costo-riga-per-riga]].
9. Somma ricorsiva: $T(0) = 1$, $T(i) = T(i-1) + c$, $T(n) = 1 + cn = O(n)$ ([[03-Analisi di algoritmi.pdf#page=30]]–[[03-Analisi di algoritmi.pdf#page=34]]) → [[equazioni-di-ricorrenza]], [[risoluzione-ricorrenze]].

## Refusi e note

- p. 5: il punto «Spesso efficienti se la partizione è bilanciata» nella ricerca combinatoria sembra copiato dalla slide su divide et impera (p. 4) e contrasta con «complessità tipicamente esponenziale».
- p. 17: «Inizializzazione: $i = 0$» → dovrebbe essere $i = 1$ (il ciclo parte da 1).
- pp. 29 e 34: «E la complessità spaziale?» senza risposta → nel wiki: $\Theta(1)$ iterativa, $\Theta(n)$ ricorsiva (🧩).
- p. 28: il risultato è dato come $O(n)$; vale anche $\Theta(n)$.
- Pseudocodice in italiano (`funzione`, `per … da … a`, `ritorna`), diverso dalle convenzioni di a1.
- Pagina del titolo: [[03-Analisi di algoritmi.pdf#page=1|1]]; pagine di intestazione: [[03-Analisi di algoritmi.pdf#page=2|2]], [[03-Analisi di algoritmi.pdf#page=7|7]], [[03-Analisi di algoritmi.pdf#page=12|12]], [[03-Analisi di algoritmi.pdf#page=20|20]].

## Concetti introdotti

[[paradigmi-di-progettazione]], [[divide-et-impera]], [[ricerca-combinatoria]], [[metodi-euristici]], [[iterazione-e-ricorsione]], [[ricerca-di-controesempi]], [[invariante-di-ciclo]], [[correttezza-per-induzione]], [[tempo-di-esecuzione]], [[equazioni-di-ricorrenza]], [[somma-iterativa]], [[somma-ricorsiva]]

## Domande aperte

- Complessità spaziale: la risposta attesa dal docente è quella della profondità della ricorsione?
- Gli esempi concreti di divide et impera arriveranno nelle prossime lezioni.

## Domande da esame

- Confronta divide et impera, ricerca combinatoria ed euristiche (garanzie, costo, quando usarle).
- Pro e contro di iterazione e ricorsione.
- Come si dimostra l'incorrettezza di un algoritmo? Elenca i tips per trovare controesempi.
- Enuncia i passi di una prova con invariante di ciclo e applicali a `somma_iterativa`.
- Dimostra per induzione la correttezza di `somma_ricorsiva`.
- Calcola il costo di `somma_iterativa` riga per riga e risolvi la ricorrenza di `somma_ricorsiva`; confronta anche lo spazio.

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_
