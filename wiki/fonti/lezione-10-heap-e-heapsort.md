---
tipo: fonte
titolo: "Corso di Algoritmi e Strutture Dati — Heapsort"
file_raw: "10 - Heap - Heapsort.pdf"
pagine: "1-50"
data_ingest: 2026-11-26
formato: slide-pdf
argomenti: [heap, max-heapify, build-max-heap, heapsort, code di priorità]
---

# Lezione 10 — Heapsort (10 - Heap - Heapsort.pdf)

## Sommario · [[10 - Heap - Heapsort.pdf#page=1|p. 1]], [[10 - Heap - Heapsort.pdf#page=2|2]]

Slide del Prof. Marrone, a.a. 26/27. La lezione parte dai limiti dei due ordinamenti già visti (insertion sort: $\Theta(n^2)$ ma sul posto; merge sort: $\Theta(n \lg n)$ ma non sul posto) per introdurre **Heap-Sort**, $O(n \lg n)$ e sul posto, basato sulla struttura dati **heap**. Segue la definizione di heap (albero binario quasi completo, rappresentato da un array con $\text{Parent}(i) = \lfloor i/2 \rfloor$, $\text{Left}(i) = 2i$, $\text{Right}(i) = 2i+1$) e le proprietà di max-heap e min-heap, poi gli algoritmi: **Max-Heapify** (con l'analisi $T(n) \le T(2n/3) + \Theta(1) = O(\lg n)$), **Build-Max-Heap** (con invariante e analisi stretta $O(n)$), **Heap-Sort** (con un esempio di 18 fotogrammi, $O(n \lg n)$) e le operazioni della **coda a priorità** realizzata con un heap: Maximum, Extract-Max, Increase-Key e Insert. L'ultima slide propone un esercizio, «Heap-Sort – da zero».

## Percorso della lezione

Pagine del wiki nell'ordine di prima comparsa nelle slide (è l'ordine delle pagine di questa lezione nel libro):
1. [[heap]] — pp. 3–6: definizione, rappresentazione con array, max-heap e min-heap
2. [[max-heapify]] — pp. 7–14: ripristino della proprietà in un nodo, costo $O(\lg n)$
3. [[build-max-heap]] — pp. 14–21: costruzione da un array arbitrario, invariante, costo $O(n)$
4. [[heapsort]] — pp. 2, 22–41, 50: l'algoritmo, l'esempio e il costo $O(n \lg n)$
5. [[heap-extract-max]] — pp. 42–44: Heap-Maximum e Heap-Extract-Max
6. [[heap-increase-key]] — pp. 45–48: risalita della chiave
7. [[max-heap-insert]] — p. 49: inserimento
8. [[tracce-su-heap]] — p. 50: esercizio «Heap-Sort – da zero», svolto

Già lette, riprese in questa lezione: *insertion-sort* e *merge-sort* (confronto di p. 2), *coda-di-priorita* (p. 42, nuova sezione «Realizzazione con un heap»), *teorema-dell-esperto* (caso 2 per Max-Heapify), *invariante-di-ciclo* (Build-Max-Heap), *albero* (altezza e forma), *array*, *ordinamento*.

**Ordine consigliato.** Le slide cominciano da Heap-Sort (p. 2) ma ne danno l'algoritmo solo a p. 22; conviene leggere nell'ordine delle pagine del libro, che mette *heap*, *max-heapify* e *build-max-heap* prima di *heapsort*.

## Punti chiave · [[10 - Heap - Heapsort.pdf#page=2|p. 2]]–[[10 - Heap - Heapsort.pdf#page=6|6]], [[10 - Heap - Heapsort.pdf#page=11|p. 11]]–[[10 - Heap - Heapsort.pdf#page=14|14]], [[10 - Heap - Heapsort.pdf#page=20|p. 20]], [[10 - Heap - Heapsort.pdf#page=21|21]], [[10 - Heap - Heapsort.pdf#page=41|p. 41]]–[[10 - Heap - Heapsort.pdf#page=44|44]], [[10 - Heap - Heapsort.pdf#page=48|p. 48]], [[10 - Heap - Heapsort.pdf#page=49|49]]

1. Heap-Sort: $O(n \lg n)$ e sul posto, basato sulla struttura dati heap → [[heapsort]].
2. Un heap è un albero binario quasi completo rappresentato da un array; $\text{Parent}(i) = \lfloor i/2 \rfloor$, $\text{Left}(i) = 2i$, $\text{Right}(i) = 2i+1$; max-heap: $A[i] \le A[\text{Parent}(i)]$ → [[heap]].
3. Max-Heapify assume che i sottoalberi di $\text{Left}(i)$ e $\text{Right}(i)$ siano max-heap e fa «scendere» $A[i]$; il sottoproblema ha dimensione al più $2n/3$, quindi $T(n) \le T(2n/3) + \Theta(1)$, caso 2 del teorema dell'esperto, $O(\lg n)$ → [[max-heapify]].
4. Build-Max-Heap chiama Max-Heapify sui nodi interni dal basso verso l'alto; invariante «i nodi $i+1, \dots, n$ sono radici di max-heap»; il limite $O(n \lg n)$ non è stretto, quello stretto è $O(n)$ perché un heap ha al più $\lceil n/2^{h+1} \rceil$ nodi di altezza $h$ → [[build-max-heap]].
5. Heap-Sort: Build-Max-Heap, poi $n-1$ volte scambio del massimo con l'ultimo, riduzione dell'heap e Max-Heapify → [[heapsort]].
6. Una coda a priorità si realizza con un heap: Heap-Maximum $\Theta(1)$; Heap-Extract-Max, Heap-Increase-Key e Max-Heap-Insert in $O(\lg n)$ → [[heap-extract-max]], [[heap-increase-key]], [[max-heap-insert]], [[coda-di-priorita]].

## Refusi e note · [[10 - Heap - Heapsort.pdf#page=3|p. 3]], [[10 - Heap - Heapsort.pdf#page=44|p. 44]], [[10 - Heap - Heapsort.pdf#page=48|48]], [[10 - Heap - Heapsort.pdf#page=49|49]]

- p. 3: la definizione di heap in inglese (Skiena) mette la chiave minima nella radice (min-heap), mentre dalla p. 5 in poi la lezione usa il max-heap (⚠️, in [[heap]]).
- pp. 44 e 49: nello pseudocodice compare «$-\,l$» e «$+\,l$» con la lettera l al posto della cifra 1 (refuso).
- pp. 45–48: l'animazione di Heap-Increase-Key si ferma dopo il primo scambio (15 diventa figlio di 14, ancora più piccolo di lui): lo svolgimento completo è 🧩 in [[heap-increase-key]].
- pp. 15–19 e 23–40: ogni pagina è un fotogramma di animazione; l'esecuzione completa è nelle animazioni 🧩 del wiki.
- p. 2 contiene note a mano sulla memoria di Merge Sort e di Heap-Sort, di lettura incerta (❓ in [[heapsort]]); p. 14 una nota a mano rossa.
- Lo pseudocodice è in stile Cormen 2ª ed. (`do`, `then`), diverso dalle [[pseudocodice|convenzioni del corso]].
- p. 50: «Heap-Sort – da zero» è solo l'array $\langle 6, 5, 3, 1, 8, 7, 2, 4 \rangle$, senza istruzioni: interpretato come «ordinare con Heap-Sort a partire dall'array», svolto in [[tracce-su-heap]].

## Concetti introdotti

[[heap]], [[max-heapify]], [[build-max-heap]], [[heapsort]], [[heap-extract-max]], [[heap-increase-key]], [[max-heap-insert]]; esercizio [[tracce-su-heap]]; ripresa di [[coda-di-priorita]].

## Domande aperte

- Il valore atteso della memoria («$O(M)$», nota di p. 2) è ambiguo: TODO chiarire con il docente a lezione.
- Heap-Sort è stabile? Le slide non lo dicono: TODO se verrà trattato.
- Decrease-Key e Extract-Min per i min-heap sono nominate a p. 42 ma non hanno pseudocodice: sono simmetriche a quelle del max-heap.

## Domande da esame

- Definire un heap e il modo in cui è rappresentato da un array; calcolare padre e figli di un nodo.
- Spiegare Max-Heapify e dimostrare che costa $O(\lg n)$: perché il sottoproblema ha dimensione al più $2n/3$ e qual è il caso peggiore?
- Perché Build-Max-Heap costa $O(n)$ e non $O(n \lg n)$? Calcolare la serie $\sum h/2^h$.
- Eseguire Build-Max-Heap e Heap-Sort a mano su un array dato.
- Dimostrare la correttezza di Build-Max-Heap con l'invariante di ciclo.
- Descrivere le operazioni di una coda a priorità con un heap e i loro costi: Extract-Max, Increase-Key, Insert.
- Confrontare Heap-Sort con Insertion Sort e Merge Sort: tempo e memoria.

_Aggiornato: 2026-11-26 — ingest 10 - Heap - Heapsort.pdf_

<!-- nav:inizio -->
---
**Lezione 10 · pagina 1 di 9** · ← [[tree-delete|Tree-Delete (eliminazione da un BST)]] · [[lezioni|Indice]] · [[heap|Heap (binary heap)]] →
<!-- nav:fine -->
