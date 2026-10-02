---
tipo: entità
categoria: algoritmo
paradigma: "[[divide-et-impera]] + [[randomizzazione]]"
fonti_pdf: ["07-Quicksort.pdf#page=19", "07-Quicksort.pdf#page=20", "07-Quicksort.pdf#page=23"]
---

# Quicksort randomizzato

## Problema risolto

[[ordinamento]] sul posto, come [[quicksort]], ma con il pivot scelto **a caso**.

## Idea

> 📄 Fonte: [[07-Quicksort.pdf#page=20]]

- Per aumentare la probabilità che in media il partizionamento effettuato da Quicksort sia ben bilanciato, si può scegliere in maniera **aleatoria** il pivot.
- La versione randomizzata di Quicksort è ritenuta la scelta migliore per ordinare array di grosse dimensioni.

È l'applicazione della [[randomizzazione]] ([[07-Quicksort.pdf#page=19]]): uno strumento per migliorare algoritmi con caso peggiore cattivo ma caso medio buono, come [[quicksort]] ($\Theta(n^2)$ contro $\Theta(n\lg n)$, [[07-Quicksort.pdf#page=2]]).

> 🧩 Spiegazione mia — cosa cambia davvero. Con il pivot fisso $A[r]$ esistono input (l'array ordinato) che portano **sempre** al caso peggiore: chi fornisce l'input decide il costo. Con il pivot casuale il costo dipende dalle scelte casuali dell'algoritmo, non dall'input: nessun input è sistematicamente cattivo. Il caso peggiore $\Theta(n^2)$ esiste ancora (scelte sfortunate a ogni livello), ma ha probabilità bassissima.

## Pseudocodice

> 📄 Fonte: [[07-Quicksort.pdf#page=20]] (riportato fedelmente; le due procedure sono affiancate nella slide, numeri di riga miei e continui per poterli usare nell'animazione)

```
Randomized-Quicksort (A,p,r)
1  if p<r
2      q ← Randomized-Partition (A,p,r)
3      Randomized-Quicksort (A,p,q-1)
4      Randomized-Quicksort (A,q+1,r)

Randomized-Partition (A,p,r)
5  i ← Random (p,r)
6  exchange A[r] ↔ A[i]
7  return Partition (A,p,r)
```

Simboli: `Random (p,r)` restituisce un indice intero tra $p$ e $r$ scelto a caso (🧩: la slide non lo definisce; si intende con la stessa probabilità $\frac{1}{r-p+1}$ per ogni indice, 📚 Cormen, 3ª ed., §5.1). Lo scambio della riga 6 porta l'elemento scelto in $A[r]$, dove [[partition]] si aspetta il pivot.

![[07-quicksort-p20-quicksort-randomizzato.png]]

> 🧩 Spiegazione mia — la riga 6 è tutta la modifica: [[partition]] resta identica e continua a usare $A[r]$, ma ora $A[r]$ è un elemento qualsiasi del sotto-array, ciascuno con la stessa probabilità.

## Esempio di esecuzione

![[animazione-quicksort-randomizzato.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo su un'istanza mia: l'array **già ordinato** ⟨1, 2, …, 8⟩, cioè il caso peggiore del [[quicksort]] deterministico ([[07-Quicksort.pdf#page=14]]). Ogni chiamata mostra l'indice estratto da `Random(p, r)` (generatore con seme fisso), lo scambio con $A[r]$ e la posizione $q$ del pivot. Con il pivot fisso $A[r]$ questo input darebbe 7 livelli di ricorsione; con il pivot casuale l'albero resta basso.

> 🧩 Sanity check sul costo ([[divide_et_impera.py]], media di 20 esecuzioni su input **ordinato**):

| $n$ | confronti medi (randomizzato) | $n \lg n$ | $n(n-1)/2$ (deterministico) |
|-----|-------------------------------|-----------|-----------------------------|
| 100 | 643 | 664 | 4 950 |
| 1 000 | 11 093 | 9 966 | 499 500 |
| 10 000 | 156 787 | 132 877 | 49 995 000 |

Il randomizzato resta vicino a $n \lg n$ anche sull'input peggiore del deterministico.

## Correttezza

> 🧩 Derivazione mia: Randomized-Partition è uno scambio seguito da [[partition]]. Lo scambio non cambia l'insieme degli elementi di $A[p..r]$, e Partition è corretta per qualsiasi valore in $A[r]$ ([[07-Quicksort.pdf#page=13]]). La dimostrazione per induzione di [[quicksort]] § Correttezza vale identica: la correttezza **non** dipende dalle scelte casuali, solo il tempo.

## Complessità

> 📄 Fonte: [[07-Quicksort.pdf#page=23]]

- Nella versione randomizzata è di interesse il **tempo di esecuzione atteso**.
- Si dimostra che è $O(n \log n)$.
- Dimostrazione sul libro di testo.

> 📚 Fonte esterna: la dimostrazione è in Cormen, Leiserson, Rivest, Stein, *Introduzione agli algoritmi e strutture dati*, 3ª ed., §7.4.2 («Tempo di esecuzione atteso»). Il wiki non la ricostruisce perché la slide la rimanda al libro.

> 🧩 Spiegazione mia — cosa vuol dire «atteso»: è la **media sulle scelte casuali** dell'algoritmo, per un input **qualsiasi** fissato. Il «caso medio» di [[quicksort]] ([[07-Quicksort.pdf#page=18]]) era invece una media sugli **input**, e richiedeva un'ipotesi sulla loro distribuzione. Per la versione randomizzata non serve: la casualità la mette l'algoritmo.

| Caso | Tempo | Pagina |
|------|-------|--------|
| atteso (qualsiasi input) | $O(n \log n)$ | [[07-Quicksort.pdf#page=23]] |
| peggiore (scelte sfortunate a ogni livello) | $\Theta(n^2)$ (🧩: la dimostrazione di pp. 21–22 vale per ogni scelta del pivot) | [[07-Quicksort.pdf#page=21]] |

**Spazio:** come [[quicksort]], sul posto; pila delle chiamate $\Theta(\lg n)$ attesa e $\Theta(n)$ nel caso peggiore (🧩).

## Proprietà

- **Sul posto**, **non stabile** (come [[quicksort]], 🧩).
- **Algoritmo randomizzato** — 🧩: a parità di input, due esecuzioni possono fare scelte diverse e costi diversi, ma producono sempre lo stesso output ordinato.

## Connessioni

- [[randomizzazione]] — il principio generale (p. 19)
- [[quicksort]] — la versione deterministica: stesso pseudocodice a meno di Randomized-Partition
- [[partition]] — invariata, riceve il pivot già spostato in $A[r]$
- [[nuts-and-bolts]] — stessa idea di pivot casuale, applicata a dadi e bulloni
- [[casi-di-complessita]] — tempo atteso contro caso medio

## Fonti

- [[lezione-07-quicksort]]
- [[07-Quicksort.pdf#page=19]], [[07-Quicksort.pdf#page=20]], [[07-Quicksort.pdf#page=23]]

_Aggiornato: 2026-10-01 — ingest 07-Quicksort.pdf_
