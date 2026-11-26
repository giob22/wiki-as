---
tipo: esercizio
argomento: "tracce di Build-Max-Heap e Heap-Sort su un heap"
difficoltà: bassa
---

# Tracce su heap

## Metodo

1. Scrivere l'array con gli indici da 1 e l'albero corrispondente: i figli di $i$ sono $2i$ e $2i+1$, il padre è $\lfloor i/2 \rfloor$ ([[heap]]).
2. **Build-Max-Heap** ([[build-max-heap]]): per $i = \lfloor n/2 \rfloor$ fino a 1, eseguire Max-Heapify sul nodo $i$: se $A[i]$ è minore di un figlio, scambiarlo con il **figlio maggiore** e ripetere sulla posizione del figlio, finché $A[i]$ è $\ge$ i figli o è una foglia ([[max-heapify]]).
3. **Heap-Sort** ([[heapsort]]): per $i = n$ fino a 2, scambiare $A[1]$ con $A[i]$, ridurre heap-size a $i-1$ ed eseguire Max-Heapify sulla radice. Annotare a ogni passo l'array, separando con una barra la parte ordinata.
4. Controllo finale: l'array è ordinato e ogni passo di Max-Heapify ha lasciato un max-heap.

## Strumenti usati

- [[heap]] (rappresentazione con array, proprietà di max-heap), [[max-heapify]], [[build-max-heap]], [[heapsort]]
- [[invariante-di-ciclo]] per controllare lo stato a metà esecuzione

## Casi svolti

### Caso 1 — Heap-Sort da zero su $\langle 6, 5, 3, 1, 8, 7, 2, 4 \rangle$ · [[10 - Heap - Heapsort.pdf#page=50|p. 50]]
**Traccia:** la slide (titolo «Heap-Sort – da zero») dà solo l'array di 8 elementi, senza svolgimento. Svolgimento mio (🧩), verificato con [[heap.py]].

**Build-Max-Heap** ($n = 8$, $i = 4, 3, 2, 1$):

| $i$ | Nodo e figli | Azione | Array |
|---|---|---|---|
| (inizio) | | | $\langle 6, 5, 3, 1, 8, 7, 2, 4 \rangle$ |
| 4 | $A[4] = 1$, figlio $A[8] = 4$ | $1 < 4$: scambio | $\langle 6, 5, 3, 4, 8, 7, 2, 1 \rangle$ |
| 3 | $A[3] = 3$, figli $A[6] = 7$, $A[7] = 2$ | $3 < 7$: scambio con 7 | $\langle 6, 5, 7, 4, 8, 3, 2, 1 \rangle$ |
| 2 | $A[2] = 5$, figli $A[4] = 4$, $A[5] = 8$ | $5 < 8$: scambio con 8 | $\langle 6, 8, 7, 4, 5, 3, 2, 1 \rangle$ |
| 1 | $A[1] = 6$, figli $A[2] = 8$, $A[3] = 7$ | $6 < 8$: scambio con 8; poi su $A[2] = 6$, figli 4, 5: $6 \ge$ entrambi, stop | $\langle 8, 6, 7, 4, 5, 3, 2, 1 \rangle$ |

4 scambi in tutto. **Heap-Sort** (la barra separa heap e parte ordinata):

| $i$ | Dopo lo scambio $A[1] \leftrightarrow A[i]$ | Dopo Max-Heapify (A,1) |
|---|---|---|
| 8 | $\langle 1, 6, 7, 4, 5, 3, 2 \mid 8 \rangle$ | $\langle 7, 6, 3, 4, 5, 1, 2 \mid 8 \rangle$ |
| 7 | $\langle 2, 6, 3, 4, 5, 1 \mid 7, 8 \rangle$ | $\langle 6, 5, 3, 4, 2, 1 \mid 7, 8 \rangle$ |
| 6 | $\langle 1, 5, 3, 4, 2 \mid 6, 7, 8 \rangle$ | $\langle 5, 4, 3, 1, 2 \mid 6, 7, 8 \rangle$ |
| 5 | $\langle 2, 4, 3, 1 \mid 5, 6, 7, 8 \rangle$ | $\langle 4, 2, 3, 1 \mid 5, 6, 7, 8 \rangle$ |
| 4 | $\langle 1, 2, 3 \mid 4, 5, 6, 7, 8 \rangle$ | $\langle 3, 2, 1 \mid 4, 5, 6, 7, 8 \rangle$ |
| 3 | $\langle 1, 2 \mid 3, 4, 5, 6, 7, 8 \rangle$ | $\langle 2, 1 \mid 3, 4, 5, 6, 7, 8 \rangle$ |
| 2 | $\langle 1 \mid 2, 3, 4, 5, 6, 7, 8 \rangle$ | $\langle 1 \mid 2, 3, 4, 5, 6, 7, 8 \rangle$ |

**Risultato:** $\langle 1, 2, 3, 4, 5, 6, 7, 8 \rangle$. **Verifica:** [[heap.py]] esegue Build-Max-Heap e Heap-Sort sullo stesso array, stampa gli stati intermedi (che coincidono con le righe delle tabelle) e controlla il risultato finale.

## Trappole

- Scambiare con il figlio **maggiore**, non con il primo figlio che è più grande del nodo: altrimenti l'altro figlio resta maggiore del nuovo padre.
- Dimenticare di **ridurre heap-size** prima di Max-Heapify: l'elemento già sistemato verrebbe di nuovo trattato come parte dell'heap.
- Cominciare Build-Max-Heap da $n$ invece che da $\lfloor n/2 \rfloor$: le foglie sono già heap, e Max-Heapify su di esse non fa nulla ma si sprecano chiamate.
- Gli indici partono da 1: $\text{Left}(i) = 2i$; con indici da 0 le formule cambiano.

_Aggiornato: 2026-11-26 — ingest 10 - Heap - Heapsort.pdf_

<!-- nav:inizio -->
---
**Lezione 10 · pagina 9 di 9** · ← [[max-heap-insert|Max-Heap-Insert]] · [[lezioni|Indice]] · [[lezione-11-alberi-rosso-neri|Lezione 11: introduzione e riepilogo]] →
<!-- nav:fine -->
