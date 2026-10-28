---
tipo: fonte
titolo: "Corso di Algoritmi e Strutture Dati — Alberi binari di ricerca"
file_raw: "09-Alberi binari ricerca.pdf"
pagine: "1-21"
data_ingest: 2026-10-28
formato: slide-pdf
argomenti: [code di priorità, alberi binari di ricerca, visita in ordine, ricerca, minimo, massimo, successore, inserimento, eliminazione]
---

# Lezione 09 — Alberi binari di ricerca (09-Alberi binari ricerca.pdf)

## Sommario

Slide del Prof. Marrone, a.a. 26/27 ([[09-Alberi binari ricerca.pdf#page=1]]). La lezione si apre con le **code di priorità**: perché servono (inserire un job costa meno che riordinare tutto), le tre operazioni (Insert, Find-Minimum/Maximum, Delete-Minimum/Maximum) e un esempio con un array ordinato. Introduce poi gli **alberi binari di ricerca**: operazioni sugli insiemi dinamici, costo proporzionale all'altezza ($\lg n$ se completo, $n$ se degenere), e la proprietà di ordinamento delle chiavi. Segue lo pseudocodice, con figure ed esempi animati, di: **visita in ordine** ($\Theta(n)$), **ricerca** ricorsiva e iterativa, **minimo e massimo**, **successore** (due casi), **inserimento** e **eliminazione** (tre casi, con il successore che prende il posto del nodo con due figli). Tutte le operazioni tranne la visita costano $O(h)$.

## Percorso della lezione

Pagine del wiki nell'ordine di prima comparsa nelle slide (è l'ordine delle pagine di questa lezione nel libro):
1. [[coda-di-priorita]] — pp. 2–5: definizione, operazioni, esempio con array ordinato
2. [[albero-binario-di-ricerca]] — pp. 6–7: operazioni, costo $O(h)$, proprietà, rappresentazione
3. [[inorder-tree-walk]] — pp. 8–9: visita in ordine, dimostrazione di $\Theta(n)$ con il metodo di sostituzione
4. [[tree-search]] — pp. 10–11: ricerca ricorsiva e iterativa, $O(h)$ per srotolamento
5. [[tree-minimum-maximum]] — p. 12: minimo e massimo
6. [[tree-successor]] — pp. 13–15: i due casi del successore
7. [[tree-insert]] — pp. 16–18: inserimento di 19 e di 10
8. [[tree-delete]] — pp. 19–21: i tre casi dell'eliminazione

Già lette, riprese in questa lezione: *albero* (altezza e bilanciamento, lezione 08), *coda*, *pila*, *lista-concatenata*, *tipo-di-dato-astratto* (lezione 04), *metodo-di-sostituzione* ed *equazioni-di-ricorrenza* (usati per i costi).

**Ordine di lettura:** le slide sono lineari, basta seguire le pagine. *tree-successor* usa *tree-minimum-maximum*, e *tree-delete* usa *tree-successor*: l'ordine delle slide le presenta già nell'ordine giusto.

## Punti chiave

1. Una coda di priorità offre più flessibilità dell'ordinamento: un job entra in qualsiasi momento senza riordinare tutto ([[09-Alberi binari ricerca.pdf#page=2]]) → [[coda-di-priorita]].
2. Operazioni Insert, Find-Minimum/Maximum, Delete-Minimum/Maximum ([[09-Alberi binari ricerca.pdf#page=3]]); definizione come struttura dati astratta con priorità ([[09-Alberi binari ricerca.pdf#page=4]]); esempio con input 1, 5, 3, 2, 6 ([[09-Alberi binari ricerca.pdf#page=5]]).
3. Gli alberi di ricerca supportano Search, Minimum, Maximum, Predecessor, Successor, Insert, Delete; si usano come dizionario e come coda a priorità; le operazioni costano un tempo proporzionale all'altezza ([[09-Alberi binari ricerca.pdf#page=6]]) → [[albero-binario-di-ricerca]].
4. Proprietà del BST: sottoalbero sinistro $\le key[x] \le$ sottoalbero destro ([[09-Alberi binari ricerca.pdf#page=7]]).
5. Inorder-Tree-Walk stampa le chiavi in ordine crescente in tempo $\Theta(n)$ ([[09-Alberi binari ricerca.pdf#page=8]], [[09-Alberi binari ricerca.pdf#page=9]]) → [[inorder-tree-walk]].
6. Tree-Search ricorsiva e iterativa, $O(h)$ ([[09-Alberi binari ricerca.pdf#page=10]], [[09-Alberi binari ricerca.pdf#page=11]]) → [[tree-search]].
7. Tree-Minimum e Tree-Maximum, $O(h)$ ([[09-Alberi binari ricerca.pdf#page=12]]) → [[tree-minimum-maximum]].
8. Successore: minimo del sottoalbero destro, oppure il più basso antenato di cui $x$ sta nel sottoalbero sinistro; successore di 6 = 7, di 13 = 15; $O(h)$ ([[09-Alberi binari ricerca.pdf#page=13]]–[[09-Alberi binari ricerca.pdf#page=15]]) → [[tree-successor]].
9. Tree-Insert scende dalla radice e attacca $z$ come foglia; inserimenti di 19 e di 10; $O(h)$ ([[09-Alberi binari ricerca.pdf#page=16]]–[[09-Alberi binari ricerca.pdf#page=18]]) → [[tree-insert]].
10. Tree-Delete: nessun figlio, un figlio, due figli (si taglia il successore e se ne copia la chiave); $O(h)$ ([[09-Alberi binari ricerca.pdf#page=19]]–[[09-Alberi binari ricerca.pdf#page=21]]) → [[tree-delete]].

## Refusi e note

- Le pagine [[09-Alberi binari ricerca.pdf#page=9|9]], [[09-Alberi binari ricerca.pdf#page=15|15]], [[09-Alberi binari ricerca.pdf#page=17|17]], [[09-Alberi binari ricerca.pdf#page=18|18]] e [[09-Alberi binari ricerca.pdf#page=21|21]] contengono il primo fotogramma di animazioni (stato iniziale, valori correnti vuoti): l'esecuzione completa è nelle animazioni 🧩 del wiki.
- p. 9: «Dimostriamo che impiega un tempo $\Theta(n)$», senza dimostrazione: svolta 🧩 in [[inorder-tree-walk]] con il metodo di sostituzione.
- p. 6: l'altezza attesa di un BST costruito in modo aleatorio ($\lg n$) è enunciata senza dimostrazione (📚 Cormen §12.4).
- p. 18: l'albero disegnato (19 figlio destro di 18, 20 figlio destro di 19) non è il risultato dell'inserimento di 19 di p. 17, dove 19 diventa figlio sinistro di 20 (⚠️, in [[tree-insert]]).
- pp. 8–20: pseudocodice in stile Cormen 2ª ed. (`then`, `do`, `//`), diverso dalle [[pseudocodice|convenzioni del corso]].
- p. 4: la definizione di coda di priorità è in stile enciclopedico («Nella teoria delle code…»); il senso di «inserito prima» è «posto davanti nella coda».

## Concetti introdotti

[[coda-di-priorita]], [[albero-binario-di-ricerca]], [[inorder-tree-walk]], [[tree-search]], [[tree-minimum-maximum]], [[tree-successor]], [[tree-insert]], [[tree-delete]].

## Domande aperte

- Predecessor è elencato tra le operazioni (p. 6) ma non ha pseudocodice: è simmetrico a Tree-Successor (scambiando sinistra e destra), TODO se verrà trattato.
- La slide p. 6 annuncia alberi di ricerca con caso peggiore «buono» (bilanciati), senza nominarli: TODO alla lezione relativa.

## Domande da esame

- Definire la proprietà del BST; dimostrare che la visita in ordine stampa le chiavi ordinate e costa $\Theta(n)$.
- Scrivere Tree-Search ricorsiva e iterativa e dimostrare $O(h)$.
- Successore: i due casi, con un esempio su un albero dato.
- Eseguire Tree-Insert e Tree-Delete su un albero dato, nei tre casi.
- Perché le operazioni costano $O(h)$ e quanto vale $h$ nel caso migliore e peggiore?

_Aggiornato: 2026-10-28 — ingest 09-Alberi binari ricerca.pdf_

<!-- nav:inizio -->
---
**Lezione 09 · pagina 1 di 9** · ← [[albero|Albero]] · [[lezioni|Indice]] · [[coda-di-priorita|Coda di priorità]] →
<!-- nav:fine -->
