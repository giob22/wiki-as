---
tipo: entità
categoria: algoritmo
paradigma: "[[metodi-euristici]] (greedy)"
fonti_pdf: ["01-Introduzione.pdf#page=26", "01-Introduzione.pdf#page=27", "01-Introduzione.pdf#page=28"]
---

# ClosestPair (Soluzione 2 del Robot Tour)

## Problema risolto

[[robot-tour-optimization]]. È un'euristica: **non** sempre trova il giro minimo.

## Idea

Invece di costruire il giro da un punto, si costruiscono **catene di vertici**: all'inizio ogni punto è una catena da solo. A ogni passo si collegano con un arco i due **estremi più vicini** che appartengono a **catene distinte**; dopo $n-1$ passi resta una sola catena e si chiude il ciclo unendo i suoi due estremi ([[01-Introduzione.pdf#page=26]]). Unire solo estremi di catene distinte evita cicli prematuri e vertici di grado maggiore di 2.

## Pseudocodice

> 📄 Fonte: [[01-Introduzione.pdf#page=26]] (riportato fedelmente)

```
ClosestPair(P)
1  Let n be the number of points in set P.
2  For i = 1 to n − 1 do
3      d = ∞
4      For each pair of endpoints (s,t) from distinct vertex chains
5          if dist(s,t) ≤ d then sm = s, tm = t, and d = dist(s,t)
6      Connect (sm, tm) by an edge
7  Connect the two endpoints by an edge
```

## Esempio di esecuzione

![[animazione-closest-pair.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo, sui sei punti di p. 28 (coordinate lette dal grafico): gli archi vengono aggiunti tra le catene nell'ordine AD, BE, CF, AB, EF, poi la chiusura diagonale DC; nell'ultimo fotogramma il giro ottimo tratteggiato in verde (7.29 contro 6.24). Ogni fotogramma riporta in basso il numero del passo e cosa succede.


Commento della fonte: «Più complessa, ma "sembra" risolvere il problema» ([[01-Introduzione.pdf#page=27]]). Sui punti della retta di [[nearest-neighbor]] funziona: trova il giro di lunghezza 64, cioè l'ottimo (🧩 verificato con lo script [[controesempi_euristiche.py]]).

**Controesempio** ([[01-Introduzione.pdf#page=28]]): sei punti su due file, A, B, C in alto e D, E, F in basso.

![[01-introduzione-p28-closest-pair-controesempio.png]]
*Due file di tre punti: la distanza verticale tra le file è minore della distanza orizzontale tra punti consecutivi. ([[01-Introduzione.pdf#page=28]])*

> 🧩 Derivazione mia. Coordinate lette dal grafico (approssimate): $A=(0,\,0.88)$, $B=(1.12,\,0.88)$, $C=(2.24,\,0.88)$, $D=(0,0)$, $E=(1.12,0)$, $F=(2.24,0)$. Distanza verticale $v = 0.88$, orizzontale $h = 1.12$, quindi $v < h$.

| Passo | Coppie di estremi candidate più vicine | Arco scelto | Catene dopo il passo |
|-------|----------------------------------------|-------------|----------------------|
| 1 | AD, BE, CF ($v = 0.88$) | AD | {A–D}, {B}, {C}, {E}, {F} |
| 2 | BE, CF (0.88) | BE | {A–D}, {B–E}, {C}, {F} |
| 3 | CF (0.88) | CF | {A–D}, {B–E}, {C–F} |
| 4 | AB, DE, BC, EF ($h = 1.12$) | AB | {D–A–B–E}, {C–F} |
| 5 | EF (1.12) | EF | {D–A–B–E–F–C} |
| chiusura | estremi D e C | DC | ciclo |

$$
\begin{aligned}
L_{CP} &= 3v + 2h + \sqrt{(2h)^2 + v^2}          && \text{AD, BE, CF; AB, EF; diagonale DC} \\
       &= 3(0.88) + 2(1.12) + \sqrt{2.24^2 + 0.88^2} \\
       &= 2.64 + 2.24 + 2.407 = 7.29 \\
L_{opt} &= 4h + 2v = 4.48 + 1.76 = 6.24          && \text{giro perimetrale A B C F E D A}
\end{aligned}
$$

**Sanity check:** verificato con [[controesempi_euristiche.py]] (7.287 contro 6.240); provando tutti i 720 ordini di input (quindi tutte le regole di scelta a parità) la lunghezza è sempre 7.287. Qualunque sia la scelta tra le coppie a parità, l'algoritmo prima unisce tutte le coppie verticali (le più corte) e alla fine è costretto a chiudere con una lunga diagonale, mentre il giro ottimo usa solo due archi verticali.
**Ipotesi:** coordinate lette a occhio dalla figura; il risultato qualitativo vale per ogni istanza di questa forma con $v < h$ abbastanza vicini.

## Correttezza

Non corretto (controesempio sopra). La lezione lo usa per la *Take-Home Lesson #1* ([[01-Introduzione.pdf#page=35]]) → [[metodi-euristici]].

## Complessità

> 🧩 Derivazione mia (non nella fonte): il ciclo esterno fa $n-1$ iterazioni; il ciclo interno esamina le coppie di estremi di catene distinte, al più $O(n^2)$ coppie (ogni catena ha ≤ 2 estremi) → implementazione diretta $O(n^3)$.

## Connessioni

- [[nearest-neighbor]], [[optimal-tsp]], [[controesempi-per-euristiche]]

## Fonti

- [[lezione-01-introduzione]]
- [[01-Introduzione.pdf#page=25]] («Soluzione?»), [[01-Introduzione.pdf#page=26]], [[01-Introduzione.pdf#page=27]], [[01-Introduzione.pdf#page=28]]

_Aggiornato: 2026-09-26 — ingest 01-Introduzione.pdf_
_Aggiornato: 2026-10-01 — aggiunta l'animazione dell'algoritmo_
