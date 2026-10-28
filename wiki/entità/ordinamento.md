---
tipo: entità
categoria: problema
fonti_pdf: ["01-Introduzione.pdf#page=7", "01-Introduzione.pdf#page=11", "05-Insertion sort.pdf#page=2", "05-Insertion sort.pdf#page=3"]
---

# Problema dell'ordinamento (Sorting)

## Definizione formale

> 📄 Fonte: [[01-Introduzione.pdf#page=7]]

- **Problem:** Sorting
- **Input:** una sequenza di $n$ chiavi $a_1, \dots, a_n$
- **Output:** la permutazione (riordinamento) della sequenza d'ingresso $a'_1, \dots, a'_n$ tale che $a'_1 \le a'_2 \le \dots \le a'_n$

È l'esempio con cui la lezione 01 introduce le nozioni di problema computazionale e di [[algoritmo-e-problema|istanza]].

> 📄 Fonte: [[05-Insertion sort.pdf#page=2]] — la lezione 05 riprende la stessa definizione in italiano

**Problema:** data una sequenza di $n$ valori di ingresso $(a_1, a_2, \dots, a_n)$, determinare una permutazione $(a'_1, a'_2, \dots, a'_n)$ della sequenza di ingresso tale che $a'_1 \le a'_2 \le \dots \le a'_n$.

## Applicazioni

> 📄 Fonte: [[05-Insertion sort.pdf#page=3]]

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

## Algoritmi che lo risolvono

| Algoritmo | Caso migliore | Caso peggiore | Spazio aggiuntivo | Pagina |
|-----------|---------------|---------------|-------------------|--------|
| [[insertion-sort]] | $\Theta(n)$ (già ordinato) | $\Theta(n^2)$ (ordine decrescente) | $\Theta(1)$, sul posto | [[05-Insertion sort.pdf#page=20]], [[05-Insertion sort.pdf#page=22]] |
| [[selection-sort]] | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(1)$ (🧩) | [[05-Insertion sort.pdf#page=28]] |
| [[merge-sort]] | $\Theta(n\lg n)$ | $\Theta(n\lg n)$ | $\Theta(n)$, **non** sul posto | [[06-Merge Sort (1).pdf#page=7]], [[06-Merge Sort (1).pdf#page=25]] |
| [[quicksort]] | $\Theta(n\lg n)$ (partizioni bilanciate) | $\Theta(n^2)$ (vettore ordinato) | sul posto (pila da $\Theta(\lg n)$ a $\Theta(n)$, 🧩) | [[07-Quicksort 1.pdf#page=2]], [[07-Quicksort 1.pdf#page=14]], [[07-Quicksort 1.pdf#page=15]] |
| [[quicksort-randomizzato]] | — | $\Theta(n^2)$ (improbabile); **atteso** $O(n\log n)$ | sul posto | [[07-Quicksort 1.pdf#page=20]], [[07-Quicksort 1.pdf#page=23]] |

Confronto numerico su $n = 10^6$ a $10^9$ op/s: ≈ 16.7 minuti (insertion sort, $n^2$) contro ≈ 0.02 secondi (merge sort, $n \log n$) — derivazione in [[efficienza-degli-algoritmi]].

> 🧩 Osservazione mia sulla tabella: l'input già ordinato è il caso **migliore** di insertion sort e il caso **peggiore** di quicksort con pivot $A[r]$ ([[07-Quicksort 1.pdf#page=14]]); merge sort non distingue gli input. Merge sort e insertion sort sono stabili, quicksort no (dettagli nelle pagine degli algoritmi).

## Altre occorrenze

- Per gli algoritmi di ordinamento la **dimensione dell'input** è la lunghezza della sequenza da ordinare ([[03-Analisi di algoritmi.pdf#page=22]], [[02-Notazione asintotica.pdf#page=3]]) → [[tempo-di-esecuzione]].
- «"Sort" is not a single step operation» nel [[modello-ram]] ([[02-Notazione asintotica.pdf#page=5]]).
- Ordinamento è uno degli esempi classici di [[divide-et-impera]] ([[03-Analisi di algoritmi.pdf#page=4]]).
- Nello pseudocodice degli esercizi, `sort` può essere usata come funzione di libreria solo se esplicitamente consentito ([[a1-indicazioni_psuedocodice.pdf#page=4]]) → [[pseudocodice]].

## Fonti

- [[lezione-01-introduzione]], [[lezione-05-insertion-sort]], [[lezione-06-merge-sort]], [[lezione-07-quicksort]]
- [[01-Introduzione.pdf#page=7]], [[01-Introduzione.pdf#page=11]], [[05-Insertion sort.pdf#page=2]], [[05-Insertion sort.pdf#page=3]]

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf (definizione di p. 2, applicazioni di p. 3, tabella degli algoritmi)_
_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf e 07-Quicksort.pdf_
_Aggiornato: 2026-10-10 — link ripuntati alla versione aggiornata delle slide 06-Merge Sort (1).pdf_
_Aggiornato: 2026-10-14 — link ripuntati alla versione aggiornata delle slide 07-Quicksort 1.pdf_

<!-- nav:inizio -->
---
**Lezione 01 · pagina 3 di 18** · ← [[algoritmo-e-problema|Algoritmo, problema computazionale, istanza, correttezza, struttura dati]] · [[lezioni|Indice]] · [[efficienza-degli-algoritmi|Efficienza degli algoritmi («Algorithms as a technology»)]] →
<!-- nav:fine -->
