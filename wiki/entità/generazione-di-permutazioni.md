---
tipo: entità
categoria: algoritmo
paradigma: "backtracking con candidati = elementi non ancora usati"
fonti_pdf: ["15 - Backtracking.pdf#page=20", "15 - Backtracking.pdf#page=21", "15 - Backtracking.pdf#page=22", "15 - Backtracking.pdf#page=23", "15 - Backtracking.pdf#page=24"]
---

# Generazione di tutte le permutazioni

> 📚 Slide in inglese di S. Skiena («Constructing Permutations by Backtracking»).

## Problema risolto · [[15 - Backtracking.pdf#page=20|p. 20]]

- **Input:** un intero $n$ (l'insieme $\{1, \dots, n\}$).
- **Output:** tutte le $n!$ **permutazioni** di un insieme di $n$ elementi.

Quante sono le permutazioni di un insieme di $n$ elementi? Per costruirle tutte si usa un vettore di $n$ celle in cui il valore di $a_i$ è un intero da 1 a $n$ che **non è ancora comparso** nel vettore, e corrisponde all'$i$-esimo elemento della permutazione (p. 20).

## Idea · [[15 - Backtracking.pdf#page=20|p. 20]]

Si usa lo schema di [[backtracking]] con

$$
S_k = \{1, \dots, n\} - a, \qquad a \text{ è una soluzione quando } k = n
$$

cioè i candidati per la posizione $k$ sono gli elementi non ancora usati nelle prime $k-1$ posizioni (la slide scrive $S_k = (1, \dots, n) - v$ a p. 20 e $S_k = \{1, \dots, n\} - a$ a p. 22). Per **evitare di ripetere elementi** della permutazione si escludono quelli già presenti.

## Pseudocodice · [[15 - Backtracking.pdf#page=22|p. 22]]–[[15 - Backtracking.pdf#page=24|24]]

```c
void construct_candidates(int a[], int k, int n, int c[], int *nc) {
    int i;                          /* counter */
    bool in_perm[NMAX];             /* what is now in the permutation? */
    for (i = 1; i < NMAX; i++) {
        in_perm[i] = false;
    }
    for (i = 1; i < k; i++) {
        in_perm[a[i]] = true;
    }
    *nc = 0;
    for (i = 1; i <= n; i++) {
        if (!in_perm[i]) {
            c[*nc] = i;
            *nc = *nc + 1;
        }
    }
}
```

Le altre routine sono essenzialmente le stesse dei sottoinsiemi (p. 23):

```c
void process_solution(int a[], int k, int input) {
    int i;                          /* counter */
    for (i = 1; i <= k; i++) {
        printf(" %d", a[i]);
    }
    printf("\n");
}
int is_a_solution(int a[], int k, int n) {
    return (k == n);
}
void generate_permutations(int n) {
    int a[NMAX];                    /* solution vector */
    backtrack(a, 0, n);
}
```

La riga della chiamata iniziale è `backtrack(a, 0, n)` (p. 24).

![[15-backtracking-p20-permutazioni.png]]
![[15-backtracking-p22-permutazioni-candidati.png]]
![[15-backtracking-p23-permutazioni-routine.png]]
![[15-backtracking-p24-permutazioni-main.png]]

## Esempio di esecuzione · [[15 - Backtracking.pdf#page=21|p. 21]]

![[animazione-generazione-di-permutazioni.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero Backtrack per $n = 3$ con $S_k = \{1, 2, 3\} - a$: ogni ingresso, ritorno e soluzione è un fotogramma.

La slide mostra l'albero di generazione e l'ordine degli stati (in rosso le soluzioni):

$$
\begin{aligned}
&(1) \to (1,2) \to \mathbf{(1,2,3)} \to (1,2) \to (1) \to (1,3) \to \mathbf{(1,3,2)} \to (1,3) \to (1) \to () \to \\
&(2) \to (2,1) \to \mathbf{(2,1,3)} \to (2,1) \to (2) \to (2,3) \to \mathbf{(2,3,1)} \to (2,3) \to \dots
\end{aligned}
$$

fino a $(3,1,2)$ e $(3,2,1)$. Le foglie dell'albero, da sinistra a destra, sono $123, 132, 213, 231, 312, 321$. Nota a mano di p. 21: «posso togliere grandi porzioni di albero appena diventano inutili o ridondanti» (la potatura).

![[15-backtracking-p21-permutazioni-albero.png]]

> ⚠️ Contraddizione (refuso): nella sequenza di p. 21, dopo $(2,3,1) \to (2,3)$ compare un $()$ prima di $(2) \to () \to (3)$; l'esecuzione reale, verificata con [[backtracking.py]], è $(2,3) \to (2) \to () \to (3)$: il $()$ dopo $(2,3)$ è in più.

Traccia (verificata con [[backtracking.py]]): 16 chiamate di Backtrack ($1 + 3 + 6 + 6$ per i livelli $k = 0, 1, 2, 3$) e 6 soluzioni, nell'ordine $123, 132, 213, 231, 312, 321$ (ordine lessicografico, perché i candidati sono provati in ordine crescente).

## Correttezza · [[15 - Backtracking.pdf#page=20|p. 20]]

> 🧩 Derivazione mia. Per l'invariante di [[backtracking]] basta controllare che i figli di un nodo corrispondano esattamente ai candidati $S_k$: in posizione $k$ si provano tutti e soli gli elementi non ancora usati, quindi ogni foglia (a profondità $n$) contiene $n$ elementi distinti di $\{1, \dots, n\}$, cioè una permutazione; ogni permutazione corrisponde a uno e un solo cammino dalla radice (si scelgono in ordine $a_1, a_2, \dots, a_n$), quindi è generata una sola volta.

## Complessità

> 📄 Le slide danno solo il numero delle permutazioni, $n!$.

### Derivazione — numero di chiamate e costo
**Si parte da:** l'albero delle chiamate: al livello $k$ ci sono tanti nodi quanti i vettori parziali di $k$ elementi distinti, cioè $n(n-1)\cdots(n-k+1) = n!/(n-k)!$.

> 🧩 Derivazione mia.

$$
\begin{aligned}
\#\text{chiamate} &= \sum_{k=0}^{n} \frac{n!}{(n-k)!} && \text{livelli } k = 0, \dots, n \\
&= n! \sum_{j=0}^{n} \frac{1}{j!} && j = n - k \\
&\le n! \cdot e = O(n!) && \textstyle\sum_{j \ge 0} 1/j! = e
\end{aligned}
$$

(in effetti per $n \ge 1$ vale $\lfloor e \cdot n! \rfloor$ chiamate, verificato in [[backtracking.py]] per $n = 1, \dots, 8$: 2, 5, 16, 65, 326, 1957, 13700, 109601). Ogni chiamata esegue `construct_candidates`, che costa $O(n)$ (azzera `in_perm` fino a `NMAX`, marca $k - 1$ elementi, scorre $n$ candidati), e ogni soluzione costa $O(n)$ per la stampa. Totale: $O(n \cdot n!)$.
**Sanity check:** $n = 3$: $1 + 3 + 6 + 6 = 16$ chiamate; $n = 8$: 40320 permutazioni e 109601 chiamate.
**Ipotesi:** `NMAX` dell'ordine di $n$; modello RAM.

## Connessioni

- [[backtracking]] — lo schema generale
- [[ricerca-combinatoria]] — le $n!$ permutazioni sono lo spazio di ricerca di [[optimal-tsp]] (problema del commesso viaggiatore)
- [[visita-in-profondita]] — il backtracking è una DFS sull'albero delle permutazioni

## Fonti · [[15 - Backtracking.pdf#page=20|p. 20]]–[[15 - Backtracking.pdf#page=24|24]]

- [[lezione-15-backtracking]]

_Aggiornato: 2026-11-26 — ingest 15 - Backtracking.pdf_

<!-- nav:inizio -->
---
**Lezione 15 · pagina 3 di 3** · ← [[backtracking|Backtracking]] · [[lezioni|Indice]] · fine del libro →
<!-- nav:fine -->
