---
tipo: entità
categoria: algoritmo
paradigma: "iterativo"
fonti_pdf: ["03-Analisi di algoritmi.pdf#page=11", "03-Analisi di algoritmi.pdf#page=17", "03-Analisi di algoritmi.pdf#page=28"]
---

# somma_iterativa — somma dei primi $n$ interi (versione iterativa)

## Problema risolto · [[03-Analisi di algoritmi.pdf#page=10|p. 10]]

Input: un intero $n \ge 0$. Output: $1 + 2 + \dots + n$.

## Idea

Accumulare in $s$ i numeri da 1 a $n$ con un ciclo.

## Pseudocodice · [[03-Analisi di algoritmi.pdf#page=11|p. 11]]

```
funzione somma_iterativa(n)
1  s ← 0
2  per i da 1 a n
3      s ← s + i
4  ritorna s
```

Nelle [[pseudocodice|convenzioni del corso]] la riga 2 si scrive `for i ← 1 to n`.

## Esempio di esecuzione

![[animazione-somma-iterativa.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo, `somma_iterativa(4)`: i valori di `i` e `s` a ogni riga, l'invariante $s = \sum_{k=1}^{i-1} k$ verificato a ogni iterazione e il conteggio dei passi che arriva a $2n + 4 = 12$ (slide 03 p. 28). Ogni fotogramma riporta in basso il numero del passo e cosa succede.

> 🧩 Traccia mia con $n = 4$:

| inizio iterazione | $i$ | $s$ prima | $s$ dopo | invariante $s = \sum_{k=1}^{i-1} k$ |
|---|---|---|---|---|
| 1 | 1 | 0 | 1 | $0$ ✓ |
| 2 | 2 | 1 | 3 | $1$ ✓ |
| 3 | 3 | 3 | 6 | $1+2 = 3$ ✓ |
| 4 | 4 | 6 | 10 | $1+2+3 = 6$ ✓ |
| uscita | 5 | 10 | — | $1+2+3+4 = 10$ = risultato ✓ |

## Correttezza · [[03-Analisi di algoritmi.pdf#page=17|p. 17]]

Invariante: all'inizio dell'iterazione $i$, $s = \sum_{k=1}^{i-1} k$. Dimostrazione completa, con la segnalazione del refuso «$i = 0$» della slide → [[invariante-di-ciclo]].

## Complessità · [[03-Analisi di algoritmi.pdf#page=23|p. 23]]–[[03-Analisi di algoritmi.pdf#page=29|29]], [[03-Analisi di algoritmi.pdf#page=24|p. 24]], [[03-Analisi di algoritmi.pdf#page=25|p. 25]], [[03-Analisi di algoritmi.pdf#page=26|p. 26]], [[03-Analisi di algoritmi.pdf#page=27|p. 27]]

| Riga | Operazione | Costo × esecuzioni |
|---|---|---|
| 1 | assegnazione | 1 |
| 2 | inizializzazione del ciclo ($i = 1$) | 1 |
| 2 | test di ciclo $i \le n$ | $n + 1$ |
| 3 | corpo | $n$ (*) |
| 4 | return | 1 |

(*) «in realtà abbiamo $n$ somme, $n$ assegnazioni e $n$ incrementi».

$$ T(n) = 1 + 1 + (n+1) + n + 1 = 2n + 4 \ \Rightarrow\ O(n) $$

(risultato di p. 28)

> 🧩 Derivazione mia (conteggio fine della nota *): contando separatamente somma, assegnazione e incremento, il corpo costa $3n$ e $T(n) = 4n + 4$: cambia la costante, **non** l'ordine $\Theta(n)$ — è esattamente ciò che la [[notazione-asintotica]] permette di ignorare.

**Spazio** («E la complessità spaziale?»): 🧩 $\Theta(1)$, due variabili ($s$, $i$) qualunque sia $n$.

**Verifica:** [[somma_primi_n.py]] conta $2n+4$ passi per $n \in \{0,1,2,5,10,100\}$.

![[03-analisi-algoritmi-p28-costo-somma-iterativa.png]]

## Connessioni

- [[somma-ricorsiva]] — stessa funzione, forma ricorsiva
- [[tempo-di-esecuzione]], [[analisi-del-costo-riga-per-riga]]

## Fonti · [[03-Analisi di algoritmi.pdf#page=10|p. 10]], [[03-Analisi di algoritmi.pdf#page=11|11]], [[03-Analisi di algoritmi.pdf#page=17|p. 17]], [[03-Analisi di algoritmi.pdf#page=23|p. 23]], [[03-Analisi di algoritmi.pdf#page=29|p. 29]]

- [[lezione-03-analisi-di-algoritmi]]

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_
_Aggiornato: 2026-10-01 — aggiunta l'animazione dell'algoritmo_

<!-- nav:inizio -->
---
**Lezione 03 · pagina 5 di 13** · ← [[iterazione-e-ricorsione|Iterazione e ricorsione]] · [[lezioni|Indice]] · [[somma-ricorsiva|somma_ricorsiva — somma dei primi n interi (versione ricorsiva)]] →
<!-- nav:fine -->
