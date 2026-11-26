---
tipo: entità
categoria: algoritmo
paradigma: "visita di un grafo per livelli, con una coda"
fonti_pdf: ["13 - Algoritmi di visita di un grafo.pdf#page=9", "13 - Algoritmi di visita di un grafo.pdf#page=12", "13 - Algoritmi di visita di un grafo.pdf#page=14", "13 - Algoritmi di visita di un grafo.pdf#page=19", "13 - Algoritmi di visita di un grafo.pdf#page=21"]
---

# Visita in ampiezza (BFS)

## Problema risolto · [[13 - Algoritmi di visita di un grafo.pdf#page=9|p. 9]]

- **Input:** un [[grafo]] $G = (V, E)$, orientato o no, rappresentato con [[liste-di-adiacenza]], e un nodo **sorgente** $s$.
- **Output:** per ogni vertice $v$, la distanza $d[v]$ (numero di archi) da $s$ e il predecessore $\pi[v]$; i vertici raggiungibili da $s$ con i loro $\pi$ formano un albero con radice $s$ (*breadth-first tree*).

La BFS (*Breadth First Search*) è un semplice algoritmo per «visitare» i nodi di un grafo (p. 9). Importanti algoritmi si basano su questo approccio: l'algoritmo di **Dijkstra** per lo shortest path ([[dijkstra]]) e l'algoritmo di **Prim** per il minimum spanning tree.

## Idea · [[13 - Algoritmi di visita di un grafo.pdf#page=9|p. 9]]–[[13 - Algoritmi di visita di un grafo.pdf#page=11|11]]

A partire da $s$, la BFS visita tutti i nodi adiacenti a un nodo e poi procede a visitare allo stesso modo gli adiacenti (p. 9):
- tutti i nodi che distano $k$ dalla sorgente vengono visitati prima del primo nodo che dista $k+1$;
- la BFS produce un albero con radice in $s$ che contiene tutti i nodi raggiungibili da $s$;
- il percorso da $s$ a $v$ nell'albero è il **più breve** da $s$ a $v$ nel grafo.

Per tenere traccia dei nodi esplorati si usano i **colori** ([[visita-di-un-grafo]]): **bianco** se non è ancora visitato, **grigio** se è stato visitato ma non tutti i suoi vicini, **nero** se è stato visitato insieme a tutti i suoi vicini (p. 10). Se $v$ è visitato in quanto vicino di $u$, $u$ è il predecessore di $v$; ogni nodo è visitato al più una volta e ha al più un predecessore. L'albero ottenuto **dipende dall'ordine** con cui si visitano i vicini, **ma la lunghezza dei percorsi minimi non cambia** (p. 11).

![[13-visite-grafi-p11-bfs-grafo.png]]

## Pseudocodice · [[13 - Algoritmi di visita di un grafo.pdf#page=12|p. 12]]

Assume una rappresentazione con liste di adiacenza. Il predecessore $\pi$ di un nodo è NIL se il nodo è la sorgente o non è stato raggiunto (ancora).

```
BFS (G,s)
1  for each vertex u ∈ V[G] - {s}
2      do color[u] ← WHITE
3         d[u] ← ∞
4         π[u] ← NIL
5  color[s] ← GRAY
6  d[s] ← 0
7  π[s] ← NIL
8  Q ← Ø
9  Enqueue (Q,s)
10 while Q ≠ Ø
11     do u ← Dequeue (Q)
12        for each v ∈ Adj[u]
13            do if color[v] = WHITE
14                then color[v] ← GRAY
15                     d[v] ← d[u] + 1
16                     π[v] ← u
17                     Enqueue (Q,v)
18        color[u] ← BLACK
```

I numeri di riga sono miei (nell'animazione la numerazione parte dall'intestazione `BFS (G,s)`, quindi ogni numero è aumentato di 1).

![[13-visite-grafi-p12-bfs-codice.png]]

## Esempio di esecuzione · [[13 - Algoritmi di visita di un grafo.pdf#page=11|p. 11]]

![[animazione-visita-in-ampiezza.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero BFS sul grafo non orientato di p. 11 (vertici $r, s, t, u, v, w, x, y$) con sorgente $s$ e liste in ordine alfabetico: le slide mostrano solo il grafo di partenza (coda vuota, «ancora vuoto» l'albero). Si vedono i colori, i valori $d$, la coda $Q$, il vettore $\pi$ e gli archi dell'albero in blu.

Traccia (verificata con [[visite_di_grafi.py]]):

| Estratto $u$ | $Adj[u]$ | Nuovi grigi ($d$, $\pi$) | Coda dopo |
|---|---|---|---|
| (inizio) | — | $s$ ($d = 0$) | $\langle s \rangle$ |
| $s$ | $r, w$ | $r$ (1, $s$), $w$ (1, $s$) | $\langle r, w \rangle$ |
| $r$ | $s, v$ | $v$ (2, $r$) | $\langle w, v \rangle$ |
| $w$ | $s, t, x$ | $t$ (2, $w$), $x$ (2, $w$) | $\langle v, t, x \rangle$ |
| $v$ | $r$ | nessuno | $\langle t, x \rangle$ |
| $t$ | $u, w, x$ | $u$ (3, $t$) | $\langle x, u \rangle$ |
| $x$ | $t, u, w, y$ | $y$ (3, $x$) | $\langle u, y \rangle$ |
| $u$ | $t, x, y$ | nessuno | $\langle y \rangle$ |
| $y$ | $u, x$ | nessuno | $\langle \rangle$ |

Risultato: $d(s, r, w, v, t, x, u, y) = (0, 1, 1, 2, 2, 2, 3, 3)$; ordine di estrazione $s, r, w, v, t, x, u, y$. Con un diverso ordine dei vicini l'albero cambia (per esempio $\pi[u] = x$ invece di $t$ con le liste in ordine inverso) ma le $d$ restano le stesse (p. 11).

## Correttezza · [[13 - Algoritmi di visita di un grafo.pdf#page=12|p. 12]]–[[13 - Algoritmi di visita di un grafo.pdf#page=21|21]]

**Invariante del ciclo `while`** (p. 12): all'inizio di ogni iterazione, $Q$ contiene tutti i nodi grigi.
- *Vero prima della prima iterazione*: $Q = \langle s \rangle$ e $s$ è l'unico nodo grigio (righe 5–9).
- *Una iterazione conserva la proprietà*: l'estrazione di $u$ toglie un nodo grigio dalla coda; ogni vicino bianco $v$ diventa grigio e viene accodato (righe 13–17); alla fine $u$ diventa nero (riga 18). Quindi grigi e nodi in coda restano gli stessi.

> 🧩 L'invariante implica che a ogni iterazione i nodi grigi sono quelli ancora in attesa di essere esplorati; al termine, con $Q = \emptyset$, non ci sono nodi grigi: ogni nodo raggiunto è nero.

### Derivazione — distanze minime · [[13 - Algoritmi di visita di un grafo.pdf#page=15|p. 15]]–[[13 - Algoritmi di visita di un grafo.pdf#page=19|19]]
**Fonte:** definizione di distanza minima e quattro risultati (lemmi 1–3, teorema) dimostrati nelle slide.
**Si parte da:** la **distanza minima** $\delta(s, v)$, il numero minimo di archi di un qualunque percorso da $s$ a $v$ ($\delta(s, v) = \infty$ se non c'è un percorso); un percorso di lunghezza minima è uno *shortest path* (p. 15).

**Lemma 1** (p. 16). Per ogni arco $(u, v) \in E$: $\delta(s, v) \le \delta(s, u) + 1$.
- Se $u$ è raggiungibile da $s$ lo è anche $v$, e lo shortest path da $s$ a $v$ non può essere più lungo dello shortest path da $s$ a $u$ più l'arco $(u, v)$.
- Se $u$ non è raggiungibile, $\delta(s, u) = \infty$ e la tesi è vera.

**Lemma 2** (p. 17). Dopo BFS, per ogni vertice $v$: $d[v] \ge \delta(s, v)$. Per induzione sul numero di operazioni di Enqueue:
- *Base:* dopo che $s$ è accodato, $d[s] = \delta(s, s) = 0$ e per gli altri nodi $d[v] = \infty \ge \delta(s, v)$.
- *Passo:* sia $v$ un vertice bianco scoperto cercando i vicini di $u$; per ipotesi induttiva $d[u] \ge \delta(s, u)$. La distanza assegnata è

$$
d[v] = d[u] + 1 \ge \delta(s, u) + 1 \ge \delta(s, v) \qquad \text{ipotesi induttiva, poi lemma 1}
$$

$v$ diventa grigio e non viene più riaccodato: la sua distanza non cambia più.

**Lemma 3** (p. 18). Durante l'esecuzione, se la coda contiene $\langle v_1, v_2, \dots, v_r \rangle$ ($v_1$ testa, $v_r$ coda), allora $d[v_i] \le d[v_{i+1}]$ per $i = 1, \dots, r-1$ e $d[v_r] \le d[v_1] + 1$. Per induzione sul numero di operazioni sulla coda:
- *Base:* all'inizio la coda contiene solo $s$ e la tesi vale.
- *Passo 1 (si estrae la testa $v_1$):* la nuova testa è $v_2$ (se la coda è vuota, tesi banale). Per ipotesi $d[v_1] \le d[v_2]$ e $d[v_r] \le d[v_1] + 1$, quindi $d[v_r] \le d[v_2] + 1$: vera anche per $v_2$.
- *Passo 2 (si accoda $v_{r+1}$, scoperto a partire da $u$, già estratto):* per ipotesi $d[u] \le d[v_1]$, quindi $d[v_{r+1}] = d[u] + 1 \le d[v_1] + 1$; inoltre $d[v_r] \le d[u] + 1 = d[v_{r+1}]$; le altre relazioni restano immutate.

**Corollario 1** (p. 18). Dal lemma 3 e dal fatto che la distanza di un nodo è assegnata al più una volta: se $v_i$ è accodato prima di $v_j$, allora $d[v_i] \le d[v_j]$.

**Teorema** (completezza, p. 19). BFS scopre tutti i nodi raggiungibili da $s$ e al termine $d[v] = \delta(s, v)$ per ogni $v$. Per ogni $v$ raggiungibile, uno shortest path da $s$ a $v$ è uno shortest path da $s$ a $\pi[v]$ seguito dall'arco $(\pi[v], v)$. Dimostrazione per assurdo (le slide arrivano fino a metà):
- si assuma che qualche vertice riceva una distanza diversa da quella minima; tra questi sia $v$ quello con la più piccola distanza minima (chiaramente $v \ne s$);
- per il lemma 2 $d[v] \ge \delta(s, v)$, quindi $d[v] > \delta(s, v)$ e $v$ deve essere raggiungibile da $s$ (altrimenti $\delta(s, v) = \infty \ge d[v]$);
- sia $u$ il nodo che precede $v$ lungo uno shortest path da $s$ a $v$, quindi $\delta(s, v) = \delta(s, u) + 1$.

> ❓ Salto non ricostruito dalla slide: la p. 19 si interrompe qui (la dimostrazione continua nell'animazione, che non è nel PDF). 🧩 Completamento mio, standard: poiché $\delta(s, u) < \delta(s, v)$, $u$ ha la distanza corretta, $d[u] = \delta(s, u)$, quindi $d[v] > \delta(s, v) = d[u] + 1$ (★). Quando $u$ viene estratto dalla coda, $v$ può essere:
> - **bianco:** la riga 15 assegna $d[v] = d[u] + 1$, in contraddizione con (★);
> - **nero** (già estratto prima di $u$): per il corollario 1 $d[v] \le d[u]$, in contraddizione con (★);
> - **grigio** (scoperto da un nodo $w$ estratto prima di $u$): $d[v] = d[w] + 1$ e per il corollario 1 $d[w] \le d[u]$, quindi $d[v] \le d[u] + 1$, in contraddizione con (★).
>
> In ogni caso l'assunzione è assurda: la tesi vale. L'ultima affermazione del teorema segue perché $\pi[v] = u$ per un nodo $u$ con $d[v] = d[u] + 1$.

### Derivazione — breadth-first tree · [[13 - Algoritmi di visita di un grafo.pdf#page=20|p. 20]], [[13 - Algoritmi di visita di un grafo.pdf#page=21|21]]
**Fonte:** definizione del *predecessor subgraph* e lemma 4 con la dimostrazione.
**Si parte da:** il teorema di completezza.

Il **predecessor subgraph** di $G$ è $G_\pi = (V_\pi, E_\pi)$ con
$$
V_\pi = \{v \in V : \pi[v] \ne \text{NIL}\} \cup \{s\}, \qquad E_\pi = \{(\pi[v], v) : v \in V_\pi - \{s\}\} \ \text{(tree edges)}
$$
È un albero perché dalla definizione di $E_\pi$ vale $\lvert E_\pi \rvert = \lvert V_\pi \rvert - 1$, condizione necessaria e sufficiente per un albero (p. 20). È un **breadth-first tree** se $V_\pi$ consiste dei vertici raggiungibili da $s$ e se per ogni $v \in V_\pi$ esiste un unico percorso semplice da $s$ a $v$ in $G_\pi$ che è anche lo shortest path da $s$ a $v$ in $G$.

**Lemma 4** (p. 21). Il predecessor subgraph restituito da BFS è un breadth-first tree. BFS pone $\pi[v] = u$ se e solo se $(u, v) \in E$ e $v$ è raggiungibile da $s$; quindi $V_\pi$ consiste dei vertici raggiungibili da $s$. Dato che il predecessor subgraph è un albero, contiene un unico percorso da $s$ a ciascun vertice; applicando il teorema precedente, ogni percorso è uno shortest path.

![[13-visite-grafi-p19-bfs-completezza.png]]
![[13-visite-grafi-p20-bfs-albero.png]]

Il percorso si stampa con [[print-path]].

## Complessità · [[13 - Algoritmi di visita di un grafo.pdf#page=13|p. 13]], [[13 - Algoritmi di visita di un grafo.pdf#page=14|14]]

### Derivazione — $T = O(V + E)$ · [[13 - Algoritmi di visita di un grafo.pdf#page=13|p. 13]], [[13 - Algoritmi di visita di un grafo.pdf#page=14|14]]
**Fonte:** analisi **aggregata** nelle slide («Effettuiamo un'analisi aggregata per determinare il tempo di esecuzione»).
**Si parte da:** il pseudocodice (righe 1–18) e dalla somma delle lunghezze delle liste: $\lvert E \rvert$ se $G$ è orientato, $2\lvert E \rvert$ se non orientato ([[liste-di-adiacenza]], p. 4).

| Parte | Quante volte | Costo |
|---|---|---|
| inizializzazione (righe 1–4) | $\lvert V \rvert - 1$ iterazioni, tre assegnamenti | $\Theta(V)$ |
| righe 5–9 | una volta | $\Theta(1)$ |
| accodamento e deaccodamento | ogni nodo entra in coda al più una volta (solo se bianco, e quando entra diventa grigio; mai ricolorato bianco) ed è estratto al più una volta; `Enqueue` e `Dequeue` costano $O(1)$ | $O(V)$ |
| `for each v ∈ Adj[u]` (righe 12–17) | la lista di $u$ è scorsa **solo quando $u$ è deaccodato**, quindi una volta per nodo | $O(E)$ |

$$
\begin{aligned}
\sum_{u \text{ estratto}} \lvert Adj[u] \rvert &\le \sum_{u \in V} \lvert Adj[u] \rvert = \Theta(E) && \text{ogni lista scorsa al più una volta} \\
T(V, E) &= \underbrace{\Theta(V)}_{\text{init}} + \underbrace{O(V)}_{\text{coda}} + \underbrace{O(E)}_{\text{liste}} = O(V + E) && \text{somma delle parti}
\end{aligned}
$$

La slide chiude: il tempo di esecuzione di BFS è $O(V + E)$.

![[13-visite-grafi-p13-bfs-costo-1.png]]
![[13-visite-grafi-p14-bfs-costo-2.png]]

> 🧩 Perché non $O(V \cdot V)$ (errore tipico): il `while` fa al più $V$ giri e ciascun `for` interno sembra poter scorrere fino a $V - 1$ vicini, ma non tutti i nodi hanno $V - 1$ vicini. L'analisi aggregata **somma** le iterazioni di tutti i giri, che in totale sono $\sum_u \lvert Adj[u] \rvert = \Theta(E)$. Esempio: in un grafo a stella con centro e $V - 1$ foglie, le iterazioni sono $2(V - 1)$, non $V^2$. Servono entrambi i termini perché $E$ può arrivare a circa $V^2$ (grafo denso) e può essere 0 mentre l'inizializzazione costa comunque $V$.

**Sanity check** ([[visite_di_grafi.py]], grafo di p. 11): le iterazioni del `for` interno sono 20 $= 2 \lvert E \rvert$ ($\lvert E \rvert = 10$, $\lvert V \rvert = 8$); sul grafo di p. 28 della lezione 08 ($V = 5$, $E = 7$) le liste hanno 14 voci.
**Ipotesi:** modello RAM; liste di adiacenza; se non tutti i nodi sono raggiungibili da $s$ si scorrono solo le liste dei raggiunti, e il limite resta $O(V + E)$.

## Proprietà

- **Visita per livelli:** i nodi sono scoperti in ordine non decrescente di $d$ (corollario 1).
- **Distanze minime:** $d[v] = \delta(s, v)$ per ogni $v$ (teorema), anche se l'albero dipende dall'ordine delle liste.
- Lavora su grafi orientati e non, **non** su grafi pesati: con pesi la strada con più archi può costare meno (p. 46, → [[dijkstra]]).

## Connessioni

- [[visita-di-un-grafo]] — le due strategie e i colori
- [[print-path]] — stampa lo shortest path usando $\pi$
- [[visita-in-profondita]] — l'altra visita, con una pila (la ricorsione) invece della coda
- [[coda]] — la struttura usata da BFS (FIFO)
- [[dijkstra]] — la stessa idea con una coda di priorità e pesi

## Fonti · [[13 - Algoritmi di visita di un grafo.pdf#page=9|p. 9]]–[[13 - Algoritmi di visita di un grafo.pdf#page=21|21]]

- [[lezione-13-algoritmi-di-visita-di-un-grafo]]

_Aggiornato: 2026-11-26 — ingest 13 - Algoritmi di visita di un grafo.pdf_

<!-- nav:inizio -->
---
**Lezione 13 · pagina 3 di 7** · ← [[visita-di-un-grafo|Visita di un grafo]] · [[lezioni|Indice]] · [[print-path|Print-Path]] →
<!-- nav:fine -->
