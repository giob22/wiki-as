---
tipo: entità
categoria: algoritmo
paradigma: "[[metodi-euristici]] (greedy)"
fonti_pdf: ["01-Introduzione.pdf#page=38", "01-Introduzione.pdf#page=45", "01-Introduzione.pdf#page=46"]
---

# EarliestJobFirst (Soluzione 1 del Movie Scheduling)

## Problema risolto

[[movie-scheduling]] — **non** correttamente.

## Idea e pseudocodice

> 📄 Fonte: [[01-Introduzione.pdf#page=38]]

```
EarliestJobFirst(I)
1  Accept the earliest starting job j from S which does not overlap any
   previously accepted job, and repeat until no more such jobs remain.
```

(la slide scrive «earlest», refuso per *earliest*)

## Esempio di esecuzione

![[animazione-earliest-job-first.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo, sui 9 film di p. 37 (intervalli misurati sulla figura della slide): a ogni passo il job che inizia prima, i job esclusi perché si sovrappongono (✘) e gli accettati (cerchio blu), con lo stesso esito delle slide (pp. 39–45). Ogni fotogramma riporta in basso il numero del passo e cosa succede.


Traccia sull'istanza di [[01-Introduzione.pdf#page=37]], una slide per passo ([[01-Introduzione.pdf#page=39]]–[[01-Introduzione.pdf#page=45]]); ✔ = accettato, ✘ = escluso perché si sovrappone a un accettato:

| Pagina | Evento |
|--------|--------|
| [[01-Introduzione.pdf#page=39\|p. 39]] | ✔ The President's Algorist (inizia per primo) |
| [[01-Introduzione.pdf#page=40\|p. 40]] | ✘ Tarjan of the Jungle, ✘ Halting State, ✘ "Discrete" Mathematics |
| [[01-Introduzione.pdf#page=41\|p. 41]] | ✔ Steiner's Tree |
| [[01-Introduzione.pdf#page=42\|p. 42]] | ✘ The Four Volume Problem |
| [[01-Introduzione.pdf#page=43\|p. 43]] | ✔ Programming Challenges |
| [[01-Introduzione.pdf#page=44\|p. 44]] | ✘ Process Terminated |
| [[01-Introduzione.pdf#page=45\|p. 45]] | ✔ Calculated Bets |

Risultato: **4** film.

![[01-introduzione-p45-earliest-job-first-esito.png]]
*Esito finale di EarliestJobFirst: cerchi blu = accettati, divieti rossi = esclusi. ([[01-Introduzione.pdf#page=45]])*

Commento della fonte: «This idea makes sense, at least until we realize that accepting the earliest job might block us from taking many other jobs if that first job is long» ([[01-Introduzione.pdf#page=46]]).

## Correttezza

> 🧩 Derivazione mia — controesempio minimo per la frase di p. 46 (verificato con [[controesempi_euristiche.py]]): $S = \{[0,10), [1,2), [3,4), [5,6)\}$. EarliestJobFirst accetta $[0,10)$, che si sovrappone a tutti gli altri → **1** film; l'ottimo è $\{[1,2), [3,4), [5,6)\}$ → **3** film. Quindi l'algoritmo è **incorretto**.

## Complessità

> 🧩 Derivazione mia: ordinando per inizio ($O(n \log n)$) e poi scorrendo una volta la lista, basta confrontare ogni job con l'ultimo accettato → $O(n\log n)$. È efficiente, ma sbagliato.

## Connessioni

- [[shortest-job-first]], [[optimal-scheduling]], [[controesempi-per-euristiche]]
- [[ricerca-di-controesempi]] — «hunt for the weakness»: il job lungo iniziale

## Fonti

- [[lezione-01-introduzione]]
- [[01-Introduzione.pdf#page=38]]–[[01-Introduzione.pdf#page=46]]

_Aggiornato: 2026-09-26 — ingest 01-Introduzione.pdf_
_Aggiornato: 2026-10-01 — aggiunta l'animazione dell'algoritmo_

<!-- nav:inizio -->
---
**Lezione 01 · pagina 13 di 18** · ← [[movie-scheduling|Movie Scheduling Problem (selezione di intervalli)]] · [[lezioni|Indice]] · [[shortest-job-first|ShortestJobFirst (Soluzione 2 del Movie Scheduling)]] →
<!-- nav:fine -->
