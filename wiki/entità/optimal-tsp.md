---
tipo: entità
categoria: algoritmo
paradigma: "[[ricerca-combinatoria]] (esaustiva)"
fonti_pdf: ["01-Introduzione.pdf#page=29", "01-Introduzione.pdf#page=33", "01-Introduzione.pdf#page=34"]
---

# OptimalTSP (Soluzione 3 del Robot Tour)

## Problema risolto

[[robot-tour-optimization]] — in modo **corretto**.

## Idea

Provare **tutti** gli ordinamenti (permutazioni) dei punti e tenere quello di costo minimo ([[01-Introduzione.pdf#page=29]]).

## Pseudocodice

> 📄 Fonte: [[01-Introduzione.pdf#page=29]]

```
OptimalTSP(P)
1  d = ∞
2  For each of the n! permutations Pi of point set P
3      If (cost(Pi) ≤ d) then d = cost(Pi) and Pmin = Pi
4  Return Pmin
```

## Esempio di esecuzione

![[animazione-optimal-tsp.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo, istanza di esempio mia con 4 punti (le slide non ne danno una abbastanza piccola da enumerare): tutte le $4! = 24$ permutazioni una dopo l'altra, in blu la corrente e in verde la migliore trovata finora ($d$, $P_{min}$). Con il test `≤` della riga 3, i giri di costo uguale già trovati (stesso giro percorso da un altro punto o al contrario) sostituiscono $P_{min}$. Ogni fotogramma riporta in basso il numero del passo e cosa succede.

## Correttezza

«Corretto?» ([[01-Introduzione.pdf#page=30]]) → «Sì» ([[01-Introduzione.pdf#page=31]]). Motivazione della fonte (Skiena): poiché si considerano tutti i possibili ordinamenti, si è garantiti di trovare il giro più breve; l'algoritmo è corretto perché sceglie il migliore tra tutte le possibilità ([[01-Introduzione.pdf#page=34]]).

> 🧩 Derivazione mia (invariante del ciclo di riga 2): «all'inizio di ogni iterazione, $d$ è il costo minimo tra le permutazioni già esaminate e $P_{min}$ ne realizza il costo». Vale all'inizio (nessuna permutazione esaminata, $d = \infty$); si conserva perché la riga 3 aggiorna $d$ se la nuova permutazione non è peggiore; alla fine le permutazioni esaminate sono tutte, quindi $P_{min}$ è ottimo. Termina perché le permutazioni sono in numero finito ($n!$). → [[invariante-di-ciclo]]

## Complessità

«Efficiente?» ([[01-Introduzione.pdf#page=32]]) → «$20! = 2{,}432{,}902{,}008{,}176{,}640{,}000$, $1000 = \dots$» ([[01-Introduzione.pdf#page=33]]).

> 🧩 Derivazione mia:
$$
T(n) = \underbrace{n!}_{\text{permutazioni}} \cdot \underbrace{\Theta(n)}_{\text{cost}(P_i):\ n \text{ distanze}} = \Theta(n \cdot n!)
$$
- $n = 20$: $20! \approx 2.43\cdot10^{18}$ permutazioni; a $10^9$ permutazioni/s servono $\approx 2.43\cdot10^{9}$ s $\approx 77$ anni (coerente con la tabella di [[02-Notazione asintotica.pdf#page=36]], $n!$ con $n = 20$: 77.1 years).
- $n = 1000$ (il «1000 = …» della slide): $1000! \approx 10^{2567.6}$, un numero di 2568 cifre (calcolato con [[tempi_crescita.py]]).

«Even a powerful computer couldn't hope to enumerate all the 20! orderings of 20 points within a day» ([[01-Introduzione.pdf#page=34]]).

## Connessioni

- [[ricerca-combinatoria]] — corretto ma esponenziale
- [[exhaustive-scheduling]] — ricerca esaustiva analoga ma sui $2^n$ sottoinsiemi
- [[dominanza-asintotica]] — $n!$ in cima alla classifica di crescita

## Fonti

- [[lezione-01-introduzione]]
- [[01-Introduzione.pdf#page=29]]–[[01-Introduzione.pdf#page=34]]

_Aggiornato: 2026-09-26 — ingest 01-Introduzione.pdf_
_Aggiornato: 2026-10-01 — aggiunta l'animazione dell'algoritmo_
