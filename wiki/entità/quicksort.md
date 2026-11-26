---
tipo: entità
categoria: algoritmo
paradigma: "[[divide-et-impera]]"
fonti_pdf: ["07-Quicksort 1.pdf#page=2", "07-Quicksort 1.pdf#page=3", "07-Quicksort 1.pdf#page=4", "07-Quicksort 1.pdf#page=14", "07-Quicksort 1.pdf#page=15", "07-Quicksort 1.pdf#page=16", "07-Quicksort 1.pdf#page=17", "07-Quicksort 1.pdf#page=18", "07-Quicksort 1.pdf#page=21", "07-Quicksort 1.pdf#page=22"]
---

# Quicksort

Le sezioni seguono l'ordine delle slide: proprietà (p. 2) → divide et impera (p. 3) → pseudocodice (p. 4) → [[partition]] (pp. 5–13) → casi peggiore, migliore, bilanciato e medio (pp. 14–18) → dimostrazione del caso peggiore (pp. 21–22). La versione randomizzata (pp. 19–20, 23) ha una pagina a sé: [[quicksort-randomizzato]].

## Problema risolto

[[ordinamento]] di un array $A[1..n]$, **sul posto**.

## Idea · [[07-Quicksort 1.pdf#page=2|p. 2]], [[07-Quicksort 1.pdf#page=3|3]]

Quick Sort ha un tempo di esecuzione:
- $\Theta(n^2)$ nel caso peggiore;
- $\Theta(n \lg n)$ nel caso «medio»;
- ordina sul posto.

Nella pratica risulta essere tra i più efficienti, grazie al fatto che i fattori «nascosti» in $\Theta(n \lg n)$ sono piuttosto piccoli.

> 💡 Connessione: i «fattori nascosti» sono le costanti che la [[notazione-asintotica]] ignora. A parità di $\Theta(n\lg n)$ conta la costante: è la stessa osservazione delle costanti nascoste di [[efficienza-degli-algoritmi]].

Utilizza un approccio **[[divide-et-impera]]**:
- **Divide** — scelto un elemento $x$, detto *pivot*, partiziona l'array $A[p..r]$ in due sottoarray tali che $A[p..q-1]$ contiene gli elementi $\le x$ e $A[q+1..r]$ contiene gli elementi $> x$; il pivot va in $A[q]$.
- **Conquer** — ordina i due sottoarray mediante chiamate ricorsive.
- **Combine** — i sottoarray sono ordinati sul posto, quindi non occorre fare nulla.

![[07-quicksort-p3-divide-conquer-combine.png]]

> 🧩 Spiegazione mia — perché il Combine è vuoto: dopo il Divide ogni elemento di $A[p..q-1]$ è $\le x \le$ ogni elemento di $A[q+1..r]$. Se le due parti vengono ordinate, l'intero $A[p..r]$ è già ordinato. In [[merge-sort]] succede il contrario: Divide banale, Combine $\Theta(n)$.

## Pseudocodice · [[07-Quicksort 1.pdf#page=4|p. 4]], [[07-Quicksort 1.pdf#page=6|p. 6]]

```
Quicksort (A,p,r)
1  if p<r
2      q ← Partition (A,p,r)
3      Quicksort (A,p,q-1)
4      Quicksort (A,q+1,r)
```

Per ordinare l'intero array si invoca `Quicksort (A,1,length[A])`.

![[07-quicksort-p4-pseudocodice-quicksort.png]]

Annotazioni a mano sulla slide:
- accanto a `if p<r`: «logica base è gestita da quicksort non entrando nell'if». Il caso base ($p \ge r$, al più un elemento) non ha istruzioni proprie: semplicemente non si esegue il corpo dell'`if`;
- sotto la slide: «pivot piccolo: troppi swap» e «pivot grande: sposto solo una barriera».

> ⚠️ Contraddizione: la seconda annotazione è invertita rispetto a Partition. Per la regola di p. 6, un elemento **maggiore** del pivot fa avanzare solo la barriera $j$; un elemento **minore o uguale** fa avanzare $i$ e provoca uno scambio. Quindi con un pivot **piccolo** (quasi tutti gli elementi lo superano) si sposta solo una barriera, mentre con un pivot **grande** (quasi tutti gli elementi sono $\le$) si fanno molti scambi. 🧩 Verificato con il codice su 8 elementi: pivot massimo → 7 scambi nel ciclo; pivot minimo → 0 scambi, solo $j$ avanza. In entrambi i casi la partizione è sbilanciata ($n - 1$ e 0), che è il caso peggiore della sezione «Complessità».

Simboli: $A[p..r]$ = sotto-array da ordinare; $q$ = posizione finale del pivot restituita da [[partition]]. Il pivot $A[q]$ è già al suo posto definitivo e non partecipa alle chiamate ricorsive.

## Esempio di esecuzione · [[07-Quicksort 1.pdf#page=7|p. 7]], [[07-Quicksort 1.pdf#page=11|p. 11]]

![[animazione-quicksort.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo sull'array delle slide 07 pp. 5–12, ⟨2, 8, 7, 1, 3, 5, 6, 4⟩. Le slide tracciano solo la prima Partition; l'animazione prosegue con tutte le chiamate ricorsive. In giallo il sotto-array della chiamata attiva ($p$ e $r$ indicati sopra), in verde i pivot già al loro posto definitivo.

> 🧩 Derivazione mia — albero delle chiamate (la prima riga è la traccia di p. 7–p. 11; il resto è verificato con [[divide_et_impera.py]]):

| Chiamata | $A[p..r]$ prima | pivot | $q$ | $A[p..r]$ dopo Partition |
|---|---|---|---|---|
| Quicksort(A, 1, 8) | ⟨2, 8, 7, 1, 3, 5, 6, 4⟩ | 4 | 4 | ⟨2, 1, 3, **4**, 7, 5, 6, 8⟩ |
| ↳ Quicksort(A, 1, 3) | ⟨2, 1, 3⟩ | 3 | 3 | ⟨2, 1, **3**⟩ |
| &nbsp;&nbsp;↳ Quicksort(A, 1, 2) | ⟨2, 1⟩ | 1 | 1 | ⟨**1**, 2⟩ |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ Quicksort(A, 1, 0), Quicksort(A, 2, 2) | — | — | — | caso base |
| &nbsp;&nbsp;↳ Quicksort(A, 4, 3) | — | — | — | caso base |
| ↳ Quicksort(A, 5, 8) | ⟨7, 5, 6, 8⟩ | 8 | 8 | ⟨7, 5, 6, **8**⟩ |
| &nbsp;&nbsp;↳ Quicksort(A, 5, 7) | ⟨7, 5, 6⟩ | 6 | 6 | ⟨5, **6**, 7⟩ |
| &nbsp;&nbsp;&nbsp;&nbsp;↳ Quicksort(A, 5, 5), Quicksort(A, 7, 7) | — | — | — | caso base |
| &nbsp;&nbsp;↳ Quicksort(A, 9, 8) | — | — | — | caso base |

Risultato: ⟨1, 2, 3, 4, 5, 6, 7, 8⟩, ottenuto senza alcuna fase di fusione. Le chiamate con pivot 8 e pivot 3 sono partizioni sbilanciate ($n - 1$ e 0), quelle con pivot 4 e 6 sono bilanciate.

## Correttezza · [[07-Quicksort 1.pdf#page=13|p. 13]]

La correttezza di [[partition]] è dimostrata con l'invariante di p. 13.

> 🧩 Derivazione mia — [[correttezza-per-induzione]] forte su $n = r - p + 1$:
> - **Base** ($n \le 1$): `p<r` è falso, nessuna operazione; un sotto-array di 0 o 1 elementi è ordinato.
> - **Passo** ($n \ge 2$): Partition restituisce $q$ con $A[p..q-1] \le A[q] < A[q+1..r]$. Le due chiamate lavorano su $q - p$ e $r - q$ elementi, entrambi $\le n - 1$, quindi per ipotesi induttiva al ritorno le due parti sono ordinate. Non toccano $A[q]$ né scambiano elementi tra le due parti, quindi la proprietà del Divide resta vera e $A[p..r]$ è ordinato.
> - **Terminazione:** il pivot è escluso da entrambe le chiamate, quindi la dimensione scende di almeno 1.

## Complessità

### Come si imposta l'analisi: dallo pseudocodice alla ricorrenza · [[07-Quicksort 1.pdf#page=12|p. 12]], [[07-Quicksort 1.pdf#page=21|p. 21]]

> 🧩 Schema mio, che usa i costi delle slide.

**Passo 1 — costo di una chiamata.** Una chiamata `Quicksort(A,p,r)` su $n = r - p + 1$ elementi esegue:
- il test `if p<r` (riga 1): $\Theta(1)$;
- [[partition]] (riga 2): $\Theta(n)$;
- due chiamate ricorsive (righe 3–4): una sul sotto-array sinistro, di $q$ elementi, e una sul destro, di $n - q - 1$ elementi (il pivot resta fuori).

Quindi, indicando con $q$ la **dimensione** della parte sinistra (come fa la slide di p. 21):
$$
T(n) = T(q) + T(n - q - 1) + \Theta(n), \qquad T(0) = T(1) = \Theta(1)
$$

**Passo 2 — $q$ dipende dall'input.** La ricorrenza non è ancora risolvibile, perché $q$ lo decide Partition in base ai valori dell'array. Ogni «caso» delle slide corrisponde a una scelta di $q$, che trasforma la ricorrenza in una ricorrenza in una sola variabile.

**Passo 3 — si risolve con il metodo adatto alla sua forma.**

| Caso | $q$ | Ricorrenza | Metodo | Risultato | Slide |
|---|---|---|---|---|---|
| peggiore (sbilanciato) | $n - 1$ (o $0$) | $T(n-1) + \Theta(n)$ | srotolamento | $\Theta(n^2)$ | p. 14 |
| migliore (bilanciato) | $\approx n/2$ | $\le 2T(n/2) + \Theta(n)$ | [[teorema-dell-esperto]] | $O(n\lg n)$ | p. 15 |
| rapporto 9:1 | $9n/10$ | $\le T(9n/10) + T(n/10) + cn$ | [[metodo-albero-di-ricorrenza]] | $O(n\lg n)$ | pp. 16–17 |
| medio | buono e cattivo alternati | — | ragionamento sull'albero | $O(n\lg n)$ (intuitivo) | p. 18 |
| peggiore, dimostrazione | qualsiasi | $\max_q(\dots) + \Theta(n)$ | [[metodo-di-sostituzione]] | $\Theta(n^2)$ | pp. 21–22 |

Le sezioni seguenti risolvono le ricorrenze nell'ordine delle slide.

### 1. Caso peggiore — srotolamento della ricorrenza · [[07-Quicksort 1.pdf#page=14|p. 14]]

- Il caso peggiore si presenta quando il partizionamento produce un sottoproblema con $n - 1$ elementi e uno con 0 elementi (dimostrazione in seguito, pp. 21–22).
- Supponendo che un tale partizionamento sbilanciato si verifichi in ogni iterazione, il tempo di esecuzione è
$$ T(n) = T(n-1) + T(0) + \Theta(n) = T(n-1) + \Theta(n) $$
- Intuitivamente, la soluzione è $T(n) = \Theta(n^2)$: si ottiene una serie aritmetica, verificabile con il [[metodo-di-sostituzione]].
- Il tempo di esecuzione di Quicksort nel caso peggiore non è migliore di quello di [[insertion-sort]]. Il caso peggiore di Quicksort si ha quando il vettore è **ordinato**, caso in cui Insertion Sort richiede un tempo $O(n)$.

**Come funziona il metodo** (→ [[equazioni-di-ricorrenza]]). La ricorrenza riduce $n$ di **1** a ogni passo, quindi si può srotolare:
1. si sostituisce $T(n-1)$ con la sua definizione, poi $T(n-2)$, e così via;
2. dopo qualche passo si riconosce la forma generale dopo $k$ passi;
3. si sceglie $k$ in modo da arrivare al caso base;
4. si calcola la somma che è rimasta.

**Applicazione** (🧩), con $cn$ al posto di $\Theta(n)$ e $T(0) = c_0$:
$$
\begin{aligned}
T(n) &= T(n-1) + cn && \text{ricorrenza} \\
     &= T(n-2) + c(n-1) + cn && \text{passo 1: sostituisco } T(n-1) = T(n-2) + c(n-1) \\
     &= T(n-k) + c\sum_{m=n-k+1}^{n} m && \text{passo 2: forma dopo } k \text{ passi} \\
     &= T(0) + c\sum_{m=1}^{n} m && \text{passo 3: } k = n \text{, caso base} \\
     &= c_0 + c\,\frac{n(n+1)}{2} = \Theta(n^2) && \text{passo 4: serie aritmetica (somma di Gauss)}
\end{aligned}
$$

**Quale input lo realizza** (🧩): con il vettore ordinato il pivot $x = A[r]$ è il massimo. Il test $A[j] \le x$ è sempre vero e Partition restituisce $q = r$: $n - 1$ elementi a sinistra (ancora ordinati), 0 a destra, e lo stesso si ripete a ogni livello.

**Verifica** ([[divide_et_impera.py]]): su un array ordinato Partition fa $\frac{n(n-1)}{2}$ confronti in tutto, cioè 4950 per $n = 100$.

### 2. Caso migliore — teorema dell'esperto · Quicksort [[07-Quicksort 1.pdf#page=15|p. 15]] · Merge Sort [[06-Merge Sort (1).pdf#page=44|p. 44]]

- Il caso migliore è quando i due sottoproblemi sono perfettamente bilanciati ad ogni iterazione: dimensioni $\lfloor n/2 \rfloor$ e $\lceil n/2 \rceil - 1$.
- Tempo di esecuzione $T(n) \le 2T(n/2) + \Theta(n)$.
- Soluzione: $T(n) = O(n \lg n)$, dal caso 2 del [[teorema-dell-esperto]].

**Come funziona il metodo**. Il teorema risolve direttamente le ricorrenze della forma $T(n) = aT(n/b) + f(n)$:
1. si riconoscono $a$ (numero di sottoproblemi), $b$ (fattore di riduzione) e $f(n)$ (lavoro fuori dalle chiamate);
2. si calcola $n^{\log_b a}$;
3. si confronta $f(n)$ con $n^{\log_b a}$: più piccola di un fattore polinomiale (caso 1), dello stesso ordine (caso 2), più grande di un fattore polinomiale e regolare (caso 3);
4. si legge la soluzione del caso.

**Applicazione** (🧩):
$$
\begin{aligned}
&a = 2,\quad b = 2,\quad f(n) = \Theta(n) && \text{passo 1: due chiamate su metà, Partition lineare} \\
&n^{\log_b a} = n^{\log_2 2} = n && \text{passo 2} \\
&f(n) = \Theta(n) = \Theta\!\left(n^{\log_b a}\right) && \text{passo 3: stesso ordine} \Rightarrow \text{caso 2} \\
&T(n) = \Theta\!\left(n^{\log_b a}\lg n\right) = \Theta(n\lg n) && \text{passo 4}
\end{aligned}
$$

La slide scrive $O$ perché la ricorrenza è una disuguaglianza ($\le$): le due parti sono **al più** $n/2$. Le loro dimensioni sommano a $\lfloor n/2 \rfloor + \lceil n/2 \rceil - 1 = n - 1$, cioè tutti gli elementi tranne il pivot.

### 3. Rapporto costante 9:1 — albero di ricorrenza · [[07-Quicksort 1.pdf#page=16|p. 16]], [[07-Quicksort 1.pdf#page=17|17]]

- Il tempo medio di esecuzione di Quicksort è più vicino al caso migliore che non al caso peggiore.
- Supponiamo che il partizionamento produca due sottoproblemi la cui dimensione è sempre nel rapporto 9:1:
$$ T(n) \le T(9n/10) + T(n/10) + cn $$
- Utilizziamo il metodo dell'albero di ricorrenza.
- Il costo è $O(n \lg n)$: $\Theta(\lg n)$ livelli, ciascuno di costo al più $cn$.
- Qualunque partizionamento con rapporto *costante* (anche 99:1) produce un costo $O(n \lg n)$, perché la profondità è sempre $\Theta(\lg n)$.

**Perché non il teorema dell'esperto** (🧩): i due sottoproblemi hanno dimensioni diverse ($9n/10$ e $n/10$), quindi la ricorrenza non ha la forma $aT(n/b) + f(n)$ con un unico $b$.

**Come funziona il metodo** (→ [[metodo-albero-di-ricorrenza]]):
1. si disegna l'albero: ogni nodo riporta il **costo locale** della sua chiamata (qui $c$ per la sua dimensione), i figli sono le chiamate ricorsive;
2. si calcola il **costo di ogni livello**, sommando i nodi del livello;
3. si conta il **numero di livelli**, cioè la profondità del ramo più lungo, fino alla dimensione 1;
4. si somma su tutti i livelli (qui basta maggiorare: livelli × costo massimo di un livello).

![[07-quicksort-p17-albero-9-1.png]]
*Albero della ricorrenza 9:1: costo $cn$ per livello fino alla profondità $\log_{10} n$ (dove finisce il ramo più corto), poi $\le cn$ fino a $\log_{10/9} n$ (ramo più lungo).*

**Applicazione** (🧩):
$$
\begin{aligned}
&\text{livello } i:\ \text{i sottoproblemi sono parti disgiunte dell'array} \Rightarrow \textstyle\sum \text{dimensioni} \le n && \text{passo 2} \\
&\text{costo del livello } i \le cn && \text{passo 2: } c \times \text{somma delle dimensioni} \\
&\text{ramo più lungo (sempre } 9/10\text{):}\ \ n\left(\tfrac{9}{10}\right)^i = 1 \iff i = \log_{10/9} n && \text{passo 3} \\
T(n) &\le cn\left(\log_{10/9} n + 1\right) && \text{passo 4: livelli} \times cn \\
     &= cn\left(\frac{\lg n}{\lg(10/9)} + 1\right) = O(n\lg n) && \text{cambio di base: } \lg(10/9) \text{ è una costante}
\end{aligned}
$$

Con 99:1 cambia solo la base del logaritmo, $\log_{100/99} n$: la profondità resta $\Theta(\lg n)$ e il costo $O(n\lg n)$ (→ [[logaritmi-nell-analisi]]).

**Verifica** ([[divide_et_impera.py]]): simulando lo split 9:1 con $n = 10^3$ il ramo più lungo ha 66 livelli, e $\log_{10/9} 10^3 \approx 65.6$.

### 4. Caso medio — partizioni buone e cattive alternate · [[07-Quicksort 1.pdf#page=18|p. 18]], [[07-Quicksort 1.pdf#page=23|p. 23]]

- Nel caso medio, tipicamente partizioni «buone» e «cattive» si alternano.
- Intuitivamente, se si alternano best case e worst case, il tempo di esecuzione complessivo è quello del best case.
- Il costo $\Theta(n-1)$ della partizione cattiva viene assorbito nel costo $\Theta(n)$ della partizione buona, e la partizione risultante è buona.

![[07-quicksort-p18-partizioni-alternate.png]]
*A sinistra: partizione cattiva ($0$ e $n - 1$, costo $\Theta(n)$) seguita da una buona ($\frac{n-1}{2} - 1$ e $\frac{n-1}{2}$, costo $\Theta(n-1)$). A destra: una sola partizione buona ($\frac{n-1}{2}$ e $\frac{n-1}{2}$, costo $\Theta(n)$).*

**Come si legge con l'albero** (🧩): si confrontano due pezzi di albero.
- A sinistra, dopo **due** livelli si arriva a sottoproblemi di dimensione circa $\frac{n-1}{2}$, spendendo $\Theta(n) + \Theta(n-1) = \Theta(n)$.
- A destra, dopo **un** livello si arriva agli stessi sottoproblemi, spendendo $\Theta(n)$.
- Il costo per arrivare agli stessi sottoproblemi è dello stesso ordine. L'albero con le partizioni alternate ha al più il doppio dei livelli, cioè ancora $\Theta(\lg n)$, con costo $O(n)$ per coppia di livelli: il totale resta $O(n\lg n)$.

È un argomento intuitivo: la dimostrazione del tempo atteso riguarda la versione randomizzata ed è sul libro di testo (→ [[quicksort-randomizzato]]).

### 5. Dimostrazione del caso peggiore — metodo di sostituzione · Quicksort [[07-Quicksort 1.pdf#page=21|p. 21]], [[07-Quicksort 1.pdf#page=22|22]] · Merge Sort [[06-Merge Sort (1).pdf#page=30|p. 30]]

Dimostriamo che il tempo di esecuzione è $\Theta(n^2)$ nel caso peggiore, dimostrando prima con il metodo di sostituzione che $T(n) = O(n^2)$:

$$
\begin{aligned}
T(n) &= \max_{0 \le q \le n-1} \big(T(q) + T(n-q-1)\big) + \Theta(n) \\
     &\le \max_{0 \le q \le n-1} \big(cq^2 + c(n-q-1)^2\big) + \Theta(n) \\
     &= c \cdot \max_{0 \le q \le n-1} \big(q^2 + (n-q-1)^2\big) + \Theta(n) \\
     &\le c(n-1)^2 + \Theta(n) \\
     &= cn^2 - c(2n-1) + \Theta(n) \\
     &\le cn^2
\end{aligned}
$$

La funzione ha la concavità verso l'alto (la derivata seconda rispetto a $q$ è positiva), quindi il massimo è assunto agli estremi.

In precedenza abbiamo visto un caso (il caso sbilanciato) in cui il tempo di esecuzione è $\Theta(n^2)$. Quindi il tempo di esecuzione nel caso peggiore è $\Omega(n^2)$. Combinando questo risultato con quello della slide precedente, il tempo di esecuzione nel caso peggiore è $\Theta(n^2)$.

![[07-quicksort-p21-worst-case-sostituzione.png]]

**Perché serve questo metodo** (🧩): il caso 1 ha **supposto** che la partizione peggiore fosse quella sbilanciata. Per dimostrarlo bisogna considerare **tutte** le possibili divisioni, cioè il $\max$ su $q$. Una ricorrenza con un $\max$ non si srotola e non ha la forma del teorema dell'esperto; si può però verificare una soluzione ipotizzata.

**Come funziona il metodo** (→ [[metodo-di-sostituzione]]):
1. si **ipotizza** la soluzione: $T(n) \le cn^2$;
2. si **assume** che valga per tutte le dimensioni più piccole di $n$ (ipotesi induttiva);
3. la si **sostituisce** nella ricorrenza e si dimostra che ne segue $T(n) \le cn^2$ con la **stessa** costante $c$;
4. si controllano i **casi base**.

**Applicazione** (🧩), riga per riga della catena della slide:
1. **Prima riga:** è la ricorrenza dell'impostazione iniziale, con il $\max$ su tutte le dimensioni $q$ possibili della parte sinistra.
2. **Seconda riga — passo 2 del metodo:** ipotesi induttiva $T(k) \le ck^2$ per ogni $k < n$, applicata sia a $q$ sia a $n - q - 1$. Serve per **ogni** $k < n$ (induzione forte), perché $q$ può essere qualsiasi.
3. **Terza riga:** si raccoglie $c > 0$, che non sposta il punto di massimo.
4. **Quarta riga:** $f(q) = q^2 + (n-q-1)^2$ ha $f''(q) = 2 + 2 = 4 > 0$, quindi è convessa e sull'intervallo $[0, n-1]$ ha il massimo agli estremi: $f(0) = f(n-1) = (n-1)^2$.
5. **Quinta riga:** $c(n-1)^2 = cn^2 - 2cn + c = cn^2 - c(2n-1)$.
6. **Sesta riga — passo 3 del metodo:** se $c'n$ maggiora il termine $\Theta(n)$, serve $c(2n-1) \ge c'n$. Poiché $2n - 1 \ge n$, basta scegliere $c \ge c'$: si ottiene $T(n) \le cn^2$ con la stessa $c$ dell'ipotesi.
7. **Passo 4, casi base** (la slide non li tratta): per $n = 1$ basta $c \ge T(1)$. $T(0)$ non può essere $\le c \cdot 0^2 = 0$; quando $q = 0$ o $q = n - 1$ il termine $T(0)$ è una costante e si assorbe nel $\Theta(n)$.

**Limite inferiore**: il $\max$ è almeno il valore per $q = n - 1$, cioè la ricorrenza sbilanciata del caso 1, che vale $\Theta(n^2)$. Quindi il caso peggiore è $\Omega(n^2)$, e con il limite superiore $\Theta(n^2)$.

> 🎯 Esame: scrivere $T(n) = T(q) + T(n-q-1) + \Theta(n)$ dallo pseudocodice; per ogni caso dire quale $q$ lo realizza, quale metodo si usa e perché; svolgere lo srotolamento del caso peggiore, il teorema dell'esperto del caso migliore, l'albero del 9:1 e la sostituzione con il massimo agli estremi.

### Spazio · [[07-Quicksort 1.pdf#page=2|p. 2]]

> 🧩 Derivazione mia: [[partition]] usa $\Theta(1)$ memoria, quindi Quicksort è **sul posto** quanto ai dati. La pila delle chiamate però è profonda quanto l'albero di ricorsione: $\Theta(\lg n)$ nel caso bilanciato, $\Theta(n)$ nel caso peggiore (99 livelli per $n = 100$ ordinato in [[divide_et_impera.py]]).

## Proprietà · [[07-Quicksort 1.pdf#page=2|p. 2]], [[07-Quicksort 1.pdf#page=14|p. 14]]

- **Sul posto**.
- **Non stabile** — 🧩 derivabile da [[partition]] § Proprietà.
- **Sensibile all'input** — 🧩: il costo dipende dall'ordine iniziale; l'input già ordinato è il peggiore (con pivot $A[r]$), al contrario di [[insertion-sort]] per cui è il migliore.

## Connessioni

- [[partition]] — il Divide, $\Theta(n)$
- [[quicksort-randomizzato]] — pivot casuale: nessun input fisso è sistematicamente cattivo
- [[merge-sort]] — stesso paradigma; $\Theta(n\lg n)$ garantito ma non sul posto
- [[insertion-sort]] — stesso caso peggiore $\Theta(n^2)$, ma su input opposti
- [[metodo-di-sostituzione]], [[metodo-albero-di-ricorrenza]], [[teorema-dell-esperto]] — tutti e tre usati nell'analisi
- [[casi-di-complessita]] — migliore, peggiore e medio con ordini diversi
- [[ordinamento]] — tabella comparativa

## Fonti · [[07-Quicksort 1.pdf#page=2|p. 2]], [[07-Quicksort 1.pdf#page=4|p. 4]], [[07-Quicksort 1.pdf#page=14|p. 14]], [[07-Quicksort 1.pdf#page=18|p. 18]], [[07-Quicksort 1.pdf#page=21|p. 21]], [[07-Quicksort 1.pdf#page=22|22]]

- [[lezione-07-quicksort]]

_Aggiornato: 2026-10-01 — ingest 07-Quicksort.pdf_
_Aggiornato: 2026-10-10 — link ripuntati alla versione aggiornata delle slide 06-Merge Sort (1).pdf_
_Aggiornato: 2026-10-14 — versione aggiornata delle slide (07-Quicksort 1.pdf): annotazioni di p. 4; sezione Complessità riorganizzata per metodo_

<!-- nav:inizio -->
---
**Lezione 07 · pagina 2 di 7** · ← [[lezione-07-quicksort|Lezione 07: introduzione e riepilogo]] · [[lezioni|Indice]] · [[partition|Partition]] →
<!-- nav:fine -->
