# Index — Algoritmi e Strutture Dati

## Overview
- [[overview]] — panoramica del corso, copertura
- [[log]] — registro cronologico delle operazioni sul wiki
- [[CLAUDE]] — schema e regole di manutenzione del wiki
- [[lezioni]] — **indice del libro**: le pagine lezione per lezione, nell'ordine di lettura; ogni pagina ha in fondo i link precedente · indice · successiva (generati da [[libro.py]])

## Concetti

**Fondamenti** (L01)
- [[algoritmo-e-problema]] — algoritmo, problema, istanza, correttezza, struttura dati (alta)
- [[efficienza-degli-algoritmi]] — numero di operazioni, $n^2$ contro $n\log n$ (alta)

**Progettazione** (L01, L03, L06, L07)
- [[paradigmi-di-progettazione]] — tre famiglie: tempo/qualità/scalabilità (alta)
- [[divide-et-impera]] — divide → conquer → combine; ricorrenza $aT(n/b) + D(n) + C(n)$ (alta)
- [[randomizzazione]] — scelte casuali, tempo atteso contro caso medio (media)
- [[ricerca-combinatoria]] — esaustiva, ottimo garantito, $n!$ e $2^n$ (alta)
- [[metodi-euristici]] — nessuna garanzia; algoritmi contro euristiche (alta)

**Correttezza** (L03)
- [[correttezza-parziale-e-totale]] — «se termina è giusto» contro «termina ed è giusto»; invariante/induzione + variante/misura (alta)
- [[ricerca-di-controesempi]] — incorrettezza, testing, 5 tips (alta)
- [[invariante-di-ciclo]] — inizializzazione, conservazione, conclusione, variante (alta)
- [[correttezza-per-induzione]] — misura, casi base, passo induttivo (alta)
- [[iterazione-e-ricorsione]] — confronto dei due stili (media)

**Analisi di complessità** (L02, L03, L05, L06, L07)
- [[modello-ram]] — costo unitario, niente gerarchie di memoria (alta)
- [[tempo-di-esecuzione]] — $T(n) = \sum c_i t_i(n)$; complessità spaziale (alta)
- [[casi-di-complessita]] — peggiore, migliore, medio (alta)
- [[notazione-asintotica]] — $O$, $\Omega$, $\Theta$: definizioni, esempi, proprietà (alta)
- [[regole-di-calcolo-asintotico]] — somma, differenza, costante, prodotto (media)
- [[dominanza-asintotica]] — little-o, limite, classifica di crescita, tabella dei tempi (alta)
- [[equazioni-di-ricorrenza]] — $T(n) = T(n-1) + c$, srotolamento; ricorrenze divide et impera (alta)
- [[metodo-di-sostituzione]] — ipotesi + induzione, costanti e casi base (alta)
- [[metodo-albero-di-ricorrenza]] — costo per livello × livelli, serie geometrica (alta)
- [[teorema-dell-esperto]] — $aT(n/b) + f(n)$: tre casi e gap (alta)
- [[logaritmi-nell-analisi]] — dimezzamento ripetuto, numeri armonici, la base non conta (alta)

**Strutture dati** (L04, L08, L09)
- [[tipo-di-dato-astratto]] — operazioni astratte contro implementazione (media)
- [[strutture-contigue-e-collegate]] — array contro puntatori, vantaggi delle liste (alta)

**Grafi e alberi** (L08)
- [[grafo]] — $G = (V, E)$, cammino, connessione, grado, cricca (alta)
- [[tipi-di-grafo]] — orientato, pesato, semplice, sparso, aciclico, immerso (alta)
- [[albero]] — non orientato, connesso, aciclico; $n - 1$ archi; altezza e bilanciamento (alta)

**Notazione**
- [[pseudocodice]] — convenzioni del corso (alta)

## Entità

**Problemi**
- [[ordinamento]] — sorting: definizione, applicazioni, algoritmi a confronto
- [[substring-pattern-matching]] — trovare $p$ in $t$
- [[robot-tour-optimization]] — commesso viaggiatore (TSP)
- [[movie-scheduling]] — massimo insieme di intervalli disgiunti
- [[torre-di-hanoi]] — S&T L06: $2^n - 1$ mosse, soluzione ricorsiva (🧩)
- [[massimo-sottoarray]] — S&T L06, solo rimando al libro
- [[nuts-and-bolts]] — S&T L07: $O(n^2)$ e randomizzato $O(n\log n)$ atteso (🧩)

**Algoritmi**
- [[nearest-neighbor]] — euristica TSP, $\Theta(n^2)$, sbagliata
- [[closest-pair]] — euristica TSP, sbagliata
- [[optimal-tsp]] — esaustivo, corretto, $\Theta(n\cdot n!)$
- [[earliest-job-first]] — euristica scheduling, sbagliata
- [[shortest-job-first]] — euristica scheduling, sbagliata
- [[exhaustive-scheduling]] — esaustivo, corretto, $2^n$ sottoinsiemi
- [[optimal-scheduling]] — greedy per data di fine, corretto ed efficiente
- [[somma-iterativa]] — $2n + 4 = O(n)$, spazio $\Theta(1)$
- [[somma-ricorsiva]] — $T(n) = 1 + cn$, spazio $\Theta(n)$
- [[insertion-sort]] — migliore $\Theta(n)$, peggiore $\Theta(n^2)$, sul posto, invariante
- [[selection-sort]] — $n(n-1)/2$ confronti sempre, $\Theta(n^2)$ (esercizio 2.2.2)
- [[findmatch]] — pattern matching a forza bruta, $O(nm)$
- [[potenza-veloce]] — $a^n$ con $O(\lg n)$ moltiplicazioni
- [[merge]] — fusione con sentinelle, $\Theta(n)$, invariante
- [[merge-sort]] — $\Theta(n\lg n)$ in ogni caso, non sul posto
- [[partition]] — pivot $A[r]$, quattro aree, $\Theta(n)$, invariante
- [[quicksort]] — peggiore $\Theta(n^2)$ (vettore ordinato), migliore e medio $\Theta(n\lg n)$, sul posto
- [[quicksort-randomizzato]] — pivot casuale, tempo atteso $O(n\log n)$
- [[inorder-tree-walk]] — visita in ordine, $\Theta(n)$ per sostituzione
- [[tree-search]] — ricerca ricorsiva e iterativa, $O(h)$
- [[tree-minimum-maximum]] — minimo e massimo, $O(h)$
- [[tree-successor]] — due casi, $O(h)$
- [[tree-insert]] — inserimento come foglia, $O(h)$
- [[tree-delete]] — tre casi, $O(h)$

**Strutture dati**
- [[array]] — accesso $\Theta(1)$, località
- [[array-dinamico]] — raddoppio, $\lceil\lg n\rceil$ raddoppi, $M \le 2n$
- [[lista-concatenata]] — semplice e doppia; inserimento, ricerca, cancellazione
- [[pila]] — LIFO, Push/Pop $O(1)$
- [[coda]] — FIFO, Enqueue/Dequeue $O(1)$, array circolare
- [[matrice-di-adiacenza]] — $n 	imes n$, test di un arco $O(1)$, spazio $\Theta(n^2)$
- [[liste-di-adiacenza]] — array di liste, spazio $\Theta(n + m)$, codice C
- [[coda-di-priorita]] — Insert, Find-Min/Max, Delete-Min/Max
- [[albero-binario-di-ricerca]] — proprietà del BST, operazioni $O(h)$

## Fonti
- [[presentazione-del-corso]] — 00-Presentazione.pdf, pp. 1–8
- [[lezione-01-introduzione]] — 01-Introduzione.pdf, pp. 1–60
- [[lezione-02-notazione-asintotica]] — 02-Notazione asintotica.pdf, pp. 1–38
- [[lezione-03-analisi-di-algoritmi]] — 03-Analisi di algoritmi.pdf, pp. 1–34
- [[lezione-04-strutture-dati-elementari]] — 04-Strutture dati elementari.pdf, pp. 1–30
- [[lezione-05-insertion-sort]] — 05-Insertion sort.pdf, pp. 1–33
- [[lezione-06-merge-sort]] — 06-Merge Sort (1).pdf, pp. 1–48 (versione aggiornata; la precedente [[06-Merge Sort.pdf]] di 30 pagine è sostituita)
- [[lezione-07-quicksort]] — 07-Quicksort 1.pdf, pp. 1–25 (versione aggiornata; la precedente [[07-Quicksort.pdf]] è sostituita)
- [[lezione-08-grafi-e-alberi]] — 08-Grafi e alberi.pdf, pp. 1–44
- [[lezione-09-alberi-binari-di-ricerca]] — 09-Alberi binari ricerca.pdf, pp. 1–21
- [[convenzioni-per-lo-pseudocodice]] — a1-indicazioni_psuedocodice.pdf, pp. 1–4

## Esercizi
- [[analisi-del-costo-riga-per-riga]] — tabella costo × esecuzioni (bassa)
- [[risoluzione-ricorrenze]] — srotolamento, sostituzione, albero, esperto (media)
- [[dimostrazioni-notazione-asintotica]] — costanti $c$, $n_0$; confutazioni (media)
- [[stima-dei-tempi-di-esecuzione]] — tempi e $n$ massimo, tabella di L01 p. 12 svolta (bassa)
- [[controesempi-per-euristiche]] — TSP e scheduling (media)
- [[dimostrazioni-di-correttezza]] — invariante e induzione (media)
- [[tracce-pila-e-coda]] — Figure 10.1 e 10.2 (bassa)
- [[progettazione-divide-et-impera]] — Torre di Hanoi, Nuts and Bolts (media)

## Esame
_nessun materiale ancora — lancia `prepara esame`_

## Asset
Figure in `raw/assets/` (nome `<file>-pN-descrizione.png`, 110 dpi con PyMuPDF): 2 da 00, 10 da 01, 6 da 02, 5 da 03, 6 da 04, 14 da 05, 22 da 06 (dalla versione aggiornata), 15 da 07, 22 da 08, 18 da 09.
Grafici di funzione generati (🧩) in `output/grafici/` — script [[genera_grafici_as.py]] (SVG, solo libreria standard): $3n^2-100n+6$ contro $3n^2$ e $0.01n^3$; $f(n)/n^2$ e soglia $\Theta$; crescita delle funzioni in scala log; razzo contro vela; copie dell'array dinamico; test del while di insertion sort (migliore/peggiore).
Script dei grafici: [[genera_grafici_as.py]].
Animazioni degli algoritmi (🧩) in `output/animazioni/`: 28 SVG `animazione-<algoritmo>.svg`: una per ogni pagina entità di categoria algoritmo (24), per gli algoritmi miei dei problemi [[torre-di-hanoi]] e [[nuts-and-bolts]] (3) e per la costruzione delle [[liste-di-adiacenza]] (1), incorporate in «Esempio di esecuzione».
Codice di verifica in `output/codice/`:
- [[tempi_crescita.py]] — tempi e crescita delle funzioni (L01 pp. 11–12, 33, 59; L02 p. 36)
- [[controesempi_euristiche.py]] — euristiche TSP e scheduling, ricerca esaustiva (L01)
- [[somma_primi_n.py]] — costo 2n+4, invariante, ricorrenza e profondità (L03)
- [[strutture_elementari.py]] — array dinamico, pila e coda (L04)
- [[ordinamento.py]] — insertion sort (traccia, $t_j$, invariante, stabilità) e selection sort (L05)
- [[stringhe_e_logaritmi.py]] — findmatch, potenza veloce, logaritmi, split della ricerca binaria (L05)
- [[divide_et_impera.py]] — merge, merge sort, ricorrenze di L06, partition, quicksort (anche randomizzato), Hanoi, Nuts and Bolts (L06–L07)
- [[grafi_e_alberi.py]] — liste di adiacenza, archi degli alberi, altezze, operazioni sui BST sugli alberi delle slide (L08–L09)

Navigazione a libro: [[libro.py]] legge [[lezioni]] e scrive in fondo a ogni pagina la barra precedente · indice · successiva.
_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf e 07-Quicksort.pdf_
_Aggiornato: 2026-10-10 — versione aggiornata delle slide 06-Merge Sort (1).pdf_
_Aggiornato: 2026-10-28 — ingest 08 e 09; indice delle lezioni come libro_
