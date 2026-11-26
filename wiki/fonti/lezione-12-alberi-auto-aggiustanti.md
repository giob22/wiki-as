---
tipo: fonte
titolo: "Corso di Algoritmi e Strutture Dati — Alberi auto-aggiustanti"
file_raw: "12 - Alberi auto-aggiustanti.pdf"
pagine: "1-16"
data_ingest: 2026-11-26
formato: slide-pdf
argomenti: [splay tree, splay, ricerca, inserimento, eliminazione, analisi ammortizzata, confronto con alberi rosso-neri]
---

# Lezione 12 — Alberi auto-aggiustanti (12 - Alberi auto-aggiustanti.pdf)

## Sommario · [[12 - Alberi auto-aggiustanti.pdf#page=1|p. 1]], [[12 - Alberi auto-aggiustanti.pdf#page=2|2]]

Slide del Prof. Marrone, a.a. 26/27. Gli **alberi auto-aggiustanti** (*splay trees*) sono BST senza altri vincoli: a ogni accesso l'elemento toccato viene portato nella radice con **rotazioni**, così si ottengono tempi **ammortizzati** logaritmici su una sequenza di $n$ operazioni e gli elementi più usati stanno vicino alla radice, senza memorizzare informazioni di bilanciamento. La lezione definisce l'operazione **Splay** con tre casi (figlio della radice; nonno con padre e figlio dallo stesso lato, «zig-zig»; nonno con lati opposti, «zig-zag»), poi **Splay-Tree-Search**, **-Insert** e **-Delete**. Il costo si calcolerà con l'analisi ammortizzata nelle lezioni successive. Le ultime slide (pp. 10–16) confrontano splay tree, albero rosso-nero e BST ordinario, con un esempio di Splay(17), il working set e una tabella.

## Percorso della lezione

Pagine del wiki nell'ordine di prima comparsa nelle slide (è l'ordine delle pagine di questa lezione nel libro):
1. [[splay-tree]] — pp. 2, 9–16: idea, costo ammortizzato, esempio, working set, confronto con rosso-nero e BST
2. [[splay]] — pp. 3–5: i tre casi di rotazioni
3. [[splay-tree-operazioni]] — pp. 6–8: ricerca, inserimento ed eliminazione

Già lette, riprese in questa lezione: *left-rotate* (rotazioni, lezione 11), *albero-rosso-nero* (confronto), *albero-binario-di-ricerca*, *tree-search*, *tree-insert*, *tree-delete* (lezione 09).

**Ordine consigliato.** Per capire cosa fa la struttura conviene leggere *splay* prima di *splay-tree*: le slide danno prima l'idea (p. 2), poi lo splay (pp. 3–5), poi le operazioni (pp. 6–8) e solo alla fine i confronti (pp. 10–16).

## Punti chiave · [[12 - Alberi auto-aggiustanti.pdf#page=2|p. 2]]–[[12 - Alberi auto-aggiustanti.pdf#page=9|9]], [[12 - Alberi auto-aggiustanti.pdf#page=14|p. 14]]–[[12 - Alberi auto-aggiustanti.pdf#page=16|16]]

1. Uno splay tree è un BST che a ogni accesso porta l'elemento nella radice con rotazioni; nessuna informazione di bilanciamento → [[splay-tree]].
2. Splay su $x$: caso I ($x$ figlio della radice: una rotazione), caso II ($x$ e il padre sono entrambi figli dello stesso lato: rotazione sul nonno, poi sul padre), caso III (lati opposti: rotazione sul padre, poi sul nuovo padre) → [[splay]].
3. Search: dopo la ricerca si fa lo splay del nodo trovato o della foglia su cui la ricerca è terminata; Insert: splay del nodo inserito; Delete: splay del padre di $z$ → [[splay-tree-operazioni]].
4. Il costo reale si calcola con l'analisi ammortizzata (lezioni successive); costo ammortizzato $O(\log n)$.
5. La rotazione conserva l'ordine: $A < x < B < y < C$.
6. Confronto: nessun vincitore assoluto; splay per accessi ripetuti e località temporale, rosso-nero per un limite su ogni ricerca (p. 15); tabella di p. 16.

## Refusi e note · [[12 - Alberi auto-aggiustanti.pdf#page=6|p. 6]]–[[12 - Alberi auto-aggiustanti.pdf#page=8|8]], [[12 - Alberi auto-aggiustanti.pdf#page=11|p. 11]], [[12 - Alberi auto-aggiustanti.pdf#page=12|12]]

- pp. 6–8: nel testo estratto dal PDF le righe dello pseudocodice sono in ordine mescolato; l'ordine corretto è quello delle figure (⚠️ in [[splay-tree-operazioni]]).
- p. 6: la slide scrive «Se l'albero è vuoto, non si fa nulla» (il testo estratto ha un punto in più); la riga `then x ← left[x]` è in grassetto nella figura.
- pp. 11 e 12 hanno lo stesso contenuto (l'esempio di Splay(17), «zig-zag»).
- Le slide non danno pseudocodice di Splay: è mia la traduzione dei tre casi (🧩 in [[splay]]).
- p. 13 e pp. 10–16: slide di tono riassuntivo (non in stile delle precedenti), con figure e una tabella finale.

## Concetti introdotti

[[splay-tree]], [[splay]], [[splay-tree-operazioni]].

## Domande aperte

- Il costo ammortizzato $O(\log n)$ è dichiarato ma non dimostrato: TODO alla lezione sull'analisi ammortizzata.
- La slide p. 8 non indica quale nodo $z$ si elimina: nell'animazione 🧩 si è scelto $z = 3$.

## Domande da esame

- Cos'è uno splay tree e in cosa si distingue da un albero rosso-nero? Che informazioni di bilanciamento memorizza?
- Descrivere l'operazione Splay e i tre casi, con le rotazioni di ciascuno.
- Eseguire Splay su un nodo dato di un albero (con i casi zig-zig e zig-zag).
- Come funzionano Splay-Tree-Search, Insert e Delete? Su quale nodo si fa lo splay in ciascuna, anche per una chiave assente?
- Perché ogni rotazione conserva la proprietà del BST?
- Quando conviene uno splay tree rispetto a un albero rosso-nero? Quali sono l'altezza nel caso peggiore e il costo ammortizzato di una ricerca?

_Aggiornato: 2026-11-26 — ingest 12 - Alberi auto-aggiustanti.pdf_

<!-- nav:inizio -->
---
**Lezione 12 · pagina 1 di 4** · ← [[rb-delete|RB-Delete e RB-Delete-Fixup]] · [[lezioni|Indice]] · [[splay-tree|Splay tree (albero auto-aggiustante)]] →
<!-- nav:fine -->
