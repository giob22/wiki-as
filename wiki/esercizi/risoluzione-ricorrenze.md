---
tipo: esercizio
argomento: "costo di algoritmi ricorsivi"
difficoltà: bassa
---

# Scrivere e risolvere equazioni di ricorrenza

## Metodo

1. Dallo pseudocodice ricorsivo: **caso base** → valore di $T$ sul caso base (costo costante).
2. **Caso ricorsivo**: $T(n) =$ (somma dei $T$ delle chiamate ricorsive, con i loro argomenti) $+$ (costo del lavoro locale: confronti, somme, return).
3. Risolvere **srotolando** (sostituzione iterata): scrivere 2–3 passi, individuare la forma generale dopo $k$ passi, **verificarla per induzione**, scegliere $k$ per arrivare al caso base.
4. Esprimere il risultato in forma chiusa e in [[notazione-asintotica]].

## Strumenti usati

- [[equazioni-di-ricorrenza]], [[correttezza-per-induzione]] (per verificare la forma generale)

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

## Trappole

- Dimenticare il caso base (la ricorrenza senza $T(0)$ non determina $T$).
- Srotolare senza verificare la forma generale.
- Confondere il **tempo** $\Theta(n)$ con lo **spazio**: nella versione ricorsiva anche lo spazio è $\Theta(n)$, nella iterativa è $\Theta(1)$ ([[iterazione-e-ricorsione]]).

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_
