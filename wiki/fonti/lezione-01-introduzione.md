---
tipo: fonte
titolo: "Corso di Algoritmi e Strutture Dati — Introduzione (concetti fondamentali)"
file_raw: "01-Introduzione.pdf"
pagine: "1-60"
data_ingest: 2026-09-26
formato: slide-pdf
argomenti: [algoritmo, problema, istanza, correttezza, struttura dati, efficienza, euristiche, commesso viaggiatore, movie scheduling]
---

# Lezione 01 — Introduzione (01-Introduzione.pdf)

## Sommario

La lezione motiva lo studio degli algoritmi, ne dà le definizioni di base (algoritmo, problema, istanza, correttezza, struttura dati) e mostra perché l'efficienza conta (insertion sort contro merge sort su un milione di elementi). Il cuore sono due problemi «Stop & Think» tratti da Skiena. Per il **Robot Tour Optimization** (commesso viaggiatore) due euristiche ragionevoli — nearest neighbor e closest pair — cadono su controesempi, mentre la ricerca esaustiva è corretta ma richiede $n!$ passi. Per il **Movie Scheduling** falliscono EarliestJobFirst e ShortestJobFirst, l'esaustivo sui $2^n$ sottoinsiemi è proibitivo, e alla fine una regola greedy semplice (scegliere il job che termina prima) è corretta ed efficiente. Le due *Take-Home Lesson* sono: algoritmi contro euristiche, e il fatto che la correttezza va dimostrata con cura.

## Percorso della lezione

**PDF:** [[01-Introduzione.pdf]] (pp. 1–60)

Pagine del wiki nell'ordine di prima comparsa nelle slide (è l'ordine delle pagine di questa lezione nel libro, dopo questa):
1. [[algoritmo-e-problema]] — pp. 7–10 · algoritmo, problema, istanza, correttezza, struttura dati
2. [[ordinamento]] — p. 7 · il problema d'esempio (poi p. 11: insertion sort e merge sort)
3. [[efficienza-degli-algoritmi]] — pp. 11–12 · numero di operazioni, 1000 s contro 0.02 s
4. [[stima-dei-tempi-di-esecuzione]] — esercizio di p. 12 (la tabella vuota della slide, svolta)
5. [[robot-tour-optimization]] — pp. 13–17 e 35 · il problema del commesso viaggiatore
6. [[nearest-neighbor]] — pp. 18–24 · soluzione 1 e controesempio sulla retta
7. [[closest-pair]] — pp. 25–28 · soluzione 2 e controesempio a due file
8. [[optimal-tsp]] — pp. 29–34 · soluzione 3, esaustiva: corretta ma $n!$
9. [[ricerca-combinatoria]] — pp. 29, 58–59 (e lezione 03 p. 5) · perché $n!$ e $2^n$
10. [[metodi-euristici]] — p. 35, Take-Home Lesson #1 (e lezione 03 p. 6)
11. [[movie-scheduling]] — pp. 36–37 · il problema e l'istanza con 9 film
12. [[earliest-job-first]] — pp. 38–46 · soluzione 1 e traccia
13. [[shortest-job-first]] — pp. 47–55 · soluzione 2 e traccia
14. [[exhaustive-scheduling]] — pp. 56–59 · soluzione 3, $2^n$ sottoinsiemi
15. [[optimal-scheduling]] — p. 60 · soluzione 4, corretta ed efficiente
16. [[ricerca-di-controesempi]] — p. 60, Take-Home Lesson #2 (e lezione 03 pp. 13–15)
17. [[controesempi-per-euristiche]] — esercizio riassuntivo su tutte le euristiche

**Ordine consigliato.**
Le slide sono coerenti; l'unico accorgimento è che le pagine 9, 10 e 16 (ricerca combinatoria, metodi euristici, ricerca di controesempi) contengono già le definizioni della lezione 03: leggerle qui dà il quadro generale; alla lezione 03 non vanno riaperte.

## Punti chiave

1. Il corso integrato ASD + ML: immagine a scala («Hello world → OOP → data structures → algorithms → AI & ML») ([[01-Introduzione.pdf#page=2]]).
2. «What is an algorithm?» con video ([[01-Introduzione.pdf#page=4]], [[01-Introduzione.pdf#page=5]]: youtu.be/CvSOaYi89B4); domande di motivazione ed esempi di ambiti: industria/commercio (scheduling, ottimizzazione, allocazione, logistica), Internet (routing, ricerca, sicurezza/crittografia), sistemi/ingegneria del software (sistemi operativi, compilatori, app), biologia, genomica, gaming, AI ([[01-Introduzione.pdf#page=6]]).
3. Definizioni di algoritmo, problema, istanza (esempio: ordinamento), correttezza, struttura dati ([[01-Introduzione.pdf#page=7]]–[[01-Introduzione.pdf#page=10]]) → [[algoritmo-e-problema]].
4. Efficienza = numero di operazioni in funzione della dimensione dell'input; $n^2$ contro $n\log n$; 1000 s contro 0.02 s per $n = 10^6$; terza proprietà: facilità di implementazione ([[01-Introduzione.pdf#page=11]]) → [[efficienza-degli-algoritmi]].
5. Esercizio: $n$ massimo risolvibile in un tempo $t$ per varie $f(n)$ ([[01-Introduzione.pdf#page=12]]) → [[stima-dei-tempi-di-esecuzione]].
6. Robot Tour Optimization ([[01-Introduzione.pdf#page=13]]–[[01-Introduzione.pdf#page=35]]) → [[robot-tour-optimization]], [[nearest-neighbor]], [[closest-pair]], [[optimal-tsp]].
7. *Take-Home Lesson #1*: algoritmi (sempre corretti) contro euristiche (nessuna garanzia) ([[01-Introduzione.pdf#page=35]]) → [[metodi-euristici]].
8. Movie Scheduling ([[01-Introduzione.pdf#page=36]]–[[01-Introduzione.pdf#page=60]]) → [[movie-scheduling]], [[earliest-job-first]], [[shortest-job-first]], [[exhaustive-scheduling]], [[optimal-scheduling]].
9. *Take-Home Lesson #2*: algoritmi dall'aspetto ragionevole possono essere sbagliati; la correttezza va dimostrata ([[01-Introduzione.pdf#page=60]]) → [[ricerca-di-controesempi]].

## Refusi e note

- p. 38 ss.: «earlest» → *earliest*; p. 56: «mutally» → *mutually*.
- p. 33: «1000 = …» è lasciato in sospeso; $1000! \approx 10^{2567.6}$ (🧩).
- p. 59: $2^{100} \approx 1.26\cdot10^{30}$ è un troncamento di $1.2677\cdot10^{30}$.
- p. 11: il risultato 0.02 s per merge sort presuppone il logaritmo in base 2.
- Pagina del titolo: [[01-Introduzione.pdf#page=1|1]]; intestazione di sezione «Introduzione — Concetti fondamentali»: [[01-Introduzione.pdf#page=3|3]].
- Molte pagine sono passi di animazione della stessa slide (pp. 14–35, 37–59): nel wiki sono riassunti per passi.

## Concetti introdotti

[[algoritmo-e-problema]], [[efficienza-degli-algoritmi]], [[metodi-euristici]], [[ricerca-combinatoria]], [[ricerca-di-controesempi]], [[ordinamento]], [[robot-tour-optimization]], [[movie-scheduling]], [[nearest-neighbor]], [[closest-pair]], [[optimal-tsp]], [[earliest-job-first]], [[shortest-job-first]], [[exhaustive-scheduling]], [[optimal-scheduling]]

## Domande aperte

- Le coordinate esatte dei punti di p. 28 (controesempio di ClosestPair) non sono date: nel wiki sono lette dal grafico.
- La soluzione per il commesso viaggiatore è rimandata («Ne discuteremo ….», p. 35).
- La correttezza di OptimalScheduling è affermata ma non dimostrata nella slide (dimostrazione 🧩 nel wiki).

## Domande da esame

- Definire algoritmo corretto; perché un controesempio basta a dimostrare l'incorrettezza?
- Differenza tra algoritmo ed euristica (Take-Home Lesson #1), con un esempio.
- Mostrare un controesempio per nearest neighbor / closest pair / EarliestJobFirst / ShortestJobFirst.
- Perché la ricerca esaustiva è corretta? Quanto costa per il TSP e per il movie scheduling?
- Qual è la regola corretta per il movie scheduling e perché funziona?
- Stimare i tempi di insertion sort e merge sort per $n = 10^6$.

_Aggiornato: 2026-09-26 — ingest 01-Introduzione.pdf_
_Aggiornato: 2026-10-28 — aggiunto il «Percorso della lezione» (spostato dall'indice lezioni.md)_

<!-- nav:inizio -->
---
**Lezione 01 · pagina 1 di 18** · ← [[pseudocodice|Convenzioni per lo pseudocodice]] · [[lezioni|Indice]] · [[algoritmo-e-problema|Algoritmo, problema computazionale, istanza, correttezza, struttura dati]] →
<!-- nav:fine -->
