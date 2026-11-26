---
tipo: fonte
titolo: "Corso di Algoritmi e Strutture Dati — Backpropagation"
file_raw: "14 - Backpropagation.pdf"
pagine: "1-30"
data_ingest: 2026-11-26
formato: slide-pdf
argomenti: [grafo computazionale, regola della catena, backpropagation, ordinamento topologico, reti neurali]
---

# Lezione 14 — Backpropagation (14 - Backpropagation.pdf)

## Sommario · [[14 - Backpropagation.pdf#page=1|p. 1]], [[14 - Backpropagation.pdf#page=2|2]]

Slide del Prof. Marrone, a.a. 26/27, che usano gli algoritmi sui grafi (DAG, ordinamento topologico, riuso dei risultati intermedi) per spiegare la **backpropagation** del Machine Learning (che è il corso della seconda parte dell'esame integrato). Si parte dal calcolo del gradiente di una funzione composta, rappresentata come **grafo computazionale** feedforward (DAG per layer, ogni nodo è una funzione locale dei predecessori). L'algoritmo ha due passi in ordine topologico: **forward** (valori dei nodi) e **backward** (derivate $\delta_v = \partial C/\partial z_v$, accumulate con la regola della catena in ordine topologico inverso). Un esempio numerico completo, $C(a,b) = \tfrac{1}{2}(\sin(ab) + b - 1)^2$ in $(2, 3)$, dà $\nabla C \approx (4{,}9562;\ 5{,}0247)$. Seguono lo pseudocodice, la correttezza per induzione (invariante sulle $\delta$) e il costo $O(V+E)$. L'ultima parte collega il tutto alle reti neurali feedforward e all'apprendimento (aggiornamento $w_i \leftarrow w_i - \eta\,\partial C/\partial w_i$): la backpropagation calcola solo il gradiente, non modifica i parametri.

## Percorso della lezione

Pagine del wiki nell'ordine di prima comparsa nelle slide (è l'ordine delle pagine di questa lezione nel libro):
1. [[grafo-computazionale]] — pp. 2–6: motivazione, definizione per layer, esempio, il problema del gradiente
2. [[backpropagation]] — pp. 7–30: perché serve, regola della catena, forward, backward, esempio, pseudocodice, correttezza, costo, reti neurali

Già lette, riprese in questa lezione: *grafo* e *tipi-di-grafo* (DAG), *ordinamento-topologico* e *visita-in-profondita* (lezione 13: l'ordine topologico), *albero* (il grafo computazionale non è un albero).

**Ordine consigliato.** Le slide sono lineari; conviene aver letto prima l'ordinamento topologico (lezione 13).

## Punti chiave · [[14 - Backpropagation.pdf#page=2|p. 2]], [[14 - Backpropagation.pdf#page=3|3]], [[14 - Backpropagation.pdf#page=7|p. 7]]–[[14 - Backpropagation.pdf#page=10|10]], [[14 - Backpropagation.pdf#page=22|p. 22]]–[[14 - Backpropagation.pdf#page=24|24]], [[14 - Backpropagation.pdf#page=29|p. 29]]

1. Il gradiente di una funzione composta si calcola in modo sistematico rappresentandola come grafo computazionale → [[grafo-computazionale]].
2. Un grafo computazionale feedforward è un DAG per layer: archi solo verso layer superiori, ogni nodo è $z_v = f_v(z_{u_1}, \dots, z_{u_k})$.
3. Regola della catena sul grafo: $\partial C/\partial x = \sum_j (\partial C/\partial y_j)(\partial y_j/\partial x)$ sui successori di $x$.
4. Forward: valori in ordine topologico; backward: $\delta_C = 1$, poi $\delta_u \mathrel{+}= \delta_v \cdot \partial z_v/\partial z_u$ in ordine topologico inverso → [[backpropagation]].
5. Esempio numerico su $(2, 3)$: $\delta[a] \approx 4{,}9562$, $\delta[b] \approx 5{,}0247$ (due cammini, due contributi, una somma).
6. Correttezza con invariante: quando si processa $v$, $\delta_v$ è già corretta; costo $O(V+E)$ per ciascuno dei due passi.
7. Una rete neurale feedforward è un grafo computazionale con struttura regolare; la backpropagation calcola $\nabla C$ ma non aggiorna i parametri (ottimizzazione: $w_i \leftarrow w_i - \eta\,\partial C/\partial w_i$).

## Refusi e note · [[14 - Backpropagation.pdf#page=2|p. 2]], [[14 - Backpropagation.pdf#page=5|5]], [[14 - Backpropagation.pdf#page=26|p. 26]], [[14 - Backpropagation.pdf#page=28|28]], [[14 - Backpropagation.pdf#page=29|29]], [[14 - Backpropagation.pdf#page=30|30]]

- pp. 2, 5, 26, 28, 29: note a mano del docente (trascritte nelle pagine; p. 28 e p. 29 di lettura parzialmente incerta).
- pp. 11–21: ogni passo è una slide separata («FORWARD 1/5 … BACKWARD 5/5», «RISULTATO»).
- p. 22: lo pseudocodice è in stile Python (`for v in …`, `←`, `+=`), diverso dalle [[pseudocodice|convenzioni del corso]].
- p. 24: la slide avverte che i limiti assumono costo $O(1)$ per ogni operazione elementare e per il contributo di ogni arco.
- p. 30: primo fotogramma di un'animazione («1. Forward pass», immagine di un gatto, uscite Cane e Gatto, valori di input 0,20; 0,80; 0,50): non c'è lo svolgimento.

## Concetti introdotti

[[grafo-computazionale]], [[backpropagation]].

## Domande aperte

- Le slide non entrano nelle funzioni dei neuroni (somma pesata, attivazioni): rimandate alla parte di Machine Learning.
- Il costo dell'ottimizzazione (aggiornamento dei parametri) non è trattato qui.

## Domande da esame

- Cos'è un grafo computazionale feedforward e perché è un DAG ma non un albero?
- Scrivere la regola della catena su un grafo e spiegare perché serve sommare i contributi dei successori.
- Descrivere il passo forward e quello backward della backpropagation; perché si usano l'ordine topologico e quello inverso?
- Eseguire forward e backward su una funzione composta semplice, anche con più cammini per lo stesso nodo.
- Dimostrare la correttezza della backpropagation (invariante sulle $\delta$).
- Qual è la complessità del forward e del backward e quali ipotesi sono assunte?
- Qual è il ruolo della backpropagation nell'apprendimento di una rete neurale? Cosa non fa?

_Aggiornato: 2026-11-26 — ingest 14 - Backpropagation.pdf_

<!-- nav:inizio -->
---
**Lezione 14 · pagina 1 di 3** · ← [[dijkstra|Algoritmo di Dijkstra (percorsi minimi)]] · [[lezioni|Indice]] · [[grafo-computazionale|Grafo computazionale]] →
<!-- nav:fine -->
