---
tipo: entità
categoria: algoritmo
paradigma: "ricorsivo"
fonti_pdf: ["03-Analisi di algoritmi.pdf#page=11", "03-Analisi di algoritmi.pdf#page=19", "03-Analisi di algoritmi.pdf#page=33"]
---

# somma_ricorsiva — somma dei primi $n$ interi (versione ricorsiva)

## Problema risolto

Input: un intero $n \ge 0$. Output: $1 + 2 + \dots + n$ ([[03-Analisi di algoritmi.pdf#page=10]]).

## Idea

$S(n) = n + S(n-1)$, con $S(0) = 0$: la somma fino a $n$ è $n$ più la somma fino a $n - 1$.

## Pseudocodice

> 📄 Fonte: [[03-Analisi di algoritmi.pdf#page=11]] (righe numerate da me)

```
funzione somma_ricorsiva(n)
1  se n = 0
2      ritorna 0
3  altrimenti
4      ritorna n + somma_ricorsiva(n − 1)
```

## Esempio di esecuzione

> 🧩 Traccia mia con $n = 3$ (le chiamate scendono, i valori risalgono):

```
somma_ricorsiva(3) = 3 + somma_ricorsiva(2)
                         = 2 + somma_ricorsiva(1)
                               = 1 + somma_ricorsiva(0)
                                     = 0            ← caso base
                               = 1 + 0 = 1
                         = 2 + 1 = 3
                   = 3 + 3 = 6
```
Chiamate attive contemporaneamente nel punto più profondo: 4 ($n = 3, 2, 1, 0$), cioè $n + 1$.

## Correttezza

Per induzione su $n$ ([[03-Analisi di algoritmi.pdf#page=19]]): misura $n$; base $S(0) = 0$; se $S(n-1)$ è corretto, $S(n) = n + S(n-1)$ è corretto; ogni chiamata usa $n - 1 < n$ → termina. Passaggi espliciti → [[correttezza-per-induzione]].

## Complessità

> 📄 Fonte: [[03-Analisi di algoritmi.pdf#page=31]]–[[03-Analisi di algoritmi.pdf#page=33]]

- $T(0)$: un confronto e un return ⇒ 1 (righe 1–2)
- $T(i)$, $0 < i \le n$: una chiamata ricorsiva con argomento $i - 1$, una somma, un return ⇒ $T(i) = T(i-1) + c$ (riga 4)

$$ T(n) = T(n-1) + c = T(n-2) + 2c = \dots = T(0) + n\,c = 1 + c\,n = O(n) $$

Srotolamento completo e verifica della forma generale → [[equazioni-di-ricorrenza]].

**Spazio** («E la complessità spaziale?», [[03-Analisi di algoritmi.pdf#page=34]]): 🧩 $\Theta(n)$ — $n+1$ record di attivazione contemporaneamente sulla pila (traccia sopra). È il costo nascosto della ricorsione rispetto a [[somma-iterativa]] ($\Theta(1)$).

**Verifica:** [[somma_primi_n.py]] (costo con $c = 1$ pari a $n + 1$, profondità massima $n + 1$).

## Connessioni

- [[somma-iterativa]], [[iterazione-e-ricorsione]]
- [[risoluzione-ricorrenze]] — esercizio

## Fonti

- [[lezione-03-analisi-di-algoritmi]]
- [[03-Analisi di algoritmi.pdf#page=11]], [[03-Analisi di algoritmi.pdf#page=19]], [[03-Analisi di algoritmi.pdf#page=30]]–[[03-Analisi di algoritmi.pdf#page=34]]

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_
