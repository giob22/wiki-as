---
tipo: entità
categoria: algoritmo
paradigma: "riduzione a un sottoproblema più piccolo (ricorsione in coda)"
fonti_pdf: ["10 - Heap - Heapsort.pdf#page=7", "10 - Heap - Heapsort.pdf#page=11", "10 - Heap - Heapsort.pdf#page=12", "10 - Heap - Heapsort.pdf#page=13", "10 - Heap - Heapsort.pdf#page=14"]
---

# Max-Heapify

## Problema risolto · [[10 - Heap - Heapsort.pdf#page=7|p. 7]]

- **Input:** un array $A$ che rappresenta un [[heap]] e un indice $i$; si **assume** che gli alberi con radice in $\text{Left}(i)$ e $\text{Right}(i)$ siano max-heap.
- **Output:** $A$ modificato in modo che anche l'albero con radice in $i$ sia un max-heap.

Nota a mano di p. 7: Max-Heapify «prende un nodo e lo riordina affinché sia un max heap».

![[10-heap-heapsort-p7-max-heapify-problema.png]]

## Idea · [[10 - Heap - Heapsort.pdf#page=7|p. 7]]–[[10 - Heap - Heapsort.pdf#page=10|10]]

La sola cosa che può non andare è che $A[i]$ sia più piccolo di uno dei suoi figli. Si sceglie il più grande fra $A[i]$, $A[\text{Left}(i)]$ e $A[\text{Right}(i)]$: se è già $A[i]$ non c'è nulla da fare, altrimenti si scambia $A[i]$ con quel figlio e si ripete lo stesso ragionamento sul sottoalbero del figlio, dove la chiave scesa potrebbe ora violare la proprietà.

## Pseudocodice · [[10 - Heap - Heapsort.pdf#page=11|p. 11]]

```
Max-Heapify (A,i)
1  l ← Left(i)
2  r ← Right(i)
3  largest ← i
4  if l ≤ heap-size[A] and A[l] > A[largest]
5      then largest ← l
6  if r ≤ heap-size[A] and A[r] > A[largest]
7      then largest ← r
8  if largest ≠ i
9      then exchange A[i] ↔ A[largest]
10          Max-Heapify (A,largest)
```

Le slide numerano le righe solo nel testo; i numeri sono miei, per le tabelle di costo.

![[10-heap-heapsort-p11-max-heapify-codice.png]]

## Esempio di esecuzione · [[10 - Heap - Heapsort.pdf#page=7|p. 7]]–[[10 - Heap - Heapsort.pdf#page=10|10]]

![[animazione-max-heapify.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero Max-Heapify sull'albero delle slide: $A = \langle 16, 4, 10, 14, 7, 9, 3, 2, 8, 1 \rangle$, $i = 2$, $heap\text{-}size[A] = 10$. Si vedono, per ogni chiamata, il calcolo di $l$, $r$, $largest$, la scelta e lo scambio.

Traccia (verificata con [[heap.py]]; le slide mostrano lo stato di partenza a p. 7, la chiamata con $i = 2$ a p. 8, quella con $i = 4$ a p. 9 e il risultato a p. 10):

| Chiamata | $i$ | $l$, $r$ | $A[i]$, $A[l]$, $A[r]$ | $largest$ | Scambio | Array dopo |
|---|---|---|---|---|---|---|
| 1 | 2 | 4, 5 | 4, 14, 7 | 4 | $A[2] \leftrightarrow A[4]$ | $\langle 16, 14, 10, 4, 7, 9, 3, 2, 8, 1 \rangle$ |
| 2 | 4 | 8, 9 | 4, 2, 8 | 9 | $A[4] \leftrightarrow A[9]$ | $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$ |
| 3 | 9 | 18, 19 | — | 9 | nessuno ($l, r > heap\text{-}size$) | invariato |

## Correttezza · [[10 - Heap - Heapsort.pdf#page=7|p. 7]]

> 🧩 Derivazione mia, per induzione sull'altezza $h$ del nodo $i$. **Ipotesi (precondizione):** i sottoalberi di $\text{Left}(i)$ e $\text{Right}(i)$ sono max-heap.
> - **Base** ($h = 0$, $i$ è una foglia): $l, r > heap\text{-}size[A]$, quindi $largest = i$ e non si fa nulla; un albero di un solo nodo è un max-heap.
> - **Passo** ($h > 0$): sia $c = largest$ dopo le righe 3–7, cioè l'indice del massimo fra $A[i]$ e i suoi figli.
>   - Se $c = i$, $A[i] \ge$ entrambi i figli e i sottoalberi sono max-heap: l'albero in $i$ è un max-heap.
>   - Se $c \ne i$, dopo lo scambio $A[i]$ contiene il vecchio $A[c]$, che era $\ge$ l'altro figlio e $\ge$ tutto il proprio sottoalbero (era una radice di max-heap): quindi è $\ge$ tutti i discendenti di $i$. Il sottoalbero del figlio *non* scelto è invariato e resta un max-heap. Nel sottoalbero di $c$ è cambiata solo la radice (ora contiene il vecchio $A[i]$) e i suoi figli sono ancora radici di max-heap: la precondizione vale per la chiamata ricorsiva su $c$, che ha altezza $< h$, e per ipotesi induttiva la rende un max-heap.
> - **Terminazione:** a ogni chiamata ricorsiva l'indice scende di un livello, al massimo fino a una foglia.

## Complessità · [[10 - Heap - Heapsort.pdf#page=11|p. 11]]–[[10 - Heap - Heapsort.pdf#page=14|14]]

La slide imposta il costo come somma di due termini (p. 11): tempo **costante** per individuare il massimo fra tre elementi e fare lo scambio (righe 1–9), più il tempo per eseguire Max-Heapify su un **problema di dimensione minore** (riga 10). Resta da stabilire quanto vale la dimensione del sottoproblema (p. 12, «Stop & Think»). Sia $n$ la dimensione del problema originario, $m$ la dimensione del sottoalbero con più elementi e $h$ l'altezza del nodo.

### Derivazione — dimensione del sottoproblema · [[10 - Heap - Heapsort.pdf#page=12|p. 12]], [[10 - Heap - Heapsort.pdf#page=13|13]]
**Fonte:** i due casi sono dati con le formule; il rapporto $m/n$ è dato come limite.
**Si parte da:** la forma dell'heap ([[heap]]) e dalla serie geometrica $\sum_{i=0}^{k} 2^i = 2^{k+1} - 1$.

**Caso 1: ultimo livello pieno** (non è il caso peggiore, p. 12). L'albero di radice $i$ ha livelli $0..h$ tutti pieni; il sottoalbero più grande ha livelli $0..h-1$ pieni:

$$
\begin{aligned}
n &= \textstyle\sum_{i=0}^{h} 2^i = 2^{h+1} - 1 && \text{albero perfetto di altezza } h \\
m &= \textstyle\sum_{i=0}^{h-1} 2^i = 2^h - 1 && \text{sottoalbero perfetto di altezza } h-1 \\
\dfrac{m}{n} &= \dfrac{2^h - 1}{2 \cdot 2^h - 1} \xrightarrow[h \to \infty]{} \dfrac{1}{2} && \text{divido numeratore e denominatore per } 2^h
\end{aligned}
$$

quindi il sottoproblema ha dimensione $O(n/2)$.

**Caso 2: ultimo livello pieno a metà** (è il caso peggiore, p. 13). Il sottoalbero sinistro ha l'ultimo livello pieno, quello destro no:

$$
\begin{aligned}
m &= 2^h - 1 && \text{sottoalbero sinistro: perfetto di altezza } h-1 \\
n &= (2^h - 1) + (2^{h-1} - 1) + 1 = 3 \cdot 2^{h-1} - 1 && \text{sinistro} + \text{destro (altezza } h-2) + \text{radice} \\
\dfrac{m}{n} &= \dfrac{2 \cdot 2^{h-1} - 1}{3 \cdot 2^{h-1} - 1} \xrightarrow[h \to \infty]{} \dfrac{2}{3} && \text{divido per } 2^{h-1}
\end{aligned}
$$

quindi il sottoproblema ha dimensione $O(2n/3)$.

> 🧩 Perché il caso 2 è il peggiore. Sia $\ell$ il numero di nodi sull'ultimo livello, $1 \le \ell \le 2^h$. Se $\ell \le 2^{h-1}$ tutti i nodi dell'ultimo livello stanno a sinistra: $m = 2^{h-1} - 1 + \ell$, $n = 2^h - 1 + \ell$, e $m/n$ **cresce** con $\ell$ (aggiungere lo stesso numero a numeratore e denominatore, con $m < n$, avvicina il rapporto a 1), fino al valore del caso 2 per $\ell = 2^{h-1}$. Se $\ell > 2^{h-1}$ il sottoalbero sinistro è già pieno ($m = 2^h - 1$ fisso) e $n$ cresce: $m/n$ **decresce** fino a $1/2$ del caso 1 per $\ell = 2^h$. Il massimo di $m/n$ è quindi $\to 2/3$.

**Sanity check:** per $h = 3$ e ultimo livello a metà ($\ell = 4$): $n = 3 \cdot 4 - 1 = 11$, $m = 7$, $m/n = 0.64$, già vicino a $2/3$.
**Ipotesi:** heap con la forma di p. 3 e radice $i$ con due sottoalberi.

### Derivazione — $T(n) = O(\lg n)$ · [[10 - Heap - Heapsort.pdf#page=14|p. 14]]
**Fonte:** «Il tempo di esecuzione è $T(n) \le T(2n/3) + \Theta(1)$. Rientra nel caso 2 del teorema dell'esperto. La complessità di Max-Heapify è $O(\lg n)$» (senza i passaggi).
**Si parte da:** [[teorema-dell-esperto]] con $a = 1$, $b = 3/2$, $f(n) = \Theta(1)$.

$$
\begin{aligned}
n^{\log_b a} &= n^{\log_{3/2} 1} = n^0 = 1 && \log_b 1 = 0 \\
f(n) &= \Theta(1) = \Theta\!\left(n^{\log_b a}\right) && \text{caso 2 del teorema} \\
T(n) &= \Theta\!\left(n^{\log_b a} \lg n\right) = \Theta(\lg n) && \text{conclusione del caso 2}
\end{aligned}
$$

Poiché la ricorrenza è una *disuguaglianza* ($\le$), il risultato è un limite superiore: $T(n) = O(\lg n)$. Lo stesso risultato per srotolamento:

$$
T(n) \le T\!\left(\tfrac{2n}{3}\right) + c \le T\!\left(\left(\tfrac{2}{3}\right)^2 n\right) + 2c \le \dots \le T\!\left(\left(\tfrac{2}{3}\right)^k n\right) + k c \qquad \text{ipotesi induttiva } k \text{ volte}
$$

Si arriva a un sottoproblema di dimensione 1 quando $(2/3)^k n \le 1$, cioè per $k = \log_{3/2} n = \lg n / \lg(3/2)$; allora $T(n) \le T(1) + c \log_{3/2} n = O(\lg n)$, perché il cambio di base è un fattore costante.

> 🧩 Limite inferiore: se la radice è la chiave più piccola, Max-Heapify la fa scendere fino a una foglia (un'iterazione per livello), cioè $\Theta(h) = \Theta(\lg n)$ chiamate ($h = \lfloor \lg n \rfloor$, [[heap]]). Il caso peggiore è quindi $\Theta(\lg n)$.

**Sanity check** ([[heap.py]]): nell'esempio ($n = 10$, $h = 3$) il nodo 2 produce 3 chiamate, quante i livelli da 2 a una foglia, e $\lceil \log_{3/2} 10 \rceil = 6 \ge 3$.
**Ipotesi:** costo costante delle righe 1–9 (modello RAM); caso peggiore = sottoproblema di dimensione $2n/3$ a ogni chiamata.

### Costo in funzione dell'altezza del nodo · [[10 - Heap - Heapsort.pdf#page=21|p. 21]]
Le slide usano anche (p. 21) che Max-Heapify su un nodo di altezza $h$ ha complessità $O(h)$: ogni chiamata fa lavoro costante e porta l'indice un livello più in basso, quindi ci sono al più $h$ chiamate ricorsive. Questa forma è quella che serve per [[build-max-heap]].

## Proprietà

- **In-place** (🧩): modifica solo $A$; la ricorsione è in coda (nessun lavoro dopo la chiamata della riga 10), quindi si può scrivere come ciclo con spazio aggiuntivo $O(1)$; come scritta usa uno spazio di pila $O(h) = O(\lg n)$.
- Usata da [[build-max-heap]], [[heapsort]] e [[heap-extract-max]].

## Connessioni

- [[heap]] — la proprietà che Max-Heapify ripristina
- [[teorema-dell-esperto]] — caso 2, usato per la ricorrenza
- [[equazioni-di-ricorrenza]] — $T(n) \le T(2n/3) + \Theta(1)$

## Fonti · [[10 - Heap - Heapsort.pdf#page=7|p. 7]], [[10 - Heap - Heapsort.pdf#page=11|11]]–[[10 - Heap - Heapsort.pdf#page=14|14]]

- [[lezione-10-heap-e-heapsort]]

_Aggiornato: 2026-11-26 — ingest 10 - Heap - Heapsort.pdf_

<!-- nav:inizio -->
---
**Lezione 10 · pagina 3 di 9** · ← [[heap|Heap (binary heap)]] · [[lezioni|Indice]] · [[build-max-heap|Build-Max-Heap]] →
<!-- nav:fine -->
