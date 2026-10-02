# Lezioni — Algoritmi e Strutture Dati

Percorso di studio lezione per lezione. **Ogni pagina del wiki compare una sola volta**, nel punto in cui il suo argomento compare per la prima volta nelle slide: aperta una pagina, leggila tutta (contiene anche le slide successive che la riguardano, indicate accanto al link). Quando una lezione riprende una pagina già letta, è indicata in corsivo senza link.
Ordine delle lezioni: prefisso numerico del nome del file (`00-`, `01-`, …). Dove le slide saltano avanti e indietro tra argomenti c'è anche un **ordine consigliato**.

Quadro generale: [[overview]] · catalogo di tutte le pagine: [[index]] · registro delle operazioni: [[log]]

---

## Lezione 00 — Presentazione del corso
**PDF:** [[00-Presentazione.pdf]] (pp. 1–8)

1. [[presentazione-del-corso]] — pp. 1–8 · corso integrato ASD + ML, docenza, modalità d'esame, programma, obiettivi, libri

> 💡 Prima di iniziare con la lezione 01 conviene leggere anche la pagina sulle convenzioni per lo pseudocodice (sezione *Materiale di supporto* in fondo): lo pseudocodice compare già dalla lezione 01.

---

## Lezione 01 — Introduzione: concetti fondamentali
**PDF:** [[01-Introduzione.pdf]] (pp. 1–60)

### In ordine di slide
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
18. [[lezione-01-introduzione]] — riepilogo: pp. 1–6 (motivazione, esempi di ambiti), punti chiave, refusi, domande d'esame

### Ordine consigliato
Le slide sono coerenti; l'unico accorgimento è che le pagine 9, 10 e 16 (ricerca combinatoria, metodi euristici, ricerca di controesempi) contengono già le definizioni della lezione 03: leggerle qui dà il quadro generale; alla lezione 03 non vanno riaperte.

---

## Lezione 02 — Notazione asintotica
**PDF:** [[02-Notazione asintotica.pdf]] (pp. 1–38)

### In ordine di slide
1. [[modello-ram]] — pp. 2, 5–6 · ipotesi del modello, «flat-earth model»
2. [[tempo-di-esecuzione]] — pp. 3, 8 · $T(n) = \sum c_i t_i(n)$, efficienza asintotica, complessità spaziale
3. [[casi-di-complessita]] — pp. 7, 9–12 · Base(), Base2(n), peggiore/migliore/medio, lotteria
4. [[notazione-asintotica]] — pp. 15–18, 21–23, 27 · $O$, $\Omega$, $\Theta$, esempi su $3n^2-100n+6$, proprietà
5. [[dimostrazioni-notazione-asintotica]] — esercizio sugli esempi di pp. 21–24
6. [[regole-di-calcolo-asintotico]] — pp. 24–26 · somma, differenza, costante, prodotto
7. [[dominanza-asintotica]] — pp. 30–37 · razzo e vela, little-o, limite, tabella di crescita, classifiche
8. [[lezione-02-notazione-asintotica]] — riepilogo

Già letta: *stima-dei-tempi-di-esecuzione* (lezione 01) — il caso 4 ricalcola la tabella di p. 36.

### Ordine consigliato
Le slide alternano argomenti: modello RAM (p. 2) → tempo (p. 3) → modello RAM (pp. 5–6) → casi (p. 7) → tempo (p. 8) → casi (pp. 9–12), e le proprietà di $O$/$\Omega$/$\Theta$ (p. 27) arrivano dopo le regole di calcolo (pp. 24–26). Aggregando per pagina, l'ordine sopra è già quello consigliato: prima il modello, poi come si conta, poi quale caso, poi la notazione **completa** (proprietà incluse) e solo dopo le regole di calcolo, che la usano.

---

## Lezione 03 — Analisi di correttezza e di complessità degli algoritmi
**PDF:** [[03-Analisi di algoritmi.pdf]] (pp. 1–34)

### In ordine di slide
1. [[paradigmi-di-progettazione]] — pp. 2–3 · tre famiglie di approcci
2. [[divide-et-impera]] — p. 4
3. [[iterazione-e-ricorsione]] — pp. 7–11 · confronto dei due stili
4. [[somma-iterativa]] — p. 11 (poi pp. 17, 23–29) · pseudocodice, invariante, costo $2n+4$
5. [[somma-ricorsiva]] — p. 11 (poi pp. 19, 30–34) · pseudocodice, induzione, ricorrenza
6. [[correttezza-parziale-e-totale]] — p. 16 (con la definizione di 01 p. 9) · parziale = «se termina, è giusto»; totale = parziale + terminazione; quale strumento dimostra cosa
7. [[invariante-di-ciclo]] — pp. 16–17
8. [[correttezza-per-induzione]] — pp. 18–19
9. [[dimostrazioni-di-correttezza]] — esercizio su invariante e induzione
10. [[analisi-del-costo-riga-per-riga]] — esercizio sulle pp. 23–29 (e su Base/Base2 della lezione 02)
11. [[equazioni-di-ricorrenza]] — pp. 30–34
12. [[risoluzione-ricorrenze]] — esercizio sulle pp. 30–33
13. [[lezione-03-analisi-di-algoritmi]] — riepilogo, refusi (p. 17 «i = 0»; p. 5), domande d'esame

Già lette: *ricerca-combinatoria* (p. 5), *metodi-euristici* (p. 6), *ricerca-di-controesempi* (pp. 12–15) nella lezione 01; *modello-ram* e *tempo-di-esecuzione* (pp. 20–22, identiche alle pp. 2–3 della lezione 02) nella lezione 02.

### Ordine consigliato
Qui le slide non sono lineari rispetto alle pagine: la somma $1..n$ compare a p. 11, ma la sua correttezza (pp. 17–19) e la sua complessità (pp. 23–34) arrivano molto dopo, e le pagine delle due somme contengono già tutto. Conviene prima la **teoria** e poi gli **esempi**:

1. *paradigmi-di-progettazione* → *divide-et-impera* → *iterazione-e-ricorsione*
2. *correttezza-parziale-e-totale* (il quadro) → *invariante-di-ciclo* → *correttezza-per-induzione* (gli strumenti)
3. *equazioni-di-ricorrenza* (complessità ricorsiva; la parte iterativa è in *tempo-di-esecuzione*, già letta)
4. *somma-iterativa* → *somma-ricorsiva* (gli esempi completi, come sintesi)
5. esercizi: *dimostrazioni-di-correttezza* → *analisi-del-costo-riga-per-riga* → *risoluzione-ricorrenze*
6. riepilogo *lezione-03-analisi-di-algoritmi*

---

## Lezione 04 — Strutture dati elementari
**PDF:** [[04-Strutture dati elementari.pdf]] (pp. 1–30)

### In ordine di slide
1. [[tipo-di-dato-astratto]] — pp. 2–4 · operazioni astratte contro implementazione
2. [[strutture-contigue-e-collegate]] — p. 5 (poi pp. 15, 21) · array contro puntatori, vantaggi delle liste
3. [[array]] — pp. 7–9
4. [[array-dinamico]] — pp. 10–12 · raddoppio, $M \le 2n$, «no free lunch»
5. [[lista-concatenata]] — pp. 14–22 · codice C, costi, liste doppie
6. [[pila]] — pp. 24–26, 28–29 · LIFO, Figura 10.1, DFS
7. [[coda]] — pp. 25, 27–29 · FIFO, Figura 10.2, BFS
8. [[tracce-pila-e-coda]] — esercizio sulle Figure 10.1 e 10.2
9. [[lezione-04-strutture-dati-elementari]] — riepilogo, osservazione su `delete_list`, domande d'esame

### Ordine consigliato
*strutture-contigue-e-collegate* compare a p. 5 ma la sua tabella di confronto usa anche le liste (pp. 15, 21): leggila **dopo** *lista-concatenata*. Ordine: *tipo-di-dato-astratto* → *array* → *array-dinamico* → *lista-concatenata* → *strutture-contigue-e-collegate* → *pila* → *coda* → *tracce-pila-e-coda* → riepilogo.

---

## Lezione 05 — Insertion sort
**PDF:** [[05-Insertion sort.pdf]] (pp. 1–33)

### In ordine di slide
Prima, pp. 2–3: *ordinamento* (già letta nella lezione 01). È stata aggiornata con questa lezione: rileggi le sezioni «Definizione formale» (p. 2), «Applicazioni» (p. 3) e la nuova tabella «Algoritmi che lo risolvono».

1. [[insertion-sort]] — pp. 4–23 · idea e ordinamento sul posto (p. 4), pseudocodice e traccia su ⟨5, 2, 4, 6, 1, 3⟩ (pp. 5–15), invariante (p. 16), tabella dei costi (p. 17), $T(n)$ (pp. 18–19), caso migliore lineare (p. 20), caso peggiore quadratico (pp. 21–22), codice C++ (p. 23)
2. [[selection-sort]] — pp. 24–29 · esercizio 2.2.2: consegne, codice C, correttezza, efficienza $n(n-1)/2$, memoria (risposte 🧩)
3. [[substring-pattern-matching]] — p. 30 · il problema e l'esempio *abba* in *aababba*
4. [[findmatch]] — p. 31 · algoritmo a forza bruta e sua efficienza $O(nm)$
5. [[logaritmi-nell-analisi]] — pp. 32–33 · dimezzamento ripetuto, alberi, bit, numeri armonici, split 1/3–2/3 della ricerca binaria
6. [[potenza-veloce]] — p. 32 · `power(a,n)` con $O(\lg n)$ moltiplicazioni
7. [[lezione-05-insertion-sort]] — riepilogo, refusi (codice C++ per valore, esercizio 2.2.2), domande d'esame

Già lette, con casi nuovi da questa lezione: *invariante-di-ciclo* (p. 16), *casi-di-complessita* (pp. 20–22), *efficienza-degli-algoritmi* (insertion sort ora ha la sua pagina), *dominanza-asintotica* (collegamento ai logaritmi), *analisi-del-costo-riga-per-riga* (casi 4–5), *dimostrazioni-di-correttezza* (casi 5–6), *stima-dei-tempi-di-esecuzione* (caso 5, p. 33).

### Ordine consigliato
Le slide sono lineari: segui l'ordine sopra. Durante la lezione, per le pp. 4–23 tieni aperta solo *insertion-sort*: le sue sezioni sono nello stesso ordine delle slide. Le pagine di esercizi «già lette» servono dopo, per ripassare.

---

## Lezione 06 — Divide et impera: Merge Sort
**PDF:** [[06-Merge Sort.pdf]] (pp. 1–30)

### In ordine di slide
1. [[torre-di-hanoi]] — pp. 2–4 · S&T: il problema, la figura dei pioli, le 7 mosse per 3 dischi; algoritmo ricorsivo e $2^n - 1$ mosse (🧩)
2. [[merge-sort]] — pp. 5–7 (poi pp. 13–15) · idea divide et impera, albero su ⟨5, 2, 8, 0, 4, 7, 1, 9, 3, 2, 6⟩; pseudocodice (p. 13), ricorrenza $aT(n/b) + D(n) + C(n)$ (p. 14), albero di ricorsione e $\Theta(n\lg n)$ (p. 15)
3. [[merge]] — pp. 8–12 · pseudocodice con sentinelle, traccia su ⟨2, 4, 5, 7⟩ + ⟨1, 2, 3, 6⟩, invariante, costo $\Theta(n)$
4. [[massimo-sottoarray]] — p. 16 · S&T: solo il titolo e il rimando al libro (cap. 4.1)
5. [[metodo-di-sostituzione]] — pp. 18–20 (poi p. 26) · ipotesi + induzione, $2T(\lfloor n/2 \rfloor) + n \le cn\lg n$ con $c \ge 2$, perché due casi base
6. [[metodo-albero-di-ricorrenza]] — pp. 21–27 · $3T(n/4) + cn^2$: livelli, costo per livello, serie geometrica, verifica con $d \ge \frac{16}{13}c$, anche $\Omega(n^2)$
7. [[teorema-dell-esperto]] — pp. 28–30 · tre casi, gap, esempi $9T(n/3) + n$, $T(2n/3) + 1$, $3T(n/4) + n\lg n$, $2T(n/2) + n\lg n$
8. [[lezione-06-merge-sort]] — riepilogo, refusi (titolo «Imera», parti intere), domande d'esame

Già lette, aggiornate con questa lezione: *divide-et-impera* (p. 14: ricorrenza generale e tabella degli esempi), *equazioni-di-ricorrenza* (p. 17: definizione di ricorrenza e i tre metodi), *invariante-di-ciclo* (p. 10, collegamento a Merge), *ordinamento* (tabella con merge sort), *efficienza-degli-algoritmi* ($n\lg n$ ora dimostrato), *risoluzione-ricorrenze* (casi 2–5 e 7), *dimostrazioni-di-correttezza* (casi 7–8), *correttezza-per-induzione*, *logaritmi-nell-analisi*.

### Ordine consigliato
Le slide spezzano merge sort in due (pp. 5–7 e 13–15) con Merge in mezzo (pp. 8–12), e il metodo dell'albero compare una prima volta a p. 15 prima di essere spiegato (pp. 21–27). Ordine suggerito:
1. *torre-di-hanoi*, come riscaldamento sulla ricorsione;
2. *merge* per intero: è il mattone che Merge-Sort usa, e il suo costo $\Theta(n)$ serve nell'analisi;
3. *merge-sort* per intero: la sezione «Soluzione con l'albero di ricorsione» anticipa il metodo che *metodo-albero-di-ricorrenza* spiega in generale;
4. *equazioni-di-ricorrenza* (solo la sezione nuova «Ricorrenze divide et impera»), poi *metodo-di-sostituzione*, *metodo-albero-di-ricorrenza*, *teorema-dell-esperto*, nell'ordine delle slide;
5. *massimo-sottoarray* quando vuoi: è solo un rimando al libro.

---

## Lezione 07 — Quicksort
**PDF:** [[07-Quicksort.pdf]] (pp. 1–25)

### In ordine di slide
1. [[quicksort]] — pp. 2–4 (poi pp. 14–18, 21–22) · proprietà, divide/conquer/combine, pseudocodice; caso peggiore (p. 14), migliore (p. 15), 9:1 (pp. 16–17), medio (p. 18), dimostrazione $\Theta(n^2)$ per sostituzione (pp. 21–22)
2. [[partition]] — pp. 5–13 · quattro aree, traccia su ⟨2, 8, 7, 1, 3, 5, 6, 4⟩, pseudocodice e costo $\Theta(n)$ (p. 12), invariante (p. 13)
3. [[randomizzazione]] — p. 19 (poi pp. 20, 23) · caso peggiore cattivo e caso medio buono; tempo atteso contro caso medio
4. [[quicksort-randomizzato]] — pp. 20, 23 · Randomized-Partition, tempo atteso $O(n\log n)$ (dimostrazione sul libro)
5. [[nuts-and-bolts]] — pp. 24–25 · S&T: algoritmo $O(n^2)$ e randomizzato $O(n\log n)$ atteso (soluzioni 🧩)
6. [[progettazione-divide-et-impera]] — esercizi: Torre di Hanoi (L06), Nuts and Bolts, massimo sottoarray
7. [[lezione-07-quicksort]] — riepilogo, refusi e note, domande d'esame

Già lette, con casi nuovi da questa lezione: *divide-et-impera* (p. 3), *metodo-albero-di-ricorrenza* (pp. 16–18), *teorema-dell-esperto* (p. 15), *metodo-di-sostituzione* (p. 21), *casi-di-complessita* (pp. 14–18, 23), *insertion-sort* (p. 14, confronto sul vettore ordinato), *ordinamento* (righe di quicksort), *invariante-di-ciclo* (p. 13), *risoluzione-ricorrenze* (caso 6), *dimostrazioni-di-correttezza* (casi 9–10).

### Ordine consigliato
Le slide presentano quicksort (pp. 2–4), poi Partition (pp. 5–13), poi tornano all'analisi di quicksort (pp. 14–18), la interrompono con la randomizzazione (pp. 19–20) e la riprendono con la dimostrazione del caso peggiore (pp. 21–22). Ordine suggerito:
1. *partition* per intero: è il cuore di quicksort, e la traccia di pp. 7–11 è la prima chiamata dell'esempio;
2. *quicksort* per intero, compresa la dimostrazione di pp. 21–22 (sta nella stessa sezione «Complessità»);
3. *randomizzazione* e *quicksort-randomizzato*;
4. *nuts-and-bolts*, poi *progettazione-divide-et-impera* per ripassare la progettazione su entrambe le lezioni.

---

## Materiale di supporto — a1: convenzioni per lo pseudocodice
**PDF:** [[a1-indicazioni_psuedocodice.pdf]] (pp. 1–4)

1. [[pseudocodice]] — pp. 2–4 · tutte le regole, esempio, trappole (aliasing, corto circuito)
2. [[convenzioni-per-lo-pseudocodice]] — riepilogo della fonte

_Aggiornato: 2026-09-26 — riorganizzato: una pagina = un link in tutto il file, ordine di prima comparsa nelle slide, ordine consigliato dove le slide non sono lineari_
_Aggiornato: 2026-09-30 — aggiunta la lezione 05 (Insertion sort)_
_Aggiornato: 2026-10-01 — aggiunte le lezioni 06 (Merge Sort) e 07 (Quicksort)_
