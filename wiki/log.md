# Log — Algoritmi e Strutture Dati

Formato entry: `## [YYYY-MM-DD] <operazione> | <dettaglio>`
Filtra ultimi 10: `grep "^## " wiki/log.md | tail -10`

---

## [2026-09-26] setup | Wiki as inizializzato
- struttura, `.obsidian` (temi, plugin, snippet) e CLAUDE.md ricavati da wiki-asi, adattati al corso: analisi di complessità, ricorrenze, invarianti, convenzioni per lo pseudocodice, cartella `output/codice/` per le verifiche eseguibili
- 7 PDF copiati in raw/ (00–05 e a1)

## [2026-09-26] ingest | Presentazione del corso (00-Presentazione.pdf) | pagine coperte: 1-8
- fonte: [[presentazione-del-corso]]; dati del corso e modalità d'esame (p. 4, trascritta dall'immagine) riportati anche in CLAUDE.md e overview

## [2026-09-26] ingest | Introduzione — concetti fondamentali (01-Introduzione.pdf) | pagine coperte: 1-60
- fonte: [[lezione-01-introduzione]]
- concetti creati (5): algoritmo-e-problema, efficienza-degli-algoritmi, metodi-euristici, ricerca-combinatoria, ricerca-di-controesempi (gli ultimi tre completati con la L03)
- entità create (10): ordinamento, robot-tour-optimization, movie-scheduling, nearest-neighbor, closest-pair, optimal-tsp, earliest-job-first, shortest-job-first, exhaustive-scheduling, optimal-scheduling
- esercizi: stima-dei-tempi-di-esecuzione (tabella vuota di p. 12 svolta), controesempi-per-euristiche
- verifiche eseguibili: tempi_crescita.py, controesempi_euristiche.py (NN 84 contro ottimo 64; ClosestPair 7.287 contro 6.240 con qualunque regola a parità; controesempi minimi per EJF e SJF; OptimalScheduling = esaustivo su tutte le istanze piccole)
- derivazioni espanse: 1000 s / 0.02 s (log in base 2), traccia NN, traccia ClosestPair, n! e 2^n, 20! in anni, 1000!, 2^100, dimostrazione per scambio di OptimalScheduling (🧩)
- note: coordinate di p. 28 lette dal grafico; refusi «earlest», «mutally»

## [2026-09-26] ingest | Notazione asintotica (02-Notazione asintotica.pdf) | pagine coperte: 1-38
- fonte: [[lezione-02-notazione-asintotica]]
- concetti creati (6): modello-ram, tempo-di-esecuzione, casi-di-complessita, notazione-asintotica, regole-di-calcolo-asintotico, dominanza-asintotica
- esercizi: dimostrazioni-notazione-asintotica, analisi-del-costo-riga-per-riga (Base, Base2)
- derivazioni espanse: costanti c e n0 per tutti gli esempi su 3n²−100n+6 (n0 = 300 per O(n³), n0 = 10⁴ per Ω(n²) con verifica a 9999), proprietà transitiva/riflessiva/simmetrica/trasposta, somma/differenza (esempi 5n² e 500n²), prodotto, limiti di dominanza, razzo contro vela, tabella di p. 36 ricalcolata
- grafici: genera_grafici_as.py (big-oh esempio, rapporto Θ, crescita funzioni, razzo/vela)
- refusi/note: C1/C2 scambiati tra p. 16 e p. 18; «anti-simmetrica» = simmetria trasposta; arrotondamenti a p. 36

## [2026-09-26] ingest | Analisi di correttezza e di complessità (03-Analisi di algoritmi.pdf) | pagine coperte: 1-34
- fonte: [[lezione-03-analisi-di-algoritmi]]
- concetti creati (6): paradigmi-di-progettazione, divide-et-impera, iterazione-e-ricorsione, invariante-di-ciclo, correttezza-per-induzione, equazioni-di-ricorrenza (+ completati ricerca-combinatoria, metodi-euristici, ricerca-di-controesempi)
- entità create (2): somma-iterativa, somma-ricorsiva
- esercizi: analisi-del-costo-riga-per-riga, risoluzione-ricorrenze, dimostrazioni-di-correttezza
- verifiche eseguibili: somma_primi_n.py (2n+4 passi, invariante con assert, T(n) = n+1 con c = 1, profondità n+1)
- derivazioni espanse: invariante con funzione variante, induzione con n(n+1)/2, srotolamento con verifica della forma generale, complessità spaziale Θ(1) contro Θ(n) (domanda lasciata aperta dalle slide)
- refusi: p. 17 «i = 0» → i = 1; p. 5 punto copiato da divide et impera

## [2026-09-26] ingest | Strutture dati elementari (04-Strutture dati elementari.pdf) | pagine coperte: 1-30
- fonte: [[lezione-04-strutture-dati-elementari]]
- concetti creati (2): tipo-di-dato-astratto, strutture-contigue-e-collegate
- entità create (5): array, array-dinamico, lista-concatenata, pila, coda
- esercizi: tracce-pila-e-coda (Figure 10.1 e 10.2)
- verifiche eseguibili: strutture_elementari.py (raddoppi = ⌈lg n⌉, copie ≤ 2n, tracce pila e coda coincidenti con le figure)
- derivazioni espanse: ⌈lg n⌉, M ≤ 2n con serie Σ i xⁱ, conteggio esatto 2^k − 1, accesso Θ(1) all'array, pseudocodice di lista/pila/coda nelle convenzioni del corso (📚 Cormen § 10.1–10.2)
- osservazione: con item_ahead di p. 19 cancellare la testa costa Θ(n), non Θ(1)

## [2026-09-26] ingest | Convenzioni per lo pseudocodice (a1-indicazioni_psuedocodice.pdf) | pagine coperte: 1-4
- fonte: [[convenzioni-per-lo-pseudocodice]]; concetto [[pseudocodice]]; regole riportate anche in CLAUDE.md

## [2026-09-26] revisione | copertura totale degli ingest del giorno
- tutte le 174 pagine dei 6 PDF ingeriti sono citate con link `[[file.pdf#page=N]]`; nessun link rotto; nessuna pagina orfana; 29 figure in raw/assets tutte incorporate; 5 grafici SVG
- 05-Insertion sort.pdf escluso dall'ingest su indicazione dell'utente (da fare)
- lezioni.md: lezioni 00–04 + a1 con percorso di lettura e argomenti in ordine di PDF

## [2026-09-26] lint | link orfani e non risolti su tutto il vault
- controllati tutti i file del vault (note, PDF, figure, SVG, script), esclusi i link nei blocchi di codice
- corretti 10 file senza link in entrata: CLAUDE.md, index, log (ora collegati da index/overview/lezioni), 05-Insertion sort.pdf (collegato da lezioni e overview), 5 script Python (citazioni `output/...` trasformate in link `[[nome.py]]` in 25 pagine + sezione in index), cache `__pycache__` eliminata e aggiunta a .gitignore
- corretto 1 link non risolto nel log (segnaposto `[[file.pdf#page=N]]` messo in codice)
- esito: 0 file orfani, 0 link non risolti; copertura delle 174 pagine PDF invariata

## [2026-09-26] riorganizzazione | lezioni.md
- ogni pagina wiki linkata una sola volta in tutto il file, nell'ordine di prima comparsa nelle slide, con le slide coperte accanto al link
- eliminati gli elenchi slide-per-slide con link ripetuti; pagine riprese in lezioni successive indicate in corsivo senza link
- aggiunto «ordine consigliato» per L01, L02, L03 (teoria prima degli esempi della somma) e L04 (confronto array/liste dopo le liste)
- regole aggiornate in CLAUDE.md (formato di lezioni.md, passo 13 dell'ingest, controlli del LINT)

## [2026-09-30] ingest | Insertion sort (05-Insertion sort.pdf) | pagine coperte: 1-33
- fonte: [[lezione-05-insertion-sort]]
- entità create (5): insertion-sort, selection-sort, substring-pattern-matching, findmatch, potenza-veloce
- concetti creati (1): logaritmi-nell-analisi
- pagine aggiornate: ordinamento (definizione p. 2, applicazioni p. 3, tabella degli algoritmi), efficienza-degli-algoritmi, invariante-di-ciclo, casi-di-complessita, dominanza-asintotica
- esercizi aggiornati: analisi-del-costo-riga-per-riga (casi 4–5), dimostrazioni-di-correttezza (casi 5–6), stima-dei-tempi-di-esecuzione (caso 5)
- pagina insertion-sort scritta con le sezioni nell'ordine delle slide (pp. 4 → 23), per seguirla durante la lezione
- verifiche eseguibili: ordinamento.py (traccia pp. 5–15 con t_j = 2, 2, 1, 5, 4; Σt_j = n−1 e n(n+1)/2−1; invariante con assert; stabilità; selection sort n(n−1)/2 confronti su ogni input), stringhe_e_logaritmi.py (findmatch: 10 confronti sull'esempio, (n−m+1)m nel caso peggiore; power ≤ 2(⌊lg n⌋+1) moltiplicazioni; H(n) − ln n → 0.577; log_{3/2} 10^6 = 34.07, lg 10^6 = 19.93)
- grafico: grafico-insertion-sort-casi.svg; 14 figure in raw/assets/05-insertion-sort-pN-*.png
- derivazioni espanse: numeri di esecuzioni della tabella di p. 17, caso migliore e peggiore con coefficienti a, b, c espliciti, conservazione dell'invariante, H(n) con integrali, cambio di base del logaritmo, O(lg n) della potenza veloce; risposte 🧩 alle domande senza soluzione (pp. 24, 26, 27, 29, 31)
- refusi/note: codice C++ di p. 23 riceve il vector per valore (ordina una copia); pseudocodice in stile Cormen 2ª ed.; esercizio 2.2.2 = Cormen 2.2-2 (la traccia dice n−1, il codice cicla fino a n); «≈ 35» di p. 33 = ⌈34.07⌉
- revisione di copertura: tutte le 33 pagine citate; ripristinati anche i link alle pagine di titolo/intestazione delle lezioni 01–04 persi con la riorganizzazione di lezioni.md; 0 file orfani, 0 link non risolti, 0 link ripetuti in lezioni.md

## [2026-09-30] query | contraddizione apparente in strutture-contigue-e-collegate (p. 21, punto 2)
- nessuna contraddizione: la slide dice che nelle liste collegate inserimenti e cancellazioni sono più semplici che negli array; la traduzione era ambigua e l'ho riscritta
- aggiunta la sezione «"Più semplice" dipende dall'operazione» con i costi per push front, push_back, insert in posizione i, cancellazione e push/pop, per array (statico/dinamico) e lista (semplice/doppia, con/senza puntatore alla coda)
