---
tipo: fonte
titolo: "Lecture 4: Elementary Data Structures (Skiena, integrata dal Prof. Marrone)"
file_raw: "04-Strutture dati elementari.pdf"
pagine: "1-30"
data_ingest: 2026-09-26
formato: slide-pdf
argomenti: [astrazione dei dati, strutture contigue e collegate, array, array dinamici, puntatori, liste concatenate, pile, code]
---

# Lezione 04 — Strutture dati elementari (04-Strutture dati elementari.pdf)

## Sommario

Slide di Skiena con integrazioni del Prof. Marrone (costi $\Theta$ in italiano sotto ai codici). Una struttura dati si descrive con le **operazioni astratte** e con la loro **implementazione**, e le implementazioni si dividono in **contigue** (array) e **collegate** (puntatori). Gli **array** danno accesso costante e località, ma hanno dimensione fissa. Gli **array dinamici** la superano raddoppiando la capacità: il costo totale delle copie resta $O(n)$ grazie alla serie geometrica. Le **liste concatenate** sono presentate con codice C per inserimento, ricerca e cancellazione, con i loro casi migliore e peggiore, i vantaggi rispetto agli array e la variante doppia. Chiudono **pile** (LIFO) e **code** (FIFO), con le figure 10.1 e 10.2 del Cormen, l'osservazione che tutte le operazioni costano $O(1)$ e il legame con DFS/BFS.

## Percorso della lezione · [[04-Strutture dati elementari.pdf|04-Strutture dati elementari.pdf]]

**PDF:** (pp. 1–30)

Pagine del wiki nell'ordine di prima comparsa nelle slide (è l'ordine delle pagine di questa lezione nel libro, dopo questa):
1. [[tipo-di-dato-astratto]] — pp. 2–4 · operazioni astratte contro implementazione
2. [[strutture-contigue-e-collegate]] — p. 5 (poi pp. 15, 21) · array contro puntatori, vantaggi delle liste
3. [[array]] — pp. 7–9
4. [[array-dinamico]] — pp. 10–12 · raddoppio, $M \le 2n$, «no free lunch»
5. [[lista-concatenata]] — pp. 14–22 · codice C, costi, liste doppie
6. [[pila]] — pp. 24–26, 28–29 · LIFO, Figura 10.1, DFS
7. [[coda]] — pp. 25, 27–29 · FIFO, Figura 10.2, BFS
8. [[tracce-pila-e-coda]] — esercizio sulle Figure 10.1 e 10.2

**Ordine consigliato.**
*strutture-contigue-e-collegate* compare a p. 5 ma la sua tabella di confronto usa anche le liste (pp. 15, 21): leggila **dopo** *lista-concatenata*. Ordine: *tipo-di-dato-astratto* → *array* → *array-dinamico* → *lista-concatenata* → *strutture-contigue-e-collegate* → *pila* → *coda* → *tracce-pila-e-coda*.

## Punti chiave · [[04-Strutture dati elementari.pdf#page=3|p. 3]]–[[04-Strutture dati elementari.pdf#page=5|5]], [[04-Strutture dati elementari.pdf#page=8|p. 8]]–[[04-Strutture dati elementari.pdf#page=10|10]], [[04-Strutture dati elementari.pdf#page=12|p. 12]], [[04-Strutture dati elementari.pdf#page=15|p. 15]], [[04-Strutture dati elementari.pdf#page=16|16]], [[04-Strutture dati elementari.pdf#page=20|p. 20]]–[[04-Strutture dati elementari.pdf#page=22|22]], [[04-Strutture dati elementari.pdf#page=25|p. 25]], [[04-Strutture dati elementari.pdf#page=29|p. 29]]

1. Strutture elementari come componenti «off-the-shelf»; operazioni astratte contro implementazione; Push/Pop → [[tipo-di-dato-astratto]].
2. Contigue (array, matrici, heap, hash table) contro collegate (liste, alberi, liste di adiacenza) → [[strutture-contigue-e-collegate]].
3. Array: accesso costante, niente spazio sprecato, località per la cache → [[array]].
4. Array dinamici: $\lceil\log_2 n\rceil$ raddoppi, $M \le 2n$ spostamenti, «free lunch» della serie geometrica; nota sul teorema no free lunch → [[array-dinamico]].
5. Puntatori, `*p`, `&x`, `NULL`.
6. Liste: struttura C, `insert_list` $\Theta(1)$, `search_list` e `item_ahead` $\Theta(1)$/$\Theta(n)$, `delete_list` $\Theta(1)$/$\Theta(n)$ → [[lista-concatenata]].
7. Vantaggi delle liste sugli array statici; liste doppie a costo big-Oh nullo.
8. Pila (LIFO) e coda (FIFO); implementazioni su array (Figure 10.1, 10.2); tutte le operazioni $O(1)$; DFS contro BFS → [[pila]], [[coda]], [[tracce-pila-e-coda]].

## Refusi e note · [[04-Strutture dati elementari.pdf#page=1|p. 1]], [[04-Strutture dati elementari.pdf#page=2|2]], [[04-Strutture dati elementari.pdf#page=6|p. 6]], [[04-Strutture dati elementari.pdf#page=7|7]], [[04-Strutture dati elementari.pdf#page=13|p. 13]], [[04-Strutture dati elementari.pdf#page=14|14]], [[04-Strutture dati elementari.pdf#page=23|p. 23]], [[04-Strutture dati elementari.pdf#page=24|24]], [[04-Strutture dati elementari.pdf#page=30|p. 30]]

- p. 20: con l'`item_ahead` di p. 19 cancellare la **testa** costa $\Theta(n)$, non $\Theta(1)$ come suggerisce «cancelli la testa» (🧩, dettagli in [[lista-concatenata]]); inoltre `delete_list` presuppone che il nodo sia nella lista.
- p. 4: «difference circumstances» → *different*.
- p. 11: la formula $\sum i\cdot n/2^i$ è un conteggio approssimato; il conteggio esatto $2^{\lceil \lg n\rceil} - 1 < 2n$ dà lo stesso limite (🧩).
- p. 12 (teorema NFL) è una nota a margine, non un argomento del corso.
- Pagina del titolo: p. 1; pagine di intestazione o «Questions?»: p. 2, p. 6, p. 7, p. 13, p. 14, p. 23, p. 24, p. 30.

## Concetti introdotti

[[tipo-di-dato-astratto]], [[strutture-contigue-e-collegate]], [[array]], [[array-dinamico]], [[lista-concatenata]], [[pila]], [[coda]]

## Domande aperte

- Heap e tabelle hash sono solo citate (p. 3, p. 5): saranno trattate più avanti.
- DFS e BFS (p. 29) arriveranno con i grafi.

## Domande da esame

- Differenza tra operazioni astratte e implementazione; esempio.
- Strutture contigue contro collegate: esempi, vantaggi e svantaggi.
- Perché l'array dinamico costa $O(n)$ in totale? Derivare $M \le 2n$.
- Costo di inserimento, ricerca e cancellazione in una lista (casi migliore e peggiore); cosa cambia con una lista doppia.
- Implementare pila e coda su array; eseguire una traccia di PUSH/POP ed ENQUEUE/DEQUEUE.

_Aggiornato: 2026-09-26 — ingest 04-Strutture dati elementari.pdf_
_Aggiornato: 2026-10-28 — aggiunto il «Percorso della lezione» (spostato dall'indice lezioni.md)_

<!-- nav:inizio -->
---
**Lezione 04 · pagina 1 di 9** · ← [[risoluzione-ricorrenze|Scrivere e risolvere equazioni di ricorrenza]] · [[lezioni|Indice]] · [[tipo-di-dato-astratto|Astrazione dei dati (operazioni astratte vs implementazione)]] →
<!-- nav:fine -->
