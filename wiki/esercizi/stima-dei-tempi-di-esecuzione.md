---
tipo: esercizio
argomento: "tempi di esecuzione e dimensione massima risolvibile"
difficoltà: bassa
---

# Stima dei tempi di esecuzione e dell'$n$ massimo risolvibile

## Metodo

- **Tempo dato $n$:** $t = f(n) \cdot \tau$, con $\tau$ = tempo per operazione (es. $10^{-9}$ s se $10^9$ op/s; $10^{-6}$ s se «$f(n)$ microsecondi»). Poi convertire nell'unità più leggibile.
- **$n$ dato il tempo:** risolvere $f(n) \le t/\tau$ e prendere il **massimo intero**. Per funzioni invertibili in forma chiusa: $\lg n \le T \Rightarrow n \le 2^T$; $\sqrt n \le T \Rightarrow n \le T^2$; $n^k \le T \Rightarrow n \le T^{1/k}$; $2^n \le T \Rightarrow n \le \lg T$. Per $n\lg n$ e $n!$ si procede per tentativi (o ricerca binaria).
- Convenzioni: minuto = 60 s, ora = 3600 s, giorno = 86 400 s, mese = 30 giorni, anno = 365 giorni, secolo = 100 anni.

## Strumenti usati

- [[efficienza-degli-algoritmi]], [[dominanza-asintotica]]
- Script di verifica: [[tempi_crescita.py]]

## Casi svolti

### Caso 1 — insertion sort vs merge sort ([[01-Introduzione.pdf#page=11]]) · [[06-Merge Sort (1).pdf#page=29|p. 27]]
$n = 10^6$, $10^9$ op/s: $t_{IS} = 10^{12}/10^9 = 1000$ s $\approx 16.7$ min; $t_{MS} = 10^6 \cdot 19.93 / 10^9 \approx 0.02$ s. Passaggi in [[efficienza-degli-algoritmi]]; il costo $n\lg n$ di merge sort è dimostrato in [[merge-sort]].

### Caso 2 — tabella dell'$n$ massimo ([[01-Introduzione.pdf#page=12]])
**Traccia:** «For each function $f(n)$ and time $t$ in the following table, determine the largest size $n$ of a problem that can be solved in time $t$, assuming that the algorithm to solve the problem takes $f(n)$ microseconds.» La tabella nella slide è **vuota**.

![[01-introduzione-p12-tabella-n-max-tempo.png]]

> 🧩 Svolgimento mio (verificato con [[tempi_crescita.py]]). Tempo disponibile in µs: $T = t \cdot 10^6$.

| $f(n)$ | 1 secondo | 1 minuto | 1 ora | 1 giorno | 1 mese | 1 anno | 1 secolo |
|---|---|---|---|---|---|---|---|
| $\lg n$ | $2^{10^6}$ | $2^{6\cdot10^7}$ | $2^{3.6\cdot10^9}$ | $2^{8.64\cdot10^{10}}$ | $2^{2.59\cdot10^{12}}$ | $2^{3.15\cdot10^{13}}$ | $2^{3.15\cdot10^{15}}$ |
| $\sqrt n$ | $10^{12}$ | $3.6\cdot10^{15}$ | $1.30\cdot10^{19}$ | $7.46\cdot10^{21}$ | $6.72\cdot10^{24}$ | $9.95\cdot10^{26}$ | $9.95\cdot10^{30}$ |
| $n$ | $10^6$ | $6\cdot10^7$ | $3.6\cdot10^9$ | $8.64\cdot10^{10}$ | $2.59\cdot10^{12}$ | $3.15\cdot10^{13}$ | $3.15\cdot10^{15}$ |
| $n\lg n$ | 62 746 | 2 801 417 | $1.33\cdot10^8$ | $2.76\cdot10^9$ | $7.19\cdot10^{10}$ | $7.98\cdot10^{11}$ | $6.86\cdot10^{13}$ |
| $n^2$ | 1 000 | 7 745 | 60 000 | 293 938 | 1 609 968 | 5 615 692 | 56 156 922 |
| $n^3$ | 100 | 391 | 1 532 | 4 420 | 13 736 | 31 593 | 146 645 |
| $2^n$ | 19 | 25 | 31 | 36 | 41 | 44 | 51 |
| $n!$ | 9 | 11 | 12 | 13 | 15 | 16 | 17 |

Esempi di calcolo:
$$
\begin{aligned}
&n^2,\ 1\text{ s}: && n^2 \le 10^6 \Rightarrow n \le 10^3 \\
&2^n,\ 1\text{ s}: && 2^n \le 10^6 \Rightarrow n \le \lg 10^6 = 19.93 \Rightarrow n = 19 && (2^{19} = 524\,288 \le 10^6 < 2^{20}) \\
&n!,\ 1\text{ s}: && 9! = 362\,880 \le 10^6 < 10! = 3\,628\,800 \Rightarrow n = 9 \\
&n^2,\ 1\text{ giorno}: && n \le \sqrt{8.64\cdot10^{10}} = 293\,938.7 \Rightarrow n = 293\,938
\end{aligned}
$$

**Lettura:** passando da 1 secondo a 1 secolo (fattore $\approx 3\cdot10^9$) un algoritmo lineare guadagna lo stesso fattore, uno quadratico solo $\sqrt{3\cdot10^9} \approx 5.6\cdot10^4$, uno esponenziale appena $+32$ ($\lg(3\cdot10^9) \approx 31.6$), uno fattoriale $+8$.

### Caso 3 — $20!$, $1000!$, $2^{20}$, $2^{100}$ ([[01-Introduzione.pdf#page=33]], [[01-Introduzione.pdf#page=59]]) · [[02-Notazione asintotica.pdf#page=36|p. 36]]
- $20! = 2\,432\,902\,008\,176\,640\,000$ ✓ (slide); a 1 ns per permutazione: $2.43\cdot10^9$ s $= 77.1$ anni ✓ (tabella di p. 36).
- $1000! \approx 10^{2567.6}$, 2568 cifre (il «1000 = …» della slide).
- $2^{20} = 1\,048\,576 \approx 1$M ✓; $2^{100} = 1.2677\cdot10^{30}$ (slide: $1.26\cdot10^{30}$, troncato).

### Caso 4 — ricalcolo della tabella di crescita ([[02-Notazione asintotica.pdf#page=36]])
Con 1 ns per operazione. Esempi: $n\lg n$, $n = 10^6$: $10^6 \cdot 19.93$ ns $= 19.93$ ms ✓; $n^2$, $n = 10^9$: $10^{18}$ ns $= 10^9$ s $= 10^9 / (3.1536\cdot10^7) = 31.7$ anni ✓; $2^n$, $n = 50$: $1.126\cdot10^{15}$ ns $= 1.126\cdot10^6$ s $= 13.0$ giorni ✓. Tabella completa e verifiche in [[dominanza-asintotica]].

### Caso 5 — ricerca binaria con split sbilanciato ([[05-Insertion sort.pdf#page=38]])
**Traccia:** quante domande servono per cercare in un elenco di un milione di nomi se ogni divisione è 1/3–2/3 invece di 1/2–1/2?
$$ \log_{3/2} 10^6 = \frac{\ln 10^6}{\ln 1.5} = \frac{13.8155}{0.4055} = 34.07 \approx 35, \qquad \lg 10^6 = 19.93 \approx 20 $$
**Risultato:** circa 35 contro 20 domande nel caso peggiore: il rapporto è la costante $1/\lg(3/2) = 1.71$. La complessità resta logaritmica: la base non conta → [[logaritmi-nell-analisi]].

## Trappole

- Leggere bene l'unità: «$f(n)$ microsecondi» (p. 12) contro «1 operazione = 1 ns» (tabella di p. 36) contro «$10^9$ operazioni al secondo» (p. 11).
- La base del logaritmo cambia il risultato numerico (non l'ordine asintotico): nelle slide $\lg = \log_2$.
- Per $\lg n$ il valore di $n$ è astronomico: si lascia in forma $2^{T}$.
- L'$n$ massimo è un **intero**: arrotondare per difetto.

_Aggiornato: 2026-09-26 — ingest 01-Introduzione.pdf e 02-Notazione asintotica.pdf_

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_
_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf e 07-Quicksort.pdf_
_Aggiornato: 2026-10-10 — link ripuntati alla versione aggiornata delle slide 06-Merge Sort (1).pdf_

<!-- nav:inizio -->
---
**Lezione 01 · pagina 5 di 18** · ← [[efficienza-degli-algoritmi|Efficienza degli algoritmi («Algorithms as a technology»)]] · [[lezioni|Indice]] · [[robot-tour-optimization|Robot Tour Optimization (problema del commesso viaggiatore, TSP)]] →
<!-- nav:fine -->
