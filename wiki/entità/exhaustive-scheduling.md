---
tipo: entità
categoria: algoritmo
paradigma: "[[ricerca-combinatoria]] (esaustiva)"
fonti_pdf: ["01-Introduzione.pdf#page=56", "01-Introduzione.pdf#page=58", "01-Introduzione.pdf#page=59"]
---

# ExhaustiveScheduling (Soluzione 3 del Movie Scheduling)

## Problema risolto

[[movie-scheduling]] — correttamente, ma in tempo esponenziale.

## Pseudocodice · [[01-Introduzione.pdf#page=56|p. 56]], [[01-Introduzione.pdf#page=58|p. 58]]

```
ExhaustiveScheduling(S)
1  j = 0, Smax = ∅
2  For each of the 2^n subsets Si of intervals S
3      If (Si is mutually non-overlapping) and (size(Si) > j)
4          then j = size(Si) and Smax = Si.
5  Return Smax
```

La versione di p. 56 scrive «For each subsets Si of intervals S» con parametro `I`; la p. 58 («Soluzione 3 (e mezzo…)») precisa **«of the $2^n$»** sottoinsiemi, con la nota evidenziata: «Non ci interessa delle permutazioni!! (l'ordine non è importante)».

![[01-introduzione-p58-exhaustive-scheduling-2n.png]]
*La correzione «e mezzo»: si enumerano sottoinsiemi, non permutazioni.*

## Esempio di esecuzione

![[animazione-exhaustive-scheduling.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo, istanza di esempio mia con 4 intervalli ($2^9 = 512$ sottoinsiemi dei 9 film sarebbero troppi fotogrammi): tutti i $2^4 = 16$ sottoinsiemi, in verde quelli senza sovrapposizioni e in rosso gli altri, con $j$ e $S_{max}$ aggiornati come nello pseudocodice di p. 58. Ogni fotogramma riporta in basso il numero del passo e cosa succede.

## Correttezza

> 🧩 Derivazione mia: esamina **ogni** sottoinsieme e conserva il più grande tra quelli ammissibili (invariante: $S_{max}$ è il più grande sottoinsieme ammissibile tra quelli già esaminati e $j = |S_{max}|$). Terminati i $2^n$ sottoinsiemi, $S_{max}$ è ottimo. È corretto per costruzione, come [[optimal-tsp]].

## Complessità · 01-Introduzione.pdf [[01-Introduzione.pdf#page=57|p. 57]], [[01-Introduzione.pdf#page=59|p. 59]] · 02-Notazione asintotica.pdf [[02-Notazione asintotica.pdf#page=36|p. 36]]

Commento della fonte: «The slowness of this approach make it prohibitive like the exhaustive approach for the robot route»; poi «Well, $2^n$ is better than $n!$ of Problem 1 ($2^{20} \approx 1$M), … but $2^{100} \approx 1.26 \cdot 10^{30}$».

> 🧩 Derivazione mia: $2^n$ sottoinsiemi (ogni intervallo dentro o fuori); controllare che $S_i$ sia privo di sovrapposizioni costa $O(|S_i|^2) \subseteq O(n^2)$ confrontando le coppie → $T(n) = O(n^2\, 2^n)$.

**Numeri** (verificati con [[tempi_crescita.py]]): $2^{20} = 1\,048\,576$; $2^{100} = 1.2677\cdot10^{30}$ (la slide tronca a $1.26$). A $10^9$ sottoinsiemi al secondo, $2^{100}$ richiederebbe $\approx 4\cdot 10^{13}$ anni (riga $n = 100$, colonna $2^n$ di p. 36).

## Connessioni

- [[ricerca-combinatoria]], [[optimal-tsp]], [[optimal-scheduling]]
- [[dominanza-asintotica]] — $n! \gg 2^n$

## Fonti · [[01-Introduzione.pdf#page=56|p. 56]], [[01-Introduzione.pdf#page=59|p. 59]]

- [[lezione-01-introduzione]]

_Aggiornato: 2026-09-26 — ingest 01-Introduzione.pdf_
_Aggiornato: 2026-10-01 — aggiunta l'animazione dell'algoritmo_

<!-- nav:inizio -->
---
**Lezione 01 · pagina 15 di 18** · ← [[shortest-job-first|ShortestJobFirst (Soluzione 2 del Movie Scheduling)]] · [[lezioni|Indice]] · [[optimal-scheduling|OptimalScheduling (Soluzione 4 del Movie Scheduling)]] →
<!-- nav:fine -->
