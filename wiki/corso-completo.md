# Algoritmi e Strutture Dati — corso completo

Testo unico di studio del corso (LM Ingegneria Informatica, UNINA, Prof. Stefano Marrone). Contiene **solo ciò che sta nei PDF del corso**, nell'ordine delle slide: definizioni, pseudocodice, tabelle di costo, esempi, figure e le dimostrazioni svolte a mano dal docente. I passaggi che le slide saltano sono ricostruiti in una riga dove servono a seguire il discorso; le derivazioni estese, i grafici e le animazioni aggiuntivi e gli esercizi stanno nelle pagine concetto, entità ed esercizio, richiamate in fondo a ogni lezione («Approfondimenti nel wiki»).

**Come leggerlo.** Il riferimento al PDF compare solo nel titolo di ogni sezione (`p. N` apre la pagina). Le equazioni numerate sono quelle delle slide di ciascuna lezione. Il PDF di una lezione si genera con `python output/crea_pdf.py N` (file in `output/pdf/`); il sito di studio si genera da questo file con `python output/crea_sito.py`.

## Indice

| # | Lezione | PDF sorgente |
|---|---|---|
| 10 | [[#Lezione 10 — Heapsort\|Heapsort]] | 10 - Heap - Heapsort.pdf |
| 11 | [[#Lezione 11 — Alberi rosso-neri\|Alberi rosso-neri]] | 11 . Alberi rosso-neri.pdf |
| 12 | [[#Lezione 12 — Alberi auto-aggiustanti\|Alberi auto-aggiustanti]] | 12 - Alberi auto-aggiustanti.pdf |
| 13 | [[#Lezione 13 — Algoritmi di visita di un grafo\|Algoritmi di visita di un grafo]] | 13 - Algoritmi di visita di un grafo.pdf |
| 14 | [[#Lezione 14 — Backpropagation\|Backpropagation]] | 14 - Backpropagation.pdf |
| 15 | [[#Lezione 15 — Backtracking\|Backtracking]] | 15 - Backtracking.pdf |

## Lezione 10 — Heapsort

*Fonte: 10 - Heap - Heapsort.pdf (50 pagine: slide, con appunti a mano alle p. 2, 3, 5, 7, 14).*

### Heapsort: dove siamo · [[10 - Heap - Heapsort.pdf#page=2|p. 2]]

- **Insertion Sort**: $\Theta(n^2)$ nel caso peggiore, $\Theta(n)$ nel migliore; ordina sul posto.
- **Merge Sort**: $\Theta(n \lg n)$; non ordina sul posto (nota a mano: l'uso di memoria cresce troppo velocemente al crescere di $n$).
- **Heap Sort**: $O(n \lg n)$; ordina sul posto (nota a mano: in termini di memoria non si può scendere sotto l'ordine di $O(M)$, almeno in questo caso); basato sulla struttura dati *heap* (struttura dati aggregata).

![[10-heap-heapsort-p2-introduzione-heapsort.png]]
*Note a mano del docente sulla memoria di Merge Sort e Heap Sort.*

### Definizione di heap · [[10 - Heap - Heapsort.pdf#page=3|p. 3]], [[10 - Heap - Heapsort.pdf#page=4|4]]

Un **binary heap** è un albero binario con una chiave in ogni nodo tale che:
1. tutte le foglie stanno al più su due livelli adiacenti (l'albero è *bilanciato*);
2. tutte le foglie dell'ultimo livello stanno a sinistra, e tutti i livelli tranne l'ultimo sono completamente pieni;
3. la chiave nella radice è $\le$ di tutte le chiavi dei figli, e i sottoalberi sinistro e destro sono a loro volta heap binari.

Le condizioni 1 e 2 specificano la **forma** dell'albero, la 3 il **contenuto**. Un heap mantiene un ordine parziale degli elementi: più debole dell'ordine totale (quindi più facile da mantenere), più forte dell'ordine casuale (quindi il minimo si individua in fretta).

![[10-heap-heapsort-p4-binary-heap.png]]
*Un heap con le chiavi 1492, 1783, 1776, 1804, 1865, 1945, 1963, 1918, 2001, 1941, come albero e come array.*

### Rappresentazione con array · [[10 - Heap - Heapsort.pdf#page=5|p. 5]], [[10 - Heap - Heapsort.pdf#page=6|6]]

- $heap\text{-}size[A] \le length[A]$
- $\text{Parent}(i) = \lfloor i/2 \rfloor$, $\text{Left}(i) = 2i$, $\text{Right}(i) = 2i + 1$
- le operazioni si implementano in maniera efficiente

![[10-heap-heapsort-p5-rappresentazione-array-albero.png]]
*Heap $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$ come array e come albero (nota a mano: consiste in una mappa logica per la ricerca).*

- **Max-heap:** $A[i] \le A[\text{Parent}(i)]$ per ogni $i > 1$; nella radice c'è il valore più grande.
- **Min-heap:** $A[i] \ge A[\text{Parent}(i)]$ per ogni $i > 1$; nella radice c'è il valore più piccolo.

### Max-Heapify · [[10 - Heap - Heapsort.pdf#page=7|p. 7]]–[[10 - Heap - Heapsort.pdf#page=11|11]]

Assumendo che gli alberi con radice in $\text{Left}(i)$ e $\text{Right}(i)$ siano max-heap, si vuole fare in modo che anche l'albero con radice in $i$ lo sia (nota a mano: prende un nodo e lo riordina affinché sia un max-heap). Nell'esempio $A = \langle 16, 4, 10, 14, 7, 9, 3, 2, 8, 1 \rangle$, $i = 2$: la chiave 4 viene scambiata con il figlio maggiore 14, poi con il figlio maggiore 8, e il risultato è $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$.

![[10-heap-heapsort-p7-max-heapify-problema.png]]

```
Max-Heapify (A,i)
l ← Left(i)
r ← Right(i)
largest ← i
if l ≤ heap-size[A] and A[l] > A[largest]
    largest ← l
if r ≤ heap-size[A] and A[r] > A[largest]
    largest ← r
if largest ≠ i
    exchange A[i] ↔ A[largest]
    Max-Heapify (A,largest)
```

**Tempo di esecuzione:** tempo costante per individuare il massimo fra tre elementi e fare lo scambio, più il tempo per eseguire Max-Heapify su un problema di dimensione minore.

### Dimensione del sottoproblema · [[10 - Heap - Heapsort.pdf#page=12|p. 12]]–[[10 - Heap - Heapsort.pdf#page=14|14]]

Si pone $n$ = dimensione del problema originario, $m$ = dimensione del sottoalbero con più elementi, $h$ = altezza del nodo.

**Caso 1: ultimo livello pieno** (non è il caso peggiore):

$$
n = \sum_{i=0}^{h} 2^i = 2^{h+1} - 1 \qquad m = \sum_{i=0}^{h-1} 2^i = 2^h - 1 \qquad \frac{m}{n} = \frac{2^h - 1}{2 \cdot 2^h - 1} \xrightarrow[h \to \infty]{} \frac{1}{2}
$$

quindi il sottoproblema è $O(n/2)$.

**Caso 2: ultimo livello pieno a metà** (è il caso peggiore):

$$
m = 2^h - 1 \qquad n = (2^h - 1) + (2^{h-1} - 1) + 1 = 3 \cdot 2^{h-1} - 1 \qquad \frac{m}{n} = \frac{2 \cdot 2^{h-1} - 1}{3 \cdot 2^{h-1} - 1} \xrightarrow[h \to \infty]{} \frac{2}{3}
$$

quindi il sottoproblema è $O(2n/3)$.

![[10-heap-heapsort-p12-sottoproblema-caso-1.png]]
![[10-heap-heapsort-p13-sottoproblema-caso-2.png]]

Il tempo di esecuzione è $T(n) \le T(2n/3) + \Theta(1)$: rientra nel caso 2 del teorema dell'esperto, quindi la complessità di Max-Heapify è $O(\lg n)$.

### Da Max-Heapify a Build-Max-Heap · [[10 - Heap - Heapsort.pdf#page=14|p. 14]]–[[10 - Heap - Heapsort.pdf#page=21|21]]

Max-Heapify può essere usato per «convertire» un array in un heap, partendo dal basso e invocandolo sui nodi (nota a mano: perché per ogni passaggio assumiamo che gli heap inferiori siano tutto ok). I nodi foglia si saltano perché costituiscono un heap di 1 elemento.
- Max-Heapify$(A, i)$: ripristina la proprietà di max-heap nel sottoalbero radicato in $i$, assumendo che i sottoalberi sinistro e destro siano già max-heap.
- Build-Max-Heap$(A)$: trasforma l'intero array in un max-heap, chiamando Max-Heapify sui nodi interni dal basso verso l'alto.

```
Build-Max-Heap (A)
heap-size[A] ← length[A]
for i ← ⌊length[A]/2⌋ downto 1
    do Max-Heapify (A,i)
```

Esempio: partendo da $\langle 4, 1, 3, 2, 16, 9, 10, 14, 8, 7 \rangle$ (p. 15) si arriva, con una chiamata per ogni $i = 5, 4, 3, 2, 1$ (pp. 15–19), a $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$.

![[10-heap-heapsort-p15-build-max-heap-inizio.png]]

**Invariante:** all'inizio di ciascuna iterazione del ciclo `for`, ogni nodo $i+1, i+2, \dots, n$ è la radice di un max-heap.
- *Vero prima della prima iterazione:* $i = \lfloor n/2 \rfloor$, i nodi $i+1..n$ sono foglie e quindi max-heap.
- *Si conserva:* i figli di $i$ sono radici di max-heap (per ipotesi), quindi vale la precondizione di Max-Heapify, che rende anche $i$ radice di un max-heap; decrementando $i$ l'invariante si conserva.
- *Al termine:* tutti i nodi $i \ge 1$ sono radici di max-heap, in particolare per $i = 1$ il vettore è un max-heap.

**Complessità.** $O(n)$ invocazioni di Max-Heapify $\Rightarrow O(n \lg n)$, ma **non è un limite stretto**, dato che:
- un heap di $n$ elementi ha altezza $\lfloor \lg n \rfloor$;
- un heap di $n$ elementi ha al più $\lceil n/2^{h+1} \rceil$ elementi di altezza $h$: le foglie (altezza 0) sono $n - \lfloor n/2 \rfloor = \lceil n/2 \rceil$, i nodi di altezza 1 sono circa la metà, $\lceil n/2^2 \rceil$;
- Max-Heapify ha complessità $O(h)$ per un nodo di altezza $h$.

$$
T(n) = \sum_{h=0}^{\lfloor \lg n \rfloor} \left\lceil \frac{n}{2^{h+1}} \right\rceil O(h) = O\!\left( n \sum_{h=0}^{\lfloor \lg n \rfloor} \frac{h}{2^h} \right) = O\!\left( n \sum_{h=0}^{\infty} \frac{h}{2^h} \right) = O(2n) = O(n)
$$

![[10-heap-heapsort-p21-build-max-heap-complessita.png]]

### Heap-Sort · [[10 - Heap - Heapsort.pdf#page=22|p. 22]]–[[10 - Heap - Heapsort.pdf#page=41|41]]

1. Si rende l'array un max-heap (con Build-Max-Heap): il primo elemento è l'elemento massimo.
2. Si scambia il primo elemento con l'ultimo: l'elemento massimo è «sistemato».
3. Si decrementa la dimensione dell'heap e si invoca Max-Heapify per mantenere la proprietà del max-heap.

Esempio dall'heap $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$: per ogni $i$ un fotogramma «scambiamo … con … e decrementiamo la dimensione dell'heap» e uno «invochiamo Max-Heapify su $A[1]$» (pp. 23–39); essendo rimasto un solo elemento l'algoritmo termina (p. 40).

![[10-heap-heapsort-p23-heapsort-inizio.png]]

| $i$ | Scambio | Dopo Max-Heapify su $A[1]$ (barra = parte ordinata) |
|---|---|---|
| 10 | 16 con 1 | $\langle 14, 8, 10, 4, 7, 9, 3, 2, 1 \mid 16 \rangle$ |
| 9 | 14 con 1 | $\langle 10, 8, 9, 4, 7, 1, 3, 2 \mid 14, 16 \rangle$ |
| 8 | 10 con 2 | $\langle 9, 8, 3, 4, 7, 1, 2 \mid 10, 14, 16 \rangle$ |
| 7 | 9 con 2 | $\langle 8, 7, 3, 4, 2, 1 \mid 9, 10, 14, 16 \rangle$ |
| 6 | 8 con 1 | $\langle 7, 4, 3, 1, 2 \mid 8, 9, 10, 14, 16 \rangle$ |
| 5 | 7 con 2 | $\langle 4, 2, 3, 1 \mid 7, 8, 9, 10, 14, 16 \rangle$ |
| 4 | 4 con 1 | $\langle 3, 2, 1 \mid 4, 7, 8, 9, 10, 14, 16 \rangle$ |
| 3 | 3 con 1 | $\langle 2, 1 \mid 3, 4, 7, 8, 9, 10, 14, 16 \rangle$ |
| 2 | 2 con 1 | $\langle 1 \mid 2, 3, 4, 7, 8, 9, 10, 14, 16 \rangle$ |

```
Heap-Sort (A)
Build-Max-Heap (A)
for i ← length[A] downto 2
    do exchange A[1] ↔ A[i]
       heap-size[A] ← heap-size[A] - 1
       Max-Heapify (A,1)
```

**Tempo di esecuzione:** $O(n \lg n)$. Build-Max-Heap impiega $O(n)$; ci sono $n - 1$ invocazioni di Max-Heapify, ciascuna di costo $O(\lg n)$.

### Code a priorità con un heap · [[10 - Heap - Heapsort.pdf#page=42|p. 42]]–[[10 - Heap - Heapsort.pdf#page=49|49]]

Un max-heap (min-heap) realizza in modo efficiente una coda a massima (minima) priorità: una struttura dati che mantiene un insieme $S$ di elementi e supporta
- **Insert**$(S, x)$: inserisce $x$ in $S$;
- **Maximum**$(S)$ (**Minimum**): restituisce l'elemento con la chiave più grande (piccola);
- **Extract-Max**$(S)$ (**Extract-Min**): rimuove e restituisce l'elemento con la chiave più grande (piccola);
- **Increase-Key**$(S, x, k)$ (**Decrease-Key**): incrementa (decrementa) la chiave di $x$ al valore $k$.

**Heap-Maximum** (tempo $\Theta(1)$):
```
Heap-Maximum (A)
return A[1]
```

**Heap-Extract-Max** (tempo $O(\lg n)$, una sola invocazione di Max-Heapify): l'ultimo elemento viene messo al posto della radice e si invoca Max-Heapify per ristabilire la proprietà.
```
Heap-Extract-Max (A)
if heap-size[A] < 1
    error "heap empty"
max ← A[1]
A[1] ← A[heap-size[A]]
heap-size[A] ← heap-size[A] - 1
Max-Heapify (A,1)
return max
```

**Heap-Increase-Key** (tempo $O(\lg n)$, $O(\lg n)$ scambi): si fa risalire l'elemento di cui si cambia la chiave in direzione della radice fino a trovare la giusta collocazione. Esempio (pp. 45–47): nell'heap $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$ la chiave 4 diventa 15 e viene scambiata con il padre 8.
```
Heap-Increase-Key (A,i,key)
if key < A[i]
    error "new key is smaller"
A[i] ← key
while i > 1 and A[Parent(i)] < A[i]
    exchange A[i] ↔ A[Parent(i)]
    i ← Parent(i)
```

![[10-heap-heapsort-p46-increase-key-chiave.png]]

**Max-Heap-Insert** (tempo $O(\lg n)$, una sola invocazione di Heap-Increase-Key): il nuovo elemento viene messo dopo l'ultimo con valore $-\infty$, poi Heap-Increase-Key imposta la chiave.
```
Max-Heap-Insert (A,key)
heap-size[A] ← heap-size[A] + 1
A[heap-size[A]] ← -∞
Heap-Increase-Key (A,heap-size[A],key)
```

### Heap-Sort da zero · [[10 - Heap - Heapsort.pdf#page=50|p. 50]]

Esercizio: ordinare con Heap-Sort, partendo da zero, l'array $\langle 6, 5, 3, 1, 8, 7, 2, 4 \rangle$.

![[10-heap-heapsort-p50-heapsort-da-zero.png]]

*Approfondimenti nel wiki: [[heap]], [[max-heapify]], [[build-max-heap]], [[heapsort]], [[heap-extract-max]], [[heap-increase-key]], [[max-heap-insert]], [[tracce-su-heap]]*

## Lezione 11 — Alberi rosso-neri

*Fonte: 11 . Alberi rosso-neri.pdf (48 pagine di slide).*

### Perché un heap non basta · [[11 . Alberi rosso-neri.pdf#page=2|p. 2]]–[[11 . Alberi rosso-neri.pdf#page=7|7]]

- Un max-heap garantisce altezza logaritmica $h = \Theta(\log n)$ e permette di accedere al massimo, nella radice, in $O(1)$.
- Non mantiene però l'ordinamento delle chiavi tipico di un BST: non vale la proprietà «sinistra < nodo < destra». Per cercare una chiave arbitraria bisogna, nel caso peggiore, esaminare tutti i nodi: $O(n)$.
- Esempio: cercare la chiave 30. Dal confronto con la radice non si può scegliere un solo sottoalbero: la chiave potrebbe trovarsi sia nel sinistro sia nel destro. Complessità della ricerca: $O(n)$. Un heap risolve il problema dell'altezza ma non permette ricerche efficienti di chiavi arbitrarie.

![[11-alberi-rosso-neri-p3-heap-ricerca.png]]

- Un albero binario di ricerca (BST) permette di cercare, inserire ed eliminare una chiave in tempo proporzionale all'altezza $h$ dell'albero.
- Tuttavia, se le chiavi vengono inserite in ordine (1, 2, 3, …) il BST può degenerare in una lista concatenata: l'altezza diventa $\Theta(n)$ e le operazioni richiedono $O(n)$ nel caso peggiore.
- Si possono «fondere» le idee di un BST e di un heap per ottenere una struttura dati che conservi l'ordinamento del BST ma garantisca altezza logaritmica anche nel caso peggiore?

### Alberi rosso-neri: a cosa servono · [[11 . Alberi rosso-neri.pdf#page=8|p. 8]], [[11 . Alberi rosso-neri.pdf#page=9|9]]

Si usano perché risolvono un problema concreto: mantenere un insieme di chiavi ordinato su cui si fanno inserimenti, cancellazioni e ricerche in modo
- veloce, tempo $O(\log n)$;
- garantito nel caso pessimo (non solo «in media»);
- con un'implementazione facile da scrivere.

In un normale BST la proprietà è «a sinistra <, a destra >» e le operazioni (search, insert, delete) percorrono un cammino dalla radice a una foglia, con costo circa l'altezza. Se si inseriscono chiavi già ordinate (1, 2, 3, 4, 5, …) l'albero diventa una lista, $h = n$, e i tempi diventano $O(n)$ invece di $O(\log n)$: i BST «puri» non garantiscono buone prestazioni nel caso pessimo.

### Definizione · [[11 . Alberi rosso-neri.pdf#page=10|p. 10]]–[[11 . Alberi rosso-neri.pdf#page=13|13]]

Gli **alberi rosso-neri** sono alberi di ricerca in cui ogni nodo ha un attributo addizionale $color$, che può valere rosso o nero. I puntatori a NIL sono sostituiti da **nodi foglia esterni**. Devono valere:
1. ogni nodo è o rosso o nero;
2. la radice è nera;
3. ogni nodo foglia esterno (NIL) è nero;
4. se un nodo è rosso, entrambi i figli sono neri;
5. per ogni nodo, tutti i percorsi dal nodo alle foglie contengono lo stesso numero di nodi neri.

Gli alberi rosso-neri garantiscono che nessun percorso dalla radice a una foglia è lungo più del doppio di un altro percorso.

![[11-alberi-rosso-neri-p11-esempio-albero.png]]
*Un albero rosso-nero con le foglie NIL.*

Nell'implementazione c'è una **unica sentinella** $nil[T]$, di colore nero (gli altri attributi sono indifferenti). Per comodità di visualizzazione la sentinella si omette nelle figure.

### Black-height · [[11 . Alberi rosso-neri.pdf#page=14|p. 14]]

La **black-height** $bh(x)$ di un nodo $x$ è il numero di nodi neri lungo un qualunque percorso da $x$ a una foglia. Dal conteggio è escluso $x$ ed è incluso il nodo foglia esterno. La black-height di un albero rosso-nero è la black-height della radice. È una misura parziale (solo i neri), mentre l'altezza conta tutti i nodi: in un albero rosso-nero l'altezza è al massimo il doppio della black-height della radice, ma in generale non sono uguali.

$$
bh(x) \le h(x) \le 2 \cdot bh(x)
$$

### Altezza di un albero rosso-nero · [[11 . Alberi rosso-neri.pdf#page=15|p. 15]], [[11 . Alberi rosso-neri.pdf#page=16|16]]

**Teorema.** Un albero rosso-nero con $n$ nodi interni ha altezza al più $2\lg(n+1)$.

Si dimostra prima che un sottoalbero con radice in un nodo $x$ contiene almeno $2^{bh(x)} - 1$ nodi interni, per induzione sull'altezza di $x$:
- *Altezza 0:* è un nodo foglia esterno e la tesi è vera perché $2^{bh(x)} - 1 = 2^0 - 1 = 0$ e il sottoalbero con radice in una foglia esterna non contiene nodi interni.
- *Passo induttivo:* si consideri un nodo interno $x$ con altezza $> 0$ e due figli. Ciascun figlio ha black-height $bh(x)$ se è rosso, $bh(x) - 1$ se è nero. Dato che l'altezza dei figli è minore di quella di $x$, si applica l'ipotesi induttiva: ogni figlio ha almeno $2^{bh(x)-1} - 1$ nodi interni. Quindi $x$ ha almeno $\left(2^{bh(x)-1} - 1\right) + \left(2^{bh(x)-1} - 1\right) + 1 = 2^{bh(x)} - 1$ nodi interni.

Dimostrazione del teorema:
- per la proprietà 4, almeno la metà dei nodi su ogni percorso dalla radice a una foglia, escludendo la radice, sono neri;
- quindi la black-height $bh$ della radice deve essere almeno $h/2$, dove $h$ è l'altezza dell'albero ($h \le 2\,bh$);
- il numero di nodi interni $n$ è almeno $2^{h/2} - 1$:

$$
n \ge 2^{bh} - 1 \ge 2^{h/2} - 1 \iff \lg(n+1) \ge \frac{h}{2} \iff h \le 2\lg(n+1)
$$

La tesi è dimostrata.

### Navigazione e modifica · [[11 . Alberi rosso-neri.pdf#page=17|p. 17]]

Le query Minimum, Maximum, Successor e Predecessor richiedono un tempo $O(\lg n)$ su un albero rosso-nero. Insert e Delete vanno invece opportunamente riviste per preservare le proprietà dell'albero.

### Rotazioni · [[11 . Alberi rosso-neri.pdf#page=18|p. 18]]–[[11 . Alberi rosso-neri.pdf#page=20|20]]

Per preservare le proprietà di un albero rosso-nero vengono effettuate delle **rotazioni**, che preservano le proprietà di un albero di ricerca.
- **Rotazione a sinistra** (sul nodo $x$): presuppone che il figlio di destra non sia NIL. Nella figura $A = x$, con figlio destro $B$; $\alpha$ è il sottoalbero sinistro di $A$, $\beta$ e $\gamma$ quelli di $B$.
  1. $\beta$ diventa figlio di destra di $A$;
  2. il padre di $A$ diventa $B$ (il padre di $A$ diventa il padre di $B$);
  3. $A$ diventa il figlio di sinistra di $B$.
- In maniera equivalente si definisce la rotazione a destra.

```
Left-Rotate (T,x)
y ← right[x]
// operazione 1.
right[x] ← left[y]
if left[y] ≠ nil[T]
    then p[left[y]] ← x
// operazione 2.
p[y] ← p[x]
if p[x] = nil[T]
    then root[T] ← y
    else if x = left[p[x]]
        then left[p[x]] ← y
        else right[p[x]] ← y
// operazione 3.
left[y] ← x
p[x] ← y
```

Il tempo di esecuzione è $O(1)$.

![[11-alberi-rosso-neri-p20-rotazioni-esempio.png]]
*Left-Rotate (T,x) con $x = 11$ porta l'albero in alto in quello in basso; Right-Rotate (T,y) con $y = 18$ fa il percorso inverso.*

### Inserimento di un nodo · [[11 . Alberi rosso-neri.pdf#page=21|p. 21]]–[[11 . Alberi rosso-neri.pdf#page=23|23]]

**Strategia.**
- Si inserisce il nodo come in un normale albero di ricerca, con RB-Insert, una versione (leggermente) modificata di Tree-Insert.
- Si colora il nodo di rosso.
- Si invoca una funzione ausiliaria (RB-Insert-Fixup) per ripristinare le proprietà degli alberi rosso-neri.
- Il tempo di esecuzione, vedremo, è $O(\lg n)$.

```
RB-Insert (T,z)
y ← nil[T]
x ← root[T]
while x ≠ nil[T]
    do y ← x
       if key[z] < key[x]
           then x ← left[x]
           else x ← right[x]
p[z] ← y
if y = nil[T]
    then root[T] ← z        // albero vuoto
    else if key[z] < key[y]
        then left[y] ← z
        else right[y] ← z
left[z] ← nil[T]
right[z] ← nil[T]
color[z] ← RED
RB-Insert-Fixup (T,z)
```

Il tempo di esecuzione di RB-Insert è $O(h)$. Nella slide l'albero di esempio ha $z = 19$ da inserire in un albero con radice 15.

**Quali proprietà possono essere invalidate dall'inserimento?**
1. ogni nodo è rosso o nero: vale;
2. la radice è nera: non vale se l'albero era vuoto;
3. ogni foglia NIL è nera: vale;
4. se un nodo è rosso entrambi i figli sono neri: non vale se il padre di $z$ è rosso;
5. stessa black-height: vale.

### RB-Insert-Fixup: invariante · [[11 . Alberi rosso-neri.pdf#page=24|p. 24]]–[[11 . Alberi rosso-neri.pdf#page=26|26]]

RB-Insert-Fixup è costituito da un ciclo `while`, eseguito finché il padre di $z$ resta rosso. È costruito per mantenere il seguente invariante. All'inizio di ogni iterazione:
- a) il nodo $z$ è rosso;
- b) se $p[z]$ è la radice, allora $p[z]$ è nero;
- c) in tutto l'albero c'è al massimo una violazione delle proprietà degli alberi rosso-neri, ed è o di tipo 2 o di tipo 4:
  1. se è di tipo 2, si presenta perché $z$ è la radice ed è rosso;
  2. se è di tipo 4, si presenta perché sia $z$ sia $p[z]$ sono rossi.

**Prima della prima iterazione** ($z$ è il nodo appena inserito):
- a) vera perché il nodo inserito è rosso;
- b) se $p[z]$ è la radice, non è stata modificata da RB-Insert e quindi è rimasta nera;
- c) le proprietà 1, 3 e 5 non vengono violate da RB-Insert: se l'albero era vuoto e il nodo inserito è la nuova radice c'è una violazione di tipo 2 e nessuna di tipo 4 (foglie nere); se l'albero non era vuoto e $z$ viene inserito come figlio di un nodo rosso c'è una violazione di tipo 4 e nessuna di tipo 2.

**Il ciclo termina** quando il padre di $z$ è nero: l'invariante (c.2) garantisce che non ci sono violazioni di tipo 4; in base a c.1) ci potrebbe essere una violazione di tipo 2 dove $z$ è la radice ed è rosso, ed è sufficiente ricolorare di nero la radice. Se $z$ è il primo nodo inserito, il ciclo termina subito: il padre di $z$ è la sentinella, che è un nodo nero.

### Il corpo del ciclo · [[11 . Alberi rosso-neri.pdf#page=27|p. 27]]–[[11 . Alberi rosso-neri.pdf#page=36|36]]

Per preservare l'invariante, se si è entrati nel ciclo:
- il padre di $z$ ($p[z]$) è rosso;
- il nonno di $z$ ($p[p[z]]$) esiste ed è un nodo interno: dato che $p[z]$ è rosso, per b) non può essere la radice, e quindi il padre di $p[z]$ non è la sentinella;
- il nonno di $z$ è un nodo nero: se fosse rosso, con $p[z]$ rosso ci sarebbe una violazione di tipo 4 fra $p[z]$ e $p[p[z]]$, contrariamente a c.2);
- non ci sono violazioni di tipo 2: se ci fosse, $z$ sarebbe la radice e il padre di $z$ (la sentinella) sarebbe nero (assurdo: $p[z]$ è rosso).

Si distingue se il padre di $z$ è figlio di sinistra o di destra del nonno: i due casi sono simmetrici (si scambia left con right). Si considera il caso in cui il padre di $z$ è il figlio di sinistra. Si sa che $z$ è rosso, $p[z]$ è rosso e $p[p[z]]$ è nero; si distingue in base al colore dello zio $y$.

**Caso 1: $y$ è rosso.** $p[z]$ e $y$ diventano neri, $p[p[z]]$ diventa rosso (ricolorazione) e $z \leftarrow p[p[z]]$.

![[11-alberi-rosso-neri-p29-caso-1.png]]

Verifica dell'invariante ($z'$ è il valore di $z$ nella nuova iterazione):
- a) $z'$ è $p[p[z]]$, che è colorato di rosso;
- b) $p[z']$ non è modificato in questa iterazione, quindi se è la radice allora è nero (nessuna violazione di tipo 2 se si entra nel `while`);
- c) non si introducono violazioni di tipo 5 (né 1 e 3): se $z'$ è la radice si è risolta la violazione di tipo 4 e resta una sola violazione di tipo 2 ($z'$ è la radice ed è rosso); se $z'$ non è la radice non si è introdotta una violazione di tipo 2, e può esserci una violazione di tipo 4 fra $z'$ e $p[z']$ se $p[z']$ è rosso.

**Caso 2: $y$ è nero e $z$ è figlio di destra.** $z \leftarrow p[z]$ e Left-Rotate su $z$. Dato che $z$ e $p[z]$ sono rossi, non si viola la proprietà 5 e la black-height. Ci si riconduce al caso 3.

![[11-alberi-rosso-neri-p31-caso-2.png]]

**Caso 3: $y$ è nero e $z$ è figlio di sinistra.** $p[z]$ diventa nero, $p[p[z]]$ rosso e Right-Rotate su $p[p[z]]$; ciò preserva la proprietà 5, e il ciclo termina perché $p[z]$ è nero.

![[11-alberi-rosso-neri-p33-caso-3.png]]

```
RB-Insert-Fixup (T,z)
while color[p[z]] = RED
    do if p[z] = left[p[p[z]]]
          then y ← right[p[p[z]]]            // zio
               if color[y] = RED
                  then color[p[z]] ← BLACK
                       color[y] ← BLACK
                       color[p[p[z]]] ← RED
                       z ← p[p[z]]
                  else if z = right[p[z]]
                        then z ← p[z]
                             Left-Rotate (T,z)
                       color[p[z]] ← BLACK
                       color[p[p[z]]] ← RED
                       Right-Rotate (T,p[p[z]])
          else (stesso codice di then con right e left scambiati)
color[root[T]] ← BLACK
```

Verifica dell'invariante per i casi 2 e 3:
- a) nel caso 2 $z$ diventa $p[z]$, che è rosso, e poi non si modifica più $z$;
- b) il caso 3 colora $p[z]$ di nero;
- c) non si introducono violazioni di tipo 5 (né 1 e 3): $z$ (che è rosso) non è la radice e quindi non viola la proprietà 2; non ci sono altre violazioni di 2 perché l'unico nodo che diventa rosso diventa figlio di un nodo nero (e quindi non può essere la radice); i casi 2 e 3 correggono una violazione di 4 senza introdurne altre.

**Tempo di esecuzione di RB-Insert-Fixup: $O(\lg n)$.**
- Il ciclo si ripete solo se siamo nel caso 1, durante il quale $z$ sale di due livelli.
- Il ciclo viene ripetuto $O(\lg n)$ volte.
- Vengono eseguite al più due rotazioni.
- Il ciclo termina quando si entra nel caso 2 o 3.

### Esempio di inserimento · [[11 . Alberi rosso-neri.pdf#page=37|p. 37]]–[[11 . Alberi rosso-neri.pdf#page=41|41]]

Albero: radice 11 (nero); 2 (rosso) e 14 (nero); 1 e 7 (neri) sotto 2, 15 (rosso) sotto 14; 5 e 8 (rossi) sotto 7. Si inserisce $z = 4$ come figlio sinistro di 5.

- **Caso 1** (violazione della proprietà 4; lo zio di $z$, $y = 8$, è rosso): i nodi sono ricolorati e $z$ diventa il nonno di $z$ (il nodo 7).
- **Caso 2** (violazione della proprietà 4; lo zio $y = 14$ è nero; $z = 7$ è il figlio di destra di $p[z] = 2$): rotazione a sinistra.
- **Caso 3** (violazione della proprietà 4; lo zio $y$ è nero; $z = 2$ è il figlio di sinistra di $p[z] = 7$): rotazione a destra e ricolorazione dei nodi 7 e 11.

![[11-alberi-rosso-neri-p37-inserimento-caso-1-esempio.png]]
![[11-alberi-rosso-neri-p38-inserimento-caso-2-esempio.png]]
![[11-alberi-rosso-neri-p39-inserimento-caso-3-esempio.png]]
![[11-alberi-rosso-neri-p40-inserimento-caso-3-ricolorazione.png]]

A p. 41 è mostrata una schermata del visualizzatore «Red/Black Tree Visualization» (cs.usfca.edu, con le operazioni Insert, Delete, Find).

![[11-alberi-rosso-neri-p41-visualizzatore.png]]

### Eliminazione di un elemento · [[11 . Alberi rosso-neri.pdf#page=42|p. 42]]–[[11 . Alberi rosso-neri.pdf#page=48|48]]

La cancellazione si basa sull'algoritmo Tree-Delete dei normali BST, con alcune modifiche. Come nell'inserimento, anche nella cancellazione può essere necessario ripristinare le proprietà rosso-nere:
- se il nodo fisicamente rimosso è rosso, le proprietà rosso-nere restano valide;
- se il nodo fisicamente rimosso è nero, si invoca RB-Delete-Fixup, che ripristina le proprietà attraverso eventuali ricolorazioni e rotazioni.

La cancellazione segue inizialmente le stesse regole di un BST: si distinguono i casi in cui il nodo da eliminare ha **zero, uno o due figli**. Le proprietà degli alberi rosso-neri permettono però alcune osservazioni:
- un nodo rosso può essere una foglia oppure avere due figli, necessariamente neri;
- non può avere un solo figlio, altrimenti sarebbe violata la proprietà 5 (black-height);
- se il nodo da eliminare ha due figli, viene individuato il suo successore, che ha al massimo un figlio.

Pertanto il nodo fisicamente rimosso ha sempre al massimo un figlio. I casi effettivi da gestire sono tre:
1. si elimina una **foglia rossa**: l'albero resta rosso-nero (non cambia la black-height, non si creano nodi rossi consecutivi, la radice resta nera);
2. si elimina un **nodo nero con un unico figlio rosso**: il figlio prende il suo posto e viene colorato di nero; le proprietà sono preservate;
3. si elimina una **foglia nera**: la black-height diminuisce lungo alcuni cammini, occorre intervenire con RB-Delete-Fixup per ripristinare le proprietà.

![[11-alberi-rosso-neri-p45-cancellazione-foglia.png]]
*Caso I — eliminare una foglia: albero rosso-nero iniziale, si sceglie $z = 19$.*

![[11-alberi-rosso-neri-p46-cancellazione-un-figlio.png]]
*Caso II — un solo figlio: si sceglie $z = 20$ (nero).*

![[11-alberi-rosso-neri-p47-cancellazione-due-figli.png]]
*Caso III — due figli: si sceglie $z = 18$.*

RB-Delete-Fixup è diverso da RB-Insert-Fixup: RB-Insert-Fixup corregge principalmente la presenza di due nodi rossi consecutivi, RB-Delete-Fixup corregge principalmente lo squilibrio della black-height provocato dall'eliminazione di un nodo nero. Entrambi utilizzano rotazioni e ricolorazioni, ma gestiscono situazioni differenti.

**Complessità.** La ricerca e l'eliminazione strutturale richiedono $O(h)$; anche RB-Delete-Fixup richiede $O(h)$ nel caso peggiore; poiché un albero rosso-nero ha altezza $h = O(\log n)$, l'intera cancellazione richiede $O(\log n)$.

*Approfondimenti nel wiki: [[albero-rosso-nero]], [[left-rotate]], [[rb-insert]], [[rb-delete]]*

## Lezione 12 — Alberi auto-aggiustanti

*Fonte: 12 - Alberi auto-aggiustanti.pdf (16 pagine di slide).*

### Alberi auto-aggiustanti (splay trees) · [[12 - Alberi auto-aggiustanti.pdf#page=2|p. 2]]

- Gli **alberi auto-aggiustanti** (splay trees) sono alberi binari di ricerca che non impongono ulteriori vincoli sulla disposizione degli elementi.
- L'idea è che ogni volta che si accede a un elemento dell'albero, l'albero viene riaggiustato in modo che tale elemento venga posto nella radice.
- Utilizzando delle rotazioni per riaggiustare l'albero, si ottengono **tempi di esecuzione ammortizzati** di tipo logaritmico su una sequenza di $n$ operazioni.
- Vantaggio pratico: gli elementi cui si accede più di frequente si trovano nelle vicinanze della radice e quindi si accede più velocemente ad essi.
- È una struttura per insiemi ordinati (come un BST) che si **adatta automaticamente al pattern di accesso**, con **costo ammortizzato** $O(\log n)$ per operazione, senza memorizzare informazioni di bilanciamento (ad esempio i colori).

### L'operazione splay · [[12 - Alberi auto-aggiustanti.pdf#page=3|p. 3]]–[[12 - Alberi auto-aggiustanti.pdf#page=5|5]]

L'operazione splay su un nodo $x$ consiste nell'effettuare una **serie di rotazioni** che portano $x$ nella radice dell'albero.

- **Caso I: $x$ è figlio della radice.** Rotazione sul padre di $x$ (sulla radice): Left-Rotate $(T,y)$.

![[12-alberi-auto-aggiustanti-p3-splay-caso-1.png]]

- **Caso II: $x$ ha un nonno e sia $x$ sia il padre di $x$ sono figli di sinistra (o di destra) del proprio genitore.** Rotazione sul nonno di $x$ (Right-Rotate $(T,z)$), poi rotazione sul padre di $x$ (Right-Rotate $(T,y)$).

![[12-alberi-auto-aggiustanti-p4-splay-caso-2.png]]

- **Caso III: $x$ ha un nonno, $x$ è figlio di sinistra (destra) e il padre di $x$ è figlio di destra (sinistra).** Rotazione sul padre di $x$ (Right-Rotate $(T,y)$), poi rotazione sul nuovo padre di $x$ (era il nonno di $x$: Left-Rotate $(T,z)$).

![[12-alberi-auto-aggiustanti-p5-splay-caso-3.png]]

### Ricerca, inserimento ed eliminazione · [[12 - Alberi auto-aggiustanti.pdf#page=6|p. 6]]–[[12 - Alberi auto-aggiustanti.pdf#page=9|9]]

**Ricerca.** Dopo aver cercato una chiave, si esegue un'operazione splay sul nodo che contiene la chiave o sulla foglia su cui la ricerca è terminata. Se l'albero è vuoto non si fa nulla.

```
Splay-Tree-Search (T,k)
x ← root[T]
while x ≠ NIL and key[x] ≠ k
    do y ← x
       if k < key[x]
           then x ← left[x]
           else x ← right[x]
if x ≠ NIL
    then Splay (T,x)
    else if root[T] ≠ NIL
        then Splay (T,y)
return x
```

**Inserimento.** Dopo aver inserito un elemento, si esegue un'operazione splay sul nodo che contiene il nuovo elemento inserito. Nell'esempio l'albero (radice 15; 6 e 18; 3, 7, 17 e 20; 2, 4 e 13) riceve il nodo 19.

```
Splay-Tree-Insert (T,z)
Tree-Insert (z)
Splay (T,z)
```

**Eliminazione.** Dopo aver eliminato un nodo $z$, si esegue un'operazione splay sul nodo che era il padre di $z$ prima dell'eliminazione. Se il padre di $z$ è NIL ($z$ è la radice) non si fa nulla.

```
Splay-Tree-Delete (T,z)
Tree-Delete (z)
if p[z] ≠ NIL
    then Splay (T,p[z])
```

**Costo?** Per calcolare il costo reale delle operazioni si usa un approccio noto come analisi ammortizzata (lo vedremo nelle prossime lezioni).

### Alberi rosso-neri contro splay · [[12 - Alberi auto-aggiustanti.pdf#page=10|p. 10]]–[[12 - Alberi auto-aggiustanti.pdf#page=12|12]]

La differenza non è l'ordinamento BST: è il modo in cui si ottengono buone prestazioni.
- **Albero rosso-nero:** mantiene un'altezza logaritmica anche se cambiano le chiavi cercate.
- **Splay tree:** si riorganizza a ogni accesso, portando il nodo cercato alla radice.
- Idea chiave: lo splay sfrutta la storia degli accessi, non impone un bilanciamento permanente.

![[12-alberi-auto-aggiustanti-p10-rosso-nero-vs-splay.png]]

**Esempio sul costo.** Stesso albero della lezione: 17 viene cercato e portato in radice. Prima, 17 è interno all'albero; dopo Splay(17), 17 è la radice (zig-zag: due rotazioni che conservano l'ordinamento delle chiavi). Se 17 viene cercato di nuovo (senza accessi intermedi): $O(1)$.

![[12-alberi-auto-aggiustanti-p11-splay-17-esempio.png]]

### Working set (cenni) · [[12 - Alberi auto-aggiustanti.pdf#page=13|p. 13]]

La struttura si adatta alla **località temporale**: una chiave usata di recente può costare meno da ritrovare, anche quando l'albero contiene molte chiavi. Nella sequenza di accessi A → B → C → A → A → D → A, prima dell'ultimo A è stato consultato un solo elemento distinto: D. Con $t_i$ = numero di chiavi distinte consultate dall'accesso precedente alla stessa chiave, il contributo logaritmico nel limite ammortizzato è $O(1 + \log(t_i + 1))$. È un limite per sequenze, **non** il tempo effettivo garantito per ogni singolo accesso.

### Impatto della splay · [[12 - Alberi auto-aggiustanti.pdf#page=14|p. 14]]

La forma dell'albero cambia, ma l'ordine delle chiavi resta identico. Una rotazione a sinistra su $x$ (figli $A$ e $y$; $y$ ha figli $B$ e $C$) porta $y$ in alto, con $x$ a sinistra (figli $A$ e $B$) e $C$ a destra. $B$ cambia padre ma contiene sempre chiavi fra $x$ e $y$:

$$
A < x < B < y < C
$$

La visita in ordine è invariata: per questo ogni rotazione conserva la proprietà BST.

![[12-alberi-auto-aggiustanti-p14-impatto-splay.png]]

### Splay tree contro albero rosso-nero · [[12 - Alberi auto-aggiustanti.pdf#page=15|p. 15]], [[12 - Alberi auto-aggiustanti.pdf#page=16|16]]

Non esiste un vincitore assoluto: dipende dalle richieste dell'applicazione.
- **Splay tree:** accessi ripetuti alle stesse chiavi; accessi con forte località temporale; nessun colore o bilanciamento da memorizzare.
- **Albero rosso-nero:** serve un limite per ogni ricerca; latenza prevedibile $O(\log n)$; le ricerche non devono modificare l'albero.
- Rosso-nero: bilanciamento garantito. Splay: riorganizzazione adattiva alla storia degli accessi.

| Caratteristica | BST ordinario | Albero rosso-nero | Splay tree |
|---|---|---|---|
| Rispetta l'ordinamento BST | Sì | Sì | Sì |
| Bilanciamento garantito | No | Sì | No |
| Si riorganizza dopo le ricerche | No | No | Sì |
| Altezza nel caso peggiore | $O(n)$ | $O(\log n)$ | $O(n)$ |
| Ricerca: costo ammortizzato | $O(n)$ | $O(\log n)$ | $O(\log n)$ |

*Approfondimenti nel wiki: [[splay-tree]], [[splay]], [[splay-tree-operazioni]]*

## Lezione 13 — Algoritmi di visita di un grafo

*Fonte: 13 - Algoritmi di visita di un grafo.pdf (53 pagine: slide, con note a mano alle p. 38 e 40; le pp. 44–53 sono slide in inglese di S. Skiena).*

### Grafi e rappresentazioni · [[13 - Algoritmi di visita di un grafo.pdf#page=2|p. 2]]–[[13 - Algoritmi di visita di un grafo.pdf#page=6|6]]

Un grafo consiste di un insieme di nodi $V$ connessi mediante un insieme di archi $E$, direzionali e non direzionali. Due rappresentazioni:
- **liste di adiacenza**, tipicamente preferite per grafi sparsi ($\lvert E \rvert \ll \lvert V \rvert^2$);
- **matrice di adiacenza**, tipicamente preferita per grafi densi o quando serve sapere velocemente se due nodi sono connessi.

Entrambe sono utilizzabili sia per grafi direzionali sia non direzionali.

**Liste di adiacenza.** Un array $Adj$ di $\lvert V \rvert$ liste, una per ciascun vertice; ogni lista $Adj[u]$ contiene i vertici $v$ tali che $(u, v) \in E$.

![[13-visite-grafi-p3-liste-di-adiacenza.png]]

- La somma delle lunghezze di tutte le liste è $\lvert E \rvert$ se $G$ è direzionale, $2\lvert E \rvert$ se $G$ è non direzionale; la memoria richiesta è in ogni caso $\Theta(V + E)$.
- Le liste possono rappresentare grafi pesati: a ogni link è associato un peso dato dalla funzione $w: E \to \mathbb{R}$; il peso $w(u, v)$ del link $(u, v)$ si può memorizzare insieme al vertice $v$ nella lista di adiacenza di $u$.
- Un potenziale svantaggio è che, per determinare se un arco $(u, v)$ è presente, bisogna effettuare una ricerca nella lista di adiacenza di $u$.

**Matrice di adiacenza.** Una matrice $A$ di dimensione $\lvert V \rvert \times \lvert V \rvert$, con $a_{ij} = 1$ se $(i, j) \in E$, 0 altrimenti.

![[13-visite-grafi-p5-matrice-di-adiacenza.png]]

- Richiede $\Theta(V^2)$ memoria, indipendentemente dal numero di archi.
- Dato che in un grafo non direzionale $(u, v)$ e $(v, u)$ rappresentano lo stesso arco, la matrice è simmetrica rispetto alla diagonale principale, $A = A^T$: si può dimezzare il consumo di memoria.
- Può rappresentare grafi pesati: $a_{ij}$ vale il peso di $(i, j)$ se l'arco esiste, altrimenti vale NIL, 0 (a seconda dei casi).
- Si preferisce in genere per grafi di piccole dimensioni e quando i grafi non sono pesati (0 o 1 consuma 1 bit).

### Visita di un grafo · [[13 - Algoritmi di visita di un grafo.pdf#page=7|p. 7]]

Una volta rappresentato un grafo, vogliamo esplorarne sistematicamente i vertici e gli archi, a partire da un nodo sorgente, evitando di visitare più volte lo stesso vertice. Due strategie fondamentali:
- **visita in ampiezza** (BFS): esplora prima i vertici più vicini alla sorgente, procedendo per livelli;
- **visita in profondità** (DFS): esplora un cammino il più possibile in profondità, tornando indietro quando non può proseguire.

Le visite permettono anche di risolvere problemi più complessi, come l'**ordinamento topologico**, che dispone i vertici di un grafo orientato aciclico (DAG) rispettando le dipendenze tra essi.

### Visita in ampiezza · [[13 - Algoritmi di visita di un grafo.pdf#page=9|p. 9]]–[[13 - Algoritmi di visita di un grafo.pdf#page=12|12]]

La visita in ampiezza (BFS, *Breadth First Search*) è un semplice algoritmo per «visitare» i nodi di un grafo. Importanti algoritmi si basano su questo approccio: l'algoritmo di Dijkstra per lo shortest path e l'algoritmo di Prim per il minimum spanning tree.
- A partire da un nodo sorgente $s$, BFS visita tutti i nodi adiacenti di un nodo e poi procede a visitare allo stesso modo gli adiacenti.
- Tutti i nodi che distano $k$ dalla sorgente vengono visitati prima del primo nodo che dista $k+1$.
- BFS produce un albero con radice in $s$ che contiene tutti i nodi raggiungibili da $s$.
- Il percorso da $s$ a $v$ nell'albero è il più breve da $s$ a $v$ nel grafo.

BFS opera su grafi direzionali e non. Per tenere traccia dei nodi esplorati utilizza i colori: **bianco** se non è ancora stato visitato; **grigio** se è stato visitato ma non tutti i suoi vicini sono stati visitati; **nero** se è stato visitato insieme a tutti i suoi vicini. Se il nodo $v$ viene visitato in quanto vicino di $u$, allora $u$ è il predecessore di $v$; ogni nodo viene visitato al più una volta e quindi ha al più un predecessore.

![[13-visite-grafi-p11-bfs-grafo.png]]
*Grafo non orientato (vertici $r, s, t, u, v, w, x, y$) per la visita in ampiezza; a destra l'albero BFS, con i livelli $d = 0, 1, 2, 3$, ancora vuoto.*

L'albero che si ottiene dipende dall'ordine con cui si visitano i vicini, ma la lunghezza dei percorsi minimi non cambia.

```
BFS (G,s)
for each vertex u ∈ V[G] - {s}
    do color[u] ← WHITE
       d[u] ← ∞
       π[u] ← NIL
color[s] ← GRAY
d[s] ← 0
π[s] ← NIL
Q ← Ø
Enqueue (Q,s)
while Q ≠ Ø
    do u ← Dequeue (Q)
       for each v ∈ Adj[u]
           do if color[v] = WHITE
               then color[v] ← GRAY
                    d[v] ← d[u] + 1
                    π[v] ← u
                    Enqueue (Q,v)
       color[u] ← BLACK
```

Assume una rappresentazione mediante liste di adiacenza. Il predecessore $\pi$ di un nodo è NIL se il nodo è la sorgente o non è stato raggiunto (ancora). **Invariante:** all'inizio di ogni iterazione del ciclo `while`, $Q$ contiene tutti i nodi grigi; è vero prima della prima iterazione, e una iterazione conserva questa proprietà.

### Visita in ampiezza: costo · [[13 - Algoritmi di visita di un grafo.pdf#page=13|p. 13]], [[13 - Algoritmi di visita di un grafo.pdf#page=14|14]]

Si effettua un'**analisi aggregata** per determinare il tempo di esecuzione.
- L'overhead legato all'inizializzazione è $O(V)$.
- Il tempo legato alle operazioni di accodamento e deaccodamento è $O(V)$: `Enqueue` e `Dequeue` richiedono $O(1)$; ogni nodo viene accodato al più una volta (un nodo viene accodato solo se è bianco e, quando viene accodato, viene colorato di grigio; un nodo non viene mai ricolorato bianco); un nodo in coda può essere deaccodato al più una volta.
- Il tempo legato all'analisi delle liste di adiacenza è $O(E)$: la lista di adiacenza di un nodo è analizzata solo quando il nodo viene deaccodato; la somma delle lunghezze di tutte le liste è $\Theta(E)$.

Il tempo di esecuzione di BFS è $O(V + E)$.

### Visita in ampiezza: percorso minimo · [[13 - Algoritmi di visita di un grafo.pdf#page=15|p. 15]]–[[13 - Algoritmi di visita di un grafo.pdf#page=19|19]]

Si definisce la **distanza minima** $\delta(s, v)$ tra $s$ e $v$ come il numero minimo di archi di qualunque percorso tra $s$ e $v$; se non c'è un percorso, $\delta(s, v) = \infty$. Un percorso tra $s$ e $v$ di lunghezza minima è uno *shortest path* da $s$ a $v$.

**Lemma 1.** Per ogni arco $(u, v) \in E$ si ha $\delta(s, v) \le \delta(s, u) + 1$. Se $u$ è raggiungibile da $s$, lo è anche $v$: lo shortest path da $s$ a $v$ non può essere più lungo dello shortest path da $s$ a $u$ più l'arco $(u, v)$. Se $u$ non è raggiungibile, $\delta(s, u) = \infty$ e la tesi è vera.

**Lemma 2.** Dopo aver eseguito BFS su $G$ a partire da $s$, per ogni vertice $v$ si ha $d[v] \ge \delta(s, v)$. Per induzione sul numero di operazioni di Enqueue.
- *Caso base:* dopo che $s$ è stato accodato, la tesi è vera per $s$ ($d[s] = \delta(s, s) = 0$) e per gli altri nodi ($d[v] = \infty \ge \delta(s, v)$).
- *Passo induttivo:* sia $v$ un vertice bianco scoperto durante la ricerca dei vicini di $u$. L'ipotesi induttiva è $d[u] \ge \delta(s, u)$. La distanza assegnata a $v$ è $d[v] = d[u] + 1 \ge \delta(s, u) + 1 \ge \delta(s, v)$ (lemma 1). Il vertice $v$ viene colorato di grigio e quindi non viene più riaccodato, per cui la sua distanza non cambia più.

**Lemma 3.** Durante l'esecuzione di BFS, se la coda $Q$ contiene i vertici $\langle v_1, v_2, \dots, v_r \rangle$ ($v_1$ testa, $v_r$ coda), allora per ogni $i = 1, \dots, r$ vale $d[v_i] \le d[v_{i+1}]$ e $d[v_r] \le d[v_1] + 1$. Per induzione sul numero di operazioni sulla coda.
- *Caso base:* inizialmente la coda contiene $s$ e la tesi vale.
- *Passo induttivo 1) si estrae la testa $v_1$:* la nuova testa diventa $v_2$; se la coda è vuota la tesi è banale. L'ipotesi induttiva è $d[v_1] \le d[v_2]$ e $d[v_r] \le d[v_1] + 1 \Rightarrow d[v_r] \le d[v_2] + 1$ (vera anche per $v_2$).
- *Passo induttivo 2) si accoda un nodo:* questo diventa $v_{r+1}$ e il nodo $u$ a partire dal quale è stato scoperto è già stato estratto. Per ipotesi $d[u] \le d[v_1] \Rightarrow d[v_{r+1}] = d[u] + 1 \le d[v_1] + 1$ e $d[v_r] \le d[u] + 1 = d[v_{r+1}]$; le altre relazioni restano immutate.

**Corollario 1.** Dal lemma 3 e dal fatto che la distanza di un nodo è assegnata al più una volta: se il vertice $v_i$ è accodato prima di $v_j$, allora $d[v_i] \le d[v_j]$.

**Teorema (completezza).** BFS scopre tutti i nodi raggiungibili dalla sorgente $s$ e al termine si ha $d[v] = \delta(s, v)$ per tutti i vertici $v$. Per ogni vertice $v$ raggiungibile da $s$, uno shortest path da $s$ a $v$ è uno shortest path da $s$ a $\pi[v]$ seguito dall'arco $(\pi[v], v)$.
- Si assume per assurdo che qualche vertice riceva una distanza diversa da quella minima.
- Tra tali vertici, sia $v$ quello con la più piccola distanza minima (chiaramente $v$ non può essere $s$).
- Per il lemma 2, $d[v] \ge \delta(s, v)$, quindi $d[v] > \delta(s, v)$ e $v$ deve essere raggiungibile da $s$ (altrimenti $\delta(s, v) = \infty \ge d[v]$).
- Sia $u$ il nodo che precede $v$ lungo uno shortest path da $s$ a $v$, quindi $\delta(s, v) = \delta(s, u) + 1$.

(La slide si interrompe a questo punto.)

### Visita in ampiezza: albero di visita · [[13 - Algoritmi di visita di un grafo.pdf#page=20|p. 20]], [[13 - Algoritmi di visita di un grafo.pdf#page=21|21]]

BFS costruisce un albero, detto *breadth-first tree*. Formalmente si definisce il **predecessor subgraph** di $G$: $G_\pi = (V_\pi, E_\pi)$ con $V_\pi = \{v \in V : \pi[v] \ne \text{NIL}\} \cup \{s\}$ e $E_\pi = \{(\pi[v], v) : v \in V_\pi - \{s\}\}$ (tree edges). Un predecessor subgraph è un albero perché, dalla definizione di $E_\pi$, $\lvert E_\pi \rvert = \lvert V_\pi \rvert - 1$, condizione necessaria e sufficiente per un albero. È un breadth-first tree se $V_\pi$ consiste dei vertici raggiungibili da $s$ e, per ogni $v \in V_\pi$, esiste un unico percorso semplice da $s$ a $v$ in $G_\pi$ che è anche lo shortest path da $s$ a $v$ in $G$.

**Lemma 4.** Il predecessor subgraph restituito da BFS è un breadth-first tree. BFS pone $\pi[v] = u$ se e solo se $(u, v) \in E$ e $v$ è raggiungibile da $s$; quindi $V_\pi$ consiste dei vertici raggiungibili da $s$. Dato che il predecessor subgraph è un albero, contiene un unico percorso da $s$ a ciascun vertice; applicando il teorema precedente, si conclude che ogni percorso è uno shortest path.

### Visita in ampiezza: stampa · [[13 - Algoritmi di visita di un grafo.pdf#page=22|p. 22]], [[13 - Algoritmi di visita di un grafo.pdf#page=23|23]]

Stampa i vertici lungo uno shortest path da $s$ a $y$, assumendo di aver eseguito BFS in precedenza. Il tempo di esecuzione è lineare nel numero di vertici sul percorso.

```
Print-Path (G,s,v)
if v = s
    then print s
    else if π[v] = NIL
        then print "no path from s to v exists"
        else Print-Path (G,s,π[v])
             print v
```

### Visita in profondità · [[13 - Algoritmi di visita di un grafo.pdf#page=25|p. 25]]–[[13 - Algoritmi di visita di un grafo.pdf#page=28|28]]

La **depth-first search** (DFS) esplora i vicini del nodo scoperto più di recente che ha ancora vicini non esplorati: la visita procede «in profondità». Se ci sono nodi non esplorati, la ricerca riparte da uno di essi; tutti i vertici sono esplorati. DFS tiene traccia dei predecessori di un nodo (come BFS). Il predecessor subgraph può essere composto da più alberi, per questo è definito in maniera leggermente diversa: $G_\pi = (V, E_\pi)$ con $E_\pi = \{(\pi[v], v) : v \in V \text{ e } \pi[v] \ne \text{NIL}\}$ (tree edges). Il predecessor subgraph forma una **depth-first forest** composta di diversi **depth-first tree**.

Come in BFS, i nodi sono colorati di bianco, grigio e nero: ciò assicura che ogni vertice finisca in un solo depth-first tree e quindi che gli alberi siano disgiunti. DFS marca ciascun nodo con due **timestamp**:
- $d[v]$ segna l'istante di tempo in cui $v$ è scoperto (e colorato di grigio);
- $f[v]$ segna l'istante di tempo in cui termina la ricerca dei vicini di $v$ (che viene colorato di nero).

I timestamp sono interi compresi tra 1 e $2\lvert V \rvert$; per ogni nodo c'è un istante di scoperta e uno di completamento; per ogni vertice $u$, $d[u] < f[u]$.

![[13-visite-grafi-p28-dfs-codice.png]]
*Esempio di DFS con i tempi $d/f$ (archi dell'albero in blu) e pseudocodice. Anche per DFS i risultati della ricerca variano a seconda dell'ordine con cui si esaminano i nodi.*

```
DFS (G)
for each vertex u ∈ V[G]
    do color[u] ← WHITE
       π[u] ← NIL
time ← 0
for each vertex u ∈ V[G]
    do if color[u] = WHITE
        then DFS-Visit (u)

DFS-Visit (u)
color[u] ← GRAY
time ← time + 1
d[u] ← time
for each v ∈ Adj[u]
    do if color[v] = WHITE
        then π[v] ← u
             DFS-Visit (v)
color[u] ← BLACK
f[u] ← time ← time + 1
```

### Visita in profondità: costo · [[13 - Algoritmi di visita di un grafo.pdf#page=29|p. 29]]

- I cicli `for` di DFS impiegano $\Theta(V)$, esclusa la chiamata a DFS-Visit.
- DFS-Visit viene chiamata una volta per ciascun nodo: è chiamata solo su vertici bianchi e la prima cosa che fa è colorare il vertice di grigio.
- Il tempo impiegato dal ciclo `for` di DFS-Visit su tutte le invocazioni è $\Theta(E)$.
- Il tempo complessivo è $O(V + E)$.

### Struttura a parentesi · [[13 - Algoritmi di visita di un grafo.pdf#page=30|p. 30]]–[[13 - Algoritmi di visita di un grafo.pdf#page=32|32]]

Una proprietà della DFS è che i tempi di scoperta e di terminazione dei nodi hanno una **struttura a parentesi**: scrivendo $d[u]$ come «$(u$» e $f[u]$ come «$u)$» si ottiene un'espressione corretta.

![[13-visite-grafi-p30-dfs-parentesi.png]]

**Teorema 1.** Per ogni coppia di nodi $u$ e $v$ si può verificare solo una delle seguenti condizioni:
- gli intervalli $[d[u], f[u]]$ e $[d[v], f[v]]$ sono disgiunti e $u$ non è discendente di $v$ né $v$ è discendente di $u$ nella depth-first forest;
- l'intervallo $[d[u], f[u]]$ è contenuto interamente nell'intervallo $[d[v], f[v]]$ e $u$ è un discendente di $v$ in un depth-first tree;
- l'intervallo $[d[v], f[v]]$ è contenuto interamente nell'intervallo $[d[u], f[u]]$ e $v$ è un discendente di $u$ in un depth-first tree.

**Corollario 1.** Un vertice $v$ è un discendente di $u$ nella depth-first forest se e solo se $d[u] < d[v] < f[v] < f[u]$.

*Dimostrazione.* Si supponga $d[u] < d[v]$. Quando $v$ viene scoperto, $u$ o è ancora grigio o è nero.
- **Caso 1) $d[v] < f[u]$:** $v$ viene scoperto quando $u$ è ancora grigio, quindi $v$ è un discendente di $u$. I vicini di $v$ saranno esplorati tutti (ovvero $v$ sarà colorato di nero) prima che siano esplorati tutti i vicini di $u$, cioè $f[v] < f[u]$; quindi $[d[v], f[v]]$ è contenuto interamente in $[d[u], f[u]]$.
- **Caso 2) $f[u] < d[v]$:** ne segue $d[u] < f[u] < d[v] < f[v]$, cioè gli intervalli sono disgiunti. Dato che $u$ è nero quando $v$ viene scoperto, nessun vertice è un discendente dell'altro.

### Teorema del cammino bianco · [[13 - Algoritmi di visita di un grafo.pdf#page=33|p. 33]], [[13 - Algoritmi di visita di un grafo.pdf#page=34|34]]

**Teorema 2.** In una depth-first forest, un vertice $v$ è un discendente di $u$ se e solo se, al tempo $d[u]$, $v$ può essere raggiunto da $u$ attraverso un percorso che consiste di soli nodi bianchi.

*Dimostrazione.* ($\Rightarrow$) $v$ è un discendente di $u$ in un depth-first tree; sia $w$ un qualunque nodo lungo il percorso da $u$ a $v$ nel depth-first tree: $w$ è un discendente di $u$ e quindi (corollario 1) $d[u] < d[w]$, quindi $w$ è bianco quando si scopre $u$. Al tempo $d[u]$ c'è dunque un percorso da $u$ a $v$ che consiste di soli nodi bianchi (anche $v$ è bianco).

($\Leftarrow$) Si assume che tutti i nodi lungo tale percorso, eccetto $v$, diventino discendenti di $u$. Altrimenti, sia $v$ il nodo più vicino a $u$ che non diventa discendente di $u$. Sia $w$ il predecessore di $v$ lungo tale percorso ($w$ diventa un discendente di $u$), quindi $f[w] \le f[u]$ per il corollario 1 (l'uguale c'è perché $w$ potrebbe essere $u$). $v$ viene scoperto dopo che viene scoperto $u$ ma prima che $w$ sia finito ($v$ è un vicino di $w$): $d[u] < d[v] < f[w] \le f[u]$. Per il teorema 1, $[d[v], f[v]]$ è contenuto in $[d[u], f[u]]$ e quindi (corollario 1) $v$ deve essere un discendente di $u$.

### Classificazione degli archi · [[13 - Algoritmi di visita di un grafo.pdf#page=35|p. 35]]–[[13 - Algoritmi di visita di un grafo.pdf#page=37|37]]

Una DFS partiziona gli archi di un grafo in 4 insiemi:
- **tree edges**: gli archi in una depth-first forest; $(u, v)$ è un tree edge se $v$ è scoperto esplorando i vicini di $u$;
- **back edges**: archi $(u, v)$ con $v$ antenato di $u$ in un depth-first tree; i self-loop sono considerati back edges;
- **forward edges**: archi $(u, v)$ con $u$ antenato di $v$ in un depth-first tree;
- **cross edges**: tutti gli altri archi, tra nodi di diversi depth-first tree o dello stesso depth-first tree ma che non sono l'uno il discendente dell'altro.

Per i grafi non direzionali ci può essere ambiguità tra $(u, v)$ e $(v, u)$, che sono lo stesso arco: un arco viene classificato sulla base della «direzione» che viene incontrata prima.

DFS può classificare gli archi man mano che li incontra: un arco $(u, v)$ può essere classificato sulla base del **colore di $v$** nel momento in cui l'arco è esplorato per la prima volta.
- Se $v$ è bianco, $(u, v)$ è un tree edge.
- Se $v$ è grigio, $(u, v)$ è un back edge.
- Se $v$ è nero ($f[v] < f[u]$), $(u, v)$ può essere un forward edge o un cross edge: se $d[u] < d[v]$ è un forward edge ($d[u] < d[v] < f[v] < f[u]$); se $d[u] > d[v]$ è un cross edge.

In una DFS su un grafo non direzionale, **ogni arco è o un tree edge o un back edge**. Si assume che $u$ venga scoperto prima di $v$; dato che $v$ è un vicino di $u$, $v$ deve essere scoperto e completato prima che sia completato $u$. Se $(u, v)$ viene esplorato per primo nella direzione $u \to v$, allora è un tree edge; se viene esplorato per primo nella direzione $v \to u$, allora è un back edge.

![[13-visite-grafi-p37-dfs-grafo-non-orientato.png]]

### Ordinamento topologico · [[13 - Algoritmi di visita di un grafo.pdf#page=38|p. 38]]–[[13 - Algoritmi di visita di un grafo.pdf#page=43|43]]

Nota a mano di p. 38 (lettura incerta): la disposizione deve rappresentare la proprietà del fenomeno, il posizionamento rispetta il fenomeno sottostante; ordine topologico $v_1, v_2, v_3, v_4, v_5, v_6, v_7$.

![[13-visite-grafi-p38-ordinamento-topologico.png]]

DFS può essere usato per realizzare un ordinamento topologico di un *directed acyclic graph* (DAG). Un ordinamento topologico di un DAG determina un ordine dei nodi tale che, se esiste un arco $u \to v$, allora $u$ precede $v$. Se il grafo non è aciclico, non è possibile un tale ordinamento. Tale ordinamento è utile, ad esempio, quando gli archi indicano una relazione di precedenza.

```
Topological-Sort (G)
Call DFS(G) to compute finishing times f[v] for each vertex v
As each vertex is finished, insert it onto the front of a linked list
return the linked list of vertices
```

Nota a mano di p. 40 (lettura incerta): facciamo ordinamento *del* grafo e non *sul* grafo; fin ora abbiamo sempre visto ordinamenti sul grafo e non del grafo. Il tempo di esecuzione è $\Theta(V + E)$: DFS richiede $\Theta(V + E)$ e l'inserimento di $\lvert V \rvert$ vertici nella lista richiede $O(V)$.

![[13-visite-grafi-p40-topological-sort-codice.png]]
*DAG con vertici $a, \dots, j$ e ordinamento $a, b, e, f, d, c, g, j, h, i$.*

**Lemma 1.** Un grafo direzionale è aciclico se e solo se una DFS su $G$ non restituisce back edges.
- Se $G$ restituisce un back edge, allora il grafo direzionale è ciclico: se $(u, v)$ è un back edge, $v$ è un antenato di $u$ in un depth-first tree, quindi c'è un percorso da $v$ a $u$ e il link $u \to v$ completa il ciclo.
- Se il grafo contiene un ciclo $c$, allora la DFS restituisce (almeno) un back edge: sia $v$ il primo vertice di $c$ scoperto durante la DFS e $u \to v$ l'arco che precede $v$ nel ciclo. Al tempo $d[v]$, i vertici di $c$ formano un percorso di nodi bianchi da $v$ a $u$, quindi $u$ diventerà un discendente di $v$ e $u \to v$ un back edge.

**Teorema 1.** Topological-Sort (G) produce un ordinamento topologico di un DAG $G$. Occorre mostrare che, per ogni coppia di vertici $u$ e $v$, se c'è un arco $u \to v$ allora $f[v] < f[u]$. Si consideri un arco $u \to v$ che viene esplorato da DFS:
- $v$ non può essere grigio, altrimenti $u \to v$ sarebbe un back edge, il che contraddice il lemma 1;
- se $v$ è bianco, $v$ diventa un discendente di $u$ e quindi $f[v] < f[u]$;
- se $v$ è nero, l'esplorazione di $v$ è già finita e quindi, dato che si sta ancora esplorando $u$, $f[v] < f[u]$.

### Percorsi minimi · [[13 - Algoritmi di visita di un grafo.pdf#page=44|p. 44]]–[[13 - Algoritmi di visita di un grafo.pdf#page=53|53]]

*(Slide in inglese di S. Skiena, «Lecture 14: Shortest Paths».)*

**Applicazioni degli shortest path.** Trovare il cammino minimo tra due nodi si presenta in molte applicazioni: **problemi di trasporto** (il modo più economico di viaggiare tra due luoghi), **pianificazione del movimento** (il modo più naturale per un personaggio dei cartoni di muoversi in un ambiente simulato), **problemi di comunicazione** (quanto tempo impiega un messaggio per andare da un posto a un altro; quali due posti sono i più lontani, cioè qual è il **diametro** della rete).

**Grafi non pesati.** Lo shortest path usa il numero minimo di archi e si trova in tempo $O(n + m)$ con la ricerca in ampiezza. In un grafo pesato il peso di un percorso fra due vertici è la somma dei pesi degli archi sul percorso. La BFS non funziona sui grafi pesati perché visitare più archi può costare meno di visitarne meno, ad esempio $1+1+1+1+1+1+1 < 10$. Ci può essere un numero esponenziale di shortest path tra due nodi: non si possono riportare efficientemente *tutti* gli shortest path.

**Pesi negativi.** I cicli di costo negativo rendono privo di senso il problema di trovare lo shortest path, perché si può sempre ripercorrere il ciclo per ridurre il costo del percorso. Si assume quindi che tutti i pesi degli archi siano positivi; altri algoritmi trattano correttamente gli archi di costo negativo.

**Algoritmo di Dijkstra.** Il principio è che se $(s, \dots, x, \dots, t)$ è lo shortest path da $s$ a $t$, allora $(s, \dots, x)$ farebbe meglio a essere lo shortest path da $s$ a $x$.

**Inizializzazione e aggiornamento.** Lo shortest path da $s$ a $s$ è $d(s, s) = 0$. Se tutti i pesi sono positivi, l'arco più piccolo incidente su $s$, diciamo $(s, x)$, definisce $d(s, x)$. Non appena si stabilisce lo shortest path da $s$ a un nuovo nodo $x$, si percorrono tutti i suoi archi incidenti per vedere se esiste un modo migliore di arrivare dagli altri nodi passando per $x$.

```
known = {s}
for i = 1 to n, dist[i] = ∞
for each edge (s,v), dist[v] = d(s,v)
last = s
while (last ≠ t)
    select v such that dist(v) = min_unknown dist(i)
    for each (v,x), dist[x] = min(dist[x], dist[v] + w(v,x))
    last = v
    known = known ∪ {v}
```

![[13-visite-grafi-p51-dijkstra-esempio.png]]
*Esempio: il grafo $G$ e il suo albero dei cammini minimi Dijkstra(G,A).*

![[13-visite-grafi-p52-dijkstra-grafo.png]]
*Primo fotogramma di un'animazione: grafo non orientato, pesi non negativi, sorgente $A$, coda di priorità $Q$ ordinata per distanza (tutti i vertici a $\infty$).*

**Analisi.** Trovare il fringe-edge di peso minimo richiede tempo $O(n)$ (basta scorrere la lista dei fringe). Dopo aver aggiunto un nuovo vertice $v$ all'albero, scorrere la sua lista di adiacenza per aggiornare il costo di aggiungere i vertici fringe, se si è trovato un modo più economico passando per $v$, si fa in $O(n)$. Il tempo totale è $n \times n = O(n^2)$.

Possiamo fare di meglio? Possiamo sfruttare la «località temporale» dei nodi visitati?

*Approfondimenti nel wiki: [[visita-di-un-grafo]], [[visita-in-ampiezza]], [[print-path]], [[visita-in-profondita]], [[ordinamento-topologico]], [[dijkstra]]*

## Lezione 14 — Backpropagation

*Fonte: 14 - Backpropagation.pdf (30 pagine: slide, con note a mano alle p. 2, 5, 26, 28, 29).*

### Motivazione · [[14 - Backpropagation.pdf#page=2|p. 2]]

- Calcolo di derivate in funzioni composte (nota a mano: da dove nasce → regola della catena).
- Si considera una funzione scalare $C: \mathbb{R}^n \to \mathbb{R}$ ottenuta come composizione di molte operazioni elementari. Esempio: $C(x) = \tfrac{1}{2}\bigl(f(g(h(x)))\bigr)^2$.
- Obiettivo: calcolare il gradiente $\nabla C(x)$ in modo sistematico ed efficiente.
- Idea: sfruttare la struttura di composizione rappresentandola come un **grafo computazionale**.

### Grafi computazionali feedforward · [[14 - Backpropagation.pdf#page=3|p. 3]]

Si usa un **grafo diretto aciclico (DAG)** organizzato per layer:
- Layer 0: variabili di input $x_1, \dots, x_n$;
- Layer $1, 2, \dots, L-1$: variabili intermedie;
- Layer $L$: uscita scalare $C$ (o poche variabili di output).

Ogni nodo $v$ (non di input) rappresenta una funzione locale $z_v = f_v\bigl(z_{u_1}, \dots, z_{u_k}\bigr)$. Il grafo è feedforward: archi solo da layer inferiori a layer superiori, niente cicli («inferiore» e «superiore» sono intesi in termini di profondità di livello).

### Esempio di grafo semplice · [[14 - Backpropagation.pdf#page=4|p. 4]], [[14 - Backpropagation.pdf#page=5|5]]

Input $a$, $b$; $C(a, b) = \tfrac{1}{2}(\sin(a \cdot b) + b - 1)^2$. Ogni nodo rappresenta una variabile; ogni arco una dipendenza diretta.

| Layer 0 | Layer 1 | Layer 2 | Layer 3 | Layer 4 |
|---|---|---|---|---|
| $a$, $b$ | $c = a \cdot b$ | $d = \sin(c)$ | $e = d + b$ | $C = \tfrac{1}{2}(e-1)^2$ |

![[14-backpropagation-p5-grafo-semplice.png]]
*Il grafo con i suoi layer; note a mano: grafo operazionale in cui i nodi rappresentano le operazioni computazionalmente indipendenti, è un flusso di dati; è un DAG ma non è un albero, quindi non ha una radice.*

### Il problema del gradiente sul grafo · [[14 - Backpropagation.pdf#page=6|p. 6]]

- C'è un'unica uscita scalare $C$ in cima al grafo.
- Si vogliono le derivate rispetto agli input, $\partial C/\partial a$ e $\partial C/\partial b$.
- Si possono volere anche $\partial C/\partial c$, $\partial C/\partial d$, … per tutti i nodi interni.
- La regola della catena si può applicare in modo meccanico sul grafo, ma la sua applicazione ripetuta potrebbe essere molto onerosa.

### Perché serve la backpropagation · [[14 - Backpropagation.pdf#page=7|p. 7]]

Si supponga una rete con un milione di parametri $w_1, \dots, w_n$ e una funzione scalare di costo $C$: $\nabla C = (\partial C/\partial w_1, \partial C/\partial w_2, \dots, \partial C/\partial w_n)$.

**Il problema algoritmico.** Calcolare ogni derivata separatamente può ripetere gran parte dei calcoli: come riutilizzare le quantità intermedie già disponibili? **L'idea:** dividere la computazione in due momenti separati, un passaggio in avanti per i valori e un passaggio all'indietro per tutte le derivate.

### Regola della catena su un grafo · [[14 - Backpropagation.pdf#page=8|p. 8]]

Sia $x$ una variabile interna del grafo e $C$ l'uscita finale. Se $x$ influenza $C$ tramite i successori $y_1, \dots, y_k$:

$$
\frac{\partial C}{\partial x} = \sum_{j} \left( \frac{\partial C}{\partial y_j} \cdot \frac{\partial y_j}{\partial x} \right)
$$

Nel grafo $x$ è un nodo e gli $y_j$ sono i suoi successori diretti. Una volta note le derivate $\partial C/\partial y_j$, si può risalire a $\partial C/\partial x$: questo è il principio di base della backpropagation sul grafo.

### Passo forward (valori) · [[14 - Backpropagation.pdf#page=9|p. 9]]

Input: valori iniziali $x_1, \dots, x_n$ nel layer 0. Per $\ell = 0, 1, \dots, L$, per ogni nodo $v$ nel layer $\ell$:
- se $v$ è di input, $value[v]$ è fornito dall'esterno;
- altrimenti $value[v] = f_v(value[u] \text{ per } u \in pred[v])$.

Alla fine del forward si ha il valore di ogni nodo, in particolare di $C$. I $value[v]$ si possono memorizzare per usarli nel passo backward.

### Passo backward (derivate) · [[14 - Backpropagation.pdf#page=10|p. 10]]

Inizializzazione: $\delta_v = 0$ per tutti i nodi $v$. Per il nodo di uscita $C$: $\delta_C = 1$ (oppure $\delta_C = d\,Costo/dC$ se c'è una funzione di costo esterna). Per $\ell = L, L-1, \dots, 0$, per ogni nodo $v$ nel layer $\ell$ e per ogni predecessore $u$ di $v$:

$$
\delta_u \mathrel{+}= \delta_v \cdot \frac{\partial z_v}{\partial z_u}
$$

Al termine, per i nodi di input $x_i$: $\delta_{x_i} = \partial C/\partial x_i$.

### Esempio: calcolo del gradiente · [[14 - Backpropagation.pdf#page=11|p. 11]]–[[14 - Backpropagation.pdf#page=21|21]]

Si vuole valutare $C(a, b) = \tfrac{1}{2}(\sin(a \cdot b) + b - 1)^2$ e calcolarne il gradiente nel punto $(2, 3)$, con $value[a] = 2$ e $value[b] = 3$.

![[14-backpropagation-p11-esempio-forward-1.png]]

**Forward** (pp. 11–15; il seno è valutato in radianti; i valori si memorizzano perché servono nel backward):
1. $value[a] = 2$, $value[b] = 3$;
2. $value[c] = value[a] \cdot value[b] = 2 \cdot 3 = 6$;
3. $value[d] = \sin(value[c]) = \sin(6) \approx -0{,}2794$;
4. $value[e] = value[d] + value[b] = \sin(6) + 3 \approx 2{,}7206$ (il valore di $b$ è riutilizzato senza ricalcolarlo);
5. $C = \tfrac{1}{2}(value[e] - 1)^2 = \tfrac{1}{2}(\sin(6) + 2)^2 \approx 1{,}4802$.

**Backward** (pp. 16–20): $\delta[v] = \partial C/\partial z_v$, inizialmente 0 per ogni $v \ne C$, e $\delta[C] = \partial C/\partial C = 1$. Le quantità rosse sono accumulatori delle derivate, non valori dei nodi.
1. Da $C$ a $e$: $\partial C/\partial e = e - 1 \approx 1{,}7206$; $\delta[e] \mathrel{+}= \delta[C] \cdot (e-1) \approx 1{,}7206$.
2. Da $e$ a $d$ e $b$: $e = d + b$, $\partial e/\partial d = \partial e/\partial b = 1$, quindi $\delta[d] \mathrel{+}= \delta[e] \cdot 1 \approx 1{,}7206$ e $\delta[b] \mathrel{+}= \delta[e] \cdot 1 \approx 1{,}7206$. Attenzione: $\delta[b]$ è ancora parziale, perché manca il contributo di $c$.
3. Da $d$ a $c$: $d = \sin(c)$ usa il valore di $c$ memorizzato nel forward; $\partial d/\partial c = \cos(c) = \cos(6) \approx 0{,}9602$; $\delta[c] \mathrel{+}= \delta[d] \cdot \cos(6) \approx 1{,}6521$. Non serve ricalcolare il cammino a monte di $c$.
4. Da $c$ ad $a$ e $b$: $c = a \cdot b$; $\partial c/\partial a = b = 3 \Rightarrow \delta[a] \mathrel{+}= \delta[c] \cdot 3 \approx 4{,}9562$; $\partial c/\partial b = a = 2 \Rightarrow \delta[b] \leftarrow \delta[b] + \delta[c] \cdot 2 \approx 5{,}0247$. Nota: per $b$, $1{,}7206 + 3{,}3041 \approx 5{,}0247$: due cammini, due contributi, una somma.

![[14-backpropagation-p20-backward-ultimo-passo.png]]

**Risultato** (p. 21, verifica con la regola della catena):

$$
\frac{\partial C}{\partial a} = (\sin(ab) + b - 1) \cdot b\cos(ab) \approx 4{,}9562, \qquad \frac{\partial C}{\partial b} = (\sin(ab) + b - 1) \cdot (a\cos(ab) + 1) \approx 5{,}0247
$$

$\nabla C(2, 3) \approx (4{,}9562;\ 5{,}0247)$; i calcoli usano valori non arrotondati.

### Pseudocodice e correttezza · [[14 - Backpropagation.pdf#page=22|p. 22]], [[14 - Backpropagation.pdf#page=23|23]]

$Ord$ = ordine topologico di $G$; $pred[v]$ = predecessori di $v$; $value[v]$ = valore; $\delta[v]$ = derivata del costo rispetto al valore di $v$.

```
FORWARD
for v in Ord:
    if v è un input:
        value[v] ← input[v]
    else:
        args ← [value[u] for u in pred[v]]
        value[v] ← f_v(args)

BACKWARD
for v in V: δ[v] ← 0
δ[C] ← 1
for v in reverse(Ord):
    for u in pred[v]:
        dlocal ← ∂f_v/∂z_u
        δ[u] += δ[v] · dlocal
```

La derivata locale è valutata usando i valori del forward. Per un DAG per layer, $Ord$ può essere semplicemente l'ordine dei layer.

**Correttezza.** Si ordinano i nodi in ordine topologico $v_1, \dots, v_m$.
- *Forward:* ogni nodo usa solo predecessori già calcolati → corretto per costruzione.
- *Backward:* usa l'ordine topologico inverso $v_m, \dots, v_1$. **Invariante:** quando si processa $v$, $\delta_v = \partial C/\partial z_v$ è già corretto.
  - Base: nodo di uscita $C$, $\delta_C = \partial C/\partial C = 1$.
  - Passo induttivo: si suppongano corrette le $\delta_y$ per tutti i successori $y$ di $x$; allora $\delta_x = \sum_{y \in succ(x)} \delta_y \cdot \partial z_y/\partial z_x$, che è la regola della catena. Quindi per induzione $\delta_v$ è corretta per ogni nodo $v$.

### Complessità computazionale · [[14 - Backpropagation.pdf#page=24|p. 24]]

Siano $V$ ed $E$ il numero di nodi e di archi del grafo computazionale.
- **Forward:** ogni nodo è valutato una volta e ogni dipendenza è letta una volta: $O(V + E)$.
- **Backward:** ogni nodo e ogni arco sono elaborati una volta: $O(V + E)$.

I limiti assumono costo $O(1)$ per ciascuna operazione elementare e per il contributo di ogni arco; operazioni più complesse vanno contabilizzate separatamente.

### Dai grafi alle reti neurali · [[14 - Backpropagation.pdf#page=25|p. 25]]–[[14 - Backpropagation.pdf#page=28|28]]

Una **rete neurale feedforward** può essere rappresentata come un DAG di operazioni matematiche (input, layer 1, layer 2, costo). Non serve ancora conoscere il funzionamento dei neuroni: interessano la struttura delle dipendenze e l'ordine in cui si possono eseguire i calcoli.

![[14-backpropagation-p25-rete-neurale.png]]

Una rete neurale feedforward è un caso particolare di grafo computazionale:
- **nodi:** operazioni di somma pesata, funzioni di attivazione, ecc.;
- **archi:** connessioni che trasportano i valori (e le dipendenze).

La backpropagation «classica» delle reti neurali è l'algoritmo visto, applicato a un grafo con struttura molto regolare (layer di neuroni). Capita la backpropagation su grafi generici, diventa banale capirla e specializzarla al caso delle reti neurali (nota a mano: è solo una tecnica del calcolo del gradiente sui grafi computazionali).

- **Forward: i valori** — si parte dagli input e si calcolano i valori dei nodi, rispettando le dipendenze. *Ordine topologico:* ogni nodo usa soltanto valori già calcolati.
- **Backward: le derivate** — si parte dal costo $C$ e si propagano le derivate verso i predecessori. *Ordine topologico inverso:* ogni nodo accumula i contributi di tutti i suoi successori. (Nota a mano: verifico se la predizione è giusta ⇒ in base all'errore commesso …, per propagare all'indietro l'errore e ricavare la derivata; lettura incerta.)

### Dai grafi all'apprendimento · [[14 - Backpropagation.pdf#page=29|p. 29]], [[14 - Backpropagation.pdf#page=30|30]]

Nel Machine Learning, la backpropagation **calcola il gradiente del costo rispetto ai parametri**. Non modifica, da sola, i parametri della rete.

| Forward | Backward | Ottimizzazione |
|---|---|---|
| Calcolo del costo $C$ | Calcolo di $\nabla C$ | Aggiornamento dei parametri |

Esempio di aggiornamento: $w_i \leftarrow w_i - \eta \cdot \partial C/\partial w_i$ (note a mano: $\eta$ = *learning rate*, valore di scala; $w_i$ = parametri; $\partial C/\partial w_i$ = errore commesso).

Da ASD: grafi orientati, DFS, ordinamento topologico, riuso dei risultati intermedi. Da ML: scelta del modello, del costo e dell'algoritmo di ottimizzazione.

L'ultima slide (p. 30) mostra il primo fotogramma di un'animazione, «1. Forward pass»: l'immagine di un gatto entra nella rete (valori di input 0,20; 0,80; 0,50), un livello nascosto di due nodi e due uscite, «Cane» e «Gatto».

*Approfondimenti nel wiki: [[grafo-computazionale]], [[backpropagation]]*

## Lezione 15 — Backtracking

*Fonte: 15 - Backtracking.pdf (24 pagine di slide in inglese di S. Skiena, con note a mano alle p. 2, 15, 21).*

### Sudoku · [[15 - Backtracking.pdf#page=2|p. 2]], [[15 - Backtracking.pdf#page=3|3]]

![[15-backtracking-p2-sudoku.png]]
*Un Sudoku e la sua soluzione. Nota a mano (lettura incerta): posso creare un grafo dello spazio delle soluzioni, e una soluzione è un nodo di questo grafo ⇒ posso sapere se un nodo è soluzione o meno ma lo devo visitare ⇒ devo guardare tutto il grafo (potenzialmente).*

Risolvere il Sudoku comporta una forma di **ricerca esaustiva** delle configurazioni possibili. Sfruttare i vincoli per escludere certe possibilità in certe posizioni permette di **potare** la ricerca fino al punto in cui le persone riescono a risolvere il Sudoku a mano. Il **backtracking** è la chiave per implementare in modo corretto ed efficiente programmi di ricerca esaustiva.

### Backtracking · [[15 - Backtracking.pdf#page=4|p. 4]]

Il backtracking è un metodo sistematico per iterare su tutte le configurazioni possibili di uno spazio di ricerca. È un algoritmo generale che va personalizzato per ogni applicazione. La soluzione è modellata come un vettore $a = (a_1, a_2, \dots, a_n)$, in cui ogni elemento $a_i$ è scelto da un insieme finito e ordinato $S_i$. Il vettore può rappresentare una disposizione in cui $a_i$ contiene l'$i$-esimo elemento di una permutazione; oppure un sottoinsieme $S$, in cui $a_i$ è vero se e solo se l'$i$-esimo elemento dell'universo è in $S$.

### L'idea del backtracking · [[15 - Backtracking.pdf#page=5|p. 5]]

A ogni passo dell'algoritmo di backtracking si parte da una soluzione parziale, $a = (a_1, a_2, \dots, a_k)$, e si prova a estenderla aggiungendo un altro elemento in fondo. Dopo l'estensione si verifica se quello che si ha finora è una soluzione completa. Se non lo è, la questione critica è se la soluzione parziale corrente $a$ sia potenzialmente estendibile a una soluzione:
- se sì, si ricorre e si continua;
- se no, si cancella l'ultimo elemento da $a$ e si prova un'altra possibilità per quella posizione, se esiste.

### Implementazione del backtracking · [[15 - Backtracking.pdf#page=6|p. 6]]–[[15 - Backtracking.pdf#page=12|12]]

**Backtracking ricorsivo** (p. 7):

```
Backtrack (a, k)
if a is a solution, print (a)
else {
    k = k + 1
    compute S_k
    while S_k ≠ ∅ do
        a_k = an element in S_k
        S_k = S_k − a_k
        Backtrack (a, k)
}
```

**Backtracking e DFS** (p. 8): il backtracking è in realtà una visita in profondità di un grafo implicito di configurazioni.
- Può essere usato facilmente per iterare su tutti i sottoinsiemi o su tutte le permutazioni di un insieme.
- Assicura la correttezza enumerando tutte le possibilità.
- Per essere efficiente bisogna potare i rami morti o ridondanti dello spazio di ricerca, quando possibile.

**Implementazione in C** (p. 9):

```c
void backtrack(int a[], int k, data input) {
    int c[MAXCANDIDATES];       /* candidates for next position */
    int nc;                     /* next position candidate count */
    int i;                      /* counter */
    if (is_a_solution(a, k, input)) {
        process_solution(a, k, input);
    } else {
        k = k + 1;
        construct_candidates(a, k, input, c, &nc);
        for (i = 0; i < nc; i++) {
            a[k] = c[i];
            make_move(a, k, input);
            backtrack(a, k, input);
            unmake_move(a, k, input);
            if (finished) {
                return;         /* terminate early */
            }
        }
    }
}
```

- `is_a_solution(a, k, input)` (p. 10): funzione booleana che verifica se i primi $k$ elementi del vettore $a$ sono una soluzione completa per il problema dato; l'ultimo argomento, `input`, permette di passare informazioni generali per valutare se $a$ è una soluzione.
- `construct_candidates(a, k, input, c, nc)` (p. 11): riempie un array `c` con l'insieme completo dei possibili candidati per la $k$-esima posizione di $a$, dato il contenuto delle prime $k-1$ posizioni; il numero di candidati restituiti è `nc`.
- `process_solution(a, k)` (p. 12): stampa, conta o in qualche modo elabora una soluzione completa una volta costruita.

Il backtracking assicura la correttezza enumerando tutte le possibilità; assicura l'efficienza non visitando mai uno stato più di una volta. Poiché a ogni chiamata ricorsiva si alloca un nuovo array di candidati `c`, i sottoinsiemi dei candidati di estensione non ancora considerati a ogni posizione non interferiscono fra loro.

### Costruire tutti i sottoinsiemi · [[15 - Backtracking.pdf#page=13|p. 13]]–[[15 - Backtracking.pdf#page=18|18]]

Per costruire tutti i $2^n$ sottoinsiemi si usa un array/vettore di $n$ celle, in cui il valore di $a_i$ è vero o falso, a significare se l'$i$-esimo elemento è o non è nel sottoinsieme. Nella notazione dell'algoritmo generale, $S_k = (\text{true}, \text{false})$ e $a$ è una soluzione ogni volta che $k \ge n$.

```c
int is_a_solution(int a[], int k, int n) {
    return (k == n);
}

void construct_candidates(int a[], int k, int n, int c[], int *nc) {
    c[0] = true;
    c[1] = false;
    *nc = 2;
}

void process_solution(int a[], int k, int input) {
    int i;                      /* counter */
    printf("{");
    for (i = 1; i <= k; i++) {
        if (a[i] == true) {
            printf(" %d", i);
        }
    }
    printf(" }\n");
}

void generate_subsets(int n) {
    int a[NMAX];                /* solution vector */
    backtrack(a, 0, n);
}
```

Qui si stampano gli elementi di ogni sottoinsieme, ma si può fare quello che si vuole, per esempio testare se è una soluzione di un problema di vertex cover.

**Ordine di generazione dei sottoinsiemi di $\{1, 2, 3\}$** (p. 15):

$$
\begin{aligned}
&(1) \to (1,2) \to (1,2,3) \to (1,2,-) \to (1,-) \to (1,-,3) \to (1,-,-) \to (1,-) \to (1) \to (-) \to \\
&(-,2) \to (-,2,3) \to (-,2,-) \to (-,-) \to (-,-,3) \to (-,-,-) \to (-,-) \to (-) \to ()
\end{aligned}
$$

Le foglie dell'albero sono $\{1,2,3\}$, $\{1,2\}$, $\{1,3\}$, $\{1\}$, $\{2,3\}$, $\{2\}$, $\{3\}$, $\{\}$ (nota a mano, lettura incerta: che significa che non è un algoritmo sistematico ma va verso la costruzione → sono fuso?).

![[15-backtracking-p15-sottoinsiemi-albero.png]]

### Costruire tutte le permutazioni · [[15 - Backtracking.pdf#page=19|p. 19]]–[[15 - Backtracking.pdf#page=24|24]]

Quante sono le permutazioni di un insieme di $n$ elementi? Per costruire tutte le $n!$ permutazioni si usa un array/vettore di $n$ celle, in cui il valore di $a_i$ è un intero da 1 a $n$ che non è ancora comparso nel vettore, corrispondente all'$i$-esimo elemento della permutazione. Nella notazione dell'algoritmo generale, $S_k = (1, \dots, n) - v$ e $v$ è una soluzione ogni volta che $k \ge n$.

**Ordine di generazione delle permutazioni** (p. 21): $(1) \to (1,2) \to (1,2,3) \to (1,2) \to (1) \to (1,3) \to (1,3,2) \to (1,3) \to (1) \to () \to (2) \to (2,1) \to (2,1,3) \to (2,1) \to (2) \to (2,3) \to (2,3,1) \to (2,3) \to () \to (2) \to () \to (3) \to (3,1) \to (3,1,2) \to (3,1) \to (3) \to (3,2) \to (3,2,1) \to (3,2) \to (3) \to ()$. Le soluzioni sono $123, 132, 213, 231, 312, 321$ (nota a mano: posso togliere grandi porzioni di albero appena diventano inutili o ridondanti).

![[15-backtracking-p21-permutazioni-albero.png]]

Per evitare di ripetere elementi della permutazione, $S_k = \{1, \dots, n\} - a$ e $a$ è una soluzione ogni volta che $k = n$:

```c
void construct_candidates(int a[], int k, int n, int c[], int *nc) {
    int i;                      /* counter */
    bool in_perm[NMAX];         /* what is now in the permutation? */
    for (i = 1; i < NMAX; i++) {
        in_perm[i] = false;
    }
    for (i = 1; i < k; i++) {
        in_perm[a[i]] = true;
    }
    *nc = 0;
    for (i = 1; i <= n; i++) {
        if (!in_perm[i]) {
            c[*nc] = i;
            *nc = *nc + 1;
        }
    }
}
```

Per completare il lavoro servono `process_solution` e `is_a_solution`, oltre ai parametri giusti per `backtrack`; sono essenzialmente gli stessi dei sottoinsiemi:

```c
void process_solution(int a[], int k, int input) {
    int i;                      /* counter */
    for (i = 1; i <= k; i++) {
        printf(" %d", a[i]);
    }
    printf("\n");
}

int is_a_solution(int a[], int k, int n) {
    return (k == n);
}

void generate_permutations(int n) {
    int a[NMAX];                /* solution vector */
    backtrack(a, 0, n);
}
```

*Approfondimenti nel wiki: [[backtracking]], [[generazione-di-permutazioni]]*
