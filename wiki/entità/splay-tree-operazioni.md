---
tipo: entità
categoria: algoritmo
paradigma: "operazione del BST seguita da uno splay"
fonti_pdf: ["12 - Alberi auto-aggiustanti.pdf#page=6", "12 - Alberi auto-aggiustanti.pdf#page=7", "12 - Alberi auto-aggiustanti.pdf#page=8", "12 - Alberi auto-aggiustanti.pdf#page=9"]
---

# Splay-Tree-Search, Splay-Tree-Insert e Splay-Tree-Delete

## Problema risolto · [[12 - Alberi auto-aggiustanti.pdf#page=6|p. 6]]–[[12 - Alberi auto-aggiustanti.pdf#page=8|8]]

Le tre operazioni di un [[splay-tree]] sono quelle del BST ([[tree-search]], [[tree-insert]], [[tree-delete]]), ciascuna seguita da un'operazione [[splay]] su un nodo scelto in modo da portarlo alla radice:

| Operazione | Dopo l'operazione si fa lo splay del nodo… | Casi particolari |
|---|---|---|
| Search (p. 6) | che contiene la chiave, **oppure della foglia su cui la ricerca è terminata** | se l'albero è vuoto non si fa nulla |
| Insert (p. 7) | che contiene il nuovo elemento inserito | |
| Delete (p. 8) | che **era il padre di $z$** prima dell'eliminazione di $z$ | se il padre di $z$ è NIL ($z$ è la radice) non si fa nulla |

## Pseudocodice · [[12 - Alberi auto-aggiustanti.pdf#page=6|p. 6]], [[12 - Alberi auto-aggiustanti.pdf#page=7|7]], [[12 - Alberi auto-aggiustanti.pdf#page=8|8]]

```
Splay-Tree-Search (T,k)
1  x ← root[T]
2  while x ≠ NIL and key[x] ≠ k
3      do y ← x
4         if k < key[x]
5             then x ← left[x]
6             else x ← right[x]
7  if x ≠ NIL
8      then Splay (T,x)
9      else if root[T] ≠ NIL
10         then Splay (T,y)
11 return x

Splay-Tree-Insert (T,z)
1  Tree-Insert (z)
2  Splay (T,z)

Splay-Tree-Delete (T,z)
1  Tree-Delete (z)
2  if p[z] ≠ NIL
3      then Splay (T,p[z])
```

> ⚠️ Contraddizione (refuso di impaginazione): nel testo estratto dal PDF le righe di Splay-Tree-Search, -Insert e -Delete compaiono in ordine mescolato; l'ordine qui sopra è quello delle figure di pp. 6–8 (Insert chiama prima Tree-Insert, poi Splay). Nella figura di p. 6 la riga `then x ← left[x]` è in grassetto. I numeri di riga sono miei.

![[12-alberi-auto-aggiustanti-p6-splay-tree-search.png]]
![[12-alberi-auto-aggiustanti-p7-splay-tree-insert.png]]
![[12-alberi-auto-aggiustanti-p8-splay-tree-delete.png]]

## Esempio di esecuzione · [[12 - Alberi auto-aggiustanti.pdf#page=6|p. 6]]–[[12 - Alberi auto-aggiustanti.pdf#page=8|8]]

![[animazione-splay-tree-operazioni.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero le tre operazioni sull'albero delle slide (radice 15; 6 e 18; 3, 7, 17, 20; 2, 4, 13): ricerca della chiave **assente** 19 (si fa lo splay dell'ultimo nodo visitato, 20), inserimento di 19 (come a p. 7), cancellazione di 3 (istanza mia: le slide non indicano $z$ a p. 8).

Tracce (verificate con [[splay_tree.py]]):

| Operazione | Albero di partenza | Passi | Radice dopo | Casi dello splay |
|---|---|---|---|---|
| Search (19), assente | albero di p. 6 | la discesa 15 → 18 → 20 si ferma su NIL: $y = 20$; Splay (T,20) | 20 | II |
| Insert (19) | albero di p. 6 (19 è il nodo $z$ di p. 7) | Tree-Insert: 19 figlio sinistro di 20; Splay (T,19) | 19 | III, poi I |
| Delete (3) | albero di p. 6; $z = 3$ con figli 2 e 4 | Tree-Delete taglia il successore 4 e ne copia la chiave in $z$; $p[z] = 6$ | 6 | I (6 è figlio della radice 15) |

> 🧩 In Splay-Tree-Delete, $p[z]$ letto **dopo** Tree-Delete è ancora il padre di prima: se $z$ ha al più un figlio, $z$ viene tolto ma il suo campo $p$ non cambia; se ha due figli, $z$ resta nell'albero (riceve la chiave del successore) con lo stesso padre. Per questo la riga 3 splay-a il «padre di $z$ prima dell'eliminazione».

## Correttezza · [[12 - Alberi auto-aggiustanti.pdf#page=6|p. 6]]–[[12 - Alberi auto-aggiustanti.pdf#page=8|8]]

> 🧩 Derivazione mia. Le operazioni del BST sono corrette per [[tree-search]], [[tree-insert]] e [[tree-delete]]; [[splay]] non cambia l'insieme né l'ordine delle chiavi, quindi il risultato (il nodo restituito, l'albero con $z$ aggiunto o tolto) resta corretto. Lo splay del **padre** di $z$ in Delete è lecito perché è un nodo ancora presente nell'albero; lo splay di $y$ in Search, per una chiave assente, evita che una ricerca fallita lasci l'albero profondo: il nodo $y$ è l'ultimo toccato, quindi il più «recente».

## Complessità · [[12 - Alberi auto-aggiustanti.pdf#page=9|p. 9]]

La slide non dà il costo: «per calcolare il costo reale delle operazioni si usa un approccio noto come analisi ammortizzata (lo vedremo nelle prossime lezioni!!)». Il costo ammortizzato dichiarato a p. 2 è $O(\log n)$ per operazione.

> 🧩 Costo reale (derivazione mia): ciascuna operazione costa quanto la corrispondente del BST, $O(h)$, più lo [[splay]], che costa $\Theta(d)$ con $d$ la profondità del nodo ($d \le h$): in totale $O(h)$, quindi $O(n)$ nel caso peggiore per un singolo accesso. In Search lo splay riguarda il nodo trovato o l'ultimo visitato, la cui profondità è la lunghezza del cammino appena percorso: la ricerca e lo splay hanno lo stesso ordine di costo.

## Connessioni

- [[splay]] — l'operazione chiamata da tutte e tre
- [[splay-tree]] — la struttura
- [[tree-search]], [[tree-insert]], [[tree-delete]] — le operazioni del BST che vengono eseguite per prime

## Fonti · [[12 - Alberi auto-aggiustanti.pdf#page=6|p. 6]]–[[12 - Alberi auto-aggiustanti.pdf#page=9|9]]

- [[lezione-12-alberi-auto-aggiustanti]]

_Aggiornato: 2026-11-26 — ingest 12 - Alberi auto-aggiustanti.pdf_

<!-- nav:inizio -->
---
**Lezione 12 · pagina 4 di 4** · ← [[splay|Splay]] · [[lezioni|Indice]] · [[lezione-13-algoritmi-di-visita-di-un-grafo|Lezione 13: introduzione e riepilogo]] →
<!-- nav:fine -->
