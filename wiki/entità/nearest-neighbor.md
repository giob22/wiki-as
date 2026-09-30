---
tipo: entità
categoria: algoritmo
paradigma: "[[metodi-euristici]] (greedy)"
fonti_pdf: ["01-Introduzione.pdf#page=18", "01-Introduzione.pdf#page=24"]
---

# NearestNeighbor (Soluzione 1 del Robot Tour)

## Problema risolto

[[robot-tour-optimization]]: dato un insieme di punti nel piano, trovare il ciclo più corto che li visita tutti. **Non** lo risolve correttamente: è un'euristica.

## Idea

Parti da un punto e vai sempre al **punto non ancora visitato più vicino**; alla fine torna al punto di partenza ([[01-Introduzione.pdf#page=18]]).

## Pseudocodice

> 📄 Fonte: [[01-Introduzione.pdf#page=18]] (riportato fedelmente, notazione della slide)

```
NearestNeighbor(P)
1  Pick and visit an initial point p0 from P
2  p = p0
3  i = 0
4  While there are still unvisited points
5      i = i + 1
6      Select pi to be the closest unvisited point to p(i-1)
7      Visit pi
8  Return to p0 from p(n-1)
```

> 🧩 Traduzione mia nelle [[pseudocodice|convenzioni del corso]] (indici da 1, `←`, `▷`):

```
NEAREST-NEIGHBOR(P)            ▷ P[1..n] punti
1  n ← length[P]
2  tour[1] ← P[1]              ▷ punto iniziale
3  visitato[1] ← true
4  for i ← 2 to n
5      tour[i] ← punto non visitato più vicino a tour[i-1]
6      visitato[tour[i]] ← true
7  return tour                 ▷ il ciclo si chiude da tour[n] a tour[1]
```

## Esempio di esecuzione

**Caso buono** — punti su una circonferenza ([[01-Introduzione.pdf#page=16]], [[01-Introduzione.pdf#page=17]]): il giro 0→1→2→…→8→0 è quello ottimo.

**Punti casuali** ([[01-Introduzione.pdf#page=20]], [[01-Introduzione.pdf#page=21]]): il giro prodotto ha incroci, segno che non è minimo.

**Casi limite**: la slide li introduce in [[01-Introduzione.pdf#page=19]] (solo il titolo), mostra i punti casuali in [[01-Introduzione.pdf#page=20]]–[[01-Introduzione.pdf#page=21]] e i punti sulla retta in [[01-Introduzione.pdf#page=22]]–[[01-Introduzione.pdf#page=23]].

**Controesempio** ([[01-Introduzione.pdf#page=22]]–[[01-Introduzione.pdf#page=24]]): punti sulla retta con coordinate $-21, -5, -1, 0, 1, 3, 11$, partenza da $0$.

![[01-introduzione-p24-nearest-neighbor-controesempio.png]]
*Il giro di nearest-neighbor salta avanti e indietro lungo la retta. ([[01-Introduzione.pdf#page=24]])*

> 🧩 Derivazione mia (traccia del giro della figura; ogni riga = un'iterazione della riga 6):

| Passo | Punto corrente | Candidati più vicini (distanza) | Scelto |
|-------|----------------|-------------------------------|--------|
| 1 | 0 | 1 e −1 (1) | 1 |
| 2 | 1 | −1 e 3 (2) | −1 |
| 3 | −1 | 3 e −5 (4) | 3 |
| 4 | 3 | −5 e 11 (8) | −5 |
| 5 | −5 | 11 e −21 (16) | 11 |
| 6 | 11 | −21 (32) | −21 |
| ritorno | −21 | 0 (21) | 0 |

$$
\begin{aligned}
L_{NN} &= 1 + 2 + 4 + 8 + 16 + 32 + 21 && \text{somma delle distanze della traccia} \\
       &= 84 \\
L_{opt} &= 2\,(11 - (-21)) = 64       && \text{vai all'estremo destro e torna a quello sinistro}
\end{aligned}
$$

**Sanity check:** verificato con [[controesempi_euristiche.py]] (NN = 84, ottimo esaustivo = 64).
**Ipotesi:** a ogni passo ci sono **due** candidati equidistanti; la figura li sceglie nel modo peggiore (zig-zag). È il tip «go for a tie» di [[ricerca-di-controesempi]]. La struttura dell'istanza è quella del tip «seek extremes»: le distanze dal punto corrente raddoppiano a ogni passo (1, 2, 4, 8, 16, 32), alternativamente a destra e a sinistra, e l'algoritmo, che guarda solo al passo successivo, non può «pianificare» di esaurire prima un lato.

**Commento della fonte:** «Semplice ed efficiente ma … **completamente sbagliata!**» ([[01-Introduzione.pdf#page=24]]).

## Correttezza

Non è corretto: il controesempio sopra è un'istanza su cui termina con un giro non minimo ([[algoritmo-e-problema]]).

## Complessità

> 🧩 Derivazione mia (la slide dice solo «efficiente»): all'iterazione $i$ si scandiscono i $n - i$ punti non visitati per trovare il più vicino.

$$
T(n) = \sum_{i=1}^{n-1} c\,(n-i) = c\,\frac{(n-1)n}{2} = \Theta(n^2) \qquad \text{somma di Gauss su } n-1 \text{ termini}
$$

Ipotesi: calcolo della distanza in tempo costante ([[modello-ram]]), nessuna struttura dati per la ricerca del più vicino.

## Connessioni

- [[closest-pair]] — seconda euristica, anch'essa sbagliata
- [[optimal-tsp]] — soluzione corretta ma esponenziale
- [[metodi-euristici]], [[ricerca-di-controesempi]], [[controesempi-per-euristiche]]

## Fonti

- [[lezione-01-introduzione]]
- [[01-Introduzione.pdf#page=16]]–[[01-Introduzione.pdf#page=24]]

_Aggiornato: 2026-09-26 — ingest 01-Introduzione.pdf_
