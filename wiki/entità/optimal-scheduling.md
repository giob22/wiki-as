---
tipo: entità
categoria: algoritmo
paradigma: "greedy (corretto)"
fonti_pdf: ["01-Introduzione.pdf#page=60"]
---

# OptimalScheduling (Soluzione 4 del Movie Scheduling)

## Problema risolto

[[movie-scheduling]] — in modo **corretto ed efficiente** ([[01-Introduzione.pdf#page=60]]).

## Pseudocodice

> 📄 Fonte: [[01-Introduzione.pdf#page=60]]

```
OptimalScheduling(I)
1  While (S ≠ ∅) do
2      Accept the job j from S with the earliest completion date.
3      Delete j, and any interval which intersects j from S.
```

![[01-introduzione-p60-optimal-scheduling.png]]
*Soluzione 4 e Take-Home Lesson #2. ([[01-Introduzione.pdf#page=60]])*

## Idea

È la stessa struttura di [[shortest-job-first]], ma il criterio è la **data di fine** più vicina, non la durata né l'inizio.

## Correttezza

La slide afferma che la soluzione è corretta ed efficiente ma **non** riporta la dimostrazione; subito dopo ricorda che «algorithm correctness is a property that must be carefully demonstrated».

> 🧩 Derivazione mia (argomento di scambio, spiega il perché dell'affermazione della slide):
> 1. Sia $j_1$ il job che termina per primo in $S$ e sia $O$ una soluzione ottima qualunque, con primo job (in ordine di fine) $o_1$.
> 2. Poiché $f_{j_1} \le f_{o_1}$, sostituendo $o_1$ con $j_1$ in $O$ non si crea nessuna sovrapposizione: tutti gli altri job di $O$ iniziano dopo $f_{o_1} \ge f_{j_1}$. Si ottiene un'altra soluzione ottima $O'$ che contiene $j_1$.
> 3. Tolti $j_1$ e gli intervalli che lo intersecano, il problema residuo ha la stessa forma: per induzione sul numero di intervalli, le scelte successive sono ancora estendibili a un ottimo.
> 4. Termina perché a ogni iterazione $S$ perde almeno $j$.
>
> Controllo empirico: [[controesempi_euristiche.py]] confronta OptimalScheduling con la ricerca esaustiva su tutte le istanze fino a 4 intervalli a estremi interi in $[0,5]$: **nessun** fallimento (think exhaustively, [[03-Analisi di algoritmi.pdf#page=14]]).

## Esempio di esecuzione

![[animazione-optimal-scheduling.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo, la regola di p. 60 applicata ai 9 film di p. 37 (le slide non mostrano questa esecuzione): a ogni passo il job che finisce prima; il risultato, 4 film, coincide con l'ottimo trovato per ricerca esaustiva in [[controesempi_euristiche.py]]. Ogni fotogramma riporta in basso il numero del passo e cosa succede.


> 🧩 Sui controesempi delle euristiche: $\{[0,10), [1,2), [3,4), [5,6)\}$ → sceglie $[1,2), [3,4), [5,6)$ (3, ottimo); $\{[0,5), [4,7), [6,11)\}$ → sceglie $[0,5), [6,11)$ (2, ottimo). Vedi [[controesempi-per-euristiche]].

## Complessità

> 🧩 Derivazione mia: ordinare per data di fine costa $O(n\log n)$; poi una scansione lineare accetta un job se inizia dopo la fine dell'ultimo accettato → $T(n) = O(n \log n)$. La versione letterale dello pseudocodice (minimo ed eliminazione a ogni iterazione) costa $O(n^2)$: in entrambi i casi polinomiale, contro $O(n^2 2^n)$ di [[exhaustive-scheduling]].

## Connessioni

- [[earliest-job-first]], [[shortest-job-first]] — stesse idee greedy, criterio sbagliato
- [[correttezza-per-induzione]] — la dimostrazione è un'induzione sul numero di intervalli
- [[ricerca-di-controesempi]] — Take-Home Lesson #2

## Fonti

- [[lezione-01-introduzione]]
- [[01-Introduzione.pdf#page=60]]

_Aggiornato: 2026-09-26 — ingest 01-Introduzione.pdf_
_Aggiornato: 2026-10-01 — aggiunta l'animazione dell'algoritmo_
