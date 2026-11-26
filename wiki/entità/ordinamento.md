---
tipo: entità
categoria: problema
fonti_pdf: ["01-Introduzione.pdf#page=7", "01-Introduzione.pdf#page=11", "05-Insertion sort.pdf#page=2", "05-Insertion sort.pdf#page=3"]
---

# Problema dell'ordinamento (Sorting)

## Definizione formale · 01-Introduzione.pdf [[01-Introduzione.pdf#page=7|p. 7]] · 05-Insertion sort.pdf [[05-Insertion sort.pdf#page=2|p. 2]]

- **Problem:** Sorting
- **Input:** una sequenza di $n$ chiavi $a_1, \dots, a_n$
- **Output:** la permutazione (riordinamento) della sequenza d'ingresso $a'_1, \dots, a'_n$ tale che $a'_1 \le a'_2 \le \dots \le a'_n$

È l'esempio con cui la lezione 01 introduce le nozioni di problema computazionale e di [[algoritmo-e-problema|istanza]].

> 📄 La lezione 05 riprende la stessa definizione in italiano

**Problema:** data una sequenza di $n$ valori di ingresso $(a_1, a_2, \dots, a_n)$, determinare una permutazione $(a'_1, a'_2, \dots, a'_n)$ della sequenza di ingresso tale che $a'_1 \le a'_2 \le \dots \le a'_n$.

## Applicazioni · [[05-Insertion sort.pdf#page=3|p. 3]]

L'ordinamento serve come passo di molti altri problemi: **Searching**, **Closest pair**, **Element uniqueness**, **Frequency distribution**, **Selection in an array**, **Convex hulls**, «…».

> *«Sorting lies at the heart of many algorithms. Sorting the data is one of the first things any algorithm designer should try in the quest for efficiency.»*

> 🧩 Spiegazione mia di come l'ordinamento aiuta in ciascuno (la slide dà solo l'elenco; ogni esempio usa il fatto che, dopo l'ordinamento, gli elementi «simili» sono adiacenti):
> - *Searching*: in un array ordinato si può cercare dimezzando l'intervallo (ricerca binaria, [[logaritmi-nell-analisi]]).
> - *Closest pair* (la coppia di numeri più vicini): dopo l'ordinamento è tra due elementi consecutivi, basta una scansione.
> - *Element uniqueness* (ci sono duplicati?): i duplicati diventano adiacenti.
> - *Frequency distribution* (quale elemento compare più spesso?): le copie uguali formano blocchi contigui da contare.
> - *Selection in an array* (il $k$-esimo più piccolo): dopo l'ordinamento è $A[k]$.
> - *Convex hulls* (involucro convesso di punti nel piano): si ordinano i punti per coordinata e li si scandisce in quell'ordine.

![[05-insertion-sort-p3-applicazioni-ordinamento.png]]

## Algoritmi che lo risolvono · 05-Insertion sort.pdf [[05-Insertion sort.pdf#page=24|p. 22]], [[05-Insertion sort.pdf#page=26|p. 24]], [[05-Insertion sort.pdf#page=38|p. 33]] · Merge Sort [[06-Merge Sort (1).pdf#page=7|p. 7]], [[06-Merge Sort (1).pdf#page=29|p. 27]] · Quicksort [[07-Quicksort 1.pdf#page=2|p. 2]], [[07-Quicksort 1.pdf#page=14|p. 14]], [[07-Quicksort 1.pdf#page=15|15]], [[07-Quicksort 1.pdf#page=20|p. 20]], [[07-Quicksort 1.pdf#page=23|p. 23]]

| Algoritmo | Caso migliore | Caso peggiore | Spazio aggiuntivo |
|---|---|---|---|
| [[insertion-sort]] | $\Theta(n)$ (già ordinato) | $\Theta(n^2)$ (ordine decrescente) | $\Theta(1)$, sul posto |
| [[selection-sort]] | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(1)$ (🧩) |
| [[merge-sort]] | $\Theta(n\lg n)$ | $\Theta(n\lg n)$ | $\Theta(n)$, **non** sul posto |
| [[quicksort]] | $\Theta(n\lg n)$ (partizioni bilanciate) | $\Theta(n^2)$ (vettore ordinato) | sul posto (pila da $\Theta(\lg n)$ a $\Theta(n)$, 🧩) |
| [[quicksort-randomizzato]] | — | $\Theta(n^2)$ (improbabile); **atteso** $O(n\log n)$ | sul posto |

Confronto numerico su $n = 10^6$ a $10^9$ op/s: ≈ 16.7 minuti (insertion sort, $n^2$) contro ≈ 0.02 secondi (merge sort, $n \log n$) — derivazione in [[efficienza-degli-algoritmi]].

> 🧩 Osservazione mia sulla tabella: l'input già ordinato è il caso **migliore** di insertion sort e il caso **peggiore** di quicksort con pivot $A[r]$; merge sort non distingue gli input. Merge sort e insertion sort sono stabili, quicksort no (dettagli nelle pagine degli algoritmi).

## Altre occorrenze · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=4|p. 4]], [[03-Analisi di algoritmi.pdf#page=22|p. 22]] · 02-Notazione asintotica.pdf [[02-Notazione asintotica.pdf#page=3|p. 3]], [[02-Notazione asintotica.pdf#page=5|p. 5]] · Pseudocodice [[a1-indicazioni_psuedocodice.pdf#page=4|p. 4]]

- Per gli algoritmi di ordinamento la **dimensione dell'input** è la lunghezza della sequenza da ordinare → [[tempo-di-esecuzione]].
- «"Sort" is not a single step operation» nel [[modello-ram]].
- Ordinamento è uno degli esempi classici di [[divide-et-impera]].
- Nello pseudocodice degli esercizi, `sort` può essere usata come funzione di libreria solo se esplicitamente consentito → [[pseudocodice]].

## Fonti · 01-Introduzione.pdf [[01-Introduzione.pdf#page=7|p. 7]], [[01-Introduzione.pdf#page=11|p. 11]] · 05-Insertion sort.pdf [[05-Insertion sort.pdf#page=2|p. 2]], [[05-Insertion sort.pdf#page=3|3]]

- [[lezione-01-introduzione]], [[lezione-05-insertion-sort]], [[lezione-06-merge-sort]], [[lezione-07-quicksort]]

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf (definizione di p. 2, applicazioni di p. 3, tabella degli algoritmi)_
_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf e 07-Quicksort.pdf_
_Aggiornato: 2026-10-10 — link ripuntati alla versione aggiornata delle slide 06-Merge Sort (1).pdf_
_Aggiornato: 2026-10-14 — link ripuntati alla versione aggiornata delle slide 07-Quicksort 1.pdf_

<!-- nav:inizio -->
---
**Lezione 01 · pagina 3 di 18** · ← [[algoritmo-e-problema|Algoritmo, problema computazionale, istanza, correttezza, struttura dati]] · [[lezioni|Indice]] · [[efficienza-degli-algoritmi|Efficienza degli algoritmi («Algorithms as a technology»)]] →
<!-- nav:fine -->
