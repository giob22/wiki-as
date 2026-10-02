---
tipo: esercizio
argomento: "costo di algoritmi ricorsivi"
difficoltà: media
---

# Scrivere e risolvere equazioni di ricorrenza

## Metodo

1. Dallo pseudocodice ricorsivo: **caso base** → valore di $T$ sul caso base (costo costante).
2. **Caso ricorsivo**: $T(n) =$ (somma dei $T$ delle chiamate ricorsive, con i loro argomenti) $+$ (costo del lavoro locale: confronti, somme, return). Per un algoritmo divide et impera: $T(n) = aT(n/b) + D(n) + C(n)$ ([[06-Merge Sort.pdf#page=14]]).
3. Scegliere il metodo di soluzione (🧩 criterio mio, dagli esempi delle lezioni 03, 06, 07):
   - sottoproblemi di dimensione $n - 1$ (o $n - k$): **srotolare** (sostituzione iterata), individuare la forma generale dopo $k$ passi, **verificarla per induzione**, scegliere $k$ per arrivare al caso base;
   - forma $aT(n/b) + f(n)$ con $a \ge 1$, $b > 1$: provare il [[teorema-dell-esperto]] (calcolare $n^{\log_b a}$ e confrontarlo con $f(n)$);
   - teorema non applicabile (gap, divisioni sbilanciate come 9:1): [[metodo-albero-di-ricorrenza]] per una soluzione di tentativo;
   - soluzione ipotizzata con approssimazioni: verificarla con il [[metodo-di-sostituzione]], costanti esplicite e casi base.
4. Esprimere il risultato in forma chiusa e in [[notazione-asintotica]].

## Strumenti usati

- [[equazioni-di-ricorrenza]], [[correttezza-per-induzione]] (per verificare la forma generale)
- [[metodo-di-sostituzione]], [[metodo-albero-di-ricorrenza]], [[teorema-dell-esperto]]
- Serie aritmetica $\sum_{m=1}^{n} m = \frac{n(n+1)}{2}$; serie geometrica $\sum_{i=0}^{\infty} x^i = \frac{1}{1-x}$ per $|x| < 1$; identità $a^{\log_b n} = n^{\log_b a}$

## Casi svolti

### Caso 1 — somma ricorsiva
**Traccia:** [[03-Analisi di algoritmi.pdf#page=30]]–[[03-Analisi di algoritmi.pdf#page=33]]: costo di `somma_ricorsiva(n)`.

```
funzione somma_ricorsiva(n)
1  se n = 0
2      ritorna 0
3  altrimenti
4      ritorna n + somma_ricorsiva(n − 1)
```

**Ricorrenza** ([[03-Analisi di algoritmi.pdf#page=31]], [[03-Analisi di algoritmi.pdf#page=32]]): $T(0) = 1$ (un confronto e un return), $T(i) = T(i-1) + c$ per $0 < i \le n$ (una chiamata, una somma, un return).

$$
\begin{aligned}
T(n) &= T(n-1) + c = T(n-2) + 2c = T(n-3) + 3c && \text{tre passi di srotolamento} \\
     &= T(n-k) + kc && \text{forma generale} \\
     &= T(0) + nc && k = n \\
     &= 1 + cn = \Theta(n)
\end{aligned}
$$

Verifica della forma generale per induzione su $k$: in [[equazioni-di-ricorrenza]].

**Risultato:** $T(n) = 1 + cn = O(n)$ ([[03-Analisi di algoritmi.pdf#page=33]]). **Spazio** (🧩): $\Theta(n)$, profondità della ricorsione $n + 1$.

**Sanity check:** $T(1) = 1 + c$; con $c = 1$ lo script [[somma_primi_n.py]] misura $T(n) = n + 1$.

### Caso 2 — merge sort: scrivere la ricorrenza e risolverla con l'albero
**Traccia:** [[06-Merge Sort.pdf#page=13]]–[[06-Merge Sort.pdf#page=15]].

- Dallo pseudocodice: $D(n) = \Theta(1)$ (calcolo di $q$), $a = b = 2$ (due chiamate su metà), $C(n) = \Theta(n)$ ([[merge]]) ⇒ $T(n) = 2T(n/2) + \Theta(n)$ ([[06-Merge Sort.pdf#page=14]]).
- Con $n$ potenza di 2 e $T(1) = c$: livello $i$ = $2^i$ nodi da $cn/2^i$ = $cn$; livelli $\lg n + 1$; totale $cn(\lg n + 1) = \Theta(n\lg n)$ ([[06-Merge Sort.pdf#page=15]]).
- Passaggi completi e verifica per induzione in [[merge-sort]] § Complessità.

**Risultato:** $\Theta(n\lg n)$. Controllo con il teorema dell'esperto: caso 2.

### Caso 3 — sostituzione: $T(n) = 2T(\lfloor n/2 \rfloor) + n$, $T(1) = 1$
**Traccia:** [[06-Merge Sort.pdf#page=18]]–[[06-Merge Sort.pdf#page=20]]: dimostrare $T(n) = O(n\lg n)$.

$$
\begin{aligned}
T(n) &\le 2c\lfloor n/2 \rfloor\lg\lfloor n/2 \rfloor + n \le cn\lg(n/2) + n && \text{ipotesi induttiva, } \lfloor n/2 \rfloor \le n/2 \\
     &= cn\lg n - (c-1)n \le cn\lg n && c \ge 1
\end{aligned}
$$

- Casi base: $n = 1$ non va ($c\lg 1 = 0 < 1$); si usano $T(2) = 4 \le 2c$ e $T(3) = 5 \le 3c\lg 3$, quindi $c \ge 2$, $n_0 = 2$.
- Due casi base perché dimezzando da $n \ge 4$ si arriva a 2 o a 3, mai a 1 ([[06-Merge Sort.pdf#page=20]]).
- Passaggi commentati in [[metodo-di-sostituzione]].

**Risultato:** $T(n) \le 2n\lg n$ per $n \ge 2$; [[divide_et_impera.py]] conferma $\max T(n)/(n\lg n) = 2$.

### Caso 4 — albero + sostituzione: $T(n) = 3T(\lfloor n/4 \rfloor) + \Theta(n^2)$
**Traccia:** [[06-Merge Sort.pdf#page=22]]–[[06-Merge Sort.pdf#page=27]].

1. Albero di $3T(n/4) + cn^2$: livello $i$ con $3^i$ nodi da $c(n/4^i)^2$, cioè $(3/16)^i cn^2$; $\log_4 n$ livelli interni; $n^{\log_4 3}$ foglie.
2. Somma: $T(n) < \sum_{i \ge 0}(3/16)^i cn^2 + \Theta(n^{\log_4 3}) = \frac{16}{13}cn^2 + \Theta(n^{\log_4 3}) = O(n^2)$.
3. Verifica: $T(n) \le 3d(n/4)^2 + cn^2 = \frac{3}{16}dn^2 + cn^2 \le dn^2$ se $d \ge \frac{16}{13}c$; caso base $d \ge T(1)$.
4. Limite inferiore: la radice costa già $\Theta(n^2)$ ⇒ $\Omega(n^2)$ ⇒ $\Theta(n^2)$.

Passaggi riga per riga in [[metodo-albero-di-ricorrenza]].

**Risultato:** $T(n) = \Theta(n^2)$; [[divide_et_impera.py]] trova $\max T(n)/n^2 = 1.2308 \approx \frac{16}{13}$ con $c = 1$.

### Caso 5 — teorema dell'esperto: quattro ricorrenze
**Traccia:** [[06-Merge Sort.pdf#page=29]], [[06-Merge Sort.pdf#page=30]].

| Ricorrenza | $a$ | $b$ | $f(n)$ | $n^{\log_b a}$ | Confronto | Caso | $T(n)$ |
|------------|-----|-----|--------|----------------|-----------|------|--------|
| $9T(n/3) + n$ | 9 | 3 | $n$ | $n^2$ | $f = O(n^{2-1})$, $\epsilon = 1$ | 1 | $\Theta(n^2)$ |
| $T(2n/3) + 1$ | 1 | 3/2 | 1 | $n^0 = 1$ | $f = \Theta(1)$ | 2 | $\Theta(\lg n)$ |
| $3T(n/4) + n\lg n$ | 3 | 4 | $n\lg n$ | $n^{0.793}$ | $f = \Omega(n^{0.793+0.2})$; $3\frac{n}{4}\lg\frac{n}{4} \le \frac34 n\lg n$ | 3 | $\Theta(n\lg n)$ |
| $2T(n/2) + n\lg n$ | 2 | 2 | $n\lg n$ | $n$ | $f/n = \lg n$, non polinomiale | gap | — |

Spiegazioni, verifiche numeriche e soluzione $\Theta(n\lg^2 n)$ dell'ultima con l'albero (🧩) in [[teorema-dell-esperto]].

### Caso 6 — quicksort: caso peggiore, migliore, 9:1
**Traccia:** [[07-Quicksort.pdf#page=14]]–[[07-Quicksort.pdf#page=17]], [[07-Quicksort.pdf#page=21]], [[07-Quicksort.pdf#page=22]].

- **Sbilanciato:** $T(n) = T(n-1) + \Theta(n)$: srotolando, $T(0) + c\sum_{m=1}^{n} m = c_0 + c\frac{n(n+1)}{2} = \Theta(n^2)$ (serie aritmetica).
- **Bilanciato:** $T(n) \le 2T(n/2) + \Theta(n)$: esperto, caso 2, $O(n\lg n)$.
- **9:1:** $T(n) \le T(9n/10) + T(n/10) + cn$: albero con livelli di costo $\le cn$ e profondità $\log_{10/9} n \approx 6.58\lg n$ ⇒ $O(n\lg n)$.
- **Caso peggiore in generale:** $T(n) = \max_{0 \le q \le n-1}(T(q) + T(n-q-1)) + \Theta(n) \le c(n-1)^2 + \Theta(n) \le cn^2$ (massimo agli estremi perché $q^2 + (n-q-1)^2$ è convessa); con il caso sbilanciato, $\Theta(n^2)$.

Passaggi completi in [[quicksort]] § Complessità.

### Caso 7 — Torre di Hanoi (ricorrenza con $n - 1$)
**Traccia:** [[06-Merge Sort.pdf#page=4]] (7 mosse per 3 dischi; ricorrenza mia, 🧩).

$M(n) = 2M(n-1) + 1$, $M(0) = 0$ ⇒ srotolando $M(n) = 2^k M(n-k) + \sum_{m=0}^{k-1} 2^m$ ⇒ con $k = n$, $M(n) = 2^n - 1$. Passaggi in [[torre-di-hanoi]].

## Trappole

- Dimenticare il caso base (la ricorrenza senza $T(0)$ non determina $T$).
- Srotolare senza verificare la forma generale.
- Confondere il **tempo** $\Theta(n)$ con lo **spazio**: nella versione ricorsiva anche lo spazio è $\Theta(n)$, nella iterativa è $\Theta(1)$ ([[iterazione-e-ricorsione]]).
- Sostituzione: chiudere l'induzione con una costante diversa da quella dell'ipotesi; scegliere un caso base dove la disuguaglianza è falsa ($n = 1$ con $n\lg n$).
- Teorema dell'esperto: dimenticare la condizione di regolarità nel caso 3; applicarlo quando $f$ differisce da $n^{\log_b a}$ solo per un fattore logaritmico (gap); applicarlo a ricorrenze con $T(n-1)$.
- Albero: contare $\log_b n$ livelli invece di $\log_b n + 1$; dimenticare il costo delle foglie $\Theta(n^{\log_b a})$.

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_
_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf e 07-Quicksort.pdf (casi 2–7, scelta del metodo)_
