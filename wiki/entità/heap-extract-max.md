---
tipo: entità
categoria: algoritmo
paradigma: "riduzione a Max-Heapify"
fonti_pdf: ["10 - Heap - Heapsort.pdf#page=42", "10 - Heap - Heapsort.pdf#page=43", "10 - Heap - Heapsort.pdf#page=44"]
---

# Heap-Maximum e Heap-Extract-Max

## Problema risolto · [[10 - Heap - Heapsort.pdf#page=42|p. 42]]

Su un max-heap che realizza una [[coda-di-priorita]] a massima priorità: **Maximum**$(S)$ restituisce l'elemento con la chiave più grande; **Extract-Max**$(S)$ lo rimuove e lo restituisce. Con un min-heap le operazioni simmetriche sono Minimum ed Extract-Min.

## Idea · [[10 - Heap - Heapsort.pdf#page=43|p. 43]], [[10 - Heap - Heapsort.pdf#page=44|44]]

- Il massimo è nella radice, quindi Heap-Maximum lo legge in tempo costante.
- Heap-Extract-Max lo memorizza, poi mette **l'ultimo elemento al posto della radice** e invoca [[max-heapify]] per ristabilire la proprietà del max-heap: l'heap perde l'ultima posizione e la radice, che ora può essere troppo piccola, scende fino al suo posto.

## Pseudocodice · [[10 - Heap - Heapsort.pdf#page=43|p. 43]], [[10 - Heap - Heapsort.pdf#page=44|44]]

```
Heap-Maximum (A)
1  return A[1]

Heap-Extract-Max (A)
1  if heap-size[A] < 1
2      error "heap empty"
3  max ← A[1]
4  A[1] ← A[heap-size[A]]
5  heap-size[A] ← heap-size[A] - 1
6  Max-Heapify (A,1)
7  return max
```

> ⚠️ Contraddizione (refuso): la slide scrive `heap-size[A] - l` alla riga 5, con la lettera «l» al posto del numero 1.

![[10-heap-heapsort-p44-heap-extract-max.png]]

## Esempio di esecuzione · [[10 - Heap - Heapsort.pdf#page=44|p. 44]]

![[animazione-heap-extract-max.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) sull'heap di [[10 - Heap - Heapsort.pdf#page=6|p. 6]] (istanza mia, le slide non danno un esempio): Extract-Max restituisce 16, l'ultimo elemento (1) va in radice e scende in tre scambi, fino a una foglia.

Traccia (verificata con [[heap.py]]), su $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$:

| Passo | Azione | Array (heap-size) |
|---|---|---|
| riga 3 | $max \leftarrow 16$ | $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$ (10) |
| righe 4–5 | $A[1] \leftarrow A[10] = 1$, heap-size $= 9$ | $\langle 1, 14, 10, 8, 7, 9, 3, 2, 4 \rangle$ (9) |
| riga 6 | Max-Heapify: 1 scambia con 14 (il maggiore fra 14 e 10), poi con 8 (il maggiore fra 8 e 7), poi con 4 (il maggiore fra 2 e 4) | $\langle 14, 8, 10, 4, 7, 9, 3, 2, 1 \rangle$ (9) |
| riga 7 | restituisce 16 | |

## Correttezza · [[10 - Heap - Heapsort.pdf#page=44|p. 44]]

> 🧩 Derivazione mia. Prima di Max-Heapify, $A[2..heap\text{-}size]$ contiene le radici dei due sottoalberi della vecchia radice, che erano max-heap e lo restano (non toccati); l'unico elemento fuori posto può essere la nuova radice $A[1]$. Vale quindi la precondizione di [[max-heapify]] su $i = 1$, che rende $A[1..heap\text{-}size]$ un max-heap. Il valore restituito $max$ era il massimo, per la proprietà del max-heap. *Caso limite:* con un solo elemento, $A[1] \leftarrow A[1]$, heap-size $= 0$ e Max-Heapify non fa nulla ($l, r > 0$).

## Complessità · [[10 - Heap - Heapsort.pdf#page=43|p. 43]], [[10 - Heap - Heapsort.pdf#page=44|44]]

- **Heap-Maximum:** $\Theta(1)$, una sola istruzione (p. 43).
- **Heap-Extract-Max:** $O(\lg n)$, perché c'è **una sola invocazione di Max-Heapify** (p. 44) e le altre righe costano $O(1)$:

$$
T(n) = \underbrace{O(1)}_{\text{righe 1–5, 7}} + \underbrace{O(\lg n)}_{\text{riga 6: Max-Heapify su un heap di } n-1 \text{ nodi}} = O(\lg n)
$$

**Sanity check:** nell'esempio, 3 scambi, quanti i livelli sotto la radice che la chiave 1 attraversa ($h = 3$ è il massimo possibile con 9 elementi).
**Ipotesi:** modello RAM; heap di $n$ elementi con altezza $\lfloor \lg n \rfloor$ ([[heap]]).

## Connessioni

- [[max-heapify]] — l'unica chiamata costosa
- [[coda-di-priorita]] — Extract-Max è Delete-Maximum; Heap-Maximum è Find-Maximum
- [[heapsort]] — le righe 3–5 di Heap-Sort sono la stessa idea: scambio con l'ultimo, riduzione dell'heap, Max-Heapify
- [[tree-minimum-maximum]] — la stessa operazione su un BST costa $O(h)$

## Fonti · [[10 - Heap - Heapsort.pdf#page=42|p. 42]]–[[10 - Heap - Heapsort.pdf#page=44|44]]

- [[lezione-10-heap-e-heapsort]]

_Aggiornato: 2026-11-26 — ingest 10 - Heap - Heapsort.pdf_

<!-- nav:inizio -->
---
**Lezione 10 · pagina 6 di 9** · ← [[heapsort|Heap-Sort]] · [[lezioni|Indice]] · [[heap-increase-key|Heap-Increase-Key]] →
<!-- nav:fine -->
