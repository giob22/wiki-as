---
tipo: esercizio
argomento: "incorrettezza di algoritmi greedy tramite controesempi"
difficoltà: media
---

# Trovare controesempi per euristiche (greedy)

## Metodo

1. Capire la **regola di scelta** dell'euristica (il «criterio greedy»).
2. Cercare la **debolezza**: in quale situazione la scelta locale migliore impedisce scelte future migliori? (hunt for the weakness)
3. Costruire l'istanza **più piccola** che la sfrutti (think small), provando anche **parità** (go for a tie) e **estremi** (seek extremes) ([[03-Analisi di algoritmi.pdf#page=14]]).
4. Calcolare l'uscita dell'euristica **e** l'ottimo (a mano o per enumerazione esaustiva) e mostrare che differiscono.
5. Se non si trova un controesempio, **non** concludere che l'algoritmo è corretto: serve una dimostrazione ([[03-Analisi di algoritmi.pdf#page=15]]).

## Strumenti usati

- [[ricerca-di-controesempi]], [[metodi-euristici]], [[ricerca-combinatoria]] (l'esaustivo come riferimento)
- Script: [[controesempi_euristiche.py]]

## Casi svolti

### Caso 1 — NearestNeighbor sulla retta
**Traccia:** [[01-Introduzione.pdf#page=22]]–[[01-Introduzione.pdf#page=24]]. Punti $-21, -5, -1, 0, 1, 3, 11$, partenza da 0.
**Svolgimento:** traccia completa in [[nearest-neighbor]]: giro $0 \to 1 \to -1 \to 3 \to -5 \to 11 \to -21 \to 0$.
$$ L_{NN} = 1 + 2 + 4 + 8 + 16 + 32 + 21 = 84, \qquad L_{opt} = 2\cdot(11 + 21) = 64 $$
**Risultato:** $84 > 64$ → NearestNeighbor è incorretto. Tip usati: tie ed extremes.

### Caso 2 — ClosestPair su due file di punti
**Traccia:** [[01-Introduzione.pdf#page=28]]. Punti A, B, C a quota $0.88$ e D, E, F a quota 0, ascisse $0, 1.12, 2.24$ (lette dal grafico).
**Svolgimento:** traccia completa in [[closest-pair]]: prima i tre archi verticali (0.88), poi due orizzontali (1.12), infine la chiusura diagonale $\sqrt{2.24^2 + 0.88^2} = 2.407$.
$$ L_{CP} = 3(0.88) + 2(1.12) + 2.407 = 7.29, \qquad L_{opt} = 4(1.12) + 2(0.88) = 6.24 $$
**Risultato:** $7.29 > 6.24$ per ogni regola di scelta a parità (verificato su tutti i 720 ordini di input).

### Caso 3 — EarliestJobFirst
**Traccia:** frase di [[01-Introduzione.pdf#page=46]] («accepting the earliest job might block us from taking many other jobs if that first job is long»).
> 🧩 Controesempio mio: $\{[0,10), [1,2), [3,4), [5,6)\}$ → EJF sceglie $[0,10)$ (1 film); ottimo $\{[1,2), [3,4), [5,6)\}$ (3 film).

### Caso 4 — ShortestJobFirst
**Traccia:** frase di [[01-Introduzione.pdf#page=55]] («accepting the shortest job might block us from taking two other jobs»).
> 🧩 Controesempio mio: $\{[0,5), [4,7), [6,11)\}$ → SJF sceglie $[4,7)$ (1 film); ottimo $\{[0,5), [6,11)\}$ (2 film).

### Caso 5 — nessun controesempio per OptimalScheduling
> 🧩 Ricerca esaustiva mia: su tutte le istanze fino a 4 intervalli con estremi interi in $[0, 5]$, [[optimal-scheduling]] dà sempre lo stesso numero di film dell'esaustivo. Questo **non** è una dimostrazione (Take-Home Lesson #2, [[01-Introduzione.pdf#page=60]]); la dimostrazione per scambio è in [[optimal-scheduling]].

## Trappole

- Un'euristica può dare il risultato giusto sull'istanza d'esempio: nell'istanza di [[01-Introduzione.pdf#page=37]] sia EJF sia SJF scelgono 4 film; il controesempio va costruito apposta.
- Nei casi a parità, dichiarare la regola di scelta o mostrare che il controesempio vale per tutte.
- Confrontare sempre con l'**ottimo**, non con un'altra euristica.

_Aggiornato: 2026-09-26 — ingest 01-Introduzione.pdf e 03-Analisi di algoritmi.pdf_
