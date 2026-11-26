---
tipo: entità
categoria: algoritmo
paradigma: "visita di un grafo in profondità, con la ricorsione"
fonti_pdf: ["13 - Algoritmi di visita di un grafo.pdf#page=25", "13 - Algoritmi di visita di un grafo.pdf#page=28", "13 - Algoritmi di visita di un grafo.pdf#page=29", "13 - Algoritmi di visita di un grafo.pdf#page=31", "13 - Algoritmi di visita di un grafo.pdf#page=35"]
---

# Visita in profondità (DFS)

## Problema risolto · [[13 - Algoritmi di visita di un grafo.pdf#page=25|p. 25]]

- **Input:** un [[grafo]] $G = (V, E)$, orientato o no, con liste di adiacenza.
- **Output:** per ogni vertice $v$ il predecessore $\pi[v]$ e due **timestamp**: $d[v]$ (istante di scoperta) e $f[v]$ (istante di completamento); i $\pi$ formano una **depth-first forest**.

## Idea · [[13 - Algoritmi di visita di un grafo.pdf#page=25|p. 25]], [[13 - Algoritmi di visita di un grafo.pdf#page=26|26]]

La DFS (*Depth-First Search*) esplora i vicini del **nodo scoperto più di recente** che ha ancora vicini non esplorati: la visita procede «in profondità». Se ci sono nodi non esplorati, la ricerca **riparte da uno di essi**: alla fine tutti i vertici sono esplorati. Come in [[visita-in-ampiezza|BFS]], DFS tiene traccia dei predecessori; il predecessor subgraph può essere composto da **più alberi**, quindi è definito in maniera leggermente diversa:

$$
G_\pi = (V, E_\pi), \qquad E_\pi = \{(\pi[v], v) : v \in V \ \text{e}\ \pi[v] \ne \text{NIL}\} \quad \text{(tree edges)}
$$

e forma una **depth-first forest**, composta da diversi **depth-first tree** (p. 25).

Come in BFS i nodi sono **bianchi, grigi o neri** ([[visita-di-un-grafo]]): ciò assicura che ogni vertice finisca in un solo depth-first tree, quindi gli alberi sono disgiunti (p. 26). DFS marca ciascun nodo con due timestamp:
- $d[v]$: l'istante in cui $v$ è **scoperto** (e colorato di grigio);
- $f[v]$: l'istante in cui **termina la ricerca dei vicini** di $v$ (che viene colorato di nero).

I timestamp sono interi compresi tra 1 e $2\lvert V \rvert$; per ogni nodo c'è un istante di scoperta e uno di completamento, e per ogni vertice $u$ vale $d[u] < f[u]$.

## Pseudocodice · [[13 - Algoritmi di visita di un grafo.pdf#page=28|p. 28]]

```
DFS (G)
1  for each vertex u ∈ V[G]
2      do color[u] ← WHITE
3         π[u] ← NIL
4  time ← 0
5  for each vertex u ∈ V[G]
6      do if color[u] = WHITE
7          then DFS-Visit (u)

DFS-Visit (u)
1  color[u] ← GRAY
2  time ← time + 1
3  d[u] ← time
4  for each v ∈ Adj[u]
5      do if color[v] = WHITE
6          then π[v] ← u
7               DFS-Visit (v)
8  color[u] ← BLACK
9  f[u] ← time ← time + 1
```

I numeri di riga sono miei. Anche per DFS **i risultati della ricerca variano a seconda dell'ordine con cui si esaminano i nodi** (p. 28).

![[13-visite-grafi-p27-dfs-grafo.png]]
![[13-visite-grafi-p28-dfs-codice.png]]

## Esempio di esecuzione · [[13 - Algoritmi di visita di un grafo.pdf#page=28|p. 28]]

![[animazione-visita-in-profondita.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero DFS sul grafo non orientato di p. 28, con le liste di adiacenza ordinate in modo da riprodurre i tempi della figura. Per ogni vertice un fotogramma di scoperta (righe 1–3 di DFS-Visit, e 13–14 per la chiamata ricorsiva) e uno di completamento (righe 8–9), con la pila delle chiamate.

La figura di p. 28 mostra l'albero DFS dalla sorgente $s$ con i tempi $d/f$ (archi dell'albero in blu, gli altri in grigio): $s$ 1/20, $a$ 2/11, $d$ 3/8, $g$ 4/5, $h$ 6/7, $e$ 9/10, $b$ 12/17, $f$ 13/16, $i$ 14/15, $c$ 18/19. Tree edges: $(s,a)$, $(a,d)$, $(d,g)$, $(d,h)$, $(a,e)$, $(s,b)$, $(b,f)$, $(f,i)$, $(s,c)$. Gli altri archi, $(g,a)$, $(d,s)$, $(i,b)$ e $(f,s)$, sono back edge (verso un antenato).

Traccia (verificata con [[visite_di_grafi.py]], che riproduce esattamente i tempi della slide):

| Vertice | Scoperto ($d$) | Terminato ($f$) | Predecessore $\pi$ |
|---|---|---|---|
| $s$ | 1 | 20 | NIL |
| $a$ | 2 | 11 | $s$ |
| $d$ | 3 | 8 | $a$ |
| $g$ | 4 | 5 | $d$ |
| $h$ | 6 | 7 | $d$ |
| $e$ | 9 | 10 | $a$ |
| $b$ | 12 | 17 | $s$ |
| $f$ | 13 | 16 | $b$ |
| $i$ | 14 | 15 | $f$ |
| $c$ | 18 | 19 | $s$ |

## Complessità · [[13 - Algoritmi di visita di un grafo.pdf#page=29|p. 29]]

### Derivazione — $T = \Theta(V + E)$ · [[13 - Algoritmi di visita di un grafo.pdf#page=29|p. 29]]
**Fonte:** analisi nella slide: «I cicli for di DFS impiegano $\Theta(V)$, esclusa la chiamata a DFS-Visit; DFS-Visit viene chiamata una volta per ciascun nodo; il ciclo for di DFS-Visit su tutte le invocazioni è $\Theta(E)$; il tempo complessivo è $O(V + E)$».
**Si parte da:** il pseudocodice e la somma delle lunghezze delle liste ($\lvert E \rvert$ orientato, $2\lvert E \rvert$ non orientato).

- Le righe 1–7 di DFS fanno due cicli sui vertici, escluso il lavoro delle chiamate di DFS-Visit: $\Theta(V)$.
- **DFS-Visit è chiamata una sola volta per nodo**: è chiamata solo su vertici bianchi e la prima cosa che fa è colorare il vertice di grigio, quindi nessun vertice è visitato due volte.
- Il ciclo `for each v ∈ Adj[u]` di DFS-Visit, sommato su tutte le invocazioni, scorre ogni lista di adiacenza una volta: $\sum_{u \in V} \lvert Adj[u] \rvert = \Theta(E)$.

$$
T(V, E) = \Theta(V) + \Theta(E) = \Theta(V + E)
$$

La slide scrive $O(V + E)$; i due ordini coincidono perché ogni termine è raggiunto (anche se non tutti i vertici sono raggiungibili da una sola sorgente, DFS riparte dai bianchi).

![[13-visite-grafi-p29-dfs-costo.png]]

**Sanity check** ([[visite_di_grafi.py]]): sul grafo di p. 28 ($V = 10$) le liste hanno in tutto 26 voci $= 2 \lvert E \rvert$ con $\lvert E \rvert = 13$.
**Ipotesi:** modello RAM; liste di adiacenza.

## Correttezza · [[13 - Algoritmi di visita di un grafo.pdf#page=30|p. 30]]–[[13 - Algoritmi di visita di un grafo.pdf#page=37|37]]

### Struttura a parentesi · [[13 - Algoritmi di visita di un grafo.pdf#page=30|p. 30]]
I tempi di scoperta e di terminazione hanno una **struttura a parentesi**: scrivendo $d[u]$ come «$(u$» e $f[u]$ come «$u)$» si ottiene un'espressione corretta. Per l'esempio di p. 28:

$$
(s\ (a\ (d\ (g\ g)\ (h\ h)\ d)\ (e\ e)\ a)\ (b\ (f\ (i\ i)\ f)\ b)\ (c\ c)\ s)
$$

![[13-visite-grafi-p30-dfs-parentesi.png]]

### Derivazione — Teorema 1 (annidamento) · [[13 - Algoritmi di visita di un grafo.pdf#page=31|p. 31]], [[13 - Algoritmi di visita di un grafo.pdf#page=32|32]]
**Fonte:** enunciato e dimostrazione nelle slide.
**Teorema 1.** Per ogni coppia di nodi $u$ e $v$ si può verificare **una sola** delle seguenti condizioni:
1. gli intervalli $[d[u], f[u]]$ e $[d[v], f[v]]$ sono **disgiunti** e $u$ non è discendente di $v$ né $v$ di $u$ nella depth-first forest;
2. $[d[u], f[u]]$ è contenuto interamente in $[d[v], f[v]]$ e $u$ è un discendente di $v$ in un depth-first tree;
3. $[d[v], f[v]]$ è contenuto interamente in $[d[u], f[u]]$ e $v$ è un discendente di $u$ in un depth-first tree.

**Corollario 1.** $v$ è un discendente di $u$ nella depth-first forest se e solo se $d[u] < d[v] < f[v] < f[u]$.

*Dimostrazione.* Si supponga $d[u] < d[v]$. Quando $v$ è scoperto, $u$ è ancora grigio o è nero.
- **Caso 1) $d[v] < f[u]$:** $v$ è scoperto quando $u$ è ancora grigio, quindi $v$ è un discendente di $u$. I vicini di $v$ saranno quindi esplorati tutti ($v$ nero) prima che siano esplorati tutti i vicini di $u$, cioè $f[v] < f[u]$: l'intervallo $[d[v], f[v]]$ è contenuto in $[d[u], f[u]]$.
- **Caso 2) $f[u] < d[v]$:** $d[u] < f[u] < d[v] < f[v]$, quindi gli intervalli sono disgiunti. Dato che $u$ è nero quando $v$ è scoperto, nessun vertice è discendente dell'altro.

### Derivazione — Teorema 2 (cammino bianco) · [[13 - Algoritmi di visita di un grafo.pdf#page=33|p. 33]], [[13 - Algoritmi di visita di un grafo.pdf#page=34|34]]
**Teorema 2.** In una depth-first forest, un vertice $v$ è un discendente di $u$ se e solo se al tempo $d[u]$ $v$ può essere raggiunto da $u$ attraverso un percorso che consiste di **soli nodi bianchi**.

*($\Rightarrow$)* $v$ è un discendente di $u$ in un depth-first tree. Sia $w$ un qualunque nodo lungo il percorso da $u$ a $v$ nel depth-first tree: $w$ è un discendente di $u$, quindi per il corollario 1 $d[u] < d[w]$, e quindi $w$ è bianco quando si scopre $u$. Dunque al tempo $d[u]$ il percorso da $u$ a $v$ (con $v$ bianco) è fatto di soli nodi bianchi.

*($\Leftarrow$)* Al tempo $d[u]$ c'è un percorso da $u$ a $v$ di soli nodi bianchi. Si assuma che tutti i nodi del percorso, eccetto $v$, diventino discendenti di $u$. Altrimenti, sia $v$ il nodo più vicino a $u$ che **non** diventa discendente di $u$, e sia $w$ il suo predecessore lungo il percorso ($w$ diventa discendente di $u$), quindi $f[w] \le f[u]$ per il corollario 1 (l'uguaglianza vale perché $w$ potrebbe essere $u$). $v$ è scoperto dopo che è scoperto $u$ ma prima che $w$ sia finito ($v$ è un vicino di $w$):

$$
d[u] < d[v] < f[w] \le f[u]
$$

Per il teorema 1, $[d[v], f[v]]$ è contenuto in $[d[u], f[u]]$ e quindi (corollario 1) $v$ deve essere un discendente di $u$.

> ⚠️ Contraddizione (refuso): a p. 33 la slide cita «corollario 8» dove intende il corollario 1.

![[13-visite-grafi-p33-dfs-cammino-bianco.png]]

**Sanity check** ([[visite_di_grafi.py]]): su tutte le coppie di vertici dell'esempio di p. 28 gli intervalli $[d, f]$ sono disgiunti oppure uno è contenuto nell'altro (teorema 1).
**Ipotesi:** timestamp assegnati come nello pseudocodice (ogni scoperta e ogni terminazione incrementano `time` di 1).

## Classificazione degli archi · [[13 - Algoritmi di visita di un grafo.pdf#page=35|p. 35]]–[[13 - Algoritmi di visita di un grafo.pdf#page=37|37]]

Una DFS **partiziona gli archi** di un grafo in quattro insiemi (p. 35):
- **tree edge**: gli archi della depth-first forest; $(u, v)$ lo è se $v$ è scoperto esplorando i vicini di $u$;
- **back edge**: archi $(u, v)$ con $v$ **antenato** di $u$ in un depth-first tree (i self-loop sono considerati back edge);
- **forward edge**: archi $(u, v)$ con $u$ antenato di $v$ in un depth-first tree (non tree);
- **cross edge**: tutti gli altri, tra nodi di diversi depth-first tree o dello stesso albero ma non uno discendente dell'altro.

Per i grafi non orientati può esserci ambiguità tra $(u, v)$ e $(v, u)$, che sono lo stesso arco: un arco viene classificato sulla base della «direzione» incontrata per prima.

**Classificazione al volo** (p. 36): un arco $(u, v)$ può essere classificato in base al **colore di $v$** nel momento in cui è esplorato per la prima volta:
- $v$ **bianco**: $(u, v)$ è un tree edge;
- $v$ **grigio**: $(u, v)$ è un back edge;
- $v$ **nero** ($f[v] < f[u]$): forward o cross edge; se $d[u] < d[v]$ è un **forward edge** ($d[u] < d[v] < f[v] < f[u]$), se $d[u] > d[v]$ è un **cross edge**.

![[13-visite-grafi-p36-dfs-classificazione-archi.png]]

**Grafi non orientati** (p. 37): in una DFS ogni arco è o un tree edge o un back edge. Assumendo che $u$ sia scoperto prima di $v$: dato che $v$ è un vicino di $u$, $v$ deve essere scoperto e completato prima che sia completato $u$. Se $(u, v)$ è esplorato per primo nella direzione $u \to v$ allora è un tree edge; se è esplorato per primo nella direzione $v \to u$ allora è un back edge.

![[13-visite-grafi-p37-dfs-grafo-non-orientato.png]]

> 🧩 Sul grafo di p. 28 ([[visite_di_grafi.py]]) la DFS dà 9 tree edge e 4 back edge, nessun forward o cross, come atteso per un grafo non orientato. Perché il colore decide: se $v$ è grigio, è nella pila delle chiamate aperte, quindi è un antenato di $u$ (back); se è nero ha già finito, quindi non è un antenato di $u$ ed è stato scoperto prima ($d[v] < d[u]$, cross) o dopo ($d[v] > d[u]$, forward).

## Connessioni

- [[visita-di-un-grafo]] — le due strategie, i colori
- [[visita-in-ampiezza]] — l'altra visita (coda invece di ricorsione)
- [[ordinamento-topologico]] — usa i tempi $f$ di una DFS
- [[inorder-tree-walk]] — anche la visita in ordine di un albero binario è una visita ricorsiva in profondità

## Fonti · [[13 - Algoritmi di visita di un grafo.pdf#page=25|p. 25]]–[[13 - Algoritmi di visita di un grafo.pdf#page=37|37]]

- [[lezione-13-algoritmi-di-visita-di-un-grafo]]

_Aggiornato: 2026-11-26 — ingest 13 - Algoritmi di visita di un grafo.pdf_

<!-- nav:inizio -->
---
**Lezione 13 · pagina 5 di 7** · ← [[print-path|Print-Path]] · [[lezioni|Indice]] · [[ordinamento-topologico|Ordinamento topologico (Topological-Sort)]] →
<!-- nav:fine -->
