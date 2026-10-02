---
tipo: entità
categoria: problema
fonti_pdf: ["06-Merge Sort.pdf#page=16"]
---

# Problema del massimo sottoarray

## Definizione formale

> 📄 Fonte: [[06-Merge Sort.pdf#page=16]]

La slide è un «Stop & Think» che contiene solo il titolo, «Problema del massimo sottoarray», e il rimando al **Capitolo 4.1 del libro di testo**. Non ci sono testo del problema, algoritmo o analisi.

> 📚 Fonte esterna: Cormen, Leiserson, Rivest, Stein, *Introduzione agli algoritmi e strutture dati*, 3ª ed., §4.1. Enunciato:
> - **Input:** un array $A[1..n]$ di numeri, anche negativi.
> - **Output:** indici $i \le j$ tali che la somma $A[i] + A[i+1] + \dots + A[j]$ sia **massima** tra tutti i sottoarray non vuoti e contigui.
>
> Se tutti i numeri fossero non negativi la risposta sarebbe l'intero array: il problema è interessante solo con valori negativi.

## Algoritmi che lo risolvono

TODO: da espandere se una lezione presenterà la soluzione. Le slide non la danno e il wiki non la inventa. Il libro (📚 §4.1) la tratta come esempio di [[divide-et-impera]], nella stessa lezione di [[merge-sort]].

## Connessioni

- [[divide-et-impera]] — il problema è posto nella lezione sul paradigma, tra merge sort e le ricorrenze
- [[progettazione-divide-et-impera]] — esercizi di progettazione della stessa lezione

## Fonti

- [[lezione-06-merge-sort]]
- [[06-Merge Sort.pdf#page=16]]

_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf_
