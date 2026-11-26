# Overview — Algoritmi e Strutture Dati · [[00-Presentazione.pdf#page=2|p. 2]]–[[00-Presentazione.pdf#page=5|5]], [[00-Presentazione.pdf#page=7|p. 7]], [[00-Presentazione.pdf#page=8|8]]

Corso della LM in Ingegneria Informatica, UNINA, a.a. 26/27 — parte ASD del corso integrato ASD + ML. Docente: Prof. Stefano Marrone. Testo: Cormen, Leiserson, Rivest, Stein, *Introduzione agli algoritmi e strutture dati*, 3ª ed.; consigliato Skiena, *The Algorithm Design Manual*. Esame: opzione A (unica seduta integrata dopo ML) o B (ASD a fine modulo + ML dopo), voto unico 50/50 → [[presentazione-del-corso]].

**Temi principali**: tecniche di analisi e strutture dati elementari; divide et impera; ricerca combinatoriale e metodi euristici; tecniche di analisi e strutture dati avanzate; programmazione dinamica; grafi.

Indice del libro (pagine nell'ordine di lettura, con navigazione precedente/successiva) → [[lezioni]] · catalogo → [[index]] · registro → [[log]]

## Argomenti coperti nel wiki

| Area | Pagine | Stato |
|---|---|---|
| Fondamenti: algoritmo, correttezza, efficienza | [[algoritmo-e-problema]], [[efficienza-degli-algoritmi]], [[ordinamento]] | completo per la fonte |
| Ordinamento elementare | [[insertion-sort]], [[selection-sort]] | completo per la fonte |
| Divide et impera e ordinamento efficiente | [[merge]], [[merge-sort]], [[partition]], [[quicksort]], [[quicksort-randomizzato]], [[randomizzazione]] | completo per la fonte (tempo atteso: dimostrazione sul libro) |
| Ricorrenze | [[metodo-di-sostituzione]], [[metodo-albero-di-ricorrenza]], [[teorema-dell-esperto]] | completo per la fonte |
| Problemi «Stop & Think» di progettazione | [[torre-di-hanoi]], [[nuts-and-bolts]], [[massimo-sottoarray]] | soluzioni mie (🧩); massimo sottoarray solo enunciato |
| Crescita delle funzioni: stringhe e logaritmi | [[substring-pattern-matching]], [[findmatch]], [[logaritmi-nell-analisi]], [[potenza-veloce]] | completo per la fonte |
| Progettazione: famiglie di approcci | [[paradigmi-di-progettazione]], [[divide-et-impera]], [[ricerca-combinatoria]], [[metodi-euristici]] | introduttivo (come nelle slide) |
| Problemi d'esempio e loro algoritmi | [[robot-tour-optimization]], [[movie-scheduling]] e 7 algoritmi | completo per la fonte |
| Correttezza | [[ricerca-di-controesempi]], [[invariante-di-ciclo]], [[correttezza-per-induzione]], [[iterazione-e-ricorsione]] | completo per la fonte |
| Analisi di complessità | [[modello-ram]], [[tempo-di-esecuzione]], [[casi-di-complessita]], [[equazioni-di-ricorrenza]], [[somma-iterativa]], [[somma-ricorsiva]] | completo per la fonte |
| Notazione asintotica | [[notazione-asintotica]], [[regole-di-calcolo-asintotico]], [[dominanza-asintotica]] | completo per la fonte |
| Strutture dati elementari | [[tipo-di-dato-astratto]], [[strutture-contigue-e-collegate]], [[array]], [[array-dinamico]], [[lista-concatenata]], [[pila]], [[coda]] | completo per la fonte |
| Grafi e alberi | [[grafo]], [[tipi-di-grafo]], [[matrice-di-adiacenza]], [[liste-di-adiacenza]], [[albero]] | completo per la fonte (visite dei grafi annunciate, non trattate) |
| Alberi binari di ricerca e code di priorità | [[coda-di-priorita]], [[albero-binario-di-ricerca]], [[inorder-tree-walk]], [[tree-search]], [[tree-minimum-maximum]], [[tree-successor]], [[tree-insert]], [[tree-delete]] | completo per la fonte |
| Pseudocodice | [[pseudocodice]] | completo |

**Filo logico finora.** Un algoritmo è corretto se termina con l'uscita giusta su **ogni** istanza ([[algoritmo-e-problema]]). La lezione 01 mostra quanto sia facile sbagliare: euristiche ragionevoli per il commesso viaggiatore e per lo scheduling cadono su controesempi, la ricerca esaustiva è corretta ma esponenziale, e solo per lo scheduling esiste una regola greedy corretta ed efficiente ([[metodi-euristici]], [[ricerca-combinatoria]], [[optimal-scheduling]]). La lezione 03 fornisce gli strumenti per stabilire la correttezza: controesempi per smentirla, invarianti e induzione per dimostrarla. L'efficienza si misura contando i passi nel [[modello-ram]] ([[tempo-di-esecuzione]]), di norma nel caso peggiore ([[casi-di-complessita]]), e si riassume con $O$, $\Omega$, $\Theta$ ([[notazione-asintotica]]). Ciò che conta è l'ordine di crescita ([[dominanza-asintotica]]): per $n$ grandi un algoritmo $n\log n$ batte qualunque macchina più veloce con un algoritmo $n^2$. La lezione 04 introduce i mattoni: array e liste, e sopra di essi pile e code con operazioni $O(1)$. La lezione 05 applica tutto a un algoritmo vero, insertion sort: correttezza con l'invariante, costo riga per riga, caso migliore lineare e caso peggiore quadratico. Aggiunge selection sort come esercizio e mostra da dove nascono i logaritmi. Le lezioni 06 e 07 passano al **divide et impera**: merge sort ottiene $\Theta(n\lg n)$ in ogni caso con un Combine lineare ([[merge]]) ma non ordina sul posto; quicksort ordina sul posto con un Divide lineare ([[partition]]) ma il suo costo dipende dal bilanciamento, da $\Theta(n\lg n)$ a $\Theta(n^2)$, e la [[randomizzazione]] del pivot rende il caso peggiore improbabile. Per analizzarli servono le ricorrenze $aT(n/b) + f(n)$, risolte per sostituzione, con l'albero di ricorrenza o con il teorema dell'esperto. La lezione 08 introduce i **grafi** (tipi, terminologia, matrice e liste di adiacenza, con costi opposti di spazio e di accesso) e gli **alberi**, il cui costo di percorrenza dipende dall'altezza: $\Theta(\log n)$ se bilanciati, $\Theta(n)$ se degeneri. La lezione 09 ci costruisce sopra gli **alberi binari di ricerca**: la proprietà di ordinamento delle chiavi fa costare $O(h)$ ricerca, minimo, successore, inserimento ed eliminazione, e $\Theta(n)$ la visita in ordine, che stampa le chiavi ordinate.

## Argomenti mancanti / da ingerire · 00-Presentazione.pdf [[00-Presentazione.pdf#page=5|p. 5]] · 05-Insertion sort.pdf [[05-Insertion sort.pdf#page=37|p. 37]] · Merge Sort [[06-Merge Sort (1).pdf#page=30|p. 28]], [[06-Merge Sort (1).pdf#page=52|p. 48]] · Quicksort [[07-Quicksort 1.pdf#page=23|p. 23]] · 04-Strutture dati elementari.pdf [[04-Strutture dati elementari.pdf#page=5|p. 5]], [[04-Strutture dati elementari.pdf#page=29|p. 29]] · 08-Grafi e alberi.pdf [[08-Grafi e alberi.pdf#page=29|p. 29]] · 09-Alberi binari ricerca.pdf [[09-Alberi binari ricerca.pdf#page=6|p. 6]]

- Syllabus del corso (link di p. 5) — TODO
- Ricerca binaria (citata in p. 32, pseudocodice non ancora presentato) — lezioni future
- S&T «Albero di ricorsione?»: solo la domanda, spunto di risposta 🧩 in [[metodo-albero-di-ricorrenza]]
- Massimo sottoarray: solo il titolo in p. 26, soluzione sul libro (cap. 4.1) — TODO se verrà trattato
- Dimostrazione del tempo atteso di quicksort randomizzato (rimandata al libro)
- Heap, tabelle hash (citati in p. 5), visite dei grafi DFS/BFS, alberi di ricerca bilanciati, programmazione dinamica — lezioni future

## Fonti ingerite

11 — [[presentazione-del-corso]], [[lezione-01-introduzione]], [[lezione-02-notazione-asintotica]], [[lezione-03-analisi-di-algoritmi]], [[lezione-04-strutture-dati-elementari]], [[lezione-05-insertion-sort]], [[lezione-06-merge-sort]], [[lezione-07-quicksort]], [[lezione-08-grafi-e-alberi]], [[lezione-09-alberi-binari-di-ricerca]], [[convenzioni-per-lo-pseudocodice]]

_Aggiornato: 2026-09-26 — ingest di tutto il materiale in raw/ tranne 05-Insertion sort.pdf_
_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_
_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf e 07-Quicksort.pdf_
_Aggiornato: 2026-10-10 — versione aggiornata delle slide 06-Merge Sort (1).pdf_
_Aggiornato: 2026-10-14 — link ripuntati alla versione aggiornata delle slide 07-Quicksort 1.pdf_
_Aggiornato: 2026-10-28 — ingest 08-Grafi e alberi.pdf e 09-Alberi binari ricerca.pdf_
