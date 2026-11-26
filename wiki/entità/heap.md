---
tipo: entità
categoria: struttura-dati
fonti_pdf: ["10 - Heap - Heapsort.pdf#page=3", "10 - Heap - Heapsort.pdf#page=4", "10 - Heap - Heapsort.pdf#page=5", "10 - Heap - Heapsort.pdf#page=6"]
---

# Heap (binary heap)

## Cos'è · [[10 - Heap - Heapsort.pdf#page=3|p. 3]], [[10 - Heap - Heapsort.pdf#page=4|4]], [[10 - Heap - Heapsort.pdf#page=6|6]]

Le slide (in inglese, p. 3) definiscono un **binary heap** come un albero binario con una chiave in ogni nodo tale che:
1. tutte le foglie stanno al più su **due livelli adiacenti**;
2. tutte le foglie del livello più basso stanno **a sinistra**, e tutti i livelli tranne l'ultimo sono **completamente pieni**;
3. la chiave nella radice è $\le$ di tutti i suoi figli, e i sottoalberi sinistro e destro sono a loro volta heap binari.

Le condizioni 1 e 2 specificano la **forma** dell'albero (che quindi è *bilanciato*, nota a mano di p. 3), la condizione 3 specifica l'**etichettatura**, cioè il *contenuto* (nota a mano).

Gli heap mantengono un **ordine parziale** sull'insieme degli elementi: più debole dell'ordine totale (quindi si mantiene in modo efficiente) ma più forte dell'ordine casuale (quindi il minimo si individua rapidamente) (p. 4). Nelle slide un heap con le chiavi 1492, 1783, 1776, 1804, 1865, 1945, 1963, 1918, 2001, 1941 è mostrato sia come albero sia come array (p. 4).

![[10-heap-heapsort-p3-definizione-heap.png]]
![[10-heap-heapsort-p4-binary-heap.png]]

> ⚠️ Contraddizione (di convenzione): la definizione di p. 3 mette la chiave minima nella radice (**min-heap**), mentre il resto della lezione usa il **max-heap**. A p. 6 sono definiti entrambi:
> - **max-heap**: $A[i] \le A[\text{Parent}(i)]$ per ogni $i > 1$, quindi nella radice c'è il valore più grande;
> - **min-heap**: $A[i] \ge A[\text{Parent}(i)]$ per ogni $i > 1$, quindi nella radice c'è il valore più piccolo.

![[10-heap-heapsort-p6-max-heap-min-heap.png]]

## Rappresentazione in memoria · [[10 - Heap - Heapsort.pdf#page=5|p. 5]]

Un heap è rappresentato da un [[array]] $A$ (un array è una struttura contigua, → [[strutture-contigue-e-collegate]]) che si legge come un albero binario completo riempito per livelli, da sinistra a destra (nota a mano di p. 5: «consiste in una mappa logica per la ricerca», con una freccia verso l'albero). Gli attributi sono:
- $length[A]$, il numero di elementi dell'array;
- $heap\text{-}size[A]$, il numero di elementi dell'array che appartengono all'heap, con $heap\text{-}size[A] \le length[A]$;
- le posizioni dei parenti, con indici da 1:

$$
\text{Parent}(i) = \lfloor i/2 \rfloor \qquad \text{Left}(i) = 2i \qquad \text{Right}(i) = 2i + 1
$$

Le operazioni sull'heap si implementano in maniera efficiente (p. 5). L'esempio della slide è $A = \langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$: la radice 16 (posizione 1) ha figli 14 (2) e 10 (3); 14 ha figli 8 (4) e 7 (5); 10 ha figli 9 (6) e 3 (7); 8 ha figli 2 (8) e 4 (9); 7 ha il figlio sinistro 1 (10).

![[10-heap-heapsort-p5-rappresentazione-array-albero.png]]

> 🧩 Perché $\text{Left}(i) = 2i$: se i nodi sono numerati per livelli da sinistra a destra, il livello $d$ contiene i numeri da $2^d$ a $2^{d+1} - 1$. Il nodo $i = 2^d + k$ ($0 \le k < 2^d$) ha $k$ nodi alla sua sinistra sul livello; ognuno ha 2 figli sul livello successivo, quindi i suoi figli sono i numeri $2^{d+1} + 2k$ e $2^{d+1} + 2k + 1$, cioè $2i$ e $2i + 1$.

## Operazioni

| Operazione | Pagina wiki | Costo |
|---|---|---|
| ripristino della proprietà in un nodo | [[max-heapify]] | $O(\lg n)$ |
| costruzione da un array arbitrario | [[build-max-heap]] | $O(n)$ |
| ordinamento | [[heapsort]] | $O(n \lg n)$ |
| massimo, estrazione del massimo | [[heap-extract-max]] | $\Theta(1)$, $O(\lg n)$ |
| aumento di una chiave | [[heap-increase-key]] | $O(\lg n)$ |
| inserimento | [[max-heap-insert]] | $O(\lg n)$ |

Le ultime quattro realizzano una [[coda-di-priorita]].

## Derivazioni · [[10 - Heap - Heapsort.pdf#page=12|p. 12]], [[10 - Heap - Heapsort.pdf#page=13|13]], [[10 - Heap - Heapsort.pdf#page=21|21]]

### Derivazione — altezza e numero di nodi per altezza · [[10 - Heap - Heapsort.pdf#page=21|p. 21]]
**Fonte:** le tre affermazioni sono date senza passaggi («Dato che…»).
**Si parte da:** la forma dell'heap (livelli $0, \dots, h$, tutti pieni tranne al più l'ultimo) e da $\text{Left}(i) = 2i$.

> 🧩 Derivazione mia. **(a) Altezza.** Sia $h$ l'altezza (numero di archi del cammino più lungo dalla radice a una foglia). I livelli $0, \dots, h-1$ sono pieni e l'ultimo ne ha da 1 a $2^h$ nodi:

$$
\begin{aligned}
\textstyle\sum_{i=0}^{h-1} 2^i + 1 \le n \le \sum_{i=0}^{h} 2^i \;&\Longrightarrow\; 2^h \le n \le 2^{h+1} - 1 && \text{serie geometrica: } \textstyle\sum_{i=0}^{k} 2^i = 2^{k+1} - 1 \\
&\Longrightarrow\; h \le \lg n < h + 1 && \text{passo ai logaritmi in base 2 (}\lg = \log_2\text{)} \\
&\Longrightarrow\; h = \lfloor \lg n \rfloor && \text{definizione di parte intera}
\end{aligned}
$$

**(b) Foglie.** Il nodo $i$ ha un figlio sinistro se e solo se $2i \le n$, cioè $i \le \lfloor n/2 \rfloor$: i nodi interni sono $1, \dots, \lfloor n/2 \rfloor$ e le foglie (altezza 0) sono i restanti $n - \lfloor n/2 \rfloor = \lceil n/2 \rceil$. Per questo Build-Max-Heap parte da $i = \lfloor n/2 \rfloor$.

**(c) Nodi di altezza $h$.** Sia $n_h$ il numero di nodi di altezza $h$ in un heap di $n$ nodi. Si dimostra $n_h \le \lceil n / 2^{h+1} \rceil$ per induzione su $h$.
- *Base* $h = 0$: $n_0 = \lceil n/2 \rceil = \lceil n/2^{0+1} \rceil$ per (b).
- *Passo:* togliendo le foglie rimane un albero della stessa forma con $n' = n - \lceil n/2 \rceil = \lfloor n/2 \rfloor$ nodi, in cui i nodi di altezza $h-1$ sono quelli di altezza $h$ dell'albero originale. Per ipotesi induttiva:

$$
n_h = n'_{h-1} \le \left\lceil \frac{n'}{2^{h}} \right\rceil = \left\lceil \frac{\lfloor n/2 \rfloor}{2^{h}} \right\rceil \le \left\lceil \frac{n}{2^{h+1}} \right\rceil \qquad \text{perché } \lfloor n/2 \rfloor \le n/2
$$

**Sanity check** ([[heap.py]], $n = 10$): altezza $\lfloor \lg 10 \rfloor = 3$; nodi di altezza 0, 1, 2, 3: 5, 3, 1, 1, contro i limiti $\lceil 10/2 \rceil = 5$, $\lceil 10/4 \rceil = 3$, $\lceil 10/8 \rceil = 2$, $\lceil 10/16 \rceil = 1$.
**Ipotesi:** albero con la forma dell'heap (condizioni 1 e 2 di p. 3).

## Connessioni

- [[max-heapify]], [[build-max-heap]], [[heapsort]] — gli algoritmi che lavorano sulla proprietà di max-heap
- [[coda-di-priorita]] — un heap è la sua realizzazione efficiente
- [[albero]] — altezza e bilanciamento: l'altezza $\Theta(\lg n)$ di un heap viene dalla sua forma
- [[albero-binario-di-ricerca]] — anche il BST è un albero binario con le chiavi ordinate, ma con un'altra proprietà (sinistra $\le$ nodo $\le$ destra) e senza vincoli di forma

## Fonti · [[10 - Heap - Heapsort.pdf#page=3|p. 3]], [[10 - Heap - Heapsort.pdf#page=4|4]], [[10 - Heap - Heapsort.pdf#page=5|5]], [[10 - Heap - Heapsort.pdf#page=6|6]], [[10 - Heap - Heapsort.pdf#page=21|21]]

- [[lezione-10-heap-e-heapsort]]

_Aggiornato: 2026-11-26 — ingest 10 - Heap - Heapsort.pdf_

<!-- nav:inizio -->
---
**Lezione 10 · pagina 2 di 9** · ← [[lezione-10-heap-e-heapsort|Lezione 10: introduzione e riepilogo]] · [[lezioni|Indice]] · [[max-heapify|Max-Heapify]] →
<!-- nav:fine -->
