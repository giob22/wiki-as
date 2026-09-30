---
tipo: entità
categoria: algoritmo
paradigma: "iterativo"
fonti_pdf: ["03-Analisi di algoritmi.pdf#page=11", "03-Analisi di algoritmi.pdf#page=17", "03-Analisi di algoritmi.pdf#page=28"]
---

# somma_iterativa — somma dei primi $n$ interi (versione iterativa)

## Problema risolto

Input: un intero $n \ge 0$. Output: $1 + 2 + \dots + n$ ([[03-Analisi di algoritmi.pdf#page=10]]).

## Idea

Accumulare in $s$ i numeri da 1 a $n$ con un ciclo.

## Pseudocodice

> 📄 Fonte: [[03-Analisi di algoritmi.pdf#page=11]] (righe numerate da me)

```
funzione somma_iterativa(n)
1  s ← 0
2  per i da 1 a n
3      s ← s + i
4  ritorna s
```

Nelle [[pseudocodice|convenzioni del corso]] la riga 2 si scrive `for i ← 1 to n`.

## Esempio di esecuzione

> 🧩 Traccia mia con $n = 4$:

| inizio iterazione | $i$ | $s$ prima | $s$ dopo | invariante $s = \sum_{k=1}^{i-1} k$ |
|---|---|---|---|---|
| 1 | 1 | 0 | 1 | $0$ ✓ |
| 2 | 2 | 1 | 3 | $1$ ✓ |
| 3 | 3 | 3 | 6 | $1+2 = 3$ ✓ |
| 4 | 4 | 6 | 10 | $1+2+3 = 6$ ✓ |
| uscita | 5 | 10 | — | $1+2+3+4 = 10$ = risultato ✓ |

## Correttezza

Invariante: all'inizio dell'iterazione $i$, $s = \sum_{k=1}^{i-1} k$ ([[03-Analisi di algoritmi.pdf#page=17]]). Dimostrazione completa, con la segnalazione del refuso «$i = 0$» della slide → [[invariante-di-ciclo]].

## Complessità

> 📄 Fonte: [[03-Analisi di algoritmi.pdf#page=23]]–[[03-Analisi di algoritmi.pdf#page=28]]

| Riga | Operazione | Costo × esecuzioni | Pagina |
|------|------------|--------------------|--------|
| 1 | assegnazione | 1 | [[03-Analisi di algoritmi.pdf#page=24]] |
| 2 | inizializzazione del ciclo ($i = 1$) | 1 | [[03-Analisi di algoritmi.pdf#page=25]] |
| 2 | test di ciclo $i \le n$ | $n + 1$ | [[03-Analisi di algoritmi.pdf#page=25]] |
| 3 | corpo | $n$ (*) | [[03-Analisi di algoritmi.pdf#page=26]] |
| 4 | return | 1 | [[03-Analisi di algoritmi.pdf#page=27]] |

(*) «in realtà abbiamo $n$ somme, $n$ assegnazioni e $n$ incrementi» ([[03-Analisi di algoritmi.pdf#page=26]]).

$$ T(n) = 1 + 1 + (n+1) + n + 1 = 2n + 4 \ \Rightarrow\ O(n) $$

(risultato di [[03-Analisi di algoritmi.pdf#page=28]])

> 🧩 Derivazione mia (conteggio fine della nota *): contando separatamente somma, assegnazione e incremento, il corpo costa $3n$ e $T(n) = 4n + 4$: cambia la costante, **non** l'ordine $\Theta(n)$ — è esattamente ciò che la [[notazione-asintotica]] permette di ignorare.

**Spazio** («E la complessità spaziale?», [[03-Analisi di algoritmi.pdf#page=29]]): 🧩 $\Theta(1)$, due variabili ($s$, $i$) qualunque sia $n$.

**Verifica:** [[somma_primi_n.py]] conta $2n+4$ passi per $n \in \{0,1,2,5,10,100\}$.

![[03-analisi-algoritmi-p28-costo-somma-iterativa.png]]

## Connessioni

- [[somma-ricorsiva]] — stessa funzione, forma ricorsiva
- [[tempo-di-esecuzione]], [[analisi-del-costo-riga-per-riga]]

## Fonti

- [[lezione-03-analisi-di-algoritmi]]
- [[03-Analisi di algoritmi.pdf#page=10]], [[03-Analisi di algoritmi.pdf#page=11]], [[03-Analisi di algoritmi.pdf#page=17]], [[03-Analisi di algoritmi.pdf#page=23]]–[[03-Analisi di algoritmi.pdf#page=29]]

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_
