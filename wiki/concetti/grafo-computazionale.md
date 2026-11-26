---
tipo: concetto
importanza_esame: media
prerequisiti: ["grafo", "ordinamento-topologico"]
fonti_pdf: ["14 - Backpropagation.pdf#page=2", "14 - Backpropagation.pdf#page=3", "14 - Backpropagation.pdf#page=5", "14 - Backpropagation.pdf#page=6"]
---

# Grafo computazionale

## Definizione · [[14 - Backpropagation.pdf#page=3|p. 3]]

Un **grafo computazionale feedforward** è un grafo diretto aciclico (DAG, [[grafo]]) **organizzato per layer** che rappresenta una funzione ottenuta come composizione di molte operazioni elementari:
- **Layer 0:** le variabili di input $x_1, \dots, x_n$;
- **Layer $1, 2, \dots, L-1$:** le variabili intermedie;
- **Layer $L$:** l'uscita scalare $C$ (o poche variabili di output).

Ogni nodo $v$ non di input rappresenta una **funzione locale** $z_v = f_v\bigl(z_{u_1}, \dots, z_{u_k}\bigr)$ dei valori dei suoi predecessori $u_1, \dots, u_k$ (indicati $pred[v]$). Il grafo è *feedforward*: gli archi vanno solo da layer inferiori a layer superiori, e non ci sono cicli. «Inferiore» e «superiore» sono intesi in termini di profondità di livello.

## Motivazione · [[14 - Backpropagation.pdf#page=2|p. 2]]

Si considera una funzione scalare $C: \mathbb{R}^n \to \mathbb{R}$ ottenuta come **composizione di molte operazioni elementari**, per esempio

$$
C(x) = \tfrac{1}{2}\bigl(f(g(h(x)))\bigr)^2
$$

L'obiettivo è calcolare il **gradiente** $\nabla C(x)$ in modo sistematico ed efficiente. L'idea è sfruttare la struttura di composizione, rappresentandola come un grafo computazionale. Nota a mano di p. 2: «da dove nasce → regola della catena».

![[14-backpropagation-p4-grafo-composizione.png]]

## Un esempio semplice · [[14 - Backpropagation.pdf#page=4|p. 4]], [[14 - Backpropagation.pdf#page=5|5]]

La funzione di esempio, con input $a$ e $b$, è

$$
C(a, b) = \tfrac{1}{2}\bigl(\sin(a \cdot b) + b - 1\bigr)^2
$$

e si scompone in operazioni elementari (p. 4: la composizione evidenzia $c = a \cdot b$, $d = \sin(c)$, $e = d + b$, $C = \tfrac{1}{2}(e-1)^2$). Ogni nodo rappresenta una variabile e ogni arco una dipendenza diretta:

| Layer | Nodo | Operazione |
|---|---|---|
| 0 | $a$, $b$ | input |
| 1 | $c$ | $c = a \cdot b$ |
| 2 | $d$ | $d = \sin(c)$ |
| 3 | $e$ | $e = d + b$ (riceve $d$ dal layer 2 e $b$ dal layer 0: «anche da un layer non adiacente») |
| 4 | $C$ | $C = \tfrac{1}{2}(e-1)^2$ |

Note a mano di p. 5: è un **grafo operazionale** in cui i nodi rappresentano le operazioni computazionalmente indipendenti, quindi è un flusso di dati; è un **DAG ma non è un albero**, quindi non ha una radice.

![[14-backpropagation-p5-grafo-semplice.png]]

## Il problema del gradiente sul grafo · [[14 - Backpropagation.pdf#page=6|p. 6]]

C'è un'unica uscita scalare $C$ in cima al grafo; si vogliono le derivate rispetto agli input, $\partial C/\partial a$ e $\partial C/\partial b$, e magari anche $\partial C/\partial c$, $\partial C/\partial d$, … per tutti i nodi interni. La regola della catena si può applicare **in modo meccanico** sul grafo, ma la sua applicazione ripetuta potrebbe essere molto onerosa: si risolve con la [[backpropagation]].

## Spiegazione

> 🧩 La differenza con un albero è essenziale: in un albero ogni nodo ha un solo padre, quindi la derivata di $C$ rispetto a un nodo si propagherebbe lungo un unico cammino. In un DAG un nodo può avere più successori (qui $b$ ha come successori $c$ ed $e$) e la derivata rispetto a $b$ è la **somma** dei contributi di tutti i cammini fino a $C$. Per questo l'ordine di elaborazione conta e serve un [[ordinamento-topologico]].

## Perché importa

È la struttura su cui si definisce la backpropagation, e collega gli algoritmi sui grafi (DAG, ordine topologico) all'apprendimento automatico (p. 29): le reti neurali feedforward sono grafi computazionali con una struttura molto regolare.

## Connessioni

- [[backpropagation]] — l'algoritmo che calcola il gradiente su questo grafo
- [[ordinamento-topologico]] — l'ordine in cui si valutano i nodi
- [[grafo]], [[tipi-di-grafo]] — un DAG
- [[albero]] — il grafo computazionale non è un albero

## Fonti · [[14 - Backpropagation.pdf#page=2|p. 2]]–[[14 - Backpropagation.pdf#page=6|6]]

- [[lezione-14-backpropagation]]

_Aggiornato: 2026-11-26 — ingest 14 - Backpropagation.pdf_

<!-- nav:inizio -->
---
**Lezione 14 · pagina 2 di 3** · ← [[lezione-14-backpropagation|Lezione 14: introduzione e riepilogo]] · [[lezioni|Indice]] · [[backpropagation|Backpropagation]] →
<!-- nav:fine -->
