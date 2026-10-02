---
tipo: fonte
titolo: "Corso di Algoritmi e Strutture Dati — Quicksort"
file_raw: "07-Quicksort.pdf"
pagine: "1-25"
data_ingest: 2026-10-01
formato: slide-pdf
argomenti: [quicksort, partition, invariante di ciclo, caso peggiore, caso migliore, partizionamento bilanciato, caso medio, randomizzazione, quicksort randomizzato, nuts and bolts]
---

# Lezione 07 — Quicksort (07-Quicksort.pdf)

## Sommario

Slide del Prof. Marrone, a.a. 26/27 ([[07-Quicksort.pdf#page=1]]). La lezione presenta **quicksort**: tempi $\Theta(n^2)$ nel caso peggiore e $\Theta(n\lg n)$ nel caso medio, ordinamento sul posto, schema divide et impera con Combine vuoto, pseudocodice. Segue **Partition** con pivot $A[r]$: le quattro aree, una traccia passo per passo su ⟨2, 8, 7, 1, 3, 5, 6, 4⟩, lo pseudocodice, il costo $\Theta(n)$ e l'invariante. L'analisi esamina il partizionamento sbilanciato (caso peggiore, input ordinato), quello bilanciato (caso migliore, teorema dell'esperto), quello con rapporto costante 9:1 (albero di ricorrenza) e l'alternanza di partizioni buone e cattive (caso medio). Introduce la **randomizzazione** e **quicksort randomizzato**, dimostra per sostituzione che il caso peggiore è $\Theta(n^2)$ e rimanda al libro per il tempo atteso $O(n\log n)$. Chiude con lo «Stop and Think» **Nuts and Bolts**.

## Punti chiave

1. Quicksort: $\Theta(n^2)$ caso peggiore, $\Theta(n\lg n)$ caso «medio», sul posto, costanti nascoste piccole ([[07-Quicksort.pdf#page=2]]) → [[quicksort]].
2. Divide (partizione attorno al pivot), Conquer (due chiamate ricorsive), Combine (niente da fare) ([[07-Quicksort.pdf#page=3]]) → [[divide-et-impera]].
3. Pseudocodice di Quicksort, invocato come `Quicksort(A,1,length[A])` ([[07-Quicksort.pdf#page=4]]).
4. Partition: pivot $x = A[r]$, quattro aree $p..i$, $i+1..j-1$, $j..r-1$, $r$; regola di aggiornamento delle barriere ([[07-Quicksort.pdf#page=5]], [[07-Quicksort.pdf#page=6]]) → [[partition]].
5. Traccia di Partition su ⟨2, 8, 7, 1, 3, 5, 6, 4⟩: risultato ⟨2, 1, 3, 4, 7, 5, 6, 8⟩, $q = 4$ ([[07-Quicksort.pdf#page=7]]–[[07-Quicksort.pdf#page=11]]).
6. Pseudocodice di Partition e costo $\Theta(n)$, $n = r - p + 1$ ([[07-Quicksort.pdf#page=12]]).
7. Invariante di Partition: $A[k] \le x$ per $p \le k \le i$, $A[k] > x$ per $i+1 \le k \le j-1$, $A[r] = x$ ([[07-Quicksort.pdf#page=13]]) → [[invariante-di-ciclo]].
8. Caso peggiore: partizioni $n - 1$ e 0, $T(n) = T(n-1) + \Theta(n) = \Theta(n^2)$; si ha con il vettore ordinato, su cui insertion sort è $O(n)$ ([[07-Quicksort.pdf#page=14]]) → [[casi-di-complessita]].
9. Caso migliore: partizioni $\lfloor n/2 \rfloor$ e $\lceil n/2 \rceil - 1$, $T(n) \le 2T(n/2) + \Theta(n) = O(n\lg n)$ dal caso 2 del teorema dell'esperto ([[07-Quicksort.pdf#page=15]]) → [[teorema-dell-esperto]].
10. Rapporto 9:1: $T(n) \le T(9n/10) + T(n/10) + cn$, $\Theta(\lg n)$ livelli di costo $\le cn$, $O(n\lg n)$; vale per ogni rapporto costante ([[07-Quicksort.pdf#page=16]], [[07-Quicksort.pdf#page=17]]) → [[metodo-albero-di-ricorrenza]].
11. Caso medio: partizioni buone e cattive alternate, il costo della cattiva è assorbito dalla buona ([[07-Quicksort.pdf#page=18]]).
12. Randomizzazione per algoritmi con caso peggiore cattivo e caso medio buono: random sampling, randomized hashing, random search ([[07-Quicksort.pdf#page=19]]) → [[randomizzazione]].
13. Quicksort randomizzato: Randomized-Partition sceglie il pivot con `Random(p,r)` ([[07-Quicksort.pdf#page=20]]) → [[quicksort-randomizzato]].
14. Caso peggiore $O(n^2)$ per sostituzione con $\max_q (T(q) + T(n-q-1))$ e massimo agli estremi; con il caso sbilanciato, $\Theta(n^2)$ ([[07-Quicksort.pdf#page=21]], [[07-Quicksort.pdf#page=22]]) → [[metodo-di-sostituzione]].
15. Tempo atteso della versione randomizzata $O(n\log n)$, dimostrazione sul libro ([[07-Quicksort.pdf#page=23]]).
16. S&T Nuts and Bolts: algoritmo $O(n^2)$ e algoritmo randomizzato $O(n\log n)$ atteso ([[07-Quicksort.pdf#page=24]], [[07-Quicksort.pdf#page=25]]) → [[nuts-and-bolts]].

## Refusi e note

- p. 15: il testo estratto mostra «⌊n/2⌊ e ⌊n/2⌊-1»; nella figura le dimensioni sono $\lfloor n/2 \rfloor$ e $\lceil n/2 \rceil - 1$.
- p. 12: la slide conta «$n$ iterazioni»: il corpo del `for` si esegue $n - 1$ volte e il test $n$ volte (🧩, in [[partition]]). Stesso $\Theta(n)$.
- p. 13: la conservazione dell'invariante è solo enunciata; la dimostrazione è in [[partition]] (🧩).
- p. 18: argomento intuitivo, non una dimostrazione; la slide stessa dice «Intuitivamente».
- p. 21: nella ricorrenza $q$ indica la **dimensione** del sottoproblema sinistro, non l'indice restituito da Partition. Il caso base $T(0)$ non è trattato (🧩, in [[quicksort]]).
- p. 23: la dimostrazione del tempo atteso è rimandata al libro (📚 Cormen §7.4.2): il wiki non la ricostruisce.
- p. 25: testo del problema in inglese; nessuna soluzione nelle slide (soluzioni 🧩 in [[nuts-and-bolts]]).
- `Random(p,r)` non è definita nella slide (🧩: intero uniforme in $p..r$).

## Concetti introdotti

[[quicksort]], [[partition]], [[quicksort-randomizzato]], [[randomizzazione]], [[nuts-and-bolts]]; aggiornati [[metodo-di-sostituzione]], [[metodo-albero-di-ricorrenza]], [[teorema-dell-esperto]], [[casi-di-complessita]], [[ordinamento]], [[invariante-di-ciclo]], [[progettazione-divide-et-impera]].

## Domande aperte

- Il caso medio è solo intuitivo (p. 18) e la dimostrazione del tempo atteso è sul libro (p. 23).
- La slide non tratta lo spazio della pila di ricorsione (🧩: $\Theta(n)$ nel caso peggiore).
- Nuts and Bolts: le slide non danno soluzioni; quelle del wiki sono mie.

## Domande da esame

- Scrivere Quicksort e Partition; eseguire Partition su un array dato mostrando le quattro aree.
- Enunciare e dimostrare l'invariante di Partition.
- Caso peggiore: quando si verifica, ricorrenza, soluzione; confronto con insertion sort sull'input ordinato.
- Caso migliore e partizione 9:1: perché $O(n\lg n)$ anche con rapporto 99:1?
- Dimostrare per sostituzione che il caso peggiore è $O(n^2)$ (massimo agli estremi) e poi $\Theta(n^2)$.
- Quicksort randomizzato: pseudocodice, cosa significa tempo atteso, differenza dal caso medio.
- Nuts and Bolts: algoritmo quadratico e randomizzato.

_Aggiornato: 2026-10-01 — ingest 07-Quicksort.pdf_
