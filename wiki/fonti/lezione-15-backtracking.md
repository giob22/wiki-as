---
tipo: fonte
titolo: "Lecture 15: Backtracking (S. Skiena)"
file_raw: "15 - Backtracking.pdf"
pagine: "1-24"
data_ingest: 2026-11-26
formato: slide-pdf
argomenti: [backtracking, ricerca esaustiva, sottoinsiemi, permutazioni, potatura, Sudoku]
---

# Lezione 15 — Backtracking (15 - Backtracking.pdf)

## Sommario · [[15 - Backtracking.pdf#page=1|p. 1]], [[15 - Backtracking.pdf#page=2|2]]

Slide in inglese di Steven Skiena (Stony Brook University), «Lecture 15: Backtracking», con tre note a mano del docente (pp. 2, 15, 21). Il **backtracking** è un metodo sistematico per iterare su tutte le configurazioni di uno spazio di ricerca: si modella la soluzione come un vettore $a = (a_1, \dots, a_n)$ con ogni $a_i$ scelto in un insieme finito $S_i$, si parte da una soluzione parziale, la si estende, si controlla se è completa e se è ancora estendibile; altrimenti si toglie l'ultimo elemento e si prova un'altra possibilità. È una visita in profondità su un grafo implicito di configurazioni; l'efficienza si ottiene con la potatura dei rami morti o ridondanti. Le slide danno lo schema ricorsivo (p. 7) e l'implementazione in C parametrica (`is_a_solution`, `construct_candidates`, `process_solution`, `make_move`, `unmake_move`, pp. 9–12), poi due istanze: **tutti i sottoinsiemi** ($S_k = (\text{true}, \text{false})$, $2^n$ soluzioni, pp. 13–18) e **tutte le permutazioni** ($S_k = \{1, \dots, n\} - a$, $n!$ soluzioni, pp. 19–24), con gli alberi di generazione di $\{1, 2, 3\}$.

## Percorso della lezione

Pagine del wiki nell'ordine di prima comparsa nelle slide (è l'ordine delle pagine di questa lezione nel libro):
1. [[backtracking]] — pp. 2–18: Sudoku, idea, pseudocodice, DFS, implementazione, sottoinsiemi
2. [[generazione-di-permutazioni]] — pp. 19–24: permutazioni

Già lette, riprese in questa lezione: *ricerca-combinatoria* (la ricerca esaustiva della lezione 01), *visita-in-profondita* (lezione 13), *exhaustive-scheduling* e *optimal-tsp* (i problemi della lezione 01 che enumerano sottoinsiemi e permutazioni).

**Ordine consigliato.** Le slide sono lineari; la pagina *backtracking* contiene sia lo schema sia l'istanza dei sottoinsiemi, *generazione-di-permutazioni* l'altra istanza.

## Punti chiave · [[15 - Backtracking.pdf#page=3|p. 3]]–[[15 - Backtracking.pdf#page=5|5]], [[15 - Backtracking.pdf#page=7|p. 7]]–[[15 - Backtracking.pdf#page=9|9]], [[15 - Backtracking.pdf#page=14|p. 14]], [[15 - Backtracking.pdf#page=20|20]]

1. Una ricerca esaustiva con vincoli può essere potata fino a poter risolvere un Sudoku a mano; il backtracking è la chiave per implementarla in modo corretto ed efficiente → [[backtracking]].
2. Si estende una soluzione parziale $a = (a_1, \dots, a_k)$; se non è estendibile si toglie l'ultimo elemento e si prova un'altra possibilità.
3. Backtrack$(a, k)$: se $a$ è una soluzione la si elabora, altrimenti $k \leftarrow k+1$, si calcola $S_k$ e per ogni candidato si ricorre.
4. Il backtracking è una DFS su un grafo implicito di configurazioni: corretto perché enumera tutte le possibilità, efficiente solo se si pota.
5. Sottoinsiemi: $S_k = (\text{true}, \text{false})$, soluzione per $k \ge n$, $2^n$ soluzioni.
6. Permutazioni: $S_k = \{1, \dots, n\} - a$, soluzione per $k = n$, $n!$ soluzioni → [[generazione-di-permutazioni]].

## Refusi e note · [[15 - Backtracking.pdf#page=2|p. 2]], [[15 - Backtracking.pdf#page=15|p. 15]], [[15 - Backtracking.pdf#page=21|21]]

- p. 2, p. 15 e p. 21: note a mano del docente, di lettura parzialmente incerta (trascritte nelle pagine).
- p. 15: la sequenza degli stati omette alcune risalite (⚠️ in [[backtracking]]).
- p. 21: nella sequenza compare un $()$ in più dopo $(2,3)$ (⚠️ in [[generazione-di-permutazioni]]).
- pp. 6, 13 e 19: pagine di titolo di argomento («Topic: …»).
- p. 20: $S_k = (1, \dots, n) - v$ e p. 22: $S_k = \{1, \dots, n\} - a$ (stessa cosa con due notazioni; $v$ è il vettore).
- Il codice è in C (non nelle convenzioni di pseudocodice del corso) e la slide p. 7 scrive lo pseudocodice con `=` e parentesi graffe, nello stile del C.

## Concetti introdotti

[[backtracking]], [[generazione-di-permutazioni]].

## Domande aperte

- Le slide non mostrano una potatura concreta (per esempio sul Sudoku), solo il principio: TODO se verrà trattato a lezione.
- Il costo dell'enumerazione non è dato: derivato 🧩 nelle pagine ($2^n$ e $n!$ configurazioni).

## Domande da esame

- Descrivere lo schema generale del backtracking e le routine che vanno specializzate per ogni problema.
- Perché il backtracking è una visita in profondità e in che senso il grafo è «implicito»?
- Come si genera ogni sottoinsieme di $\{1, \dots, n\}$? Qual è l'insieme dei candidati e quando $a$ è una soluzione?
- Come si genera ogni permutazione? Perché i candidati sono gli elementi non ancora usati?
- Eseguire il backtracking a mano su $n = 3$ (sottoinsiemi o permutazioni) e disegnare l'albero di generazione.
- Quante chiamate ricorsive e quante soluzioni ci sono per i sottoinsiemi e per le permutazioni? Come cambiano con la potatura?

_Aggiornato: 2026-11-26 — ingest 15 - Backtracking.pdf_

<!-- nav:inizio -->
---
**Lezione 15 · pagina 1 di 3** · ← [[backpropagation|Backpropagation]] · [[lezioni|Indice]] · [[backtracking|Backtracking]] →
<!-- nav:fine -->
