---
tipo: concetto
importanza_esame: alta
prerequisiti: ["grafo", "liste-di-adiacenza", "matrice-di-adiacenza"]
fonti_pdf: ["13 - Algoritmi di visita di un grafo.pdf#page=7", "13 - Algoritmi di visita di un grafo.pdf#page=10", "13 - Algoritmi di visita di un grafo.pdf#page=26"]
---

# Visita di un grafo

## Definizione · [[13 - Algoritmi di visita di un grafo.pdf#page=7|p. 7]]

Una volta rappresentato un [[grafo]] (con [[liste-di-adiacenza]] o [[matrice-di-adiacenza]]), una **visita** è un'esplorazione sistematica dei suoi vertici e dei suoi archi, a partire da un **nodo sorgente**, **evitando di visitare più volte lo stesso vertice**.

## Le due strategie · [[13 - Algoritmi di visita di un grafo.pdf#page=7|p. 7]]

| Strategia | Cosa fa | Pagina |
|---|---|---|
| **Visita in ampiezza** (BFS, *Breadth First Search*) | esplora prima i vertici più vicini alla sorgente, procedendo **per livelli** | [[visita-in-ampiezza]] |
| **Visita in profondità** (DFS, *Depth First Search*) | esplora un cammino il più possibile **in profondità**, tornando indietro quando non può proseguire | [[visita-in-profondita]] |

Le visite permettono anche di risolvere problemi più complessi, come l'**ordinamento topologico**, che dispone i vertici di un grafo orientato aciclico (DAG) rispettando le dipendenze tra essi → [[ordinamento-topologico]].

![[13-visite-grafi-p7-visita-di-un-grafo.png]]

## I colori dei nodi · [[13 - Algoritmi di visita di un grafo.pdf#page=10|p. 10]], [[13 - Algoritmi di visita di un grafo.pdf#page=26|26]]

Per tenere traccia dei nodi esplorati, entrambe le visite colorano i vertici (BFS opera su grafi orientati e non, p. 10). In ogni istante un nodo può essere:
- **bianco**, se non è ancora stato visitato;
- **grigio**, se è stato visitato ma non tutti i suoi vicini sono stati visitati;
- **nero**, se è stato visitato insieme a tutti i suoi vicini.

Se il nodo $v$ viene visitato in quanto vicino di $u$, allora $u$ è il **predecessore** di $v$, scritto $\pi[v]$. Ogni nodo viene visitato al più una volta e quindi ha al più un predecessore. Nella DFS i colori assicurano che ogni vertice finisca in un solo albero della foresta di visita, quindi gli alberi sono disgiunti (p. 26).

## Spiegazione

> 🧩 Perché servono i colori: un vertice grigio è «in lavorazione» (nella coda di BFS, o nella pila delle chiamate di DFS), uno nero è finito. Controllare il colore prima di visitare un vicino è ciò che impedisce di visitare due volte lo stesso vertice anche nei grafi con cicli: senza questo controllo la visita non terminerebbe. Entrambe le visite costano $O(V + E)$ con le liste di adiacenza: ogni vertice è trattato una volta e ogni lista di adiacenza è scorsa una volta, quindi si leggono $\lvert E \rvert$ (grafo orientato) o $2\lvert E \rvert$ (non orientato) voci.

## Perché importa

Le visite sono la base di molti algoritmi su grafi: la BFS calcola le distanze minime in numero di archi, ed è alla base degli algoritmi di Dijkstra (percorsi minimi, → [[dijkstra]]) e di Prim (albero di copertura minimo) (p. 9); la DFS serve per l'ordinamento topologico e per classificare gli archi.

## Connessioni

- [[visita-in-ampiezza]], [[visita-in-profondita]], [[ordinamento-topologico]] — gli algoritmi
- [[dijkstra]] — percorsi minimi con pesi, che estende l'idea della BFS
- [[liste-di-adiacenza]], [[matrice-di-adiacenza]] — le rappresentazioni su cui lavorano
- [[albero]] — le visite costruiscono un albero (o una foresta) di visita

## Fonti · [[13 - Algoritmi di visita di un grafo.pdf#page=7|p. 7]], [[13 - Algoritmi di visita di un grafo.pdf#page=10|10]], [[13 - Algoritmi di visita di un grafo.pdf#page=26|26]]

- [[lezione-13-algoritmi-di-visita-di-un-grafo]]

_Aggiornato: 2026-11-26 — ingest 13 - Algoritmi di visita di un grafo.pdf_

<!-- nav:inizio -->
---
**Lezione 13 · pagina 2 di 7** · ← [[lezione-13-algoritmi-di-visita-di-un-grafo|Lezione 13: introduzione e riepilogo]] · [[lezioni|Indice]] · [[visita-in-ampiezza|Visita in ampiezza (BFS)]] →
<!-- nav:fine -->
