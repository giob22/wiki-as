---
tipo: fonte
titolo: "Corso di Algoritmi e Strutture Dati — Alberi rosso-neri"
file_raw: "11 . Alberi rosso-neri.pdf"
pagine: "1-48"
data_ingest: 2026-11-26
formato: slide-pdf
argomenti: [alberi rosso-neri, black-height, rotazioni, RB-Insert, RB-Insert-Fixup, cancellazione]
---

# Lezione 11 — Alberi rosso-neri (11 . Alberi rosso-neri.pdf)

## Sommario · [[11 . Alberi rosso-neri.pdf#page=1|p. 1]], [[11 . Alberi rosso-neri.pdf#page=2|2]]

Slide del Prof. Marrone, a.a. 26/27. La lezione motiva gli **alberi rosso-neri** con i limiti delle strutture precedenti: un heap ha altezza logaritmica ma non permette ricerche efficienti (devono esaminare tutti i nodi, $O(n)$); un BST ha operazioni $O(h)$ ma degenera in una lista se le chiavi sono inserite in ordine. Un albero rosso-nero è un BST con un colore per nodo e cinque proprietà (radice nera, foglie NIL nere, niente rosso con figli rossi, stessa black-height) che garantiscono altezza al più $2\lg(n+1)$ (teorema dimostrato per induzione sulla black-height). Seguono le **rotazioni** (Left-Rotate in $O(1)$), l'**inserimento** (RB-Insert come Tree-Insert con nodo rosso, poi RB-Insert-Fixup: invariante, tre casi in base al colore dello zio, $O(\lg n)$ con al più due rotazioni, con un esempio completo) e la **cancellazione** (come Tree-Delete, con tre casi effettivi e RB-Delete-Fixup per la foglia nera, $O(\log n)$).

## Percorso della lezione

Pagine del wiki nell'ordine di prima comparsa nelle slide (è l'ordine delle pagine di questa lezione nel libro):
1. [[albero-rosso-nero]] — pp. 2–17: perché un heap non basta, definizione, sentinella, black-height, teorema sull'altezza
2. [[left-rotate]] — pp. 18–20: rotazione a sinistra e a destra, $O(1)$
3. [[rb-insert]] — pp. 21–41: RB-Insert, RB-Insert-Fixup, invariante, casi 1–3, esempio, $O(\lg n)$
4. [[rb-delete]] — pp. 42–48: i casi della cancellazione e RB-Delete-Fixup

Già lette, riprese in questa lezione: *heap* (lezione 10), *albero-binario-di-ricerca*, *tree-insert*, *tree-delete*, *tree-successor* (lezione 09), *lista-concatenata*, *albero*, *invariante-di-ciclo*, *correttezza-per-induzione*.

**Ordine consigliato.** Le slide sono lineari: segui le pagine nell'ordine del libro. Per capire i casi del fixup conviene aver letto prima *left-rotate*.

## Punti chiave · [[11 . Alberi rosso-neri.pdf#page=2|p. 2]]–[[11 . Alberi rosso-neri.pdf#page=10|10]], [[11 . Alberi rosso-neri.pdf#page=14|p. 14]]–[[11 . Alberi rosso-neri.pdf#page=19|19]], [[11 . Alberi rosso-neri.pdf#page=21|p. 21]], [[11 . Alberi rosso-neri.pdf#page=24|24]], [[11 . Alberi rosso-neri.pdf#page=36|36]], [[11 . Alberi rosso-neri.pdf#page=42|p. 42]]–[[11 . Alberi rosso-neri.pdf#page=44|44]], [[11 . Alberi rosso-neri.pdf#page=48|48]]

1. Un heap non permette ricerche efficienti di chiavi arbitrarie; un BST può degenerare in una lista; si cerca una struttura che mantenga l'ordine del BST con altezza logaritmica garantita → [[albero-rosso-nero]].
2. Cinque proprietà: nodi rossi o neri, radice nera, foglie NIL nere, un rosso ha figli neri, stesso numero di nodi neri su ogni percorso; nessun percorso è più lungo del doppio di un altro.
3. Black-height $bh(x)$: $bh(x) \le h(x) \le 2\,bh(x)$.
4. Teorema: un albero rosso-nero con $n$ nodi interni ha altezza $h \le 2\lg(n+1)$; lemma: un sottoalbero di radice $x$ ha almeno $2^{bh(x)} - 1$ nodi interni.
5. Le rotazioni preservano le proprietà del BST e costano $O(1)$ → [[left-rotate]].
6. Inserimento: come in un BST, nodo rosso, poi RB-Insert-Fixup → [[rb-insert]]; il ciclo si ripete solo nel caso 1; al più due rotazioni; $O(\lg n)$.
7. Cancellazione: come Tree-Delete; si rimuove fisicamente un nodo con al più un figlio; tre casi effettivi; $O(\log n)$ → [[rb-delete]].

## Refusi e note · [[11 . Alberi rosso-neri.pdf#page=4|p. 4]], [[11 . Alberi rosso-neri.pdf#page=22|p. 22]], [[11 . Alberi rosso-neri.pdf#page=32|32]], [[11 . Alberi rosso-neri.pdf#page=34|34]], [[11 . Alberi rosso-neri.pdf#page=45|p. 45]]–[[11 . Alberi rosso-neri.pdf#page=47|47]]

- p. 4 (vuota), pp. 5–7, 11–13 e 28–31: fotogrammi o passi successivi della stessa slide; p. 29 e p. 41 contengono solo figure (caso 1 e schermata del visualizzatore).
- pp. 32 e 34: nel codice di RB-Insert-Fixup mancano due parentesi quadre (`right[p[p[z]]` e `color[p[p[z]]←RED`).
- p. 22: nel testo estratto dal PDF le righe di RB-Insert sono mescolate; l'ordine corretto è quello della figura (come in Tree-Insert con le modifiche in rosso).
- pp. 45–47: sono i fotogrammi iniziali di animazioni con le didascalie «Caso I/II/III»; non c'è lo svolgimento. RB-Delete-Fixup non ha pseudocodice (⚠️ ❓ in [[rb-delete]]).
- Lo pseudocodice è in stile Cormen 2ª ed., con sentinella $nil[T]$.

## Concetti introdotti

[[albero-rosso-nero]], [[left-rotate]], [[rb-insert]], [[rb-delete]].

## Domande aperte

- RB-Delete-Fixup: le slide non ne danno i casi; TODO se verranno trattati a lezione.
- Il costo $O(\lg n)$ di Successor/Predecessor è citato a p. 17 senza dimostrazione: segue da $O(h)$ e dal teorema sull'altezza.

## Domande da esame

- Perché un heap non basta per cercare una chiave e perché un BST non garantisce $O(\log n)$? Quali idee si fondono negli alberi rosso-neri?
- Elencare le cinque proprietà di un albero rosso-nero e definire la black-height.
- Dimostrare che un albero rosso-nero con $n$ nodi interni ha altezza al più $2\lg(n+1)$ (lemma sul numero minimo di nodi interni, poi $bh \ge h/2$).
- Descrivere Left-Rotate e mostrare che preserva le proprietà del BST. Costo?
- Quali proprietà può violare RB-Insert e come lo fa RB-Insert-Fixup? Distinguere i tre casi e dire quali cambiano la struttura.
- Perché il costo di RB-Insert-Fixup è $O(\lg n)$ e perché si fanno al più due rotazioni?
- Eseguire l'inserimento di una chiave in un albero rosso-nero dato.
- Quali sono i casi della cancellazione? Perché il nodo fisicamente rimosso ha al massimo un figlio e quando serve RB-Delete-Fixup?

_Aggiornato: 2026-11-26 — ingest 11 . Alberi rosso-neri.pdf_

<!-- nav:inizio -->
---
**Lezione 11 · pagina 1 di 5** · ← [[tracce-su-heap|Tracce su heap]] · [[lezioni|Indice]] · [[albero-rosso-nero|Albero rosso-nero]] →
<!-- nav:fine -->
