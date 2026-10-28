---
tipo: fonte
titolo: "Lecture 10: Graph Data Structures (Skiena) + slide sugli alberi"
file_raw: "08-Grafi e alberi.pdf"
pagine: "1-44"
data_ingest: 2026-10-28
formato: slide-pdf
argomenti: [grafi, tipi di grafo, cammino, connessione, grado, cricca, matrice di adiacenza, liste di adiacenza, alberi, profondità, altezza, bilanciamento]
---

# Lezione 08 — Grafi e alberi (08-Grafi e alberi.pdf)

## Sommario

Le pagine 1–36 sono le slide di S. Skiena, *Lecture 10: Graph Data Structures* ([[08-Grafi e alberi.pdf#page=1]]); le pagine 37–44 sono slide in italiano sugli alberi. La lezione definisce il **grafo** $G = (V, E)$ e mostra come modella reti stradali, circuiti, reti sociali e il web. Passa poi in rassegna i **tipi di grafo**: orientato o no, pesato o no, semplice o no, sparso o denso, ciclico o aciclico, immerso o topologico. Con il grafo delle amicizie introduce cammino e cammino minimo, connessione, grado, cricca. Presenta le due rappresentazioni, **matrice di adiacenza** e **liste di adiacenza**, le confronta e mostra l'implementazione in C delle liste (strutture, inizializzazione, lettura, inserimento di un arco). Chiude con gli **alberi**: definizione come grafo non orientato, connesso e aciclico, conseguenze ($n - 1$ archi), radice, profondità, altezza, bilanciamento ($\Theta(\log n)$ contro $\Theta(n)$) e la base del logaritmo per alberi $k$-ari.

## Percorso della lezione

Pagine del wiki nell'ordine di prima comparsa nelle slide (è l'ordine delle pagine di questa lezione nel libro):
1. [[grafo]] — pp. 2–7 (poi pp. 17–24): definizione, esempi di modellazione, terminologia dal grafo delle amicizie
2. [[tipi-di-grafo]] — pp. 8–16: le sei coppie di caratteristiche
3. [[matrice-di-adiacenza]] — pp. 25–27: definizione, appunti a mano, risposte alle domande sullo spazio
4. [[liste-di-adiacenza]] — pp. 28–36: definizione, confronto con la matrice, codice C, animazione di `insert_edge`
5. [[albero]] — pp. 37–44: definizione, conseguenze, radice, altezza, bilanciamento, base del logaritmo

Già lette, riprese in questa lezione: *lista-concatenata* (ogni lista di adiacenza è una lista concatenata), *logaritmi-nell-analisi* (la base del logaritmo, p. 43), *metodo-albero-di-ricorrenza* (alberi di ricorsione, p. 44).

**Ordine di lettura:** le slide sono lineari, basta seguire le pagine. La terminologia del grafo delle amicizie (pp. 17–24) arriva dopo i tipi di grafo, ma sta nella pagina *grafo*, che si legge per prima: le due cose sono indipendenti.

## Punti chiave

1. Un grafo $G = (V, E)$ è un insieme di vertici e un insieme di archi, coppie ordinate o non ordinate di vertici ([[08-Grafi e alberi.pdf#page=3]]) → [[grafo]].
2. Reti stradali, circuiti, reti sociali, web, flusso di controllo, similarità sono grafi ([[08-Grafi e alberi.pdf#page=4]]–[[08-Grafi e alberi.pdf#page=6]]).
3. Il tipo di grafo decide gli algoritmi appropriati ([[08-Grafi e alberi.pdf#page=9]]); orientato, pesato, semplice, sparso, aciclico (alberi e DAG), immerso ([[08-Grafi e alberi.pdf#page=10]]–[[08-Grafi e alberi.pdf#page=15]]) → [[tipi-di-grafo]].
4. Grafo delle amicizie: orientato o no, cammino e cammino minimo, connesso e fortemente connesso, grado, cricca ([[08-Grafi e alberi.pdf#page=18]]–[[08-Grafi e alberi.pdf#page=23]]).
5. Matrice di adiacenza $n \times n$ con $M[i, j] = 1$ se $(i, j) \in E$; spreca spazio sui grafi sparsi ([[08-Grafi e alberi.pdf#page=26]]) → [[matrice-di-adiacenza]].
6. Liste di adiacenza: array di puntatori a liste concatenate; test di un arco in $O(d_i)$ ([[08-Grafi e alberi.pdf#page=28]]) → [[liste-di-adiacenza]].
7. Confronto: matrici più veloci nel test di un arco e nell'inserimento/cancellazione, liste migliori per grado, memoria sui grafi piccoli, attraversamento e per la maggior parte dei problemi ([[08-Grafi e alberi.pdf#page=30]]).
8. Codice C: `edgenode`, `graph`, `initialize_graph`, `read_graph`, `insert_edge` con inserimento in testa e doppia copia degli archi non orientati ([[08-Grafi e alberi.pdf#page=31]]–[[08-Grafi e alberi.pdf#page=35]]).
9. Albero = grafo non orientato, connesso, aciclico; cammino unico, archi essenziali, $n - 1$ archi ([[08-Grafi e alberi.pdf#page=37]]–[[08-Grafi e alberi.pdf#page=39]]) → [[albero]].
10. Radice, figli, foglie; profondità, altezza, livelli ([[08-Grafi e alberi.pdf#page=40]], [[08-Grafi e alberi.pdf#page=41]]).
11. Bilanciato $h = \Theta(\log n)$, degenere $h = \Theta(n)$; percorrere un ramo costa $O(h)$ ([[08-Grafi e alberi.pdf#page=42]]).
12. Albero $k$-ario perfetto: $n = \frac{k^{h+1} - 1}{k - 1}$, $h = \log_k(n(k-1) + 1) - 1 = \Theta(\log_k n)$ ([[08-Grafi e alberi.pdf#page=43]]).
13. Alberi di cartelle, di espressione, di ricorsione: stessa struttura, interpretazioni diverse ([[08-Grafi e alberi.pdf#page=44]]).

## Annotazioni a mano

- p. 3: «strumento per formalizzare problemi, mantenere informazioni» → [[grafo]];
- p. 8: i grafi «permettono di rappresentare relazioni fra un dato e i suoi simili» → [[tipi-di-grafo]];
- p. 12: grafo «complesso» se due nodi sono collegati da due archi diretti → [[tipi-di-grafo]];
- p. 27 (pagina di soli appunti): informazioni sugli archi, «più nodi che archi → non connesso» (⚠️), matrice come bitmap, esempio $2 \times 2$ con peso → [[matrice-di-adiacenza]];
- p. 29 (pagina di soli appunti): «modalità di navigazione → come scorro il grafo partendo da un nodo» → [[liste-di-adiacenza]];
- p. 39: «la complessità spaziale dipende dalla struttura fisica → struttura dati utilizzata» → [[albero]].

## Refusi e note

- Le pagine [[08-Grafi e alberi.pdf#page=2|2]], [[08-Grafi e alberi.pdf#page=8|8]], [[08-Grafi e alberi.pdf#page=17|17]], [[08-Grafi e alberi.pdf#page=25|25]] sono titoli di sezione; [[08-Grafi e alberi.pdf#page=7|7]], [[08-Grafi e alberi.pdf#page=16|16]], [[08-Grafi e alberi.pdf#page=24|24]], [[08-Grafi e alberi.pdf#page=36|36]] contengono solo «Questions?».
- p. 1: il file si chiama «Grafi e alberi» ma le slide 1–36 sono la «Lecture 10» di Skiena; le pp. 37–44 sono aggiunte in italiano.
- p. 5: «with junctions as vertices as components as edges» (manca «and»).
- p. 28: «$N \times 1$ array of pointers» con $N$ maiuscolo, mentre il resto usa $n$ per il numero di vertici.
- p. 27: «Posso avere più nodi che archi → grafo non connesso» non è sempre vero: un albero ha $n - 1$ archi ed è connesso (⚠️, in [[matrice-di-adiacenza]]).
- p. 30: «Less memory on big graphs? matrices (small win)» vale per grafi grandi **e densi** (🧩, in [[liste-di-adiacenza]]).
- p. 19 contiene un esempio volgare tradotto in modo neutro nel wiki.

## Concetti introdotti

[[grafo]], [[tipi-di-grafo]], [[matrice-di-adiacenza]], [[liste-di-adiacenza]], [[albero]].

## Domande aperte

- La slide di p. 29 annuncia le «modalità di navigazione» (visite del grafo) senza svilupparle: TODO alla lezione sulle visite.
- Le domande di p. 26 sullo spazio (grafo non orientato, grafo sparso) non hanno risposta nelle slide: risposte 🧩 in [[matrice-di-adiacenza]].

## Domande da esame

- Definire grafo, cammino, grafo connesso e fortemente connesso, grado, cricca.
- Elencare i tipi di grafo con un esempio ciascuno.
- Confrontare matrice e liste di adiacenza: spazio, test di un arco, grado, visita, inserimento e cancellazione.
- Spiegare `insert_edge` e perché un arco non orientato compare due volte.
- Definire albero e dimostrare che ha $n - 1$ archi; profondità, altezza, bilanciamento.
- Ricavare l'altezza di un albero $k$-ario perfetto con $n$ nodi.

_Aggiornato: 2026-10-28 — ingest 08-Grafi e alberi.pdf_

<!-- nav:inizio -->
---
**Lezione 08 · pagina 1 di 6** · ← [[progettazione-divide-et-impera|Progettazione di algoritmi divide et impera]] · [[lezioni|Indice]] · [[grafo|Grafo]] →
<!-- nav:fine -->
