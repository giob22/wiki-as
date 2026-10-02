---
tipo: entità
categoria: algoritmo
paradigma: "[[divide-et-impera]]"
fonti_pdf: ["07-Quicksort.pdf#page=2", "07-Quicksort.pdf#page=3", "07-Quicksort.pdf#page=4", "07-Quicksort.pdf#page=14", "07-Quicksort.pdf#page=15", "07-Quicksort.pdf#page=16", "07-Quicksort.pdf#page=17", "07-Quicksort.pdf#page=18", "07-Quicksort.pdf#page=21", "07-Quicksort.pdf#page=22"]
---

# Quicksort

Le sezioni seguono l'ordine delle slide: proprietà (p. 2) → divide et impera (p. 3) → pseudocodice (p. 4) → [[partition]] (pp. 5–13) → casi peggiore, migliore, bilanciato e medio (pp. 14–18) → dimostrazione del caso peggiore (pp. 21–22). La versione randomizzata (pp. 19–20, 23) ha una pagina a sé: [[quicksort-randomizzato]].

## Problema risolto

[[ordinamento]] di un array $A[1..n]$, **sul posto**.

## Idea

> 📄 Fonte: [[07-Quicksort.pdf#page=2]]

Quick Sort ha un tempo di esecuzione:
- $\Theta(n^2)$ nel caso peggiore;
- $\Theta(n \lg n)$ nel caso «medio»;
- ordina sul posto.

Nella pratica risulta essere tra i più efficienti, grazie al fatto che i fattori «nascosti» in $\Theta(n \lg n)$ sono piuttosto piccoli.

> 💡 Connessione: i «fattori nascosti» sono le costanti che la [[notazione-asintotica]] ignora. A parità di $\Theta(n\lg n)$ conta la costante: è la stessa osservazione delle costanti nascoste di [[efficienza-degli-algoritmi]].

> 📄 Fonte: [[07-Quicksort.pdf#page=3]]

Utilizza un approccio **[[divide-et-impera]]**:
- **Divide** — scelto un elemento $x$, detto *pivot*, partiziona l'array $A[p..r]$ in due sottoarray tali che $A[p..q-1]$ contiene gli elementi $\le x$ e $A[q+1..r]$ contiene gli elementi $> x$; il pivot va in $A[q]$.
- **Conquer** — ordina i due sottoarray mediante chiamate ricorsive.
- **Combine** — i sottoarray sono ordinati sul posto, quindi non occorre fare nulla.

![[07-quicksort-p3-divide-conquer-combine.png]]

> 🧩 Spiegazione mia — perché il Combine è vuoto: dopo il Divide ogni elemento di $A[p..q-1]$ è $\le x \le$ ogni elemento di $A[q+1..r]$. Se le due parti vengono ordinate, l'intero $A[p..r]$ è già ordinato. In [[merge-sort]] succede il contrario: Divide banale, Combine $\Theta(n)$.

## Pseudocodice

> 📄 Fonte: [[07-Quicksort.pdf#page=4]] (riportato fedelmente, numeri di riga miei)

```
Quicksort (A,p,r)
1  if p<r
2      q ← Partition (A,p,r)
3      Quicksort (A,p,q-1)
4      Quicksort (A,q+1,r)
```

Per ordinare l'intero array si invoca `Quicksort (A,1,length[A])`.

Simboli: $A[p..r]$ = sotto-array da ordinare; $q$ = posizione finale del pivot restituita da [[partition]]. Il pivot $A[q]$ è già al suo posto definitivo e non partecipa alle chiamate ricorsive.

## Esempio di esecuzione

![[animazione-quicksort.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo sull'array delle slide 07 pp. 5–12, ⟨2, 8, 7, 1, 3, 5, 6, 4⟩. Le slide tracciano solo la prima Partition; l'animazione prosegue con tutte le chiamate ricorsive. In giallo il sotto-array della chiamata attiva ($p$ e $r$ indicati sopra), in verde i pivot già al loro posto definitivo.

> 🧩 Derivazione mia — albero delle chiamate (la prima riga è la traccia di [[07-Quicksort.pdf#page=7]]–[[07-Quicksort.pdf#page=11]]; il resto è verificato con [[divide_et_impera.py]]):

| Chiamata | $A[p..r]$ prima | pivot | $q$ | $A[p..r]$ dopo Partition |
|----------|-----------------|-------|-----|--------------------------|
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

## Correttezza

La correttezza di [[partition]] è dimostrata con l'invariante di [[07-Quicksort.pdf#page=13]].

> 🧩 Derivazione mia — [[correttezza-per-induzione]] forte su $n = r - p + 1$:
> - **Base** ($n \le 1$): `p<r` è falso, nessuna operazione; un sotto-array di 0 o 1 elementi è ordinato.
> - **Passo** ($n \ge 2$): Partition restituisce $q$ con $A[p..q-1] \le A[q] < A[q+1..r]$. Le due chiamate lavorano su $q - p$ e $r - q$ elementi, entrambi $\le n - 1$, quindi per ipotesi induttiva al ritorno le due parti sono ordinate. Non toccano $A[q]$ né scambiano elementi tra le due parti, quindi la proprietà del Divide resta vera e $A[p..r]$ è ordinato.
> - **Terminazione:** il pivot è escluso da entrambe le chiamate, quindi la dimensione scende di almeno 1.

## Complessità

### Caso peggiore: partizionamento sbilanciato
> 📄 Fonte: [[07-Quicksort.pdf#page=14]]

- Il caso peggiore si presenta quando il partizionamento produce un sottoproblema con $n - 1$ elementi e uno con 0 elementi (dimostrazione in seguito, pp. 21–22).
- Supponendo che un tale partizionamento sbilanciato si verifichi in ogni iterazione, il tempo di esecuzione è
$$ T(n) = T(n-1) + T(0) + \Theta(n) = T(n-1) + \Theta(n) $$
- Intuitivamente, la soluzione è $T(n) = \Theta(n^2)$: si ottiene una serie aritmetica, verificabile con il [[metodo-di-sostituzione]].
- Il tempo di esecuzione di Quicksort nel caso peggiore non è migliore di quello di [[insertion-sort]]. Il caso peggiore di Quicksort si ha quando il vettore è **ordinato**, caso in cui Insertion Sort richiede un tempo $O(n)$.

### Derivazione — la serie aritmetica
**Fonte:** [[07-Quicksort.pdf#page=14]] («si ottiene una serie aritmetica», senza passaggi)
**Si parte da:** $T(n) = T(n-1) + cn$, con $cn$ al posto di $\Theta(n)$ (costo di [[partition]]) e $T(0) = c_0$ costante

> 🧩 Derivazione mia:

$$
\begin{aligned}
T(n) &= T(n-1) + cn && \text{ricorrenza} \\
     &= T(n-2) + c(n-1) + cn && \text{ricorrenza su } n-1 \\
     &= T(n-k) + c\sum_{m=n-k+1}^{n} m && \text{dopo } k \text{ passi} \\
     &= T(0) + c\sum_{m=1}^{n} m && k = n \\
     &= c_0 + c\,\frac{n(n+1)}{2} && \text{somma di Gauss (serie aritmetica)} \\
     &= \Theta(n^2) && \tfrac{c}{2} n^2 \text{ domina}
\end{aligned}
$$

> 🧩 Perché il vettore **ordinato** realizza questo caso: il pivot $x = A[r]$ è il **massimo** di $A[p..r]$. Il test $A[j] \le x$ è sempre vero, $i$ arriva a $r - 1$ e Partition restituisce $q = r$: a sinistra $n - 1$ elementi (ancora ordinati), a destra 0. La situazione si ripete a ogni livello.
>
> **Sanity check** ([[divide_et_impera.py]]): su un array ordinato i confronti di Partition sono $(n-1) + (n-2) + \dots + 1 = \frac{n(n-1)}{2}$: 45, 4950, 499500 per $n = 10, 100, 1000$, con profondità di ricorsione $n - 1$. Su un array casuale sono 23, 646, 11082.

### Caso migliore: partizionamento bilanciato
> 📄 Fonte: [[07-Quicksort.pdf#page=15]]

- Il caso migliore è quando i due sottoproblemi sono perfettamente bilanciati ad ogni iterazione: dimensioni $\lfloor n/2 \rfloor$ e $\lceil n/2 \rceil - 1$.
- Tempo di esecuzione $T(n) \le 2T(n/2) + \Theta(n)$.
- Soluzione: $T(n) = O(n \lg n)$, dal caso 2 del [[teorema-dell-esperto]].

> 🧩 Derivazione mia:
> - Le due dimensioni sommano a $\lfloor n/2 \rfloor + \lceil n/2 \rceil - 1 = n - 1$: tutti gli elementi tranne il pivot.
> - Teorema dell'esperto con $a = 2$, $b = 2$, $f(n) = \Theta(n)$: $n^{\log_b a} = n^{\log_2 2} = n$, e $f(n) = \Theta(n^{\log_b a})$ ⇒ caso 2 ⇒ $\Theta(n^{\log_b a} \lg n) = \Theta(n \lg n)$.
> - La slide scrive $O$ perché la ricorrenza è una disuguaglianza ($\le$): le due metà sono al più $n/2$.

### Partizionamento con rapporto costante (9:1)
> 📄 Fonte: [[07-Quicksort.pdf#page=16]], [[07-Quicksort.pdf#page=17]]

- Il tempo medio di esecuzione di Quicksort è più vicino al caso migliore che non al caso peggiore.
- Supponiamo che il partizionamento produca due sottoproblemi la cui dimensione è sempre nel rapporto 9:1:
$$ T(n) \le T(9n/10) + T(n/10) + cn $$
- Utilizziamo il [[metodo-albero-di-ricorrenza]].
- Il costo è $O(n \lg n)$: $\Theta(\lg n)$ livelli, ciascuno di costo al più $cn$.
- Qualunque partizionamento con rapporto *costante* (anche 99:1) produce un costo $O(n \lg n)$, perché la profondità è sempre $\Theta(\lg n)$.

![[07-quicksort-p17-albero-9-1.png]]
*Albero della ricorrenza 9:1: costo $cn$ per livello fino alla profondità $\log_{10} n$ (dove finisce il ramo più corto), poi $\le cn$ fino a $\log_{10/9} n$ (ramo più lungo). ([[07-Quicksort.pdf#page=17]])*

### Derivazione — 9:1 costa $O(n \lg n)$
**Fonte:** [[07-Quicksort.pdf#page=17]] (albero disegnato, somma senza passaggi)

> 🧩 Derivazione mia:

$$
\begin{aligned}
&\text{livello } i:\ \text{i sottoproblemi sono parti disgiunte dell'array} \Rightarrow \textstyle\sum \text{dimensioni} \le n && \\
&\text{costo del livello } i \le c \cdot n && cn \text{ per ogni nodo di dimensione } n' \text{, sommato} \\
&\text{ramo più corto (sempre } 1/10\text{):}\ \ n \left(\tfrac{1}{10}\right)^i = 1 \iff i = \log_{10} n && \text{fin qui i livelli sono completi: costo } cn \\
&\text{ramo più lungo (sempre } 9/10\text{):}\ \ n \left(\tfrac{9}{10}\right)^i = 1 \iff i = \log_{10/9} n && \text{profondità dell'albero} \\
T(n) &\le cn \left(\log_{10/9} n + 1\right) && \text{livelli} \times \text{costo massimo} \\
     &= cn\left(\frac{\lg n}{\lg(10/9)} + 1\right) \approx 6.58\, cn \lg n + cn && \text{cambio di base, } \lg(10/9) \approx 0.152 \\
     &= O(n \lg n)
\end{aligned}
$$

> Con 99:1 la profondità è $\log_{100/99} n = \lg n / \lg(100/99) \approx 69\, \lg n$: costante più grande, stesso $\Theta(\lg n)$. La base del logaritmo cambia solo la costante ([[logaritmi-nell-analisi]]).
>
> Il limite è stretto: i primi $\log_{10} n$ livelli sono completi e costano $cn$ ciascuno, quindi $T(n) \ge cn \log_{10} n = \Omega(n \lg n)$.
>
> **Sanity check** ([[divide_et_impera.py]]): simulando lo split 9:1, il ramo più lungo ha 66 livelli per $n = 10^3$ ($\log_{10/9} 10^3 \approx 65.6$) e 132 per $n = 10^6$ ($\approx 131.1$).
> **Ipotesi:** rapporto **costante** a ogni livello. Se lo sbilanciamento cresce con $n$ (es. sempre $n - 1$ e 0) la profondità diventa $\Theta(n)$.

### Caso medio
> 📄 Fonte: [[07-Quicksort.pdf#page=18]]

- Nel caso medio, tipicamente partizioni «buone» e «cattive» si alternano.
- Intuitivamente, se si alternano best case e worst case, il tempo di esecuzione complessivo è quello del best case.
- Il costo $\Theta(n-1)$ della partizione cattiva viene assorbito nel costo $\Theta(n)$ della partizione buona, e la partizione risultante è buona.

![[07-quicksort-p18-partizioni-alternate.png]]
*A sinistra: partizione cattiva ($0$ e $n - 1$, costo $\Theta(n)$) seguita da una buona ($\frac{n-1}{2} - 1$ e $\frac{n-1}{2}$, costo $\Theta(n-1)$). A destra: una sola partizione buona ($\frac{n-1}{2}$ e $\frac{n-1}{2}$, costo $\Theta(n)$). ([[07-Quicksort.pdf#page=18]])*

> 🧩 Derivazione mia — cosa dice la figura:
> - a sinistra, dopo **due** livelli si ottengono sottoproblemi di dimensione $\frac{n-1}{2} - 1$ e $\frac{n-1}{2}$, con costo $\Theta(n) + \Theta(n-1) = \Theta(n)$;
> - a destra, dopo **un** livello si ottengono sottoproblemi di dimensione $\frac{n-1}{2}$, con costo $\Theta(n)$;
> - stessi sottoproblemi (a meno di un elemento), stesso ordine di costo: la coppia «cattiva + buona» vale quanto una partizione buona con una costante più grande. L'albero ha al più il doppio dei livelli, cioè ancora $\Theta(\lg n)$, e il totale resta $O(n \lg n)$.
>
> È un argomento **intuitivo**: la dimostrazione rigorosa del tempo atteso riguarda la versione randomizzata, ed è rimandata al libro di testo ([[07-Quicksort.pdf#page=23]], → [[quicksort-randomizzato]]).

### Dimostrazione del caso peggiore
> 📄 Fonte: [[07-Quicksort.pdf#page=21]], [[07-Quicksort.pdf#page=22]]

Dimostriamo che il tempo di esecuzione è $\Theta(n^2)$ nel caso peggiore, dimostrando prima con il [[metodo-di-sostituzione]] che $T(n) = O(n^2)$:

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

> 🧩 Derivazione mia — i passaggi della catena, uno per riga:
> 1. **Prima riga:** qui $q$ è la **dimensione** del sottoproblema sinistro (non l'indice restituito da Partition): il pivot esclude un elemento, quindi il destro ha $n - q - 1$ elementi. Il caso peggiore è il $\max$ su tutte le possibili divisioni; $\Theta(n)$ è il costo di [[partition]].
> 2. **Seconda riga:** ipotesi induttiva $T(k) \le ck^2$ per ogni $k < n$, applicata a $q$ e $n - q - 1$, entrambi $\le n - 1$.
> 3. **Terza riga:** si raccoglie la costante $c > 0$, che non cambia il punto di massimo.
> 4. **Quarta riga:** sia $f(q) = q^2 + (n-q-1)^2$. Allora $f'(q) = 2q - 2(n-q-1)$ e $f''(q) = 2 + 2 = 4 > 0$: $f$ è convessa e sull'intervallo $[0, n-1]$ ha il massimo in un estremo. $f(0) = f(n-1) = (n-1)^2$.
> 5. **Quinta riga:** $c(n-1)^2 = cn^2 - 2cn + c = cn^2 - c(2n-1)$.
> 6. **Sesta riga:** sia $c'n$ un maggiorante del termine $\Theta(n)$ (per $n \ge 1$). Serve $c(2n-1) \ge c'n$. Poiché $2n - 1 \ge n$ per $n \ge 1$, basta scegliere $c \ge c'$.
>
> **Caso base** (la slide non lo tratta): $T(0)$ è una costante positiva e non può essere $\le c \cdot 0^2 = 0$, lo stesso problema di [[06-Merge Sort.pdf#page=19]]. Si risolve così: quando $q = 0$ o $q = n - 1$ il termine $T(0)$ non va maggiorato con l'ipotesi, perché è una costante assorbita nel $\Theta(n)$. Per $n = 1$ basta $c \ge T(1)$.
>
> **Perché anche $\Omega(n^2)$:** il $\max$ nella prima riga è almeno il valore per $q = n - 1$, che dà la ricorrenza sbilanciata $T(n-1) + T(0) + \Theta(n) = \Theta(n^2)$ di p. 14. Esiste quindi un input (l'array ordinato) che costa $\Theta(n^2)$.

> 🎯 Esame: perché il caso peggiore è $\Theta(n^2)$ e quale input lo realizza; perché uno split 9:1 (o 99:1) dà comunque $O(n \lg n)$; la dimostrazione per sostituzione con il massimo agli estremi.

### Spazio

> 🧩 Derivazione mia: [[partition]] usa $\Theta(1)$ memoria, quindi Quicksort è **sul posto** ([[07-Quicksort.pdf#page=2]]) quanto ai dati. La pila delle chiamate però è profonda quanto l'albero di ricorsione: $\Theta(\lg n)$ nel caso bilanciato, $\Theta(n)$ nel caso peggiore (99 livelli per $n = 100$ ordinato in [[divide_et_impera.py]]).

## Proprietà

- **Sul posto** ([[07-Quicksort.pdf#page=2]]).
- **Non stabile** — 🧩 derivabile da [[partition]] § Proprietà.
- **Sensibile all'input** — 🧩: il costo dipende dall'ordine iniziale; l'input già ordinato è il peggiore (con pivot $A[r]$), al contrario di [[insertion-sort]] per cui è il migliore ([[07-Quicksort.pdf#page=14]]).

## Connessioni

- [[partition]] — il Divide, $\Theta(n)$
- [[quicksort-randomizzato]] — pivot casuale: nessun input fisso è sistematicamente cattivo
- [[merge-sort]] — stesso paradigma; $\Theta(n\lg n)$ garantito ma non sul posto
- [[insertion-sort]] — stesso caso peggiore $\Theta(n^2)$, ma su input opposti
- [[metodo-di-sostituzione]], [[metodo-albero-di-ricorrenza]], [[teorema-dell-esperto]] — tutti e tre usati nell'analisi
- [[casi-di-complessita]] — migliore, peggiore e medio con ordini diversi
- [[ordinamento]] — tabella comparativa

## Fonti

- [[lezione-07-quicksort]]
- [[07-Quicksort.pdf#page=2]]–[[07-Quicksort.pdf#page=4]], [[07-Quicksort.pdf#page=14]]–[[07-Quicksort.pdf#page=18]], [[07-Quicksort.pdf#page=21]], [[07-Quicksort.pdf#page=22]]

_Aggiornato: 2026-10-01 — ingest 07-Quicksort.pdf_
