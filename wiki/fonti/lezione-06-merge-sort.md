---
tipo: fonte
titolo: "Corso di Algoritmi e Strutture Dati — Progettazione di algoritmi: Divide et Impera (Merge Sort)"
file_raw: "06-Merge Sort.pdf"
pagine: "1-30"
data_ingest: 2026-10-01
formato: slide-pdf
argomenti: [divide et impera, torre di hanoi, merge sort, merge, ricorrenze, metodo di sostituzione, albero di ricorrenza, teorema dell'esperto, massimo sottoarray]
---

# Lezione 06 — Divide et impera: Merge Sort (06-Merge Sort.pdf)

## Sommario

Slide del Prof. Marrone, a.a. 26/27, intitolate «Progettazione di algoritmi – Divide et Imera» ([[06-Merge Sort.pdf#page=1]]). La lezione si apre con lo «Stop & Think» della **Torre di Hanoi**, posto e mostrato con la sequenza di mosse per tre dischi. Presenta poi **merge sort**: idea divide et impera, albero delle divisioni e fusioni su un esempio di 11 elementi, la funzione **Merge** con sentinelle (pseudocodice, traccia, invariante e costo lineare) e la procedura **Merge-Sort**. L'analisi introduce la ricorrenza generale del divide et impera $aT(n/b) + D(n) + C(n)$ e la risolve per merge sort con l'albero di ricorsione: $\Theta(n\lg n)$. Dopo uno «Stop & Think» sul **massimo sottoarray** (solo rimando al libro), la seconda metà è dedicata ai tre metodi per risolvere le ricorrenze: **sostituzione** (con il problema dei casi base), **albero di ricorrenza** (esempio $3T(n/4) + cn^2$ verificato per sostituzione) e **teorema dell'esperto** (tre casi, quattro esempi, uno dei quali cade nel gap).

## Punti chiave

1. S&T Torre di Hanoi: problema, figura dei pioli e dei dischi, sequenza di 7 mosse per 3 dischi ([[06-Merge Sort.pdf#page=2]]–[[06-Merge Sort.pdf#page=4]]) → [[torre-di-hanoi]].
2. Merge sort: divide in due metà, ordina ricorsivamente fino a lunghezza 1, combina con Merge; non ordina sul posto ([[06-Merge Sort.pdf#page=6]]) → [[merge-sort]].
3. Albero di divisioni e fusioni su ⟨5, 2, 8, 0, 4, 7, 1, 9, 3, 2, 6⟩ ([[06-Merge Sort.pdf#page=7]]).
4. Merge con array ausiliari $L$, $R$ e sentinelle $\infty$; traccia su ⟨2, 4, 5, 7⟩ + ⟨1, 2, 3, 6⟩ ([[06-Merge Sort.pdf#page=8]], [[06-Merge Sort.pdf#page=9]]) → [[merge]].
5. Invariante di Merge: $A[p..k-1]$ contiene i $k - p$ elementi più piccoli di $L$ e $R$, ordinati; $L[i]$, $R[j]$ minimi non ricopiati ([[06-Merge Sort.pdf#page=10]], [[06-Merge Sort.pdf#page=11]]) → [[invariante-di-ciclo]].
6. Merge costa tempo proporzionale a $n = n_1 + n_2$ ([[06-Merge Sort.pdf#page=12]]).
7. Pseudocodice di Merge-Sort, invocato come `Merge-Sort(A,1,n)` ([[06-Merge Sort.pdf#page=13]]).
8. Ricorrenza del divide et impera con $\Theta(1)$, $D(n)$, $C(n)$, $a$, $1/b$; per merge sort $D = \Theta(1)$, $C = \Theta(n)$, $a = b = 2$ ([[06-Merge Sort.pdf#page=14]]) → [[divide-et-impera]].
9. Albero di ricorsione di $2T(n/2) + cn$: $\lg n + 1$ livelli da $cn$, totale $cn\lg n + cn = \Theta(n\lg n)$ ([[06-Merge Sort.pdf#page=15]]).
10. S&T Problema del massimo sottoarray, capitolo 4.1 del libro ([[06-Merge Sort.pdf#page=16]]) → [[massimo-sottoarray]].
11. Ricorrenza: equazione o disequazione che descrive una funzione tramite i suoi valori su ingressi più piccoli; tre metodi ([[06-Merge Sort.pdf#page=17]]) → [[equazioni-di-ricorrenza]].
12. Metodo di sostituzione su $2T(\lfloor n/2 \rfloor) + n$: $T(n) \le cn\lg n$ con $c \ge 2$, casi base $T(2) = 4$ e $T(3) = 5$; perché due casi base ([[06-Merge Sort.pdf#page=18]]–[[06-Merge Sort.pdf#page=20]]) → [[metodo-di-sostituzione]].
13. Albero di ricorrenza di $3T(n/4) + cn^2$: $\log_4 n$, $3^i$ nodi, somma $< \frac{16}{13}cn^2 + \Theta(n^{\log_4 3})$; verifica con $d \ge \frac{16}{13}c$; anche $\Omega(n^2)$ ([[06-Merge Sort.pdf#page=21]]–[[06-Merge Sort.pdf#page=27]]) → [[metodo-albero-di-ricorrenza]].
14. Teorema dell'esperto: tre casi, osservazioni sul gap ([[06-Merge Sort.pdf#page=28]]) → [[teorema-dell-esperto]].
15. Esempi: $9T(n/3) + n$ (caso 1), $T(2n/3) + 1$ (caso 2), $3T(n/4) + n\lg n$ (caso 3), $2T(n/2) + n\lg n$ (gap) ([[06-Merge Sort.pdf#page=29]], [[06-Merge Sort.pdf#page=30]]).

## Refusi e note

- p. 1: «Divide et **Imera**» per «Impera». Il file si chiama «Merge Sort» ma copre l'intero paradigma divide et impera e i metodi per le ricorrenze.
- Le pagine [[06-Merge Sort.pdf#page=5|5]] (titolo «Merge Sort») e [[06-Merge Sort.pdf#page=16|16]] (titolo dello S&T) sono solo titoli. Le pagine 3, 4, 7, 12, 15, 20 e 25 hanno il contenuto solo come figura: è trascritto nelle pagine del wiki, con l'immagine accanto.
- p. 8: le slide ripetono i punti di p. 6 accanto allo pseudocodice di Merge.
- pp. 8, 9, 12: pseudocodice in stile Cormen 2ª ed. (`do`, `then`, `//`, assegnamenti multipli), diverso dalle [[pseudocodice|convenzioni del corso]]: segnalato in [[merge]].
- p. 19: la slide scrive «assumiamo vero per ⌊n/2⌋», e il testo estratto del PDF mostra parentesi sbagliate (⌊n/2⌊); nella figura sono corrette. Lo stesso a p. 26 per ⌊n/4⌋.
- p. 22: la ricorrenza è data con $\lfloor n/4 \rfloor$, l'albero è costruito senza parti intere (approssimazione dichiarata nella slide).
- p. 26: per $n = 2, 3$ si ha $\lfloor n/4 \rfloor = 0$: oltre a $T(1)$ servono anche questi casi base (🧩, in [[metodo-albero-di-ricorrenza]]).
- p. 29: «$\epsilon \approx 0{,}2$» viene da $1 - \log_4 3 \approx 0.207$.
- Le slide non danno l'algoritmo per la Torre di Hanoi né la correttezza di Merge-Sort: nel wiki sono marcati 🧩.

## Concetti introdotti

[[merge]], [[merge-sort]], [[torre-di-hanoi]], [[massimo-sottoarray]], [[metodo-di-sostituzione]], [[metodo-albero-di-ricorrenza]], [[teorema-dell-esperto]], [[progettazione-divide-et-impera]]; aggiornati [[divide-et-impera]], [[equazioni-di-ricorrenza]], [[ordinamento]], [[invariante-di-ciclo]], [[efficienza-degli-algoritmi]].

## Domande aperte

- Il massimo sottoarray è solo annunciato (p. 16): soluzione da cercare nel libro (Cormen §4.1) o in una lezione successiva.
- La dimostrazione del teorema dell'esperto non è nelle slide.
- Le slide non trattano lo spazio di merge sort oltre a «non sul posto»: nel wiki $\Theta(n)$ è una mia derivazione.

## Domande da esame

- Scrivere Merge e Merge-Sort; eseguire la traccia di Merge su due sequenze date.
- Enunciare e dimostrare l'invariante di Merge; a che servono le sentinelle?
- Scrivere la ricorrenza di merge sort ($D$, $C$, $a$, $b$) e risolverla con l'albero di ricorsione.
- Dimostrare per sostituzione che $2T(\lfloor n/2 \rfloor) + n = O(n\lg n)$; perché servono due casi base?
- Risolvere $3T(n/4) + cn^2$ con l'albero e verificare per sostituzione.
- Enunciare il teorema dell'esperto e applicarlo; mostrare una ricorrenza nel gap.
- Torre di Hanoi: algoritmo ricorsivo e numero di mosse.

_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf_
