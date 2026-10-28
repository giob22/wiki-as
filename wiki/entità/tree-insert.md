---
tipo: entità
categoria: algoritmo
paradigma: "discesa lungo un ramo"
fonti_pdf: ["09-Alberi binari ricerca.pdf#page=16", "09-Alberi binari ricerca.pdf#page=17", "09-Alberi binari ricerca.pdf#page=18"]
---

# Tree-Insert (inserimento in un BST)

## Problema risolto

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=16]]

Inserire un nuovo nodo $z$, con $key[z]$ assegnata e $left[z] = right[z] = $ `NIL`, nell'albero $T$, rispettando la proprietà dell'[[albero-binario-di-ricerca]].

## Idea

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=16]]

Rispettando la proprietà di un albero di ricerca, l'elemento da inserire **attraversa l'albero verso il basso** a partire dalla radice. Il puntatore $x$ scende come in una ricerca; $y$ resta un passo indietro e, quando $x$ diventa `NIL`, è il nodo a cui attaccare $z$.

## Pseudocodice

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=16]] (riportato fedelmente, numeri di riga miei)

```
Tree-Insert (T,z)
1  y ← NIL
2  x ← root[T]
3  while x≠NIL
4      do y ← x
5         if key[z] < key[x]
6            then x ← left[x]
7            else x ← right[x]
8  p[z] ← y
9  if y = NIL
10    then root[T] ← z        // albero vuoto
11    else if key[z] < key[y]
12       then left[y] ← z
13       else right[y] ← z
```

![[09-alberi-binari-ricerca-p16-tree-insert.png]]

Simboli: $z$ = nodo da inserire; $x$ = nodo corrente della discesa; $y$ = padre di $x$, cioè l'ultimo nodo visitato.

## Esempio di esecuzione

![[animazione-tree-insert.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo sull'albero di [[09-Alberi binari ricerca.pdf#page=16]]: prima l'inserimento di 19 (pp. 16–17), poi quello di 10 (p. 18). $x$ è in giallo, $y$ in azzurro, il nuovo nodo $z$ in verde.

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=17]], [[09-Alberi binari ricerca.pdf#page=18]] (fotogrammi iniziali delle animazioni della slide: «inserire la chiave 19 rispettando la proprietà BST», «inserire la chiave 10 nell'albero della slide»)

![[09-alberi-binari-ricerca-p17-inserimento-19.png]]
![[09-alberi-binari-ricerca-p18-inserimento-10.png]]

> 🧩 Tracce mie (verificate con [[grafi_e_alberi.py]]):

| $key[z]$ | Discesa di $x$ | $y$ finale | Risultato |
|----------|----------------|------------|-----------|
| 19 | 15 (19 ≥ 15, destra) → 18 (destra) → 20 (19 < 20, sinistra) → `NIL` | 20 | 19 figlio **sinistro** di 20 |
| 10 | 15 (sinistra) → 6 (destra) → 7 (destra) → 13 (10 < 13, sinistra) → `NIL` | 13 | 10 figlio **sinistro** di 13 |

> ⚠️ Contraddizione (🧩): la figura di p. 18 disegna 19 come figlio destro di 18 e 20 come figlio destro di 19. È un BST valido, ma non è l'albero che si ottiene inserendo 19 con Tree-Insert nell'albero di p. 17: lì 19 diventa figlio sinistro di 20 (prima riga della tabella). L'inserimento di 10 dà lo stesso risultato nei due alberi, perché 10 scende nel sottoalbero sinistro della radice.

## Correttezza

> 🧩 Derivazione mia.
> - **Invariante** del `while`: $y$ è il padre di $x$ (o `NIL` se $x$ è la radice), e $z$ può essere attaccato nel sottoalbero di radice $x$ rispettando la proprietà del BST rispetto a tutti gli antenati già superati. Ogni passo sceglie il lato con lo stesso confronto di [[tree-search]] (righe 5–7).
> - **Conclusione:** quando $x = $ `NIL`, il posto vuoto in cui $x$ è caduto è il figlio sinistro o destro di $y$, e le righe 8–13 attaccano lì $z$. Rispetto a ogni antenato, $z$ sta dal lato scelto dal confronto, quindi la proprietà del BST resta vera.
> - **Caso limite:** albero vuoto ($root[T] = $ `NIL`): il ciclo non parte, $y = $ `NIL` e $z$ diventa la radice (riga 10).
> - Chiavi uguali vanno a **destra** (riga 7): coerente con $key[y] \ge key[x]$ nel sottoalbero destro ([[09-Alberi binari ricerca.pdf#page=7]]).

## Complessità

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=16]] — «Il tempo di esecuzione è $O(h)$»

> 🧩 Derivazione mia: ogni iterazione del `while` fa lavoro costante e porta $x$ un livello più in basso, quindi le iterazioni sono al più $h + 1$. Le righe 8–13 sono a costo costante. Totale $O(h)$. L'altezza può crescere di 1, se $z$ finisce sotto il nodo più profondo.

> 🧩 Conseguenza: inserire $n$ chiavi già **ordinate** costruisce l'albero degenere, con costo $\sum_{i=0}^{n-1} O(i) = O(n^2)$ (→ [[albero-binario-di-ricerca]] § Derivazione).

## Connessioni

- [[tree-search]] — stessa discesa, ma qui si memorizza il padre $y$
- [[albero-binario-di-ricerca]] — la proprietà conservata
- [[tree-delete]] — l'operazione inversa

## Fonti

- [[lezione-09-alberi-binari-di-ricerca]]
- [[09-Alberi binari ricerca.pdf#page=16]]–[[09-Alberi binari ricerca.pdf#page=18]]

_Aggiornato: 2026-10-28 — ingest 09-Alberi binari ricerca.pdf_

<!-- nav:inizio -->
---
**Lezione 09 · pagina 8 di 9** · ← [[tree-successor|Tree-Successor (successore di un nodo)]] · [[lezioni|Indice]] · [[tree-delete|Tree-Delete (eliminazione da un BST)]] →
<!-- nav:fine -->
