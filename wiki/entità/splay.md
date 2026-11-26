---
tipo: entità
categoria: algoritmo
paradigma: "riorganizzazione con rotazioni lungo un cammino"
fonti_pdf: ["12 - Alberi auto-aggiustanti.pdf#page=3", "12 - Alberi auto-aggiustanti.pdf#page=4", "12 - Alberi auto-aggiustanti.pdf#page=5"]
---

# Splay

## Problema risolto · [[12 - Alberi auto-aggiustanti.pdf#page=3|p. 3]]

- **Input:** un [[splay-tree]] $T$ e un suo nodo $x$.
- **Output:** $T$, con le stesse chiavi nello stesso ordine, in cui $x$ è la **radice**.

L'operazione splay su un nodo $x$ consiste nell'effettuare una **serie di rotazioni** ([[left-rotate]]) che portano $x$ nella radice dell'albero.

## Idea · [[12 - Alberi auto-aggiustanti.pdf#page=3|p. 3]]–[[12 - Alberi auto-aggiustanti.pdf#page=5|5]]

Si ripetono rotazioni finché $x$ non è la radice; a ogni passo si guarda la posizione di $x$ rispetto al padre $y$ e al nonno $z$ (se esiste). Le slide distinguono tre casi, e per ciascuno dicono quali rotazioni fare.

| Caso | Posizione di $x$ | Rotazioni (in ordine) |
|---|---|---|
| **I** (p. 3) | $x$ è figlio della radice | rotazione sul padre di $x$ (che è la radice) |
| **II** (p. 4) | $x$ ha un nonno e **sia $x$ sia il padre di $x$ sono figli di sinistra (o di destra)** del proprio genitore | 1. rotazione **sul nonno** di $x$; 2. rotazione **sul padre** di $x$ |
| **III** (p. 5) | $x$ ha un nonno, $x$ è figlio di sinistra (destra) e il padre di $x$ è figlio di destra (sinistra) | 1. rotazione **sul padre** di $x$; 2. rotazione **sul nuovo padre** di $x$ (era il nonno di $x$) |

Le figure: **caso I** ($x$ figlio destro della radice $y$): Left-Rotate $(T,y)$ porta $x$ in radice, con $y$ come suo figlio sinistro. **Caso II** ($x$ figlio sinistro di $y$, figlio sinistro di $z$): Right-Rotate $(T,z)$ porta $y$ sopra $z$, poi Right-Rotate $(T,y)$ porta $x$ sopra $y$; il risultato ha $x$ in radice, $y$ come suo figlio destro e $z$ come figlio destro di $y$. **Caso III** ($x$ figlio sinistro di $y$, figlio destro di $z$): Right-Rotate $(T,y)$ porta $x$ sopra $y$, poi Left-Rotate $(T,z)$ porta $x$ sopra $z$; il risultato ha $x$ in radice con figli $z$ e $y$.

![[12-alberi-auto-aggiustanti-p3-splay-caso-1.png]]
![[12-alberi-auto-aggiustanti-p4-splay-caso-2.png]]
![[12-alberi-auto-aggiustanti-p5-splay-caso-3.png]]

## Pseudocodice · [[12 - Alberi auto-aggiustanti.pdf#page=3|p. 3]]–[[12 - Alberi auto-aggiustanti.pdf#page=5|5]]

> 📄 Le slide descrivono Splay solo con i tre casi (nessuno pseudocodice). Il codice seguente è la traduzione 🧩 mia dei tre casi; «rotazione su $y$ (x sale)» è Left-Rotate o Right-Rotate su $y$ a seconda che $x$ sia figlio destro o sinistro di $y$.

```
Splay (T,x)
1  while p[x] ≠ NIL
2      do y ← p[x]
3         z ← p[y]
4         if z = NIL                            ▷ caso I
5             then rotazione su y (x sale sopra y)
6         else if (x = left[y]) = (y = left[z]) ▷ caso II
7             then rotazione sul nonno z (y sale sopra z)
8                  rotazione sul padre y (x sale sopra y)
9         else                                  ▷ caso III
10            rotazione sul padre y (x sale sopra y)
11            rotazione sul nuovo padre z (x sale sopra z)
```

## Esempio di esecuzione · [[12 - Alberi auto-aggiustanti.pdf#page=11|p. 11]]

![[animazione-splay.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero Splay sull'albero di p. 6: prima Splay(17), come a p. 11 (un caso III: Right-Rotate (T,18) e poi Left-Rotate (T,15)), poi Splay(13) sull'albero risultante (due casi II). Per ogni rotazione c'è un fotogramma con le righe del pseudocodice 🧩.

Traccia (verificata con [[splay_tree.py]]):

| Chiamata | Profondità di $x$ | Casi | Rotazioni | Risultato |
|---|---|---|---|---|
| Splay(17) su p. 6 | 2 | III | Right-Rotate (T,18), Left-Rotate (T,15) | radice 17, figli 15 e 18 (come a p. 11) |
| Splay(13) sull'albero precedente | 4 | II, II | Left-Rotate (T,6), Left-Rotate (T,7), Right-Rotate (T,17), Right-Rotate (T,15) | radice 13, figli 7 e 15 |
| Splay(17) di nuovo | 0 | — | nessuna | l'albero non cambia (costo $O(1)$, p. 11) |

## Correttezza · [[12 - Alberi auto-aggiustanti.pdf#page=14|p. 14]]

> 🧩 Derivazione mia.
> - **L'ordine delle chiavi non cambia:** ogni rotazione conserva la visita in ordine ($A < x < B < y < C$, p. 14), quindi anche la loro composizione; la proprietà del BST resta vera.
> - **I tre casi sono esaustivi:** un nodo $x \ne$ radice ha un padre $y$. Se $y$ è la radice non c'è nonno: caso I. Altrimenti esiste il nonno $z$ e le coppie ($x$ figlio sinistro o destro di $y$; $y$ figlio sinistro o destro di $z$) sono quattro: due con lo stesso lato (caso II, e la sua simmetrica) e due con lati opposti (caso III, e la sua simmetrica).
> - **Terminazione:** nel caso I $x$ sale di un livello; nei casi II e III di due. La profondità di $x$ scende ad ogni giro del `while`, e quando vale 0 $x$ è la radice ($p[x] = $ `NIL`).

## Complessità · [[12 - Alberi auto-aggiustanti.pdf#page=2|p. 2]], [[12 - Alberi auto-aggiustanti.pdf#page=9|9]]

La slide dichiara il costo **ammortizzato** $O(\log n)$ per operazione, che «vedremo nelle prossime lezioni» (analisi ammortizzata): non è derivato qui.

> 🧩 Costo reale di un singolo Splay (derivazione mia): il caso I fa 1 rotazione e porta $x$ su di 1 livello; i casi II e III ne fanno 2 e portano $x$ su di 2 livelli. Quindi **il numero di rotazioni è esattamente la profondità iniziale $d$ di $x$**, e ciascuna costa $O(1)$ ([[left-rotate]]): $T_{\text{Splay}} = \Theta(d)$. Nel caso peggiore $d$ può essere $n - 1$ (albero degenere): $O(n)$ per un singolo accesso, come dice il confronto di p. 16 ($O(n)$ per l'altezza nel caso peggiore). Verifica con [[splay_tree.py]]: Splay(17) ($d = 2$) fa 2 rotazioni, Splay(13) ($d = 4$) ne fa 4, la ricerca dell'ultima chiave in un albero degenere di 200 nodi ne fa 199.

**Ipotesi:** costo costante per rotazione (modello RAM); l'analisi ammortizzata sulla sequenza di operazioni è oggetto delle lezioni successive.

## Connessioni

- [[splay-tree]] — la struttura che usa Splay a ogni accesso
- [[splay-tree-operazioni]] — Search, Insert e Delete che la chiamano
- [[left-rotate]] — le rotazioni che compongono i tre casi
- [[albero-rosso-nero]] — l'altro albero con rotazioni, ma con colori e proprietà fisse

## Fonti · [[12 - Alberi auto-aggiustanti.pdf#page=3|p. 3]]–[[12 - Alberi auto-aggiustanti.pdf#page=5|5]], [[12 - Alberi auto-aggiustanti.pdf#page=11|p. 11]], [[12 - Alberi auto-aggiustanti.pdf#page=14|14]]

- [[lezione-12-alberi-auto-aggiustanti]]

_Aggiornato: 2026-11-26 — ingest 12 - Alberi auto-aggiustanti.pdf_

<!-- nav:inizio -->
---
**Lezione 12 · pagina 3 di 4** · ← [[splay-tree|Splay tree (albero auto-aggiustante)]] · [[lezioni|Indice]] · [[splay-tree-operazioni|Splay-Tree-Search, Splay-Tree-Insert e Splay-Tree-Delete]] →
<!-- nav:fine -->
