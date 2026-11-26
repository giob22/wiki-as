---
tipo: fonte
titolo: "Corso di Algoritmi e Strutture Dati — Quicksort"
file_raw: "07-Quicksort 1.pdf"
pagine: "1-25"
data_ingest: 2026-10-14
formato: slide-pdf
argomenti: [quicksort, partition, invariante di ciclo, caso peggiore, caso migliore, partizionamento bilanciato, caso medio, randomizzazione, quicksort randomizzato, nuts and bolts]
---

# Lezione 07 — Quicksort (07-Quicksort 1.pdf) · [[07-Quicksort.pdf|Quicksort (vecchia)]]

> Versione aggiornata delle slide, che sostituisce la precedente (ingerita il 2026-10-01). Le 25 pagine sono identiche e nello stesso ordine; l'unica differenza sono le **annotazioni a mano a p. 4**, accanto allo pseudocodice di Quicksort (→ [[quicksort]] § Pseudocodice). Tutti i link del wiki puntano alla nuova versione.

## Sommario · [[07-Quicksort 1.pdf#page=1|p. 1]]

Slide del Prof. Marrone, a.a. 26/27. La lezione presenta **quicksort**: tempi $\Theta(n^2)$ nel caso peggiore e $\Theta(n\lg n)$ nel caso medio, ordinamento sul posto, schema divide et impera con Combine vuoto, pseudocodice. Segue **Partition** con pivot $A[r]$: le quattro aree, una traccia passo per passo su ⟨2, 8, 7, 1, 3, 5, 6, 4⟩, lo pseudocodice, il costo $\Theta(n)$ e l'invariante. L'analisi esamina il partizionamento sbilanciato (caso peggiore, input ordinato), quello bilanciato (caso migliore, teorema dell'esperto), quello con rapporto costante 9:1 (albero di ricorrenza) e l'alternanza di partizioni buone e cattive (caso medio). Introduce la **randomizzazione** e **quicksort randomizzato**, dimostra per sostituzione che il caso peggiore è $\Theta(n^2)$ e rimanda al libro per il tempo atteso $O(n\log n)$. Chiude con lo «Stop and Think» **Nuts and Bolts**.

## Percorso della lezione · [[07-Quicksort 1.pdf|Quicksort]]

**PDF:** (pp. 1–25; versione aggiornata, uguale alla precedente salvo le annotazioni di p. 4)

Pagine del wiki nell'ordine di prima comparsa nelle slide (è l'ordine delle pagine di questa lezione nel libro, dopo questa):
1. [[quicksort]] — pp. 2–4 (poi pp. 14–18, 21–22) · proprietà, divide/conquer/combine, pseudocodice con le annotazioni a mano (p. 4); complessità organizzata per metodo: la ricorrenza $T(q) + T(n-q-1) + \Theta(n)$, poi caso peggiore per srotolamento (p. 14), migliore con il teorema dell'esperto (p. 15), 9:1 con l'albero (pp. 16–17), medio (p. 18), dimostrazione $\Theta(n^2)$ per sostituzione (pp. 21–22)
2. [[partition]] — pp. 5–13 · quattro aree, traccia su ⟨2, 8, 7, 1, 3, 5, 6, 4⟩, pseudocodice e costo $\Theta(n)$ (p. 12), invariante (p. 13)
3. [[randomizzazione]] — p. 19 (poi pp. 20, 23) · caso peggiore cattivo e caso medio buono; tempo atteso contro caso medio
4. [[quicksort-randomizzato]] — pp. 20, 23 · Randomized-Partition, tempo atteso $O(n\log n)$ (dimostrazione sul libro)
5. [[nuts-and-bolts]] — pp. 24–25 · S&T: algoritmo $O(n^2)$ e randomizzato $O(n\log n)$ atteso (soluzioni 🧩)
6. [[progettazione-divide-et-impera]] — esercizi: Torre di Hanoi (L06), Nuts and Bolts, massimo sottoarray

Già lette, con casi nuovi da questa lezione: *divide-et-impera* (p. 3), *metodo-albero-di-ricorrenza* (pp. 16–18), *teorema-dell-esperto* (p. 15), *metodo-di-sostituzione* (p. 21), *casi-di-complessita* (pp. 14–18, 23), *insertion-sort* (p. 14, confronto sul vettore ordinato), *ordinamento* (righe di quicksort), *invariante-di-ciclo* (p. 13), *risoluzione-ricorrenze* (caso 6), *dimostrazioni-di-correttezza* (casi 9–10).

**Ordine consigliato.**
Le slide presentano quicksort (pp. 2–4), poi Partition (pp. 5–13), poi tornano all'analisi di quicksort (pp. 14–18), la interrompono con la randomizzazione (pp. 19–20) e la riprendono con la dimostrazione del caso peggiore (pp. 21–22). Ordine suggerito:
1. *partition* per intero: è il cuore di quicksort, e la traccia di pp. 7–11 è la prima chiamata dell'esempio;
2. *quicksort* per intero, compresa la dimostrazione di pp. 21–22 (sta nella stessa sezione «Complessità»);
3. *randomizzazione* e *quicksort-randomizzato*;
4. *nuts-and-bolts*, poi *progettazione-divide-et-impera* per ripassare la progettazione su entrambe le lezioni.

## Punti chiave · [[07-Quicksort 1.pdf#page=2|p. 2]]–[[07-Quicksort 1.pdf#page=7|7]], [[07-Quicksort 1.pdf#page=11|p. 11]]–[[07-Quicksort 1.pdf#page=25|25]]

1. Quicksort: $\Theta(n^2)$ caso peggiore, $\Theta(n\lg n)$ caso «medio», sul posto, costanti nascoste piccole → [[quicksort]].
2. Divide (partizione attorno al pivot), Conquer (due chiamate ricorsive), Combine (niente da fare) → [[divide-et-impera]].
3. Pseudocodice di Quicksort, invocato come `Quicksort(A,1,length[A])`.
4. Partition: pivot $x = A[r]$, quattro aree $p..i$, $i+1..j-1$, $j..r-1$, $r$; regola di aggiornamento delle barriere → [[partition]].
5. Traccia di Partition su ⟨2, 8, 7, 1, 3, 5, 6, 4⟩: risultato ⟨2, 1, 3, 4, 7, 5, 6, 8⟩, $q = 4$.
6. Pseudocodice di Partition e costo $\Theta(n)$, $n = r - p + 1$.
7. Invariante di Partition: $A[k] \le x$ per $p \le k \le i$, $A[k] > x$ per $i+1 \le k \le j-1$, $A[r] = x$ → [[invariante-di-ciclo]].
8. Caso peggiore: partizioni $n - 1$ e 0, $T(n) = T(n-1) + \Theta(n) = \Theta(n^2)$; si ha con il vettore ordinato, su cui insertion sort è $O(n)$ → [[casi-di-complessita]].
9. Caso migliore: partizioni $\lfloor n/2 \rfloor$ e $\lceil n/2 \rceil - 1$, $T(n) \le 2T(n/2) + \Theta(n) = O(n\lg n)$ dal caso 2 del teorema dell'esperto → [[teorema-dell-esperto]].
10. Rapporto 9:1: $T(n) \le T(9n/10) + T(n/10) + cn$, $\Theta(\lg n)$ livelli di costo $\le cn$, $O(n\lg n)$; vale per ogni rapporto costante → [[metodo-albero-di-ricorrenza]].
11. Caso medio: partizioni buone e cattive alternate, il costo della cattiva è assorbito dalla buona.
12. Randomizzazione per algoritmi con caso peggiore cattivo e caso medio buono: random sampling, randomized hashing, random search → [[randomizzazione]].
13. Quicksort randomizzato: Randomized-Partition sceglie il pivot con `Random(p,r)` → [[quicksort-randomizzato]].
14. Caso peggiore $O(n^2)$ per sostituzione con $\max_q (T(q) + T(n-q-1))$ e massimo agli estremi; con il caso sbilanciato, $\Theta(n^2)$ → [[metodo-di-sostituzione]].
15. Tempo atteso della versione randomizzata $O(n\log n)$, dimostrazione sul libro.
16. S&T Nuts and Bolts: algoritmo $O(n^2)$ e algoritmo randomizzato $O(n\log n)$ atteso → [[nuts-and-bolts]].

## Refusi e note · [[07-Quicksort 1.pdf#page=6|p. 6]]

- p. 4 (annotazioni a mano): «logica base è gestita da quicksort non entrando nell'if»; «pivot piccolo: troppi swap», «pivot grande: sposto solo una barriera». La seconda nota è invertita rispetto alla regola di Partition di p. 6: con il pivot piccolo avanza solo la barriera $j$, con il pivot grande si fanno molti scambi (⚠️, verificato con il codice in [[quicksort]]).
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
_Aggiornato: 2026-10-14 — ingest della versione aggiornata 07-Quicksort 1.pdf_
_Aggiornato: 2026-10-28 — aggiunto il «Percorso della lezione» (spostato dall'indice lezioni.md)_

<!-- nav:inizio -->
---
**Lezione 07 · pagina 1 di 7** · ← [[teorema-dell-esperto|Teorema dell'esperto (metodo dell'esperto)]] · [[lezioni|Indice]] · [[quicksort|Quicksort]] →
<!-- nav:fine -->
