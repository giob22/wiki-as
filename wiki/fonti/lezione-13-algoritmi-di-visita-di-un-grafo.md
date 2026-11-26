---
tipo: fonte
titolo: "Corso di Algoritmi e Strutture Dati — Algoritmi di visita di un grafo"
file_raw: "13 - Algoritmi di visita di un grafo.pdf"
pagine: "1-53"
data_ingest: 2026-11-26
formato: slide-pdf
argomenti: [rappresentazioni dei grafi, visita in ampiezza, visita in profondità, ordinamento topologico, classificazione degli archi, percorsi minimi, Dijkstra]
---

# Lezione 13 — Algoritmi di visita di un grafo (13 - Algoritmi di visita di un grafo.pdf)

## Sommario · [[13 - Algoritmi di visita di un grafo.pdf#page=1|p. 1]], [[13 - Algoritmi di visita di un grafo.pdf#page=2|2]]

Slide del Prof. Marrone, a.a. 26/27. La lezione richiama le due rappresentazioni dei grafi (liste e matrice di adiacenza, pp. 2–6) e introduce le **visite** (p. 7). La **visita in ampiezza** (BFS, pp. 8–23) usa colori e una coda; ne dimostra la correttezza (lemmi 1–4 e teorema sulle distanze minime), costruisce il breadth-first tree, ne analizza il costo con l'analisi aggregata ($O(V+E)$) e stampa lo shortest path con Print-Path. La **visita in profondità** (DFS, pp. 24–37) aggiunge i timestamp $d$ e $f$, ne dà il costo $O(V+E)$, la struttura a parentesi, il teorema di annidamento e quello del cammino bianco e la classificazione degli archi (tree, back, forward, cross). L'**ordinamento topologico** (pp. 38–43) usa i tempi di completamento della DFS su un DAG, con la dimostrazione (un grafo orientato è aciclico se e solo se la DFS non produce back edge). L'ultima sezione, **percorsi minimi** (pp. 44–53, slide di Skiena in inglese), presenta l'algoritmo di Dijkstra con il suo costo $O(n^2)$.

## Percorso della lezione

Pagine del wiki nell'ordine di prima comparsa nelle slide (è l'ordine delle pagine di questa lezione nel libro):
1. [[visita-di-un-grafo]] — p. 7: le due strategie e i colori dei nodi
2. [[visita-in-ampiezza]] — pp. 8–21: BFS, correttezza, costo
3. [[print-path]] — pp. 22–23: stampa di uno shortest path
4. [[visita-in-profondita]] — pp. 24–37: DFS, timestamp, teoremi, classificazione degli archi
5. [[ordinamento-topologico]] — pp. 38–43: Topological-Sort e le sue dimostrazioni
6. [[dijkstra]] — pp. 44–53: percorsi minimi e algoritmo di Dijkstra

Già lette, riprese in questa lezione: *liste-di-adiacenza* e *matrice-di-adiacenza* (pp. 2–6: nuove sezioni «Ripresa nella lezione 13»), *grafo*, *coda*, *lista-concatenata*, *coda-di-priorita*.

**Ordine consigliato.** Le slide sono lineari. Prima delle visite conviene rileggere le sezioni «Ripresa nella lezione 13» di *liste-di-adiacenza* e *matrice-di-adiacenza* (pp. 2–6); per Dijkstra serve aver capito la BFS.

## Punti chiave · [[13 - Algoritmi di visita di un grafo.pdf#page=2|p. 2]], [[13 - Algoritmi di visita di un grafo.pdf#page=7|7]], [[13 - Algoritmi di visita di un grafo.pdf#page=9|p. 9]]–[[13 - Algoritmi di visita di un grafo.pdf#page=14|14]], [[13 - Algoritmi di visita di un grafo.pdf#page=19|p. 19]], [[13 - Algoritmi di visita di un grafo.pdf#page=25|p. 25]], [[13 - Algoritmi di visita di un grafo.pdf#page=29|29]], [[13 - Algoritmi di visita di un grafo.pdf#page=31|31]], [[13 - Algoritmi di visita di un grafo.pdf#page=35|35]], [[13 - Algoritmi di visita di un grafo.pdf#page=40|p. 40]], [[13 - Algoritmi di visita di un grafo.pdf#page=50|p. 50]], [[13 - Algoritmi di visita di un grafo.pdf#page=53|53]]

1. Liste di adiacenza per grafi sparsi, matrice per grafi densi o per test rapidi su un arco; somma delle liste $\lvert E \rvert$ (orientato) o $2\lvert E \rvert$ (non orientato); matrice simmetrica nei grafi non orientati → [[liste-di-adiacenza]], [[matrice-di-adiacenza]].
2. Una visita esplora i vertici da una sorgente evitando ripetizioni; due strategie, BFS (per livelli) e DFS (in profondità) → [[visita-di-un-grafo]].
3. BFS: colori bianco/grigio/nero, predecessori $\pi$, distanze $d$; $d[v] = \delta(s, v)$; costo $O(V+E)$ con l'analisi aggregata → [[visita-in-ampiezza]].
4. Print-Path stampa uno shortest path in tempo lineare nel numero di vertici → [[print-path]].
5. DFS: timestamp $d[v] < f[v]$ in $[1, 2\lvert V \rvert]$, depth-first forest, costo $O(V+E)$, struttura a parentesi, teoremi di annidamento e del cammino bianco, archi tree/back/forward/cross → [[visita-in-profondita]].
6. Topological-Sort: DFS e lista con inserimento in testa, $\Theta(V+E)$; un grafo orientato è aciclico se e solo se la DFS non dà back edge → [[ordinamento-topologico]].
7. Dijkstra: pesi positivi, scelta del vertice non noto con $dist$ minima e aggiornamento dei vicini, $O(n^2)$ → [[dijkstra]].

## Refusi e note · [[13 - Algoritmi di visita di un grafo.pdf#page=14|p. 14]], [[13 - Algoritmi di visita di un grafo.pdf#page=19|19]], [[13 - Algoritmi di visita di un grafo.pdf#page=22|p. 22]], [[13 - Algoritmi di visita di un grafo.pdf#page=33|33]], [[13 - Algoritmi di visita di un grafo.pdf#page=43|43]]

- p. 14: il testo estratto dal PDF ha del testo spurio («perché non può enere r(v+e)») dopo «$O(V+E)$»: la figura mostra solo la frase «Il tempo di esecuzione di BFS è $O(V+E)$».
- p. 19: la dimostrazione del teorema di completezza si interrompe a metà; il completamento è 🧩 in [[visita-in-ampiezza]] (❓).
- pp. 22 e 23: stesso contenuto (Print-Path); le righe dello pseudocodice sono mescolate nel testo estratto.
- p. 33: «corollario 8» è un refuso per il corollario 1; p. 43: «lemma 11» è un refuso per il lemma 1.
- p. 29: la slide scrive $O(V+E)$ per DFS; con le somme dei due termini è $\Theta(V+E)$.
- pp. 8, 24, 27 e 44: pagine di intestazione di sezione; pp. 4, 6: richiami delle rappresentazioni già viste (lezione 08); p. 38 e p. 40 contengono note a mano (⚠️ lettura incerta in [[ordinamento-topologico]]).
- pp. 44–53: slide in inglese di S. Skiena; p. 52 contiene il primo fotogramma di un'animazione.
- Lo pseudocodice è in stile Cormen 2ª ed. (`do`, `then`) per BFS, DFS e Print-Path, diverso dalle [[pseudocodice|convenzioni del corso]].

## Concetti introdotti

[[visita-di-un-grafo]], [[visita-in-ampiezza]], [[print-path]], [[visita-in-profondita]], [[ordinamento-topologico]], [[dijkstra]].

## Domande aperte

- La dimostrazione del teorema di completezza della BFS (p. 19) è interrotta: TODO verificare con il docente la sua conclusione.
- Dijkstra: la slide chiede se si può fare meglio sfruttando la «località temporale» dei nodi visitati (p. 53), senza risposta: TODO alla lezione successiva (coda di priorità).
- La slide p. 51 mostra l'albero «Dijkstra(G,A)» con etichette numeriche sugli archi (1–6): interpretate come ordine di inserimento.

## Domande da esame

- Descrivere BFS con i colori e il ruolo della coda; qual è l'invariante del ciclo `while`?
- Perché BFS costa $O(V+E)$? Spiegare l'analisi aggregata e perché non è $O(V \cdot V)$.
- Dimostrare che $d[v] = \delta(s, v)$ (lemmi 1–3 e teorema) e che il predecessor subgraph è un breadth-first tree.
- Scrivere DFS e DFS-Visit; calcolare $d$ e $f$ su un grafo dato e scrivere la struttura a parentesi.
- Enunciare e dimostrare il teorema di annidamento e quello del cammino bianco.
- Classificare gli archi di un grafo secondo una DFS; perché nei grafi non orientati ogni arco è tree o back?
- Come funziona Topological-Sort? Dimostrare che un grafo orientato è aciclico se e solo se la DFS non produce back edge, e che $f[v] < f[u]$ per ogni arco $u \to v$.
- Descrivere l'algoritmo di Dijkstra; perché non funziona con pesi negativi? Qual è il suo costo e come si può migliorare?

_Aggiornato: 2026-11-26 — ingest 13 - Algoritmi di visita di un grafo.pdf_

<!-- nav:inizio -->
---
**Lezione 13 · pagina 1 di 7** · ← [[splay-tree-operazioni|Splay-Tree-Search, Splay-Tree-Insert e Splay-Tree-Delete]] · [[lezioni|Indice]] · [[visita-di-un-grafo|Visita di un grafo]] →
<!-- nav:fine -->
