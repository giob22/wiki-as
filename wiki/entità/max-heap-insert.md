---
tipo: entità
categoria: algoritmo
paradigma: "riduzione a Heap-Increase-Key"
fonti_pdf: ["10 - Heap - Heapsort.pdf#page=42", "10 - Heap - Heapsort.pdf#page=49"]
---

# Max-Heap-Insert

## Problema risolto · [[10 - Heap - Heapsort.pdf#page=42|p. 42]]

Operazione **Insert**$(S, x)$ della [[coda-di-priorita]]: inserisce un nuovo elemento nel max-heap $A$, che passa da $heap\text{-}size[A]$ a $heap\text{-}size[A] + 1$ elementi, mantenendo la proprietà di max-heap.

## Idea · [[10 - Heap - Heapsort.pdf#page=49|p. 49]]

Il nuovo elemento viene messo **dopo l'ultimo elemento con un valore $-\infty$**; poi si invoca [[heap-increase-key]] per impostare la chiave al valore voluto, e l'elemento risale al suo posto.

## Pseudocodice · [[10 - Heap - Heapsort.pdf#page=49|p. 49]]

```
Max-Heap-Insert (A,key)
1  heap-size[A] ← heap-size[A] + 1
2  A[heap-size[A]] ← -∞
3  Heap-Increase-Key (A,heap-size[A],key)
```

> ⚠️ Contraddizione (refuso): la slide scrive `heap-size[A] + l`, con la lettera «l» al posto del numero 1.

![[10-heap-heapsort-p49-max-heap-insert.png]]

## Esempio di esecuzione · [[10 - Heap - Heapsort.pdf#page=49|p. 49]]

![[animazione-max-heap-insert.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) sull'heap di [[10 - Heap - Heapsort.pdf#page=6|p. 6]] (istanza mia: le slide non danno un esempio) inserendo la chiave 15.

Traccia (verificata con [[heap.py]]), $A = \langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$, $key = 15$:

| Passo | Azione | Array |
|---|---|---|
| righe 1–2 | heap-size $= 11$, $A[11] \leftarrow -\infty$ | $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1, -\infty \rangle$ |
| riga 3 | Heap-Increase-Key: $A[11] \leftarrow 15$; $7 < 15$: scambio con $A[5]$ | $\langle 16, 14, 10, 8, 15, 9, 3, 2, 4, 1, 7 \rangle$ |
| riga 3 | $14 < 15$: scambio con $A[2]$ | $\langle 16, 15, 10, 8, 14, 9, 3, 2, 4, 1, 7 \rangle$ |
| riga 3 | $16 \ge 15$: stop | $\langle 16, 15, 10, 8, 14, 9, 3, 2, 4, 1, 7 \rangle$ |

## Correttezza · [[10 - Heap - Heapsort.pdf#page=49|p. 49]]

> 🧩 Derivazione mia. Con la nuova foglia $A[heap\text{-}size] = -\infty$ l'array è ancora un max-heap: $-\infty$ non è maggiore di nessun padre. Poi $key \ge -\infty$, quindi in [[heap-increase-key]] l'errore della riga 1 non scatta, e l'algoritmo porta la chiave $key$ nella posizione giusta lungo il cammino verso la radice (correttezza di Heap-Increase-Key). Con $-\infty$ nella foglia si evita di dover trattare l'inserimento come un caso a parte.

## Complessità · [[10 - Heap - Heapsort.pdf#page=49|p. 49]]

La slide dichiara $O(\lg n)$, perché c'è **una sola invocazione di Heap-Increase-Key**:

$$
T(n) = \underbrace{O(1)}_{\text{righe 1–2}} + \underbrace{O(\lg n)}_{\text{riga 3: Heap-Increase-Key su } n+1 \text{ elementi}} = O(\lg n)
$$

**Sanity check:** nell'esempio, 2 scambi per un heap di 11 elementi ($\lfloor \lg 11 \rfloor = 3$).
**Ipotesi:** modello RAM; l'array ha spazio per un elemento in più (altrimenti il costo include il ridimensionamento).

## Connessioni

- [[heap-increase-key]] — fa tutto il lavoro
- [[coda-di-priorita]] — Insert
- [[tree-insert]] — l'inserimento nel BST, che invece costa $O(h)$ e attacca una foglia

## Fonti · [[10 - Heap - Heapsort.pdf#page=42|p. 42]], [[10 - Heap - Heapsort.pdf#page=49|49]]

- [[lezione-10-heap-e-heapsort]]

_Aggiornato: 2026-11-26 — ingest 10 - Heap - Heapsort.pdf_

<!-- nav:inizio -->
---
**Lezione 10 · pagina 8 di 9** · ← [[heap-increase-key|Heap-Increase-Key]] · [[lezioni|Indice]] · [[tracce-su-heap|Tracce su heap]] →
<!-- nav:fine -->
