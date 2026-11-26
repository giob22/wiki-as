# Algoritmi e Strutture Dati — corso completo

Testo unico di studio del corso (LM Ingegneria Informatica, UNINA, Prof. Stefano Marrone). Contiene **solo ciò che sta nei PDF del corso**, nell'ordine delle slide: definizioni, pseudocodice, tabelle di costo, esempi, figure e le dimostrazioni svolte a mano dal docente. I passaggi che le slide saltano sono ricostruiti in una riga dove servono a seguire il discorso; le derivazioni estese, i grafici e le animazioni aggiuntivi e gli esercizi stanno nelle pagine concetto, entità ed esercizio, richiamate in fondo a ogni lezione («Approfondimenti nel wiki»).

**Come leggerlo.** Il riferimento al PDF compare solo nel titolo di ogni sezione (`p. N` apre la pagina). Le equazioni numerate sono quelle delle slide di ciascuna lezione. Il PDF di una lezione si genera con `python output/crea_pdf.py N` (file in `output/pdf/`); il sito di studio si genera da questo file con `python output/crea_sito.py`.

## Indice

| # | Lezione | PDF sorgente |
|---|---|---|
| 0 | [[#Lezione 0 — Presentazione del corso e convenzioni per lo pseudocodice\|Presentazione del corso e pseudocodice]] | 00-Presentazione.pdf, a1-indicazioni_psuedocodice.pdf |
| 1 | [[#Lezione 1 — Introduzione: concetti fondamentali\|Introduzione]] | 01-Introduzione.pdf |
| 2 | [[#Lezione 2 — Notazione asintotica\|Notazione asintotica]] | 02-Notazione asintotica.pdf |
| 3 | [[#Lezione 3 — Analisi di algoritmi\|Analisi di algoritmi]] | 03-Analisi di algoritmi.pdf |
| 4 | [[#Lezione 4 — Strutture dati elementari\|Strutture dati elementari]] | 04-Strutture dati elementari.pdf |
| 5 | [[#Lezione 5 — Insertion sort\|Insertion sort]] | 05-Insertion sort.pdf |
| 6 | [[#Lezione 6 — Merge Sort\|Merge Sort]] | 06-Merge Sort (1).pdf |
| 7 | [[#Lezione 7 — Quicksort\|Quicksort]] | 07-Quicksort 1.pdf |
| 8 | [[#Lezione 8 — Grafi e alberi\|Grafi e alberi]] | 08-Grafi e alberi.pdf |
| 9 | [[#Lezione 9 — Alberi binari di ricerca\|Alberi binari di ricerca]] | 09-Alberi binari ricerca.pdf |
| 10 | [[#Lezione 10 — Heapsort\|Heapsort]] | 10 - Heap - Heapsort.pdf |
| 11 | [[#Lezione 11 — Alberi rosso-neri\|Alberi rosso-neri]] | 11 . Alberi rosso-neri.pdf |
| 12 | [[#Lezione 12 — Alberi auto-aggiustanti\|Alberi auto-aggiustanti]] | 12 - Alberi auto-aggiustanti.pdf |
| 13 | [[#Lezione 13 — Algoritmi di visita di un grafo\|Algoritmi di visita di un grafo]] | 13 - Algoritmi di visita di un grafo.pdf |
| 14 | [[#Lezione 14 — Backpropagation\|Backpropagation]] | 14 - Backpropagation.pdf |
| 15 | [[#Lezione 15 — Backtracking\|Backtracking]] | 15 - Backtracking.pdf |

## Lezione 0 — Presentazione del corso e convenzioni per lo pseudocodice

*Fonte: 00-Presentazione.pdf (8 pagine di slide) e a1-indicazioni_psuedocodice.pdf (4 pagine, materiale di supporto).*

### Il corso integrato ASD + ML · [[00-Presentazione.pdf#page=2|p. 2]], [[00-Presentazione.pdf#page=1|p. 1]], [[a1-indicazioni_psuedocodice.pdf#page=1|p. 1]]

Corso integrato **Algorithms, Data Structures and Machine Learning**.
- **ASD:** correctness, time/space complexity, data structures, sorting, graphs, indexing.
- **ML:** classification, regression, clustering, evaluation, pipelines.
- **Bridges** (argomenti ponte): k-NN e similarity search; space-partitioning trees; computational graphs e backprop; complexity – model cost.
- I moduli si svolgono in sequenza (ASD → ML); la valutazione è unificata (50 % / 50 %).

![[00-presentazione-p2-corso-integrato-asd-ml.png]]
*Schema del corso integrato: ASD, ML e argomenti ponte.*

### Docenti, ricevimento e contatti · [[00-Presentazione.pdf#page=3|p. 3]]

Docenti: Stefano Marrone (ASD) e Carlo Sansone (ML). Ricevimento del Prof. Marrone: giovedì 14:30–16:30, Edificio 3/A, IV piano, stanza 4.19. Contatti via e-mail o Teams dall'account istituzionale (formato `nome.cognome@unina.it`). Sito del corso ASD: docenti.unina.it/stefano.marrone. Codice Teams del corso integrato: vyria8z.

### Modalità d'esame · [[00-Presentazione.pdf#page=4|p. 4]]

| Opzione | Quando | Cosa si sostiene | Requisiti/Soglie | Esito |
|---|---|---|---|---|
| A — Unica seduta | Dopo ML | **Pratica integrata** (contest ML + analisi algoritmo ASD) + **Orale integrato** (ASD+ML) | Soglia sulla pratica integrata per ammissione all'orale integrato | Voto unico (ASD 50 % + ML 50 %) |
| B — Due momenti | Fine ASD e dopo ML | **ASD:** Pratica + Orale (orale solo su ASD), unica data; **ML:** Pratica (contest) + Orale (orale solo su ML) | ASD: soglia complessiva, pratica ASD necessaria; ML: soglia pratica per accesso all'orale ML | Voto unico (ASD 50 % + ML 50 %) dopo il momento ML |

![[00-presentazione-p4-modalita-esame.png]]

### Argomenti ASD · [[00-Presentazione.pdf#page=5|p. 5]]

- Tecniche di analisi e strutture dati elementari.
- Tecniche di progettazione: divide et impera; ricerca combinatoriale, metodi euristici.
- Tecniche di analisi e strutture dati avanzate.
- Tecniche di progettazione: programmazione dinamica; grafi.

### Obiettivi formativi · [[00-Presentazione.pdf#page=6|p. 6]]

- **Analisi:** correttezza e complessità.
- **Progettazione:** principi e tecniche, strutture dati; problemi e algoritmi noti come esempio; applicazione a problemi non noti.
- Al termine del corso: analizzare correttezza e prestazioni asintotiche degli algoritmi; applicare e combinare tecniche, paradigmi e strutture dati avanzate per sintetizzare algoritmi corretti ed efficienti, anche per problemi non noti; familiarità con strutture dati e algoritmi per problemi fondamentali.

### Libri di testo · [[00-Presentazione.pdf#page=7|p. 7]], [[00-Presentazione.pdf#page=8|8]]

- **Testo di riferimento:** T. H. Cormen, C. E. Leiserson, R. L. Rivest, C. Stein, *Introduzione agli algoritmi e strutture dati*, 3ª ed., McGraw-Hill Italia (ISBN 9788838665158); slide e dispense sul canale Teams. La slide cita la prefazione del libro: il testo è pensato come un «buffet» da cui scegliere il materiale adatto al corso.
- **Testo consigliato:** S. Skiena, *The Algorithm Design Manual*, 3ª ed., Springer 2020 (ISBN-13 978-3030542559). Molte slide delle lezioni 2 e 4 sono tratte dal corso di Skiena.

### Convenzioni per lo pseudocodice · [[a1-indicazioni_psuedocodice.pdf#page=2|p. 2]]–[[a1-indicazioni_psuedocodice.pdf#page=4|4]]

Regole di scrittura dello pseudocodice fissate dal docente per le lezioni e per gli esercizi d'esame (sono le convenzioni del Cormen).

- L'**indentazione** indica la struttura dei blocchi (niente parentesi).
- I costrutti iterativi e di condizione hanno significato analogo ai linguaggi di alto livello; costrutti di controllo disponibili: **while**, **for**, **if-else**.
- La notazione $i \leftarrow j$ indica che il valore di $j$ viene **assegnato** a $i$.
- L'operatore `[]` indica sia l'accesso ai singoli elementi di un array sia l'accesso ai campi di un oggetto (per esempio `length[A]`).
- Si assume che gli **indici inizino da 1**.
- Sono disponibili i **sotto-array** (*slices*) come in Fortran, Matlab, Python: $A[i..j]$ è la porzione di array che inizia dall'$i$-esimo elemento e termina al $j$-esimo.
- Sono presenti **aggregati eterogenei** (= strutture C): l'accesso a un campo si fa sia con l'operatore `.` (`A.campo1`) sia con `[]` (`campo1[A]`); diversamente dal C, una variabile di tipo aggregato è un **puntatore alla struttura**; un puntatore non riferito ad alcuna struttura ha valore **NIL**; attenzione: `y ← x` seguito da `x.f ← 3` modifica **anche** `y`.
- I parametri **non aggregati** sono passati **per valore** alle procedure; quelli **aggregati** (strutture) **per riferimento** (come in Java). Tutte le variabili sono **locali** alla procedura descritta.
- Operatori di confronto: $<$, $\le$, $=$, $\ge$, $>$, $\ne$. Gli operatori booleani **and** e **or** sono valutati con la tecnica del **corto circuito**.
- **Commenti** mono-riga con $\triangleright$; i blocchi sono dati dall'indentazione.
- Non è necessario esplicitare il **tipo** delle variabili: può essere inferito dall'uso.
- **Funzioni di libreria:** sarà esplicitato nell'esercizio in quali casi è consentito usare «funzioni di libreria» assunte presenti (per esempio «sort»).

*Approfondimenti nel wiki: [[presentazione-del-corso]], [[convenzioni-per-lo-pseudocodice]], [[pseudocodice]]*

## Lezione 1 — Introduzione: concetti fondamentali

*Fonte: 01-Introduzione.pdf.*


### Motivazione: gli algoritmi nella vita quotidiana · [[01-Introduzione.pdf#page=4|p. 4]], [[01-Introduzione.pdf#page=5|5]], [[01-Introduzione.pdf#page=6|6]], [[01-Introduzione.pdf#page=1|p. 1]], [[01-Introduzione.pdf#page=2|p. 2]], [[01-Introduzione.pdf#page=3|p. 3]], [[01-Introduzione.pdf#page=4|p. 4]], [[01-Introduzione.pdf#page=5|p. 5]]

Domande della slide: *«What is an algorithm?»* (con un video collegato), *«What algorithms do you use in everyday life? What algorithms do you think are used by your favorite games and apps? Have you ever made an algorithm for a program? What did it do? Was it correct and efficient?»*

Alcuni esempi di campi di applicazione:
1. industria e commercio: pianificazione (*scheduling*), ottimizzazione, allocazione, logistica;
2. Internet: instradamento (*routing*), ricerca, sicurezza e crittografia;
3. ingegneria dei sistemi e del software: sistemi operativi, compilatori, applicazioni;
4. biologia;
5. genomica;
6. videogiochi;
7. intelligenza artificiale;
8. … (la slide lascia l'elenco da completare: «Tell by yourself»).

### Definizione · [[01-Introduzione.pdf#page=7|p. 7]], [[01-Introduzione.pdf#page=9|p. 9]], [[01-Introduzione.pdf#page=10|10]], [[01-Introduzione.pdf#page=6|p. 6]], [[01-Introduzione.pdf#page=8|p. 8]]

- Un **algoritmo** è una sequenza di passi computazionali che prende in *ingresso* un dato insieme di valori e produce un insieme di valori in *uscita*.
- Un algoritmo è uno strumento per risolvere un **problema computazionale** ben definito, cioè una relazione specificata tra ingresso e uscita.
- Un dato insieme di valori in ingresso costituisce un'**istanza** del problema.

- Un algoritmo è **corretto** se, **per ogni istanza** del problema, **termina** fornendo l'insieme corretto di valori in uscita.
- Un algoritmo **incorretto** potrebbe, in corrispondenza di *alcune* istanze, non terminare oppure terminare con un'uscita non corretta.
- Una **struttura dati** è una modalità di memorizzazione e organizzazione dei dati pensata per facilitare l'accesso e la manipolazione dei dati.

La slide p. 8 introduce la definizione di correttezza lasciandola in sospeso («Un algoritmo è corretto se, …..»): è la versione "a comparsa" della p. 9.

### Formule · [[01-Introduzione.pdf#page=7|p. 7]]

Il problema di esempio della fonte è l'[[ordinamento]]:

- **Input:** una sequenza di $n$ chiavi $\langle a_1, \dots, a_n \rangle$
- **Output:** la permutazione (riordinamento) $\langle a'_1, \dots, a'_n \rangle$ della sequenza d'ingresso tale che $a'_1 \le a'_2 \le \dots \le a'_n$

Simboli: $n$ = numero di chiavi (dimensione dell'istanza), $a_i$ = $i$-esima chiave in ingresso, $a'_i$ = $i$-esima chiave in uscita.

### Definizione formale · 01-Introduzione.pdf [[01-Introduzione.pdf#page=7|p. 7]] · 05-Insertion sort.pdf [[05-Insertion sort.pdf#page=2|p. 2]]

- **Problem:** Sorting
- **Input:** una sequenza di $n$ chiavi $a_1, \dots, a_n$
- **Output:** la permutazione (riordinamento) della sequenza d'ingresso $a'_1, \dots, a'_n$ tale che $a'_1 \le a'_2 \le \dots \le a'_n$

È l'esempio con cui la lezione 01 introduce le nozioni di problema computazionale e di [[algoritmo-e-problema|istanza]].

**Problema:** data una sequenza di $n$ valori di ingresso $(a_1, a_2, \dots, a_n)$, determinare una permutazione $(a'_1, a'_2, \dots, a'_n)$ della sequenza di ingresso tale che $a'_1 \le a'_2 \le \dots \le a'_n$.

### Definizione · [[01-Introduzione.pdf#page=11|p. 11]]

L'**efficienza** di un algoritmo è solitamente misurata in termini di **numero di operazioni**, espresso in funzione della **dimensione dei dati in ingresso**, richieste per produrre i dati in uscita.

Oltre a **correttezza** ed **efficienza**, una terza proprietà, non meno importante, è la **facilità di implementazione**.

### Formule · 01-Introduzione.pdf [[01-Introduzione.pdf#page=11|p. 11]] · Merge Sort [[06-Merge Sort (1).pdf#page=27|p. 27]]

Se un algoritmo esegue $f(n)$ operazioni su un'istanza di dimensione $n$ e il calcolatore esegue $v$ operazioni al secondo, il tempo è

$$ t = \frac{f(n)}{v} $$

- $n$ = dimensione dell'ingresso (per l'ordinamento: numero di elementi)
- $f(n)$ = numero di operazioni (adimensionale)
- $v$ = operazioni al secondo (nella slide $v = 10^9$ op/s)
- $t$ = tempo in secondi

Esempi della fonte: [[insertion-sort]] ha costo proporzionale a $n^2$, [[merge-sort]] a $n\log n$ (dimostrato nella lezione 06).

### Spiegazione · [[01-Introduzione.pdf#page=12|p. 12]]

L'esercizio di p. 12 chiede, per ogni funzione $f(n) \in \{\lg n, \sqrt n, n, n\lg n, n^2, n^3, 2^n, n!\}$ e per ogni tempo $t \in$ {1 secondo, minuto, ora, giorno, mese, anno, secolo}, la **massima dimensione $n$** risolvibile in tempo $t$ se l'algoritmo impiega $f(n)$ microsecondi. La tabella è vuota nella slide: è svolta in [[stima-dei-tempi-di-esecuzione]].

Il risultato chiave dello svolgimento: in un secolo un algoritmo $2^n$ risolve solo $n \approx 51$ e un algoritmo $n!$ solo $n \approx 17$; un algoritmo lineare arriva a $\sim 3 \cdot 10^{15}$. Aumentare il tempo disponibile di un fattore enorme sposta di pochissimo $n$ per le funzioni esponenziali.

### Definizione formale · [[01-Introduzione.pdf#page=13|p. 13]]–[[01-Introduzione.pdf#page=15|15]], [[01-Introduzione.pdf#page=35|p. 35]]

- **Problem:** Robot Tour Optimization
- **Input:** un insieme $S$ di $n$ punti nel piano
- **Output:** qual è il **ciclo più corto** che visita ogni punto dell'insieme $S$?

Il problema è introdotto come «S&T» (*Stop & Think*): Problema 1. Le figure delle pp. 14–15 mostrano un robot (un aspirapolvere) che deve muoversi tra le stanze di una pianta: l'obiettivo è il giro più breve. È il famoso **problema del commesso viaggiatore** (*Traveling Salesman Problem*).

### Algoritmi che lo risolvono (lezione 01) · [[01-Introduzione.pdf#page=17|p. 17]], [[01-Introduzione.pdf#page=18|18]], [[01-Introduzione.pdf#page=21|p. 21]], [[01-Introduzione.pdf#page=24|p. 24]], [[01-Introduzione.pdf#page=26|p. 26]], [[01-Introduzione.pdf#page=28|p. 28]], [[01-Introduzione.pdf#page=29|29]], [[01-Introduzione.pdf#page=33|p. 33]]–[[01-Introduzione.pdf#page=35|35]], [[01-Introduzione.pdf#page=25|p. 25]]

| Soluzione | Algoritmo | Corretto? | Efficiente? |
|---|---|---|---|
| 1 | [[nearest-neighbor]] | **no** — controesempio sulla retta | sì |
| 2 | [[closest-pair]] | **no** — controesempio a due file di punti | sì (più complessa) |
| 3 | [[optimal-tsp]] | **sì** | **no** — $n!$ permutazioni |

Figure delle istanze:

![[01-introduzione-p17-nearest-neighbor-caso-buono.png]]
*Punti su una circonferenza (p. 16–17): qui [[nearest-neighbor]] trova il giro giusto 0→1→…→8→0.*

![[01-introduzione-p21-nearest-neighbor-punti-casuali.png]]
*Punti sparsi (pp. 20–21) e giro prodotto da nearest-neighbor, con incroci evidenti.*

«Soluzione? Ne discuteremo ….»: la lezione non presenta un algoritmo corretto ed efficiente. La slide cita (Skiena) che per 20 punti nemmeno un calcolatore potente enumererebbe le $20!$ permutazioni in un giorno e che per circuiti reali con $n \approx 1000$ tutti i computer del mondo non finirebbero prima della fine dell'universo.

### Idea · [[01-Introduzione.pdf#page=18|p. 18]]

Parti da un punto e vai sempre al **punto non ancora visitato più vicino**; alla fine torna al punto di partenza.

### Pseudocodice · [[01-Introduzione.pdf#page=18|p. 18]]

```
NearestNeighbor(P)
1  Pick and visit an initial point p0 from P
2  p = p0
3  i = 0
4  While there are still unvisited points
5      i = i + 1
6      Select pi to be the closest unvisited point to p(i-1)
7      Visit pi
8  Return to p0 from p(n-1)
```

```
NEAREST-NEIGHBOR(P)            ▷ P[1..n] punti
1  n ← length[P]
2  tour[1] ← P[1]              ▷ punto iniziale
3  visitato[1] ← true
4  for i ← 2 to n
5      tour[i] ← punto non visitato più vicino a tour[i-1]
6      visitato[tour[i]] ← true
7  return tour                 ▷ il ciclo si chiude da tour[n] a tour[1]
```

### Esempio di esecuzione · [[01-Introduzione.pdf#page=16|p. 16]], [[01-Introduzione.pdf#page=17|17]], [[01-Introduzione.pdf#page=19|p. 19]]–[[01-Introduzione.pdf#page=24|24]]

**Caso buono** — punti su una circonferenza: il giro 0→1→2→…→8→0 è quello ottimo.

**Punti casuali**: il giro prodotto ha incroci, segno che non è minimo.

**Casi limite**: la slide li introduce in p. 19 (solo il titolo), mostra i punti casuali in p. 20–p. 21 e i punti sulla retta in p. 22–p. 23.

**Controesempio**: punti sulla retta con coordinate $-21, -5, -1, 0, 1, 3, 11$, partenza da $0$.

![[01-introduzione-p24-nearest-neighbor-controesempio.png]]
*Il giro di nearest-neighbor salta avanti e indietro lungo la retta.*

$$
\begin{aligned}
L_{NN} &= 1 + 2 + 4 + 8 + 16 + 32 + 21 && \text{somma delle distanze della traccia} \\
       &= 84 \\
L_{opt} &= 2\,(11 - (-21)) = 64       && \text{vai all'estremo destro e torna a quello sinistro}
\end{aligned}
$$

**Commento della fonte:** «Semplice ed efficiente ma … **completamente sbagliata!**».

### Idea · [[01-Introduzione.pdf#page=26|p. 26]]

Invece di costruire il giro da un punto, si costruiscono **catene di vertici**: all'inizio ogni punto è una catena da solo. A ogni passo si collegano con un arco i due **estremi più vicini** che appartengono a **catene distinte**; dopo $n-1$ passi resta una sola catena e si chiude il ciclo unendo i suoi due estremi. Unire solo estremi di catene distinte evita cicli prematuri e vertici di grado maggiore di 2.

### Pseudocodice · [[01-Introduzione.pdf#page=26|p. 26]]

```
ClosestPair(P)
1  Let n be the number of points in set P.
2  For i = 1 to n − 1 do
3      d = ∞
4      For each pair of endpoints (s,t) from distinct vertex chains
5          if dist(s,t) ≤ d then sm = s, tm = t, and d = dist(s,t)
6      Connect (sm, tm) by an edge
7  Connect the two endpoints by an edge
```

### Esempio di esecuzione · [[01-Introduzione.pdf#page=27|p. 27]], [[01-Introduzione.pdf#page=28|28]]

Commento della fonte: «Più complessa, ma "sembra" risolvere il problema». Sui punti della retta di [[nearest-neighbor]] funziona: trova il giro di lunghezza 64, cioè l'ottimo (🧩 verificato con lo script [[controesempi_euristiche.py]]).

**Controesempio**: sei punti su due file, A, B, C in alto e D, E, F in basso.

![[01-introduzione-p28-closest-pair-controesempio.png]]
*Due file di tre punti: la distanza verticale tra le file è minore della distanza orizzontale tra punti consecutivi.*

| Passo | Coppie di estremi candidate più vicine | Arco scelto | Catene dopo il passo |
|---|---|---|---|
| 1 | AD, BE, CF ($v = 0.88$) | AD | {A–D}, {B}, {C}, {E}, {F} |
| 2 | BE, CF (0.88) | BE | {A–D}, {B–E}, {C}, {F} |
| 3 | CF (0.88) | CF | {A–D}, {B–E}, {C–F} |
| 4 | AB, DE, BC, EF ($h = 1.12$) | AB | {D–A–B–E}, {C–F} |
| 5 | EF (1.12) | EF | {D–A–B–E–F–C} |
| chiusura | estremi D e C | DC | ciclo |

$$
\begin{aligned}
L_{CP} &= 3v + 2h + \sqrt{(2h)^2 + v^2}          && \text{AD, BE, CF; AB, EF; diagonale DC} \\
       &= 3(0.88) + 2(1.12) + \sqrt{2.24^2 + 0.88^2} \\
       &= 2.64 + 2.24 + 2.407 = 7.29 \\
L_{opt} &= 4h + 2v = 4.48 + 1.76 = 6.24          && \text{giro perimetrale A B C F E D A}
\end{aligned}
$$

### Idea · [[01-Introduzione.pdf#page=29|p. 29]]

Provare **tutti** gli ordinamenti (permutazioni) dei punti e tenere quello di costo minimo.

### Pseudocodice · [[01-Introduzione.pdf#page=29|p. 29]]

```
OptimalTSP(P)
1  d = ∞
2  For each of the n! permutations Pi of point set P
3      If (cost(Pi) ≤ d) then d = cost(Pi) and Pmin = Pi
4  Return Pmin
```

### Formule · [[01-Introduzione.pdf#page=29|p. 29]], [[01-Introduzione.pdf#page=58|p. 58]]

Le due ricerche esaustive viste nella lezione 01:

| Algoritmo | Spazio esplorato | Dimensione |
|---|---|---|
| [[optimal-tsp]] | permutazioni di $n$ punti | $n!$ |
| [[exhaustive-scheduling]] | sottoinsiemi di $n$ intervalli | $2^n$ |

### Correttezza · [[01-Introduzione.pdf#page=30|p. 30]], [[01-Introduzione.pdf#page=31|31]], [[01-Introduzione.pdf#page=34|p. 34]]

«Corretto?» → «Sì». Motivazione della fonte (Skiena): poiché si considerano tutti i possibili ordinamenti, si è garantiti di trovare il giro più breve; l'algoritmo è corretto perché sceglie il migliore tra tutte le possibilità.

### Complessità · 01-Introduzione.pdf [[01-Introduzione.pdf#page=32|p. 32]]–[[01-Introduzione.pdf#page=34|34]] · 02-Notazione asintotica.pdf [[02-Notazione asintotica.pdf#page=36|p. 36]]

«Efficiente?» → «$20! = 2{,}432{,}902{,}008{,}176{,}640{,}000$, $1000 = \dots$».

$$
T(n) = \underbrace{n!}_{\text{permutazioni}} \cdot \underbrace{\Theta(n)}_{\text{cost}(P_i):\ n \text{ distanze}} = \Theta(n \cdot n!)
$$
- $n = 20$: $20! \approx 2.43\cdot10^{18}$ permutazioni; a $10^9$ permutazioni/s servono $\approx 2.43\cdot10^{9}$ s $\approx 77$ anni (coerente con la tabella di p. 36, $n!$ con $n = 20$: 77.1 years).
- $n = 1000$ (il «1000 = …» della slide): $1000! \approx 10^{2567.6}$, un numero di 2568 cifre (calcolato con [[tempi_crescita.py]]).

«Even a powerful computer couldn't hope to enumerate all the 20! orderings of 20 points within a day».

### Definizione · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=6|p. 6]] · 01-Introduzione.pdf [[01-Introduzione.pdf#page=35|p. 35]]

I metodi euristici sono **regole pratiche** o strategie di ricerca che trovano soluzioni **«abbastanza buone»** in **tempi ragionevoli**, **senza garanzie di ottimalità**. Sono utili per problemi difficili o di grande scala, o quando il tempo è limitato.

Esempi classici: **commesso viaggiatore**, **zaino**, «…». Caratteristiche della soluzione:
- tempi in genere **polinomiali per iterazione**;
- **nessuna garanzia** di ottimalità o completezza;
- **valutazione empirica**.

> There is a fundamental difference between **algorithms**, which always produce a correct result, and **heuristics**, which may usually do a good job but without providing any guarantee.

### Spiegazione · 01-Introduzione.pdf [[01-Introduzione.pdf#page=24|p. 24]], [[01-Introduzione.pdf#page=27|p. 27]], [[01-Introduzione.pdf#page=28|28]], [[01-Introduzione.pdf#page=35|p. 35]], [[01-Introduzione.pdf#page=46|p. 46]], [[01-Introduzione.pdf#page=55|p. 55]], [[01-Introduzione.pdf#page=60|p. 60]] · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=14|p. 14]]

Un'euristica può dare il risultato giusto **molto spesso** e sembrare corretta; ma per il [[algoritmo-e-problema|concetto di correttezza]] serve che funzioni su **ogni** istanza. Le euristiche viste nella lezione 01 e la loro sorte:

| Euristica | Problema | Idea | Esito |
|---|---|---|---|
| [[nearest-neighbor]] | [[robot-tour-optimization]] | vai sempre al punto non visitato più vicino | «semplice ed efficiente ma … completamente sbagliata!» |
| [[closest-pair]] | [[robot-tour-optimization]] | unisci sempre la coppia di estremi più vicina | «più complessa, ma "sembra" risolvere il problema» — poi controesempio |
| [[earliest-job-first]] | [[movie-scheduling]] | accetta il job che inizia prima | un job lungo iniziale blocca molti altri |
| [[shortest-job-first]] | [[movie-scheduling]] | accetta il job più corto | il job più corto può bloccarne due |

Per il [[movie-scheduling]] esiste invece una regola corretta **ed** efficiente: [[optimal-scheduling]] (accetta il job che **termina** prima). Per il [[robot-tour-optimization]] (commesso viaggiatore) la slide rimanda la soluzione: «Soluzione? Ne discuteremo ….».

### Definizione formale · [[01-Introduzione.pdf#page=36|p. 36]], [[01-Introduzione.pdf#page=37|37]]

- **Problem:** Movie Scheduling Problem
- **Input:** un insieme $S$ di $n$ intervalli sulla retta
- **Output:** qual è il **più grande sottoinsieme** di intervalli **mutuamente non sovrapposti** che si può scegliere da $S$?

Introdotto come «S&T: Problema 2 — Movie scheduling». Interpretazione: ogni intervallo è il periodo di riprese di un film; un attore può lavorare a un solo film alla volta e vuole girarne il maggior numero possibile. La slide invita: «Proponete soluzioni …».

### Istanza della lezione · [[01-Introduzione.pdf#page=37|p. 37]]

![[01-introduzione-p37-movie-scheduling-istanza.png]]
*Nove intervalli (titoli di «film» a tema informatico): Tarjan of the Jungle, The Four Volume Problem, The President's Algorist, Steiner's Tree, Process Terminated, Halting State, Programming Challenges, "Discrete" Mathematics, Calculated Bets.*

### Idea e pseudocodice · [[01-Introduzione.pdf#page=38|p. 38]]

```
EarliestJobFirst(I)
1  Accept the earliest starting job j from S which does not overlap any
   previously accepted job, and repeat until no more such jobs remain.
```

(la slide scrive «earlest», refuso per *earliest*)

### Esempio di esecuzione · [[01-Introduzione.pdf#page=37|p. 37]], [[01-Introduzione.pdf#page=39|p. 39]], [[01-Introduzione.pdf#page=45|p. 45]], [[01-Introduzione.pdf#page=46|46]], [[01-Introduzione.pdf#page=40|p. 40]], [[01-Introduzione.pdf#page=41|p. 41]], [[01-Introduzione.pdf#page=42|p. 42]], [[01-Introduzione.pdf#page=43|p. 43]], [[01-Introduzione.pdf#page=44|p. 44]]

Traccia sull'istanza di p. 37, una slide per passo; ✔ = accettato, ✘ = escluso perché si sovrappone a un accettato:

| Pagina | Evento |
|---|---|
| p. 39 | ✔ The President's Algorist (inizia per primo) |
| p. 40 | ✘ Tarjan of the Jungle, ✘ Halting State, ✘ "Discrete" Mathematics |
| p. 41 | ✔ Steiner's Tree |
| p. 42 | ✘ The Four Volume Problem |
| p. 43 | ✔ Programming Challenges |
| p. 44 | ✘ Process Terminated |
| p. 45 | ✔ Calculated Bets |

Risultato: **4** film.

![[01-introduzione-p45-earliest-job-first-esito.png]]
*Esito finale di EarliestJobFirst: cerchi blu = accettati, divieti rossi = esclusi.*

Commento della fonte: «This idea makes sense, at least until we realize that accepting the earliest job might block us from taking many other jobs if that first job is long».

### Pseudocodice · [[01-Introduzione.pdf#page=47|p. 47]]

```
ShortestJobFirst(I)
1  While (S ≠ ∅) do
2      Accept the shortest possible job j from S.
3      Delete j, and any interval which intersects j from S.
```

### Esempio di esecuzione · [[01-Introduzione.pdf#page=37|p. 37]], [[01-Introduzione.pdf#page=48|p. 48]], [[01-Introduzione.pdf#page=54|p. 54]], [[01-Introduzione.pdf#page=55|55]], [[01-Introduzione.pdf#page=49|p. 49]], [[01-Introduzione.pdf#page=50|p. 50]], [[01-Introduzione.pdf#page=51|p. 51]], [[01-Introduzione.pdf#page=52|p. 52]], [[01-Introduzione.pdf#page=53|p. 53]]

Traccia sull'istanza di p. 37:

| Pagina | Evento |
|---|---|
| p. 48 | ✔ Steiner's Tree (il più corto) |
| p. 49 | ✘ Tarjan of the Jungle, ✘ The Four Volume Problem, ✘ Halting State |
| p. 50 | ✔ "Discrete" Mathematics |
| p. 51 | ✘ The President's Algorist |
| p. 52 | ✔ Calculated Bets |
| p. 53 | ✘ Process Terminated |
| p. 54 | ✔ Programming Challenges |

Risultato: **4** film. Su questa istanza entrambe le euristiche ([[earliest-job-first]] e questa) ne selezionano 4: il loro difetto emerge su istanze diverse.

![[01-introduzione-p54-shortest-job-first-esito.png]]
*Esito finale di ShortestJobFirst.*

Commento della fonte: «This idea makes sense at first. At least until we realize that accepting the shortest job might block us from taking two other jobs».

### Pseudocodice · [[01-Introduzione.pdf#page=56|p. 56]], [[01-Introduzione.pdf#page=58|p. 58]]

```
ExhaustiveScheduling(S)
1  j = 0, Smax = ∅
2  For each of the 2^n subsets Si of intervals S
3      If (Si is mutually non-overlapping) and (size(Si) > j)
4          then j = size(Si) and Smax = Si.
5  Return Smax
```

La versione di p. 56 scrive «For each subsets Si of intervals S» con parametro `I`; la p. 58 («Soluzione 3 (e mezzo…)») precisa **«of the $2^n$»** sottoinsiemi, con la nota evidenziata: «Non ci interessa delle permutazioni!! (l'ordine non è importante)».

![[01-introduzione-p58-exhaustive-scheduling-2n.png]]
*La correzione «e mezzo»: si enumerano sottoinsiemi, non permutazioni.*

### Complessità · 01-Introduzione.pdf [[01-Introduzione.pdf#page=57|p. 57]], [[01-Introduzione.pdf#page=59|p. 59]] · 02-Notazione asintotica.pdf [[02-Notazione asintotica.pdf#page=36|p. 36]]

Commento della fonte: «The slowness of this approach make it prohibitive like the exhaustive approach for the robot route»; poi «Well, $2^n$ is better than $n!$ of Problem 1 ($2^{20} \approx 1$M), … but $2^{100} \approx 1.26 \cdot 10^{30}$».

### Problema risolto · [[01-Introduzione.pdf#page=60|p. 60]]

[[movie-scheduling]] — in modo **corretto ed efficiente**.

### Pseudocodice · [[01-Introduzione.pdf#page=60|p. 60]]

```
OptimalScheduling(I)
1  While (S ≠ ∅) do
2      Accept the job j from S with the earliest completion date.
3      Delete j, and any interval which intersects j from S.
```

![[01-introduzione-p60-optimal-scheduling.png]]
*Soluzione 4 e Take-Home Lesson #2.*

### Definizione · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=13|p. 13]], [[03-Analisi di algoritmi.pdf#page=15|p. 15]] · 01-Introduzione.pdf [[01-Introduzione.pdf#page=60|p. 60]]

Per mostrare l'**incorrettezza** di un algoritmo: «Searching for **counterexamples** is the best way to disprove the correctness». Un **controesempio** è un'istanza del problema su cui l'algoritmo non termina o restituisce un'uscita sbagliata.

**Testing:** definire casi di test aiuta a scoprire malfunzionamenti, dimostrando l'incorrettezza dell'algoritmo; va usato **in congiunzione** con l'analisi formale di correttezza.

Ma **fallire** nella ricerca di un controesempio **non è garanzia** di correttezza dell'algoritmo.

> Reasonable-looking algorithms can easily be incorrect. Algorithm correctness is a property that must be carefully demonstrated.

*Approfondimenti nel wiki: [[lezione-01-introduzione]], [[algoritmo-e-problema]], [[ordinamento]], [[efficienza-degli-algoritmi]], [[stima-dei-tempi-di-esecuzione]], [[robot-tour-optimization]], [[nearest-neighbor]], [[closest-pair]], [[optimal-tsp]], [[ricerca-combinatoria]], [[metodi-euristici]], [[movie-scheduling]], [[earliest-job-first]], [[shortest-job-first]], [[exhaustive-scheduling]], [[optimal-scheduling]], [[ricerca-di-controesempi]], [[controesempi-per-euristiche]]*

## Lezione 2 — Notazione asintotica

*Fonte: 02-Notazione asintotica.pdf.*

### Definizione · 02-Notazione asintotica.pdf [[02-Notazione asintotica.pdf#page=2|p. 2]], [[02-Notazione asintotica.pdf#page=5|p. 5]], [[02-Notazione asintotica.pdf#page=6|6]] · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=21|p. 21]], [[02-Notazione asintotica.pdf#page=1|p. 1]], [[02-Notazione asintotica.pdf#page=4|p. 4]]

Gli algoritmi si possono studiare in modo **indipendente dalla macchina e dal linguaggio** perché tutte le analisi usano il **modello di calcolo RAM** (*Random Access Machine*):

- ogni operazione **«semplice»** ($+$, $-$, $=$, `if`, `call`) richiede **1 passo**;
- **cicli** e **chiamate a sottoprogrammi** *non* sono operazioni semplici: dipendono dalla dimensione dei dati e dal contenuto del sottoprogramma. «Sort» non è un'operazione a passo singolo;
- ogni **accesso alla memoria** richiede esattamente **1 passo**.

Il tempo di esecuzione di un algoritmo si misura **contando il numero di passi**.

> «This model is useful and accurate in the same sense as the flat-earth model (which *is* useful)!»

Per analizzare un algoritmo occorre definire il **modello del calcolatore**: **singolo processore**, **memoria ad accesso casuale**, **assenza di gerarchie di memoria**. Assunzione: le istruzioni **aritmetiche**, di **accesso alla memoria** e di **controllo** richiedono un **tempo costante**.

### Definizione · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=21|p. 21]], [[03-Analisi di algoritmi.pdf#page=22|22]] · 02-Notazione asintotica.pdf [[02-Notazione asintotica.pdf#page=2|p. 2]], [[02-Notazione asintotica.pdf#page=3|3]], [[02-Notazione asintotica.pdf#page=8|p. 8]]

**Analizzare** un algoritmo significa stimare le **risorse** richieste in termini di:
- **occupazione di memoria**,
- **impegno di banda**,
- **tempo di calcolo**.

- Il **tempo di esecuzione** è solitamente espresso **in funzione della dimensione dei valori in ingresso**:
  - per algoritmi di **ordinamento**: lunghezza della sequenza da ordinare;
  - per algoritmi su **grafi**: numero di vertici e numero di archi.
- Il tempo di esecuzione è dato dalla **somma dei tempi di esecuzione di ciascuna linea** dello pseudocodice (assunti **costanti**), ciascuno **moltiplicato per il numero di volte** che la linea viene eseguita.
- Ogni operazione di base (assegnamento, confronto, somma, incremento, chiamata/return) costa una costante.

Caratterizziamo l'efficienza di un algoritmo mediante il suo tempo di esecuzione. Quando la dimensione dei dati in ingresso è tale da rendere rilevante solo l'**ordine di crescita** del tempo di esecuzione, stiamo studiando l'efficienza **asintotica** di un algoritmo.

### Spiegazione · [[02-Notazione asintotica.pdf#page=7|p. 7]], [[02-Notazione asintotica.pdf#page=11|p. 11]]

Esempi della fonte (pseudocodice in stile italiano della slide):

```
ALGORITMO Base()
   SE CONDIZIONE_VERA ALLORA          // caso fortunato
       ISTR_A_1                       // 1
       ISTR_A_2                       // 2
       RESTITUISCI
   ALTRIMENTI                         // caso sfortunato
       ISTR_B_1                       // 1
       ...                            // ...
       ISTR_B_10                      // 10
       RESTITUISCI
FINE
```

```
ALGORITMO Base2(n)
   SE CONDIZIONE_VERA ALLORA          // best case
       ISTR_A_1
       ISTR_A_2
       RESTITUISCI
   ALTRIMENTI                         // worst case
       PER i = 0 .. n FAI
           ISTR_B
       FINEPER
       RESTITUISCI
FINE
```

### Definizione · [[02-Notazione asintotica.pdf#page=9|p. 9]], [[02-Notazione asintotica.pdf#page=10|10]]

- La **complessità nel caso peggiore** (*worst case*) di un algoritmo è la funzione definita dal **massimo** numero di passi eseguiti su una qualunque istanza di dimensione $n$.
- La **complessità nel caso migliore** (*best case*) è la funzione definita dal **minimo** numero di passi eseguiti su una qualunque istanza di dimensione $n$.
- La **complessità nel caso medio** (*average case*) è la funzione definita da un numero **medio** di passi eseguiti sulle istanze di dimensione $n$.

«Each of these complexities defines a numerical function: time vs. size!»

### Formule · [[02-Notazione asintotica.pdf#page=9|p. 9]]

$$
T_{worst}(n) = \max_{x \in I_n} \text{passi}(x), \qquad
T_{best}(n) = \min_{x \in I_n} \text{passi}(x), \qquad
T_{avg}(n) = \sum_{x \in I_n} \Pr[x]\, \text{passi}(x)
$$
Il caso medio richiede quindi un'**ipotesi sulla distribuzione** $\Pr[x]$ delle istanze. Per costruzione $T_{best}(n) \le T_{avg}(n) \le T_{worst}(n)$ per ogni $n$.

![[02-notazione-asintotica-p9-casi-peggiore-medio-migliore.png]]
*Per ogni dimensione $n$ i punti in verticale sono le istanze; la curva alta (worst) ne unisce i massimi, la bassa (best) i minimi, quella intermedia (average) le medie.*

### La posizione del corso · [[02-Notazione asintotica.pdf#page=12|p. 12]], [[02-Notazione asintotica.pdf#page=13|p. 13]]

- Domanda: quale sarebbe il ragionamento sull'acquisto di un **biglietto della lotteria** in base ai casi migliore, peggiore e medio?
- In generale si userà la **complessità nel caso peggiore** come misura preferita dell'efficienza.
- L'analisi del caso peggiore è in genere facile da fare e «di solito» riflette il caso medio.
- **«Assume I am asking for worst-case analysis unless otherwise specified!»**
- Gli **algoritmi randomizzati** sono di importanza crescente e richiedono un'analisi di tipo caso medio per mostrare i loro meriti.

### Definizione · [[02-Notazione asintotica.pdf#page=15|p. 15]]–[[02-Notazione asintotica.pdf#page=17|17]], [[02-Notazione asintotica.pdf#page=14|p. 14]]

I casi migliore, peggiore e medio sono difficili da trattare perché i dettagli **precisi** delle funzioni sono molto complicati. È più facile parlare di **limiti superiori e inferiori** della funzione. Le notazioni asintotiche ($O$, $\Theta$, $\Omega$) sono il meglio che si possa praticamente fare con le funzioni di complessità.

![[02-notazione-asintotica-p15-upper-lower-bound.png]]
*Una $f(n)$ irregolare, stretta da oltre $n_0$ tra un limite superiore (blu) e uno inferiore (rosso).*

- $f(n) = O(g(n))$ significa che $C \times g(n)$ è un **limite superiore** (*upper bound*) di $f(n)$.
- $f(n) = \Omega(g(n))$ significa che $C \times g(n)$ è un **limite inferiore** (*lower bound*) di $f(n)$.
- $f(n) = \Theta(g(n))$ significa che $C_1 \times g(n)$ è un limite superiore e $C_2 \times g(n)$ un limite inferiore di $f(n)$.

$C$, $C_1$, $C_2$ sono costanti **indipendenti da $n$**.

Le definizioni implicano una costante $n_0$ **oltre la quale** sono soddisfatte: non interessano i piccoli valori di $n$.

![[02-notazione-asintotica-p17-o-omega-theta-grafici.png]]
*(a) $f(n) = O(g(n))$: da $n_0$ in poi $f$ sta sotto $c\,g$; (b) $f(n) = \Omega(g(n))$: da $n_0$ in poi sta sopra; (c) $f(n) = \Theta(g(n))$: tra $c_2\,g$ e $c_1\,g$.*


### Esempi per $\Omega$ e $\Theta$ · [[02-Notazione asintotica.pdf#page=22|p. 22]], [[02-Notazione asintotica.pdf#page=23|23]], [[02-Notazione asintotica.pdf#page=22|p. 22]]

Per $f(n) = 3n^2 - 100n + 6$:

| Affermazione | Motivo |
|---|---|
| $f(n) = \Omega(n^2)$ | $2.99\,n^2 < 3n^2 - 100n + 6$ (per $n$ abbastanza grande) |
| $f(n) \neq \Omega(n^3)$ | $3n^2 - 100n + 6 < n^3$ (per $n$ abbastanza grande) |
| $f(n) = \Omega(n)$ | $10^{10^{10}}\, n < 3n^2 - 100n + 6$ (per $n$ abbastanza grande) |
| $f(n) = \Theta(n^2)$ | vale sia $O(n^2)$ sia $\Omega(n^2)$ |
| $f(n) \neq \Theta(n^3)$ | vale solo $O(n^3)$ |
| $f(n) \neq \Theta(n)$ | vale solo $\Omega(n)$ |

### Formule · [[02-Notazione asintotica.pdf#page=18|p. 18]], [[02-Notazione asintotica.pdf#page=21|p. 21]], [[02-Notazione asintotica.pdf#page=27|p. 27]], [[02-Notazione asintotica.pdf#page=19|p. 19]], [[02-Notazione asintotica.pdf#page=20|p. 20]], [[02-Notazione asintotica.pdf#page=28|p. 28]]

> 🧮 Formula chiave:
- $f(n) = O(g(n))$ se esistono costanti positive $n_0$ e $c$ tali che, a destra di $n_0$, il valore di $f(n)$ sta sempre **su o sotto** $c \cdot g(n)$:
$$ \exists\, c > 0,\ n_0 > 0 :\ \ f(n) \le c\,g(n)\quad \forall n \ge n_0 $$
- $f(n) = \Omega(g(n))$ se esistono costanti positive $n_0$ e $c$ tali che, a destra di $n_0$, $f(n)$ sta sempre **su o sopra** $c \cdot g(n)$:
$$ \exists\, c > 0,\ n_0 > 0 :\ \ f(n) \ge c\,g(n)\quad \forall n \ge n_0 $$
- $f(n) = \Theta(g(n))$ se esistono costanti positive $n_0$, $c_1$, $c_2$ tali che, a destra di $n_0$, $f(n)$ sta sempre **tra** $c_1 \cdot g(n)$ e $c_2 \cdot g(n)$ inclusi:
$$ \exists\, c_1, c_2 > 0,\ n_0 > 0 :\ \ c_1\,g(n) \le f(n) \le c_2\,g(n)\quad \forall n \ge n_0 $$

Simboli: $f, g$ = funzioni da interi positivi a reali (qui: numeri di passi); $n$ = dimensione dell'ingresso; $c, c_1, c_2$ = costanti moltiplicative; $n_0$ = soglia.

> ⚠️ Contraddizione (solo di nomi): nella slide p. 16 $C_1$ è la costante del limite **superiore** e $C_2$ dell'inferiore; nella p. 18 $c_1$ è quella del limite **inferiore** e $c_2$ del superiore. La figura (c) di p. 17 segue la convenzione di p. 16 ($c_1 g$ sopra). Nel wiki si usa la convenzione di p. 18.

**NOTA**: l'uguaglianza va pensata come **appartenenza a un insieme di funzioni**: $f(n) = O(g(n))$ significa $f(n) \in O(g(n))$, dove $O(g(n))$ è l'insieme di tutte le funzioni limitate superiormente da un multiplo di $g$.

Quando una notazione asintotica compare in un'**equazione**, va interpretata come una **funzione ignota che non ci interessa specificare**. Esempio: $2n^2 + 3n + 1 = 2n^2 + \Theta(n)$ equivale a $2n^2 + 3n + 1 = 2n^2 + f(n)$, dove $f(n)$ è una qualunque funzione nell'insieme $\Theta(n)$ (qui $f(n) = 3n + 1$).

**Proprietà**:

| Proprietà | Enunciato | Vale per |
|---|---|---|
| Transitiva | $f(n) = O(g(n))$ e $g(n) = O(h(n)) \Rightarrow f(n) = O(h(n))$ | $O$, $\Theta$, $\Omega$ |
| Riflessiva | $f(n) = O(f(n))$ | $O$, $\Theta$, $\Omega$ |
| Simmetrica | $f(n) = \Theta(g(n)) \Leftrightarrow g(n) = \Theta(f(n))$ | $\Theta$ |
| «Anti-simmetrica» | $f(n) = O(g(n)) \Leftrightarrow g(n) = \Omega(f(n))$ | $O$/$\Omega$ |

![[02-notazione-asintotica-p27-proprieta-notazioni.png]]


### Solar Sails vs. Rockets · [[02-Notazione asintotica.pdf#page=30|p. 30]], [[02-Notazione asintotica.pdf#page=29|p. 29]]

Il razzo raggiunge una velocità alta prima di esaurire il carburante e poi prosegue a velocità costante $v_r$. La vela solare accelera lentamente per la spinta della radiazione (vento solare), ma la sua velocità $v_s = at$ deve prima o poi superare quella del razzo. È la **dominanza asintotica** in azione.

### Formule · [[02-Notazione asintotica.pdf#page=24|p. 24]]–[[02-Notazione asintotica.pdf#page=26|26]], [[02-Notazione asintotica.pdf#page=23|p. 23]]

Supponiamo $f(n) = O(n^2)$ e $g(n) = O(n^2)$.
- **Somma:** $g'(n) = f(n) + g(n)$. Sommando le costanti dei limiti si ottiene $g'(n) = O(n^2)$.
- **Differenza:** $g''(n) = f(n) - |g(n)|$. Poiché le costanti non si cancellano necessariamente, $g''(n) = O(n^2)$.
- Non sappiamo **nulla sui limiti inferiori** di $g'$ e $g''$, perché non sappiamo nulla sui limiti inferiori di $f$ e $g$.

Esempio della slide: $f(n) = 5n^2$ e $g(n) = 150n^2$ **contro** $f(n) = 500n^2$ e $g(n) = 150n^2$.

La moltiplicazione per una costante non cambia l'andamento asintotico:
$$
O(c \cdot f(n)) \to O(f(n)), \qquad \Omega(c \cdot f(n)) \to \Omega(f(n)), \qquad \Theta(c \cdot f(n)) \to \Theta(f(n))
$$
La «vecchia costante» $C$ del Big Oh diventa $c \cdot C$.

Quando entrambe le funzioni di un prodotto sono crescenti, **contano entrambe**:
$$
O(f(n)) \cdot O(g(n)) \to O(f(n) \cdot g(n)), \quad \Omega(f(n)) \cdot \Omega(g(n)) \to \Omega(f(n) \cdot g(n)), \quad \Theta(f(n)) \cdot \Theta(g(n)) \to \Theta(f(n) \cdot g(n))
$$

### Spiegazione · [[02-Notazione asintotica.pdf#page=31|p. 31]], [[02-Notazione asintotica.pdf#page=36|p. 36]], [[02-Notazione asintotica.pdf#page=30|p. 30]], [[02-Notazione asintotica.pdf#page=32|p. 32]]

| $n$ | $\lg n$ | $n$ | $n \lg n$ | $n^2$ | $2^n$ | $n!$ |
|---|---|---|---|---|---|---|
| 10 | 0.003 µs | 0.01 µs | 0.033 µs | 0.1 µs | 1 µs | 3.63 ms |
| 20 | 0.004 µs | 0.02 µs | 0.086 µs | 0.4 µs | 1 ms | 77.1 years |
| 30 | 0.005 µs | 0.03 µs | 0.147 µs | 0.9 µs | 1 sec | 8.4 × 10¹⁵ yrs |
| 40 | 0.005 µs | 0.04 µs | 0.213 µs | 1.6 µs | 18.3 min | |
| 50 | 0.006 µs | 0.05 µs | 0.282 µs | 2.5 µs | 13 days | |
| 100 | 0.007 µs | 0.1 µs | 0.644 µs | 10 µs | 4 × 10¹³ yrs | |
| 1,000 | 0.010 µs | 1.00 µs | 9.966 µs | 1 ms | | |
| 10,000 | 0.013 µs | 10 µs | 130 µs | 100 ms | | |
| 100,000 | 0.017 µs | 0.10 ms | 1.67 ms | 10 sec | | |
| 1,000,000 | 0.020 µs | 1 ms | 19.93 ms | 16.7 min | | |
| 10,000,000 | 0.023 µs | 0.01 sec | 0.23 sec | 1.16 days | | |
| 100,000,000 | 0.027 µs | 0.10 sec | 2.66 sec | 115.7 days | | |
| 1,000,000,000 | 0.030 µs | 1 sec | 29.90 sec | 31.7 years | | |

![[02-notazione-asintotica-p36-tabella-crescita-funzioni.png]]

**Take-Home Lesson**: «Although esoteric functions arise in advanced algorithm analysis, a small variety of time complexities suffice and account for most algorithms that are widely used in practice.»

- Gli algoritmi **esponenziali** diventano senza speranza molto in fretta.
- Gli algoritmi **quadratici** diventano senza speranza a (o prima di) $1\,000\,000$.
- $O(n\log n)$ è praticabile fino a circa **un miliardo**.
- $O(\log n)$ «never sweats».

![[grafico-crescita-funzioni.svg]]

### Definizione · [[02-Notazione asintotica.pdf#page=34|p. 34]], [[02-Notazione asintotica.pdf#page=36|p. 36]], [[02-Notazione asintotica.pdf#page=37|37]], [[02-Notazione asintotica.pdf#page=33|p. 33]]

$f(n)$ **domina** $g(n)$ se
$$ \lim_{n\to\infty} \frac{g(n)}{f(n)} = 0 $$
il che equivale a dire $g(n) = o(f(n))$. Il **little-oh** significa «cresce **strettamente** più lentamente di».

Notazione: $f \gg g$ indica che $f$ domina $g$.

### Formule · [[02-Notazione asintotica.pdf#page=35|p. 35]]–[[02-Notazione asintotica.pdf#page=37|37]], [[02-Notazione asintotica.pdf#page=38|p. 38]]

- $n^a$ domina $n^b$ se $a > b$, poiché $\displaystyle\lim_{n\to\infty} n^b / n^a = n^{b-a} \to 0$.
- $n^a + o(n^a)$ **non** domina $n^a$, poiché $\displaystyle\lim_{n\to\infty} n^a / (n^a + o(n^a)) \to 1$.

> 🧮 Formula chiave:
$$ n! \gg 2^n \gg n^3 \gg n^2 \gg n \log n \gg n \gg \log n \gg 1 $$

$$
n! \gg c^n \gg n^3 \gg n^2 \gg n^{1+\epsilon} \gg n\log n \gg n \gg \sqrt n \gg \log^2 n \gg \log n \gg \frac{\log n}{\log\log n} \gg \log\log n \gg \alpha(n) \gg 1
$$

*Approfondimenti nel wiki: [[lezione-02-notazione-asintotica]], [[modello-ram]], [[tempo-di-esecuzione]], [[casi-di-complessita]], [[notazione-asintotica]], [[dimostrazioni-notazione-asintotica]], [[regole-di-calcolo-asintotico]], [[dominanza-asintotica]]*

## Lezione 3 — Analisi di algoritmi

*Fonte: 03-Analisi di algoritmi.pdf.*

### Definizione · [[03-Analisi di algoritmi.pdf#page=2|p. 2]]–[[03-Analisi di algoritmi.pdf#page=6|6]], [[03-Analisi di algoritmi.pdf#page=4|p. 4]], [[03-Analisi di algoritmi.pdf#page=5|p. 5]], [[03-Analisi di algoritmi.pdf#page=1|p. 1]]

I problemi possono essere affrontati in molti modi; qui si guarda **agli approcci**, non alle strutture dati. Ogni approccio bilancia tre grandezze: **tempo di calcolo**, **qualità della soluzione** e **scalabilità**. Le tre famiglie principali sono:

| Famiglia | Idea (dalla slide) |
|---|---|
| [[divide-et-impera]] | scomponi il problema, risolvi i sottoproblemi, combina i risultati |
| [[ricerca-combinatoria]] | esplora lo spazio delle soluzioni con vincoli e potature verso l'ottimo |
| [[metodi-euristici]] | trova soluzioni «abbastanza buone» rapidamente, senza garanzia d'ottimalità |

La slide p. 2 è l'intestazione della sezione «Classificazione dei problemi».

### Definizione · [[03-Analisi di algoritmi.pdf#page=4|p. 4]]

Gli algoritmi divide et impera **scompongono** il problema in sottoproblemi **simili e più piccoli**, li **risolvono** (spesso in modo ricorsivo) e **combinano** le soluzioni. Funzionano bene quando la divisione è naturale e il «merge» (la combinazione) è efficiente.

Schema: **divide → conquer → combine**, con **casi base** ben definiti.

### Spiegazione · [[03-Analisi di algoritmi.pdf#page=4|p. 4]]

Caratteristiche della soluzione:
- spesso efficienti se la **partizione è bilanciata** (sottoproblemi di dimensione simile);
- buona **parallelizzabilità** dei sottoproblemi (sono indipendenti);
- **overhead** nel passo di combinazione; attenzione al **bilanciamento**.

Esempi classici citati: **ordinamento**, **ricerca**, «…».

### Gli esempi delle lezioni 06–07 · Merge Sort [[06-Merge Sort (1).pdf#page=27|p. 27]], [[06-Merge Sort (1).pdf#page=28|28]] · Quicksort [[07-Quicksort 1.pdf#page=3|p. 3]] · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=4|p. 4]]

| Algoritmo | Divide | Conquer | Combine | Ricorrenza | Costo |
|---|---|---|---|---|---|
| [[merge-sort]] | calcolo del punto medio, $D(n) = \Theta(1)$ | 2 metà | [[merge]], $C(n) = \Theta(n)$ | $2T(n/2) + \Theta(n)$ | $\Theta(n\lg n)$ |
| [[quicksort]] | [[partition]] attorno al pivot, $\Theta(n)$ | 2 parti, anche sbilanciate | niente da fare | da $2T(n/2) + \Theta(n)$ a $T(n-1) + \Theta(n)$ | da $\Theta(n\lg n)$ a $\Theta(n^2)$ |
| [[torre-di-hanoi]] (🧩) | — | 2 sottoproblemi di $n - 1$ dischi + 1 mossa | — | $2M(n-1) + 1$ | $2^n - 1$ mosse |
| [[nuts-and-bolts]] (🧩) | Partition dei bulloni e dei dadi | 2 sottoinsiemi | — | come quicksort randomizzato | $O(n\log n)$ atteso |

Il [[massimo-sottoarray]] è posto come ulteriore problema nella lezione 06, con rimando al libro.

### Definizione · [[03-Analisi di algoritmi.pdf#page=7|p. 7]]–[[03-Analisi di algoritmi.pdf#page=9|9]], [[03-Analisi di algoritmi.pdf#page=8|p. 8]]

Due stili con lo **stesso potere espressivo**: la scelta dipende da chiarezza, costi e vincoli.

|  | Approccio iterativo | Approccio ricorsivo |
|---|---|---|
| Meccanismo | usa cicli (`for`, `while`) e **stato esplicito** passo dopo passo | definisce il problema per **auto-somiglianza**: casi base + chiamate a sottoproblemi |
| Costi | in genere più **prevedibile** su tempo e memoria; poco overhead | **overhead di chiamata** e rischio di **stack overflow** senza tail-call/limiti |
| Quando | ottimo quando l'aggiornamento è lineare e la condizione di arresto è semplice | codice spesso più chiaro per **divide-et-impera** e **backtracking** |
| Altro | facile da ottimizzare e testare; adatto ad ambienti con limiti di stack | elegante, ma va progettata la **combinazione dei risultati** |

La sezione è introdotta dall'intestazione «Caratterizzazione degli algoritmi».

### Spiegazione · [[03-Analisi di algoritmi.pdf#page=10|p. 10]], [[03-Analisi di algoritmi.pdf#page=11|11]], [[03-Analisi di algoritmi.pdf#page=28|p. 28]], [[03-Analisi di algoritmi.pdf#page=33|p. 33]]

Esempio della fonte: somma dei primi $n$ numeri $1 + 2 + \dots + n$.

![[03-analisi-algoritmi-p11-somma-iterativa-ricorsiva.png]]
*Le due versioni affiancate.*

| | [[somma-iterativa]] | [[somma-ricorsiva]] |
|---|---|---|
| Correttezza si prova con | [[invariante-di-ciclo]] | [[correttezza-per-induzione]] |
| Tempo | $2n + 4 = O(n)$ | $1 + cn = O(n)$ |
| Spazio (🧩 mio) | $\Theta(1)$ | $\Theta(n)$ — $n+1$ record di attivazione sulla pila |

### Pseudocodice · [[03-Analisi di algoritmi.pdf#page=11|p. 11]]

```
funzione somma_iterativa(n)
1  s ← 0
2  per i da 1 a n
3      s ← s + i
4  ritorna s
```

Nelle [[pseudocodice|convenzioni del corso]] la riga 2 si scrive `for i ← 1 to n`.

### Pseudocodice · [[03-Analisi di algoritmi.pdf#page=11|p. 11]]

```
funzione somma_ricorsiva(n)
1  se n = 0
2      ritorna 0
3  altrimenti
4      ritorna n + somma_ricorsiva(n − 1)
```


### Correttezza (verifica) · [[03-Analisi di algoritmi.pdf#page=12|p. 12]]

Verificare che l'algoritmo restituisce la soluzione **per ogni istanza possibile** del problema. Per provare che è **incorretto** basta **un'istanza**: un controesempio o un'eccezione.

### Definizione · 01-Introduzione.pdf [[01-Introduzione.pdf#page=9|p. 9]] · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=16|p. 16]]

Un algoritmo è **corretto** se, **per ogni istanza** del problema, **termina** fornendo l'insieme corretto di valori in uscita. Un algoritmo incorretto, su alcune istanze, può **non terminare** oppure terminare con un'**uscita sbagliata**.

La definizione contiene quindi due richieste distinte: (1) l'uscita è giusta, (2) l'algoritmo si ferma. Separandole si ottengono due livelli di correttezza.

- L'invariante di ciclo dimostra la **correttezza parziale**.
- Per la **correttezza totale** serve anche la **terminazione**: di solito si introduce una **funzione variante** (misura intera $\ge 0$) che diminuisce a ogni iterazione.

### Formule · [[03-Analisi di algoritmi.pdf#page=16|p. 16]], [[03-Analisi di algoritmi.pdf#page=18|p. 18]]

Siano $P$ la **pre-condizione** (cosa vale sull'input, es. «$A$ è un array di $n$ numeri») e $Q$ la **post-condizione** (cosa deve valere sull'output, es. «$A$ contiene gli stessi elementi, in ordine crescente»).

$$
\begin{aligned}
&\textbf{parziale:} && \forall\, x \text{ con } P(x):\quad \text{se l'algoritmo su } x \text{ termina, allora l'output soddisfa } Q \\
&\textbf{totale:} && \forall\, x \text{ con } P(x):\quad \text{l'algoritmo su } x \text{ termina } \textbf{e} \text{ l'output soddisfa } Q
\end{aligned}
$$

$$ \text{correttezza totale} = \text{correttezza parziale} + \text{terminazione} $$

### Perché distinguerle · [[03-Analisi di algoritmi.pdf#page=16|p. 16]], [[03-Analisi di algoritmi.pdf#page=17|17]]

Un algoritmo che va in **ciclo infinito** su un'istanza non restituisce mai un'uscita, quindi non ne restituisce mai una sbagliata: rispetto a quell'istanza è parzialmente corretto «a costo zero». La correttezza parziale da sola non basta; per questo la slide chiede esplicitamente anche la terminazione.

### Come si valuta la correttezza · [[03-Analisi di algoritmi.pdf#page=13|p. 13]], [[03-Analisi di algoritmi.pdf#page=15|p. 15]], [[03-Analisi di algoritmi.pdf#page=16|16]], [[03-Analisi di algoritmi.pdf#page=18|p. 18]], [[03-Analisi di algoritmi.pdf#page=12|p. 12]]

| Obiettivo | Strumento | Cosa dimostra | Slide |
|---|---|---|---|
| dimostrare che è **sbagliato** | un **controesempio** (una sola istanza che fallisce) | che non vale la correttezza (né parziale né totale su quell'istanza) | p. 13–p. 15 |
| algoritmo **iterativo** | **invariante di ciclo** (inizializzazione, conservazione, conclusione) | correttezza **parziale** | p. 16 |
|  | **funzione variante** | **terminazione** → con l'invariante, correttezza **totale** | p. 16 |
| algoritmo **ricorsivo** | **induzione**: casi base + passo induttivo | correttezza **parziale** | p. 18 |
|  | **misura ben fondata** che decresce a ogni chiamata | **terminazione** → correttezza **totale** | p. 18 |

Non trovare controesempi **non** dimostra la correttezza: i test coprono un numero finito di istanze, la correttezza parla di tutte.

### Definizione · [[03-Analisi di algoritmi.pdf#page=16|p. 16]]

Per gli algoritmi **iterativi** si usa l'approccio basato sull'**invariante di ciclo**: una proprietà delle variabili che vale a ogni iterazione. L'invariante dimostra la **correttezza parziale** in tre passi:

1. **Inizializzazione** — l'invariante vale prima della prima iterazione.
2. **Conservazione** — se vale all'inizio di un'iterazione, vale anche alla successiva.
3. **Conclusione** — quando la condizione di ciclo è falsa, invariante + condizione d'uscita ⇒ **post-condizione**.

Per la **correttezza totale** serve anche la **terminazione**: di solito si introduce una **funzione variante** (misura intera $\ge 0$) che diminuisce a ogni iterazione.

### Correttezza · [[03-Analisi di algoritmi.pdf#page=17|p. 17]]

Invariante: all'inizio dell'iterazione $i$, $s = \sum_{k=1}^{i-1} k$. Dimostrazione completa, con la segnalazione del refuso «$i = 0$» della slide → [[invariante-di-ciclo]].

### Definizione · [[03-Analisi di algoritmi.pdf#page=18|p. 18]]

Per la ricorsione la prova di correttezza è strettamente legata all'**induzione** (spesso induzione **forte** o **strutturale**). È «simile nello spirito» agli invarianti di ciclo, ma la forma tipica è:

1. **Specifiche** — si definiscono **pre/post-condizioni** dell'algoritmo.
2. **Misura ben fondata** (es. dimensione dell'input) che **decresce** a ogni chiamata ricorsiva.
3. **Casi base** — si mostra che per gli input minimi il risultato è corretto.
4. **Passo induttivo** (induzione forte) — supposte corrette tutte le chiamate ricorsive su input «più piccoli» (**ipotesi induttiva**), si dimostra che, usando quei risultati, la funzione produce l'output corretto.
5. **Terminazione** — le chiamate ricorsive avvengono solo su input con misura strettamente minore ⇒ catena finita ⇒ termina.

### Correttezza · [[03-Analisi di algoritmi.pdf#page=19|p. 19]]

Per induzione su $n$: misura $n$; base $S(0) = 0$; se $S(n-1)$ è corretto, $S(n) = n + S(n-1)$ è corretto; ogni chiamata usa $n - 1 < n$ → termina. Passaggi espliciti → [[correttezza-per-induzione]].

### Complessità · [[03-Analisi di algoritmi.pdf#page=23|p. 23]]–[[03-Analisi di algoritmi.pdf#page=29|29]], [[03-Analisi di algoritmi.pdf#page=24|p. 24]], [[03-Analisi di algoritmi.pdf#page=25|p. 25]], [[03-Analisi di algoritmi.pdf#page=26|p. 26]], [[03-Analisi di algoritmi.pdf#page=27|p. 27]], [[03-Analisi di algoritmi.pdf#page=20|p. 20]]

| Riga | Operazione | Costo × esecuzioni |
|---|---|---|
| 1 | assegnazione | 1 |
| 2 | inizializzazione del ciclo ($i = 1$) | 1 |
| 2 | test di ciclo $i \le n$ | $n + 1$ |
| 3 | corpo | $n$ (*) |
| 4 | return | 1 |

(*) «in realtà abbiamo $n$ somme, $n$ assegnazioni e $n$ incrementi».

$$ T(n) = 1 + 1 + (n+1) + n + 1 = 2n + 4 \ \Rightarrow\ O(n) $$

(risultato di p. 28)

**Spazio** («E la complessità spaziale?»): 🧩 $\Theta(1)$, due variabili ($s$, $i$) qualunque sia $n$.

**Verifica:** [[somma_primi_n.py]] conta $2n+4$ passi per $n \in \{0,1,2,5,10,100\}$.

![[03-analisi-algoritmi-p28-costo-somma-iterativa.png]]

### Definizione · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=30|p. 30]] · Merge Sort [[06-Merge Sort (1).pdf#page=29|p. 29]]

Un programma ricorsivo viene richiamato più volte su una versione ridotta del problema. Il **costo complessivo** $T(n)$ è dato dalla **somma dei costi delle singole chiamate**, con $T(0)$ pari al costo del passo ricorsivo più interno (quello in cui la funzione non viene richiamata ulteriormente).

Il costo si esprime quindi con un'**equazione di ricorrenza**: $T(n)$ definito in funzione di $T$ su valori più piccoli, più un caso base.

Una **ricorrenza** è un'equazione o **disequazione** che descrive una funzione in termini del suo valore su ingressi di dimensione inferiore. Il tempo di esecuzione di algoritmi ricorsivi è solitamente espresso mediante una ricorrenza, ad esempio per [[merge-sort]]:
$$ T(n) = \begin{cases} \Theta(1) & \text{se } n = 1 \\ 2T(n/2) + \Theta(n) & \text{altrimenti} \end{cases} $$
Vedremo tre metodi per risolvere una ricorrenza: [[metodo-di-sostituzione]], [[metodo-albero-di-ricorrenza]], metodo dell'esperto ([[teorema-dell-esperto]]).

### Complessità · [[03-Analisi di algoritmi.pdf#page=31|p. 31]], [[03-Analisi di algoritmi.pdf#page=33|p. 33]], [[03-Analisi di algoritmi.pdf#page=35|35]]

- $T(0)$: un confronto e un return ⇒ 1 (righe 1–2)
- $T(i)$, $0 < i \le n$: una chiamata ricorsiva con argomento $i - 1$, una somma, un return ⇒ $T(i) = T(i-1) + c$ (riga 4)

$$ T(n) = T(n-1) + c = T(n-2) + 2c = \dots = T(0) + n\,c = 1 + c\,n = O(n) $$

Srotolamento completo e verifica della forma generale → [[equazioni-di-ricorrenza]].

**Spazio** («E la complessità spaziale?»): 🧩 $\Theta(n)$ — $n+1$ record di attivazione contemporaneamente sulla pila (traccia sopra). È il costo nascosto della ricorsione rispetto a [[somma-iterativa]] ($\Theta(1)$).

**Verifica:** [[somma_primi_n.py]] (costo con $c = 1$ pari a $n + 1$, profondità massima $n + 1$).

### Formule · [[03-Analisi di algoritmi.pdf#page=31|p. 31]], [[03-Analisi di algoritmi.pdf#page=32|32]]

Per [[somma-ricorsiva]]:
- $T(0)$: un confronto e un return ⇒ **1**
- $T(i)$, con $0 < i \le n$: una chiamata ricorsiva con argomento $i - 1$, una somma, un return ⇒ $T(i) = T(i-1) + c$

> 🧮 Formula chiave:
$$ T(n) = \begin{cases} 1 & n = 0 \\ T(n-1) + c & n > 0 \end{cases} \qquad \Longrightarrow \qquad T(n) = 1 + c\,n = O(n) $$

Simboli: $T(n)$ = passi per l'input $n$; $c$ = costo costante del lavoro di una chiamata non base (confronto, somma, return, chiamata).

### Somma 1-n ricorsiva (tempo e spazio) · [[03-Analisi di algoritmi.pdf#page=34|p. 34]]

```
funzione somma_ricorsiva(n)
    se n = 0
        ritorna 0
    altrimenti
        ritorna n + somma_ricorsiva(n - 1)
```

$$T(n) = T(n-1) + c = T(n-2) + 2c = T(n-3) + 3c = \dots = T(0) + n \cdot c = 1 + c \cdot n = O(n)$$

E la complessità spaziale?

### Spiegazione · [[03-Analisi di algoritmi.pdf#page=35|p. 35]]

La struttura della ricorrenza ricalca quella dell'algoritmo: il caso base dell'algoritmo dà il caso base di $T$, la chiamata ricorsiva dà il termine $T(n-1)$, il lavoro «locale» dà il termine $c$. La stessa struttura regge la [[correttezza-per-induzione]].

La domanda «E la complessità spaziale?» ha risposta $\Theta(n)$ (🧩, profondità della ricorsione) → [[tempo-di-esecuzione]].

*Approfondimenti nel wiki: [[lezione-03-analisi-di-algoritmi]], [[paradigmi-di-progettazione]], [[divide-et-impera]], [[iterazione-e-ricorsione]], [[somma-iterativa]], [[somma-ricorsiva]], [[correttezza-parziale-e-totale]], [[invariante-di-ciclo]], [[correttezza-per-induzione]], [[dimostrazioni-di-correttezza]], [[analisi-del-costo-riga-per-riga]], [[equazioni-di-ricorrenza]], [[risoluzione-ricorrenze]]*

## Lezione 4 — Strutture dati elementari

*Fonte: 04-Strutture dati elementari.pdf.*

### Definizione · [[04-Strutture dati elementari.pdf#page=3|p. 3]], [[04-Strutture dati elementari.pdf#page=4|4]], [[04-Strutture dati elementari.pdf#page=1|p. 1]], [[04-Strutture dati elementari.pdf#page=2|p. 2]]

«Mankind's progress is measured by the number of things we can do without thinking.» Le **strutture dati elementari** — pile, code, liste, heap — sono i componenti «pronti all'uso» (*off-the-shelf*) con cui si costruiscono gli algoritmi.

Ogni struttura dati ha **due aspetti**:
1. le **operazioni astratte** che supporta;
2. l'**implementazione** di queste operazioni.

Poter descrivere il comportamento delle strutture dati in termini di operazioni astratte è il motivo per cui possiamo usarle «senza pensare». Esempio (pila):
- $Push(x, s)$ — inserisce l'elemento $x$ in cima alla pila $s$;
- $Pop(s)$ — restituisce (e rimuove) l'elemento in cima alla pila $s$.

Il fatto che esistano **implementazioni diverse** delle stesse operazioni astratte permette di **ottimizzare le prestazioni** in circostanze diverse.

### Definizione · 04-Strutture dati elementari.pdf [[04-Strutture dati elementari.pdf#page=5|p. 5]], [[04-Strutture dati elementari.pdf#page=15|p. 15]] · Pseudocodice [[a1-indicazioni_psuedocodice.pdf#page=3|p. 3]], [[04-Strutture dati elementari.pdf#page=6|p. 6]], [[04-Strutture dati elementari.pdf#page=14|p. 14]]

Le strutture dati si classificano nettamente come **contigue** o **collegate**, a seconda che siano basate su **array** o su **puntatori**:
- le strutture **allocate in modo contiguo** sono composte da **singoli blocchi di memoria** e comprendono array, matrici, heap e tabelle hash;
- le strutture **collegate** sono composte da **più blocchi distinti** di memoria legati tra loro da **puntatori**, e comprendono liste, alberi e liste di adiacenza dei grafi.

- I **puntatori** rappresentano l'**indirizzo** di una locazione di memoria.
- Un numero di cellulare può essere visto come un puntatore al suo proprietario mentre si sposta per il pianeta.
- In C, `*p` indica l'elemento puntato da `p` e `&x` indica l'indirizzo (cioè il puntatore) di una variabile `x`.
- Un valore speciale `NULL` indica puntatori che terminano una struttura o non assegnati.

Nello [[pseudocodice]] del corso il puntatore nullo si chiama `NIL` e ogni variabile di tipo aggregato è un puntatore alla struttura.

### Cos'è · [[04-Strutture dati elementari.pdf#page=8|p. 8]], [[04-Strutture dati elementari.pdf#page=7|p. 7]]

Un **array** è una struttura di record di dati di **dimensione fissa** tali che ogni elemento può essere localizzato efficientemente tramite il suo **indice** o, equivalentemente, il suo **indirizzo**. È la struttura contigua per eccellenza ([[strutture-contigue-e-collegate]]).

### Operazioni e costi · [[04-Strutture dati elementari.pdf#page=8|p. 8]], [[04-Strutture dati elementari.pdf#page=10|p. 10]]

| Operazione | Costo | Fonte |
|---|---|---|
| accesso a $A[i]$ dato l'indice | tempo costante | p. 8 |
| crescita oltre la dimensione iniziale | impossibile per un array semplice | p. 10 → [[array-dinamico]] |

### Vantaggi · [[04-Strutture dati elementari.pdf#page=8|p. 8]]

- accesso in **tempo costante** dato l'indice;
- gli array consistono **solo di dati**: nessuno spazio sprecato per collegamenti o informazioni di formato;
- la **continuità fisica** (località della memoria) tra accessi successivi aiuta a sfruttare la **cache** ad alta velocità delle architetture moderne.

### Rappresentazione in memoria · [[04-Strutture dati elementari.pdf#page=9|p. 9]]

![[04-strutture-dati-p9-array.png]]
*Array $S[1..7]$ con $S = \langle 15, 6, 2, 9 \rangle$ nelle prime 4 celle e 3 celle libere (grigie).*

### Cos'è · [[04-Strutture dati elementari.pdf#page=10|p. 10]]

Un array semplice non può cambiare dimensione durante l'esecuzione e allocarne uno enorme spreca spazio. Con gli **array dinamici** si parte da un array di **dimensione 1** e se ne **raddoppia** la dimensione da $m$ a $2m$ ogni volta che lo spazio finisce (allocando il nuovo array e ricopiando i vecchi elementi).

### Formule · [[04-Strutture dati elementari.pdf#page=10|p. 10]], [[04-Strutture dati elementari.pdf#page=11|11]]

> 🧮 Formula chiave: numero di raddoppi per $n$ elementi $= \lceil \log_2 n \rceil$; spostamenti totali
$$ M = \sum_{i=1}^{\lg n} i \cdot \frac{n}{2^i} = n \sum_{i=1}^{\lg n} \frac{i}{2^i} \le n \sum_{i=1}^{\infty} \frac{i}{2^i} = 2n $$

(formula di p. 11)

Simboli: $n$ = elementi inseriti; $m$ = capacità corrente; $M$ = numero totale di spostamenti (copie) di elementi.

### Nota: «free lunch» e teorema *no free lunch* · [[04-Strutture dati elementari.pdf#page=12|p. 12]], [[04-Strutture dati elementari.pdf#page=13|p. 13]]

Nel contesto della complessità computazionale e dell'ottimizzazione, il teorema **«no free lunch» (NFL)** afferma che, per certi tipi di problemi matematici, il costo computazionale per trovare una soluzione, **mediato su tutti i problemi della classe**, è lo stesso per qualsiasi metodo di soluzione. Il nome allude al detto «no such thing as a free lunch»: nessun metodo offre una «scorciatoia». La slide lo accosta per contrasto al «free lunch» della serie geometrica.

### Cos'è · [[04-Strutture dati elementari.pdf#page=16|p. 16]]

Struttura **collegata**: ogni nodo contiene un dato e un puntatore al successore; l'ultimo punta a `NIL`. → [[strutture-contigue-e-collegate]]

### Rappresentazione in memoria · [[04-Strutture dati elementari.pdf#page=16|p. 16]]

```c
typedef struct list {
    item_type item;        /* data item */
    struct list *next;     /* point to successor */
} list;
```

![[04-strutture-dati-p16-lista-concatenata.png]]
*Lista Turing → Knuth → Karp → NIL; il cerchio grigio è il puntatore alla testa.*

### Inserimento in testa · [[04-Strutture dati elementari.pdf#page=17|p. 17]]

Non serve mantenere un ordine particolare, quindi conviene inserire ogni nuovo elemento **in testa**.

```c
void insert_list(list **l, item_type x) {
    list *p;               /* temporary pointer */
    p = malloc(sizeof(list));
    p->item = x;
    p->next = *l;
    *l = p;
}
```

Nota il `**l`: la testa della lista cambia, quindi serve un puntatore al puntatore di testa. **Costo: $\Theta(1)$**.

### Costi riassunti · [[04-Strutture dati elementari.pdf#page=17|p. 17]]–[[04-Strutture dati elementari.pdf#page=20|20]], [[04-Strutture dati elementari.pdf#page=18|p. 18]], [[04-Strutture dati elementari.pdf#page=19|p. 19]]

| Operazione | Lista semplice | Fonte |
|---|---|---|
| inserimento in testa | $\Theta(1)$ | p. 17 |
| ricerca | best $\Theta(1)$, worst $\Theta(n)$ | p. 18 |
| predecessore | best $\Theta(1)$, worst $\Theta(n)$ | p. 19 |
| cancellazione | best $\Theta(1)$, worst $\Theta(n)$ | p. 20 |

### Ricerca · [[04-Strutture dati elementari.pdf#page=18|p. 18]]

La ricerca si può fare in modo iterativo o ricorsivo; la slide mostra la versione ricorsiva:

```c
list *search_list(list *l, item_type x) {
    if (l == NULL) {
        return(NULL);
    }
    if (l->item == x) {
        return(l);
    } else {
        return(search_list(l->next, x));
    }
}
```

**Best case:** $\Theta(1)$ — il primo nodo è quello cercato. **Worst case:** $\Theta(n)$ — è l'ultimo o non c'è.

### Cancellazione — ricerca del predecessore · [[04-Strutture dati elementari.pdf#page=19|p. 19]]

```c
list *item_ahead(list *l, list *x) {
    if ((l == NULL) || (l->next == NULL)) {
        return(NULL);
    }
    if ((l->next) == x) {
        return(l);
    } else {
        return(item_ahead(l->next, x));
    }
}
```

**Best case:** $\Theta(1)$ — il primo nodo è quello cercato (è il predecessore). **Worst case:** $\Theta(n)$ — è l'ultimo o non c'è.

### Cancellazione — rimozione del nodo · 04-Strutture dati elementari.pdf [[04-Strutture dati elementari.pdf#page=20|p. 20]] · Pseudocodice [[a1-indicazioni_psuedocodice.pdf#page=4|p. 4]]

```c
void delete_list(list **l, list **x) {
    list *p;               /* item pointer */
    list *pred;            /* predecessor pointer */
    p = *l;
    pred = item_ahead(*l, *x);
    if (pred == NULL) {    /* splice out of list */
        *l = p->next;
    } else {
        pred->next = (*x)->next;
    }
    free(*x);              /* free memory used by node */
}
```

**Best case:** $\Theta(1)$ — «cancelli la testa o la trovi subito». **Worst case:** $\Theta(n)$ — tempo dominato dalla ricerca del predecessore.

> ⚠️ Contraddizione (🧩 osservazione mia sul codice): con **questo** `item_ahead`, cancellare la **testa** non costa $\Theta(1)$. Se `*x` è la testa, nessun nodo ha `next == x`, quindi `item_ahead` scorre tutta la lista prima di restituire `NULL`: $\Theta(n)$. Il caso $\Theta(1)$ si ha quando il predecessore è il primo nodo (cioè si cancella il secondo). Per avere la testa in $\Theta(1)$ bisognerebbe controllare `*l == *x` prima di chiamare `item_ahead`. Inoltre il codice presuppone che `*x` appartenga alla lista: se non c'è, `pred == NULL` e viene staccata la testa per errore.

```
LIST-SEARCH(L, k)
1  x ← L.head
2  while x ≠ NIL and x.key ≠ k        ▷ and in corto circuito
3      x ← x.next
4  return x

LIST-INSERT(L, x)                     ▷ inserimento in testa, Θ(1)
1  x.next ← L.head
2  L.head ← x

LIST-DELETE(L, x)                     ▷ x appartiene a L
1  if L.head = x
2      L.head ← x.next                ▷ testa: Θ(1)
3  else p ← L.head
4      while p.next ≠ x               ▷ ricerca del predecessore: O(n)
5          p ← p.next
6      p.next ← x.next
```

Il corto circuito di `and` alla riga 2 di LIST-SEARCH evita di leggere `x.key` quando `x = NIL`.

### Spiegazione · [[04-Strutture dati elementari.pdf#page=8|p. 8]], [[04-Strutture dati elementari.pdf#page=10|p. 10]], [[04-Strutture dati elementari.pdf#page=21|p. 21]], [[04-Strutture dati elementari.pdf#page=22|22]]

Confronto tra le due famiglie, ricavato dalle slide:

| Aspetto | Contigue ([[array]]) | Collegate ([[lista-concatenata]]) |
|---|---|---|
| Accesso all'elemento $i$-esimo | tempo costante dato l'indice | scorrimento dalla testa |
| Spazio | solo dati, nessun collegamento | dati + puntatori (il doppio con le liste doppie) |
| Località / cache | continuità fisica → sfrutta la cache | blocchi sparsi |
| Overflow | dimensione fissa (salvo array dinamici) | mai, finché la memoria non è davvero piena |
| Inserimenti/cancellazioni | bisogna spostare gli elementi successivi | più semplici: si ricollegano solo i puntatori (ma dipende dall'operazione, vedi sotto) |
| Record grandi | si spostano i dati | spostare puntatori è più facile e veloce |

1. L'overflow sulle strutture collegate non può mai avvenire a meno che la memoria sia effettivamente piena.
2. Nelle liste collegate inserimenti e cancellazioni sono **più semplici** che nelle liste contigue (array). La slide dice «Insertions and deletions are *simpler* than for contiguous (array) lists»: il soggetto sono le liste collegate, quindi il vantaggio è della lista, non dell'array.
3. Con record grandi, spostare puntatori è più facile e veloce che spostare gli elementi stessi.

«Dynamic memory allocation provides us with flexibility on how and where we use our limited storage resources.»

### Liste semplici e doppie · [[04-Strutture dati elementari.pdf#page=22|p. 22]], [[04-Strutture dati elementari.pdf#page=23|p. 23]]

Con le **liste doppiamente concatenate** (ogni nodo punta anche al predecessore) si guadagna flessibilità nelle interrogazioni sul predecessore, al costo di **raddoppiare il numero di puntatori**. Poiché il costo extra in big-Oh è **zero**, di solito si assume che le liste siano mantenute doppie, anche se non sempre è necessario. «Singly linked to doubly-linked list is as a conga line is to a can-can line.»

![[04-strutture-dati-p22-lista-semplice-doppia.png]]
*Sopra: lista semplice A→…→F; sotto: lista doppia con puntatori in entrambi i versi.*

### Cos'è · [[04-Strutture dati elementari.pdf#page=25|p. 25]], [[04-Strutture dati elementari.pdf#page=24|p. 24]]

A volte l'ordine con cui si recuperano i dati è **indipendente dal loro contenuto** e dipende solo da **quando sono arrivati**. Una **pila** supporta operazioni **last-in, first-out** (LIFO):
- $Push(x, s)$ — inserisce l'elemento $x$ **in cima** alla pila $s$;
- $Pop(s)$ — restituisce (e rimuove) l'elemento **in cima** alla pila $s$.

### Cos'è · [[04-Strutture dati elementari.pdf#page=25|p. 25]]

Una **coda** supporta operazioni **first-in, first-out** (FIFO):
- $Enqueue(x, q)$ — inserisce l'elemento $x$ **in fondo** alla coda $q$;
- $Dequeue(q)$ — restituisce (e rimuove) l'elemento **in testa** alla coda $q$.

### Rappresentazione in memoria · [[04-Strutture dati elementari.pdf#page=26|p. 26]], [[04-Strutture dati elementari.pdf#page=28|p. 28]]

Le pile si rappresentano più facilmente con un **array**, con push/pop che **incrementano/decrementano un contatore**. Tutte le operazioni costano $O(1)$, sia con array sia con liste.

![[04-strutture-dati-p26-stack-su-array.png]]
*Figura 10.1 del Cormen.*

Didascalia della figura (tradotta): implementazione di una pila $S$ con un array. Gli elementi della pila sono solo nelle posizioni in grigio chiaro. (a) $S$ ha 4 elementi; l'elemento in cima è 9. (b) $S$ dopo le chiamate $\text{PUSH}(S, 17)$ e $\text{PUSH}(S, 3)$. (c) $S$ dopo la chiamata $\text{POP}(S)$, che ha restituito l'elemento 3, il più recentemente inserito. L'elemento 3 compare ancora nell'array, ma non è più nella pila: la cima è l'elemento 17.

### Rappresentazione in memoria · [[04-Strutture dati elementari.pdf#page=27|p. 27]], [[04-Strutture dati elementari.pdf#page=28|28]]

Le code si rappresentano più facilmente con una **lista concatenata**, con enqueue/dequeue che operano alle **estremità opposte** della lista. Tutte le operazioni costano $O(1)$, sia con array sia con liste.

Implementazione su **array circolare** (Figura 10.2 del Cormen):

![[04-strutture-dati-p27-coda-su-array.png]]

Didascalia della figura (tradotta): una coda implementata con un array $Q[1..12]$. Gli elementi della coda sono solo nelle posizioni in grigio chiaro. (a) La coda ha 5 elementi, nelle posizioni $Q[7..11]$. (b) La configurazione dopo le chiamate $\text{ENQUEUE}(Q, 17)$, $\text{ENQUEUE}(Q, 3)$ ed $\text{ENQUEUE}(Q, 5)$. (c) La configurazione dopo la chiamata $\text{DEQUEUE}(Q)$, che restituisce la chiave 15, prima in testa alla coda. La nuova testa ha chiave 6.

### Operazioni (pseudocodice) · [[04-Strutture dati elementari.pdf#page=28|p. 28]]

```
STACK-EMPTY(S)
1  if S.top = 0
2      return true
3  else return false

PUSH(S, x)
1  if S.top = length[S]
2      error "overflow"          ▷ 🧩 controllo mio
3  S.top ← S.top + 1
4  S[S.top] ← x

POP(S)
1  if STACK-EMPTY(S)
2      error "underflow"
3  else S.top ← S.top − 1
4      return S[S.top + 1]
```

Ogni operazione esegue un numero costante di righe → $O(1)$, come dice p. 28.

### Operazioni (pseudocodice) · [[04-Strutture dati elementari.pdf#page=28|p. 28]]

```
ENQUEUE(Q, x)
1  Q[Q.tail] ← x
2  if Q.tail = length[Q]
3      Q.tail ← 1
4  else Q.tail ← Q.tail + 1

DEQUEUE(Q)
1  x ← Q[Q.head]
2  if Q.head = length[Q]
3      Q.head ← 1
4  else Q.head ← Q.head + 1
5  return x
```

Numero costante di righe → $O(1)$.

### Perché pile e code · [[04-Strutture dati elementari.pdf#page=29|p. 29]]

Entrambe sono adatte a un contenitore in cui l'ordine non conta, ma a volte conta. Le file in banca sono code, mentre «food in my refrigerator is treated as a stack». **L'intera differenza tra visita in profondità (DFS) e in ampiezza (BFS)** sta nel fatto che i vertici da elaborare siano tenuti in una **pila** o in una **coda**.

### Perché pile e code · [[04-Strutture dati elementari.pdf#page=29|p. 29]], [[04-Strutture dati elementari.pdf#page=30|p. 30]]

Le file in banca sono code; la differenza tra BFS e DFS è solo se i vertici da elaborare stanno in una coda o in una pila → [[pila]].

*Approfondimenti nel wiki: [[lezione-04-strutture-dati-elementari]], [[tipo-di-dato-astratto]], [[strutture-contigue-e-collegate]], [[array]], [[array-dinamico]], [[lista-concatenata]], [[pila]], [[coda]], [[tracce-pila-e-coda]]*

## Lezione 5 — Insertion sort

*Fonte: 05-Insertion sort.pdf.*

### Ordinamento: applicazioni · [[05-Insertion sort.pdf#page=3|p. 3]]

Applicazioni dell'ordinamento: *searching*, coppia più vicina (*closest pair*), unicità degli elementi (*element uniqueness*), distribuzione di frequenza (*frequency distribution*), selezione in un array, inviluppo convesso (*convex hulls*), …

L'ordinamento sta al cuore di molti algoritmi: ordinare i dati è una delle prime cose che un progettista di algoritmi dovrebbe provare nella ricerca dell'efficienza.

### Idea · [[05-Insertion sort.pdf#page=4|p. 4]], [[05-Insertion sort.pdf#page=1|p. 1]]

- Insertion sort è un algoritmo che **considera un valore alla volta** e lo **inserisce nella corretta posizione tra i valori che lo precedono**.
- È un algoritmo che ordina i valori **sul posto** (*in place*): i valori sono riordinati all'interno dell'array stesso, con **al più un numero costante** di essi memorizzati al di fuori dell'array in ogni momento.

### Proprietà · [[05-Insertion sort.pdf#page=4|p. 4]]

- **Sul posto** (in place) — dalla fonte.

### Pseudocodice · 05-Insertion sort.pdf [[05-Insertion sort.pdf#page=5|p. 5]], [[05-Insertion sort.pdf#page=19|p. 19]] · Pseudocodice [[a1-indicazioni_psuedocodice.pdf#page=4|p. 4]]

```
Insertion-Sort (A)
1  for j ← 2 to length[A]
2      do key ← A[j]
3         // Insert A[j] into A[1..j-1]
4         i ← j-1
5         while i>0 and A[i]>key
6             do A[i+1] ← A[i]
7                i ← i-1
8         A[i+1] ← key
```

Significato delle variabili:
- $j$ = indice dell'elemento da inserire (la «carta» presa in mano); il ciclo parte da 2 perché $A[1]$ da solo è già ordinato;
- $key$ = copia di $A[j]$, che durante gli spostamenti verrebbe sovrascritto;
- $i$ = indice che scorre verso sinistra in $A[1..j-1]$ cercando il posto di $key$.

La condizione `i>0 and A[i]>key` sfrutta il **corto circuito** di `and`: quando $i = 0$ il confronto `A[0] > key` non viene valutato, ed è giusto così perché $A[0]$ non esiste (indici da 1).

> ⚠️ Contraddizione (di notazione): la slide usa `do` e il commento `//` (stile della 2ª edizione del Cormen), mentre le [[pseudocodice|convenzioni del corso]] prevedono commenti con $\triangleright$ e nessun `do`. Il significato è lo stesso.

### Esempio di esecuzione · [[05-Insertion sort.pdf#page=5|p. 5]], [[05-Insertion sort.pdf#page=17|p. 17]], [[05-Insertion sort.pdf#page=8|p. 8]], [[05-Insertion sort.pdf#page=9|p. 9]], [[05-Insertion sort.pdf#page=10|p. 10]], [[05-Insertion sort.pdf#page=11|p. 11]], [[05-Insertion sort.pdf#page=12|p. 12]], [[05-Insertion sort.pdf#page=13|p. 13]], [[05-Insertion sort.pdf#page=14|p. 14]], [[05-Insertion sort.pdf#page=15|p. 15]], [[05-Insertion sort.pdf#page=16|p. 16]]

Array iniziale: $A = \langle 5, 2, 4, 6, 1, 3 \rangle$.

![[05-insertion-sort-p5-traccia-inizio.png]]
*Stato iniziale: casella `key` vuota e array ⟨5, 2, 4, 6, 1, 3⟩.*

| Slide | $j$ | $key$ | Cosa succede | $A$ dopo l'iterazione |
|---|---|---|---|---|
| p. 8, p. 9 | 2 | 2 | 5 > 2: il 5 scorre a destra, 2 va in $A[1]$ | ⟨**2**, 5, 4, 6, 1, 3⟩ |
| p. 10, p. 11 | 3 | 4 | 5 > 4 scorre; 2 ≤ 4 si ferma: 4 va in $A[2]$ | ⟨2, **4**, 5, 6, 1, 3⟩ |
| p. 12, p. 13 | 4 | 6 | 5 ≤ 6: nessuno spostamento | ⟨2, 4, 5, **6**, 1, 3⟩ |
| p. 14, p. 15 | 5 | 1 | 6, 5, 4, 2 scorrono tutti; $i$ arriva a 0 | ⟨**1**, 2, 4, 5, 6, 3⟩ |
| p. 16, p. 17 | 6 | 3 | 6, 5, 4 scorrono; 2 ≤ 3 si ferma | ⟨1, 2, **3**, 4, 5, 6⟩ |

![[05-insertion-sort-p15-traccia-completa.png]]
*Traccia completa: ogni riga è lo stato dopo un'iterazione del `for`, con il valore di `key` a sinistra.*

### Appunti a mano: invariante e costo di Insertion Sort · [[05-Insertion sort.pdf#page=6|p. 6]]

![[05-insertion-sort-p6-appunti-invariante-e-costo.png]]
*Pagina di appunti del docente: invariante del ciclo `for` (inizializzazione, conservazione, conclusione), tabella dei costi $c_i$ e dei numeri di esecuzioni $t_j$, somma e caso migliore ($t_j = 1$); nota sul caso peggiore (array ordinato in senso opposto) e sui valori $t_j = j$.*

### Appunti a mano: il caso peggiore e il limite superiore · [[05-Insertion sort.pdf#page=7|p. 7]]

![[05-insertion-sort-p7-appunti-limite-inferiore.png]]
*Appunti sul significato della notazione $O$: esiste una funzione $g$ con $m^2 = O(g(m))$ da un certo $m_0$ in poi, quindi $c \cdot g(m)$ è un limite superiore di $m^2$.*

### Correttezza · [[05-Insertion sort.pdf#page=18|p. 18]]

**Invariante:** all'inizio di ciascuna iterazione del ciclo `for`, la sottosequenza $A[1..j-1]$ consiste degli **elementi originali** di $A[1..j-1]$, ma **ordinati** in senso crescente.

- **Inizializzazione** — l'invariante è vero prima della prima iterazione: per $j = 2$ la sottosequenza $A[1..j-1]$ è costituita solo da $A[1]$, che è ovviamente una sequenza ordinata.
- **Conservazione** — un'iterazione del ciclo conserva la verità dell'invariante: l'elemento $A[j]$ viene inserito in modo da mantenere la sequenza $A[1..j]$ ordinata.
- **Conclusione** — l'invariante prova che l'algoritmo è corretto: il ciclo termina quando $j = n + 1$, ovvero quando la sequenza $A[1..n]$ è ordinata.

![[05-insertion-sort-p16-invariante.png]]

### Tabella dei costi · [[05-Insertion sort.pdf#page=19|p. 19]]

| Riga | Istruzione | Costo | Numero di esecuzioni |
|---|---|---|---|
| 1 | `for j ← 2 to length[A]` | $c_1$ | $n$ |
| 2 | `do key ← A[j]` | $c_2$ | $n - 1$ |
| 3 | `// Insert A[j] into A[1..j-1]` | — | — |
| 4 | `i ← j-1` | $c_4$ | $n - 1$ |
| 5 | `while i>0 and A[i]>key` | $c_5$ | $\sum_{j=2}^{n} t_j$ |
| 6 | `do A[i+1] ← A[i]` | $c_6$ | $\sum_{j=2}^{n} (t_j - 1)$ |
| 7 | `i ← i-1` | $c_7$ | $\sum_{j=2}^{n} (t_j - 1)$ |
| 8 | `A[i+1] ← key` | $c_8$ | $n - 1$ |

**$t_j$ è il numero di volte che viene eseguito il test del ciclo `while`** (per quel valore di $j$).

![[05-insertion-sort-p17-tabella-costi.png]]

### Formula generale · [[05-Insertion sort.pdf#page=20|p. 20]], [[05-Insertion sort.pdf#page=21|21]]

> 🧮 Formula chiave:
$$
T(n) = c_1 n + c_2 (n-1) + c_4 (n-1) + c_5 \sum_{j=2}^{n} t_j + c_6 \sum_{j=2}^{n} (t_j - 1) + c_7 \sum_{j=2}^{n} (t_j - 1) + c_8 (n-1)
$$

Il tempo dipende dall'**input**, non solo da $n$: le tre sommatorie (cerchiate in p. 21) dipendono da quanti elementi scorrono, cioè da quanto l'array è già in ordine.

### Caso migliore · [[05-Insertion sort.pdf#page=22|p. 22]]

Il **caso migliore** si verifica quando il vettore è **già ordinato** ($t_j = 1$):
$$ T(n) = c_1 n + c_2(n-1) + c_4(n-1) + c_5(n-1) + c_8(n-1) = an + b $$
Il tempo di esecuzione è **funzione lineare** di $n$.

$$
\begin{aligned}
t_j &= 1 && \text{il primo test trova } A[j-1] \le key \text{ e fallisce} \\
\textstyle\sum_{j=2}^{n} t_j &= n - 1, \qquad \textstyle\sum_{j=2}^{n} (t_j - 1) = 0 && \text{righe 6 e 7 mai eseguite} \\
T(n) &= (c_1 + c_2 + c_4 + c_5 + c_8)\, n - (c_2 + c_4 + c_5 + c_8) && \text{raccolgo } n \\
     &= an + b = \Theta(n) && a = c_1 + c_2 + c_4 + c_5 + c_8 > 0,\ b = -(c_2 + c_4 + c_5 + c_8)
\end{aligned}
$$

![[05-insertion-sort-p20-caso-migliore.png]]

### Caso peggiore · 05-Insertion sort.pdf [[05-Insertion sort.pdf#page=23|p. 23]], [[05-Insertion sort.pdf#page=24|24]] · 01-Introduzione.pdf [[01-Introduzione.pdf#page=11|p. 11]]

Il **caso peggiore** si verifica quando il vettore è **ordinato in senso decrescente**. Si usano le due sommatorie:
$$ \sum_{j=2}^{n} j = \frac{n(n+1)}{2} - 1 \qquad\qquad \sum_{j=2}^{n} (j-1) = \frac{n(n-1)}{2} $$
e si ottiene:
$$
T(n) = c_1 n + c_2(n-1) + c_4(n-1) + c_5\left(\frac{n(n+1)}{2} - 1\right) + c_6 \frac{n(n-1)}{2} + c_7 \frac{n(n-1)}{2} + c_8(n-1)
$$
$$ T(n) = an^2 + bn + c $$
Il tempo di esecuzione è **funzione quadratica** di $n$.

$$
\begin{aligned}
t_j &= j && key \text{ è minore di tutti i } j-1 \text{ elementi di } A[1..j-1]\text{: } j-1 \text{ test veri} + 1 \text{ falso } (i = 0) \\
\textstyle\sum_{j=2}^{n} j &= \textstyle\sum_{j=1}^{n} j - 1 = \frac{n(n+1)}{2} - 1 && \text{Gauss, tolgo il termine } j = 1 \\
\textstyle\sum_{j=2}^{n} (j-1) &= \textstyle\sum_{k=1}^{n-1} k = \frac{(n-1)n}{2} && k = j - 1 \\
T(n) &= \frac{c_5 + c_6 + c_7}{2}\, n^2 + \left(c_1 + c_2 + c_4 + \frac{c_5 - c_6 - c_7}{2} + c_8\right) n - (c_2 + c_4 + c_5 + c_8) && \text{sviluppo e raccolgo} \\
     &= an^2 + bn + c = \Theta(n^2) && a = \tfrac{c_5 + c_6 + c_7}{2} > 0
\end{aligned}
$$
>
> **Sanity check** ([[ordinamento.py]]): per $n = 5$ decrescente $\sum t_j = 14 = \frac{5\cdot6}{2} - 1$ e $\sum(t_j - 1) = 10 = \frac{5\cdot4}{2}$; per $n = 100$: 5049 e 4950. Sull'array della traccia $\sum t_j = 2+2+1+5+4 = 14$, un caso intermedio.
> **Ipotesi:** [[modello-ram]], costo costante $c_i$ per riga; caso peggiore = ogni $key$ è minore di tutti gli elementi che lo precedono.

![[05-insertion-sort-p22-caso-peggiore.png]]

![[grafico-insertion-sort-casi.svg]]

**Spazio:** $\Theta(1)$ oltre all'array ($key$, $i$, $j$) — è la proprietà «sul posto» di p. 4.

### Implementazione in C++ · 05-Insertion sort.pdf [[05-Insertion sort.pdf#page=25|p. 25]] · Pseudocodice [[a1-indicazioni_psuedocodice.pdf#page=3|p. 3]]

```cpp
template <typename T>
void InsertionSort (vector<T> A)
{
    for (int j=1; j<A.size(); j++)
    {
        T key = A[j];
        // Insert A[j] into A[1..j-1]
        int i = j-1;
        while (i>=0 && A[i]>key)
        {
            A[i+1] = A[i];
            i--;
        }
        A[i+1] = key;
    }
}
```

> ⚠️ Contraddizione (🧩 osservazione mia sul codice della slide): `vector<T> A` è passato **per valore**, quindi la funzione ordina una **copia** e il vettore del chiamante resta invariato. Per ordinare davvero serve il passaggio per riferimento, `vector<T>& A`. Nello pseudocodice il problema non si pone: gli array sono aggregati passati per riferimento.

![[05-insertion-sort-p23-implementazione-cpp.png]]

### Traccia dell'esercizio e idea · [[05-Insertion sort.pdf#page=26|p. 26]]

**Pseudo-code** (a parole):
- trova l'elemento **più piccolo** e scambialo con il **primo** elemento;
- trova il **secondo più piccolo** e scambialo con il **secondo** elemento;
- ripeti, trovando il successivo più piccolo e scambiandolo nella posizione corretta, per i **primi $n - 1$ elementi**.

Consegne: **Implementa**. **Analizza**: quale invariante di ciclo conserva? Perché bisogna eseguirlo fino ad $n - 1$ anziché $n$? Esprimere nella notazione $\Theta$ i tempi di esecuzione migliore e peggiore.

![[05-insertion-sort-p24-esercizio-selection-sort.png]]

### Appunti a mano: codice di Selection Sort · [[05-Insertion sort.pdf#page=27|p. 27]]

![[05-insertion-sort-p27-appunti-selection-sort-codice.png]]
*Pseudocodice scritto a mano: `Selection-Sort (A)`, `for i ← 1 to ⌊length[A]-1⌋`, `min ← i`, `for j ← i+1 to length[A]`, `if (A[min] > A[j]) min ← j`, `swap (A[min], A[i])`.*

### Pseudocodice (implementazione) · [[05-Insertion sort.pdf#page=28|p. 28]]

```c
selection_sort(int s[], int n) {
1     int i,j;        /* counters */
2     int min;        /* index of minimum */
3     for (i=0; i<n; i++) {
4         min=i;
5         for (j=i+1; j<n; j++)
6             if (s[j] < s[min]) min=j;
7         swap(s[i],s[min]);
8     }
}
```

```
SELECTION-SORT(A)
1  n ← length[A]
2  for i ← 1 to n − 1
3      min ← i
4      for j ← i + 1 to n
5          if A[j] < A[min]
6              min ← j
7      scambia A[i] con A[min]
```

### Appunti a mano: costo e correttezza di Selection Sort · [[05-Insertion sort.pdf#page=29|p. 29]]

![[05-insertion-sort-p29-appunti-selection-sort-costo-e-correttezza.png]]
*Appunti sul codice C di Selection Sort: costi $c_1, \dots, c_7$, somma $T(n) = c_1 n + \dots$ che dà un polinomio di secondo grado; poi la dimostrazione di correttezza con l'invariante del ciclo interno (`min` è l'indice del minimo di $A[i..j-1]$; inizializzazione, continuazione, conclusione).*

### Appunti a mano: invariante del ciclo esterno di Selection Sort · [[05-Insertion sort.pdf#page=30|p. 30]]

![[05-insertion-sort-p30-appunti-selection-sort-invariante.png]]
*Ciclo `for` (trascrizione, lettura parzialmente incerta). **Invariante:** l'array $A[1..i-1]$ contiene gli $i-1$ elementi minimi dell'array originale, ordinati. **Inizializzazione:** per $i = 1$ il sottoarray $A[1..0]$ è vuoto, quindi l'invariante è soddisfatto. **Conservazione:** nell'iterazione $i$ l'algoritmo di ricerca trova l'indice del minimo di $A[i..n]$ e lo porta in posizione $i$; per la correttezza della ricerca, $A[i]$ è maggiore o uguale di ogni elemento di $A[1..i-1]$ e minore o uguale di ciascuno di $A[i+1..n]$; quindi l'iterazione successiva $i+1$ verifica l'invariante. **Conclusione:** quando $i = n$, $A[1..n-1]$ contiene $n-1$ elementi dell'array originale ordinati in senso crescente: l'ultimo elemento è ordinato per la correttezza della ricerca del minimo.*

### Correttezza · [[05-Insertion sort.pdf#page=31|p. 31]]

### Complessità · [[05-Insertion sort.pdf#page=32|p. 32]], [[05-Insertion sort.pdf#page=33|33]]

$$ \sum_{i=0}^{n-2} (n - 1 - i) = (n-1) + (n-2) + \dots + 1 = \frac{n(n-1)}{2} $$

![[05-insertion-sort-p28-somma-confronti-selection.png]]

$$
\begin{aligned}
\text{confronti con } i \text{ fissato} &= (n-1) - (i+1) + 1 = n - 1 - i && j = i+1, \dots, n-1 \text{ (codice C, indici da 0)} \\
\text{confronti totali} &= \sum_{i=0}^{n-2} (n-1-i) && i = n-1 \text{ contribuisce } 0 \\
&= \sum_{k=1}^{n-1} k = \frac{n(n-1)}{2} && k = n - 1 - i \\
&= \Theta(n^2)
\end{aligned}
$$
>
> **Caso migliore = caso peggiore = $\Theta(n^2)$** (terza domanda di p. 26): il numero di confronti **non dipende dall'input**, perché il ciclo interno scorre sempre tutto $A[i+1..n]$ per trovare il minimo; anche un array già ordinato paga $\frac{n(n-1)}{2}$ confronti. Cambia solo quante volte si esegue `min=j` (al più una volta per confronto), il che non sposta l'ordine di crescita. Gli scambi sono esattamente uno per iterazione esterna: $\Theta(n)$.
>
> **Sanity check** ([[ordinamento.py]]): per $n = 100$, 4950 confronti su input ordinato, decrescente e casuale; $\frac{100\cdot 99}{2} = 4950$.

### Memoria · [[05-Insertion sort.pdf#page=34|p. 34]]

### Definizione formale · [[05-Insertion sort.pdf#page=35|p. 35]]

- **Problem:** Substring Pattern Matching
- **Input:** una stringa di testo $t$ e una stringa pattern $p$.
- **Output:** $t$ contiene il pattern $p$ come sottostringa? E se sì, **dove**?

Simboli (dal codice di p. 36): $n$ = lunghezza di $t$, $m$ = lunghezza di $p$.

### Esempio della fonte · [[05-Insertion sort.pdf#page=35|p. 35]]

![[05-insertion-sort-p30-pattern-matching-esempio.png]]
*Ricerca della sottostringa **abba** nel testo **aababba**: ogni riga è un tentativo, spostato di una posizione a destra, con i caratteri del pattern effettivamente confrontati.*

| Tentativo (posizione $i$) | Caratteri di $p$ confrontati | Esito |
|---|---|---|
| 0 | `a b` | $t[1] = a \ne b$: fallisce al 2° carattere |
| 1 | `a b b` | $t[3] = a \ne b$: fallisce al 3° carattere |
| 2 | `a` | $t[2] = b \ne a$: fallisce subito |
| 3 | `a b b a` | tutti uguali: **trovato in posizione 3** (4° carattere, contando da 1) |

Totale: $2 + 3 + 1 + 4 = 10$ confronti di caratteri (verificato con [[stringhe_e_logaritmi.py]]).

### Algoritmi che lo risolvono · [[05-Insertion sort.pdf#page=35|p. 35]], [[05-Insertion sort.pdf#page=36|36]]

| Algoritmo | Costo nel caso peggiore |
|---|---|
| [[findmatch]] (forza bruta) | $O(nm)$ — 🧩 derivazione nella pagina dell'algoritmo |

La consegna della slide è «**Valutare l'efficienza asintotica**».

### Pseudocodice · [[05-Insertion sort.pdf#page=36|p. 36]]

```c
int findmatch(char *p, char *t) {
1   int i,j;        /* counters */
2   int m, n;       /* string lengths */
3   m = strlen(p);
4   n = strlen(t);
5   for (i=0; i<=(n-m); i=i+1) {
6       j=0;
7       while ((j<m) && (t[i+j]==p[j]))
8           j = j+1;
9       if (j == m) return(i);
10  }
11  return(-1);
}
```

Restituisce la prima posizione (da 0) in cui compare $p$, oppure $-1$.

![[05-insertion-sort-p31-findmatch.png]]

### Complessità · [[05-Insertion sort.pdf#page=36|p. 36]]

$$
\begin{aligned}
\text{iterazioni del for} &\le n - m + 1 && i = 0, \dots, n - m \\
\text{confronti del while per ogni } i &\le m && j \text{ va da } 0 \text{ a } m \\
T_{worst}(n, m) &= (n - m + 1)\, m + O(n + m) && \text{più } \texttt{strlen} \text{ (righe 3–4)} \\
&= O(nm) && m \le n
\end{aligned}
$$
>
> **Istanza peggiore:** $t = aaa\dots a$ ($n$ volte) e $p = a\dots ab$ ($m-1$ volte $a$, poi $b$). In ogni posizione i primi $m - 1$ caratteri coincidono e l'ultimo no, quindi ogni tentativo costa esattamente $m$ confronti e non c'è mai un'occorrenza. Esempio: $n = 1000$, $m = 500$ → $501 \cdot 500 = 250\,500$ confronti (misurati con [[stringhe_e_logaritmi.py]]).
>
> **Caso migliore:** $p$ compare in posizione 0 → $m$ confronti (più il costo di `strlen`).
>
> **In funzione della sola $n$:** $(n - m + 1)\,m$ è massimo per $m \approx n/2$ e vale circa $n^2/4$, quindi nel caso peggiore l'algoritmo è quadratico nella lunghezza del testo.
>
> **Ipotesi:** [[modello-ram]], confronto di due caratteri in tempo costante.

### Definizione · [[05-Insertion sort.pdf#page=37|p. 37]]

*«Logarithms arise in any process where things are repeatedly halved.»* I logaritmi compaiono in ogni processo in cui qualcosa viene **ripetutamente dimezzato** (o diviso per una costante).

### Formule · [[05-Insertion sort.pdf#page=37|p. 37]]

Esempi elencati nella slide, con i passaggi che la slide lascia impliciti:

| Esempio (slide) | Risultato | Derivazione (🧩 mia dove la slide non la dà) |
|---|---|---|
| **Binary Search** | $O(\lg n)$ confronti | ogni confronto dimezza l'intervallo di ricerca (vedi p. 38, sotto) |
| **Trees** — altezza $h$ di un albero con $d$ figli per nodo e $n$ foglie | $h = \log_d n$ | un albero completo di altezza $h$ ha $d^h$ foglie: $d^h = n \Rightarrow h = \log_d n$ |
| **Bits** — quanti bit servono per rappresentare una qualunque tra $n$ possibilità? | $\lceil \lg n \rceil$ | con $b$ bit si distinguono $2^b$ valori: serve $2^b \ge n \Rightarrow b = \lceil \lg n \rceil$ |
| **Multiplication** | $a^b = \exp(\ln(a^b)) = \exp(b \ln a)$ | proprietà $\ln(a^b) = b \ln a$: il logaritmo trasforma potenze in prodotti (e prodotti in somme) |
| **Fast exponentiation** | $O(\lg n)$ moltiplicazioni | vedi [[potenza-veloce]] |
| **Summation** — numeri armonici | $H(n) = \sum_{i=1}^{n} \frac{1}{i} \sim \ln n$ | vedi derivazione sotto |

**Numeri (🧩, calcolati con [[stringhe_e_logaritmi.py]]):** albero binario con 8 foglie → $h = 3$; albero con $d = 10$ e $10^6$ foglie → $h = 6$; per $n = 10^6$ possibilità servono 20 bit.

![[05-insertion-sort-p32-logaritmi.png]]

### Idea · [[05-Insertion sort.pdf#page=37|p. 37]]

$$ a^n = \left(a^{n/2}\right)^2 \ \text{se } n \text{ è pari}, \qquad a^n = a\left(a^{\lfloor n/2 \rfloor}\right)^2 \ \text{se } n \text{ è dispari} $$

«This requires $O(\lg n)$ mult.»

### Pseudocodice · [[05-Insertion sort.pdf#page=37|p. 37]]

```
function power(a,n)
1  if (n = 0) return(1)
2  x = power(a, ⌊n/2⌋)
3  if (n is even) then return(x²)
4      else return(a * x²)
```

*Approfondimenti nel wiki: [[lezione-05-insertion-sort]], [[insertion-sort]], [[selection-sort]], [[substring-pattern-matching]], [[findmatch]], [[logaritmi-nell-analisi]], [[potenza-veloce]]*

## Lezione 6 — Merge Sort

*Fonte: 06-Merge Sort (1).pdf.*

### Definizione formale · [[06-Merge Sort (1).pdf#page=2|p. 2]], [[06-Merge Sort (1).pdf#page=3|3]], [[06-Merge Sort (1).pdf#page=1|p. 1]]

La slide di apertura rimanda all'esercizio interattivo di Khan Academy «move three disks in Towers of Hanoi» (link in p. 2).

**Problema**:
- spostare tutti i dischi dalla torre **sorgente** alla torre **destinazione** (ad esempio dal centro a sinistra);
- si può muovere **un solo disco alla volta**;
- non si può mai appoggiare un disco **più grande** sopra uno **più piccolo**.

**Domanda:** come possiamo trasformare il problema con $n$ dischi in uno o più problemi più piccoli, ma **dello stesso tipo**?

La figura mostra tre pioli (*Tower*) e una pila di dischi (*Disks*) di dimensione decrescente sul piolo centrale, dal più grande (*Largest*) in basso al più piccolo (*Smallest*) in alto.

![[06-merge-sort-p3-torre-di-hanoi.png]]

### Approccio divide et impera · [[06-Merge Sort (1).pdf#page=4|p. 4]], [[06-Merge Sort (1).pdf#page=10|p. 10]]

- **Dividere** il problema iniziale in uno o più sottoproblemi fino ad arrivare al caso base. Ad esempio: sposto solo la **sotto-torre** fatta dai dischi verde e arancione dal centro ad uno dei lati.
- Il problema più «piccolo» è lo spostamento di un **solo disco generico** da una torre di partenza ad una di destinazione: è il **caso base**.
- Serve una strategia che permetta di ottenere la soluzione originale **combinando** le soluzioni di tutti i sottoproblemi, incluso il caso base.

![[06-merge-sort-p4-hanoi-divide-et-impera.png]]

Annotazione a mano sulla slide: «Mi serve un algoritmo che gestisce la **fase decrescente**» (freccia verso il basso) e «**fase ascendente** → si combinano le soluzioni trovate» (freccia verso l'alto; l'ultima parola è di lettura incerta). È la distinzione tra la discesa delle chiamate ricorsive e la loro risalita, ripresa per merge sort in p. 10 (→ [[merge-sort]]).

### Sequenza delle mosse per tre dischi · [[06-Merge Sort (1).pdf#page=5|p. 5]]

La slide mostra otto configurazioni numerate da 1 a 8: lo stato iniziale e i sette stati dopo ogni mossa.

![[06-merge-sort-p5-hanoi-mosse.png]]

| Stato | Mossa che lo produce | A | B | C |
|---|---|---|---|---|
| 1 | — | 3, 2, 1 | — | — |
| 2 | disco 1: A → C | 3, 2 | — | 1 |
| 3 | disco 2: A → B | 3 | 2 | 1 |
| 4 | disco 1: C → B | 3 | 2, 1 | — |
| 5 | disco 3: A → C | — | 2, 1 | 3 |
| 6 | disco 1: B → A | 1 | 2 | 3 |
| 7 | disco 2: B → C | 1 | — | 3, 2 |
| 8 | disco 1: A → C | — | — | 3, 2, 1 |

### Idea · [[06-Merge Sort (1).pdf#page=7|p. 7]], [[06-Merge Sort (1).pdf#page=17|p. 17]], [[06-Merge Sort (1).pdf#page=6|p. 6]]

- Approccio **[[divide-et-impera]]**:
  - **suddivide** una sequenza di $n$ elementi in due sottosequenze di $n/2$ elementi;
  - **ordina** le sottosequenze ricorsivamente,
  - fino ad ottenere una sottosequenza di lunghezza 1, che è ordinata;
  - **combina** («merge») due sottosequenze ordinate per produrre l'intera sequenza ordinata.
- Due funzioni:
  - **[[merge|Merge]]** combina due sottosequenze ordinate in una sequenza ordinata;
  - **Merge-Sort** ordina una sequenza suddividendola in due sottosequenze, ordinando ciascuna sottosequenza (mediante chiamata ricorsiva) e invocando la funzione Merge per ottenere la sequenza ordinata.
- **Non** effettua un ordinamento sul posto (**ATTENZIONE!!!**, in rosso nella slide).

Annotazioni a mano sulla slide:
- «array dinamico è solo una forma di gestione dell'array»: usare un [[array-dinamico]] non rende l'ordinamento «sul posto», cambia solo come si gestisce la memoria;
- «Perché dividiamo in due i sottoarray? perché non dividiamo per $n$?» con la risposta «l'algoritmo ricorsivo si riduce ad un for e chiamata a funzione → la fase crescente».

### Correttezza · [[06-Merge Sort (1).pdf#page=7|p. 7]], [[06-Merge Sort (1).pdf#page=20|p. 20]], [[06-Merge Sort (1).pdf#page=21|21]]

La slide non dimostra la correttezza di Merge-Sort; dimostra quella di [[merge]].

### Appunti a mano: perché dividere il problema in 2 parti · [[06-Merge Sort (1).pdf#page=8|p. 8]]

Perché 2 è il fattore per cui dividiamo il problema? Perché non dividerlo direttamente in $n$ sottoproblemi?
- **Fase decrescente:** diventa banale; ogni pezzo ha un suo elemento, quindi ogni chiamata ricorsiva cade subito nel caso base.
- **Fase crescente:** si dovrebbero fondere $n$ sequenze in un colpo solo; qui il costo esplode, la complessità aumenta e ci si avvicina a un algoritmo iterativo.

Inoltre, più è grande il fattore per cui si divide il problema, più si avvicina a un algoritmo iterativo.

### Esempio di esecuzione · [[06-Merge Sort (1).pdf#page=9|p. 9]]

La slide mostra l'albero di ricorsione su ⟨5, 2, 8, 0, 4, 7, 1, 9, 3, 2, 6⟩ ($n = 11$): in discesa le divisioni, fino a sequenze di un elemento; in risalita le fusioni.

![[06-merge-sort-p8-albero-merge-sort.png]]
*Albero delle fusioni: dalle foglie (un elemento) fino alla sequenza ordinata ⟨0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9⟩.*

| Profondità | Sotto-sequenze dopo la divisione | Risultato delle fusioni a quel livello |
|---|---|---|
| 0 | ⟨5, 2, 8, 0, 4, 7, 1, 9, 3, 2, 6⟩ | ⟨0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9⟩ |
| 1 | ⟨5, 2, 8, 0, 4, 7⟩, ⟨1, 9, 3, 2, 6⟩ | ⟨0, 2, 4, 5, 7, 8⟩, ⟨1, 2, 3, 6, 9⟩ |
| 2 | ⟨5, 2, 8⟩, ⟨0, 4, 7⟩, ⟨1, 9, 3⟩, ⟨2, 6⟩ | ⟨2, 5, 8⟩, ⟨0, 4, 7⟩, ⟨1, 3, 9⟩, ⟨2, 6⟩ |
| 3 | ⟨5, 2⟩, ⟨8⟩, ⟨0, 4⟩, ⟨7⟩, ⟨1, 9⟩, ⟨3⟩, ⟨2⟩, ⟨6⟩ | ⟨2, 5⟩, ⟨0, 4⟩, ⟨1, 9⟩ (le altre sono singoli) |
| 4 | ⟨5⟩, ⟨2⟩, ⟨0⟩, ⟨4⟩, ⟨1⟩, ⟨9⟩ | foglie |

### Prima versione: vettori $L$ e $R$ · [[06-Merge Sort (1).pdf#page=10|p. 10]]–[[06-Merge Sort (1).pdf#page=13|13]]

```
MergeSort(A)
1  se A ha un solo elemento
2      ritorna A
3  dividi A in L e R
4  L ← MergeSort(L)
5  R ← MergeSort(R)
6  ritorna Merge(L, R)
```

Accanto allo pseudocodice la slide schematizza le tre fasi dell'esecuzione:
1. **Discesa** — se non sono nel caso base, divido il problema e richiamo la stessa funzione;
2. **Caso base** — un vettore con un solo elemento è già ordinato: non c'è nulla da fare;
3. **Risalita** — quando i sottoproblemi sono ordinati, li fondo con un merge ordinato.

![[06-merge-sort-p9-pseudocodice-con-vettori.png]]

Annotazioni a mano: «Caso base — fase ascendente» accanto alle righe 1–2, «Caso ricorsivo — fase decrescente» accanto alle righe 3–6; a p. 12, tra le righe 5 e 6, «qui $L$ e $R$ arrivano ordinati».

> ⚠️ Contraddizione (di notazione): questa prima versione è uno schizzo in italiano («se», «ritorna», «dividi A in L e R») e non segue le [[pseudocodice|convenzioni del corso]]; la slide stessa la presenta con un punto interrogativo. La versione definitiva è quella di p. 23.

**Criticità?**:
- il caso base non fa praticamente nessuna operazione;
- ho necessità di una seconda funzione (non ricorsiva) che fonda $L$ e $R$ in maniera ordinata;
- $L$ e $R$ sono due **nuovi vettori** allocati da Merge-Sort e poi passati ricorsivamente a Merge-Sort e poi nuovamente a Merge.

**Posso migliorare qualcosa?**

### Miglioramento: dal vettore agli indici · [[06-Merge Sort (1).pdf#page=14|p. 14]], [[06-Merge Sort (1).pdf#page=15|15]]

**Un sottoproblema non è un nuovo array: è una porzione dell'array originale.** La figura mostra $A = \langle 5, 2, 8, 1, 4, 7, 3, 6 \rangle$ con la metà sinistra $A[p..q] = \langle 5, 2, 8, 1 \rangle$ (in blu) e la destra $A[q+1..r] = \langle 4, 7, 3, 6 \rangle$ (in rosso).

```
MergeSort(A, p, r)
1  se p = r
2      ritorna
3  q ← floor((p + r) / 2)
4  MergeSort(A, p, q)
5  MergeSort(A, q+1, r)
6  Merge(A, p, q, r)
```

- $p = r$ indica un sottovettore di un solo elemento;
- $q$ è lo **split** che divide logicamente $A[p..r]$ in due metà;
- le chiamate ricorsive ordinano **direttamente** le due porzioni di $A$;
- Merge viene chiamato solo dopo che entrambe le metà sono ordinate;
- il caso base resta identico;
- ho sempre bisogno della funzione merge;
- sia Merge che Merge-Sort operano sempre e solo su $A$, usando **indici** per la gestione dei sotto-array.

![[06-merge-sort-p13-merge-sort-con-indici.png]]

**Tutto troppo bello?**

### Sotto-array e merge: dove nasce il «non in-place» · [[06-Merge Sort (1).pdf#page=16|p. 16]]

Merge deve utilizzare **memoria accessoria** per copiare il contenuto dei sotto-vettori, per evitare perdite durante l'inserimento in $A$, che a questo punto è una **sovrascrittura**. La creazione effettiva di $L$ e $R$ è **spostata da Merge-Sort a Merge**; il ciclo di Merge fa un «pop» da $L$ e $R$ e inserisce con sovrascrittura in $A$ (pseudocodice in [[merge]]).

**Qui nasce il «non in-place»**: la memoria ausiliaria non serve solo per dividere, ma per fondere in modo semplice e sicuro.

### Prima versione (senza sentinelle) · [[06-Merge Sort (1).pdf#page=16|p. 16]]

Nel passaggio dalla prima versione di Merge-Sort a quella con gli indici (→ [[merge-sort]] § Dal primo pseudocodice alla versione con indici), la creazione di $L$ e $R$ viene **spostata da Merge-Sort a Merge**. Merge deve usare memoria accessoria per copiare i sotto-vettori, perché l'inserimento in $A$ è ora una **sovrascrittura** e senza copie si perderebbero elementi.

```
Merge(A, p, q, r)
1  copia A[p..q]   in L
2  copia A[q+1..r] in R
3  i ← 1
4  j ← 1
5  per k da p a r
6      se L[i] ≤ R[j]
7          A[k] ← L[i]
8          i ← i + 1
9      altrimenti
10         A[k] ← R[j]
11         j ← j + 1
```

- righe 1–2: **creazione effettiva di $L$ e $R$** (spostata da Merge-Sort a Merge);
- righe 5–11: **inserimento in ordine**, cioè «pop» da $L$ e $R$ e inserimento con sovrascrittura in $A$.

Qui nasce il «non in-place»: la memoria ausiliaria non serve solo per dividere, ma per fondere in modo semplice e sicuro.

![[06-merge-sort-p15-merge-semplificato.png]]

Annotazioni a mano: accanto alle righe 1–2 «faceva parte della fase discendente pre modifiche» (nella prima versione di Merge-Sort le copie si facevano dividendo, cioè in discesa); accanto al ciclo «fase ascendente».

### Problema risolto · [[06-Merge Sort (1).pdf#page=7|p. 7]], [[06-Merge Sort (1).pdf#page=17|p. 17]], [[06-Merge Sort (1).pdf#page=23|p. 23]]

**Merge** combina due sottosequenze ordinate in una sequenza ordinata. È la prima delle «due funzioni» di [[merge-sort]]; l'altra, Merge-Sort, la invoca per ricombinare le metà ordinate.

- **Input:** un array $A$ e tre indici $p \le q < r$ tali che $A[p..q]$ e $A[q+1..r]$ sono **già ordinati**.
- **Output:** $A[p..r]$ contiene gli stessi elementi, **ordinati**.

### Pseudocodice (codice completo) · [[06-Merge Sort (1).pdf#page=17|p. 17]], [[06-Merge Sort (1).pdf#page=18|18]], [[06-Merge Sort (1).pdf#page=22|p. 22]]

```
Merge (A,p,q,r)
1  n1 ← q-p+1
2  n2 ← r-q
3  // create L[1..n1+1] and R[1..n2+1]
4  for i ← 1 to n1
5      do L[i] ← A[p+i-1]
6  for j ← 1 to n2
7      do R[j] ← A[q+j]
8  L[n1+1] ← R[n2+1] ← ∞
9  i ← j ← 1
10 for k ← p to r
11     do if L[i] ≤ R[j]
12         then A[k] ← L[i]
13              i ← i+1
14         else A[k] ← R[j]
15              j ← j+1
```

Significato dei simboli:
- $n_1$, $n_2$ = lunghezze delle due metà $A[p..q]$ e $A[q+1..r]$; $n = n_1 + n_2 = r - p + 1$;
- $L$, $R$ = copie delle due metà, con una cella in più per la sentinella $\infty$;
- $i$, $j$ = indice del primo elemento di $L$ e di $R$ non ancora ricopiato in $A$;
- $k$ = posizione di $A$ da riempire.

Accanto al codice la slide ripete i punti dell'idea di merge sort e aggiunge:
- **è una funzione iterativa!!** (Merge-Sort è ricorsiva, Merge no);
- **non** effettua un ordinamento sul posto: infatti non fa proprio ordinamento, ma piuttosto **inserisce elementi in $A$ in maniera ordinata**, prendendoli da $L$ e $R$.

![[06-merge-sort-p16-merge-codice-completo.png]]

> ⚠️ Contraddizione (di notazione): la slide usa `do`/`then`/`else` e il commento `//` (stile della 2ª edizione del Cormen), mentre le [[pseudocodice|convenzioni del corso]] prevedono commenti con $\triangleright$ e nessun `do`/`then`. Il significato è lo stesso. Anche l'assegnamento multiplo `L[n1+1] ← R[n2+1] ← ∞` (riga 8) e `i ← j ← 1` (riga 9) non è previsto dalle convenzioni: si legge come due assegnamenti.

### Esempio di esecuzione · [[06-Merge Sort (1).pdf#page=18|p. 18]], [[06-Merge Sort (1).pdf#page=21|p. 21]]

Stato iniziale della slide: $A[p..q] = \langle 2, 4, 5, 7 \rangle$, $A[q+1..r] = \langle 1, 2, 3, 6 \rangle$, quindi $n_1 = n_2 = 4$, $L = \langle 2, 4, 5, 7, \infty \rangle$, $R = \langle 1, 2, 3, 6, \infty \rangle$, $i = j = 1$.

![[06-merge-sort-p17-traccia-merge.png]]
*Le due metà copiate in $L$ e $R$ con le sentinelle; sopra, $A[p..r]$ già fuso.*

Alla fine $i = 5$ e $j = 5$: in $L$ e $R$ restano solo le due sentinelle, come dice p. 21. Al passo $k = 8$ la sentinella $R[5] = \infty$ fa scegliere $L[4]$ senza controllare che $R$ sia finito.

### Correttezza · [[06-Merge Sort (1).pdf#page=19|p. 19]]–[[06-Merge Sort (1).pdf#page=21|21]]

(La slide p. 19 ha solo il titolo «Merge: analisi di correttezza» e la pagina vuota: l'analisi è nelle due slide successive.)

**Invariante:** all'inizio di ciascuna iterazione dell'ultimo ciclo `for` (righe 10–15), la sottosequenza $A[p..k-1]$ contiene i $k - p$ elementi più piccoli di $L$ ed $R$, ordinati. Inoltre $L[i]$ e $R[j]$ sono i più piccoli elementi dei loro array a non essere stati ricopiati in $A$.

- **Inizializzazione** — l'invariante è vero prima della prima iterazione: per $k = p$ la sottosequenza $A[p..k-1]$ è vuota ($k - p = 0$). $L[1]$ e $R[1]$ sono i più piccoli elementi dei loro array a non essere stati ricopiati in $A$.
- **Conservazione** — una iterazione del ciclo conserva la verità dell'invariante. Se $L[i] \le R[j]$, $L[i]$ viene ricopiato in $A[k]$, quindi $A[p..k]$ contiene i $k - p + 1$ elementi più piccoli di $L$ ed $R$, ordinati. Incrementando $k$ ed $i$ si ristabilisce l'invariante per la successiva iterazione. Analogo discorso se $R[j] < L[i]$.
- **Conclusione** — l'invariante prova che l'algoritmo è corretto. Il ciclo termina quando $k = r + 1$, quindi $A[p..k-1]$, cioè $A[p..r]$, contiene i $k - p = r - p + 1$ elementi più piccoli di $L$ e $R$, ordinati. Gli $r - p + 1$ elementi più piccoli di $L$ e $R$ coincidono con tutti gli elementi originariamente in $A[p..r]$. In $L$ e $R$ restano i due valori sentinella.

### Complessità · [[06-Merge Sort (1).pdf#page=22|p. 22]]

La slide raggruppa le righe e assegna a ogni gruppo un costo:

| Righe | Istruzioni | Costo indicato nella slide |
|---|---|---|
| 1–2 | $n_1 \leftarrow q-p+1$, $n_2 \leftarrow r-q$ | tempo costante |
| 3–7 | creazione di $L$ e $R$, due cicli di copia | tempo proporzionale a $n = n_1 + n_2$ |
| 8–9 | sentinelle, $i \leftarrow j \leftarrow 1$ | tempo costante |
| 10–15 | ciclo di fusione | $n$ iterazioni, ciascuna richiedente un tempo costante ⇒ tempo proporzionale a $n$ |

![[06-merge-sort-p21-costo-merge.png]]

### Pseudocodice (versione definitiva) · [[06-Merge Sort (1).pdf#page=23|p. 23]]

```
Merge-Sort (A,p,r)
1  if p<r
2      q ← ⌊(p+r)/2⌋
3      Merge-Sort (A,p,q)
4      Merge-Sort (A,q+1,r)
5      Merge (A,p,q,r)
```

Invochiamo `Merge-Sort(A,1,n)` per ordinare l'intera sequenza.

Annotazioni a mano accanto allo pseudocodice: «Restituisci $A$ ⇒ non operare su $A$ se devi considerare il singolo elemento di $A$» e «L'ottimizzazione della firma ci ha portato a tutti questi benefici».

![[06-merge-sort-p22-pseudocodice-merge-sort.png]]

Significato dei simboli: $p$, $r$ = estremi del sotto-array $A[p..r]$ da ordinare; $q$ = punto di divisione; [[merge|Merge]] fonde $A[p..q]$ e $A[q+1..r]$.

$$
\begin{aligned}
q - p + 1 &= \left\lfloor \tfrac{p+r}{2} \right\rfloor - p + 1 = \left\lfloor \tfrac{r-p}{2} \right\rfloor + 1 && p \text{ intero, esce dalla parte intera} \\
          &= \left\lfloor \tfrac{n-1}{2} \right\rfloor + 1 = \left\lceil \tfrac{n}{2} \right\rceil && r - p = n - 1 \\
r - q     &= n - \left\lceil \tfrac{n}{2} \right\rceil = \left\lfloor \tfrac{n}{2} \right\rfloor && \text{il resto}
\end{aligned}
$$
> Per $n \ge 2$ entrambe le metà hanno almeno un elemento e meno di $n$ elementi: la ricorsione termina. Con $n = 11$ (l'esempio di p. 9) si ottengono 6 e 5 elementi.

### Ricorrenza del divide et impera · [[06-Merge Sort (1).pdf#page=24|p. 24]], [[06-Merge Sort (1).pdf#page=26|26]], [[06-Merge Sort (1).pdf#page=29|p. 29]]

Per un approccio [[divide-et-impera]], detti:
- $\Theta(1)$ il tempo per risolvere il caso «banale»;
- $D(n)$ il tempo per suddividere un problema;
- $C(n)$ il tempo per ricombinare le soluzioni dei sottoproblemi;
- $a$ il numero di sottoproblemi in cui si divide un problema;
- $1/b$ il fattore di riduzione della dimensione di un problema,

la complessità è esprimibile in forma di ricorrenza:

$$
T(n) = \begin{cases} \Theta(1) & \text{nel caso banale } n = 1 \\ aT(n/b) + D(n) + C(n) & \text{altrimenti } (n > 1) \end{cases}
$$

A p. 24 la slide chiede «Nel caso di Merge Sort: $D(n)=\,$?, $C(n)=\,$?, $a=b=\,$?». Annotazioni a mano: «Ricorrenza: formula matematica» (su $T(n)$), «Potrei avere più casi base» (su $\Theta(1)$), «equivale al costo dell'operazione per ottenere $q$» (sotto $D(n)$).

![[06-merge-sort-p23-ricorrenza-domande.png]]

Risposta: nel caso di merge sort $D(n) = \Theta(1)$, $C(n) = \Theta(n)$, $a = b = 2$.

![[06-merge-sort-p24-ricorrenza-divide-et-impera.png]]

### Appunti a mano: relazione tra $a$ e $b$ · [[06-Merge Sort (1).pdf#page=25|p. 25]]

- $a = b$ ⇒ ogni elemento in un solo sottoproblema;
- $a < b$ ⇒ una parte dell'input viene scartata;
- $a > b$ ⇒ i sottoproblemi si sovrappongono: se ne generano più di quanti ne servano per capire l'input.

### Soluzione con l'albero di ricorsione · [[06-Merge Sort (1).pdf#page=27|p. 27]]

Supponendo che $n$ sia una potenza di 2 e
$$
T(n) = \begin{cases} c & \text{nel caso banale } n = 1 \\ 2T(n/2) + cn & \text{altrimenti } (n > 1) \end{cases}
$$
l'albero ha costo $cn$ a ogni livello e $\lg n + 1$ livelli. Il costo totale è
$$ cn(\lg n + 1) = cn\lg n + cn = \Theta(n \lg n). $$

![[06-merge-sort-p25-albero-ricorsione-merge-sort.png]]
*Radice $cn$, due figli $cn/2$, quattro nipoti $cn/4$, …, $n$ foglie di costo $c$: ogni livello somma a $cn$.*

### Definizione formale · [[06-Merge Sort (1).pdf#page=28|p. 28]]

La slide è un «Stop & Think» che contiene solo il titolo, «Problema del massimo sottoarray», e il rimando al **Capitolo 4.1 del libro di testo**. Non ci sono testo del problema, algoritmo o analisi.

### Definizione · [[06-Merge Sort (1).pdf#page=29|p. 29]], [[06-Merge Sort (1).pdf#page=30|30]]

Il metodo di sostituzione per risolvere una [[equazioni-di-ricorrenza|ricorrenza]] consiste di due passi:
1. **ipotizzare la forma della soluzione**;
2. **verificarla tramite principio di induzione**.

Può essere usato per derivare sia **limiti superiori** che **limiti inferiori** su una ricorrenza.

È il primo dei tre metodi della lezione 06, insieme al [[metodo-albero-di-ricorrenza]] e al [[teorema-dell-esperto]].


### Metodo di sostituzione: passo induttivo e caso base · [[06-Merge Sort (1).pdf#page=31|p. 31]]

Passo induttivo (si assume vero per $\lfloor n/2 \rfloor$, si dimostra per $n$):

$$
\begin{aligned}
T(n) &= 2T(\lfloor n/2 \rfloor) + n \\
&\le 2\,(c\lfloor n/2 \rfloor \lg \lfloor n/2 \rfloor) + n \\
&\le cn \lg(n/2) + n \\
&= cn \lg n - cn \lg 2 + n \\
&= cn \lg n - cn + n \\
&= cn \lg n - (c-1)n \\
&\le cn \lg n \qquad \text{se } c \ge 1
\end{aligned}
$$

Caso base: per $n = 1$ si avrebbe $T(1) \le c \lg 1 = 0$, ma il tempo di esecuzione non può essere $\le 0$. Si usano allora $T(2)$ e $T(3)$ (la disuguaglianza $T(n) \le cn \lg n$ deve valere per $n \ge n_0$): occorre mostrare che $T(2) = 4 \le c\cdot 2 \lg 2$ e $T(3) = 5 \le c \cdot 3 \lg 3$. È sufficiente $c \ge 2$ per verificare i casi base.

### Perché due casi base · [[06-Merge Sort (1).pdf#page=32|p. 32]], [[06-Merge Sort (1).pdf#page=31|p. 31]]

![[06-merge-sort-p30-due-casi-base.png]]
*Due alberi: da 2 discendono 4, 5, poi 8–11, poi 16–23; da 3 discendono 6, 7, poi 12–15, poi 24–31. Ogni freccia va da $\lfloor n/2 \rfloor$ a $n$.*

### Definizione · [[06-Merge Sort (1).pdf#page=33|p. 33]]

- Il metodo dell'albero di ricorrenza può essere usato per **generare delle buone soluzioni di tentativo**, da verificare con il [[metodo-di-sostituzione]] se sono state fatte ipotesi semplificative per derivare le soluzioni.
- I **nodi** dell'albero di ricorrenza riportano il **costo per risolvere un dato (sotto)problema**.

### Esempio 2 — $T(n) = 3T(\lfloor n/4 \rfloor) + \Theta(n^2)$ · [[06-Merge Sort (1).pdf#page=34|p. 34]]–[[06-Merge Sort (1).pdf#page=40|40]]

Consideriamo $T(n) = 3T(\lfloor n/4 \rfloor) + \Theta(n^2)$. Costruiamo l'albero di ricorrenza per $T(n) = 3T(n/4) + cn^2$:
- ignoriamo l'arrotondamento per difetto (approssimazione);
- supponiamo che $n$ sia una potenza di 4 (approssimazione);
- esplicitiamo il coefficiente costante $c$.

![[06-merge-sort-p35-albero-3t-n4.png]]
*Espansione: la radice $cn^2$ ha tre figli $T(n/4)$; espandendo, ogni $c(n/4)^2$ ha tre figli $T(n/16)$.*

**Quanti livelli ha l'albero?** Per un nodo a livello $i$ (il livello della radice è zero), la dimensione dei (sotto)problemi è $n/4^i$. La dimensione 1 si raggiunge per $n/4^i = 1$, ovvero $i = \log_4 n$. L'albero ha quindi $\log_4 n + 1$ livelli.

**Qual è il costo a ciascun livello?** Ogni livello ha il triplo dei nodi del livello precedente, quindi il numero di nodi a livello $i$ è $3^i$. Al livello $i$, il costo di un singolo nodo è $c(n/4^i)^2$.

![[06-merge-sort-p37-albero-costo-livelli.png]]

**Somma**:
$$
\begin{aligned}
T(n) &= \sum_{i=0}^{\log_4 n - 1} 3^i c\left(\frac{n}{4^i}\right)^2 + 3^{\log_4 n}\, T(1) = \sum_{i=0}^{\log_4 n - 1}\left(\frac{3}{16}\right)^i cn^2 + \Theta\!\left(n^{\log_4 3}\right) \\
     &< \sum_{i=0}^{\infty}\left(\frac{3}{16}\right)^i cn^2 + \Theta\!\left(n^{\log_4 3}\right) = \frac{1}{1 - (3/16)}\, cn^2 + \Theta\!\left(n^{\log_4 3}\right) = \frac{16}{13}\, cn^2 + \Theta\!\left(n^{\log_4 3}\right) \\
     &\Rightarrow\ T(n) = O(n^2)
\end{aligned}
$$

![[06-merge-sort-p38-albero-somma.png]]

$$
\begin{aligned}
\text{livelli interni } (0 \le i \le \log_4 n - 1):\ \ 3^i \cdot c\frac{n^2}{16^i} &= \left(\tfrac{3}{16}\right)^i cn^2 && (4^i)^2 = 16^i \\
\text{foglie } (i = \log_4 n):\ \ 3^{\log_4 n} \cdot T(1) &= n^{\log_4 3}\, T(1) = \Theta\!\left(n^{\log_4 3}\right) && \text{identità sopra, } T(1) \text{ costante} \\
\sum_{i=0}^{\log_4 n - 1}\left(\tfrac{3}{16}\right)^i &< \sum_{i=0}^{\infty}\left(\tfrac{3}{16}\right)^i && \text{termini positivi: aggiungerne aumenta la somma} \\
\sum_{i=0}^{\infty} x^i &= \frac{1}{1-x}\ \ (|x| < 1) && \text{serie geometrica, } x = \tfrac{3}{16} \\
\frac{1}{1 - 3/16} &= \frac{1}{13/16} = \frac{16}{13} \approx 1.23 \\
\log_4 3 &\approx 0.79 < 2 \ \Rightarrow\ \Theta\!\left(n^{\log_4 3}\right) = O(n^2) && \text{le foglie sono trascurabili}
\end{aligned}
$$
> Il costo è **dominato dalla radice**: i livelli decrescono geometricamente (ognuno costa $3/16$ del precedente) e la somma è un multiplo costante del primo termine $cn^2$.

### Altri usi nelle lezioni · Merge Sort [[06-Merge Sort (1).pdf#page=41|p. 41]] · Quicksort [[07-Quicksort 1.pdf#page=21|p. 21]], [[07-Quicksort 1.pdf#page=22|22]]

- **Verifica di una soluzione di tentativo** dal [[metodo-albero-di-ricorrenza]]: $T(n) = 3T(\lfloor n/4 \rfloor) + \Theta(n^2) \le dn^2$ con $d \ge \frac{16}{13}c$ e $d \ge T(1)$. La catena completa è in [[metodo-albero-di-ricorrenza]].
- **Caso peggiore di quicksort:** $T(n) = \max_{0 \le q \le n-1}(T(q) + T(n-q-1)) + \Theta(n) \le cn^2$. Qui l'ipotesi induttiva va applicata a **tutti** i $k < n$ (induzione forte), perché $q$ può essere qualsiasi. Passaggi in [[quicksort]] § Dimostrazione del caso peggiore.
- **Limiti inferiori:** stessa tecnica con $\ge$; ad esempio il caso peggiore di quicksort è anche $\Omega(n^2)$.

### Verifica per sostituzione · [[06-Merge Sort (1).pdf#page=41|p. 41]]

Verifichiamo con il [[metodo-di-sostituzione]] che $T(n) = O(n^2)$, ovvero $\exists\, d > 0 : T(n) \le dn^2$. Passo induttivo (assumiamo vero per $\lfloor n/4 \rfloor$, dimostriamo per $n$), con i commenti miei (🧩):

$$
\begin{aligned}
T(n) &= 3T(\lfloor n/4 \rfloor) + \Theta(n^2) && \text{ricorrenza originale, con le parti intere} \\
     &\le 3T(\lfloor n/4 \rfloor) + cn^2 && c \text{ = costante superiore del } \Theta(n^2) \\
     &\le 3d\lfloor n/4 \rfloor^2 + cn^2 && \text{ipotesi induttiva} \\
     &\le 3d(n/4)^2 + cn^2 && \lfloor n/4 \rfloor \le n/4 \\
     &= (3/16)dn^2 + cn^2 && \\
     &\le dn^2 && \text{se } d \ge (16/13)c
\end{aligned}
$$

Per $n = 1$ (caso base), $T(1) \le d$: verificato quindi per $d \ge T(1)$.

![[06-merge-sort-p39-verifica-sostituzione.png]]

### Appunti a mano: metodo di sostituzione · [[06-Merge Sort (1).pdf#page=42|p. 42]]

![[06-merge-sort-p42-appunti-sostituzione.png]]
*Pagina di appunti del docente: verifica per sostituzione di un limite superiore per la ricorrenza $T(n) = 3T(\lfloor n/2 \rfloor) + O(n)$, con scelta delle costanti e del caso base.*

### Anche limite inferiore · [[06-Merge Sort (1).pdf#page=43|p. 43]]

Con il metodo di sostituzione abbiamo verificato che $T(n) = O(n^2)$. In realtà è anche $T(n) = \Omega(n^2)$: la prima chiamata ricorsiva contribuisce con un costo $\Theta(n^2)$ e quindi $\Omega(n^2)$ è un limite inferiore per la ricorrenza. Quindi $T(n) = \Theta(n^2)$.

### Definizione · [[06-Merge Sort (1).pdf#page=44|p. 44]]

Il **metodo dell'esperto** si basa sul **teorema dell'esperto** (*master theorem*).

Siano $a \ge 1$ e $b > 1$ costanti, $f(n)$ una funzione e
$$ T(n) = aT(n/b) + f(n) $$
dove $n/b$ può essere interpretato sia come $\lfloor n/b \rfloor$ che come $\lceil n/b \rceil$. Allora:

1. se $f(n) = O\!\left(n^{\log_b a - \epsilon}\right)$ per un dato $\epsilon > 0$, allora $T(n) = \Theta\!\left(n^{\log_b a}\right)$;
2. se $f(n) = \Theta\!\left(n^{\log_b a}\right)$, allora $T(n) = \Theta\!\left(n^{\log_b a} \lg n\right)$;
3. se $f(n) = \Omega\!\left(n^{\log_b a + \epsilon}\right)$ per un dato $\epsilon > 0$ **e** $af(n/b) \le cf(n)$ per una data $c < 1$ ed $n$ sufficientemente grande, allora $T(n) = \Theta(f(n))$.

**Osservazioni:**
- intuitivamente, la soluzione è data dalla **più grande** tra $f(n)$ e $n^{\log_b a}$;
- $f(n)$ deve essere **polinomialmente** più piccola (grande) di $n^{\log_b a}$ (c'è $\epsilon$);
- ⇒ c'è un **gap** tra il caso 1) e 2) e tra il caso 2) e 3).

![[06-merge-sort-p41-teorema-esperto.png]]

### Appunti a mano: metodo dell'esperto · [[06-Merge Sort (1).pdf#page=45|p. 45]]

![[06-merge-sort-p45-appunti-metodo-dell-esperto.png]]
*Appunti sul teorema dell'esperto: $T(n) = aT(n/b) + f(n)$ con $a \ge 1$ e $b > 1$ costanti; i tre casi (confronto di $f(n)$ con $n^{\log_b a}$) e, a parole, «la soluzione è data dalla più grande tra $f(n)$ e $n^{\log_b a}$; $f(n)$ deve essere polinomialmente più piccola (grande) di $n^{\log_b a}$».*

### Esempi della slide · Merge Sort [[06-Merge Sort (1).pdf#page=46|p. 46]] · 05-Insertion sort.pdf [[05-Insertion sort.pdf#page=38|p. 38]]

![[06-merge-sort-p42-esempi-esperto.png]]

**Esempio 1 — $T(n) = 9T(n/3) + n$**

$$
\begin{aligned}
&a = 9,\ b = 3,\ f(n) = n,\quad n^{\log_b a} = n^{\log_3 9} = n^2 && \log_3 9 = 2 \text{ perché } 3^2 = 9 \\
&n = f(n) = O\!\left(n^{\log_3 9 - \epsilon}\right) = O(n^{2-\epsilon}) \text{ con } \epsilon = 1 && n \le 1 \cdot n^{1}\text{: } c = 1,\ n_0 = 1 \\
&\Rightarrow \text{caso 1:}\ \ T(n) = \Theta(n^2)
\end{aligned}
$$

> **Sanity check** ([[divide_et_impera.py]], $T(1) = 1$, $n$ potenza di 3): $T(n)/n^2 = 1.4979,\ 1.4999,\ 1.5000$ per $n = 3^5, 3^8, 3^{11}$. 🧩 La soluzione esatta è $T(n) = \frac{3}{2}n^2 - \frac{1}{2}n$: provando $T(n) = An^2 + Bn$ nella ricorrenza si trova $B = 3B + 1$, cioè $B = -\frac12$, e $T(1) = 1$ dà $A = \frac32$.

**Esempio 2 — $T(n) = T(2n/3) + 1$**

$$
\begin{aligned}
&a = 1,\ b = 3/2,\ f(n) = 1,\quad n^{\log_b a} = n^{\log_{3/2} 1} = n^0 = 1 && \log_b 1 = 0 \text{ per ogni base} \\
&1 = f(n) = \Theta\!\left(n^{\log_b a}\right) = \Theta(1) \\
&\Rightarrow \text{caso 2:}\ \ T(n) = \Theta(n^0 \lg n) = \Theta(\lg n)
\end{aligned}
$$

**Esempio 3 — $T(n) = 3T(n/4) + n\lg n$**

$$
\begin{aligned}
&a = 3,\ b = 4,\ f(n) = n\lg n,\quad n^{\log_b a} = n^{\log_4 3} && \log_4 3 \approx 0.793 \\
&n\lg n = f(n) = \Omega\!\left(n^{\log_4 3 + \epsilon}\right) \text{ con } \epsilon \approx 0.2 && n\lg n \ge n = n^{0.793 + 0.207} \text{ per } n \ge 2 \\
&af(n/b) = 3\,\tfrac{n}{4}\lg\tfrac{n}{4} \le \tfrac{3}{4}\, n\lg n = cf(n) \text{ con } c = 3/4 && \lg\tfrac{n}{4} = \lg n - 2 \le \lg n \\
&\Rightarrow \text{caso 3:}\ \ T(n) = \Theta(n\lg n)
\end{aligned}
$$

> **Sanity check** ([[divide_et_impera.py]]): $T(n)/(n\lg n) = 2.19,\ 2.66,\ 2.96$ per $n = 4^5, 4^8, 4^{11}$: cresce lentamente verso una costante. 🧩 Con l'albero si trova $T(n) \approx 4n\lg n - 24n$ (serie $\sum (3/4)^i = 4$ e $\sum i(3/4)^i = 12$), quindi il rapporto è $\approx 4 - 24/\lg n$; per $n = 4^{20}$ e $4^{40}$ il calcolo dà 3.40 e 3.70, come previsto.

### Esempio fuori dal teorema: il gap tra i casi 2 e 3 · [[06-Merge Sort (1).pdf#page=47|p. 47]]

$T(n) = 2T(n/2) + n\lg n$:
- $a = 2$, $b = 2$, $f(n) = n\lg n$, $n^{\log_b a} = n^{\log_2 2} = n$;
- $f(n) = n\lg n$ **non** è polinomialmente più grande di $n$;
- $f(n)/n^{\log_b a} = n\lg n / n = \lg n$ è asintoticamente più piccolo di $n^\epsilon$, per ogni $\epsilon > 0$;
- questa ricorrenza ricade nel **gap tra i casi 2) e 3)**.

$$
\begin{aligned}
\text{costo del livello } i &= 2^i \cdot \tfrac{n}{2^i}\lg\tfrac{n}{2^i} = n(\lg n - i) && \lg\tfrac{n}{2^i} = \lg n - i \\
T(n) &\approx \sum_{i=0}^{\lg n - 1} n(\lg n - i) = n\sum_{k=1}^{\lg n} k && k = \lg n - i \\
     &= n\,\frac{\lg n(\lg n + 1)}{2} = \Theta(n\lg^2 n) && \text{somma di Gauss}
\end{aligned}
$$
> Verifica ([[divide_et_impera.py]]): $T(n)/(n\lg^2 n) = 0.560,\ 0.528,\ 0.513$ per $n = 2^{10}, 2^{20}, 2^{40}$, verso $\frac12$; $T(n)/(n\lg n)$ invece cresce senza limite (5.6, 10.6, 20.5).

### S&T: «Albero di ricorsione?» · [[06-Merge Sort (1).pdf#page=9|p. 9]], [[06-Merge Sort (1).pdf#page=48|p. 48]]

Dopo il teorema dell'esperto la lezione chiude la parte sulle ricorrenze con uno «Stop & Think» che contiene solo la domanda **«Albero di ricorsione?»**, senza altro testo.


### Crescita delle funzioni: ragionare sull'efficienza e l'importanza dei logaritmi · [[06-Merge Sort (1).pdf#page=49|p. 49]], [[06-Merge Sort (1).pdf#page=50|50]], [[06-Merge Sort (1).pdf#page=51|51]], [[06-Merge Sort (1).pdf#page=52|52]], [[06-Merge Sort (1).pdf#page=49|p. 49]], [[06-Merge Sort (1).pdf#page=50|p. 50]], [[06-Merge Sort (1).pdf#page=51|p. 51]], [[06-Merge Sort (1).pdf#page=52|p. 52]]

**Valutare l'efficienza asintotica — S&T: String Pattern Matching.** *Substring Pattern Matching*: dati un testo $t$ e un pattern $p$, $t$ contiene $p$ come sottostringa e, in tal caso, dove? La soluzione della slide è `findmatch` (forza bruta):

```
int findmatch(char *p, char *t) {
    int i,j;                      /* counters */
    int m, n;                     /* string lengths */
    m = strlen(p);
    n = strlen(t);
    for (i=0; i<=(n-m); i=i+1) {
        j=0;
        while ((j<m) && (t[i+j]==p[j]))
            j = j+1;
        if (j == m) return(i);
    }
    return(-1);
}
```

**L'importanza dei logaritmi.** I logaritmi compaiono in ogni processo in cui qualcosa viene ripetutamente **dimezzato**. Esempi:
- ricerca binaria;
- alberi: qual è l'altezza $h$ di un albero con $d$ figli a ogni livello e $n$ foglie?
- bit: quanti bit servono per rappresentare una tra $n$ possibilità?
- moltiplicazione: $ab = \exp(\ln(ab)) = \exp(b \ln a)$;
- elevamento a potenza veloce: $a^n = (a^{n/2})^2$ se $n$ è pari, $a^n = a\,(a^{\lfloor n/2 \rfloor})^2$ se $n$ è dispari; richiede $O(\lg n)$ moltiplicazioni;
- sommatorie: i numeri armonici $H_n = \sum_{i=1}^{n} \frac{1}{i} \sim \ln n$.

**S&T: l'importanza di una divisione equa.** Quante interrogazioni richiede la ricerca binaria sull'elenco telefonico di Manhattan (un milione di nomi) se ogni divisione fosse $1/3$–$2/3$ invece di $1/2$–$1/2$? $\log_{3/2}(1\,000\,000) \approx 35$ chiamate nel caso peggiore, contro $\log_2(1\,000\,000) \approx 20$.

*Take-home lesson:* la potenza della ricerca binaria deriva dalla sua complessità **logaritmica**, non dalla base del logaritmo.

*Approfondimenti nel wiki: [[lezione-06-merge-sort]], [[torre-di-hanoi]], [[merge-sort]], [[merge]], [[massimo-sottoarray]], [[metodo-di-sostituzione]], [[metodo-albero-di-ricorrenza]], [[teorema-dell-esperto]]*

## Lezione 7 — Quicksort

*Fonte: 07-Quicksort 1.pdf.*

### Idea · [[07-Quicksort 1.pdf#page=2|p. 2]], [[07-Quicksort 1.pdf#page=3|3]], [[07-Quicksort 1.pdf#page=1|p. 1]]

Quick Sort ha un tempo di esecuzione:
- $\Theta(n^2)$ nel caso peggiore;
- $\Theta(n \lg n)$ nel caso «medio»;
- ordina sul posto.

Nella pratica risulta essere tra i più efficienti, grazie al fatto che i fattori «nascosti» in $\Theta(n \lg n)$ sono piuttosto piccoli.

Utilizza un approccio **[[divide-et-impera]]**:
- **Divide** — scelto un elemento $x$, detto *pivot*, partiziona l'array $A[p..r]$ in due sottoarray tali che $A[p..q-1]$ contiene gli elementi $\le x$ e $A[q+1..r]$ contiene gli elementi $> x$; il pivot va in $A[q]$.
- **Conquer** — ordina i due sottoarray mediante chiamate ricorsive.
- **Combine** — i sottoarray sono ordinati sul posto, quindi non occorre fare nulla.

![[07-quicksort-p3-divide-conquer-combine.png]]

### Pseudocodice · [[07-Quicksort 1.pdf#page=4|p. 4]], [[07-Quicksort 1.pdf#page=6|p. 6]]

```
Quicksort (A,p,r)
1  if p<r
2      q ← Partition (A,p,r)
3      Quicksort (A,p,q-1)
4      Quicksort (A,q+1,r)
```

Per ordinare l'intero array si invoca `Quicksort (A,1,length[A])`.

![[07-quicksort-p4-pseudocodice-quicksort.png]]

Annotazioni a mano sulla slide:
- accanto a `if p<r`: «logica base è gestita da quicksort non entrando nell'if». Il caso base ($p \ge r$, al più un elemento) non ha istruzioni proprie: semplicemente non si esegue il corpo dell'`if`;
- sotto la slide: «pivot piccolo: troppi swap» e «pivot grande: sposto solo una barriera».

> ⚠️ Contraddizione: la seconda annotazione è invertita rispetto a Partition. Per la regola di p. 6, un elemento **maggiore** del pivot fa avanzare solo la barriera $j$; un elemento **minore o uguale** fa avanzare $i$ e provoca uno scambio. Quindi con un pivot **piccolo** (quasi tutti gli elementi lo superano) si sposta solo una barriera, mentre con un pivot **grande** (quasi tutti gli elementi sono $\le$) si fanno molti scambi. 🧩 Verificato con il codice su 8 elementi: pivot massimo → 7 scambi nel ciclo; pivot minimo → 0 scambi, solo $j$ avanza. In entrambi i casi la partizione è sbilanciata ($n - 1$ e 0), che è il caso peggiore della sezione «Complessità».

Simboli: $A[p..r]$ = sotto-array da ordinare; $q$ = posizione finale del pivot restituita da [[partition]]. Il pivot $A[q]$ è già al suo posto definitivo e non partecipa alle chiamate ricorsive.

### Idea · [[07-Quicksort 1.pdf#page=5|p. 5]], [[07-Quicksort 1.pdf#page=6|6]]

La funzione Partition utilizza come pivot l'**ultimo elemento** del sottoarray ($x = A[r]$). Analizza, uno ad uno e a partire dal primo, tutti gli elementi compresi tra $p$ e $r - 1$, suddividendo il vettore in **quattro aree**:

| Area | Posizioni | Contenuto | Colore nelle slide |
|---|---|---|---|
| 1ª | $p..i$ | elementi $\le$ del pivot | giallo |
| 2ª | $i+1..j-1$ | elementi $>$ del pivot | rosso |
| 3ª | $j..r-1$ | elementi non ancora analizzati | bianco |
| 4ª | $r$ | il pivot | — |

![[07-quicksort-p5-quattro-aree.png]]
*Le quattro aree separate da barriere: $i$ chiude la prima, $j$ apre la terza.*

L'elemento di posto $j$ (il primo non analizzato) viene confrontato con il pivot:
- se è **maggiore**, è sufficiente incrementare la barriera tra 2ª e 3ª area, ovvero incrementare $j$;
- se è **minore o uguale**, deve essere spostato nella prima area:
  - si incrementa $i$ (si sposta la barriera tra 1ª e 2ª area);
  - si scambia $A[i]$ con $A[j]$;
  - si incrementa $j$ (si sposta la barriera tra 2ª e 3ª area).

### Correttezza · [[07-Quicksort 1.pdf#page=3|p. 3]], [[07-Quicksort 1.pdf#page=6|p. 6]], [[07-Quicksort 1.pdf#page=13|p. 13]]

**Invariante** — all'inizio di ogni iterazione del ciclo `for`:
1. $A[k] \le x$ per $p \le k \le i$;
2. $A[k] > x$ per $i + 1 \le k \le j - 1$;
3. $A[k] = x$ se $k = r$.

- **Inizializzazione** — vero prima della prima iterazione ($i = p - 1$ e $j = p$) perché la 1ª e la 2ª area sono entrambe vuote.
- **Conservazione** — il ciclo conserva l'invariante.
- **Conclusione** — al termine ($j = r$), l'array è suddiviso in tre insiemi: elementi minori o uguali al pivot, pivot, elementi maggiori del pivot.

![[07-quicksort-p13-invariante-partition.png]]

### Esempio di esecuzione · [[07-Quicksort 1.pdf#page=7|p. 7]]–[[07-Quicksort 1.pdf#page=11|11]], [[07-Quicksort 1.pdf#page=8|p. 8]], [[07-Quicksort 1.pdf#page=9|p. 9]], [[07-Quicksort 1.pdf#page=10|p. 10]]

Array iniziale $A[1..8] = \langle 2, 8, 7, 1, 3, 5, 6, 4 \rangle$, $p = 1$, $r = 8$, $x = A[8] = 4$. Inizialmente le due barriere (tra 1ª e 2ª area e tra 2ª e 3ª area) coincidono: $i = 0$, $j = 1$.

| Slide | $j$ | $A[j]$ | $A[j] \le 4$? | Azione | $i$ dopo | $A$ dopo |
|---|---|---|---|---|---|---|
| p. 7 | 1 | 2 | sì | $i \leftarrow 1$, scambio $A[1] \leftrightarrow A[1]$ | 1 | ⟨2, 8, 7, 1, 3, 5, 6, 4⟩ |
| p. 8 | 2 | 8 | no | solo $j$ avanza | 1 | invariato |
| p. 8 | 3 | 7 | no | solo $j$ avanza | 1 | invariato |
| p. 9 | 4 | 1 | sì | $i \leftarrow 2$, scambio $A[2] \leftrightarrow A[4]$ | 2 | ⟨2, 1, 7, 8, 3, 5, 6, 4⟩ |
| p. 10 | 5 | 3 | sì | $i \leftarrow 3$, scambio $A[3] \leftrightarrow A[5]$ | 3 | ⟨2, 1, 3, 8, 7, 5, 6, 4⟩ |
| p. 10 | 6 | 5 | no | solo $j$ avanza | 3 | invariato |
| p. 11 | 7 | 6 | no | solo $j$ avanza | 3 | invariato |
| p. 11 | — | — | — | il ciclo è finito ($j = r$): scambio $A[i+1] \leftrightarrow A[r]$ | 3 | ⟨2, 1, 3, **4**, 7, 5, 6, 8⟩ |

Return $q = i + 1 = 4$: a sinistra ⟨2, 1, 3⟩ (tutti $\le 4$), a destra ⟨7, 5, 6, 8⟩ (tutti $> 4$). Verificato con [[divide_et_impera.py]].

![[07-quicksort-p7-partition-passo-1.png]]
*Passo 1: $A[1] = 2 \le 4$, $i$ e $j$ avanzano insieme.*

![[07-quicksort-p8-partition-passi-2-3.png]]
*Passi 2–3: 8 e 7 sono maggiori del pivot, avanza solo $j$ e la 2ª area cresce.*

![[07-quicksort-p9-partition-passo-4.png]]
*Passo 4: 1 ≤ 4, si incrementa $i$ e si scambia $A[2] \leftrightarrow A[4]$.*

![[07-quicksort-p10-partition-passi-5-6.png]]
*Passi 5–6: 3 entra nella 1ª area, 5 resta nella 2ª.*

![[07-quicksort-p11-partition-fine.png]]
*Passo 7 e fine: 6 > 4; ciclo finito, il pivot va in $A[i+1] = A[4]$.*

### Pseudocodice · [[07-Quicksort 1.pdf#page=12|p. 12]]

```
Partition (A,p,r)
1  x ← A[r]
2  i ← p-1
3  for j ← p to r-1
4      if A[j] ≤ x
5          i ← i+1
6          exchange A[i] ↔ A[j]
7  exchange A[i+1] ↔ A[r]
8  return i+1
```

![[07-quicksort-p12-pseudocodice-partition.png]]
*Pseudocodice e stato finale del ciclo (prima dello scambio della riga 7), con le barriere tra le aree.*

Simboli: $x$ = pivot; $i$ = ultima posizione della 1ª area (vale $p - 1$ quando l'area è vuota); $j$ = primo elemento non analizzato; `exchange` = scambio di due elementi; il valore restituito $i + 1$ è la posizione finale $q$ del pivot.

### Complessità · [[07-Quicksort 1.pdf#page=12|p. 12]]

Il tempo di esecuzione è $\Theta(n)$, con $n = r - p + 1$: $n$ iterazioni, ciascuna delle quali impiega un tempo costante.

### 1. Caso peggiore — srotolamento della ricorrenza · [[07-Quicksort 1.pdf#page=14|p. 14]]

- Il caso peggiore si presenta quando il partizionamento produce un sottoproblema con $n - 1$ elementi e uno con 0 elementi (dimostrazione in seguito, pp. 21–22).
- Supponendo che un tale partizionamento sbilanciato si verifichi in ogni iterazione, il tempo di esecuzione è
$$ T(n) = T(n-1) + T(0) + \Theta(n) = T(n-1) + \Theta(n) $$
- Intuitivamente, la soluzione è $T(n) = \Theta(n^2)$: si ottiene una serie aritmetica, verificabile con il [[metodo-di-sostituzione]].
- Il tempo di esecuzione di Quicksort nel caso peggiore non è migliore di quello di [[insertion-sort]]. Il caso peggiore di Quicksort si ha quando il vettore è **ordinato**, caso in cui Insertion Sort richiede un tempo $O(n)$.

**Come funziona il metodo** (→ [[equazioni-di-ricorrenza]]). La ricorrenza riduce $n$ di **1** a ogni passo, quindi si può srotolare:
1. si sostituisce $T(n-1)$ con la sua definizione, poi $T(n-2)$, e così via;
2. dopo qualche passo si riconosce la forma generale dopo $k$ passi;
3. si sceglie $k$ in modo da arrivare al caso base;
4. si calcola la somma che è rimasta.

**Applicazione** (🧩), con $cn$ al posto di $\Theta(n)$ e $T(0) = c_0$:
$$
\begin{aligned}
T(n) &= T(n-1) + cn && \text{ricorrenza} \\
     &= T(n-2) + c(n-1) + cn && \text{passo 1: sostituisco } T(n-1) = T(n-2) + c(n-1) \\
     &= T(n-k) + c\sum_{m=n-k+1}^{n} m && \text{passo 2: forma dopo } k \text{ passi} \\
     &= T(0) + c\sum_{m=1}^{n} m && \text{passo 3: } k = n \text{, caso base} \\
     &= c_0 + c\,\frac{n(n+1)}{2} = \Theta(n^2) && \text{passo 4: serie aritmetica (somma di Gauss)}
\end{aligned}
$$

**Quale input lo realizza** (🧩): con il vettore ordinato il pivot $x = A[r]$ è il massimo. Il test $A[j] \le x$ è sempre vero e Partition restituisce $q = r$: $n - 1$ elementi a sinistra (ancora ordinati), 0 a destra, e lo stesso si ripete a ogni livello.

**Verifica** ([[divide_et_impera.py]]): su un array ordinato Partition fa $\frac{n(n-1)}{2}$ confronti in tutto, cioè 4950 per $n = 100$.

### 2. Caso migliore — teorema dell'esperto · Quicksort [[07-Quicksort 1.pdf#page=15|p. 15]] · Merge Sort [[06-Merge Sort (1).pdf#page=44|p. 44]]

- Il caso migliore è quando i due sottoproblemi sono perfettamente bilanciati ad ogni iterazione: dimensioni $\lfloor n/2 \rfloor$ e $\lceil n/2 \rceil - 1$.
- Tempo di esecuzione $T(n) \le 2T(n/2) + \Theta(n)$.
- Soluzione: $T(n) = O(n \lg n)$, dal caso 2 del [[teorema-dell-esperto]].

**Come funziona il metodo**. Il teorema risolve direttamente le ricorrenze della forma $T(n) = aT(n/b) + f(n)$:
1. si riconoscono $a$ (numero di sottoproblemi), $b$ (fattore di riduzione) e $f(n)$ (lavoro fuori dalle chiamate);
2. si calcola $n^{\log_b a}$;
3. si confronta $f(n)$ con $n^{\log_b a}$: più piccola di un fattore polinomiale (caso 1), dello stesso ordine (caso 2), più grande di un fattore polinomiale e regolare (caso 3);
4. si legge la soluzione del caso.

**Applicazione** (🧩):
$$
\begin{aligned}
&a = 2,\quad b = 2,\quad f(n) = \Theta(n) && \text{passo 1: due chiamate su metà, Partition lineare} \\
&n^{\log_b a} = n^{\log_2 2} = n && \text{passo 2} \\
&f(n) = \Theta(n) = \Theta\!\left(n^{\log_b a}\right) && \text{passo 3: stesso ordine} \Rightarrow \text{caso 2} \\
&T(n) = \Theta\!\left(n^{\log_b a}\lg n\right) = \Theta(n\lg n) && \text{passo 4}
\end{aligned}
$$

La slide scrive $O$ perché la ricorrenza è una disuguaglianza ($\le$): le due parti sono **al più** $n/2$. Le loro dimensioni sommano a $\lfloor n/2 \rfloor + \lceil n/2 \rceil - 1 = n - 1$, cioè tutti gli elementi tranne il pivot.

### 3. Rapporto costante 9:1 — albero di ricorrenza · [[07-Quicksort 1.pdf#page=16|p. 16]], [[07-Quicksort 1.pdf#page=17|17]]

- Il tempo medio di esecuzione di Quicksort è più vicino al caso migliore che non al caso peggiore.
- Supponiamo che il partizionamento produca due sottoproblemi la cui dimensione è sempre nel rapporto 9:1:
$$ T(n) \le T(9n/10) + T(n/10) + cn $$
- Utilizziamo il metodo dell'albero di ricorrenza.
- Il costo è $O(n \lg n)$: $\Theta(\lg n)$ livelli, ciascuno di costo al più $cn$.
- Qualunque partizionamento con rapporto *costante* (anche 99:1) produce un costo $O(n \lg n)$, perché la profondità è sempre $\Theta(\lg n)$.

**Perché non il teorema dell'esperto** (🧩): i due sottoproblemi hanno dimensioni diverse ($9n/10$ e $n/10$), quindi la ricorrenza non ha la forma $aT(n/b) + f(n)$ con un unico $b$.

**Come funziona il metodo** (→ [[metodo-albero-di-ricorrenza]]):
1. si disegna l'albero: ogni nodo riporta il **costo locale** della sua chiamata (qui $c$ per la sua dimensione), i figli sono le chiamate ricorsive;
2. si calcola il **costo di ogni livello**, sommando i nodi del livello;
3. si conta il **numero di livelli**, cioè la profondità del ramo più lungo, fino alla dimensione 1;
4. si somma su tutti i livelli (qui basta maggiorare: livelli × costo massimo di un livello).

![[07-quicksort-p17-albero-9-1.png]]
*Albero della ricorrenza 9:1: costo $cn$ per livello fino alla profondità $\log_{10} n$ (dove finisce il ramo più corto), poi $\le cn$ fino a $\log_{10/9} n$ (ramo più lungo).*

**Applicazione** (🧩):
$$
\begin{aligned}
&\text{livello } i:\ \text{i sottoproblemi sono parti disgiunte dell'array} \Rightarrow \textstyle\sum \text{dimensioni} \le n && \text{passo 2} \\
&\text{costo del livello } i \le cn && \text{passo 2: } c \times \text{somma delle dimensioni} \\
&\text{ramo più lungo (sempre } 9/10\text{):}\ \ n\left(\tfrac{9}{10}\right)^i = 1 \iff i = \log_{10/9} n && \text{passo 3} \\
T(n) &\le cn\left(\log_{10/9} n + 1\right) && \text{passo 4: livelli} \times cn \\
     &= cn\left(\frac{\lg n}{\lg(10/9)} + 1\right) = O(n\lg n) && \text{cambio di base: } \lg(10/9) \text{ è una costante}
\end{aligned}
$$

Con 99:1 cambia solo la base del logaritmo, $\log_{100/99} n$: la profondità resta $\Theta(\lg n)$ e il costo $O(n\lg n)$ (→ [[logaritmi-nell-analisi]]).

**Verifica** ([[divide_et_impera.py]]): simulando lo split 9:1 con $n = 10^3$ il ramo più lungo ha 66 livelli, e $\log_{10/9} 10^3 \approx 65.6$.

### 4. Caso medio — partizioni buone e cattive alternate · [[07-Quicksort 1.pdf#page=18|p. 18]], [[07-Quicksort 1.pdf#page=23|p. 23]]

- Nel caso medio, tipicamente partizioni «buone» e «cattive» si alternano.
- Intuitivamente, se si alternano best case e worst case, il tempo di esecuzione complessivo è quello del best case.
- Il costo $\Theta(n-1)$ della partizione cattiva viene assorbito nel costo $\Theta(n)$ della partizione buona, e la partizione risultante è buona.

![[07-quicksort-p18-partizioni-alternate.png]]
*A sinistra: partizione cattiva ($0$ e $n - 1$, costo $\Theta(n)$) seguita da una buona ($\frac{n-1}{2} - 1$ e $\frac{n-1}{2}$, costo $\Theta(n-1)$). A destra: una sola partizione buona ($\frac{n-1}{2}$ e $\frac{n-1}{2}$, costo $\Theta(n)$).*

**Come si legge con l'albero** (🧩): si confrontano due pezzi di albero.
- A sinistra, dopo **due** livelli si arriva a sottoproblemi di dimensione circa $\frac{n-1}{2}$, spendendo $\Theta(n) + \Theta(n-1) = \Theta(n)$.
- A destra, dopo **un** livello si arriva agli stessi sottoproblemi, spendendo $\Theta(n)$.
- Il costo per arrivare agli stessi sottoproblemi è dello stesso ordine. L'albero con le partizioni alternate ha al più il doppio dei livelli, cioè ancora $\Theta(\lg n)$, con costo $O(n)$ per coppia di livelli: il totale resta $O(n\lg n)$.

È un argomento intuitivo: la dimostrazione del tempo atteso riguarda la versione randomizzata ed è sul libro di testo (→ [[quicksort-randomizzato]]).

### Definizione · [[07-Quicksort 1.pdf#page=19|p. 19]]

La slide cita (in inglese) che la randomizzazione è «a powerful tool to improve algorithms» con **caso peggiore cattivo** ma **caso medio buono**. Tre usi elencati:
- *random sampling* (campionamento casuale);
- *randomized hashing* (hashing randomizzato);
- *random search* (ricerca casuale).

### Spiegazione · [[07-Quicksort 1.pdf#page=14|p. 14]], [[07-Quicksort 1.pdf#page=20|p. 20]]

L'esempio della lezione è **quicksort**: scegliere il pivot in maniera aleatoria aumenta la probabilità che in media il partizionamento sia ben bilanciato, e la versione randomizzata è ritenuta la scelta migliore per ordinare array di grosse dimensioni.

### Idea · [[07-Quicksort 1.pdf#page=2|p. 2]], [[07-Quicksort 1.pdf#page=19|p. 19]], [[07-Quicksort 1.pdf#page=20|20]]

- Per aumentare la probabilità che in media il partizionamento effettuato da Quicksort sia ben bilanciato, si può scegliere in maniera **aleatoria** il pivot.
- La versione randomizzata di Quicksort è ritenuta la scelta migliore per ordinare array di grosse dimensioni.

È l'applicazione della [[randomizzazione]]: uno strumento per migliorare algoritmi con caso peggiore cattivo ma caso medio buono, come [[quicksort]] ($\Theta(n^2)$ contro $\Theta(n\lg n)$).

### Pseudocodice · [[07-Quicksort 1.pdf#page=20|p. 20]]

```
Randomized-Quicksort (A,p,r)
1  if p<r
2      q ← Randomized-Partition (A,p,r)
3      Randomized-Quicksort (A,p,q-1)
4      Randomized-Quicksort (A,q+1,r)

Randomized-Partition (A,p,r)
5  i ← Random (p,r)
6  exchange A[r] ↔ A[i]
7  return Partition (A,p,r)
```

Simboli: `Random (p,r)` restituisce un indice intero tra $p$ e $r$ scelto a caso (🧩: la slide non lo definisce; si intende con la stessa probabilità $\frac{1}{r-p+1}$ per ogni indice, 📚 Cormen, 3ª ed., §5.1). Lo scambio della riga 6 porta l'elemento scelto in $A[r]$, dove [[partition]] si aspetta il pivot.

![[07-quicksort-p20-quicksort-randomizzato.png]]

### Come si imposta l'analisi: dallo pseudocodice alla ricorrenza · [[07-Quicksort 1.pdf#page=12|p. 12]], [[07-Quicksort 1.pdf#page=21|p. 21]]

**Passo 1 — costo di una chiamata.** Una chiamata `Quicksort(A,p,r)` su $n = r - p + 1$ elementi esegue:
- il test `if p<r` (riga 1): $\Theta(1)$;
- [[partition]] (riga 2): $\Theta(n)$;
- due chiamate ricorsive (righe 3–4): una sul sotto-array sinistro, di $q$ elementi, e una sul destro, di $n - q - 1$ elementi (il pivot resta fuori).

Quindi, indicando con $q$ la **dimensione** della parte sinistra (come fa la slide di p. 21):
$$
T(n) = T(q) + T(n - q - 1) + \Theta(n), \qquad T(0) = T(1) = \Theta(1)
$$

**Passo 2 — $q$ dipende dall'input.** La ricorrenza non è ancora risolvibile, perché $q$ lo decide Partition in base ai valori dell'array. Ogni «caso» delle slide corrisponde a una scelta di $q$, che trasforma la ricorrenza in una ricorrenza in una sola variabile.

**Passo 3 — si risolve con il metodo adatto alla sua forma.**

| Caso | $q$ | Ricorrenza | Metodo | Risultato | Slide |
|---|---|---|---|---|---|
| peggiore (sbilanciato) | $n - 1$ (o $0$) | $T(n-1) + \Theta(n)$ | srotolamento | $\Theta(n^2)$ | p. 14 |
| migliore (bilanciato) | $\approx n/2$ | $\le 2T(n/2) + \Theta(n)$ | [[teorema-dell-esperto]] | $O(n\lg n)$ | p. 15 |
| rapporto 9:1 | $9n/10$ | $\le T(9n/10) + T(n/10) + cn$ | [[metodo-albero-di-ricorrenza]] | $O(n\lg n)$ | pp. 16–17 |
| medio | buono e cattivo alternati | — | ragionamento sull'albero | $O(n\lg n)$ (intuitivo) | p. 18 |
| peggiore, dimostrazione | qualsiasi | $\max_q(\dots) + \Theta(n)$ | [[metodo-di-sostituzione]] | $\Theta(n^2)$ | pp. 21–22 |

Le sezioni seguenti risolvono le ricorrenze nell'ordine delle slide.

### 5. Dimostrazione del caso peggiore — metodo di sostituzione · Quicksort [[07-Quicksort 1.pdf#page=21|p. 21]], [[07-Quicksort 1.pdf#page=22|22]] · Merge Sort [[06-Merge Sort (1).pdf#page=30|p. 30]]

Dimostriamo che il tempo di esecuzione è $\Theta(n^2)$ nel caso peggiore, dimostrando prima con il metodo di sostituzione che $T(n) = O(n^2)$:

$$
\begin{aligned}
T(n) &= \max_{0 \le q \le n-1} \big(T(q) + T(n-q-1)\big) + \Theta(n) \\
     &\le \max_{0 \le q \le n-1} \big(cq^2 + c(n-q-1)^2\big) + \Theta(n) \\
     &= c \cdot \max_{0 \le q \le n-1} \big(q^2 + (n-q-1)^2\big) + \Theta(n) \\
     &\le c(n-1)^2 + \Theta(n) \\
     &= cn^2 - c(2n-1) + \Theta(n) \\
     &\le cn^2
\end{aligned}
$$

La funzione ha la concavità verso l'alto (la derivata seconda rispetto a $q$ è positiva), quindi il massimo è assunto agli estremi.

In precedenza abbiamo visto un caso (il caso sbilanciato) in cui il tempo di esecuzione è $\Theta(n^2)$. Quindi il tempo di esecuzione nel caso peggiore è $\Omega(n^2)$. Combinando questo risultato con quello della slide precedente, il tempo di esecuzione nel caso peggiore è $\Theta(n^2)$.

![[07-quicksort-p21-worst-case-sostituzione.png]]

**Perché serve questo metodo** (🧩): il caso 1 ha **supposto** che la partizione peggiore fosse quella sbilanciata. Per dimostrarlo bisogna considerare **tutte** le possibili divisioni, cioè il $\max$ su $q$. Una ricorrenza con un $\max$ non si srotola e non ha la forma del teorema dell'esperto; si può però verificare una soluzione ipotizzata.

**Come funziona il metodo** (→ [[metodo-di-sostituzione]]):
1. si **ipotizza** la soluzione: $T(n) \le cn^2$;
2. si **assume** che valga per tutte le dimensioni più piccole di $n$ (ipotesi induttiva);
3. la si **sostituisce** nella ricorrenza e si dimostra che ne segue $T(n) \le cn^2$ con la **stessa** costante $c$;
4. si controllano i **casi base**.

**Applicazione** (🧩), riga per riga della catena della slide:
1. **Prima riga:** è la ricorrenza dell'impostazione iniziale, con il $\max$ su tutte le dimensioni $q$ possibili della parte sinistra.
2. **Seconda riga — passo 2 del metodo:** ipotesi induttiva $T(k) \le ck^2$ per ogni $k < n$, applicata sia a $q$ sia a $n - q - 1$. Serve per **ogni** $k < n$ (induzione forte), perché $q$ può essere qualsiasi.
3. **Terza riga:** si raccoglie $c > 0$, che non sposta il punto di massimo.
4. **Quarta riga:** $f(q) = q^2 + (n-q-1)^2$ ha $f''(q) = 2 + 2 = 4 > 0$, quindi è convessa e sull'intervallo $[0, n-1]$ ha il massimo agli estremi: $f(0) = f(n-1) = (n-1)^2$.
5. **Quinta riga:** $c(n-1)^2 = cn^2 - 2cn + c = cn^2 - c(2n-1)$.
6. **Sesta riga — passo 3 del metodo:** se $c'n$ maggiora il termine $\Theta(n)$, serve $c(2n-1) \ge c'n$. Poiché $2n - 1 \ge n$, basta scegliere $c \ge c'$: si ottiene $T(n) \le cn^2$ con la stessa $c$ dell'ipotesi.
7. **Passo 4, casi base** (la slide non li tratta): per $n = 1$ basta $c \ge T(1)$. $T(0)$ non può essere $\le c \cdot 0^2 = 0$; quando $q = 0$ o $q = n - 1$ il termine $T(0)$ è una costante e si assorbe nel $\Theta(n)$.

**Limite inferiore**: il $\max$ è almeno il valore per $q = n - 1$, cioè la ricorrenza sbilanciata del caso 1, che vale $\Theta(n^2)$. Quindi il caso peggiore è $\Omega(n^2)$, e con il limite superiore $\Theta(n^2)$.

### Formule · [[07-Quicksort 1.pdf#page=23|p. 23]]

Per un algoritmo randomizzato interessa il **tempo di esecuzione atteso**: per quicksort randomizzato si dimostra che è $O(n\log n)$ (dimostrazione sul libro di testo).

$$ \max_{|I| = n} \mathbb{E}[T(I)] = O(n \log n) $$
> Nel «caso medio» di [[casi-di-complessita]], invece, la media è fatta sugli **input**, secondo una distribuzione da ipotizzare.

### Complessità · [[07-Quicksort 1.pdf#page=18|p. 18]], [[07-Quicksort 1.pdf#page=21|p. 21]], [[07-Quicksort 1.pdf#page=23|p. 23]]

- Nella versione randomizzata è di interesse il **tempo di esecuzione atteso**.
- Si dimostra che è $O(n \log n)$.
- Dimostrazione sul libro di testo.

| Caso | Tempo |
|---|---|
| atteso (qualsiasi input) | $O(n \log n)$ |
| peggiore (scelte sfortunate a ogni livello) | $\Theta(n^2)$ (🧩: la dimostrazione di pp. 21–22 vale per ogni scelta del pivot) |

**Spazio:** come [[quicksort]], sul posto; pila delle chiamate $\Theta(\lg n)$ attesa e $\Theta(n)$ nel caso peggiore (🧩).

### Definizione formale · [[07-Quicksort 1.pdf#page=25|p. 25]], [[07-Quicksort 1.pdf#page=24|p. 24]]

- Sono dati $n$ **bulloni** di larghezze diverse e gli $n$ **dadi** corrispondenti.
- L'unica operazione ammessa è **provare un dado su un bullone**: si scopre se il dado è troppo largo, troppo stretto o se combacia esattamente.
- Le differenze di misura sono troppo piccole per vederle a occhio: **non** si possono confrontare direttamente due dadi tra loro, né due bulloni tra loro.
- Bisogna accoppiare ogni bullone con il suo dado.

**Consegna:** dare un algoritmo $O(n^2)$, poi un algoritmo **randomizzato** con tempo **atteso** $O(n \log n)$.

![[07-quicksort-p25-nuts-and-bolts.png]]

*Approfondimenti nel wiki: [[lezione-07-quicksort]], [[quicksort]], [[partition]], [[randomizzazione]], [[quicksort-randomizzato]], [[nuts-and-bolts]], [[progettazione-divide-et-impera]]*

## Lezione 8 — Grafi e alberi

*Fonte: 08-Grafi e alberi.pdf.*

### Definizione · [[08-Grafi e alberi.pdf#page=3|p. 3]], [[08-Grafi e alberi.pdf#page=26|p. 26]], [[08-Grafi e alberi.pdf#page=1|p. 1]], [[08-Grafi e alberi.pdf#page=2|p. 2]], [[08-Grafi e alberi.pdf#page=25|p. 25]]

I grafi sono uno dei temi unificanti dell'informatica. Un **grafo** $G = (V, E)$ è definito da un insieme di **vertici** $V$ e da un insieme di **archi** $E$, formato da coppie **ordinate** o **non ordinate** di vertici di $V$.

Annotazione a mano sulla slide: il grafo è uno «strumento per formalizzare problemi, mantenere informazioni».

Simboli usati nelle slide successive: $n = |V|$ numero di vertici, $m = |E|$ numero di archi.

### Esempi di modellazione · [[08-Grafi e alberi.pdf#page=4|p. 4]]–[[08-Grafi e alberi.pdf#page=6|6]], [[08-Grafi e alberi.pdf#page=7|p. 7]]

- **Reti stradali** (p. 4): i vertici rappresentano città o incroci, alcune coppie dei quali sono collegate da strade (gli archi). La figura mostra 8 località di Long Island: Stony Brook, Greenport, Orient Point, Riverhead, Shelter Island, Islip, Sag Harbor, Montauk.
- **Circuiti elettronici**: le giunzioni sono i vertici, i componenti sono gli archi.
- **Altri grafi e reti** (p. 6): reti sociali, il World Wide Web, il flusso di controllo di un programma, le similarità a coppie tra oggetti.

![[08-grafi-e-alberi-p4-rete-stradale.png]]
![[08-grafi-e-alberi-p5-circuito.png]]

### Definizione · [[08-Grafi e alberi.pdf#page=8|p. 8]], [[08-Grafi e alberi.pdf#page=9|9]], [[08-Grafi e alberi.pdf#page=10|p. 10]], [[08-Grafi e alberi.pdf#page=11|p. 11]], [[08-Grafi e alberi.pdf#page=12|p. 12]], [[08-Grafi e alberi.pdf#page=13|p. 13]], [[08-Grafi e alberi.pdf#page=14|p. 14]], [[08-Grafi e alberi.pdf#page=15|p. 15]], [[08-Grafi e alberi.pdf#page=16|p. 16]]

Il primo passo in ogni problema su grafi è capire **con che tipo di grafo** si ha a che fare: il tipo di grafo ha un grande impatto su quali algoritmi sono appropriati ed efficienti. Imparare il vocabolario («talk the talk») è parte importante del saperli usare («walk the walk»).

Annotazione a mano su p. 8: i grafi «permettono di rappresentare relazioni fra un dato e i suoi simili».

| Coppia | Definizione (slide) | Esempi (slide) |
|---|---|---|
| **orientato / non orientato** | $G$ è non orientato se $(x, y) \in E$ implica $(y, x) \in E$ | reti stradali **tra** città: non orientate; reti di strade **dentro** una città: quasi sempre orientate, per i sensi unici. La maggior parte dei grafi di interesse teorico è non orientata |
| **pesato / non pesato** | nei grafi pesati a ogni arco (o vertice) è assegnato un valore numerico, il **peso** | gli archi di una rete stradale possono pesare quanto la lunghezza, il tempo di percorrenza o il limite di velocità; nei grafi non pesati non c'è distinzione di costo tra archi e vertici |
| **semplice / non semplice** | un **cappio** (*self-loop*) è un arco $(x, x)$ con un solo vertice; un arco $(x, y)$ è un **multi-arco** se compare più di una volta. Un grafo senza queste strutture è **semplice** | «Sei amico di te stesso?» |
| **sparso / denso** | sparso quando solo una piccola frazione delle possibili coppie di vertici ha un arco | i grafi sono di solito sparsi per vincoli applicativi: le reti stradali devono essere sparse per via degli incroci. Tipicamente i grafi densi hanno un numero **quadratico** di archi, quelli sparsi sono di dimensione **lineare** |
| **ciclico / aciclico** | un grafo aciclico non contiene cicli. Gli **alberi** sono grafi non orientati, connessi e aciclici | i grafi orientati aciclici si chiamano **DAG**: compaiono nei problemi di scheduling, dove un arco orientato $(x, y)$ indica che $x$ deve avvenire prima di $y$ |
| **immerso / topologico** | un grafo è **immerso** (*embedded*) se ai vertici e agli archi sono state assegnate posizioni geometriche | conta un disegno del grafo, come nelle reti stradali e nei circuiti? Esempi: TSP o cammino minimo su punti del piano; grafi a griglia e grafi planari |

Annotazione a mano su p. 12: un grafo è «complesso» (cioè non semplice) se due nodi sono collegati direttamente con due archi diversi (l'ultima parola è di lettura incerta).

![[08-grafi-e-alberi-p10-orientato.png]]
![[08-grafi-e-alberi-p11-pesato.png]]
![[08-grafi-e-alberi-p12-non-semplice.png]]
![[08-grafi-e-alberi-p13-denso.png]]
![[08-grafi-e-alberi-p14-aciclico.png]]
![[08-grafi-e-alberi-p15-topologico.png]]

### Terminologia: il grafo delle amicizie · [[08-Grafi e alberi.pdf#page=18|p. 18]], [[08-Grafi e alberi.pdf#page=19|p. 19]], [[08-Grafi e alberi.pdf#page=20|p. 20]], [[08-Grafi e alberi.pdf#page=21|p. 21]], [[08-Grafi e alberi.pdf#page=22|p. 22]], [[08-Grafi e alberi.pdf#page=17|p. 17]], [[08-Grafi e alberi.pdf#page=23|p. 23]], [[08-Grafi e alberi.pdf#page=24|p. 24]]

Si considera il grafo in cui i vertici sono persone e c'è un arco tra due persone **se e solo se** sono amiche. È ben definito su qualunque insieme di persone (Stony Brook, New York, il mondo). Che domande ci si può porre su questo grafo? Ognuna introduce un concetto.

![[08-grafi-e-alberi-p18-grafo-amicizie.png]]
*Hermione Granger, Ron Weasley, Harry Potter e Dobby sono collegati; Voldemort è un vertice isolato, senza archi.*

| Domanda (slide) | Concetto | Definizione |
|---|---|---|
| «Se io sono tuo amico, tu sei mio amico?» (p. 19) | grafo **non orientato** / **orientato** | non orientato se $(x, y) \in E$ implica $(y, x) \in E$; altrimenti orientato |
| «Sono collegato a una celebrità da una catena di amici?» (p. 20) | **cammino** | sequenza di archi che collega due vertici |
| «C'è un cammino di amici tra due persone qualsiasi?» (p. 21) | grafo **connesso** / **fortemente connesso** | connesso se c'è un cammino tra due vertici qualsiasi; un grafo orientato è fortemente connesso se c'è un cammino orientato tra due vertici qualsiasi |
| «Chi ha più amici?» (p. 22) | **grado** | numero di archi adiacenti al vertice |
| «Qual è la cricca più grande?» (p. 23) | **cricca** (*clique*) | sottografo completo: ogni coppia dei suoi vertici è collegata da un arco |

Dettagli delle slide:
- p. 19: il grafo «ha sentito parlare di» è **orientato**, perché moltissime persone famose non hanno mai sentito parlare dell'autore; un grafo che richiede un partner è presumibilmente **non orientato**.
- p. 20: per impressionare qualcuno con la vicinanza al Presidente conviene dire che un membro del proprio club del libro lo conosce, piuttosto che spiegare come si è entrati nel club. Interessa quindi il **cammino minimo** tra due nodi. La figura collega Steve a Joe Biden passando per Mark Fasciano, Michael Ashner, Donald Trump e Steve Israel.
- p. 21: l'idea dei «sei gradi di separazione» presuppone che la rete sociale mondiale sia un grafo **connesso**.
- p. 23: una cricca sociale è un gruppo di amici reciproci che stanno insieme. Le cricche sono i sottografi **più densi possibile**; nel grafo delle amicizie ci si aspetta che le cricche grandi corrispondano a luoghi di lavoro, quartieri, organizzazioni religiose, scuole.

![[08-grafi-e-alberi-p20-cammino.png]]

### Cos'è · [[08-Grafi e alberi.pdf#page=26|p. 26]]

Ci sono due strutture dati principali per rappresentare i grafi: la matrice di adiacenza e le [[liste-di-adiacenza]]. Si assume che il grafo $G = (V, E)$ abbia $n$ vertici e $m$ archi.

Si può rappresentare $G$ con una matrice $M$ di dimensione $n \times n$, in cui l'elemento $M[i, j]$ vale, ad esempio, **1** se $(i, j)$ è un arco di $G$ e **0** se non lo è. Può però usare uno spazio eccessivo per grafi con molti vertici e relativamente pochi archi.

La slide chiede: si può risparmiare spazio (1) se il grafo è **non orientato**? (2) se il grafo è **sparso**? (risposte sotto).

### Appunti a mano della lezione · [[08-Grafi e alberi.pdf#page=27|p. 27]], [[08-Grafi e alberi.pdf#page=39|p. 39]]

- «Dobbiamo poter mantenere le informazioni degli archi, poiché su queste si basano le proprietà dei grafi».
- «Posso avere più nodi che archi → grafo non connesso».
- «Matrice come bitmap per memorizzare le interconnessioni», con l'esempio di una matrice $2 \times 2$ sui vertici $a$, $b$: riga $a$ = (0, 1), riga $b$ = (2, 0), dove il 2 è il «peso dell'arco». In rosso: «matrice di adiacenza».
- In verde: «con una matrice ho rappresentato l'intera struttura astratta del grafo → con una sola struttura dati».

![[08-grafi-e-alberi-p27-appunti-matrice.png]]

> ⚠️ Contraddizione (🧩, sul secondo appunto): avere meno archi che nodi non basta a dire che il grafo **non è connesso**. Un [[albero]] con $n$ nodi è connesso e ha $n - 1$ archi, cioè meno archi che nodi. È vero che con **meno di $n - 1$** archi un grafo non può essere connesso: ogni arco aggiunto unisce al più due componenti, quindi partendo da $n$ vertici isolati servono almeno $n - 1$ archi per arrivare a una sola componente.

### Cos'è · [[08-Grafi e alberi.pdf#page=28|p. 28]], [[08-Grafi e alberi.pdf#page=29|29]]

Una **lista di adiacenza** è un array di $N \times 1$ puntatori, in cui l'$i$-esimo elemento punta a una [[lista-concatenata]] degli archi incidenti sul vertice $i$.

- Per verificare se l'arco $(i, j)$ è nel grafo si cerca $j$ nella lista $i$-esima, in tempo $O(d_i)$, dove $d_i$ è il **grado** dell'$i$-esimo vertice.
- $d_i$ può essere molto minore di $n$ quando il grafo è sparso.
- Se necessario, le due **copie** di ogni arco possono essere collegate da un puntatore per facilitare le cancellazioni.

![[08-grafi-e-alberi-p28-liste-di-adiacenza.png]]
*Grafo non orientato con 5 vertici e 7 archi e le sue liste: 1 → 2, 5; 2 → 1, 5, 4, 3; 3 → 2, 4; 4 → 5, 2, 3; 5 → 1, 2, 4. Ogni arco compare in due liste.*

Appunto a mano di p. 29 (pagina a righe): «modalità di navigazione → come scorro il grafo partendo da un nodo». La lista del vertice $v$ dà direttamente i vicini di $v$, cioè i passi possibili da $v$.

![[08-grafi-e-alberi-p29-appunti-navigazione.png]]

### Confronto con la matrice di adiacenza · [[08-Grafi e alberi.pdf#page=30|p. 30]]

| Confronto | Vincitore |
|---|---|
| più veloce verificare se $(x, y)$ esiste? | matrici |
| più veloce trovare il grado di un vertice? | liste |
| meno memoria su grafi piccoli? | liste ($m + n$ contro $n^2$) |
| meno memoria su grafi grandi? | matrici (vittoria di poco) |
| inserimento o cancellazione di un arco? | matrici, $O(1)$ |
| più veloce attraversare il grafo? | liste ($m + n$ contro $n^2$) |
| migliori per la maggior parte dei problemi? | liste |

Entrambe le rappresentazioni sono molto utili e hanno proprietà diverse, anche se le liste di adiacenza sono probabilmente migliori per la maggior parte dei problemi.

![[08-grafi-e-alberi-p30-confronto-rappresentazioni.png]]

### Implementazione in C · [[08-Grafi e alberi.pdf#page=31|p. 31]]–[[08-Grafi e alberi.pdf#page=35|35]], [[08-Grafi e alberi.pdf#page=36|p. 36]]

**Archi** (p. 31):
```c
typedef struct edgenode {
    int y;                    /* adjacency info */
    int weight;               /* edge weight, if any */
    struct edgenode *next;    /* next edge in list */
} edgenode;
```

**Grafo**:
```c
typedef struct {
    edgenode *edges[MAXV+1];  /* adjacency info */
    int degree[MAXV+1];       /* outdegree of each vertex */
    int nvertices;            /* number of vertices in the graph */
    int nedges;               /* number of edges in the graph */
    int directed;             /* is the graph directed? */
} graph;
```

Il campo `degree` conta il numero di voci significative per il vertice dato. Un arco non orientato $(x, y)$ compare **due volte** in qualunque struttura basata sull'adiacenza: una volta come $y$ nella lista di $x$ e una volta come $x$ nella lista di $y$.

**Inizializzazione**:
```c
void initialize_graph(graph *g, bool directed) {
    int i;                    /* counter */
    g->nvertices = 0;
    g->nedges = 0;
    g->directed = directed;
    for (i = 1; i <= MAXV; i++) {
        g->degree[i] = 0;
    }
    for (i = 1; i <= MAXV; i++) {
        g->edges[i] = NULL;
    }
}
```

**Lettura**: un formato tipico ha una prima riga con il numero di vertici e di archi, seguita dall'elenco degli archi, una coppia di vertici per riga.
```c
void read_graph(graph *g, bool directed) {
    int i;                    /* counter */
    int m;                    /* number of edges */
    int x, y;                 /* vertices in edge (x,y) */
    initialize_graph(g, directed);
    scanf("%d %d", &(g->nvertices), &m);
    for (i = 1; i <= m; i++) {
        scanf("%d %d", &x, &y);
        insert_edge(g, x, y, directed);
    }
}
```

**Inserimento di un arco** (p. 35):
```c
void insert_edge(graph *g, int x, int y, bool directed) {
    edgenode *p;              /* temporary pointer */
    p = malloc(sizeof(edgenode));   /* allocate edgenode storage */
    p->weight = 0;
    p->y = y;
    p->next = g->edges[x];
    g->edges[x] = p;          /* insert at head of list */
    g->degree[x]++;
    if (!directed) {
        insert_edge(g, y, x, true);
    } else {
        g->nedges++;
    }
}
```

### Definizione · [[08-Grafi e alberi.pdf#page=37|p. 37]], [[08-Grafi e alberi.pdf#page=38|38]]

Riprendendo tre caratteristiche dei [[tipi-di-grafo]]:
- **non orientato**: gli archi non hanno un verso;
- **connesso**: ogni coppia di nodi è collegata da un cammino;
- **aciclico**: non contiene cicli.

Quando tutte e tre le proprietà sono presenti insieme, il grafo prende il nome di **albero**: *un albero è un grafo non orientato, connesso e privo di cicli*.

La slide di p. 38 chiede quale di tre grafi sia un albero: il grafo 1 no (c'è un ciclo), il grafo 2 no (non è connesso), il grafo 3 sì.

![[08-grafi-e-alberi-p37-albero-definizione.png]]
![[08-grafi-e-alberi-p38-quale-e-albero.png]]

### Tre conseguenze della definizione · [[08-Grafi e alberi.pdf#page=39|p. 39]]

1. **Cammino unico:** tra due nodi esiste un solo cammino semplice (in figura il percorso arancione collega E e G).
2. **Archi essenziali:** se si rimuove un arco, il grafo si disconnette.
3. **$n - 1$ archi:** con $n$ nodi gli archi sono sempre $n - 1$ (in figura 7 nodi e 6 archi).

Annotazione a mano sotto la slide: «la complessità spaziale dipende dalla struttura fisica → struttura dati utilizzata».

![[08-grafi-e-alberi-p39-conseguenze-definizione.png]]

### Radice, profondità, altezza · [[08-Grafi e alberi.pdf#page=40|p. 40]], [[08-Grafi e alberi.pdf#page=41|41]]

**La radice è una scelta (quasi) arbitraria** (p. 40): con una radice si può leggere lo stesso grafo come una **gerarchia**. Nell'esempio, scegliendo A come radice: B, C, D sono i **figli** di A; C, E, F, G sono le **foglie**.

Dopo aver scelto una radice si misura la distanza dei nodi da essa (p. 41):
- **profondità di un nodo:** numero di archi dalla radice al nodo; la radice ha profondità 0;
- **altezza dell'albero:** massima profondità tra tutti i nodi;
- **livelli:** nodi con la stessa profondità appartengono allo stesso livello.

Nell'esempio di p. 41 (A radice; B, C a profondità 1; D, E, F, G a profondità 2): profondità(G) = 2, altezza dell'albero $h = 2$.

![[08-grafi-e-alberi-p40-radice.png]]
![[08-grafi-e-alberi-p41-profondita-altezza.png]]

### Bilanciamento · 08-Grafi e alberi.pdf [[08-Grafi e alberi.pdf#page=42|p. 42]] · 09-Alberi binari ricerca.pdf [[09-Alberi binari ricerca.pdf#page=6|p. 6]]

Due alberi binari con 7 nodi, ma con altezze molto diverse:
- **bilanciato**: 7 nodi, altezza 2, $h = \Theta(\log n)$;
- **degenere** (una catena A–B–C–D–E–F–G): 7 nodi, altezza 6, $h = \Theta(n)$.

**Un algoritmo che percorre un solo ramo impiega $O(h)$ passi.**

![[08-grafi-e-alberi-p42-bilanciamento.png]]

### La base del logaritmo: perché $\log_k n$ · [[08-Grafi e alberi.pdf#page=43|p. 43]]

La base dipende dal **fattore di ramificazione** $k$ (figli per nodo), se l'albero è sufficientemente bilanciato:
- binario (2 figli per nodo): $h = \Theta(\log_2 n)$;
- ternario (3 figli per nodo): $h = \Theta(\log_3 n)$;
- $k$-ario ($k$ figli per nodo): $h = \Theta(\log_k n)$.

**Albero $k$-ario perfetto:** ogni nodo interno ha esattamente $k$ figli e tutte le foglie sono alla stessa profondità. Al livello $i$ ci sono $k^i$ nodi, quindi con altezza $h$:
$$
n = 1 + k + k^2 + \dots + k^h = \frac{k^{h+1} - 1}{k - 1} \qquad\Longrightarrow\qquad h = \log_k\big(n(k-1) + 1\big) - 1
$$
Con $k$ costante: $h = \Theta(\log_k n)$. La stessa crescita vale per alberi $k$-ari sufficientemente bilanciati.

![[08-grafi-e-alberi-p43-base-logaritmo.png]]

### Dove ritroviamo gli alberi · [[08-Grafi e alberi.pdf#page=44|p. 44]]

- **Gerarchie di cartelle**: progetto → src, test → main.c, test.c.
- **Alberi di espressione**: $(a + b) \times c$, con gli operatori nei nodi interni e gli operandi nelle foglie.
- **Alberi di ricorsione**: $T(n)$ → due $T(n/2)$ → quattro $T(n/4)$, come in [[merge-sort]] (→ [[metodo-albero-di-ricorrenza]]).

«Stessa struttura matematica, interpretazioni differenti.»

![[08-grafi-e-alberi-p44-dove-alberi.png]]

*Approfondimenti nel wiki: [[lezione-08-grafi-e-alberi]], [[grafo]], [[tipi-di-grafo]], [[matrice-di-adiacenza]], [[liste-di-adiacenza]], [[albero]]*

## Lezione 9 — Alberi binari di ricerca

*Fonte: 09-Alberi binari ricerca.pdf.*

### Cos'è · [[09-Alberi binari ricerca.pdf#page=2|p. 2]], [[09-Alberi binari ricerca.pdf#page=4|p. 4]], [[09-Alberi binari ricerca.pdf#page=1|p. 1]]

Le code di priorità sono strutture dati che offrono una **flessibilità in più rispetto all'ordinamento**. È importante perché i lavori (*job*) entrano spesso in un sistema a intervalli arbitrari: è più conveniente inserire un nuovo job in una coda di priorità che riordinare tutto a ogni nuovo arrivo (p. 2).

Nella teoria delle code, una coda di priorità è una **struttura dati astratta** (→ [[tipo-di-dato-astratto]]), simile a una [[coda]] o a una [[pila]], ma diversa perché ogni elemento inserito possiede una sua **priorità** (p. 4):
- un elemento con priorità più alta viene posto prima di un elemento con priorità più bassa;
- l'elemento con priorità più alta si trova in **testa** alla coda, quello con priorità più bassa in **fondo**.

![[09-alberi-binari-ricerca-p2-code-priorita.png]]

### Operazioni · [[09-Alberi binari ricerca.pdf#page=3|p. 3]]

La coda di priorità di base supporta tre operazioni principali:
- **Insert($Q$, $x$)**: dato un elemento $x$ con chiave $k$, lo inserisce nella coda di priorità $Q$;
- **Find-Minimum($Q$)** o **Find-Maximum($Q$)**: restituisce un puntatore all'elemento la cui chiave è più piccola (più grande) di ogni altra chiave in $Q$;
- **Delete-Minimum($Q$)** o **Delete-Maximum($Q$)**: rimuove da $Q$ l'elemento con chiave minima (massima).

![[09-alberi-binari-ricerca-p3-operazioni-coda-priorita.png]]

### Esempio · [[09-Alberi binari ricerca.pdf#page=5|p. 5]]

Input 1, 5, 3, 2, 6, dove un numero più alto ha priorità più alta. La coda è tenuta come sequenza **ordinata per priorità decrescente**:

| Operazione | Contenuto della coda (pq) |
|---|---|
| enqueue(1) | 1 |
| enqueue(5) | 5, 1 |
| enqueue(3) | 5, 3, 1 |
| enqueue(2) | 5, 3, 2, 1 |
| enqueue(6) | 6, 5, 3, 2, 1 |

![[09-alberi-binari-ricerca-p5-implementazione-coda-priorita.png]]

### Cos'è · [[09-Alberi binari ricerca.pdf#page=6|p. 6]]

- Gli alberi di ricerca sono strutture dati che supportano molte delle operazioni definite su **insiemi dinamici**: *Search, Minimum, Maximum, Predecessor, Successor, Insert, Delete*.
- Possono essere usati sia come **dizionario** sia come **coda a priorità** (→ [[coda-di-priorita]]).
- Le operazioni base richiedono un tempo **proporzionale all'altezza** $h$:
  - $\lg n$ se l'albero è completo;
  - $n$ nel caso degenere di [[lista-concatenata]].
- L'altezza attesa di un albero costruito in maniera aleatoria è $\lg n$...
- ...ma non sempre è possibile costruire l'albero in questa maniera.
- Alcuni tipi particolari di alberi di ricerca presentano nel caso peggiore un tempo di esecuzione «buono».

### Proprietà (invariante della struttura) · [[09-Alberi binari ricerca.pdf#page=7|p. 7]]

Un albero binario di ricerca soddisfa la seguente proprietà. Sia $x$ un nodo dell'albero:
- se $y$ è nel **sottoalbero sinistro** di $x$, allora $key[y] \le key[x]$;
- se $y$ è nel **sottoalbero destro** di $x$, allora $key[y] \ge key[x]$.

Esempio della slide: radice 5; figlio sinistro 3, con figli 2 e 5; figlio destro 7, con figlio destro 8.

![[09-alberi-binari-ricerca-p7-proprieta-bst.png]]

### Problema risolto · [[09-Alberi binari ricerca.pdf#page=8|p. 8]]

La proprietà di un [[albero-binario-di-ricerca]] consente di **stampare tutte le chiavi in ordine crescente** mediante una visita in ordine dell'albero.

- **Input:** un nodo $x$ (per l'intero albero, la radice).
- **Output:** le chiavi del sottoalbero di radice $x$, stampate in ordine non decrescente.

### Pseudocodice · [[09-Alberi binari ricerca.pdf#page=8|p. 8]]

```
Inorder-Tree-Walk (x)
1  if x≠NIL
2     then Inorder-Tree-Walk (left[x])
3          print key[x]
4          Inorder-Tree-Walk (right[x])
```

![[09-alberi-binari-ricerca-p8-inorder-pseudocodice.png]]

> ⚠️ Contraddizione (di notazione): `then` e l'assenza di blocchi espliciti sono nello stile della 2ª edizione del Cormen, non nelle [[pseudocodice|convenzioni del corso]]. Le righe 2–4 sono tutte il corpo dell'`if`.

### Idea · [[09-Alberi binari ricerca.pdf#page=9|p. 9]]

Visita in ordine: **sinistra → nodo → destra**. Prima si visita tutto il sottoalbero sinistro, poi si stampa la chiave del nodo, poi si visita il sottoalbero destro.

### Esempio di esecuzione · [[09-Alberi binari ricerca.pdf#page=7|p. 7]], [[09-Alberi binari ricerca.pdf#page=9|p. 9]]

![[09-alberi-binari-ricerca-p9-visita-in-ordine.png]]

Chiamate totali: 13, di cui 6 su nodi e 7 su `NIL`.

### Complessità · [[09-Alberi binari ricerca.pdf#page=9|p. 9]]

### Problema risolto · [[09-Alberi binari ricerca.pdf#page=10|p. 10]]

Dato il puntatore alla radice e una chiave, restituisce il puntatore all'elemento con la data chiave, se esiste, e `NIL` altrimenti.

### Idea · [[09-Alberi binari ricerca.pdf#page=10|p. 10]]

I nodi incontrati nella ricerca formano un **percorso verso il basso** dalla radice: a ogni nodo il confronto con $key[x]$ dice in quale dei due sottoalberi può trovarsi la chiave, e l'altro viene scartato.

### Pseudocodice · [[09-Alberi binari ricerca.pdf#page=10|p. 10]], [[09-Alberi binari ricerca.pdf#page=11|11]]

```
Tree-Search (x,k)
1  if x=NIL or key[x]=k
2     then return x
3  if k < key[x]
4     then return Tree-Search (left[x],k)
5     else return Tree-Search (right[x],k)
```

```
Iterative-Tree-Search (x,k)
1  while x≠NIL and key[x]≠k
2      if k < key[x]
3         then x ← left[x]
4         else x ← right[x]
5  return x
```

![[09-alberi-binari-ricerca-p10-tree-search.png]]
![[09-alberi-binari-ricerca-p11-iterative-tree-search.png]]

### Complessità · [[09-Alberi binari ricerca.pdf#page=10|p. 10]]

### Problema risolto · [[09-Alberi binari ricerca.pdf#page=12|p. 12]]

Trovare il nodo con la chiave minima (massima) nel sottoalbero di radice $x$ di un [[albero-binario-di-ricerca]].

### Idea · [[09-Alberi binari ricerca.pdf#page=12|p. 12]]

- L'elemento **minimo** può essere trovato percorrendo, a partire dalla radice, sempre il sottoalbero di **sinistra**.
- L'elemento **massimo** può essere trovato percorrendo, a partire dalla radice, sempre il sottoalbero di **destra**.

### Pseudocodice · [[09-Alberi binari ricerca.pdf#page=12|p. 12]]

```
Tree-Minimum (x)
1  while left[x]≠NIL
2      do x ← left[x]
3  return x

Tree-Maximum (x)
4  while right[x]≠NIL
5      do x ← right[x]
6  return x
```

![[09-alberi-binari-ricerca-p12-minimo-massimo.png]]

### Complessità · [[09-Alberi binari ricerca.pdf#page=12|p. 12]]

### Problema risolto · [[09-Alberi binari ricerca.pdf#page=13|p. 13]]

Dato un nodo, il suo **successore** è quello che lo segue nella visita in ordine dell'albero (→ [[inorder-tree-walk]]). Se il nodo ha la chiave massima, il successore è `NIL`.

### Idea · [[09-Alberi binari ricerca.pdf#page=13|p. 13]]

Due casi:
1. **Se il nodo ha un figlio destro**, il successore è il **minimo del sottoalbero destro**. Esempio: il successore di 6 è 7.
2. **Altrimenti**, è il più «basso» antenato di $x$ il cui **figlio sinistro è un antenato di $x$**. Esempio: il successore di 13 è 15.

![[09-alberi-binari-ricerca-p13-successore-casi.png]]

### Esempio di esecuzione · [[09-Alberi binari ricerca.pdf#page=13|p. 13]], [[09-Alberi binari ricerca.pdf#page=15|p. 15]]

![[09-alberi-binari-ricerca-p15-successore-animazione.png]]

### Pseudocodice · [[09-Alberi binari ricerca.pdf#page=14|p. 14]]

```
Tree-Successor (x)
1  if right[x]≠NIL
2     then return Tree-Minimum(right[x])
3  y ← p[x]
4  while y≠NIL and x=right[y]
5      do x ← y
6         y ← p[y]
7  return y
```

[[tree-minimum-maximum|Tree-Minimum]] è la procedura di p. 12.

![[09-alberi-binari-ricerca-p14-tree-successor.png]]

### Complessità · [[09-Alberi binari ricerca.pdf#page=14|p. 14]]

### Problema risolto · [[09-Alberi binari ricerca.pdf#page=16|p. 16]]

Inserire un nuovo nodo $z$, con $key[z]$ assegnata e $left[z] = right[z] = \mathrm{NIL}$, nell'albero $T$, rispettando la proprietà dell'[[albero-binario-di-ricerca]].

### Idea · [[09-Alberi binari ricerca.pdf#page=16|p. 16]]

Rispettando la proprietà di un albero di ricerca, l'elemento da inserire **attraversa l'albero verso il basso** a partire dalla radice. Il puntatore $x$ scende come in una ricerca; $y$ resta un passo indietro e, quando $x$ diventa `NIL`, è il nodo a cui attaccare $z$.

### Pseudocodice · [[09-Alberi binari ricerca.pdf#page=16|p. 16]]

```
Tree-Insert (T,z)
1  y ← NIL
2  x ← root[T]
3  while x≠NIL
4      do y ← x
5         if key[z] < key[x]
6            then x ← left[x]
7            else x ← right[x]
8  p[z] ← y
9  if y = NIL
10    then root[T] ← z        // albero vuoto
11    else if key[z] < key[y]
12       then left[y] ← z
13       else right[y] ← z
```

![[09-alberi-binari-ricerca-p16-tree-insert.png]]

Simboli: $z$ = nodo da inserire; $x$ = nodo corrente della discesa; $y$ = padre di $x$, cioè l'ultimo nodo visitato.

### Esempio di esecuzione · [[09-Alberi binari ricerca.pdf#page=16|p. 16]]–[[09-Alberi binari ricerca.pdf#page=18|18]]

![[09-alberi-binari-ricerca-p17-inserimento-19.png]]
![[09-alberi-binari-ricerca-p18-inserimento-10.png]]

> ⚠️ Contraddizione (🧩): la figura di p. 18 disegna 19 come figlio destro di 18 e 20 come figlio destro di 19. È un BST valido, ma non è l'albero che si ottiene inserendo 19 con Tree-Insert nell'albero di p. 17: lì 19 diventa figlio sinistro di 20 (prima riga della tabella). L'inserimento di 10 dà lo stesso risultato nei due alberi, perché 10 scende nel sottoalbero sinistro della radice.

### Complessità · [[09-Alberi binari ricerca.pdf#page=16|p. 16]]

### Idea · [[09-Alberi binari ricerca.pdf#page=19|p. 19]]

Si considerano 3 diversi casi:
- il nodo **non ha figli** ($z'$);
- il nodo ha **un solo figlio** ($z''$);
- il nodo ha **due figli** ($z'''$):
  - si cerca il **successore** $y$, che **non ha il figlio di sinistra**;
  - si taglia fuori $y$;
  - si scambiano chiave e dati satellite di $z$ con quelli di $y$.

In tutti i casi c'è **un nodo da tagliare fuori**: $z$ oppure il successore di $z$, e **ha al più un solo figlio**.

Nell'albero della slide (radice 15; 6 con figli 3 e 10; 3 con figlio 2; 10 con figli 8 e 13; 8 con figlio destro 9; 18 con figli 17 e 20): $z' = 20$, $z'' = 3$, $z''' = 6$. La nuvoletta «??» sul nodo 6 chiede che cosa debba prendere il suo posto.

![[09-alberi-binari-ricerca-p19-eliminazione-casi.png]]

### Esempio di esecuzione · [[09-Alberi binari ricerca.pdf#page=19|p. 19]], [[09-Alberi binari ricerca.pdf#page=21|p. 21]]

![[09-alberi-binari-ricerca-p21-eliminazione-6.png]]

### Pseudocodice · [[09-Alberi binari ricerca.pdf#page=20|p. 20]]

```
Tree-Delete (T,z)
1  if left[z]=NIL or right[z]=NIL
2     then y ← z
3     else y ← Tree-Successor (z)
4  if left[y] ≠NIL
5     then x ← left[y]
6     else x ← right[y]
7  if x ≠NIL                 // y non e' foglia
8     then p[x] ← p[y]
9  if p[y] = NIL             // y è radice
10    then root[T] ← x
11    else if y = left[p[y]]
12       then left[p[y]] ← x
13       else right[p[y]] ← x
14 if y ≠z                   // terzo caso
15    then key[z] ← key[y]
16         Copy y's satellite data into z
17 return y
```

Simboli: $z$ = nodo da eliminare; $y$ = nodo effettivamente tagliato fuori ($z$ stesso o il suo successore); $x$ = l'unico figlio di $y$, oppure `NIL`.

![[09-alberi-binari-ricerca-p20-tree-delete.png]]
*Nella figura le etichette $y'$, $y''$, $y'''$ e $x''$, $x'''$ indicano $y$ e $x$ nei tre casi: per $z'' = 3$, $y'' = 3$ e $x'' = 2$; per $z''' = 6$, $y''' = 8$ e $x''' = 9$.*

> ⚠️ Contraddizione (di notazione): la slide mescola italiano e inglese («Copy y's satellite data into z») e usa lo stile della 2ª edizione del Cormen (`then`, `//`), non le [[pseudocodice|convenzioni del corso]].

### Complessità · [[09-Alberi binari ricerca.pdf#page=20|p. 20]]

*Approfondimenti nel wiki: [[lezione-09-alberi-binari-di-ricerca]], [[coda-di-priorita]], [[albero-binario-di-ricerca]], [[inorder-tree-walk]], [[tree-search]], [[tree-minimum-maximum]], [[tree-successor]], [[tree-insert]], [[tree-delete]]*

## Lezione 10 — Heapsort

*Fonte: 10 - Heap - Heapsort.pdf (50 pagine: slide, con appunti a mano alle p. 2, 3, 5, 7, 14).*

### Heapsort: dove siamo · [[10 - Heap - Heapsort.pdf#page=2|p. 2]], [[10 - Heap - Heapsort.pdf#page=1|p. 1]]

- **Insertion Sort**: $\Theta(n^2)$ nel caso peggiore, $\Theta(n)$ nel migliore; ordina sul posto.
- **Merge Sort**: $\Theta(n \lg n)$; non ordina sul posto (nota a mano: l'uso di memoria cresce troppo velocemente al crescere di $n$).
- **Heap Sort**: $O(n \lg n)$; ordina sul posto (nota a mano: in termini di memoria non si può scendere sotto l'ordine di $O(M)$, almeno in questo caso); basato sulla struttura dati *heap* (struttura dati aggregata).

![[10-heap-heapsort-p2-introduzione-heapsort.png]]
*Note a mano del docente sulla memoria di Merge Sort e Heap Sort.*

### Definizione di heap · [[10 - Heap - Heapsort.pdf#page=3|p. 3]], [[10 - Heap - Heapsort.pdf#page=4|4]]

Un **binary heap** è un albero binario con una chiave in ogni nodo tale che:
1. tutte le foglie stanno al più su due livelli adiacenti (l'albero è *bilanciato*);
2. tutte le foglie dell'ultimo livello stanno a sinistra, e tutti i livelli tranne l'ultimo sono completamente pieni;
3. la chiave nella radice è $\le$ di tutte le chiavi dei figli, e i sottoalberi sinistro e destro sono a loro volta heap binari.

Le condizioni 1 e 2 specificano la **forma** dell'albero, la 3 il **contenuto**. Un heap mantiene un ordine parziale degli elementi: più debole dell'ordine totale (quindi più facile da mantenere), più forte dell'ordine casuale (quindi il minimo si individua in fretta).

![[10-heap-heapsort-p4-binary-heap.png]]
*Un heap con le chiavi 1492, 1783, 1776, 1804, 1865, 1945, 1963, 1918, 2001, 1941, come albero e come array.*

### Rappresentazione con array · [[10 - Heap - Heapsort.pdf#page=5|p. 5]], [[10 - Heap - Heapsort.pdf#page=6|6]]

- $heap\text{-}size[A] \le length[A]$
- $\text{Parent}(i) = \lfloor i/2 \rfloor$, $\text{Left}(i) = 2i$, $\text{Right}(i) = 2i + 1$
- le operazioni si implementano in maniera efficiente

![[10-heap-heapsort-p5-rappresentazione-array-albero.png]]
*Heap $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$ come array e come albero (nota a mano: consiste in una mappa logica per la ricerca).*

- **Max-heap:** $A[i] \le A[\text{Parent}(i)]$ per ogni $i > 1$; nella radice c'è il valore più grande.
- **Min-heap:** $A[i] \ge A[\text{Parent}(i)]$ per ogni $i > 1$; nella radice c'è il valore più piccolo.

### Max-Heapify · [[10 - Heap - Heapsort.pdf#page=7|p. 7]]–[[10 - Heap - Heapsort.pdf#page=11|11]]

Assumendo che gli alberi con radice in $\text{Left}(i)$ e $\text{Right}(i)$ siano max-heap, si vuole fare in modo che anche l'albero con radice in $i$ lo sia (nota a mano: prende un nodo e lo riordina affinché sia un max-heap). Nell'esempio $A = \langle 16, 4, 10, 14, 7, 9, 3, 2, 8, 1 \rangle$, $i = 2$: la chiave 4 viene scambiata con il figlio maggiore 14, poi con il figlio maggiore 8, e il risultato è $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$.

![[10-heap-heapsort-p7-max-heapify-problema.png]]

```
Max-Heapify (A,i)
l ← Left(i)
r ← Right(i)
largest ← i
if l ≤ heap-size[A] and A[l] > A[largest]
    largest ← l
if r ≤ heap-size[A] and A[r] > A[largest]
    largest ← r
if largest ≠ i
    exchange A[i] ↔ A[largest]
    Max-Heapify (A,largest)
```

**Tempo di esecuzione:** tempo costante per individuare il massimo fra tre elementi e fare lo scambio, più il tempo per eseguire Max-Heapify su un problema di dimensione minore.

### Dimensione del sottoproblema · [[10 - Heap - Heapsort.pdf#page=12|p. 12]]–[[10 - Heap - Heapsort.pdf#page=14|14]]

Si pone $n$ = dimensione del problema originario, $m$ = dimensione del sottoalbero con più elementi, $h$ = altezza del nodo.

**Caso 1: ultimo livello pieno** (non è il caso peggiore):

$$
n = \sum_{i=0}^{h} 2^i = 2^{h+1} - 1 \qquad m = \sum_{i=0}^{h-1} 2^i = 2^h - 1 \qquad \frac{m}{n} = \frac{2^h - 1}{2 \cdot 2^h - 1} \xrightarrow[h \to \infty]{} \frac{1}{2}
$$

quindi il sottoproblema è $O(n/2)$.

**Caso 2: ultimo livello pieno a metà** (è il caso peggiore):

$$
m = 2^h - 1 \qquad n = (2^h - 1) + (2^{h-1} - 1) + 1 = 3 \cdot 2^{h-1} - 1 \qquad \frac{m}{n} = \frac{2 \cdot 2^{h-1} - 1}{3 \cdot 2^{h-1} - 1} \xrightarrow[h \to \infty]{} \frac{2}{3}
$$

quindi il sottoproblema è $O(2n/3)$.

![[10-heap-heapsort-p12-sottoproblema-caso-1.png]]
![[10-heap-heapsort-p13-sottoproblema-caso-2.png]]

Il tempo di esecuzione è $T(n) \le T(2n/3) + \Theta(1)$: rientra nel caso 2 del teorema dell'esperto, quindi la complessità di Max-Heapify è $O(\lg n)$.

### Da Max-Heapify a Build-Max-Heap · [[10 - Heap - Heapsort.pdf#page=14|p. 14]]–[[10 - Heap - Heapsort.pdf#page=21|21]]

Max-Heapify può essere usato per «convertire» un array in un heap, partendo dal basso e invocandolo sui nodi (nota a mano: perché per ogni passaggio assumiamo che gli heap inferiori siano tutto ok). I nodi foglia si saltano perché costituiscono un heap di 1 elemento.
- Max-Heapify$(A, i)$: ripristina la proprietà di max-heap nel sottoalbero radicato in $i$, assumendo che i sottoalberi sinistro e destro siano già max-heap.
- Build-Max-Heap$(A)$: trasforma l'intero array in un max-heap, chiamando Max-Heapify sui nodi interni dal basso verso l'alto.

```
Build-Max-Heap (A)
heap-size[A] ← length[A]
for i ← ⌊length[A]/2⌋ downto 1
    do Max-Heapify (A,i)
```

Esempio: partendo da $\langle 4, 1, 3, 2, 16, 9, 10, 14, 8, 7 \rangle$ (p. 15) si arriva, con una chiamata per ogni $i = 5, 4, 3, 2, 1$ (pp. 15–19), a $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$.

![[10-heap-heapsort-p15-build-max-heap-inizio.png]]

**Invariante:** all'inizio di ciascuna iterazione del ciclo `for`, ogni nodo $i+1, i+2, \dots, n$ è la radice di un max-heap.
- *Vero prima della prima iterazione:* $i = \lfloor n/2 \rfloor$, i nodi $i+1..n$ sono foglie e quindi max-heap.
- *Si conserva:* i figli di $i$ sono radici di max-heap (per ipotesi), quindi vale la precondizione di Max-Heapify, che rende anche $i$ radice di un max-heap; decrementando $i$ l'invariante si conserva.
- *Al termine:* tutti i nodi $i \ge 1$ sono radici di max-heap, in particolare per $i = 1$ il vettore è un max-heap.

**Complessità.** $O(n)$ invocazioni di Max-Heapify $\Rightarrow O(n \lg n)$, ma **non è un limite stretto**, dato che:
- un heap di $n$ elementi ha altezza $\lfloor \lg n \rfloor$;
- un heap di $n$ elementi ha al più $\lceil n/2^{h+1} \rceil$ elementi di altezza $h$: le foglie (altezza 0) sono $n - \lfloor n/2 \rfloor = \lceil n/2 \rceil$, i nodi di altezza 1 sono circa la metà, $\lceil n/2^2 \rceil$;
- Max-Heapify ha complessità $O(h)$ per un nodo di altezza $h$.

$$
T(n) = \sum_{h=0}^{\lfloor \lg n \rfloor} \left\lceil \frac{n}{2^{h+1}} \right\rceil O(h) = O\!\left( n \sum_{h=0}^{\lfloor \lg n \rfloor} \frac{h}{2^h} \right) = O\!\left( n \sum_{h=0}^{\infty} \frac{h}{2^h} \right) = O(2n) = O(n)
$$

![[10-heap-heapsort-p21-build-max-heap-complessita.png]]

### Heap-Sort · [[10 - Heap - Heapsort.pdf#page=22|p. 22]]–[[10 - Heap - Heapsort.pdf#page=41|41]]

1. Si rende l'array un max-heap (con Build-Max-Heap): il primo elemento è l'elemento massimo.
2. Si scambia il primo elemento con l'ultimo: l'elemento massimo è «sistemato».
3. Si decrementa la dimensione dell'heap e si invoca Max-Heapify per mantenere la proprietà del max-heap.

Esempio dall'heap $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$: per ogni $i$ un fotogramma «scambiamo … con … e decrementiamo la dimensione dell'heap» e uno «invochiamo Max-Heapify su $A[1]$» (pp. 23–39); essendo rimasto un solo elemento l'algoritmo termina (p. 40).

![[10-heap-heapsort-p23-heapsort-inizio.png]]

| $i$ | Scambio | Dopo Max-Heapify su $A[1]$ (barra = parte ordinata) |
|---|---|---|
| 10 | 16 con 1 | $\langle 14, 8, 10, 4, 7, 9, 3, 2, 1 \mid 16 \rangle$ |
| 9 | 14 con 1 | $\langle 10, 8, 9, 4, 7, 1, 3, 2 \mid 14, 16 \rangle$ |
| 8 | 10 con 2 | $\langle 9, 8, 3, 4, 7, 1, 2 \mid 10, 14, 16 \rangle$ |
| 7 | 9 con 2 | $\langle 8, 7, 3, 4, 2, 1 \mid 9, 10, 14, 16 \rangle$ |
| 6 | 8 con 1 | $\langle 7, 4, 3, 1, 2 \mid 8, 9, 10, 14, 16 \rangle$ |
| 5 | 7 con 2 | $\langle 4, 2, 3, 1 \mid 7, 8, 9, 10, 14, 16 \rangle$ |
| 4 | 4 con 1 | $\langle 3, 2, 1 \mid 4, 7, 8, 9, 10, 14, 16 \rangle$ |
| 3 | 3 con 1 | $\langle 2, 1 \mid 3, 4, 7, 8, 9, 10, 14, 16 \rangle$ |
| 2 | 2 con 1 | $\langle 1 \mid 2, 3, 4, 7, 8, 9, 10, 14, 16 \rangle$ |

```
Heap-Sort (A)
Build-Max-Heap (A)
for i ← length[A] downto 2
    do exchange A[1] ↔ A[i]
       heap-size[A] ← heap-size[A] - 1
       Max-Heapify (A,1)
```

**Tempo di esecuzione:** $O(n \lg n)$. Build-Max-Heap impiega $O(n)$; ci sono $n - 1$ invocazioni di Max-Heapify, ciascuna di costo $O(\lg n)$.

### Code a priorità con un heap · [[10 - Heap - Heapsort.pdf#page=42|p. 42]]–[[10 - Heap - Heapsort.pdf#page=49|49]]

Un max-heap (min-heap) realizza in modo efficiente una coda a massima (minima) priorità: una struttura dati che mantiene un insieme $S$ di elementi e supporta
- **Insert**$(S, x)$: inserisce $x$ in $S$;
- **Maximum**$(S)$ (**Minimum**): restituisce l'elemento con la chiave più grande (piccola);
- **Extract-Max**$(S)$ (**Extract-Min**): rimuove e restituisce l'elemento con la chiave più grande (piccola);
- **Increase-Key**$(S, x, k)$ (**Decrease-Key**): incrementa (decrementa) la chiave di $x$ al valore $k$.

**Heap-Maximum** (tempo $\Theta(1)$):
```
Heap-Maximum (A)
return A[1]
```

**Heap-Extract-Max** (tempo $O(\lg n)$, una sola invocazione di Max-Heapify): l'ultimo elemento viene messo al posto della radice e si invoca Max-Heapify per ristabilire la proprietà.
```
Heap-Extract-Max (A)
if heap-size[A] < 1
    error "heap empty"
max ← A[1]
A[1] ← A[heap-size[A]]
heap-size[A] ← heap-size[A] - 1
Max-Heapify (A,1)
return max
```

**Heap-Increase-Key** (tempo $O(\lg n)$, $O(\lg n)$ scambi): si fa risalire l'elemento di cui si cambia la chiave in direzione della radice fino a trovare la giusta collocazione. Esempio (pp. 45–47): nell'heap $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$ la chiave 4 diventa 15 e viene scambiata con il padre 8.
```
Heap-Increase-Key (A,i,key)
if key < A[i]
    error "new key is smaller"
A[i] ← key
while i > 1 and A[Parent(i)] < A[i]
    exchange A[i] ↔ A[Parent(i)]
    i ← Parent(i)
```

![[10-heap-heapsort-p46-increase-key-chiave.png]]

**Max-Heap-Insert** (tempo $O(\lg n)$, una sola invocazione di Heap-Increase-Key): il nuovo elemento viene messo dopo l'ultimo con valore $-\infty$, poi Heap-Increase-Key imposta la chiave.
```
Max-Heap-Insert (A,key)
heap-size[A] ← heap-size[A] + 1
A[heap-size[A]] ← -∞
Heap-Increase-Key (A,heap-size[A],key)
```

### Heap-Sort da zero · [[10 - Heap - Heapsort.pdf#page=50|p. 50]]

Esercizio: ordinare con Heap-Sort, partendo da zero, l'array $\langle 6, 5, 3, 1, 8, 7, 2, 4 \rangle$.

![[10-heap-heapsort-p50-heapsort-da-zero.png]]

*Approfondimenti nel wiki: [[heap]], [[max-heapify]], [[build-max-heap]], [[heapsort]], [[heap-extract-max]], [[heap-increase-key]], [[max-heap-insert]], [[tracce-su-heap]]*

## Lezione 11 — Alberi rosso-neri

*Fonte: 11 . Alberi rosso-neri.pdf (48 pagine di slide).*

### Perché un heap non basta · [[11 . Alberi rosso-neri.pdf#page=2|p. 2]]–[[11 . Alberi rosso-neri.pdf#page=7|7]], [[11 . Alberi rosso-neri.pdf#page=1|p. 1]]

- Un max-heap garantisce altezza logaritmica $h = \Theta(\log n)$ e permette di accedere al massimo, nella radice, in $O(1)$.
- Non mantiene però l'ordinamento delle chiavi tipico di un BST: non vale la proprietà «sinistra < nodo < destra». Per cercare una chiave arbitraria bisogna, nel caso peggiore, esaminare tutti i nodi: $O(n)$.
- Esempio: cercare la chiave 30. Dal confronto con la radice non si può scegliere un solo sottoalbero: la chiave potrebbe trovarsi sia nel sinistro sia nel destro. Complessità della ricerca: $O(n)$. Un heap risolve il problema dell'altezza ma non permette ricerche efficienti di chiavi arbitrarie.

![[11-alberi-rosso-neri-p3-heap-ricerca.png]]

- Un albero binario di ricerca (BST) permette di cercare, inserire ed eliminare una chiave in tempo proporzionale all'altezza $h$ dell'albero.
- Tuttavia, se le chiavi vengono inserite in ordine (1, 2, 3, …) il BST può degenerare in una lista concatenata: l'altezza diventa $\Theta(n)$ e le operazioni richiedono $O(n)$ nel caso peggiore.
- Si possono «fondere» le idee di un BST e di un heap per ottenere una struttura dati che conservi l'ordinamento del BST ma garantisca altezza logaritmica anche nel caso peggiore?

### Alberi rosso-neri: a cosa servono · [[11 . Alberi rosso-neri.pdf#page=8|p. 8]], [[11 . Alberi rosso-neri.pdf#page=9|9]]

Si usano perché risolvono un problema concreto: mantenere un insieme di chiavi ordinato su cui si fanno inserimenti, cancellazioni e ricerche in modo
- veloce, tempo $O(\log n)$;
- garantito nel caso pessimo (non solo «in media»);
- con un'implementazione facile da scrivere.

In un normale BST la proprietà è «a sinistra <, a destra >» e le operazioni (search, insert, delete) percorrono un cammino dalla radice a una foglia, con costo circa l'altezza. Se si inseriscono chiavi già ordinate (1, 2, 3, 4, 5, …) l'albero diventa una lista, $h = n$, e i tempi diventano $O(n)$ invece di $O(\log n)$: i BST «puri» non garantiscono buone prestazioni nel caso pessimo.

### Definizione · [[11 . Alberi rosso-neri.pdf#page=10|p. 10]]–[[11 . Alberi rosso-neri.pdf#page=13|13]]

Gli **alberi rosso-neri** sono alberi di ricerca in cui ogni nodo ha un attributo addizionale $color$, che può valere rosso o nero. I puntatori a NIL sono sostituiti da **nodi foglia esterni**. Devono valere:
1. ogni nodo è o rosso o nero;
2. la radice è nera;
3. ogni nodo foglia esterno (NIL) è nero;
4. se un nodo è rosso, entrambi i figli sono neri;
5. per ogni nodo, tutti i percorsi dal nodo alle foglie contengono lo stesso numero di nodi neri.

Gli alberi rosso-neri garantiscono che nessun percorso dalla radice a una foglia è lungo più del doppio di un altro percorso.

![[11-alberi-rosso-neri-p11-esempio-albero.png]]
*Un albero rosso-nero con le foglie NIL.*

Nell'implementazione c'è una **unica sentinella** $nil[T]$, di colore nero (gli altri attributi sono indifferenti). Per comodità di visualizzazione la sentinella si omette nelle figure.

### Black-height · [[11 . Alberi rosso-neri.pdf#page=14|p. 14]]

La **black-height** $bh(x)$ di un nodo $x$ è il numero di nodi neri lungo un qualunque percorso da $x$ a una foglia. Dal conteggio è escluso $x$ ed è incluso il nodo foglia esterno. La black-height di un albero rosso-nero è la black-height della radice. È una misura parziale (solo i neri), mentre l'altezza conta tutti i nodi: in un albero rosso-nero l'altezza è al massimo il doppio della black-height della radice, ma in generale non sono uguali.

$$
bh(x) \le h(x) \le 2 \cdot bh(x)
$$

### Altezza di un albero rosso-nero · [[11 . Alberi rosso-neri.pdf#page=15|p. 15]], [[11 . Alberi rosso-neri.pdf#page=16|16]]

**Teorema.** Un albero rosso-nero con $n$ nodi interni ha altezza al più $2\lg(n+1)$.

Si dimostra prima che un sottoalbero con radice in un nodo $x$ contiene almeno $2^{bh(x)} - 1$ nodi interni, per induzione sull'altezza di $x$:
- *Altezza 0:* è un nodo foglia esterno e la tesi è vera perché $2^{bh(x)} - 1 = 2^0 - 1 = 0$ e il sottoalbero con radice in una foglia esterna non contiene nodi interni.
- *Passo induttivo:* si consideri un nodo interno $x$ con altezza $> 0$ e due figli. Ciascun figlio ha black-height $bh(x)$ se è rosso, $bh(x) - 1$ se è nero. Dato che l'altezza dei figli è minore di quella di $x$, si applica l'ipotesi induttiva: ogni figlio ha almeno $2^{bh(x)-1} - 1$ nodi interni. Quindi $x$ ha almeno $\left(2^{bh(x)-1} - 1\right) + \left(2^{bh(x)-1} - 1\right) + 1 = 2^{bh(x)} - 1$ nodi interni.

Dimostrazione del teorema:
- per la proprietà 4, almeno la metà dei nodi su ogni percorso dalla radice a una foglia, escludendo la radice, sono neri;
- quindi la black-height $bh$ della radice deve essere almeno $h/2$, dove $h$ è l'altezza dell'albero ($h \le 2\,bh$);
- il numero di nodi interni $n$ è almeno $2^{h/2} - 1$:

$$
n \ge 2^{bh} - 1 \ge 2^{h/2} - 1 \iff \lg(n+1) \ge \frac{h}{2} \iff h \le 2\lg(n+1)
$$

La tesi è dimostrata.

### Navigazione e modifica · [[11 . Alberi rosso-neri.pdf#page=17|p. 17]]

Le query Minimum, Maximum, Successor e Predecessor richiedono un tempo $O(\lg n)$ su un albero rosso-nero. Insert e Delete vanno invece opportunamente riviste per preservare le proprietà dell'albero.

### Rotazioni · [[11 . Alberi rosso-neri.pdf#page=18|p. 18]]–[[11 . Alberi rosso-neri.pdf#page=20|20]]

Per preservare le proprietà di un albero rosso-nero vengono effettuate delle **rotazioni**, che preservano le proprietà di un albero di ricerca.
- **Rotazione a sinistra** (sul nodo $x$): presuppone che il figlio di destra non sia NIL. Nella figura $A = x$, con figlio destro $B$; $\alpha$ è il sottoalbero sinistro di $A$, $\beta$ e $\gamma$ quelli di $B$.
  1. $\beta$ diventa figlio di destra di $A$;
  2. il padre di $A$ diventa $B$ (il padre di $A$ diventa il padre di $B$);
  3. $A$ diventa il figlio di sinistra di $B$.
- In maniera equivalente si definisce la rotazione a destra.

```
Left-Rotate (T,x)
y ← right[x]
// operazione 1.
right[x] ← left[y]
if left[y] ≠ nil[T]
    then p[left[y]] ← x
// operazione 2.
p[y] ← p[x]
if p[x] = nil[T]
    then root[T] ← y
    else if x = left[p[x]]
        then left[p[x]] ← y
        else right[p[x]] ← y
// operazione 3.
left[y] ← x
p[x] ← y
```

Il tempo di esecuzione è $O(1)$.

![[11-alberi-rosso-neri-p20-rotazioni-esempio.png]]
*Left-Rotate (T,x) con $x = 11$ porta l'albero in alto in quello in basso; Right-Rotate (T,y) con $y = 18$ fa il percorso inverso.*

### Inserimento di un nodo · [[11 . Alberi rosso-neri.pdf#page=21|p. 21]]–[[11 . Alberi rosso-neri.pdf#page=23|23]]

**Strategia.**
- Si inserisce il nodo come in un normale albero di ricerca, con RB-Insert, una versione (leggermente) modificata di Tree-Insert.
- Si colora il nodo di rosso.
- Si invoca una funzione ausiliaria (RB-Insert-Fixup) per ripristinare le proprietà degli alberi rosso-neri.
- Il tempo di esecuzione, vedremo, è $O(\lg n)$.

```
RB-Insert (T,z)
y ← nil[T]
x ← root[T]
while x ≠ nil[T]
    do y ← x
       if key[z] < key[x]
           then x ← left[x]
           else x ← right[x]
p[z] ← y
if y = nil[T]
    then root[T] ← z        // albero vuoto
    else if key[z] < key[y]
        then left[y] ← z
        else right[y] ← z
left[z] ← nil[T]
right[z] ← nil[T]
color[z] ← RED
RB-Insert-Fixup (T,z)
```

Il tempo di esecuzione di RB-Insert è $O(h)$. Nella slide l'albero di esempio ha $z = 19$ da inserire in un albero con radice 15.

**Quali proprietà possono essere invalidate dall'inserimento?**
1. ogni nodo è rosso o nero: vale;
2. la radice è nera: non vale se l'albero era vuoto;
3. ogni foglia NIL è nera: vale;
4. se un nodo è rosso entrambi i figli sono neri: non vale se il padre di $z$ è rosso;
5. stessa black-height: vale.

### RB-Insert-Fixup: invariante · [[11 . Alberi rosso-neri.pdf#page=24|p. 24]]–[[11 . Alberi rosso-neri.pdf#page=26|26]]

RB-Insert-Fixup è costituito da un ciclo `while`, eseguito finché il padre di $z$ resta rosso. È costruito per mantenere il seguente invariante. All'inizio di ogni iterazione:
- a) il nodo $z$ è rosso;
- b) se $p[z]$ è la radice, allora $p[z]$ è nero;
- c) in tutto l'albero c'è al massimo una violazione delle proprietà degli alberi rosso-neri, ed è o di tipo 2 o di tipo 4:
  1. se è di tipo 2, si presenta perché $z$ è la radice ed è rosso;
  2. se è di tipo 4, si presenta perché sia $z$ sia $p[z]$ sono rossi.

**Prima della prima iterazione** ($z$ è il nodo appena inserito):
- a) vera perché il nodo inserito è rosso;
- b) se $p[z]$ è la radice, non è stata modificata da RB-Insert e quindi è rimasta nera;
- c) le proprietà 1, 3 e 5 non vengono violate da RB-Insert: se l'albero era vuoto e il nodo inserito è la nuova radice c'è una violazione di tipo 2 e nessuna di tipo 4 (foglie nere); se l'albero non era vuoto e $z$ viene inserito come figlio di un nodo rosso c'è una violazione di tipo 4 e nessuna di tipo 2.

**Il ciclo termina** quando il padre di $z$ è nero: l'invariante (c.2) garantisce che non ci sono violazioni di tipo 4; in base a c.1) ci potrebbe essere una violazione di tipo 2 dove $z$ è la radice ed è rosso, ed è sufficiente ricolorare di nero la radice. Se $z$ è il primo nodo inserito, il ciclo termina subito: il padre di $z$ è la sentinella, che è un nodo nero.

### Il corpo del ciclo · [[11 . Alberi rosso-neri.pdf#page=27|p. 27]]–[[11 . Alberi rosso-neri.pdf#page=36|36]]

Per preservare l'invariante, se si è entrati nel ciclo:
- il padre di $z$ ($p[z]$) è rosso;
- il nonno di $z$ ($p[p[z]]$) esiste ed è un nodo interno: dato che $p[z]$ è rosso, per b) non può essere la radice, e quindi il padre di $p[z]$ non è la sentinella;
- il nonno di $z$ è un nodo nero: se fosse rosso, con $p[z]$ rosso ci sarebbe una violazione di tipo 4 fra $p[z]$ e $p[p[z]]$, contrariamente a c.2);
- non ci sono violazioni di tipo 2: se ci fosse, $z$ sarebbe la radice e il padre di $z$ (la sentinella) sarebbe nero (assurdo: $p[z]$ è rosso).

Si distingue se il padre di $z$ è figlio di sinistra o di destra del nonno: i due casi sono simmetrici (si scambia left con right). Si considera il caso in cui il padre di $z$ è il figlio di sinistra. Si sa che $z$ è rosso, $p[z]$ è rosso e $p[p[z]]$ è nero; si distingue in base al colore dello zio $y$.

**Caso 1: $y$ è rosso.** $p[z]$ e $y$ diventano neri, $p[p[z]]$ diventa rosso (ricolorazione) e $z \leftarrow p[p[z]]$.

![[11-alberi-rosso-neri-p29-caso-1.png]]

Verifica dell'invariante ($z'$ è il valore di $z$ nella nuova iterazione):
- a) $z'$ è $p[p[z]]$, che è colorato di rosso;
- b) $p[z']$ non è modificato in questa iterazione, quindi se è la radice allora è nero (nessuna violazione di tipo 2 se si entra nel `while`);
- c) non si introducono violazioni di tipo 5 (né 1 e 3): se $z'$ è la radice si è risolta la violazione di tipo 4 e resta una sola violazione di tipo 2 ($z'$ è la radice ed è rosso); se $z'$ non è la radice non si è introdotta una violazione di tipo 2, e può esserci una violazione di tipo 4 fra $z'$ e $p[z']$ se $p[z']$ è rosso.

**Caso 2: $y$ è nero e $z$ è figlio di destra.** $z \leftarrow p[z]$ e Left-Rotate su $z$. Dato che $z$ e $p[z]$ sono rossi, non si viola la proprietà 5 e la black-height. Ci si riconduce al caso 3.

![[11-alberi-rosso-neri-p31-caso-2.png]]

**Caso 3: $y$ è nero e $z$ è figlio di sinistra.** $p[z]$ diventa nero, $p[p[z]]$ rosso e Right-Rotate su $p[p[z]]$; ciò preserva la proprietà 5, e il ciclo termina perché $p[z]$ è nero.

![[11-alberi-rosso-neri-p33-caso-3.png]]

```
RB-Insert-Fixup (T,z)
while color[p[z]] = RED
    do if p[z] = left[p[p[z]]]
          then y ← right[p[p[z]]]            // zio
               if color[y] = RED
                  then color[p[z]] ← BLACK
                       color[y] ← BLACK
                       color[p[p[z]]] ← RED
                       z ← p[p[z]]
                  else if z = right[p[z]]
                        then z ← p[z]
                             Left-Rotate (T,z)
                       color[p[z]] ← BLACK
                       color[p[p[z]]] ← RED
                       Right-Rotate (T,p[p[z]])
          else (stesso codice di then con right e left scambiati)
color[root[T]] ← BLACK
```

Verifica dell'invariante per i casi 2 e 3:
- a) nel caso 2 $z$ diventa $p[z]$, che è rosso, e poi non si modifica più $z$;
- b) il caso 3 colora $p[z]$ di nero;
- c) non si introducono violazioni di tipo 5 (né 1 e 3): $z$ (che è rosso) non è la radice e quindi non viola la proprietà 2; non ci sono altre violazioni di 2 perché l'unico nodo che diventa rosso diventa figlio di un nodo nero (e quindi non può essere la radice); i casi 2 e 3 correggono una violazione di 4 senza introdurne altre.

**Tempo di esecuzione di RB-Insert-Fixup: $O(\lg n)$.**
- Il ciclo si ripete solo se siamo nel caso 1, durante il quale $z$ sale di due livelli.
- Il ciclo viene ripetuto $O(\lg n)$ volte.
- Vengono eseguite al più due rotazioni.
- Il ciclo termina quando si entra nel caso 2 o 3.

### Esempio di inserimento · [[11 . Alberi rosso-neri.pdf#page=37|p. 37]]–[[11 . Alberi rosso-neri.pdf#page=41|41]]

Albero: radice 11 (nero); 2 (rosso) e 14 (nero); 1 e 7 (neri) sotto 2, 15 (rosso) sotto 14; 5 e 8 (rossi) sotto 7. Si inserisce $z = 4$ come figlio sinistro di 5.

- **Caso 1** (violazione della proprietà 4; lo zio di $z$, $y = 8$, è rosso): i nodi sono ricolorati e $z$ diventa il nonno di $z$ (il nodo 7).
- **Caso 2** (violazione della proprietà 4; lo zio $y = 14$ è nero; $z = 7$ è il figlio di destra di $p[z] = 2$): rotazione a sinistra.
- **Caso 3** (violazione della proprietà 4; lo zio $y$ è nero; $z = 2$ è il figlio di sinistra di $p[z] = 7$): rotazione a destra e ricolorazione dei nodi 7 e 11.

![[11-alberi-rosso-neri-p37-inserimento-caso-1-esempio.png]]
![[11-alberi-rosso-neri-p38-inserimento-caso-2-esempio.png]]
![[11-alberi-rosso-neri-p39-inserimento-caso-3-esempio.png]]
![[11-alberi-rosso-neri-p40-inserimento-caso-3-ricolorazione.png]]

A p. 41 è mostrata una schermata del visualizzatore «Red/Black Tree Visualization» (cs.usfca.edu, con le operazioni Insert, Delete, Find).

![[11-alberi-rosso-neri-p41-visualizzatore.png]]

### Eliminazione di un elemento · [[11 . Alberi rosso-neri.pdf#page=42|p. 42]]–[[11 . Alberi rosso-neri.pdf#page=48|48]]

La cancellazione si basa sull'algoritmo Tree-Delete dei normali BST, con alcune modifiche. Come nell'inserimento, anche nella cancellazione può essere necessario ripristinare le proprietà rosso-nere:
- se il nodo fisicamente rimosso è rosso, le proprietà rosso-nere restano valide;
- se il nodo fisicamente rimosso è nero, si invoca RB-Delete-Fixup, che ripristina le proprietà attraverso eventuali ricolorazioni e rotazioni.

La cancellazione segue inizialmente le stesse regole di un BST: si distinguono i casi in cui il nodo da eliminare ha **zero, uno o due figli**. Le proprietà degli alberi rosso-neri permettono però alcune osservazioni:
- un nodo rosso può essere una foglia oppure avere due figli, necessariamente neri;
- non può avere un solo figlio, altrimenti sarebbe violata la proprietà 5 (black-height);
- se il nodo da eliminare ha due figli, viene individuato il suo successore, che ha al massimo un figlio.

Pertanto il nodo fisicamente rimosso ha sempre al massimo un figlio. I casi effettivi da gestire sono tre:
1. si elimina una **foglia rossa**: l'albero resta rosso-nero (non cambia la black-height, non si creano nodi rossi consecutivi, la radice resta nera);
2. si elimina un **nodo nero con un unico figlio rosso**: il figlio prende il suo posto e viene colorato di nero; le proprietà sono preservate;
3. si elimina una **foglia nera**: la black-height diminuisce lungo alcuni cammini, occorre intervenire con RB-Delete-Fixup per ripristinare le proprietà.

![[11-alberi-rosso-neri-p45-cancellazione-foglia.png]]
*Caso I — eliminare una foglia: albero rosso-nero iniziale, si sceglie $z = 19$.*

![[11-alberi-rosso-neri-p46-cancellazione-un-figlio.png]]
*Caso II — un solo figlio: si sceglie $z = 20$ (nero).*

![[11-alberi-rosso-neri-p47-cancellazione-due-figli.png]]
*Caso III — due figli: si sceglie $z = 18$.*

RB-Delete-Fixup è diverso da RB-Insert-Fixup: RB-Insert-Fixup corregge principalmente la presenza di due nodi rossi consecutivi, RB-Delete-Fixup corregge principalmente lo squilibrio della black-height provocato dall'eliminazione di un nodo nero. Entrambi utilizzano rotazioni e ricolorazioni, ma gestiscono situazioni differenti.

**Complessità.** La ricerca e l'eliminazione strutturale richiedono $O(h)$; anche RB-Delete-Fixup richiede $O(h)$ nel caso peggiore; poiché un albero rosso-nero ha altezza $h = O(\log n)$, l'intera cancellazione richiede $O(\log n)$.

*Approfondimenti nel wiki: [[albero-rosso-nero]], [[left-rotate]], [[rb-insert]], [[rb-delete]]*

## Lezione 12 — Alberi auto-aggiustanti

*Fonte: 12 - Alberi auto-aggiustanti.pdf (16 pagine di slide).*

### Alberi auto-aggiustanti (splay trees) · [[12 - Alberi auto-aggiustanti.pdf#page=2|p. 2]], [[12 - Alberi auto-aggiustanti.pdf#page=1|p. 1]]

- Gli **alberi auto-aggiustanti** (splay trees) sono alberi binari di ricerca che non impongono ulteriori vincoli sulla disposizione degli elementi.
- L'idea è che ogni volta che si accede a un elemento dell'albero, l'albero viene riaggiustato in modo che tale elemento venga posto nella radice.
- Utilizzando delle rotazioni per riaggiustare l'albero, si ottengono **tempi di esecuzione ammortizzati** di tipo logaritmico su una sequenza di $n$ operazioni.
- Vantaggio pratico: gli elementi cui si accede più di frequente si trovano nelle vicinanze della radice e quindi si accede più velocemente ad essi.
- È una struttura per insiemi ordinati (come un BST) che si **adatta automaticamente al pattern di accesso**, con **costo ammortizzato** $O(\log n)$ per operazione, senza memorizzare informazioni di bilanciamento (ad esempio i colori).

### L'operazione splay · [[12 - Alberi auto-aggiustanti.pdf#page=3|p. 3]]–[[12 - Alberi auto-aggiustanti.pdf#page=5|5]]

L'operazione splay su un nodo $x$ consiste nell'effettuare una **serie di rotazioni** che portano $x$ nella radice dell'albero.

- **Caso I: $x$ è figlio della radice.** Rotazione sul padre di $x$ (sulla radice): Left-Rotate $(T,y)$.

![[12-alberi-auto-aggiustanti-p3-splay-caso-1.png]]

- **Caso II: $x$ ha un nonno e sia $x$ sia il padre di $x$ sono figli di sinistra (o di destra) del proprio genitore.** Rotazione sul nonno di $x$ (Right-Rotate $(T,z)$), poi rotazione sul padre di $x$ (Right-Rotate $(T,y)$).

![[12-alberi-auto-aggiustanti-p4-splay-caso-2.png]]

- **Caso III: $x$ ha un nonno, $x$ è figlio di sinistra (destra) e il padre di $x$ è figlio di destra (sinistra).** Rotazione sul padre di $x$ (Right-Rotate $(T,y)$), poi rotazione sul nuovo padre di $x$ (era il nonno di $x$: Left-Rotate $(T,z)$).

![[12-alberi-auto-aggiustanti-p5-splay-caso-3.png]]

### Ricerca, inserimento ed eliminazione · [[12 - Alberi auto-aggiustanti.pdf#page=6|p. 6]]–[[12 - Alberi auto-aggiustanti.pdf#page=9|9]]

**Ricerca.** Dopo aver cercato una chiave, si esegue un'operazione splay sul nodo che contiene la chiave o sulla foglia su cui la ricerca è terminata. Se l'albero è vuoto non si fa nulla.

```
Splay-Tree-Search (T,k)
x ← root[T]
while x ≠ NIL and key[x] ≠ k
    do y ← x
       if k < key[x]
           then x ← left[x]
           else x ← right[x]
if x ≠ NIL
    then Splay (T,x)
    else if root[T] ≠ NIL
        then Splay (T,y)
return x
```

**Inserimento.** Dopo aver inserito un elemento, si esegue un'operazione splay sul nodo che contiene il nuovo elemento inserito. Nell'esempio l'albero (radice 15; 6 e 18; 3, 7, 17 e 20; 2, 4 e 13) riceve il nodo 19.

```
Splay-Tree-Insert (T,z)
Tree-Insert (z)
Splay (T,z)
```

**Eliminazione.** Dopo aver eliminato un nodo $z$, si esegue un'operazione splay sul nodo che era il padre di $z$ prima dell'eliminazione. Se il padre di $z$ è NIL ($z$ è la radice) non si fa nulla.

```
Splay-Tree-Delete (T,z)
Tree-Delete (z)
if p[z] ≠ NIL
    then Splay (T,p[z])
```

**Costo?** Per calcolare il costo reale delle operazioni si usa un approccio noto come analisi ammortizzata (lo vedremo nelle prossime lezioni).

### Alberi rosso-neri contro splay · [[12 - Alberi auto-aggiustanti.pdf#page=10|p. 10]]–[[12 - Alberi auto-aggiustanti.pdf#page=12|12]]

La differenza non è l'ordinamento BST: è il modo in cui si ottengono buone prestazioni.
- **Albero rosso-nero:** mantiene un'altezza logaritmica anche se cambiano le chiavi cercate.
- **Splay tree:** si riorganizza a ogni accesso, portando il nodo cercato alla radice.
- Idea chiave: lo splay sfrutta la storia degli accessi, non impone un bilanciamento permanente.

![[12-alberi-auto-aggiustanti-p10-rosso-nero-vs-splay.png]]

**Esempio sul costo.** Stesso albero della lezione: 17 viene cercato e portato in radice. Prima, 17 è interno all'albero; dopo Splay(17), 17 è la radice (zig-zag: due rotazioni che conservano l'ordinamento delle chiavi). Se 17 viene cercato di nuovo (senza accessi intermedi): $O(1)$.

![[12-alberi-auto-aggiustanti-p11-splay-17-esempio.png]]

### Working set (cenni) · [[12 - Alberi auto-aggiustanti.pdf#page=13|p. 13]]

La struttura si adatta alla **località temporale**: una chiave usata di recente può costare meno da ritrovare, anche quando l'albero contiene molte chiavi. Nella sequenza di accessi A → B → C → A → A → D → A, prima dell'ultimo A è stato consultato un solo elemento distinto: D. Con $t_i$ = numero di chiavi distinte consultate dall'accesso precedente alla stessa chiave, il contributo logaritmico nel limite ammortizzato è $O(1 + \log(t_i + 1))$. È un limite per sequenze, **non** il tempo effettivo garantito per ogni singolo accesso.

### Impatto della splay · [[12 - Alberi auto-aggiustanti.pdf#page=14|p. 14]]

La forma dell'albero cambia, ma l'ordine delle chiavi resta identico. Una rotazione a sinistra su $x$ (figli $A$ e $y$; $y$ ha figli $B$ e $C$) porta $y$ in alto, con $x$ a sinistra (figli $A$ e $B$) e $C$ a destra. $B$ cambia padre ma contiene sempre chiavi fra $x$ e $y$:

$$
A < x < B < y < C
$$

La visita in ordine è invariata: per questo ogni rotazione conserva la proprietà BST.

![[12-alberi-auto-aggiustanti-p14-impatto-splay.png]]

### Splay tree contro albero rosso-nero · [[12 - Alberi auto-aggiustanti.pdf#page=15|p. 15]], [[12 - Alberi auto-aggiustanti.pdf#page=16|16]]

Non esiste un vincitore assoluto: dipende dalle richieste dell'applicazione.
- **Splay tree:** accessi ripetuti alle stesse chiavi; accessi con forte località temporale; nessun colore o bilanciamento da memorizzare.
- **Albero rosso-nero:** serve un limite per ogni ricerca; latenza prevedibile $O(\log n)$; le ricerche non devono modificare l'albero.
- Rosso-nero: bilanciamento garantito. Splay: riorganizzazione adattiva alla storia degli accessi.

| Caratteristica | BST ordinario | Albero rosso-nero | Splay tree |
|---|---|---|---|
| Rispetta l'ordinamento BST | Sì | Sì | Sì |
| Bilanciamento garantito | No | Sì | No |
| Si riorganizza dopo le ricerche | No | No | Sì |
| Altezza nel caso peggiore | $O(n)$ | $O(\log n)$ | $O(n)$ |
| Ricerca: costo ammortizzato | $O(n)$ | $O(\log n)$ | $O(\log n)$ |

*Approfondimenti nel wiki: [[splay-tree]], [[splay]], [[splay-tree-operazioni]]*

## Lezione 13 — Algoritmi di visita di un grafo

*Fonte: 13 - Algoritmi di visita di un grafo.pdf (53 pagine: slide, con note a mano alle p. 38 e 40; le pp. 44–53 sono slide in inglese di S. Skiena).*

### Grafi e rappresentazioni · [[13 - Algoritmi di visita di un grafo.pdf#page=2|p. 2]]–[[13 - Algoritmi di visita di un grafo.pdf#page=6|6]], [[13 - Algoritmi di visita di un grafo.pdf#page=1|p. 1]]

Un grafo consiste di un insieme di nodi $V$ connessi mediante un insieme di archi $E$, direzionali e non direzionali. Due rappresentazioni:
- **liste di adiacenza**, tipicamente preferite per grafi sparsi ($\lvert E \rvert \ll \lvert V \rvert^2$);
- **matrice di adiacenza**, tipicamente preferita per grafi densi o quando serve sapere velocemente se due nodi sono connessi.

Entrambe sono utilizzabili sia per grafi direzionali sia non direzionali.

**Liste di adiacenza.** Un array $Adj$ di $\lvert V \rvert$ liste, una per ciascun vertice; ogni lista $Adj[u]$ contiene i vertici $v$ tali che $(u, v) \in E$.

![[13-visite-grafi-p3-liste-di-adiacenza.png]]

- La somma delle lunghezze di tutte le liste è $\lvert E \rvert$ se $G$ è direzionale, $2\lvert E \rvert$ se $G$ è non direzionale; la memoria richiesta è in ogni caso $\Theta(V + E)$.
- Le liste possono rappresentare grafi pesati: a ogni link è associato un peso dato dalla funzione $w: E \to \mathbb{R}$; il peso $w(u, v)$ del link $(u, v)$ si può memorizzare insieme al vertice $v$ nella lista di adiacenza di $u$.
- Un potenziale svantaggio è che, per determinare se un arco $(u, v)$ è presente, bisogna effettuare una ricerca nella lista di adiacenza di $u$.

**Matrice di adiacenza.** Una matrice $A$ di dimensione $\lvert V \rvert \times \lvert V \rvert$, con $a_{ij} = 1$ se $(i, j) \in E$, 0 altrimenti.

![[13-visite-grafi-p5-matrice-di-adiacenza.png]]

- Richiede $\Theta(V^2)$ memoria, indipendentemente dal numero di archi.
- Dato che in un grafo non direzionale $(u, v)$ e $(v, u)$ rappresentano lo stesso arco, la matrice è simmetrica rispetto alla diagonale principale, $A = A^T$: si può dimezzare il consumo di memoria.
- Può rappresentare grafi pesati: $a_{ij}$ vale il peso di $(i, j)$ se l'arco esiste, altrimenti vale NIL, 0 (a seconda dei casi).
- Si preferisce in genere per grafi di piccole dimensioni e quando i grafi non sono pesati (0 o 1 consuma 1 bit).

### Visita di un grafo · [[13 - Algoritmi di visita di un grafo.pdf#page=7|p. 7]]

Una volta rappresentato un grafo, vogliamo esplorarne sistematicamente i vertici e gli archi, a partire da un nodo sorgente, evitando di visitare più volte lo stesso vertice. Due strategie fondamentali:
- **visita in ampiezza** (BFS): esplora prima i vertici più vicini alla sorgente, procedendo per livelli;
- **visita in profondità** (DFS): esplora un cammino il più possibile in profondità, tornando indietro quando non può proseguire.

Le visite permettono anche di risolvere problemi più complessi, come l'**ordinamento topologico**, che dispone i vertici di un grafo orientato aciclico (DAG) rispettando le dipendenze tra essi.

### Visita in ampiezza · [[13 - Algoritmi di visita di un grafo.pdf#page=9|p. 9]]–[[13 - Algoritmi di visita di un grafo.pdf#page=12|12]], [[13 - Algoritmi di visita di un grafo.pdf#page=8|p. 8]]

La visita in ampiezza (BFS, *Breadth First Search*) è un semplice algoritmo per «visitare» i nodi di un grafo. Importanti algoritmi si basano su questo approccio: l'algoritmo di Dijkstra per lo shortest path e l'algoritmo di Prim per il minimum spanning tree.
- A partire da un nodo sorgente $s$, BFS visita tutti i nodi adiacenti di un nodo e poi procede a visitare allo stesso modo gli adiacenti.
- Tutti i nodi che distano $k$ dalla sorgente vengono visitati prima del primo nodo che dista $k+1$.
- BFS produce un albero con radice in $s$ che contiene tutti i nodi raggiungibili da $s$.
- Il percorso da $s$ a $v$ nell'albero è il più breve da $s$ a $v$ nel grafo.

BFS opera su grafi direzionali e non. Per tenere traccia dei nodi esplorati utilizza i colori: **bianco** se non è ancora stato visitato; **grigio** se è stato visitato ma non tutti i suoi vicini sono stati visitati; **nero** se è stato visitato insieme a tutti i suoi vicini. Se il nodo $v$ viene visitato in quanto vicino di $u$, allora $u$ è il predecessore di $v$; ogni nodo viene visitato al più una volta e quindi ha al più un predecessore.

![[13-visite-grafi-p11-bfs-grafo.png]]
*Grafo non orientato (vertici $r, s, t, u, v, w, x, y$) per la visita in ampiezza; a destra l'albero BFS, con i livelli $d = 0, 1, 2, 3$, ancora vuoto.*

L'albero che si ottiene dipende dall'ordine con cui si visitano i vicini, ma la lunghezza dei percorsi minimi non cambia.

```
BFS (G,s)
for each vertex u ∈ V[G] - {s}
    do color[u] ← WHITE
       d[u] ← ∞
       π[u] ← NIL
color[s] ← GRAY
d[s] ← 0
π[s] ← NIL
Q ← Ø
Enqueue (Q,s)
while Q ≠ Ø
    do u ← Dequeue (Q)
       for each v ∈ Adj[u]
           do if color[v] = WHITE
               then color[v] ← GRAY
                    d[v] ← d[u] + 1
                    π[v] ← u
                    Enqueue (Q,v)
       color[u] ← BLACK
```

Assume una rappresentazione mediante liste di adiacenza. Il predecessore $\pi$ di un nodo è NIL se il nodo è la sorgente o non è stato raggiunto (ancora). **Invariante:** all'inizio di ogni iterazione del ciclo `while`, $Q$ contiene tutti i nodi grigi; è vero prima della prima iterazione, e una iterazione conserva questa proprietà.

### Visita in ampiezza: costo · [[13 - Algoritmi di visita di un grafo.pdf#page=13|p. 13]], [[13 - Algoritmi di visita di un grafo.pdf#page=14|14]]

Si effettua un'**analisi aggregata** per determinare il tempo di esecuzione.
- L'overhead legato all'inizializzazione è $O(V)$.
- Il tempo legato alle operazioni di accodamento e deaccodamento è $O(V)$: `Enqueue` e `Dequeue` richiedono $O(1)$; ogni nodo viene accodato al più una volta (un nodo viene accodato solo se è bianco e, quando viene accodato, viene colorato di grigio; un nodo non viene mai ricolorato bianco); un nodo in coda può essere deaccodato al più una volta.
- Il tempo legato all'analisi delle liste di adiacenza è $O(E)$: la lista di adiacenza di un nodo è analizzata solo quando il nodo viene deaccodato; la somma delle lunghezze di tutte le liste è $\Theta(E)$.

Il tempo di esecuzione di BFS è $O(V + E)$.

### Visita in ampiezza: percorso minimo · [[13 - Algoritmi di visita di un grafo.pdf#page=15|p. 15]]–[[13 - Algoritmi di visita di un grafo.pdf#page=19|19]]

Si definisce la **distanza minima** $\delta(s, v)$ tra $s$ e $v$ come il numero minimo di archi di qualunque percorso tra $s$ e $v$; se non c'è un percorso, $\delta(s, v) = \infty$. Un percorso tra $s$ e $v$ di lunghezza minima è uno *shortest path* da $s$ a $v$.

**Lemma 1.** Per ogni arco $(u, v) \in E$ si ha $\delta(s, v) \le \delta(s, u) + 1$. Se $u$ è raggiungibile da $s$, lo è anche $v$: lo shortest path da $s$ a $v$ non può essere più lungo dello shortest path da $s$ a $u$ più l'arco $(u, v)$. Se $u$ non è raggiungibile, $\delta(s, u) = \infty$ e la tesi è vera.

**Lemma 2.** Dopo aver eseguito BFS su $G$ a partire da $s$, per ogni vertice $v$ si ha $d[v] \ge \delta(s, v)$. Per induzione sul numero di operazioni di Enqueue.
- *Caso base:* dopo che $s$ è stato accodato, la tesi è vera per $s$ ($d[s] = \delta(s, s) = 0$) e per gli altri nodi ($d[v] = \infty \ge \delta(s, v)$).
- *Passo induttivo:* sia $v$ un vertice bianco scoperto durante la ricerca dei vicini di $u$. L'ipotesi induttiva è $d[u] \ge \delta(s, u)$. La distanza assegnata a $v$ è $d[v] = d[u] + 1 \ge \delta(s, u) + 1 \ge \delta(s, v)$ (lemma 1). Il vertice $v$ viene colorato di grigio e quindi non viene più riaccodato, per cui la sua distanza non cambia più.

**Lemma 3.** Durante l'esecuzione di BFS, se la coda $Q$ contiene i vertici $\langle v_1, v_2, \dots, v_r \rangle$ ($v_1$ testa, $v_r$ coda), allora per ogni $i = 1, \dots, r$ vale $d[v_i] \le d[v_{i+1}]$ e $d[v_r] \le d[v_1] + 1$. Per induzione sul numero di operazioni sulla coda.
- *Caso base:* inizialmente la coda contiene $s$ e la tesi vale.
- *Passo induttivo 1) si estrae la testa $v_1$:* la nuova testa diventa $v_2$; se la coda è vuota la tesi è banale. L'ipotesi induttiva è $d[v_1] \le d[v_2]$ e $d[v_r] \le d[v_1] + 1 \Rightarrow d[v_r] \le d[v_2] + 1$ (vera anche per $v_2$).
- *Passo induttivo 2) si accoda un nodo:* questo diventa $v_{r+1}$ e il nodo $u$ a partire dal quale è stato scoperto è già stato estratto. Per ipotesi $d[u] \le d[v_1] \Rightarrow d[v_{r+1}] = d[u] + 1 \le d[v_1] + 1$ e $d[v_r] \le d[u] + 1 = d[v_{r+1}]$; le altre relazioni restano immutate.

**Corollario 1.** Dal lemma 3 e dal fatto che la distanza di un nodo è assegnata al più una volta: se il vertice $v_i$ è accodato prima di $v_j$, allora $d[v_i] \le d[v_j]$.

**Teorema (completezza).** BFS scopre tutti i nodi raggiungibili dalla sorgente $s$ e al termine si ha $d[v] = \delta(s, v)$ per tutti i vertici $v$. Per ogni vertice $v$ raggiungibile da $s$, uno shortest path da $s$ a $v$ è uno shortest path da $s$ a $\pi[v]$ seguito dall'arco $(\pi[v], v)$.
- Si assume per assurdo che qualche vertice riceva una distanza diversa da quella minima.
- Tra tali vertici, sia $v$ quello con la più piccola distanza minima (chiaramente $v$ non può essere $s$).
- Per il lemma 2, $d[v] \ge \delta(s, v)$, quindi $d[v] > \delta(s, v)$ e $v$ deve essere raggiungibile da $s$ (altrimenti $\delta(s, v) = \infty \ge d[v]$).
- Sia $u$ il nodo che precede $v$ lungo uno shortest path da $s$ a $v$, quindi $\delta(s, v) = \delta(s, u) + 1$.

(La slide si interrompe a questo punto.)

### Visita in ampiezza: albero di visita · [[13 - Algoritmi di visita di un grafo.pdf#page=20|p. 20]], [[13 - Algoritmi di visita di un grafo.pdf#page=21|21]]

BFS costruisce un albero, detto *breadth-first tree*. Formalmente si definisce il **predecessor subgraph** di $G$: $G_\pi = (V_\pi, E_\pi)$ con $V_\pi = \{v \in V : \pi[v] \ne \text{NIL}\} \cup \{s\}$ e $E_\pi = \{(\pi[v], v) : v \in V_\pi - \{s\}\}$ (tree edges). Un predecessor subgraph è un albero perché, dalla definizione di $E_\pi$, $\lvert E_\pi \rvert = \lvert V_\pi \rvert - 1$, condizione necessaria e sufficiente per un albero. È un breadth-first tree se $V_\pi$ consiste dei vertici raggiungibili da $s$ e, per ogni $v \in V_\pi$, esiste un unico percorso semplice da $s$ a $v$ in $G_\pi$ che è anche lo shortest path da $s$ a $v$ in $G$.

**Lemma 4.** Il predecessor subgraph restituito da BFS è un breadth-first tree. BFS pone $\pi[v] = u$ se e solo se $(u, v) \in E$ e $v$ è raggiungibile da $s$; quindi $V_\pi$ consiste dei vertici raggiungibili da $s$. Dato che il predecessor subgraph è un albero, contiene un unico percorso da $s$ a ciascun vertice; applicando il teorema precedente, si conclude che ogni percorso è uno shortest path.

### Visita in ampiezza: stampa · [[13 - Algoritmi di visita di un grafo.pdf#page=22|p. 22]], [[13 - Algoritmi di visita di un grafo.pdf#page=23|23]]

Stampa i vertici lungo uno shortest path da $s$ a $y$, assumendo di aver eseguito BFS in precedenza. Il tempo di esecuzione è lineare nel numero di vertici sul percorso.

```
Print-Path (G,s,v)
if v = s
    then print s
    else if π[v] = NIL
        then print "no path from s to v exists"
        else Print-Path (G,s,π[v])
             print v
```

### Visita in profondità · [[13 - Algoritmi di visita di un grafo.pdf#page=25|p. 25]]–[[13 - Algoritmi di visita di un grafo.pdf#page=28|28]], [[13 - Algoritmi di visita di un grafo.pdf#page=24|p. 24]]

La **depth-first search** (DFS) esplora i vicini del nodo scoperto più di recente che ha ancora vicini non esplorati: la visita procede «in profondità». Se ci sono nodi non esplorati, la ricerca riparte da uno di essi; tutti i vertici sono esplorati. DFS tiene traccia dei predecessori di un nodo (come BFS). Il predecessor subgraph può essere composto da più alberi, per questo è definito in maniera leggermente diversa: $G_\pi = (V, E_\pi)$ con $E_\pi = \{(\pi[v], v) : v \in V \text{ e } \pi[v] \ne \text{NIL}\}$ (tree edges). Il predecessor subgraph forma una **depth-first forest** composta di diversi **depth-first tree**.

Come in BFS, i nodi sono colorati di bianco, grigio e nero: ciò assicura che ogni vertice finisca in un solo depth-first tree e quindi che gli alberi siano disgiunti. DFS marca ciascun nodo con due **timestamp**:
- $d[v]$ segna l'istante di tempo in cui $v$ è scoperto (e colorato di grigio);
- $f[v]$ segna l'istante di tempo in cui termina la ricerca dei vicini di $v$ (che viene colorato di nero).

I timestamp sono interi compresi tra 1 e $2\lvert V \rvert$; per ogni nodo c'è un istante di scoperta e uno di completamento; per ogni vertice $u$, $d[u] < f[u]$.

![[13-visite-grafi-p28-dfs-codice.png]]
*Esempio di DFS con i tempi $d/f$ (archi dell'albero in blu) e pseudocodice. Anche per DFS i risultati della ricerca variano a seconda dell'ordine con cui si esaminano i nodi.*

```
DFS (G)
for each vertex u ∈ V[G]
    do color[u] ← WHITE
       π[u] ← NIL
time ← 0
for each vertex u ∈ V[G]
    do if color[u] = WHITE
        then DFS-Visit (u)

DFS-Visit (u)
color[u] ← GRAY
time ← time + 1
d[u] ← time
for each v ∈ Adj[u]
    do if color[v] = WHITE
        then π[v] ← u
             DFS-Visit (v)
color[u] ← BLACK
f[u] ← time ← time + 1
```

### Visita in profondità: costo · [[13 - Algoritmi di visita di un grafo.pdf#page=29|p. 29]]

- I cicli `for` di DFS impiegano $\Theta(V)$, esclusa la chiamata a DFS-Visit.
- DFS-Visit viene chiamata una volta per ciascun nodo: è chiamata solo su vertici bianchi e la prima cosa che fa è colorare il vertice di grigio.
- Il tempo impiegato dal ciclo `for` di DFS-Visit su tutte le invocazioni è $\Theta(E)$.
- Il tempo complessivo è $O(V + E)$.

### Struttura a parentesi · [[13 - Algoritmi di visita di un grafo.pdf#page=30|p. 30]]–[[13 - Algoritmi di visita di un grafo.pdf#page=32|32]]

Una proprietà della DFS è che i tempi di scoperta e di terminazione dei nodi hanno una **struttura a parentesi**: scrivendo $d[u]$ come «$(u$» e $f[u]$ come «$u)$» si ottiene un'espressione corretta.

![[13-visite-grafi-p30-dfs-parentesi.png]]

**Teorema 1.** Per ogni coppia di nodi $u$ e $v$ si può verificare solo una delle seguenti condizioni:
- gli intervalli $[d[u], f[u]]$ e $[d[v], f[v]]$ sono disgiunti e $u$ non è discendente di $v$ né $v$ è discendente di $u$ nella depth-first forest;
- l'intervallo $[d[u], f[u]]$ è contenuto interamente nell'intervallo $[d[v], f[v]]$ e $u$ è un discendente di $v$ in un depth-first tree;
- l'intervallo $[d[v], f[v]]$ è contenuto interamente nell'intervallo $[d[u], f[u]]$ e $v$ è un discendente di $u$ in un depth-first tree.

**Corollario 1.** Un vertice $v$ è un discendente di $u$ nella depth-first forest se e solo se $d[u] < d[v] < f[v] < f[u]$.

*Dimostrazione.* Si supponga $d[u] < d[v]$. Quando $v$ viene scoperto, $u$ o è ancora grigio o è nero.
- **Caso 1) $d[v] < f[u]$:** $v$ viene scoperto quando $u$ è ancora grigio, quindi $v$ è un discendente di $u$. I vicini di $v$ saranno esplorati tutti (ovvero $v$ sarà colorato di nero) prima che siano esplorati tutti i vicini di $u$, cioè $f[v] < f[u]$; quindi $[d[v], f[v]]$ è contenuto interamente in $[d[u], f[u]]$.
- **Caso 2) $f[u] < d[v]$:** ne segue $d[u] < f[u] < d[v] < f[v]$, cioè gli intervalli sono disgiunti. Dato che $u$ è nero quando $v$ viene scoperto, nessun vertice è un discendente dell'altro.

### Teorema del cammino bianco · [[13 - Algoritmi di visita di un grafo.pdf#page=33|p. 33]], [[13 - Algoritmi di visita di un grafo.pdf#page=34|34]]

**Teorema 2.** In una depth-first forest, un vertice $v$ è un discendente di $u$ se e solo se, al tempo $d[u]$, $v$ può essere raggiunto da $u$ attraverso un percorso che consiste di soli nodi bianchi.

*Dimostrazione.* ($\Rightarrow$) $v$ è un discendente di $u$ in un depth-first tree; sia $w$ un qualunque nodo lungo il percorso da $u$ a $v$ nel depth-first tree: $w$ è un discendente di $u$ e quindi (corollario 1) $d[u] < d[w]$, quindi $w$ è bianco quando si scopre $u$. Al tempo $d[u]$ c'è dunque un percorso da $u$ a $v$ che consiste di soli nodi bianchi (anche $v$ è bianco).

($\Leftarrow$) Si assume che tutti i nodi lungo tale percorso, eccetto $v$, diventino discendenti di $u$. Altrimenti, sia $v$ il nodo più vicino a $u$ che non diventa discendente di $u$. Sia $w$ il predecessore di $v$ lungo tale percorso ($w$ diventa un discendente di $u$), quindi $f[w] \le f[u]$ per il corollario 1 (l'uguale c'è perché $w$ potrebbe essere $u$). $v$ viene scoperto dopo che viene scoperto $u$ ma prima che $w$ sia finito ($v$ è un vicino di $w$): $d[u] < d[v] < f[w] \le f[u]$. Per il teorema 1, $[d[v], f[v]]$ è contenuto in $[d[u], f[u]]$ e quindi (corollario 1) $v$ deve essere un discendente di $u$.

### Classificazione degli archi · [[13 - Algoritmi di visita di un grafo.pdf#page=35|p. 35]]–[[13 - Algoritmi di visita di un grafo.pdf#page=37|37]]

Una DFS partiziona gli archi di un grafo in 4 insiemi:
- **tree edges**: gli archi in una depth-first forest; $(u, v)$ è un tree edge se $v$ è scoperto esplorando i vicini di $u$;
- **back edges**: archi $(u, v)$ con $v$ antenato di $u$ in un depth-first tree; i self-loop sono considerati back edges;
- **forward edges**: archi $(u, v)$ con $u$ antenato di $v$ in un depth-first tree;
- **cross edges**: tutti gli altri archi, tra nodi di diversi depth-first tree o dello stesso depth-first tree ma che non sono l'uno il discendente dell'altro.

Per i grafi non direzionali ci può essere ambiguità tra $(u, v)$ e $(v, u)$, che sono lo stesso arco: un arco viene classificato sulla base della «direzione» che viene incontrata prima.

DFS può classificare gli archi man mano che li incontra: un arco $(u, v)$ può essere classificato sulla base del **colore di $v$** nel momento in cui l'arco è esplorato per la prima volta.
- Se $v$ è bianco, $(u, v)$ è un tree edge.
- Se $v$ è grigio, $(u, v)$ è un back edge.
- Se $v$ è nero ($f[v] < f[u]$), $(u, v)$ può essere un forward edge o un cross edge: se $d[u] < d[v]$ è un forward edge ($d[u] < d[v] < f[v] < f[u]$); se $d[u] > d[v]$ è un cross edge.

In una DFS su un grafo non direzionale, **ogni arco è o un tree edge o un back edge**. Si assume che $u$ venga scoperto prima di $v$; dato che $v$ è un vicino di $u$, $v$ deve essere scoperto e completato prima che sia completato $u$. Se $(u, v)$ viene esplorato per primo nella direzione $u \to v$, allora è un tree edge; se viene esplorato per primo nella direzione $v \to u$, allora è un back edge.

![[13-visite-grafi-p37-dfs-grafo-non-orientato.png]]

### Ordinamento topologico · [[13 - Algoritmi di visita di un grafo.pdf#page=38|p. 38]]–[[13 - Algoritmi di visita di un grafo.pdf#page=43|43]]

Nota a mano di p. 38 (lettura incerta): la disposizione deve rappresentare la proprietà del fenomeno, il posizionamento rispetta il fenomeno sottostante; ordine topologico $v_1, v_2, v_3, v_4, v_5, v_6, v_7$.

![[13-visite-grafi-p38-ordinamento-topologico.png]]

DFS può essere usato per realizzare un ordinamento topologico di un *directed acyclic graph* (DAG). Un ordinamento topologico di un DAG determina un ordine dei nodi tale che, se esiste un arco $u \to v$, allora $u$ precede $v$. Se il grafo non è aciclico, non è possibile un tale ordinamento. Tale ordinamento è utile, ad esempio, quando gli archi indicano una relazione di precedenza.

```
Topological-Sort (G)
Call DFS(G) to compute finishing times f[v] for each vertex v
As each vertex is finished, insert it onto the front of a linked list
return the linked list of vertices
```

Nota a mano di p. 40 (lettura incerta): facciamo ordinamento *del* grafo e non *sul* grafo; fin ora abbiamo sempre visto ordinamenti sul grafo e non del grafo. Il tempo di esecuzione è $\Theta(V + E)$: DFS richiede $\Theta(V + E)$ e l'inserimento di $\lvert V \rvert$ vertici nella lista richiede $O(V)$.

![[13-visite-grafi-p40-topological-sort-codice.png]]
*DAG con vertici $a, \dots, j$ e ordinamento $a, b, e, f, d, c, g, j, h, i$.*

**Lemma 1.** Un grafo direzionale è aciclico se e solo se una DFS su $G$ non restituisce back edges.
- Se $G$ restituisce un back edge, allora il grafo direzionale è ciclico: se $(u, v)$ è un back edge, $v$ è un antenato di $u$ in un depth-first tree, quindi c'è un percorso da $v$ a $u$ e il link $u \to v$ completa il ciclo.
- Se il grafo contiene un ciclo $c$, allora la DFS restituisce (almeno) un back edge: sia $v$ il primo vertice di $c$ scoperto durante la DFS e $u \to v$ l'arco che precede $v$ nel ciclo. Al tempo $d[v]$, i vertici di $c$ formano un percorso di nodi bianchi da $v$ a $u$, quindi $u$ diventerà un discendente di $v$ e $u \to v$ un back edge.

**Teorema 1.** Topological-Sort (G) produce un ordinamento topologico di un DAG $G$. Occorre mostrare che, per ogni coppia di vertici $u$ e $v$, se c'è un arco $u \to v$ allora $f[v] < f[u]$. Si consideri un arco $u \to v$ che viene esplorato da DFS:
- $v$ non può essere grigio, altrimenti $u \to v$ sarebbe un back edge, il che contraddice il lemma 1;
- se $v$ è bianco, $v$ diventa un discendente di $u$ e quindi $f[v] < f[u]$;
- se $v$ è nero, l'esplorazione di $v$ è già finita e quindi, dato che si sta ancora esplorando $u$, $f[v] < f[u]$.

### Percorsi minimi · [[13 - Algoritmi di visita di un grafo.pdf#page=44|p. 44]]–[[13 - Algoritmi di visita di un grafo.pdf#page=53|53]]

*(Slide in inglese di S. Skiena, «Lecture 14: Shortest Paths».)*

**Applicazioni degli shortest path.** Trovare il cammino minimo tra due nodi si presenta in molte applicazioni: **problemi di trasporto** (il modo più economico di viaggiare tra due luoghi), **pianificazione del movimento** (il modo più naturale per un personaggio dei cartoni di muoversi in un ambiente simulato), **problemi di comunicazione** (quanto tempo impiega un messaggio per andare da un posto a un altro; quali due posti sono i più lontani, cioè qual è il **diametro** della rete).

**Grafi non pesati.** Lo shortest path usa il numero minimo di archi e si trova in tempo $O(n + m)$ con la ricerca in ampiezza. In un grafo pesato il peso di un percorso fra due vertici è la somma dei pesi degli archi sul percorso. La BFS non funziona sui grafi pesati perché visitare più archi può costare meno di visitarne meno, ad esempio $1+1+1+1+1+1+1 < 10$. Ci può essere un numero esponenziale di shortest path tra due nodi: non si possono riportare efficientemente *tutti* gli shortest path.

**Pesi negativi.** I cicli di costo negativo rendono privo di senso il problema di trovare lo shortest path, perché si può sempre ripercorrere il ciclo per ridurre il costo del percorso. Si assume quindi che tutti i pesi degli archi siano positivi; altri algoritmi trattano correttamente gli archi di costo negativo.

**Algoritmo di Dijkstra.** Il principio è che se $(s, \dots, x, \dots, t)$ è lo shortest path da $s$ a $t$, allora $(s, \dots, x)$ farebbe meglio a essere lo shortest path da $s$ a $x$.

**Inizializzazione e aggiornamento.** Lo shortest path da $s$ a $s$ è $d(s, s) = 0$. Se tutti i pesi sono positivi, l'arco più piccolo incidente su $s$, diciamo $(s, x)$, definisce $d(s, x)$. Non appena si stabilisce lo shortest path da $s$ a un nuovo nodo $x$, si percorrono tutti i suoi archi incidenti per vedere se esiste un modo migliore di arrivare dagli altri nodi passando per $x$.

```
known = {s}
for i = 1 to n, dist[i] = ∞
for each edge (s,v), dist[v] = d(s,v)
last = s
while (last ≠ t)
    select v such that dist(v) = min_unknown dist(i)
    for each (v,x), dist[x] = min(dist[x], dist[v] + w(v,x))
    last = v
    known = known ∪ {v}
```

![[13-visite-grafi-p51-dijkstra-esempio.png]]
*Esempio: il grafo $G$ e il suo albero dei cammini minimi Dijkstra(G,A).*

![[13-visite-grafi-p52-dijkstra-grafo.png]]
*Primo fotogramma di un'animazione: grafo non orientato, pesi non negativi, sorgente $A$, coda di priorità $Q$ ordinata per distanza (tutti i vertici a $\infty$).*

**Analisi.** Trovare il fringe-edge di peso minimo richiede tempo $O(n)$ (basta scorrere la lista dei fringe). Dopo aver aggiunto un nuovo vertice $v$ all'albero, scorrere la sua lista di adiacenza per aggiornare il costo di aggiungere i vertici fringe, se si è trovato un modo più economico passando per $v$, si fa in $O(n)$. Il tempo totale è $n \times n = O(n^2)$.

Possiamo fare di meglio? Possiamo sfruttare la «località temporale» dei nodi visitati?

*Approfondimenti nel wiki: [[visita-di-un-grafo]], [[visita-in-ampiezza]], [[print-path]], [[visita-in-profondita]], [[ordinamento-topologico]], [[dijkstra]]*

## Lezione 14 — Backpropagation

*Fonte: 14 - Backpropagation.pdf (30 pagine: slide, con note a mano alle p. 2, 5, 26, 28, 29).*

### Motivazione · [[14 - Backpropagation.pdf#page=2|p. 2]], [[14 - Backpropagation.pdf#page=1|p. 1]]

- Calcolo di derivate in funzioni composte (nota a mano: da dove nasce → regola della catena).
- Si considera una funzione scalare $C: \mathbb{R}^n \to \mathbb{R}$ ottenuta come composizione di molte operazioni elementari. Esempio: $C(x) = \tfrac{1}{2}\bigl(f(g(h(x)))\bigr)^2$.
- Obiettivo: calcolare il gradiente $\nabla C(x)$ in modo sistematico ed efficiente.
- Idea: sfruttare la struttura di composizione rappresentandola come un **grafo computazionale**.

### Grafi computazionali feedforward · [[14 - Backpropagation.pdf#page=3|p. 3]]

Si usa un **grafo diretto aciclico (DAG)** organizzato per layer:
- Layer 0: variabili di input $x_1, \dots, x_n$;
- Layer $1, 2, \dots, L-1$: variabili intermedie;
- Layer $L$: uscita scalare $C$ (o poche variabili di output).

Ogni nodo $v$ (non di input) rappresenta una funzione locale $z_v = f_v\bigl(z_{u_1}, \dots, z_{u_k}\bigr)$. Il grafo è feedforward: archi solo da layer inferiori a layer superiori, niente cicli («inferiore» e «superiore» sono intesi in termini di profondità di livello).

### Esempio di grafo semplice · [[14 - Backpropagation.pdf#page=4|p. 4]], [[14 - Backpropagation.pdf#page=5|5]]

Input $a$, $b$; $C(a, b) = \tfrac{1}{2}(\sin(a \cdot b) + b - 1)^2$. Ogni nodo rappresenta una variabile; ogni arco una dipendenza diretta.

| Layer 0 | Layer 1 | Layer 2 | Layer 3 | Layer 4 |
|---|---|---|---|---|
| $a$, $b$ | $c = a \cdot b$ | $d = \sin(c)$ | $e = d + b$ | $C = \tfrac{1}{2}(e-1)^2$ |

![[14-backpropagation-p5-grafo-semplice.png]]
*Il grafo con i suoi layer; note a mano: grafo operazionale in cui i nodi rappresentano le operazioni computazionalmente indipendenti, è un flusso di dati; è un DAG ma non è un albero, quindi non ha una radice.*

### Il problema del gradiente sul grafo · [[14 - Backpropagation.pdf#page=6|p. 6]]

- C'è un'unica uscita scalare $C$ in cima al grafo.
- Si vogliono le derivate rispetto agli input, $\partial C/\partial a$ e $\partial C/\partial b$.
- Si possono volere anche $\partial C/\partial c$, $\partial C/\partial d$, … per tutti i nodi interni.
- La regola della catena si può applicare in modo meccanico sul grafo, ma la sua applicazione ripetuta potrebbe essere molto onerosa.

### Perché serve la backpropagation · [[14 - Backpropagation.pdf#page=7|p. 7]]

Si supponga una rete con un milione di parametri $w_1, \dots, w_n$ e una funzione scalare di costo $C$: $\nabla C = (\partial C/\partial w_1, \partial C/\partial w_2, \dots, \partial C/\partial w_n)$.

**Il problema algoritmico.** Calcolare ogni derivata separatamente può ripetere gran parte dei calcoli: come riutilizzare le quantità intermedie già disponibili? **L'idea:** dividere la computazione in due momenti separati, un passaggio in avanti per i valori e un passaggio all'indietro per tutte le derivate.

### Regola della catena su un grafo · [[14 - Backpropagation.pdf#page=8|p. 8]]

Sia $x$ una variabile interna del grafo e $C$ l'uscita finale. Se $x$ influenza $C$ tramite i successori $y_1, \dots, y_k$:

$$
\frac{\partial C}{\partial x} = \sum_{j} \left( \frac{\partial C}{\partial y_j} \cdot \frac{\partial y_j}{\partial x} \right)
$$

Nel grafo $x$ è un nodo e gli $y_j$ sono i suoi successori diretti. Una volta note le derivate $\partial C/\partial y_j$, si può risalire a $\partial C/\partial x$: questo è il principio di base della backpropagation sul grafo.

### Passo forward (valori) · [[14 - Backpropagation.pdf#page=9|p. 9]]

Input: valori iniziali $x_1, \dots, x_n$ nel layer 0. Per $\ell = 0, 1, \dots, L$, per ogni nodo $v$ nel layer $\ell$:
- se $v$ è di input, $value[v]$ è fornito dall'esterno;
- altrimenti $value[v] = f_v(value[u] \text{ per } u \in pred[v])$.

Alla fine del forward si ha il valore di ogni nodo, in particolare di $C$. I $value[v]$ si possono memorizzare per usarli nel passo backward.

### Passo backward (derivate) · [[14 - Backpropagation.pdf#page=10|p. 10]]

Inizializzazione: $\delta_v = 0$ per tutti i nodi $v$. Per il nodo di uscita $C$: $\delta_C = 1$ (oppure $\delta_C = d\,Costo/dC$ se c'è una funzione di costo esterna). Per $\ell = L, L-1, \dots, 0$, per ogni nodo $v$ nel layer $\ell$ e per ogni predecessore $u$ di $v$:

$$
\delta_u \mathrel{+}= \delta_v \cdot \frac{\partial z_v}{\partial z_u}
$$

Al termine, per i nodi di input $x_i$: $\delta_{x_i} = \partial C/\partial x_i$.

### Esempio: calcolo del gradiente · [[14 - Backpropagation.pdf#page=11|p. 11]]–[[14 - Backpropagation.pdf#page=21|21]]

Si vuole valutare $C(a, b) = \tfrac{1}{2}(\sin(a \cdot b) + b - 1)^2$ e calcolarne il gradiente nel punto $(2, 3)$, con $value[a] = 2$ e $value[b] = 3$.

![[14-backpropagation-p11-esempio-forward-1.png]]

**Forward** (pp. 11–15; il seno è valutato in radianti; i valori si memorizzano perché servono nel backward):
1. $value[a] = 2$, $value[b] = 3$;
2. $value[c] = value[a] \cdot value[b] = 2 \cdot 3 = 6$;
3. $value[d] = \sin(value[c]) = \sin(6) \approx -0{,}2794$;
4. $value[e] = value[d] + value[b] = \sin(6) + 3 \approx 2{,}7206$ (il valore di $b$ è riutilizzato senza ricalcolarlo);
5. $C = \tfrac{1}{2}(value[e] - 1)^2 = \tfrac{1}{2}(\sin(6) + 2)^2 \approx 1{,}4802$.

**Backward** (pp. 16–20): $\delta[v] = \partial C/\partial z_v$, inizialmente 0 per ogni $v \ne C$, e $\delta[C] = \partial C/\partial C = 1$. Le quantità rosse sono accumulatori delle derivate, non valori dei nodi.
1. Da $C$ a $e$: $\partial C/\partial e = e - 1 \approx 1{,}7206$; $\delta[e] \mathrel{+}= \delta[C] \cdot (e-1) \approx 1{,}7206$.
2. Da $e$ a $d$ e $b$: $e = d + b$, $\partial e/\partial d = \partial e/\partial b = 1$, quindi $\delta[d] \mathrel{+}= \delta[e] \cdot 1 \approx 1{,}7206$ e $\delta[b] \mathrel{+}= \delta[e] \cdot 1 \approx 1{,}7206$. Attenzione: $\delta[b]$ è ancora parziale, perché manca il contributo di $c$.
3. Da $d$ a $c$: $d = \sin(c)$ usa il valore di $c$ memorizzato nel forward; $\partial d/\partial c = \cos(c) = \cos(6) \approx 0{,}9602$; $\delta[c] \mathrel{+}= \delta[d] \cdot \cos(6) \approx 1{,}6521$. Non serve ricalcolare il cammino a monte di $c$.
4. Da $c$ ad $a$ e $b$: $c = a \cdot b$; $\partial c/\partial a = b = 3 \Rightarrow \delta[a] \mathrel{+}= \delta[c] \cdot 3 \approx 4{,}9562$; $\partial c/\partial b = a = 2 \Rightarrow \delta[b] \leftarrow \delta[b] + \delta[c] \cdot 2 \approx 5{,}0247$. Nota: per $b$, $1{,}7206 + 3{,}3041 \approx 5{,}0247$: due cammini, due contributi, una somma.

![[14-backpropagation-p20-backward-ultimo-passo.png]]

**Risultato** (p. 21, verifica con la regola della catena):

$$
\frac{\partial C}{\partial a} = (\sin(ab) + b - 1) \cdot b\cos(ab) \approx 4{,}9562, \qquad \frac{\partial C}{\partial b} = (\sin(ab) + b - 1) \cdot (a\cos(ab) + 1) \approx 5{,}0247
$$

$\nabla C(2, 3) \approx (4{,}9562;\ 5{,}0247)$; i calcoli usano valori non arrotondati.

### Pseudocodice e correttezza · [[14 - Backpropagation.pdf#page=22|p. 22]], [[14 - Backpropagation.pdf#page=23|23]]

$Ord$ = ordine topologico di $G$; $pred[v]$ = predecessori di $v$; $value[v]$ = valore; $\delta[v]$ = derivata del costo rispetto al valore di $v$.

```
FORWARD
for v in Ord:
    if v è un input:
        value[v] ← input[v]
    else:
        args ← [value[u] for u in pred[v]]
        value[v] ← f_v(args)

BACKWARD
for v in V: δ[v] ← 0
δ[C] ← 1
for v in reverse(Ord):
    for u in pred[v]:
        dlocal ← ∂f_v/∂z_u
        δ[u] += δ[v] · dlocal
```

La derivata locale è valutata usando i valori del forward. Per un DAG per layer, $Ord$ può essere semplicemente l'ordine dei layer.

**Correttezza.** Si ordinano i nodi in ordine topologico $v_1, \dots, v_m$.
- *Forward:* ogni nodo usa solo predecessori già calcolati → corretto per costruzione.
- *Backward:* usa l'ordine topologico inverso $v_m, \dots, v_1$. **Invariante:** quando si processa $v$, $\delta_v = \partial C/\partial z_v$ è già corretto.
  - Base: nodo di uscita $C$, $\delta_C = \partial C/\partial C = 1$.
  - Passo induttivo: si suppongano corrette le $\delta_y$ per tutti i successori $y$ di $x$; allora $\delta_x = \sum_{y \in succ(x)} \delta_y \cdot \partial z_y/\partial z_x$, che è la regola della catena. Quindi per induzione $\delta_v$ è corretta per ogni nodo $v$.

### Complessità computazionale · [[14 - Backpropagation.pdf#page=24|p. 24]]

Siano $V$ ed $E$ il numero di nodi e di archi del grafo computazionale.
- **Forward:** ogni nodo è valutato una volta e ogni dipendenza è letta una volta: $O(V + E)$.
- **Backward:** ogni nodo e ogni arco sono elaborati una volta: $O(V + E)$.

I limiti assumono costo $O(1)$ per ciascuna operazione elementare e per il contributo di ogni arco; operazioni più complesse vanno contabilizzate separatamente.

### Dai grafi alle reti neurali · [[14 - Backpropagation.pdf#page=25|p. 25]]–[[14 - Backpropagation.pdf#page=28|28]]

Una **rete neurale feedforward** può essere rappresentata come un DAG di operazioni matematiche (input, layer 1, layer 2, costo). Non serve ancora conoscere il funzionamento dei neuroni: interessano la struttura delle dipendenze e l'ordine in cui si possono eseguire i calcoli.

![[14-backpropagation-p25-rete-neurale.png]]

Una rete neurale feedforward è un caso particolare di grafo computazionale:
- **nodi:** operazioni di somma pesata, funzioni di attivazione, ecc.;
- **archi:** connessioni che trasportano i valori (e le dipendenze).

La backpropagation «classica» delle reti neurali è l'algoritmo visto, applicato a un grafo con struttura molto regolare (layer di neuroni). Capita la backpropagation su grafi generici, diventa banale capirla e specializzarla al caso delle reti neurali (nota a mano: è solo una tecnica del calcolo del gradiente sui grafi computazionali).

- **Forward: i valori** — si parte dagli input e si calcolano i valori dei nodi, rispettando le dipendenze. *Ordine topologico:* ogni nodo usa soltanto valori già calcolati.
- **Backward: le derivate** — si parte dal costo $C$ e si propagano le derivate verso i predecessori. *Ordine topologico inverso:* ogni nodo accumula i contributi di tutti i suoi successori. (Nota a mano: verifico se la predizione è giusta ⇒ in base all'errore commesso …, per propagare all'indietro l'errore e ricavare la derivata; lettura incerta.)

### Dai grafi all'apprendimento · [[14 - Backpropagation.pdf#page=29|p. 29]], [[14 - Backpropagation.pdf#page=30|30]]

Nel Machine Learning, la backpropagation **calcola il gradiente del costo rispetto ai parametri**. Non modifica, da sola, i parametri della rete.

| Forward | Backward | Ottimizzazione |
|---|---|---|
| Calcolo del costo $C$ | Calcolo di $\nabla C$ | Aggiornamento dei parametri |

Esempio di aggiornamento: $w_i \leftarrow w_i - \eta \cdot \partial C/\partial w_i$ (note a mano: $\eta$ = *learning rate*, valore di scala; $w_i$ = parametri; $\partial C/\partial w_i$ = errore commesso).

Da ASD: grafi orientati, DFS, ordinamento topologico, riuso dei risultati intermedi. Da ML: scelta del modello, del costo e dell'algoritmo di ottimizzazione.

L'ultima slide (p. 30) mostra il primo fotogramma di un'animazione, «1. Forward pass»: l'immagine di un gatto entra nella rete (valori di input 0,20; 0,80; 0,50), un livello nascosto di due nodi e due uscite, «Cane» e «Gatto».

*Approfondimenti nel wiki: [[grafo-computazionale]], [[backpropagation]]*

## Lezione 15 — Backtracking

*Fonte: 15 - Backtracking.pdf (24 pagine di slide in inglese di S. Skiena, con note a mano alle p. 2, 15, 21).*

### Sudoku · [[15 - Backtracking.pdf#page=2|p. 2]], [[15 - Backtracking.pdf#page=3|3]], [[15 - Backtracking.pdf#page=1|p. 1]]

![[15-backtracking-p2-sudoku.png]]
*Un Sudoku e la sua soluzione. Nota a mano (lettura incerta): posso creare un grafo dello spazio delle soluzioni, e una soluzione è un nodo di questo grafo ⇒ posso sapere se un nodo è soluzione o meno ma lo devo visitare ⇒ devo guardare tutto il grafo (potenzialmente).*

Risolvere il Sudoku comporta una forma di **ricerca esaustiva** delle configurazioni possibili. Sfruttare i vincoli per escludere certe possibilità in certe posizioni permette di **potare** la ricerca fino al punto in cui le persone riescono a risolvere il Sudoku a mano. Il **backtracking** è la chiave per implementare in modo corretto ed efficiente programmi di ricerca esaustiva.

### Backtracking · [[15 - Backtracking.pdf#page=4|p. 4]]

Il backtracking è un metodo sistematico per iterare su tutte le configurazioni possibili di uno spazio di ricerca. È un algoritmo generale che va personalizzato per ogni applicazione. La soluzione è modellata come un vettore $a = (a_1, a_2, \dots, a_n)$, in cui ogni elemento $a_i$ è scelto da un insieme finito e ordinato $S_i$. Il vettore può rappresentare una disposizione in cui $a_i$ contiene l'$i$-esimo elemento di una permutazione; oppure un sottoinsieme $S$, in cui $a_i$ è vero se e solo se l'$i$-esimo elemento dell'universo è in $S$.

### L'idea del backtracking · [[15 - Backtracking.pdf#page=5|p. 5]]

A ogni passo dell'algoritmo di backtracking si parte da una soluzione parziale, $a = (a_1, a_2, \dots, a_k)$, e si prova a estenderla aggiungendo un altro elemento in fondo. Dopo l'estensione si verifica se quello che si ha finora è una soluzione completa. Se non lo è, la questione critica è se la soluzione parziale corrente $a$ sia potenzialmente estendibile a una soluzione:
- se sì, si ricorre e si continua;
- se no, si cancella l'ultimo elemento da $a$ e si prova un'altra possibilità per quella posizione, se esiste.

### Implementazione del backtracking · [[15 - Backtracking.pdf#page=6|p. 6]]–[[15 - Backtracking.pdf#page=12|12]]

**Backtracking ricorsivo** (p. 7):

```
Backtrack (a, k)
if a is a solution, print (a)
else {
    k = k + 1
    compute S_k
    while S_k ≠ ∅ do
        a_k = an element in S_k
        S_k = S_k − a_k
        Backtrack (a, k)
}
```

**Backtracking e DFS** (p. 8): il backtracking è in realtà una visita in profondità di un grafo implicito di configurazioni.
- Può essere usato facilmente per iterare su tutti i sottoinsiemi o su tutte le permutazioni di un insieme.
- Assicura la correttezza enumerando tutte le possibilità.
- Per essere efficiente bisogna potare i rami morti o ridondanti dello spazio di ricerca, quando possibile.

**Implementazione in C** (p. 9):

```c
void backtrack(int a[], int k, data input) {
    int c[MAXCANDIDATES];       /* candidates for next position */
    int nc;                     /* next position candidate count */
    int i;                      /* counter */
    if (is_a_solution(a, k, input)) {
        process_solution(a, k, input);
    } else {
        k = k + 1;
        construct_candidates(a, k, input, c, &nc);
        for (i = 0; i < nc; i++) {
            a[k] = c[i];
            make_move(a, k, input);
            backtrack(a, k, input);
            unmake_move(a, k, input);
            if (finished) {
                return;         /* terminate early */
            }
        }
    }
}
```

- `is_a_solution(a, k, input)` (p. 10): funzione booleana che verifica se i primi $k$ elementi del vettore $a$ sono una soluzione completa per il problema dato; l'ultimo argomento, `input`, permette di passare informazioni generali per valutare se $a$ è una soluzione.
- `construct_candidates(a, k, input, c, nc)` (p. 11): riempie un array `c` con l'insieme completo dei possibili candidati per la $k$-esima posizione di $a$, dato il contenuto delle prime $k-1$ posizioni; il numero di candidati restituiti è `nc`.
- `process_solution(a, k)` (p. 12): stampa, conta o in qualche modo elabora una soluzione completa una volta costruita.

Il backtracking assicura la correttezza enumerando tutte le possibilità; assicura l'efficienza non visitando mai uno stato più di una volta. Poiché a ogni chiamata ricorsiva si alloca un nuovo array di candidati `c`, i sottoinsiemi dei candidati di estensione non ancora considerati a ogni posizione non interferiscono fra loro.

### Costruire tutti i sottoinsiemi · [[15 - Backtracking.pdf#page=13|p. 13]]–[[15 - Backtracking.pdf#page=18|18]]

Per costruire tutti i $2^n$ sottoinsiemi si usa un array/vettore di $n$ celle, in cui il valore di $a_i$ è vero o falso, a significare se l'$i$-esimo elemento è o non è nel sottoinsieme. Nella notazione dell'algoritmo generale, $S_k = (\text{true}, \text{false})$ e $a$ è una soluzione ogni volta che $k \ge n$.

```c
int is_a_solution(int a[], int k, int n) {
    return (k == n);
}

void construct_candidates(int a[], int k, int n, int c[], int *nc) {
    c[0] = true;
    c[1] = false;
    *nc = 2;
}

void process_solution(int a[], int k, int input) {
    int i;                      /* counter */
    printf("{");
    for (i = 1; i <= k; i++) {
        if (a[i] == true) {
            printf(" %d", i);
        }
    }
    printf(" }\n");
}

void generate_subsets(int n) {
    int a[NMAX];                /* solution vector */
    backtrack(a, 0, n);
}
```

Qui si stampano gli elementi di ogni sottoinsieme, ma si può fare quello che si vuole, per esempio testare se è una soluzione di un problema di vertex cover.

**Ordine di generazione dei sottoinsiemi di $\{1, 2, 3\}$** (p. 15):

$$
\begin{aligned}
&(1) \to (1,2) \to (1,2,3) \to (1,2,-) \to (1,-) \to (1,-,3) \to (1,-,-) \to (1,-) \to (1) \to (-) \to \\
&(-,2) \to (-,2,3) \to (-,2,-) \to (-,-) \to (-,-,3) \to (-,-,-) \to (-,-) \to (-) \to ()
\end{aligned}
$$

Le foglie dell'albero sono $\{1,2,3\}$, $\{1,2\}$, $\{1,3\}$, $\{1\}$, $\{2,3\}$, $\{2\}$, $\{3\}$, $\{\}$ (nota a mano, lettura incerta: che significa che non è un algoritmo sistematico ma va verso la costruzione → sono fuso?).

![[15-backtracking-p15-sottoinsiemi-albero.png]]

### Costruire tutte le permutazioni · [[15 - Backtracking.pdf#page=19|p. 19]]–[[15 - Backtracking.pdf#page=24|24]]

Quante sono le permutazioni di un insieme di $n$ elementi? Per costruire tutte le $n!$ permutazioni si usa un array/vettore di $n$ celle, in cui il valore di $a_i$ è un intero da 1 a $n$ che non è ancora comparso nel vettore, corrispondente all'$i$-esimo elemento della permutazione. Nella notazione dell'algoritmo generale, $S_k = (1, \dots, n) - v$ e $v$ è una soluzione ogni volta che $k \ge n$.

**Ordine di generazione delle permutazioni** (p. 21): $(1) \to (1,2) \to (1,2,3) \to (1,2) \to (1) \to (1,3) \to (1,3,2) \to (1,3) \to (1) \to () \to (2) \to (2,1) \to (2,1,3) \to (2,1) \to (2) \to (2,3) \to (2,3,1) \to (2,3) \to () \to (2) \to () \to (3) \to (3,1) \to (3,1,2) \to (3,1) \to (3) \to (3,2) \to (3,2,1) \to (3,2) \to (3) \to ()$. Le soluzioni sono $123, 132, 213, 231, 312, 321$ (nota a mano: posso togliere grandi porzioni di albero appena diventano inutili o ridondanti).

![[15-backtracking-p21-permutazioni-albero.png]]

Per evitare di ripetere elementi della permutazione, $S_k = \{1, \dots, n\} - a$ e $a$ è una soluzione ogni volta che $k = n$:

```c
void construct_candidates(int a[], int k, int n, int c[], int *nc) {
    int i;                      /* counter */
    bool in_perm[NMAX];         /* what is now in the permutation? */
    for (i = 1; i < NMAX; i++) {
        in_perm[i] = false;
    }
    for (i = 1; i < k; i++) {
        in_perm[a[i]] = true;
    }
    *nc = 0;
    for (i = 1; i <= n; i++) {
        if (!in_perm[i]) {
            c[*nc] = i;
            *nc = *nc + 1;
        }
    }
}
```

Per completare il lavoro servono `process_solution` e `is_a_solution`, oltre ai parametri giusti per `backtrack`; sono essenzialmente gli stessi dei sottoinsiemi:

```c
void process_solution(int a[], int k, int input) {
    int i;                      /* counter */
    for (i = 1; i <= k; i++) {
        printf(" %d", a[i]);
    }
    printf("\n");
}

int is_a_solution(int a[], int k, int n) {
    return (k == n);
}

void generate_permutations(int n) {
    int a[NMAX];                /* solution vector */
    backtrack(a, 0, n);
}
```

*Approfondimenti nel wiki: [[backtracking]], [[generazione-di-permutazioni]]*
