---
tipo: entità
categoria: algoritmo
paradigma: "ricorsivo (dimezzamento)"
fonti_pdf: ["05-Insertion sort.pdf#page=32"]
---

# power(a, n) — potenza veloce (fast exponentiation)

## Problema risolto

Calcolare $a^n$ con $n$ intero $\ge 0$ usando poche moltiplicazioni.

## Idea

> 📄 Fonte: [[05-Insertion sort.pdf#page=32]]

$$ a^n = \left(a^{n/2}\right)^2 \ \text{se } n \text{ è pari}, \qquad a^n = a\left(a^{\lfloor n/2 \rfloor}\right)^2 \ \text{se } n \text{ è dispari} $$

«This requires $O(\lg n)$ mult.»

## Pseudocodice

> 📄 Fonte: [[05-Insertion sort.pdf#page=32]] (righe numerate da me)

```
function power(a,n)
1  if (n = 0) return(1)
2  x = power(a, ⌊n/2⌋)
3  if (n is even) then return(x²)
4      else return(a * x²)
```

## Esempio di esecuzione

![[animazione-potenza-veloce.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo, il calcolo di $2^{13}$: le chiamate scendono sulla pila dimezzando $n$ (13 → 6 → 3 → 1 → 0), poi risalgono con i valori e il contatore delle moltiplicazioni (7 in tutto, invece delle 12 del metodo ingenuo). Ogni fotogramma riporta in basso il numero del passo e cosa succede.


> 🧩 Traccia mia, $a^{13}$ ($13 = 1101_2$):

| chiamata | $\lfloor n/2 \rfloor$ | $x$ | $n$ pari? | risultato |
|----------|----------------------|-----|-----------|-----------|
| power(a, 0) | — | — | — | $1$ |
| power(a, 1) | 0 | $1$ | no | $a \cdot 1^2 = a$ |
| power(a, 3) | 1 | $a$ | no | $a \cdot a^2 = a^3$ |
| power(a, 6) | 3 | $a^3$ | sì | $(a^3)^2 = a^6$ |
| power(a, 13) | 6 | $a^6$ | no | $a \cdot (a^6)^2 = a^{13}$ |

## Correttezza

> 🧩 Derivazione mia (per induzione forte su $n$, → [[correttezza-per-induzione]]):
> - **Base** $n = 0$: restituisce $1 = a^0$.
> - **Passo:** per $n \ge 1$, $\lfloor n/2 \rfloor < n$, quindi per ipotesi induttiva $x = a^{\lfloor n/2 \rfloor}$. Se $n$ è pari, $n = 2\lfloor n/2 \rfloor$ e $x^2 = a^n$; se $n$ è dispari, $n = 2\lfloor n/2 \rfloor + 1$ e $a\,x^2 = a^n$.
> - **Terminazione:** la misura $n$ scende strettamente ($\lfloor n/2 \rfloor < n$ per $n \ge 1$) fino a 0.

## Complessità

> 🧩 Derivazione mia (la slide dà il risultato $O(\lg n)$ senza passaggi). Sia $M(n)$ il numero di moltiplicazioni:
$$
\begin{aligned}
M(0) &= 0, \qquad M(n) \le M(\lfloor n/2 \rfloor) + 2 && x^2 \text{ e l'eventuale } a \cdot (\ ) \\
M(n) &\le M(\lfloor n/2^k \rfloor) + 2k && \text{srotolo } k \text{ volte} \\
\lfloor n/2^k \rfloor &= 0 \iff k = \lfloor \lg n \rfloor + 1 && n \ge 1 \\
M(n) &\le 2(\lfloor \lg n \rfloor + 1) = O(\lg n)
\end{aligned}
$$
> Il numero di chiamate ricorsive è $\lfloor \lg n \rfloor + 2$ (da $n$ fino a 0): è il «dimezzamento ripetuto» che genera il logaritmo ([[logaritmi-nell-analisi]]).
>
> **Sanity check** ([[stringhe_e_logaritmi.py]]): $n = 10^6$ → 27 moltiplicazioni (limite 40), contro le $n - 1 = 999\,999$ del metodo ingenuo $a \cdot a \cdots a$.

## Connessioni

- [[logaritmi-nell-analisi]] — la slide in cui compare
- [[equazioni-di-ricorrenza]] — ricorrenza con $\lfloor n/2 \rfloor$ invece di $n - 1$
- [[somma-ricorsiva]] — confronto: lì la misura cala di 1 ($\Theta(n)$ chiamate), qui si dimezza ($\Theta(\lg n)$)

## Fonti

- [[lezione-05-insertion-sort]]
- le stesse slide sono riprese nella versione aggiornata della lezione 06 ([[lezione-06-merge-sort]]): [[06-Merge Sort (1).pdf#page=47]]
- [[05-Insertion sort.pdf#page=32]]

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_
_Aggiornato: 2026-10-01 — aggiunta l'animazione dell'algoritmo_
_Aggiornato: 2026-10-10 — slide riprese nella versione aggiornata della lezione 06_

<!-- nav:inizio -->
---
**Lezione 05 · pagina 7 di 7** · ← [[logaritmi-nell-analisi|L'importanza dei logaritmi]] · [[lezioni|Indice]] · [[lezione-06-merge-sort|Lezione 06: introduzione e riepilogo]] →
<!-- nav:fine -->
