---
tipo: entità
categoria: algoritmo
paradigma: "[[metodi-euristici]] (greedy)"
fonti_pdf: ["01-Introduzione.pdf#page=47", "01-Introduzione.pdf#page=54", "01-Introduzione.pdf#page=55"]
---

# ShortestJobFirst (Soluzione 2 del Movie Scheduling)

## Problema risolto

[[movie-scheduling]] — **non** correttamente.

## Pseudocodice

> 📄 Fonte: [[01-Introduzione.pdf#page=47]]

```
ShortestJobFirst(I)
1  While (S ≠ ∅) do
2      Accept the shortest possible job j from S.
3      Delete j, and any interval which intersects j from S.
```

## Esempio di esecuzione

![[animazione-shortest-job-first.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo, sui 9 film di p. 37: a ogni passo il job più corto e gli intervalli eliminati perché lo intersecano, con lo stesso esito delle slide (pp. 48–54). Ogni fotogramma riporta in basso il numero del passo e cosa succede.


Traccia sull'istanza di [[01-Introduzione.pdf#page=37]] ([[01-Introduzione.pdf#page=48]]–[[01-Introduzione.pdf#page=54]]):

| Pagina | Evento |
|--------|--------|
| [[01-Introduzione.pdf#page=48\|p. 48]] | ✔ Steiner's Tree (il più corto) |
| [[01-Introduzione.pdf#page=49\|p. 49]] | ✘ Tarjan of the Jungle, ✘ The Four Volume Problem, ✘ Halting State |
| [[01-Introduzione.pdf#page=50\|p. 50]] | ✔ "Discrete" Mathematics |
| [[01-Introduzione.pdf#page=51\|p. 51]] | ✘ The President's Algorist |
| [[01-Introduzione.pdf#page=52\|p. 52]] | ✔ Calculated Bets |
| [[01-Introduzione.pdf#page=53\|p. 53]] | ✘ Process Terminated |
| [[01-Introduzione.pdf#page=54\|p. 54]] | ✔ Programming Challenges |

Risultato: **4** film. Su questa istanza entrambe le euristiche ([[earliest-job-first]] e questa) ne selezionano 4: il loro difetto emerge su istanze diverse.

![[01-introduzione-p54-shortest-job-first-esito.png]]
*Esito finale di ShortestJobFirst. ([[01-Introduzione.pdf#page=54]])*

Commento della fonte: «This idea makes sense at first. At least until we realize that accepting the shortest job might block us from taking two other jobs» ([[01-Introduzione.pdf#page=55]]).

## Correttezza

> 🧩 Derivazione mia — controesempio minimo per la frase di p. 55 (verificato con [[controesempi_euristiche.py]]): $S = \{[0,5), [4,7), [6,11)\}$. Il più corto è $[4,7)$ (durata 3), che interseca gli altri due → **1** film; l'ottimo è $\{[0,5), [6,11)\}$ → **2** film. Tre intervalli bastano: è il tip «think small» di [[ricerca-di-controesempi]].

## Complessità

> 🧩 Derivazione mia: al più $n$ iterazioni, ognuna cerca il minimo ed elimina le intersezioni in $O(n)$ → $O(n^2)$ nella forma diretta.

## Connessioni

- [[earliest-job-first]], [[optimal-scheduling]], [[controesempi-per-euristiche]]

## Fonti

- [[lezione-01-introduzione]]
- [[01-Introduzione.pdf#page=47]]–[[01-Introduzione.pdf#page=55]]

_Aggiornato: 2026-09-26 — ingest 01-Introduzione.pdf_
_Aggiornato: 2026-10-01 — aggiunta l'animazione dell'algoritmo_

<!-- nav:inizio -->
---
**Lezione 01 · pagina 14 di 18** · ← [[earliest-job-first|EarliestJobFirst (Soluzione 1 del Movie Scheduling)]] · [[lezioni|Indice]] · [[exhaustive-scheduling|ExhaustiveScheduling (Soluzione 3 del Movie Scheduling)]] →
<!-- nav:fine -->
