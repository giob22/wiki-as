---
tipo: fonte
titolo: "Corso di Algoritmi e Strutture Dati — Insertion sort"
file_raw: "05-Insertion sort.pdf"
pagine: "1-33"
data_ingest: 2026-09-30
formato: slide-pdf
argomenti: [ordinamento, insertion sort, invariante di ciclo, analisi caso migliore e peggiore, selection sort, pattern matching, logaritmi]
---

# Lezione 05 — Insertion sort (05-Insertion sort.pdf)

## Sommario

Slide del Prof. Marrone, a.a. 26/27 ([[05-Insertion sort.pdf#page=1]]). La lezione riprende il problema dell'**ordinamento** e ne elenca le applicazioni. Presenta poi **insertion sort** completo: idea e ordinamento sul posto, pseudocodice, traccia passo per passo su ⟨5, 2, 4, 6, 1, 3⟩, dimostrazione di correttezza con invariante di ciclo, analisi di complessità con la tabella costo × esecuzioni, caso migliore lineare e caso peggiore quadratico, implementazione in C++. Segue l'esercizio del libro di testo 2.2.2 su **selection sort** (implementazione, invariante, correttezza, efficienza, memoria). Due problemi «Stop & Think» chiudono la lezione con la crescita delle funzioni: il **pattern matching** di sottostringhe e l'**importanza dei logaritmi**, con la potenza veloce e lo split sbilanciato della ricerca binaria.

## Percorso della lezione

**PDF:** [[05-Insertion sort.pdf]] (pp. 1–33)

Pagine del wiki nell'ordine di prima comparsa nelle slide (è l'ordine delle pagine di questa lezione nel libro, dopo questa):
1. [[insertion-sort]] — pp. 4–23 · idea e ordinamento sul posto (p. 4), pseudocodice e traccia su ⟨5, 2, 4, 6, 1, 3⟩ (pp. 5–15), invariante (p. 16), tabella dei costi (p. 17), $T(n)$ (pp. 18–19), caso migliore lineare (p. 20), caso peggiore quadratico (pp. 21–22), codice C++ (p. 23)
2. [[selection-sort]] — pp. 24–29 · esercizio 2.2.2: consegne, codice C, correttezza, efficienza $n(n-1)/2$, memoria (risposte 🧩)
3. [[substring-pattern-matching]] — p. 30 · il problema e l'esempio *abba* in *aababba*
4. [[findmatch]] — p. 31 · algoritmo a forza bruta e sua efficienza $O(nm)$
5. [[logaritmi-nell-analisi]] — pp. 32–33 · dimezzamento ripetuto, alberi, bit, numeri armonici, split 1/3–2/3 della ricerca binaria
6. [[potenza-veloce]] — p. 32 · `power(a,n)` con $O(\lg n)$ moltiplicazioni

Prima, pp. 2–3: *ordinamento* (già letta nella lezione 01). È stata aggiornata con questa lezione: rileggi le sezioni «Definizione formale» (p. 2), «Applicazioni» (p. 3) e la nuova tabella «Algoritmi che lo risolvono».


Già lette, con casi nuovi da questa lezione: *invariante-di-ciclo* (p. 16), *casi-di-complessita* (pp. 20–22), *efficienza-degli-algoritmi* (insertion sort ora ha la sua pagina), *dominanza-asintotica* (collegamento ai logaritmi), *analisi-del-costo-riga-per-riga* (casi 4–5), *dimostrazioni-di-correttezza* (casi 5–6), *stima-dei-tempi-di-esecuzione* (caso 5, p. 33).

**Ordine consigliato.**
Le slide sono lineari: segui l'ordine sopra. Durante la lezione, per le pp. 4–23 tieni aperta solo *insertion-sort*: le sue sezioni sono nello stesso ordine delle slide. Le pagine di esercizi «già lette» servono dopo, per ripassare.

## Punti chiave

1. Problema dell'ordinamento e applicazioni: searching, closest pair, element uniqueness, frequency distribution, selection, convex hulls ([[05-Insertion sort.pdf#page=2]], [[05-Insertion sort.pdf#page=3]]) → [[ordinamento]].
2. Insertion sort considera un valore alla volta e lo inserisce tra i precedenti; ordina sul posto ([[05-Insertion sort.pdf#page=4]]) → [[insertion-sort]].
3. Pseudocodice e traccia su ⟨5, 2, 4, 6, 1, 3⟩ ([[05-Insertion sort.pdf#page=5]]–[[05-Insertion sort.pdf#page=15]]).
4. Correttezza con invariante: $A[1..j-1]$ contiene gli elementi originali di $A[1..j-1]$, ordinati ([[05-Insertion sort.pdf#page=16]]) → [[invariante-di-ciclo]].
5. Tabella dei costi $c_i$ e numeri di esecuzioni; $t_j$ = numero di test del `while` ([[05-Insertion sort.pdf#page=17]]).
6. $T(n) = c_1 n + c_2(n-1) + c_4(n-1) + c_5\sum t_j + c_6\sum(t_j-1) + c_7\sum(t_j-1) + c_8(n-1)$ ([[05-Insertion sort.pdf#page=18]], [[05-Insertion sort.pdf#page=19]]).
7. Caso migliore (già ordinato, $t_j = 1$): $T(n) = an + b$, lineare ([[05-Insertion sort.pdf#page=20]]).
8. Caso peggiore (ordine decrescente, $t_j = j$): $T(n) = an^2 + bn + c$, quadratico ([[05-Insertion sort.pdf#page=21]], [[05-Insertion sort.pdf#page=22]]).
9. Implementazione in C++ ([[05-Insertion sort.pdf#page=23]]).
10. Esercizio 2.2.2, selection sort: consegne, codice C, correttezza, efficienza ($\sum_{i=0}^{n-2}(n-1-i) = n(n-1)/2$), memoria ([[05-Insertion sort.pdf#page=24]]–[[05-Insertion sort.pdf#page=29]]) → [[selection-sort]].
11. S&T String Pattern Matching e `findmatch`: valutare l'efficienza asintotica ([[05-Insertion sort.pdf#page=30]], [[05-Insertion sort.pdf#page=31]]) → [[substring-pattern-matching]], [[findmatch]].
12. I logaritmi nascono dal dimezzamento ripetuto: ricerca binaria, alberi, bit, moltiplicazione, potenza veloce, numeri armonici ([[05-Insertion sort.pdf#page=32]]) → [[logaritmi-nell-analisi]], [[potenza-veloce]].
13. S&T Importance of an Even Split: $\log_{3/2} 10^6 \approx 35$ contro $\log_2 10^6 \approx 20$; take-home lesson: conta la complessità logaritmica, non la base ([[05-Insertion sort.pdf#page=33]]).

## Refusi e note

- Pagina del titolo: [[05-Insertion sort.pdf#page=1|1]].

- p. 5: pseudocodice in stile Cormen 2ª ed. (`do`, commento `//`), senza numeri di riga; la numerazione 1–8 del wiki segue la tabella di p. 17, dove il commento (riga 3) non ha costo — per questo mancano $c_3$ e la riga 3.
- p. 23: `void InsertionSort (vector<T> A)` riceve il vettore **per valore** e ordina una copia (🧩): serve `vector<T>& A`.
- p. 24: «Esercizio Libro di testo: 2.2.2» corrisponde all'esercizio 2.2-2 del Cormen. La traccia dice «per i primi $n-1$ elementi», mentre il codice di p. 25 cicla fino a $n$ (`i<n`): l'ultima iterazione è inutile ma innocua.
- pp. 26, 27, 29, 31: le domande («Dimostrarne la correttezza», «Valutare l'efficienza asintotica», «E la memoria?») non hanno soluzione nelle slide; nel wiki le risposte sono marcate 🧩.
- p. 33: «≈ 35» è $\lceil \log_{3/2} 10^6 \rceil = \lceil 34.07 \rceil$; una simulazione che scarta anche l'elemento interrogato dà 33 domande. Stesso ordine di grandezza.
- p. 2: parentesi chiusa di troppo nella definizione («$a'_n$)»).
- p. 31: a lezione il docente ha indicato che il `for` con `return` interno «non è ottimale per il calcolo della complessità» e va sostituito da un `while` che termini alla prima occorrenza. La versione ricostruita (🧩) e la sua analisi sono in [[findmatch]] § Versione alternativa con `while`.

## Concetti introdotti

[[insertion-sort]], [[selection-sort]], [[substring-pattern-matching]], [[findmatch]], [[logaritmi-nell-analisi]], [[potenza-veloce]]; aggiornati [[ordinamento]], [[invariante-di-ciclo]], [[casi-di-complessita]], [[efficienza-degli-algoritmi]], [[dominanza-asintotica]].

## Domande aperte

- Il caso medio di insertion sort non è trattato nelle slide (solo migliore e peggiore).
- La ricerca binaria è citata (pp. 32–33) ma il suo pseudocodice non è presentato: TODO alla lezione che la tratterà.
- «Trees» (p. 32): la domanda sull'altezza è posta per alberi con $d$ figli per livello; nel wiki la risposta $h = \log_d n$ è per un albero completo (🧩).

## Domande da esame

- Scrivere lo pseudocodice di insertion sort ed eseguirne la traccia su un array dato.
- Enunciare e dimostrare l'invariante di ciclo di insertion sort.
- Costruire la tabella dei costi e ricavare $T(n)$ nel caso migliore e peggiore; quali input li realizzano?
- Selection sort: invariante, perché fermarsi a $n - 1$, $\Theta$ nel caso migliore e peggiore, memoria.
- Complessità del pattern matching a forza bruta; istanza peggiore.
- Perché la base del logaritmo non conta asintoticamente? Quante moltiplicazioni richiede la potenza veloce?

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_
_Aggiornato: 2026-10-02 — versione alternativa con while (indicazione del docente a lezione)_
_Aggiornato: 2026-10-28 — aggiunto il «Percorso della lezione» (spostato dall'indice lezioni.md)_

<!-- nav:inizio -->
---
**Lezione 05 · pagina 1 di 7** · ← [[tracce-pila-e-coda|Tracce di operazioni su pila e coda (su array)]] · [[lezioni|Indice]] · [[insertion-sort|Insertion sort]] →
<!-- nav:fine -->
