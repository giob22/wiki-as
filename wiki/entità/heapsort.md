---
tipo: entità
categoria: algoritmo
paradigma: "ordinamento con una struttura dati (heap)"
fonti_pdf: ["10 - Heap - Heapsort.pdf#page=2", "10 - Heap - Heapsort.pdf#page=22", "10 - Heap - Heapsort.pdf#page=23", "10 - Heap - Heapsort.pdf#page=41", "10 - Heap - Heapsort.pdf#page=50"]
---

# Heap-Sort

## Problema risolto · [[10 - Heap - Heapsort.pdf#page=2|p. 2]]

[[ordinamento]]: dato un array $A$ di $n$ elementi, riordinarlo in ordine crescente. La lezione lo introduce dopo due algoritmi che hanno ciascuno un difetto:
- [[insertion-sort]]: $\Theta(n^2)$ nel caso peggiore, $\Theta(n)$ nel migliore; ordina sul posto;
- [[merge-sort]]: $\Theta(n \lg n)$; **non** ordina sul posto (nota a mano di p. 2: «cresce troppo velocemente l'utilizzo di memoria se cresce di $M$», cioè $n$);
- Heap-Sort: $O(n \lg n)$, ordina sul posto, ed è basato sulla struttura dati [[heap]] (nota a mano: «struttura dati …»; accanto a «ordina sul posto»: «$\sim O(M)$ → non si può scendere (almeno in questo caso) in termini di memoria»).

> ❓ Lettura incerta della nota a mano di p. 2 («$O(M)$»): sembra dire che la memoria usata non può scendere sotto quella dell'input stesso, ma la grafia è ambigua.

![[10-heap-heapsort-p2-introduzione-heapsort.png]]

## Idea · [[10 - Heap - Heapsort.pdf#page=22|p. 22]]

1. Si rende l'array un max-heap con [[build-max-heap]];
2. il primo elemento è l'elemento massimo;
3. lo si scambia con l'ultimo: il massimo è così «sistemato» nella sua posizione finale;
4. si decrementa la dimensione dell'heap e si invoca [[max-heapify]] sulla radice per ripristinare la proprietà del max-heap; si ripete.

## Pseudocodice · [[10 - Heap - Heapsort.pdf#page=41|p. 41]]

```
Heap-Sort (A)
1  Build-Max-Heap (A)
2  for i ← length[A] downto 2
3      do exchange A[1] ↔ A[i]
4         heap-size[A] ← heap-size[A] - 1
5         Max-Heapify (A,1)
```

![[10-heap-heapsort-p41-heapsort-codice.png]]

## Esempio di esecuzione · [[10 - Heap - Heapsort.pdf#page=23|p. 23]]–[[10 - Heap - Heapsort.pdf#page=40|40]]

![[animazione-heapsort.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero Heap-Sort sull'array di [[10 - Heap - Heapsort.pdf#page=15|p. 15]], $\langle 4, 1, 3, 2, 16, 9, 10, 14, 8, 7 \rangle$: dopo Build-Max-Heap si ripetono scambio e Max-Heapify, come nelle slide dalla p. 23. In verde la parte già ordinata, in grigio le posizioni fuori dall'heap.

![[10-heap-heapsort-p23-heapsort-inizio.png]]

Traccia (verificata con [[heap.py]]); le slide mostrano per ogni iterazione due fotogrammi, «scambiamo … con … e decrementiamo la dimensione dell'heap» (pp. 23, 25, …, 39) e «invochiamo Max-Heapify su $A[1]$» (pp. 24, 26, …, 38), e un ultimo «essendo rimasto un solo elemento, l'algoritmo termina» (p. 40). La barra separa heap e parte ordinata:

| $i$ | Dopo lo scambio (riga 3–4) | Dopo Max-Heapify (riga 5) |
|---|---|---|
| (inizio) | — | $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$ |
| 10 | $\langle 1, 14, 10, 8, 7, 9, 3, 2, 4 \mid 16 \rangle$ | $\langle 14, 8, 10, 4, 7, 9, 3, 2, 1 \mid 16 \rangle$ |
| 9 | $\langle 1, 8, 10, 4, 7, 9, 3, 2 \mid 14, 16 \rangle$ | $\langle 10, 8, 9, 4, 7, 1, 3, 2 \mid 14, 16 \rangle$ |
| 8 | $\langle 2, 8, 9, 4, 7, 1, 3 \mid 10, 14, 16 \rangle$ | $\langle 9, 8, 3, 4, 7, 1, 2 \mid 10, 14, 16 \rangle$ |
| 7 | $\langle 2, 8, 3, 4, 7, 1 \mid 9, 10, 14, 16 \rangle$ | $\langle 8, 7, 3, 4, 2, 1 \mid 9, 10, 14, 16 \rangle$ |
| 6 | $\langle 1, 7, 3, 4, 2 \mid 8, 9, 10, 14, 16 \rangle$ | $\langle 7, 4, 3, 1, 2 \mid 8, 9, 10, 14, 16 \rangle$ |
| 5 | $\langle 2, 4, 3, 1 \mid 7, 8, 9, 10, 14, 16 \rangle$ | $\langle 4, 2, 3, 1 \mid 7, 8, 9, 10, 14, 16 \rangle$ |
| 4 | $\langle 1, 2, 3 \mid 4, 7, 8, 9, 10, 14, 16 \rangle$ | $\langle 3, 2, 1 \mid 4, 7, 8, 9, 10, 14, 16 \rangle$ |
| 3 | $\langle 1, 2 \mid 3, 4, 7, 8, 9, 10, 14, 16 \rangle$ | $\langle 2, 1 \mid 3, 4, 7, 8, 9, 10, 14, 16 \rangle$ |
| 2 | $\langle 1 \mid 2, 3, 4, 7, 8, 9, 10, 14, 16 \rangle$ | $\langle 1 \mid 2, 3, 4, 7, 8, 9, 10, 14, 16 \rangle$ (p. 40) |

## Correttezza · [[10 - Heap - Heapsort.pdf#page=22|p. 22]]

> 🧩 Derivazione mia. **Invariante** del ciclo `for` (righe 2–5): all'inizio di ogni iterazione, $A[1..i]$ è un max-heap che contiene gli $i$ elementi più piccoli di $A$, e $A[i+1..n]$ contiene gli $n - i$ elementi più grandi, in ordine crescente.
> - **Inizializzazione** ($i = n$): dopo [[build-max-heap]], $A[1..n]$ è un max-heap e la parte ordinata è vuota.
> - **Conservazione:** $A[1]$ è il massimo di $A[1..i]$ (proprietà del max-heap) ed è $\le$ ogni elemento di $A[i+1..n]$ (che sono i più grandi di tutti). Lo scambio mette $A[1]$ in posizione $i$: ora $A[i..n]$ contiene gli $n - i + 1$ elementi più grandi, ordinati. Con $heap\text{-}size[A] \leftarrow i - 1$, l'heap $A[1..i-1]$ ha la radice (l'ex $A[i]$) forse sbagliata, ma i figli della radice sono ancora radici di max-heap: vale la precondizione di [[max-heapify]], che ripristina il max-heap. Si passa a $i - 1$.
> - **Conclusione** ($i = 1$): $A[2..n]$ contiene gli $n - 1$ elementi più grandi in ordine crescente e $A[1]$ è il minimo, quindi $A[1..n]$ è ordinato.

## Complessità · [[10 - Heap - Heapsort.pdf#page=41|p. 41]]

### Derivazione — $T(n) = O(n \lg n)$ · [[10 - Heap - Heapsort.pdf#page=41|p. 41]]
**Fonte:** «Build-Max-Heap impiega $O(n)$; $n-1$ invocazioni di Max-Heapify, ciascuna impiega $O(\lg n)$».
**Si parte da:** [[build-max-heap]] ($O(n)$) e [[max-heapify]] ($O(\lg n)$, [[heap]] di altezza $\lfloor \lg n \rfloor$).

$$
\begin{aligned}
T(n) &= T_{\text{Build}}(n) + \sum_{i=2}^{n} \left( c_3 + c_4 + T_{\text{Heapify}}(i-1) \right) && \text{riga 1} + \text{righe 3–5 per } i = n, \dots, 2 \\
&\le O(n) + (n-1) \left( c + O(\lg n) \right) && T_{\text{Heapify}}(i-1) \le O(\lg n) \text{ per ogni } i \le n \\
&= O(n) + O(n \lg n) && (n-1) \cdot O(\lg n) = O(n \lg n) \\
&= O(n \lg n) && \text{vince il termine di ordine maggiore}
\end{aligned}
$$

**Sanity check** ([[heap.py]], array di p. 15, $n = 10$): 12 chiamate di Max-Heapify in Build-Max-Heap e 23 nel ciclo ($n - 1 = 9$ chiamate dirette più le chiamate ricorsive, in totale 35), 30 scambi; $n \lg n \approx 33$.
**Ipotesi:** modello RAM; il limite vale per ogni input (non dipende dall'ordine iniziale).

## Proprietà · [[10 - Heap - Heapsort.pdf#page=2|p. 2]]

- **In-place:** ordina sul posto (p. 2): usa solo scambi dentro $A$ e un numero costante di variabili (con Max-Heapify scritta come ciclo, 🧩).
- **Tempo:** $O(n \lg n)$ (p. 2 e p. 41).

## Esercizio della slide · [[10 - Heap - Heapsort.pdf#page=50|p. 50]]

Il «Heap-Sort – da zero» di p. 50 propone l'array $\langle 6, 5, 3, 1, 8, 7, 2, 4 \rangle$ senza svolgimento: svolto in → [[tracce-su-heap]].

![[10-heap-heapsort-p50-heapsort-da-zero.png]]

## Connessioni

- [[build-max-heap]], [[max-heapify]], [[heap]] — i pezzi di cui è fatto
- [[merge-sort]], [[insertion-sort]] — i due confronti di p. 2
- [[ordinamento]] — il problema
- [[invariante-di-ciclo]] — la tecnica della correttezza

## Fonti · [[10 - Heap - Heapsort.pdf#page=2|p. 2]], [[10 - Heap - Heapsort.pdf#page=22|22]]–[[10 - Heap - Heapsort.pdf#page=41|41]], [[10 - Heap - Heapsort.pdf#page=50|50]]

- [[lezione-10-heap-e-heapsort]]

_Aggiornato: 2026-11-26 — ingest 10 - Heap - Heapsort.pdf_

<!-- nav:inizio -->
---
**Lezione 10 · pagina 5 di 9** · ← [[build-max-heap|Build-Max-Heap]] · [[lezioni|Indice]] · [[heap-extract-max|Heap-Maximum e Heap-Extract-Max]] →
<!-- nav:fine -->
