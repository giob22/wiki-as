---
tipo: entità
categoria: algoritmo
paradigma: "scelta greedy del vertice più vicino non ancora noto"
fonti_pdf: ["13 - Algoritmi di visita di un grafo.pdf#page=44", "13 - Algoritmi di visita di un grafo.pdf#page=46", "13 - Algoritmi di visita di un grafo.pdf#page=48", "13 - Algoritmi di visita di un grafo.pdf#page=50", "13 - Algoritmi di visita di un grafo.pdf#page=53"]
---

# Algoritmo di Dijkstra (percorsi minimi)

> 📚 Le pp. 44–53 della lezione sono slide in inglese di S. Skiena («Lecture 14: Shortest Paths»), inserite dal docente nella sezione «Percorsi minimi».

## Problema risolto · [[13 - Algoritmi di visita di un grafo.pdf#page=44|p. 44]]–[[13 - Algoritmi di visita di un grafo.pdf#page=47|47]]

- **Input:** un grafo **pesato** $G = (V, E)$ con pesi $w(u, v) > 0$ sugli archi, una sorgente $s$ (e, nella versione delle slide, una destinazione $t$).
- **Output:** la distanza minima $dist[v]$ da $s$ a ogni vertice $v$ (somma dei pesi lungo un percorso di peso minimo) e i percorsi.

Il problema del cammino minimo fra due nodi ha molte applicazioni (p. 45): **problemi di trasporto** (il modo più economico di viaggiare tra due luoghi), **pianificazione del movimento** (il modo più naturale in cui un personaggio dei cartoni si muove in un ambiente simulato), **problemi di comunicazione** (quanto tempo impiega un messaggio fra due posti; quali due posti sono i più lontani, cioè qual è il **diametro** della rete).

![[13-visite-grafi-p46-percorsi-minimi-non-pesati.png]]

**Grafi non pesati** (p. 46): lo shortest path usa il numero minimo di archi e si trova in $O(n + m)$ con la [[visita-in-ampiezza|ricerca in ampiezza]]. In un grafo **pesato** il peso di un percorso è la somma dei pesi dei suoi archi: la BFS **non funziona**, perché visitare più archi può costare meno di visitarne meno (esempio $1+1+1+1+1+1+1 < 10$). Inoltre ci può essere un numero **esponenziale** di percorsi minimi tra due nodi, quindi non si possono riportare *tutti* efficientemente.

**Pesi negativi** (p. 47): i cicli di costo negativo rendono il problema privo di senso, perché si può ripercorrere il ciclo per ridurre il costo del percorso. Perciò si assume che **tutti i pesi siano positivi**; altri algoritmi trattano correttamente i pesi negativi.

![[13-visite-grafi-p47-pesi-negativi.png]]

## Idea · [[13 - Algoritmi di visita di un grafo.pdf#page=48|p. 48]], [[13 - Algoritmi di visita di un grafo.pdf#page=49|49]]

Il **principio** (p. 48): se $(s, \dots, x, \dots, t)$ è lo shortest path da $s$ a $t$, allora $(s, \dots, x)$ *farebbe meglio* a essere lo shortest path da $s$ a $x$ (ogni prefisso di un cammino minimo è un cammino minimo).

**Inizializzazione e aggiornamento** (p. 49): il cammino minimo da $s$ a $s$ è $d(s, s) = 0$. Se tutti i pesi sono positivi, l'arco **più piccolo** incidente su $s$, diciamo $(s, x)$, definisce $d(s, x)$. Non appena si stabilisce lo shortest path da $s$ a un nuovo nodo $x$, si percorrono tutti i suoi archi incidenti per vedere se c'è un modo migliore di arrivare dagli altri nodi passando per $x$.

![[13-visite-grafi-p48-dijkstra-principio.png]]

## Pseudocodice · [[13 - Algoritmi di visita di un grafo.pdf#page=50|p. 50]]

(In inglese nella slide, con $n$ = numero di vertici.)

```
Dijkstra (G,s,t)
1  known = {s}
2  for i = 1 to n, dist[i] = ∞
3  for each edge (s,v), dist[v] = d(s,v)
4  last = s
5  while (last ≠ t)
6      select v such that dist(v) = min_unknown dist(i)
7      for each (v,x), dist[x] = min(dist[x], dist[v] + w(v,x))
8      last = v
9      known = known ∪ {v}
```

I numeri di riga e il nome `Dijkstra (G,s,t)` sono miei. Nell'animazione la selezione e l'aggiornamento vengono eseguiti fino a rendere **noti tutti i vertici** (ciclo fino a $known = V$), invece di fermarsi a $t$, per mostrare tutte le distanze.

![[13-visite-grafi-p50-dijkstra-pseudocodice.png]]

## Esempio di esecuzione · [[13 - Algoritmi di visita di un grafo.pdf#page=51|p. 51]], [[13 - Algoritmi di visita di un grafo.pdf#page=52|52]]

![[animazione-dijkstra.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo sul grafo di p. 52 (non orientato, sorgente $A$): $B$–$C$ 7, $B$–$D$ 9, $A$–$B$ 5, $A$–$D$ 7, $A$–$F$ 12, $C$–$D$ 4, $C$–$E$ 2, $C$–$G$ 5, $D$–$E$ 3, $D$–$F$ 4, $E$–$F$ 7, $E$–$G$ 2. Le slide mostrano il grafo $G$ con il suo albero dei cammini minimi «Dijkstra(G,A)» (p. 51) e il primo fotogramma di un'animazione (p. 52: tutti i vertici $\infty$, coda di priorità $Q$ ordinata per distanza, «grafo non orientato, pesi non negativi, sorgente $A$»).

![[13-visite-grafi-p51-dijkstra-esempio.png]]
![[13-visite-grafi-p52-dijkstra-grafo.png]]

Traccia (verificata con [[visite_di_grafi.py]]; i legami tra vertici a pari distanza, qui $C$ e $F$ con 11, sono risolti in ordine alfabetico):

| Passo | $v$ scelto | $dist[v]$ | Aggiornamenti dei vicini | $known$ dopo |
|---|---|---|---|---|
| init | $A$ | 0 | $dist[B] = 5$, $dist[D] = 7$, $dist[F] = 12$ | $\{A\}$ |
| 1 | $B$ | 5 | $dist[C] = 12$ (5+7); $D$: $5+9 = 14 > 7$, resta 7 | $\{A, B\}$ |
| 2 | $D$ | 7 | $C$: $7+4 = 11 < 12 \to 11$; $E$: $7+3 = 10$; $F$: $7+4 = 11 < 12 \to 11$ | $\{A, B, D\}$ |
| 3 | $E$ | 10 | $C$: $10+2 = 12 > 11$; $F$: $10+7 = 17$; $G$: $10+2 = 12$ | $+ E$ |
| 4 | $C$ | 11 | $G$: $11+5 = 16 > 12$ | $+ C$ |
| 5 | $F$ | 11 | nessuno | $+ F$ |
| 6 | $G$ | 12 | nessuno | tutti |

Risultato: $dist = (A: 0, B: 5, D: 7, E: 10, C: 11, F: 11, G: 12)$; albero dei cammini minimi: $A$–$B$, $A$–$D$, $D$–$E$, $D$–$C$, $D$–$F$, $E$–$G$ (6 archi, uno per vertice diverso da $A$; le etichette 1–6 sugli archi dell'albero «Dijkstra(G,A)» di p. 51 non sono pesi di $G$ e sembrano l'ordine di inserimento nell'albero, interpretazione mia 🧩).

## Correttezza · [[13 - Algoritmi di visita di un grafo.pdf#page=48|p. 48]]

La slide dà solo il principio (sottostruttura ottima). 🧩 Derivazione mia della correttezza, con pesi $\ge 0$.

> **Invariante:** quando un vertice $v$ viene scelto (riga 6), $dist[v] = \delta(s, v)$, la distanza minima vera.
> - *Per assurdo*, sia $v$ il primo vertice scelto con $dist[v] > \delta(s, v)$. Prendi uno shortest path da $s$ a $v$: parte da $s$ (noto) e arriva a $v$ (non noto), quindi ha un primo arco $(x, y)$ con $x$ noto e $y$ non noto.
> - $x$ è noto ed è stato scelto prima di $v$, quindi $dist[x] = \delta(s, x)$ (minimalità di $v$). Quando $x$ è stato scelto la riga 7 ha aggiornato $dist[y] \le dist[x] + w(x, y) = \delta(s, y)$, e $dist[y] \ge \delta(s, y)$ sempre: dunque $dist[y] = \delta(s, y)$ (principio di p. 48: il prefisso è minimo).
> - Con pesi non negativi $\delta(s, y) \le \delta(s, v)$ (il resto del percorso da $y$ a $v$ costa $\ge 0$). Per la scelta di $v$, $dist[v] \le dist[y]$. Quindi $dist[v] \le dist[y] = \delta(s, y) \le \delta(s, v) \le dist[v]$: tutto uguale, contraddizione.
> - **Se un peso è negativo** l'argomento cade (il resto del percorso potrebbe costare meno di 0): per questo le slide assumono pesi positivi (p. 47).

**Verifica** ([[visite_di_grafi.py]]): le distanze sul grafo di p. 52 coincidono con quelle calcolate indipendentemente con rilassamenti ripetuti (Bellman-Ford semplice, solo per controllo).

## Complessità · [[13 - Algoritmi di visita di un grafo.pdf#page=53|p. 53]]

### Derivazione — $T = O(n^2)$ · [[13 - Algoritmi di visita di un grafo.pdf#page=53|p. 53]]
**Fonte:** «Finding the minimum weight fringe-edge takes $O(n)$ time — just bump through fringe list. After adding new vertex $v$ to the tree, running through its adjacency list to update the cost of adding fringe vertices if we found a cheaper way through $v$ can be done in $O(n)$ time. The total time is $n \times n = O(n^2)$».

$$
T(n) = \underbrace{n}_{\text{vertici scelti}} \cdot \left( \underbrace{O(n)}_{\text{selezione del minimo}} + \underbrace{O(n)}_{\text{aggiornamento dei vicini}} \right) = O(n^2)
$$

> 🧩 Con liste di adiacenza l'aggiornamento totale è $\sum_v \lvert Adj[v] \rvert = 2m$ (non $n \cdot n$): il costo è $O(n^2 + m) = O(n^2)$, lo stesso limite perché $m \le n^2$. Il termine dominante è la selezione del minimo con una scansione lineare.

![[13-visite-grafi-p53-dijkstra-analisi.png]]

La slide chiude con una domanda aperta: «Possiamo fare di meglio? Possiamo sfruttare la «località temporale» dei nodi visitati?» (nessuna risposta nelle slide).

**Sanity check** ([[visite_di_grafi.py]]): con $n = 7$ vertici, al più $n^2 = 49$ operazioni elementari di selezione e aggiornamento.
**Ipotesi:** modello RAM; selezione per scansione lineare; pesi positivi; il costo $O(n^2)$ vale per ogni grafo con $n$ vertici.

## Proprietà

- **Greedy:** a ogni passo sceglie il vertice non noto più vicino (il «fringe» con distanza minima) e non lo rivede più.
- Richiede pesi **non negativi** (le slide dicono positivi).
- È una generalizzazione della [[visita-in-ampiezza|BFS]] (pesi tutti uguali a 1 dà le stesse distanze): la BFS esplora per numero di archi, Dijkstra per distanza pesata.

## Connessioni

- [[visita-in-ampiezza]] — percorsi minimi nei grafi non pesati
- [[visita-di-un-grafo]] — il contesto (Dijkstra è citato a p. 9 come algoritmo basato sulla BFS)
- [[coda-di-priorita]] — la coda con cui scegliere il minimo in modo efficiente (la slide di p. 52 mostra una «coda di priorità $Q$» ordinata per distanza)
- [[matrice-di-adiacenza]], [[liste-di-adiacenza]] — le rappresentazioni del grafo

## Fonti · [[13 - Algoritmi di visita di un grafo.pdf#page=44|p. 44]]–[[13 - Algoritmi di visita di un grafo.pdf#page=53|53]]

- [[lezione-13-algoritmi-di-visita-di-un-grafo]]

_Aggiornato: 2026-11-26 — ingest 13 - Algoritmi di visita di un grafo.pdf_

<!-- nav:inizio -->
---
**Lezione 13 · pagina 7 di 7** · ← [[ordinamento-topologico|Ordinamento topologico (Topological-Sort)]] · [[lezioni|Indice]] · [[lezione-14-backpropagation|Lezione 14: introduzione e riepilogo]] →
<!-- nav:fine -->
