---
tipo: entità
categoria: algoritmo
paradigma: "costruzione dal basso verso l'alto"
fonti_pdf: ["10 - Heap - Heapsort.pdf#page=14", "10 - Heap - Heapsort.pdf#page=15", "10 - Heap - Heapsort.pdf#page=20", "10 - Heap - Heapsort.pdf#page=21"]
---

# Build-Max-Heap

## Problema risolto · [[10 - Heap - Heapsort.pdf#page=14|p. 14]]

- **Input:** un array $A$ arbitrario di $n = length[A]$ elementi.
- **Output:** $A$ riordinato in modo che sia un [[heap]] (max-heap).

## Idea · [[10 - Heap - Heapsort.pdf#page=14|p. 14]]

[[max-heapify]] ripristina la proprietà in un nodo se i suoi due sottoalberi sono già max-heap. Quindi lo si invoca **partendo dal basso**: i nodi foglia si saltano perché sono heap di un solo elemento, e si risale verso la radice, così che ogni volta i sottoalberi dei figli siano già a posto. Nota a mano di p. 14: «perché per ogni passaggio assumiamo che gli heap inferiori siano tutto ok».

- Max-Heapify$(A, i)$: ripristina la proprietà di max-heap nel sottoalbero radicato in $i$, assumendo i sottoalberi sinistro e destro già max-heap;
- Build-Max-Heap$(A)$: trasforma l'intero array in un max-heap, chiamando Max-Heapify sui nodi interni, dal basso verso l'alto.

![[10-heap-heapsort-p14-da-max-heapify-a-build.png]]

## Pseudocodice · [[10 - Heap - Heapsort.pdf#page=20|p. 20]]

```
Build-Max-Heap (A)
1  heap-size[A] ← length[A]
2  for i ← ⌊length[A]/2⌋ downto 1
3      do Max-Heapify (A,i)
```

![[10-heap-heapsort-p20-build-max-heap-invariante.png]]

## Esempio di esecuzione · [[10 - Heap - Heapsort.pdf#page=15|p. 15]]–[[10 - Heap - Heapsort.pdf#page=19|19]]

![[animazione-build-max-heap.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo sull'array delle slide $\langle 4, 1, 3, 2, 16, 9, 10, 14, 8, 7 \rangle$ (p. 15): per ogni $i$ da 5 a 1 si vedono la chiamata di Max-Heapify e gli scambi; in verde i nodi che sono già radici di max-heap (l'invariante).

![[10-heap-heapsort-p15-build-max-heap-inizio.png]]

Traccia (verificata con [[heap.py]]; le slide mostrano un fotogramma per ogni $i$, pp. 15–19):

| $i$ | Max-Heapify su $A[i]$ | Array dopo |
|---|---|---|
| (inizio) | — | $\langle 4, 1, 3, 2, 16, 9, 10, 14, 8, 7 \rangle$ |
| 5 | $16 > 7$: nessuno scambio | $\langle 4, 1, 3, 2, 16, 9, 10, 14, 8, 7 \rangle$ |
| 4 | $2 <$ figli $14, 8$: scambio con 14 | $\langle 4, 1, 3, 14, 16, 9, 10, 2, 8, 7 \rangle$ |
| 3 | $3 <$ figli $9, 10$: scambio con 10 | $\langle 4, 1, 10, 14, 16, 9, 3, 2, 8, 7 \rangle$ |
| 2 | $1 <$ figli $14, 16$: scambio con 16; poi $1 < 7$ (figlio in posizione 10): scambio con 7 | $\langle 4, 16, 10, 14, 1, 9, 3, 2, 8, 7 \rangle \to \langle 4, 16, 10, 14, 7, 9, 3, 2, 8, 1 \rangle$ |
| 1 | $4 <$ figli $16, 10$: scambio con 16, poi con 14, poi con 8 | $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$ |

In totale 12 chiamate di Max-Heapify e 7 scambi (verificato con [[heap.py]]).

## Correttezza · [[10 - Heap - Heapsort.pdf#page=20|p. 20]]

**Invariante** (slide): all'inizio di ciascuna iterazione del ciclo `for`, ogni nodo $i+1, i+2, \dots, n$ è la radice di un max-heap.
- **Inizializzazione:** prima della prima iterazione $i = \lfloor n/2 \rfloor$, e i nodi $i+1, \dots, n$ sono foglie (→ [[heap]], derivazione (b)), quindi max-heap.
- **Conservazione:** i figli di $i$ sono radici di max-heap (per ipotesi), quindi vale la precondizione di Max-Heapify, che rende anche $i$ radice di un max-heap; decrementando $i$ l'invariante si conserva.
- **Conclusione:** al termine tutti i nodi $i \ge 1$ sono radici di max-heap; in particolare per $i = 1$ il vettore è un max-heap.

## Complessità · [[10 - Heap - Heapsort.pdf#page=21|p. 21]]

### Derivazione — $T(n) = O(n)$ · [[10 - Heap - Heapsort.pdf#page=21|p. 21]]
**Fonte:** «$O(n)$ invocazioni di Max-Heapify $\Rightarrow O(n \lg n)$. Non è un limite stretto», poi la serie con il risultato $O(2n) = O(n)$.
**Si parte da:** [[max-heapify]] costa $O(h)$ su un nodo di altezza $h$; un heap di $n$ elementi ha altezza $\lfloor \lg n \rfloor$ e al più $\lceil n/2^{h+1} \rceil$ nodi di altezza $h$ ([[heap]]).

**Limite grossolano.** Ci sono $\lfloor n/2 \rfloor = O(n)$ invocazioni e ognuna costa $O(\lg n)$: in totale $O(n \lg n)$. È corretto ma non stretto, perché quasi tutti i nodi sono vicini alle foglie e costano poco.

**Limite stretto.** Si somma per altezza:

$$
\begin{aligned}
T(n) &= \sum_{h=0}^{\lfloor \lg n \rfloor} \left\lceil \frac{n}{2^{h+1}} \right\rceil O(h) && \text{(n. nodi di altezza } h) \times (\text{costo di Max-Heapify}) \\
&= O\!\left( n \sum_{h=0}^{\lfloor \lg n \rfloor} \frac{h}{2^h} \right) && \lceil n/2^{h+1} \rceil \le n/2^h \text{ (vedi sotto), costanti nell'}O \\
&= O\!\left( n \sum_{h=0}^{\infty} \frac{h}{2^h} \right) && \text{aggiungo termini} \ge 0 \text{: maggiorazione} \\
&= O(2n) = O(n) && \textstyle\sum_{h=0}^{\infty} h/2^h = 2 \text{ (vedi sotto)}
\end{aligned}
$$

> 🧩 Due passaggi che la slide non spiega.
> - **Il soffitto.** Per $h \le \lfloor \lg n \rfloor$ vale $2^h \le n$, quindi $x = n/2^{h+1} \ge 1/2$, e per $x \ge 1/2$ si ha $\lceil x \rceil \le 2x$ (per $x \in [1/2, 1]$: $1 \le 2x$; per $x > 1$: $\lceil x \rceil < x + 1 < 2x$). Quindi $\lceil n/2^{h+1} \rceil \le 2 \cdot n/2^{h+1} = n/2^h$.
> - **La serie.** Dalla serie geometrica $\sum_{h=0}^{\infty} x^h = \frac{1}{1-x}$ ($|x| < 1$), derivando termine a termine: $\sum_{h=1}^{\infty} h x^{h-1} = \frac{1}{(1-x)^2}$, cioè $\sum_{h=0}^{\infty} h x^h = \frac{x}{(1-x)^2}$. Con $x = 1/2$: $\frac{1/2}{(1/2)^2} = 2$.

> 🧩 Limite inferiore: il ciclo esegue $\lfloor n/2 \rfloor$ iterazioni, ciascuna con costo $\ge$ costante, quindi $T(n) = \Omega(n)$ e dunque $T(n) = \Theta(n)$.

**Sanity check** ([[heap.py]]): $\sum_{h} \lceil n/2^{h+1} \rceil h$ vale 10, 104, 998 per $n = 10, 100, 1000$, sempre $\le 2n$ (20, 200, 2000).
**Ipotesi:** modello RAM; costo di Max-Heapify su un nodo di altezza $h$ pari a $O(h)$; array arbitrario (il limite vale per ogni input).

## Proprietà

- **In-place** (🧩): lavora sull'array $A$ stesso, con soli scambi.

## Connessioni

- [[max-heapify]] — il passo elementare
- [[heapsort]] — usa Build-Max-Heap come primo passo
- [[heap]] — altezza e numero di nodi per altezza
- [[invariante-di-ciclo]] — il metodo della dimostrazione

## Fonti · [[10 - Heap - Heapsort.pdf#page=14|p. 14]], [[10 - Heap - Heapsort.pdf#page=15|15]]–[[10 - Heap - Heapsort.pdf#page=21|21]]

- [[lezione-10-heap-e-heapsort]]

_Aggiornato: 2026-11-26 — ingest 10 - Heap - Heapsort.pdf_

<!-- nav:inizio -->
---
**Lezione 10 · pagina 4 di 9** · ← [[max-heapify|Max-Heapify]] · [[lezioni|Indice]] · [[heapsort|Heap-Sort]] →
<!-- nav:fine -->
