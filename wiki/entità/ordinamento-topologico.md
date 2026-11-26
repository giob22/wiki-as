---
tipo: entità
categoria: algoritmo
paradigma: "ordinamento dei vertici con i tempi di completamento di una DFS"
fonti_pdf: ["13 - Algoritmi di visita di un grafo.pdf#page=38", "13 - Algoritmi di visita di un grafo.pdf#page=39", "13 - Algoritmi di visita di un grafo.pdf#page=40", "13 - Algoritmi di visita di un grafo.pdf#page=41", "13 - Algoritmi di visita di un grafo.pdf#page=43"]
---

# Ordinamento topologico (Topological-Sort)

## Problema risolto · [[13 - Algoritmi di visita di un grafo.pdf#page=38|p. 38]], [[13 - Algoritmi di visita di un grafo.pdf#page=39|39]]

- **Input:** un grafo orientato aciclico, *directed acyclic graph* (**DAG**) $G$.
- **Output:** un **ordinamento topologico** di $G$: un ordine dei nodi tale che **se esiste un arco $u \to v$ allora $u$ precede $v$**.

Se il grafo non è aciclico un tale ordinamento non è possibile. L'ordinamento è utile, ad esempio, quando gli archi indicano una **relazione di precedenza** (p. 39). Nota a mano di p. 38: «la disposizione deve rappresentare la proprietà del fenomeno ... il posizionamento rispetta il fenomeno sottostante» (lettura incerta). La figura di p. 38 mostra un grafo orientato con 7 vertici $v_1, \dots, v_7$ e lo stesso grafo con i vertici disposti in fila nell'ordine topologico $v_1, v_2, v_3, v_4, v_5, v_6, v_7$, con tutti gli archi che vanno da sinistra a destra.

![[13-visite-grafi-p38-ordinamento-topologico.png]]

## Idea · [[13 - Algoritmi di visita di un grafo.pdf#page=39|p. 39]], [[13 - Algoritmi di visita di un grafo.pdf#page=40|40]]

Una [[visita-in-profondita|DFS]] può essere usata per realizzare un ordinamento topologico: ogni vertice, **quando termina** (diventa nero), viene inserito **in testa** a una lista concatenata; la lista così ottenuta, letta dall'inizio, è un ordinamento topologico. Nota a mano di p. 40: «facciamo ordinamento *del* grafo e non *sul* grafo → fin ora abbiamo sempre visto ordinamenti sul grafo e non *del* grafo» (cioè qui si ordinano i vertici del grafo, non i suoi dati).

## Pseudocodice · [[13 - Algoritmi di visita di un grafo.pdf#page=40|p. 40]]

```
Topological-Sort (G)
1  Call DFS(G) to compute finishing times f[v] for each vertex v
2  As each vertex is finished, insert it onto the front of a linked list
3  return the linked list of vertices
```

(In inglese nella slide.)

![[13-visite-grafi-p39-topological-sort-dag.png]]
![[13-visite-grafi-p40-topological-sort-codice.png]]

## Esempio di esecuzione · [[13 - Algoritmi di visita di un grafo.pdf#page=39|p. 39]], [[13 - Algoritmi di visita di un grafo.pdf#page=40|40]]

![[animazione-ordinamento-topologico.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero Topological-Sort (cioè DFS da $a$, con la lista in testa) sul DAG delle slide. L'ordine dei vicini in $Adj[a] = \langle d, b \rangle$ e $Adj[d] = \langle h, c \rangle$ è scelto da me per riprodurre l'ordine della slide.

Il DAG di p. 39 ha 10 vertici $a, \dots, j$ e gli archi $a \to d$, $a \to b$, $b \to e$, $e \to f$, $f \to d$, $d \to c$, $d \to h$, $c \to g$, $g \to j$, $j \to i$, $h \to i$; la slide mostra sotto il grafo l'ordinamento $a, b, e, f, d, c, g, j, h, i$ con gli archi sopra la fila.

Traccia (verificata con [[visite_di_grafi.py]]):

| Vertice | $d$ | $f$ | Lista dopo l'inserimento in testa |
|---|---|---|---|
| $i$ | 4 | 5 | $i$ |
| $h$ | 3 | 6 | $h, i$ |
| $j$ | 9 | 10 | $j, h, i$ |
| $g$ | 8 | 11 | $g, j, h, i$ |
| $c$ | 7 | 12 | $c, g, j, h, i$ |
| $d$ | 2 | 13 | $d, c, g, j, h, i$ |
| $f$ | 16 | 17 | $f, d, c, g, j, h, i$ |
| $e$ | 15 | 18 | $e, f, d, c, g, j, h, i$ |
| $b$ | 14 | 19 | $b, e, f, d, c, g, j, h, i$ |
| $a$ | 1 | 20 | $a, b, e, f, d, c, g, j, h, i$ |

(I vertici sono in ordine di completamento.) La lista finale coincide con quella della slide.

## Correttezza · [[13 - Algoritmi di visita di un grafo.pdf#page=41|p. 41]]–[[13 - Algoritmi di visita di un grafo.pdf#page=43|43]]

### Derivazione — Lemma 1: un grafo orientato è aciclico se e solo se una DFS non produce back edge · [[13 - Algoritmi di visita di un grafo.pdf#page=41|p. 41]], [[13 - Algoritmi di visita di un grafo.pdf#page=42|42]]
**Fonte:** enunciato e dimostrazione nelle slide, con un esempio di DFS con timestamp.

- ($\Leftarrow$, contronominale) *Se $G$ ha un back edge, il grafo orientato è ciclico.* Se $(u, v)$ è un back edge, $v$ è un antenato di $u$ in un depth-first tree, quindi c'è un percorso da $v$ a $u$ e l'arco $u \to v$ completa il ciclo.
- ($\Rightarrow$, contronominale) *Se il grafo contiene un ciclo $c$, la DFS produce almeno un back edge.* Sia $v$ il **primo vertice di $c$ scoperto** durante la DFS e $u \to v$ l'arco che precede $v$ nel ciclo. Al tempo $d[v]$ i vertici di $c$ formano un percorso di nodi bianchi da $v$ a $u$, quindi per il [[visita-in-profondita|teorema del cammino bianco]] $u$ diventerà un discendente di $v$ e $u \to v$ un back edge.

![[13-visite-grafi-p41-topological-lemma-1a.png]]
![[13-visite-grafi-p42-topological-lemma-1b.png]]

### Derivazione — Teorema 1: Topological-Sort produce un ordinamento topologico · [[13 - Algoritmi di visita di un grafo.pdf#page=43|p. 43]]
**Fonte:** dimostrazione nella slide.

Occorre mostrare che, per ogni coppia di vertici $u$ e $v$, se c'è un arco $u \to v$ allora $f[v] < f[u]$ (così, inserendo i vertici in testa per tempi $f$ crescenti, $u$ viene prima di $v$ nella lista). Si consideri un arco $u \to v$ esplorato dalla DFS; $v$ non può essere grigio, altrimenti sarebbe un back edge, il che contraddice il lemma 1 (la slide scrive «lemma 11»: refuso). Quindi:
- se $v$ è **bianco**, $v$ diventa un discendente di $u$ e perciò $f[v] < f[u]$;
- se $v$ è **nero**, l'esplorazione di $v$ è già finita e quindi, dato che si sta ancora esplorando $u$, $f[v] < f[u]$.

![[13-visite-grafi-p43-topological-teorema.png]]

**Sanity check** ([[visite_di_grafi.py]]): sul DAG di p. 39 per ogni arco $u \to v$ vale $f[v] < f[u]$ e la DFS non produce back edge; su un grafo con il ciclo $a \to b \to c \to a$ la DFS produce un back edge $(c, a)$.
**Ipotesi:** il grafo è orientato; se contiene un ciclo non esiste ordinamento topologico (e la DFS lo rivela con un back edge).

## Complessità · [[13 - Algoritmi di visita di un grafo.pdf#page=40|p. 40]]

Il tempo di esecuzione è $\Theta(V + E)$ (slide): la DFS richiede $\Theta(V + E)$ ([[visita-in-profondita]]) e l'**inserimento di $\lvert V \rvert$ vertici nella lista richiede $O(V)$** (un inserimento in testa costa $O(1)$, [[lista-concatenata]]).

$$
T(V, E) = \Theta(V + E) + O(V) = \Theta(V + E)
$$

## Connessioni

- [[visita-in-profondita]] — fornisce i tempi di completamento
- [[visita-di-un-grafo]] — il contesto (l'ordinamento topologico è citato a p. 7)
- [[lista-concatenata]] — la lista in cui si inserisce in testa
- [[ordinamento]] — qui si ordinano i vertici di un grafo, non dati (nota a mano di p. 40)

## Fonti · [[13 - Algoritmi di visita di un grafo.pdf#page=38|p. 38]]–[[13 - Algoritmi di visita di un grafo.pdf#page=43|43]]

- [[lezione-13-algoritmi-di-visita-di-un-grafo]]

_Aggiornato: 2026-11-26 — ingest 13 - Algoritmi di visita di un grafo.pdf_

<!-- nav:inizio -->
---
**Lezione 13 · pagina 6 di 7** · ← [[visita-in-profondita|Visita in profondità (DFS)]] · [[lezioni|Indice]] · [[dijkstra|Algoritmo di Dijkstra (percorsi minimi)]] →
<!-- nav:fine -->
