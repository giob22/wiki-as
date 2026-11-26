---
tipo: entità
categoria: algoritmo
paradigma: "incrementale (iterativo)"
fonti_pdf: ["05-Insertion sort.pdf#page=26", "05-Insertion sort.pdf#page=28", "05-Insertion sort.pdf#page=33"]
---

# Selection sort (Esercizio del libro di testo 2.2.2)

Le sezioni seguono l'ordine delle slide: traccia dell'esercizio (p. 24) → codice (p. 25) → correttezza (p. 26) → efficienza asintotica (pp. 27–28) → memoria (p. 29). Le slide pongono le domande; le risposte che la slide non dà sono mie (🧩).

## Problema risolto

[[ordinamento]].

## Traccia dell'esercizio e idea · [[05-Insertion sort.pdf#page=31|p. 26]]

> 📄 Fonte: p. 26 — «Esercizio Libro di testo: 2.2.2» (Cormen, esercizio 2.2-2)

**Pseudo-code** (a parole):
- trova l'elemento **più piccolo** e scambialo con il **primo** elemento;
- trova il **secondo più piccolo** e scambialo con il **secondo** elemento;
- ripeti, trovando il successivo più piccolo e scambiandolo nella posizione corretta, per i **primi $n - 1$ elementi**.

Consegne: **Implementa**. **Analizza**: quale invariante di ciclo conserva? Perché bisogna eseguirlo fino ad $n - 1$ anziché $n$? Esprimere nella notazione $\Theta$ i tempi di esecuzione migliore e peggiore.

![[05-insertion-sort-p24-esercizio-selection-sort.png]]

## Pseudocodice (implementazione) · [[05-Insertion sort.pdf#page=33|p. 28]]

```c
selection_sort(int s[], int n) {
1     int i,j;        /* counters */
2     int min;        /* index of minimum */
3     for (i=0; i<n; i++) {
4         min=i;
5         for (j=i+1; j<n; j++)
6             if (s[j] < s[min]) min=j;
7         swap(s[i],s[min]);
8     }
}
```

> 🧩 Traduzione mia nelle [[pseudocodice|convenzioni del corso]] (indici da 1, ciclo esterno fino a $n-1$ come nella traccia):

```
SELECTION-SORT(A)
1  n ← length[A]
2  for i ← 1 to n − 1
3      min ← i
4      for j ← i + 1 to n
5          if A[j] < A[min]
6              min ← j
7      scambia A[i] con A[min]
```

## Esempio di esecuzione

![[animazione-selection-sort.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo, sull'array ⟨5, 2, 4, 6, 1, 3⟩: i puntatori `i`, `j`, `min`, ogni confronto `A[j] < A[min]`, lo scambio a fine iterazione, il prefisso già sistemato in verde e il contatore dei confronti che arriva a $n(n-1)/2 = 15$. Ogni fotogramma riporta in basso il numero del passo e cosa succede.

> 🧩 Traccia mia sull'array della lezione, ⟨5, 2, 4, 6, 1, 3⟩ (indici da 1):

| $i$ | minimo di $A[i..6]$ | scambio | $A$ dopo |
|---|---|---|---|
| 1 | 1 (pos. 5) | $A[1] \leftrightarrow A[5]$ | ⟨**1**, 2, 4, 6, 5, 3⟩ |
| 2 | 2 (pos. 2) | con sé stesso | ⟨1, **2**, 4, 6, 5, 3⟩ |
| 3 | 3 (pos. 6) | $A[3] \leftrightarrow A[6]$ | ⟨1, 2, **3**, 6, 5, 4⟩ |
| 4 | 4 (pos. 6) | $A[4] \leftrightarrow A[6]$ | ⟨1, 2, 3, **4**, 5, 6⟩ |
| 5 | 5 (pos. 5) | con sé stesso | ⟨1, 2, 3, 4, **5**, 6⟩ |

## Correttezza · [[05-Insertion sort.pdf#page=36|p. 31]]

> 📄 Fonte: p. 31 — «Dimostrarne la correttezza» (senza soluzione)

> 🧩 Derivazione mia (risponde anche a «quale invariante di ciclo conserva?» di p. 26).
>
> **Invariante del ciclo esterno** (indici da 1): all'inizio dell'iterazione $i$, il sotto-array $A[1..i-1]$ contiene gli $i - 1$ elementi **più piccoli** dell'array, **ordinati**; di conseguenza ogni elemento di $A[i..n]$ è $\ge$ di ogni elemento di $A[1..i-1]$.
> - **Inizializzazione:** $i = 1$, $A[1..0]$ è vuoto: vero.
> - **Conservazione:** il ciclo interno (righe 4–6) ha a sua volta l'invariante «$A[min]$ è il minimo di $A[i..j-1]$»; alla sua uscita ($j = n + 1$) $A[min]$ è il minimo di $A[i..n]$. Lo scambio lo porta in $A[i]$: è $\ge$ di tutti quelli in $A[1..i-1]$ (per l'invariante) e $\le$ di tutti quelli rimasti, quindi $A[1..i]$ contiene gli $i$ più piccoli, ordinati.
> - **Conclusione:** il ciclo esce con $i = n$: $A[1..n-1]$ contiene gli $n - 1$ più piccoli ordinati, e $A[n]$, l'unico rimasto, è il più grande → $A[1..n]$ ordinato.
> - **Terminazione:** entrambi i cicli sono `for` con estremi finiti.
>
> **Perché fino a $n - 1$ e non $n$** (domanda di p. 26): dopo $n - 1$ iterazioni l'ultimo elemento è per forza il massimo ed è già al suo posto; un'$n$-esima iterazione cercherebbe il minimo di $A[n..n]$ (0 confronti) e scambierebbe $A[n]$ con sé stesso. Il codice C di p. 28 (`i<n`) esegue proprio questa iterazione inutile: non è un errore ma è lavoro sprecato.
>
> Verificato con [[ordinamento.py]] (asserzione dell'invariante a ogni iterazione).

## Complessità · [[05-Insertion sort.pdf#page=37|p. 32]], [[05-Insertion sort.pdf#page=38|33]]

> 📄 Fonte: p. 32 — «Valutare l'efficienza asintotica»; p. 33 — conteggio dei confronti:

$$ \sum_{i=0}^{n-2} (n - 1 - i) = (n-1) + (n-2) + \dots + 1 = \frac{n(n-1)}{2} $$

![[05-insertion-sort-p28-somma-confronti-selection.png]]

> 🧩 Derivazione mia:
$$
\begin{aligned}
\text{confronti con } i \text{ fissato} &= (n-1) - (i+1) + 1 = n - 1 - i && j = i+1, \dots, n-1 \text{ (codice C, indici da 0)} \\
\text{confronti totali} &= \sum_{i=0}^{n-2} (n-1-i) && i = n-1 \text{ contribuisce } 0 \\
&= \sum_{k=1}^{n-1} k = \frac{n(n-1)}{2} && k = n - 1 - i \\
&= \Theta(n^2)
\end{aligned}
$$
>
> **Caso migliore = caso peggiore = $\Theta(n^2)$** (terza domanda di p. 26): il numero di confronti **non dipende dall'input**, perché il ciclo interno scorre sempre tutto $A[i+1..n]$ per trovare il minimo; anche un array già ordinato paga $\frac{n(n-1)}{2}$ confronti. Cambia solo quante volte si esegue `min=j` (al più una volta per confronto), il che non sposta l'ordine di crescita. Gli scambi sono esattamente uno per iterazione esterna: $\Theta(n)$.
>
> **Sanity check** ([[ordinamento.py]]): per $n = 100$, 4950 confronti su input ordinato, decrescente e casuale; $\frac{100\cdot 99}{2} = 4950$.

> 💡 Connessione: confronto con [[insertion-sort]] — entrambi $\Theta(n^2)$ nel caso peggiore, ma insertion sort scende a $\Theta(n)$ sugli input già ordinati, selection sort no; in compenso selection sort fa solo $\Theta(n)$ scambi.

## Memoria · [[05-Insertion sort.pdf#page=34|p. 34]]

> 📄 Fonte: p. 34 — «E la memoria?» (senza soluzione)

> 🧩 Derivazione mia: oltre all'array usa solo `i`, `j`, `min` e una variabile temporanea nello `swap`, in numero fisso qualunque sia $n$ → spazio aggiuntivo $\Theta(1)$: è un ordinamento **sul posto**, come insertion sort.

## Proprietà

- **Sul posto** — 🧩 dalla risposta sulla memoria.
- **Non adattivo** — 🧩 stesso numero di confronti su ogni input.
- **Non stabile** — 🧩 lo scambio a lunga distanza può scavalcare un elemento uguale. Esempio mio: ⟨2ₐ, 2ᵦ, 1⟩ → alla prima iterazione 2ₐ viene scambiato con 1 → ⟨1, 2ᵦ, 2ₐ⟩, e i due 2 sono invertiti.

## Connessioni

- [[insertion-sort]] — l'algoritmo della lezione
- [[invariante-di-ciclo]], [[dimostrazioni-di-correttezza]] — correttezza
- [[analisi-del-costo-riga-per-riga]] — conteggio dei confronti

## Fonti · [[05-Insertion sort.pdf#page=31|p. 26]], [[05-Insertion sort.pdf#page=34|p. 34]]

- [[lezione-05-insertion-sort]]

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_
_Aggiornato: 2026-10-01 — aggiunta l'animazione dell'algoritmo_

<!-- nav:inizio -->
---
**Lezione 05 · pagina 3 di 7** · ← [[insertion-sort|Insertion sort]] · [[lezioni|Indice]] · [[substring-pattern-matching|Substring Pattern Matching (ricerca di una sottostringa)]] →
<!-- nav:fine -->
