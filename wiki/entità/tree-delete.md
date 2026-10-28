---
tipo: entità
categoria: algoritmo
paradigma: "riduzione al caso con al più un figlio"
fonti_pdf: ["09-Alberi binari ricerca.pdf#page=19", "09-Alberi binari ricerca.pdf#page=20", "09-Alberi binari ricerca.pdf#page=21"]
---

# Tree-Delete (eliminazione da un BST)

## Problema risolto

Togliere il nodo $z$ dall'[[albero-binario-di-ricerca]] $T$, mantenendo la proprietà del BST.

## Idea

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=19]]

Si considerano 3 diversi casi:
- il nodo **non ha figli** ($z'$);
- il nodo ha **un solo figlio** ($z''$);
- il nodo ha **due figli** ($z'''$):
  - si cerca il **successore** $y$, che **non ha il figlio di sinistra**;
  - si taglia fuori $y$;
  - si scambiano chiave e dati satellite di $z$ con quelli di $y$.

In tutti i casi c'è **un nodo da tagliare fuori**: $z$ oppure il successore di $z$, e **ha al più un solo figlio**.

Nell'albero della slide (radice 15; 6 con figli 3 e 10; 3 con figlio 2; 10 con figli 8 e 13; 8 con figlio destro 9; 18 con figli 17 e 20): $z' = 20$, $z'' = 3$, $z''' = 6$. La nuvoletta «??» sul nodo 6 chiede che cosa debba prendere il suo posto.

![[09-alberi-binari-ricerca-p19-eliminazione-casi.png]]

> 🧩 Perché il successore di un nodo con due figli non ha figlio sinistro: è il **minimo del sottoalbero destro** ([[tree-successor]], caso 1), e il minimo si trova scendendo a sinistra finché il figlio sinistro è `NIL` ([[tree-minimum-maximum]]).

## Pseudocodice

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=20]] (riportato fedelmente, numeri di riga miei)

```
Tree-Delete (T,z)
1  if left[z]=NIL or right[z]=NIL
2     then y ← z
3     else y ← Tree-Successor (z)
4  if left[y] ≠NIL
5     then x ← left[y]
6     else x ← right[y]
7  if x ≠NIL                 // y non e' foglia
8     then p[x] ← p[y]
9  if p[y] = NIL             // y è radice
10    then root[T] ← x
11    else if y = left[p[y]]
12       then left[p[y]] ← x
13       else right[p[y]] ← x
14 if y ≠z                   // terzo caso
15    then key[z] ← key[y]
16         Copy y's satellite data into z
17 return y
```

Simboli: $z$ = nodo da eliminare; $y$ = nodo effettivamente tagliato fuori ($z$ stesso o il suo successore); $x$ = l'unico figlio di $y$, oppure `NIL`.

![[09-alberi-binari-ricerca-p20-tree-delete.png]]
*Nella figura le etichette $y'$, $y''$, $y'''$ e $x''$, $x'''$ indicano $y$ e $x$ nei tre casi: per $z'' = 3$, $y'' = 3$ e $x'' = 2$; per $z''' = 6$, $y''' = 8$ e $x''' = 9$. ([[09-Alberi binari ricerca.pdf#page=20]])*

> ⚠️ Contraddizione (di notazione): la slide mescola italiano e inglese («Copy y's satellite data into z») e usa lo stile della 2ª edizione del Cormen (`then`, `//`), non le [[pseudocodice|convenzioni del corso]].

## Esempio di esecuzione

![[animazione-tree-delete.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo sull'albero di [[09-Alberi binari ricerca.pdf#page=19]], nei tre casi uno dopo l'altro: Delete(20), poi Delete(3), poi Delete(6). $z$ è in rosa, $y$ in azzurro, $x$ in giallo.

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=21]] (fotogramma iniziale di un'animazione della slide: «caso 3, nodo con due figli: vogliamo eliminare $z = 6$ dall'albero originale»)

![[09-alberi-binari-ricerca-p21-eliminazione-6.png]]

> 🧩 Tracce mie, ciascuna sull'albero originale (verificate con [[grafi_e_alberi.py]]):

| Caso | $z$ | $y$ (righe 1–3) | $x$ (righe 4–6) | Collegamento (righe 7–13) | Righe 14–16 | Albero risultante |
|------|-----|-----------------|-----------------|---------------------------|-------------|-------------------|
| nessun figlio | 20 | 20 | `NIL` | `right[18] ← NIL` | — | 18 resta con il solo figlio 17 |
| un figlio | 3 | 3 | 2 | `p[2] ← 6`, `left[6] ← 2` | — | 2 prende il posto di 3 |
| due figli | 6 | 8 (successore) | 9 | `p[9] ← 10`, `left[10] ← 9` | `key[6] ← 8` | il nodo che conteneva 6 ora contiene 8; 9 diventa figlio sinistro di 10 |

## Correttezza

> 🧩 Derivazione mia, caso per caso:
> - **$y$ ha al più un figlio** (righe 1–3): se $z$ ha al più un figlio, $y = z$; altrimenti $y$ è il successore, che non ha figlio sinistro (vedi sopra).
> - **Taglio di $y$** (righe 4–13): il figlio $x$ di $y$ (o `NIL`) viene attaccato al padre di $y$ dallo stesso lato in cui stava $y$. Le chiavi del sottoalbero di $x$ erano già nel sottoalbero di quel lato del padre, quindi la proprietà del BST resta vera rispetto a tutti gli antenati.
> - **Terzo caso** (righe 14–16): $key[y]$ è il successore di $key[z]$, cioè la più piccola chiave del sottoalbero destro di $z$. Messa in $z$, è $\ge$ di tutte le chiavi del sottoalbero sinistro (che erano $\le key[z] \le key[y]$) e $\le$ di tutte quelle rimaste nel sottoalbero destro. La proprietà del BST vale anche in $z$.
> - **Radice:** se $y$ era la radice ($p[y] = $ `NIL`), la nuova radice è $x$ (riga 10).

## Complessità

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=20]] — «Il tempo di esecuzione è $O(h)$»

> 🧩 Derivazione mia: l'unica parte non costante è la chiamata a [[tree-successor]] della riga 3, che costa $O(h)$. Tutte le altre righe sono assegnamenti e confronti a costo costante. Totale $O(h) + O(1) = O(h)$.

## Connessioni

- [[tree-successor]] — individua il nodo da tagliare nel caso con due figli
- [[tree-minimum-maximum]] — il successore di un nodo con due figli è un minimo
- [[tree-insert]] — l'operazione inversa
- [[lista-concatenata]] — tagliare fuori un nodo con un solo figlio è come togliere un elemento da una lista: si ricollega il predecessore al successivo

## Fonti

- [[lezione-09-alberi-binari-di-ricerca]]
- [[09-Alberi binari ricerca.pdf#page=19]]–[[09-Alberi binari ricerca.pdf#page=21]]

_Aggiornato: 2026-10-28 — ingest 09-Alberi binari ricerca.pdf_

<!-- nav:inizio -->
---
**Lezione 09 · pagina 9 di 9** · ← [[tree-insert|Tree-Insert (inserimento in un BST)]] · [[lezioni|Indice]] · fine del libro →
<!-- nav:fine -->
