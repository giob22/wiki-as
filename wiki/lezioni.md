# Indice

Il wiki si legge come un libro: ogni lezione si apre con la sua pagina di introduzione e riepilogo, poi seguono le pagine nell'ordine delle slide. In fondo a ogni pagina: pagina precedente · indice · pagina successiva.

## Lezione 00 — Presentazione del corso
1. [[presentazione-del-corso|Introduzione e riepilogo]]

## Materiale di supporto — a1: convenzioni per lo pseudocodice
1. [[convenzioni-per-lo-pseudocodice|Introduzione e riepilogo]]
2. [[pseudocodice|Convenzioni per lo pseudocodice]]

## Lezione 01 — Introduzione: concetti fondamentali
1. [[lezione-01-introduzione|Introduzione e riepilogo]]
2. [[algoritmo-e-problema|Algoritmo, problema computazionale, istanza, correttezza, struttura dati]]
3. [[ordinamento|Problema dell'ordinamento (Sorting)]]
4. [[efficienza-degli-algoritmi|Efficienza degli algoritmi («Algorithms as a technology»)]]
5. [[stima-dei-tempi-di-esecuzione|Stima dei tempi di esecuzione e dell'n massimo risolvibile]]
6. [[robot-tour-optimization|Robot Tour Optimization (problema del commesso viaggiatore, TSP)]]
7. [[nearest-neighbor|NearestNeighbor (Soluzione 1 del Robot Tour)]]
8. [[closest-pair|ClosestPair (Soluzione 2 del Robot Tour)]]
9. [[optimal-tsp|OptimalTSP (Soluzione 3 del Robot Tour)]]
10. [[ricerca-combinatoria|Ricerca combinatoria (ricerca esaustiva)]]
11. [[metodi-euristici|Metodi euristici (e differenza tra algoritmi ed euristiche)]]
12. [[movie-scheduling|Movie Scheduling Problem (selezione di intervalli)]]
13. [[earliest-job-first|EarliestJobFirst (Soluzione 1 del Movie Scheduling)]]
14. [[shortest-job-first|ShortestJobFirst (Soluzione 2 del Movie Scheduling)]]
15. [[exhaustive-scheduling|ExhaustiveScheduling (Soluzione 3 del Movie Scheduling)]]
16. [[optimal-scheduling|OptimalScheduling (Soluzione 4 del Movie Scheduling)]]
17. [[ricerca-di-controesempi|Incorrettezza e ricerca di controesempi]]
18. [[controesempi-per-euristiche|Trovare controesempi per euristiche (greedy)]]

## Lezione 02 — Notazione asintotica
1. [[lezione-02-notazione-asintotica|Introduzione e riepilogo]]
2. [[modello-ram|Modello di calcolo RAM]]
3. [[tempo-di-esecuzione|Analisi di un algoritmo: tempo di esecuzione (e spazio)]]
4. [[casi-di-complessita|Caso peggiore, migliore e medio]]
5. [[notazione-asintotica|Notazione asintotica: O, Ω, Θ]]
6. [[dimostrazioni-notazione-asintotica|Dimostrare (o confutare) f = O/Ω/Θ(g)]]
7. [[regole-di-calcolo-asintotico|Regole di calcolo con la notazione asintotica]]
8. [[dominanza-asintotica|Dominanza asintotica, little-o e crescita delle funzioni]]

## Lezione 03 — Analisi di correttezza e di complessità degli algoritmi
1. [[lezione-03-analisi-di-algoritmi|Introduzione e riepilogo]]
2. [[paradigmi-di-progettazione|Paradigmi (famiglie) di progettazione degli algoritmi]]
3. [[divide-et-impera|Divide et impera]]
4. [[iterazione-e-ricorsione|Iterazione e ricorsione]]
5. [[somma-iterativa|somma_iterativa — somma dei primi n interi (versione iterativa)]]
6. [[somma-ricorsiva|somma_ricorsiva — somma dei primi n interi (versione ricorsiva)]]
7. [[correttezza-parziale-e-totale|Correttezza parziale e correttezza totale]]
8. [[invariante-di-ciclo|Invariante di ciclo (correttezza degli algoritmi iterativi)]]
9. [[correttezza-per-induzione|Correttezza degli algoritmi ricorsivi (per induzione)]]
10. [[dimostrazioni-di-correttezza|Dimostrazioni di correttezza (invariante e induzione)]]
11. [[analisi-del-costo-riga-per-riga|Analisi del costo riga per riga]]
12. [[equazioni-di-ricorrenza|Equazioni di ricorrenza (costo degli algoritmi ricorsivi)]]
13. [[risoluzione-ricorrenze|Scrivere e risolvere equazioni di ricorrenza]]

## Lezione 04 — Strutture dati elementari
1. [[lezione-04-strutture-dati-elementari|Introduzione e riepilogo]]
2. [[tipo-di-dato-astratto|Astrazione dei dati (operazioni astratte vs implementazione)]]
3. [[strutture-contigue-e-collegate|Strutture dati contigue e collegate (e puntatori)]]
4. [[array|Array]]
5. [[array-dinamico|Array dinamico (raddoppio della capacità)]]
6. [[lista-concatenata|Lista concatenata (semplice e doppia)]]
7. [[pila|Pila (stack) — LIFO]]
8. [[coda|Coda (queue) — FIFO]]
9. [[tracce-pila-e-coda|Tracce di operazioni su pila e coda (su array)]]

## Lezione 05 — Insertion sort
1. [[lezione-05-insertion-sort|Introduzione e riepilogo]]
2. [[insertion-sort|Insertion sort]]
3. [[selection-sort|Selection sort (Esercizio del libro di testo 2.2.2)]]
4. [[substring-pattern-matching|Substring Pattern Matching (ricerca di una sottostringa)]]
5. [[findmatch|findmatch — pattern matching a forza bruta]]
6. [[logaritmi-nell-analisi|L'importanza dei logaritmi]]
7. [[potenza-veloce|power(a, n) — potenza veloce (fast exponentiation)]]

## Lezione 06 — Divide et impera: Merge Sort
1. [[lezione-06-merge-sort|Introduzione e riepilogo]]
2. [[torre-di-hanoi|Torre di Hanoi]]
3. [[merge-sort|Merge sort]]
4. [[merge|Merge (fusione di sequenze ordinate)]]
5. [[massimo-sottoarray|Problema del massimo sottoarray]]
6. [[metodo-di-sostituzione|Metodo di sostituzione]]
7. [[metodo-albero-di-ricorrenza|Metodo dell'albero di ricorrenza]]
8. [[teorema-dell-esperto|Teorema dell'esperto (metodo dell'esperto)]]

## Lezione 07 — Quicksort
1. [[lezione-07-quicksort|Introduzione e riepilogo]]
2. [[quicksort|Quicksort]]
3. [[partition|Partition]]
4. [[randomizzazione|Randomizzazione]]
5. [[quicksort-randomizzato|Quicksort randomizzato]]
6. [[nuts-and-bolts|Nuts and Bolts (dadi e bulloni)]]
7. [[progettazione-divide-et-impera|Progettazione di algoritmi divide et impera]]

## Lezione 08 — Grafi e alberi
1. [[lezione-08-grafi-e-alberi|Introduzione e riepilogo]]
2. [[grafo|Grafo]]
3. [[tipi-di-grafo|Tipi di grafo («flavors of graphs»)]]
4. [[matrice-di-adiacenza|Matrice di adiacenza]]
5. [[liste-di-adiacenza|Liste di adiacenza]]
6. [[albero|Albero]]

## Lezione 09 — Alberi binari di ricerca
1. [[lezione-09-alberi-binari-di-ricerca|Introduzione e riepilogo]]
2. [[coda-di-priorita|Coda di priorità]]
3. [[albero-binario-di-ricerca|Albero binario di ricerca (BST)]]
4. [[inorder-tree-walk|Inorder-Tree-Walk (visita in ordine)]]
5. [[tree-search|Tree-Search (ricerca in un BST)]]
6. [[tree-minimum-maximum|Tree-Minimum e Tree-Maximum]]
7. [[tree-successor|Tree-Successor (successore di un nodo)]]
8. [[tree-insert|Tree-Insert (inserimento in un BST)]]
9. [[tree-delete|Tree-Delete (eliminazione da un BST)]]
