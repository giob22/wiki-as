---
tipo: entità
categoria: algoritmo
paradigma: "[[ricerca-combinatoria]] con potatura: visita in profondità di un grafo implicito di configurazioni"
fonti_pdf: ["15 - Backtracking.pdf#page=4", "15 - Backtracking.pdf#page=5", "15 - Backtracking.pdf#page=7", "15 - Backtracking.pdf#page=8", "15 - Backtracking.pdf#page=9", "15 - Backtracking.pdf#page=14"]
---

# Backtracking

> 📚 Le slide di questa lezione sono in inglese, di S. Skiena («Lecture 15: Backtracking»).

## Problema risolto · [[15 - Backtracking.pdf#page=2|p. 2]], [[15 - Backtracking.pdf#page=3|3]]

Risolvere un problema di **ricerca esaustiva**: enumerare le configurazioni di uno spazio di ricerca per trovare quelle che sono soluzioni. L'esempio introduttivo è il **Sudoku** (p. 2: una griglia $9 \times 9$ con alcune cifre date e la sua soluzione): risolverlo comporta una forma di ricerca esaustiva delle configurazioni possibili; **sfruttare i vincoli** per escludere certe possibilità in certe posizioni permette di **potare** la ricerca fino al punto in cui le persone riescono a risolvere il Sudoku a mano (p. 3). **Il backtracking è la chiave per implementare in modo corretto ed efficiente programmi di ricerca esaustiva** (p. 3).

![[15-backtracking-p2-sudoku.png]]

Nota a mano di p. 2 (lettura incerta): «posso creare un grafo dello spazio delle soluzioni, e una soluzione è un nodo di questo grafo ⇒ posso sapere se un nodo è soluzione o meno ma lo devo visitare ⇒ devo guardare tutto il grafo (potenzialmente)».

## Idea · [[15 - Backtracking.pdf#page=4|p. 4]], [[15 - Backtracking.pdf#page=5|5]]

Il backtracking è un **metodo sistematico per iterare su tutte le configurazioni possibili** di uno spazio di ricerca. È un algoritmo generale che va **personalizzato per ogni applicazione** (p. 4). Si modella la soluzione come un vettore $a = (a_1, a_2, \dots, a_n)$, in cui ogni elemento $a_i$ è scelto da un insieme finito e ordinato $S_i$. Il vettore può rappresentare una disposizione in cui $a_i$ contiene l'$i$-esimo elemento di una **permutazione**, oppure un **sottoinsieme** $S$ in cui $a_i$ è vero se e solo se l'$i$-esimo elemento dell'universo è in $S$.

A ogni passo (p. 5) si parte da una **soluzione parziale** $a = (a_1, \dots, a_k)$ e si prova a estenderla aggiungendo un altro elemento in fondo. Dopo l'estensione si verifica se quello che si ha è una soluzione completa. Se non lo è, la questione critica è se la soluzione parziale corrente $a$ sia **potenzialmente estendibile** a una soluzione:
- se sì, si **ricorre** e si continua;
- se no, si **cancella l'ultimo elemento** da $a$ e si prova un'altra possibilità per quella posizione, se esiste.

![[15-backtracking-p5-idea.png]]

## Pseudocodice · [[15 - Backtracking.pdf#page=7|p. 7]]

```
Backtrack (a,k)
1  if a is a solution, print (a)
2  else
3      k ← k + 1
4      compute S_k
5      while S_k ≠ ∅ do
6          a_k ← an element in S_k
7          S_k ← S_k − a_k
8          Backtrack (a,k)
```

(La slide scrive con `=` e con le parentesi graffe; qui è riportato con le convenzioni del corso. I numeri di riga sono miei; nell'animazione la numerazione è quella della slide con le parentesi graffe.)

![[15-backtracking-p7-backtrack-ricorsivo.png]]

## Backtracking e DFS · [[15 - Backtracking.pdf#page=8|p. 8]]

Il backtracking è **in realtà una [[visita-in-profondita|visita in profondità]] di un grafo implicito di configurazioni**:
- può essere usato facilmente per iterare su tutti i **sottoinsiemi** o su tutte le **permutazioni** di un insieme;
- assicura la **correttezza** enumerando *tutte* le possibilità;
- per essere **efficiente** bisogna **potare** i rami morti o ridondanti dello spazio di ricerca, quando possibile.

## Implementazione · [[15 - Backtracking.pdf#page=9|p. 9]]–[[15 - Backtracking.pdf#page=12|12]]

Implementazione in C della slide (p. 9), parametrica rispetto a quattro routine specifiche dell'applicazione:

```c
void backtrack(int a[], int k, data input) {
    int c[MAXCANDIDATES];       /* candidates for next position */
    int nc;                     /* next position candidate count */
    int i;                      /* counter */
    if (is_a_solution(a, k, input)) {
        process_solution(a, k, input);
    } else {
        k = k + 1;
        construct_candidates(a, k, input, c, &nc);
        for (i = 0; i < nc; i++) {
            a[k] = c[i];
            make_move(a, k, input);
            backtrack(a, k, input);
            unmake_move(a, k, input);
            if (finished) {
                return;         /* terminate early */
            }
        }
    }
}
```

![[15-backtracking-p9-backtrack-c.png]]

- **`is_a_solution(a, k, input)`** (p. 10): funzione booleana che verifica se i primi $k$ elementi del vettore $a$ sono una soluzione completa per il problema dato; l'ultimo argomento, `input`, permette di passare informazioni generali per valutare se $a$ è una soluzione.
- **`construct_candidates(a, k, input, c, nc)`** (p. 11): riempie un array `c` con l'insieme completo dei possibili candidati per la $k$-esima posizione di $a$, dato il contenuto delle prime $k-1$ posizioni; il numero di candidati restituiti è `nc`.
- **`process_solution(a, k)`** (p. 12): stampa, conta o in qualche modo elabora una soluzione completa una volta costruita.
- **`make_move` / `unmake_move`** (p. 9): applicano e annullano la mossa (aggiornando eventuali strutture ausiliarie); `finished` permette di terminare in anticipo.

Il backtracking **assicura la correttezza enumerando tutte le possibilità** e **l'efficienza non visitando mai uno stato più di una volta** (p. 12). Poiché a ogni chiamata ricorsiva si alloca un nuovo array di candidati `c`, i sottoinsiemi dei candidati di estensione non ancora considerati a ogni posizione **non interferiscono** fra loro.

![[15-backtracking-p12-process-solution.png]]

## Costruire tutti i sottoinsiemi · [[15 - Backtracking.pdf#page=13|p. 13]]–[[15 - Backtracking.pdf#page=18|18]]

Per costruire tutti i $2^n$ sottoinsiemi si usa un vettore di $n$ celle in cui il valore di $a_i$ è vero o falso, a indicare se l'$i$-esimo elemento è o non è nel sottoinsieme (p. 14). Nella notazione dello schema generale, $S_k = (\text{true}, \text{false})$ e $a$ è una soluzione quando $k \ge n$.

Le routine (pp. 16–18):

```c
int is_a_solution(int a[], int k, int n) {
    return (k == n);
}
void construct_candidates(int a[], int k, int n, int c[], int *nc) {
    c[0] = true;
    c[1] = false;
    *nc = 2;
}
void process_solution(int a[], int k, int input) {
    int i;                      /* counter */
    printf("{");
    for (i = 1; i <= k; i++) {
        if (a[i] == true) {
            printf(" %d", i);
        }
    }
    printf(" }\n");
}
void generate_subsets(int n) {
    int a[NMAX];                /* solution vector */
    backtrack(a, 0, n);
}
```

Qui si stampano gli elementi di ogni sottoinsieme, ma si può fare altro, per esempio verificare se è una soluzione di un problema di vertex cover (p. 17).

![[15-backtracking-p14-sottoinsiemi.png]]
![[15-backtracking-p16-sottoinsiemi-candidati.png]]
![[15-backtracking-p17-sottoinsiemi-stampa.png]]
![[15-backtracking-p18-sottoinsiemi-main.png]]

### Ordine di generazione · [[15 - Backtracking.pdf#page=15|p. 15]]

La slide chiede: in quale ordine vengono generati i sottoinsiemi di $\{1, 2, 3\}$? La sequenza di stati riportata (in rosso le soluzioni; un elemento incluso è scritto con il suo numero, uno escluso con un trattino) è

$$
\begin{aligned}
&(1) \to (1,2) \to \mathbf{(1,2,3)} \to \mathbf{(1,2,-)} \to (1,-) \to \mathbf{(1,-,3)} \to \mathbf{(1,-,-)} \to (1,-) \to (1) \to (-) \to \\
&(-,2) \to \mathbf{(-,2,3)} \to \mathbf{(-,2,-)} \to (-,-) \to \mathbf{(-,-,3)} \to \mathbf{(-,-,-)} \to (-,-) \to (-) \to ()
\end{aligned}
$$

e le foglie dell'albero sono, da sinistra a destra, $\{1,2,3\}$, $\{1,2\}$, $\{1,3\}$, $\{1\}$, $\{2,3\}$, $\{2\}$, $\{3\}$, $\{\}$. Nota a mano: «che significa che non è un algoritmo sistematico ma va verso la costruzione → sono fuso?» (lettura incerta).

![[15-backtracking-p15-sottoinsiemi-albero.png]]

> ⚠️ Contraddizione (compressione della slide): la sequenza di p. 15 omette alcune risalite (per esempio, dopo $(1,2,-)$ l'esecuzione torna a $(1,2)$ e poi a $(1)$ prima di passare a $(1,-)$). È una sottosequenza di quella eseguita davvero, verificata con [[backtracking.py]]; l'animazione 🧩 mostra tutti i passaggi.

## Esempio di esecuzione · [[15 - Backtracking.pdf#page=15|p. 15]]

![[animazione-backtracking.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero Backtrack sui sottoinsiemi di $\{1, 2, 3\}$ ($n = 3$, $S_k = (\text{true}, \text{false})$): un fotogramma per ogni ingresso in un nodo, per ogni soluzione e per ogni ritorno. I nodi sono colorati se visitati, le foglie in verde se soluzioni.

Traccia (verificata con [[backtracking.py]]): le chiamate di Backtrack sono 15; le soluzioni sono, nell'ordine, $\{1,2,3\}$, $\{1,2\}$, $\{1,3\}$, $\{1\}$, $\{2,3\}$, $\{2\}$, $\{3\}$, $\{\}$ (le foglie di p. 15).

## Correttezza · [[15 - Backtracking.pdf#page=12|p. 12]]

> 🧩 Derivazione mia. **Invariante:** a ogni chiamata Backtrack$(a, k)$ il vettore parziale $(a_1, \dots, a_k)$ è un cammino dalla radice a un nodo dell'albero delle configurazioni, e tutte le configurazioni (completate) discendenti di quel nodo verranno enumerate dalla chiamata, ciascuna una volta.
> - *Base* ($k = n$): il nodo è una foglia, `is_a_solution` è vera e si elabora la soluzione.
> - *Passo:* per $k < n$ il ciclo prova **tutti** i candidati $c \in S_{k+1}$: ogni figlio del nodo corrisponde a un candidato diverso; per ipotesi induttiva ogni chiamata su un figlio enumera le sue foglie. Poiché i figli hanno candidati distinti, nessuna configurazione è enumerata due volte («mai visitare uno stato più di una volta»); poiché si provano tutti i candidati, nessuna configurazione è saltata («enumerare tutte le possibilità»).
> - `unmake_move` (e il fatto che `c` sia locale a ogni chiamata) ripristina lo stato prima del candidato successivo: i candidati non ancora considerati non interferiscono (p. 12).

## Complessità

> 📄 Le slide non danno costi dell'enumerazione se non il numero delle configurazioni: $2^n$ sottoinsiemi (p. 14) e $n!$ permutazioni (p. 20).

### Derivazione — chiamate e costo per i sottoinsiemi
**Si parte da:** lo schema Backtrack con $S_k = (\text{true}, \text{false})$ e soluzione per $k = n$.

> 🧩 Derivazione mia. L'albero delle chiamate è un albero binario completo di altezza $n$: il livello $k$ ha $2^k$ nodi (i vettori parziali di $k$ elementi).

$$
\#\text{chiamate} = \sum_{k=0}^{n} 2^k = 2^{n+1} - 1 \qquad \#\text{soluzioni} = 2^n \qquad \text{(serie geometrica)}
$$

Ogni chiamata interna costa $O(1)$ (due candidati); ogni soluzione è elaborata in $O(n)$ (la stampa scorre $k = n$ elementi). Totale: $\Theta(2^n) + 2^n \cdot O(n) = \Theta(n\, 2^n)$. **Sanity check** ([[backtracking.py]]): $n = 3$: 15 chiamate e 8 soluzioni; $n = 8$: 511 chiamate e 256 soluzioni.
**Ipotesi:** modello RAM; costo costante per make/unmake; la soluzione è elaborata con costo lineare.

### Potatura (p. 8)
Il costo cambia radicalmente con la **potatura**: se si capisce che una soluzione parziale non è potenzialmente estendibile, si taglia il sottoalbero intero (nel Sudoku, i vincoli escludono certe cifre in certe posizioni, p. 3), e di quell'albero non si visita nulla.

## Proprietà

- **Generale:** una sola struttura di algoritmo, personalizzata con quattro routine (`is_a_solution`, `construct_candidates`, `make_move`, `unmake_move`) e `process_solution`.
- **Ricorsiva e in profondità:** è una DFS su un grafo (albero) implicito che non viene mai costruito in memoria.
- **Uscita anticipata:** con `finished` si può fermare la ricerca alla prima soluzione (verificato in [[backtracking.py]]: con $n = 4$ la prima permutazione si trova dopo 5 chiamate).

## Connessioni

- [[ricerca-combinatoria]] — il paradigma della ricerca esaustiva: il backtracking è il modo di implementarla con potatura
- [[visita-in-profondita]] — il backtracking è una DFS sul grafo implicito delle configurazioni
- [[generazione-di-permutazioni]] — l'altra istanza, con $S_k = \{1, \dots, n\} - a$
- [[exhaustive-scheduling]] (enumera i $2^n$ sottoinsiemi di intervalli) e [[optimal-tsp]] (enumera le $n!$ permutazioni dei punti) — ricerche esaustive della lezione 01 che il backtracking permette di implementare

## Fonti · [[15 - Backtracking.pdf#page=2|p. 2]]–[[15 - Backtracking.pdf#page=18|18]]

- [[lezione-15-backtracking]]

_Aggiornato: 2026-11-26 — ingest 15 - Backtracking.pdf_

<!-- nav:inizio -->
---
**Lezione 15 · pagina 2 di 3** · ← [[lezione-15-backtracking|Lezione 15: introduzione e riepilogo]] · [[lezioni|Indice]] · [[generazione-di-permutazioni|Generazione di tutte le permutazioni]] →
<!-- nav:fine -->
