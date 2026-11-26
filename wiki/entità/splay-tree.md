---
tipo: entità
categoria: struttura-dati
fonti_pdf: ["12 - Alberi auto-aggiustanti.pdf#page=2", "12 - Alberi auto-aggiustanti.pdf#page=10", "12 - Alberi auto-aggiustanti.pdf#page=13", "12 - Alberi auto-aggiustanti.pdf#page=14", "12 - Alberi auto-aggiustanti.pdf#page=15", "12 - Alberi auto-aggiustanti.pdf#page=16"]
---

# Splay tree (albero auto-aggiustante)

## Cos'è · [[12 - Alberi auto-aggiustanti.pdf#page=2|p. 2]]

Gli **alberi auto-aggiustanti** (*splay trees*) sono [[albero-binario-di-ricerca|alberi binari di ricerca]] che **non impongono ulteriori vincoli** sulla disposizione degli elementi: nessun colore, nessuna altezza minima. L'idea (p. 2):
- ogni volta che si accede a un elemento, l'albero viene **riaggiustato in modo che quell'elemento venga posto nella radice**, con la operazione [[splay]];
- usando [[left-rotate|rotazioni]] per riaggiustare, si ottengono **tempi di esecuzione ammortizzati di tipo logaritmico** su una sequenza di $n$ operazioni;
- vantaggio pratico: gli elementi cui si accede più di frequente stanno **vicino alla radice**, quindi si accede più velocemente ad essi;
- è una struttura per insiemi ordinati (come un BST) che **si adatta automaticamente al pattern di accesso**, con costo ammortizzato $O(\log n)$ per operazione, **senza memorizzare informazioni di bilanciamento** (come i colori).

![[12-alberi-auto-aggiustanti-p2-idea.png]]

## Rappresentazione in memoria

> 🧩 È un BST: ogni nodo ha $key$, $left$, $right$ e $p$ ([[albero-binario-di-ricerca]], senza altri campi: le slide non citano né colori né altezze). Le operazioni di ricerca, inserimento e cancellazione sono quelle del BST seguite da uno splay.

## Operazioni

| Operazione | Pagina wiki | Cosa fa |
|---|---|---|
| Splay | [[splay]] | rotazioni che portano il nodo $x$ nella radice (tre casi) |
| Splay-Tree-Search | [[splay-tree-operazioni]] | ricerca, poi splay del nodo trovato o dell'ultimo visitato |
| Splay-Tree-Insert | [[splay-tree-operazioni]] | Tree-Insert, poi splay del nodo inserito |
| Splay-Tree-Delete | [[splay-tree-operazioni]] | Tree-Delete, poi splay del padre del nodo eliminato |

Il costo reale non è dato dalle slide in questa lezione: per calcolarlo si usa un'**analisi ammortizzata**, «lo vedremo nelle prossime lezioni» (p. 9).

## Un esempio di costo · [[12 - Alberi auto-aggiustanti.pdf#page=11|p. 11]], [[12 - Alberi auto-aggiustanti.pdf#page=12|12]]

Sull'albero di p. 6 (radice 15), la chiave 17 è interna: viene cercata e portata in radice con **uno zig-zag** (due rotazioni che conservano l'ordinamento delle chiavi). Dopo lo splay 17 è la radice, con 15 a sinistra (e sotto di lui il sottoalbero con 6, 3, 7, 2, 4, 13) e 18 a destra (con 20). Se 17 viene **cercato di nuovo** senza accessi intermedi, il costo è $O(1)$.

![[12-alberi-auto-aggiustanti-p11-splay-17-esempio.png]]

> 🧩 Verificato con [[splay_tree.py]]: la prima ricerca di 17 fa 2 rotazioni (un caso III), la seconda 0.

## Working set · [[12 - Alberi auto-aggiustanti.pdf#page=13|p. 13]]

La struttura si adatta alla **località temporale**: una chiave usata di recente può costare meno da ritrovare, anche quando l'albero contiene molte chiavi. Nell'esempio di sequenza di accessi A → B → C → A → A → D → A, prima dell'ultimo A è stato consultato un solo elemento distinto, D. Con $t_i$ = numero di chiavi distinte consultate dall'accesso precedente alla stessa chiave, il contributo logaritmico nel limite ammortizzato è

$$
O\bigl(1 + \log(t_i + 1)\bigr)
$$

È un limite per **sequenze**, **non** il tempo effettivo garantito per ogni singolo accesso (slide).

![[12-alberi-auto-aggiustanti-p13-working-set.png]]

## Impatto della splay · [[12 - Alberi auto-aggiustanti.pdf#page=14|p. 14]]

La forma dell'albero cambia, ma **l'ordine delle chiavi resta identico**. Nella figura una rotazione a sinistra su $x$ (con figli $A$ e $y$; $y$ ha figli $B$ e $C$) porta $y$ in alto, $x$ a sinistra con $A$ e $B$, e $C$ a destra. $B$ cambia padre ma contiene sempre chiavi fra $x$ e $y$:

$$
A < x < B < y < C
$$

La visita in ordine è invariata: per questo ogni rotazione conserva la proprietà del BST ([[left-rotate]]).

![[12-alberi-auto-aggiustanti-p14-impatto-splay.png]]

## Splay tree, albero rosso-nero e BST · [[12 - Alberi auto-aggiustanti.pdf#page=10|p. 10]], [[12 - Alberi auto-aggiustanti.pdf#page=15|15]], [[12 - Alberi auto-aggiustanti.pdf#page=16|16]]

La differenza fra splay tree e [[albero-rosso-nero]] **non è l'ordinamento BST**: è il modo in cui si ottengono buone prestazioni (p. 10).
- **Albero rosso-nero**: mantiene un'altezza logaritmica anche se cambiano le chiavi cercate.
- **Splay tree**: si riorganizza a ogni accesso portando il nodo cercato alla radice. Idea chiave: lo splay sfrutta la storia degli accessi, non impone un bilanciamento permanente.

![[12-alberi-auto-aggiustanti-p10-rosso-nero-vs-splay.png]]

Non esiste un vincitore assoluto: dipende dalle richieste dell'applicazione (p. 15).
- **Splay tree** conviene con accessi ripetuti alle stesse chiavi, accessi con forte località temporale, nessun colore o bilanciamento da memorizzare.
- **Albero rosso-nero** conviene se serve un limite per ogni ricerca, una latenza prevedibile $O(\log n)$, e se le ricerche non devono modificare l'albero.
- Rosso-nero: bilanciamento garantito. Splay: riorganizzazione adattiva alla storia degli accessi.

![[12-alberi-auto-aggiustanti-p15-splay-vs-rb.png]]

Tabella di confronto (p. 16):

| Caratteristica | BST ordinario | Albero rosso-nero | Splay tree |
|---|---|---|---|
| Rispetta l'ordinamento BST | Sì | Sì | Sì |
| Bilanciamento garantito | No | Sì | No |
| Si riorganizza dopo le ricerche | No | No | Sì |
| Altezza nel caso peggiore | $O(n)$ | $O(\log n)$ | $O(n)$ |
| Ricerca: costo ammortizzato | $O(n)$ | $O(\log n)$ | $O(\log n)$ |

![[12-alberi-auto-aggiustanti-p16-splay-vs-rb-vs-bst.png]]

> 🧩 L'altezza di uno splay tree può restare $\Theta(n)$ (nel caso peggiore) perché lo splay non bilancia permanentemente: dopo $n$ inserimenti in ordine crescente ([[splay_tree.py]] costruisce un albero di altezza 200 con 200 chiavi) una singola ricerca dell'ultima chiave costa 199 rotazioni e riduce l'altezza a 102; ma 200 ricerche in ordine crescente costano in totale 398 rotazioni (circa 2 a ricerca), a conferma del costo ammortizzato logaritmico dichiarato dalle slide.

## Connessioni

- [[splay]] — l'operazione che definisce la struttura
- [[albero-rosso-nero]] — l'altro modo di avere buone prestazioni sui BST
- [[albero-binario-di-ricerca]] — la struttura di base, con altezza fino a $n$
- [[left-rotate]] — le rotazioni usate da Splay

## Fonti · [[12 - Alberi auto-aggiustanti.pdf#page=2|p. 2]], [[12 - Alberi auto-aggiustanti.pdf#page=9|9]]–[[12 - Alberi auto-aggiustanti.pdf#page=16|16]]

- [[lezione-12-alberi-auto-aggiustanti]]

_Aggiornato: 2026-11-26 — ingest 12 - Alberi auto-aggiustanti.pdf_

<!-- nav:inizio -->
---
**Lezione 12 · pagina 2 di 4** · ← [[lezione-12-alberi-auto-aggiustanti|Lezione 12: introduzione e riepilogo]] · [[lezioni|Indice]] · [[splay|Splay]] →
<!-- nav:fine -->
