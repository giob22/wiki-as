---
tipo: esercizio
argomento: "tempo di esecuzione di algoritmi iterativi"
difficoltà: bassa
---

# Analisi del costo riga per riga

## Metodo · [[02-Notazione asintotica.pdf#page=12|p. 12]]

1. Numerare le righe dello pseudocodice.
2. Per ogni riga: costo $c_i$ (costante, [[modello-ram]]) e numero di esecuzioni $t_i(n)$ in funzione della dimensione $n$.
3. Per i cicli `for i ← a to b`: il **test** si esegue $(b - a + 1) + 1$ volte, il **corpo** $b - a + 1$ volte.
4. Se $t_i$ dipende dall'istanza (rami `if`, uscite anticipate), fare la tabella per il **caso peggiore** (default del corso) e, se chiesto, per il migliore.
5. Sommare: $T(n) = \sum_i c_i\, t_i(n)$ e ridurre con la [[notazione-asintotica]] tenendo il termine dominante.

## Strumenti usati

- [[tempo-di-esecuzione]] — $T(n) = \sum c_i t_i(n)$
- [[casi-di-complessita]] — scelta del caso
- [[notazione-asintotica]], [[regole-di-calcolo-asintotico]]

## Casi svolti

### Caso 1 — somma iterativa · [[03-Analisi di algoritmi.pdf#page=23|p. 23]], [[03-Analisi di algoritmi.pdf#page=28|p. 28]]
**Traccia:** p. 23–p. 28: calcolare il costo di `somma_iterativa(n)`.

```
funzione somma_iterativa(n)
1  s ← 0
2  per i da 1 a n
3      s ← s + i
4  ritorna s
```

| Riga | Costo | Esecuzioni |
|---|---|---|
| 1 | 1 | 1 |
| 2 (inizializzazione $i = 1$) | 1 | 1 |
| 2 (test $i \le n$) | 1 | $n + 1$ |
| 3 | 1 | $n$ |
| 4 | 1 | 1 |

$$
\begin{aligned}
T(n) &= 1 + 1 + (n + 1) + n + 1 && \text{somma della tabella} \\
     &= 2n + 4 && \text{raccolgo} \\
     &= \Theta(n) && c_1 = 2,\ c_2 = 3,\ n_0 = 4:\ 2n \le 2n+4 \le 3n
\end{aligned}
$$

**Risultato:** $T(n) = 2n + 4 = O(n)$ (la slide scrive $O(n)$; è anche $\Theta(n)$). **Verifica:** [[somma_primi_n.py]].

### Caso 2 — Base2(n), casi migliore e peggiore · [[02-Notazione asintotica.pdf#page=11|p. 11]]
**Traccia:** p. 11 (la slide indica solo quale ramo è best/worst case).

```
ALGORITMO Base2(n)
1  SE CONDIZIONE_VERA ALLORA
2      ISTR_A_1
3      ISTR_A_2
4      RESTITUISCI
5  ALTRIMENTI
6      PER i = 0 .. n FAI
7          ISTR_B
8      FINEPER
9      RESTITUISCI
```

> 🧩 Svolgimento mio:
- **Caso migliore** (condizione vera): righe 1, 2, 3, 4 → $T_{best}(n) = 4 = \Theta(1)$.
- **Caso peggiore** (condizione falsa): riga 1 (1) + inizializzazione $i = 0$ (1) + test: $i = 0, \dots, n$ vero ($n+1$ volte) e $i = n+1$ falso (1) → $n + 2$; corpo riga 7: $n+1$; riga 9: 1.
$$ T_{worst}(n) = 1 + 1 + (n+2) + (n+1) + 1 = 2n + 6 = \Theta(n) $$

### Caso 3 — Base() · [[02-Notazione asintotica.pdf#page=7|p. 7]]
**Traccia:** p. 7. 🧩 Caso fortunato: test + 2 istruzioni + return = 4; sfortunato: test + 10 istruzioni + return = 12. Entrambi $\Theta(1)$: caso migliore e peggiore differiscono di una costante.

### Caso 4 — insertion sort: il numero di esecuzioni dipende dall'input · [[05-Insertion sort.pdf#page=19|p. 19]], [[05-Insertion sort.pdf#page=24|p. 24]]
**Traccia:** p. 19–p. 24.
Differenza rispetto ai casi precedenti: il test del `while` si esegue $t_j$ volte, e $t_j$ dipende dai valori nell'array. Si scrive quindi $T(n)$ con le sommatorie $\sum t_j$ e $\sum (t_j - 1)$, poi si sostituisce $t_j = 1$ (caso migliore, array già ordinato) e $t_j = j$ (caso peggiore, array decrescente).
**Risultato:** $T_{best}(n) = an + b = \Theta(n)$, $T_{worst}(n) = an^2 + bn + c = \Theta(n^2)$. Tabella dei costi e sviluppo completo delle sommatorie in [[insertion-sort]] § Complessità.

### Caso 5 — selection sort: contare solo l'operazione dominante · [[05-Insertion sort.pdf#page=32|p. 32]], [[05-Insertion sort.pdf#page=33|33]]
**Traccia:** esercizio 2.2.2, p. 32, p. 33.
Il confronto `s[j] < s[min]` si esegue $n - 1 - i$ volte per ogni $i$:
$$ \sum_{i=0}^{n-2} (n - 1 - i) = \frac{n(n-1)}{2} = \Theta(n^2) $$
per **ogni** input: caso migliore = caso peggiore. Dettagli in [[selection-sort]] § Complessità.

## Trappole · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=26|p. 26]] · 02-Notazione asintotica.pdf [[02-Notazione asintotica.pdf#page=5|p. 5]]

- Il test del ciclo si esegue **una volta in più** del corpo.
- Un ciclo `PER i = 0 .. n` fa $n + 1$ iterazioni, non $n$.
- «Corpo ⇒ $n$» della slide conta una riga come un'unità; contando somma, assegnazione e incremento separatamente si ottiene $4n + 4$: cambia la costante, non l'ordine.
- Una chiamata a `sort` o a un'altra procedura **non** costa 1.
- Con due cicli annidati il ciclo interno può dipendere dall'indice esterno ($j$ da $i+1$): la somma non è $n \cdot n$ ma $\sum (n-1-i)$ (selection sort).
- Se il numero di iterazioni dipende dai dati (insertion sort), bisogna fissare il caso prima di sostituire.

_Aggiornato: 2026-09-26 — ingest 02-Notazione asintotica.pdf e 03-Analisi di algoritmi.pdf_

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_

<!-- nav:inizio -->
---
**Lezione 03 · pagina 11 di 13** · ← [[dimostrazioni-di-correttezza|Dimostrazioni di correttezza (invariante e induzione)]] · [[lezioni|Indice]] · [[equazioni-di-ricorrenza|Equazioni di ricorrenza (costo degli algoritmi ricorsivi)]] →
<!-- nav:fine -->
