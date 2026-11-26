---
tipo: concetto
importanza_esame: alta
prerequisiti: ["tempo-di-esecuzione", "iterazione-e-ricorsione"]
fonti_pdf: ["03-Analisi di algoritmi.pdf#page=30", "03-Analisi di algoritmi.pdf#page=31", "03-Analisi di algoritmi.pdf#page=32", "03-Analisi di algoritmi.pdf#page=33", "06-Merge Sort (1).pdf#page=29"]
---

# Equazioni di ricorrenza (costo degli algoritmi ricorsivi)

## Definizione · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=30|p. 30]] · Merge Sort [[06-Merge Sort (1).pdf#page=31|p. 29]]

Un programma ricorsivo viene richiamato più volte su una versione ridotta del problema. Il **costo complessivo** $T(n)$ è dato dalla **somma dei costi delle singole chiamate**, con $T(0)$ pari al costo del passo ricorsivo più interno (quello in cui la funzione non viene richiamata ulteriormente).

Il costo si esprime quindi con un'**equazione di ricorrenza**: $T(n)$ definito in funzione di $T$ su valori più piccoli, più un caso base.

Una **ricorrenza** è un'equazione o **disequazione** che descrive una funzione in termini del suo valore su ingressi di dimensione inferiore. Il tempo di esecuzione di algoritmi ricorsivi è solitamente espresso mediante una ricorrenza, ad esempio per [[merge-sort]]:
$$ T(n) = \begin{cases} \Theta(1) & \text{se } n = 1 \\ 2T(n/2) + \Theta(n) & \text{altrimenti} \end{cases} $$
Vedremo tre metodi per risolvere una ricorrenza: [[metodo-di-sostituzione]], [[metodo-albero-di-ricorrenza]], metodo dell'esperto ([[teorema-dell-esperto]]).

## Formule · [[03-Analisi di algoritmi.pdf#page=31|p. 31]], [[03-Analisi di algoritmi.pdf#page=32|32]]

Per [[somma-ricorsiva]]:
- $T(0)$: un confronto e un return ⇒ **1**
- $T(i)$, con $0 < i \le n$: una chiamata ricorsiva con argomento $i - 1$, una somma, un return ⇒ $T(i) = T(i-1) + c$

> 🧮 Formula chiave:
$$ T(n) = \begin{cases} 1 & n = 0 \\ T(n-1) + c & n > 0 \end{cases} \qquad \Longrightarrow \qquad T(n) = 1 + c\,n = O(n) $$

Simboli: $T(n)$ = passi per l'input $n$; $c$ = costo costante del lavoro di una chiamata non base (confronto, somma, return, chiamata).

## Derivazioni

### Derivazione — soluzione per sostituzione iterata (srotolamento) · [[03-Analisi di algoritmi.pdf#page=33|p. 33]]
**Fonte:** «$T(n) = T(n-1) + c = T(n-2) + 2c = T(n-3) + 3c = \dots = T(0) + n\cdot c = 1 + c\cdot n = O(n)$»

$$
\begin{aligned}
T(n) &= T(n-1) + c && \text{ricorrenza con } i = n \\
     &= \big(T(n-2) + c\big) + c = T(n-2) + 2c && \text{ricorrenza con } i = n-1 \\
     &= T(n-3) + 3c && \text{ricorrenza con } i = n-2 \\
     &\ \ \vdots \\
     &= T(n-k) + k\,c && \text{forma generale dopo } k \text{ passi} \\
     &= T(0) + n\,c && k = n \text{: si raggiunge il caso base} \\
     &= 1 + c\,n && T(0) = 1 \\
     &= O(n) && \text{(anzi } \Theta(n)\text{, perché } c > 0\text{)}
\end{aligned}
$$

> 🧩 Derivazione mia — verifica della forma generale per induzione su $k$: vale per $k = 1$; se $T(n) = T(n-k) + kc$ e $n - k > 0$, applicando la ricorrenza a $T(n-k)$ si ha $T(n) = T(n-k-1) + c + kc = T(n-(k+1)) + (k+1)c$. Senza questa verifica il «$\vdots$» è solo un'intuizione.

**Sanity check:** $n = 0 \Rightarrow T = 1$ ✓ (solo caso base); $n = 1 \Rightarrow T = 1 + c$ (una chiamata non base + caso base) ✓. Con $c = 1$, [[somma_primi_n.py]] conta $T(n) = n + 1$ per $n \in \{0,1,2,5,10,100\}$.
**Ipotesi:** costo di ogni chiamata non base costante (niente copie di dati dipendenti da $n$).

![[03-analisi-algoritmi-p33-ricorrenza-somma-ricorsiva.png]]

## Spiegazione · [[03-Analisi di algoritmi.pdf#page=35|p. 35]]

La struttura della ricorrenza ricalca quella dell'algoritmo: il caso base dell'algoritmo dà il caso base di $T$, la chiamata ricorsiva dà il termine $T(n-1)$, il lavoro «locale» dà il termine $c$. La stessa struttura regge la [[correttezza-per-induzione]].

La domanda «E la complessità spaziale?» ha risposta $\Theta(n)$ (🧩, profondità della ricorsione) → [[tempo-di-esecuzione]].

### Ricorrenze divide et impera (lezioni 06–07) · Merge Sort [[06-Merge Sort (1).pdf#page=26|p. 24]] · Quicksort [[07-Quicksort 1.pdf#page=14|p. 14]]

Per un algoritmo [[divide-et-impera]] la ricorrenza ha la forma $T(n) = aT(n/b) + D(n) + C(n)$, con caso banale $\Theta(1)$. Lo srotolamento usato sopra funziona bene quando la dimensione cala di 1; quando cala di un **fattore** $b$ si usano:
- il [[metodo-albero-di-ricorrenza]], per trovare una soluzione di tentativo sommando i costi livello per livello;
- il [[metodo-di-sostituzione]], per verificarla per induzione con costanti esplicite;
- il [[teorema-dell-esperto]], che dà la soluzione direttamente se $f(n)$ ricade in uno dei tre casi.

> 🧩 Le ricorrenze con $n - 1$ si incontrano ancora: il caso peggiore di [[quicksort]], $T(n) = T(n-1) + \Theta(n) = \Theta(n^2)$ (serie aritmetica), e la [[torre-di-hanoi]], $M(n) = 2M(n-1) + 1 = 2^n - 1$ (serie geometrica). Per queste il teorema dell'esperto non si applica e si srotola come per [[somma-ricorsiva]].

## Perché importa

> 🎯 Esame: scrivere la ricorrenza di un algoritmo ricorsivo leggendo lo pseudocodice e risolverla srotolandola fino al caso base.

## Connessioni

- [[tempo-di-esecuzione]] — l'analogo per il codice iterativo
- [[divide-et-impera]] — la fonte principale di ricorrenze nel corso
- [[metodo-di-sostituzione]], [[metodo-albero-di-ricorrenza]], [[teorema-dell-esperto]] — i tre metodi di soluzione della lezione 06
- [[merge-sort]], [[quicksort]] — le ricorrenze dei due ordinamenti divide et impera
- [[risoluzione-ricorrenze]] — esercizi

## Fonti · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=30|p. 30]], [[03-Analisi di algoritmi.pdf#page=35|p. 35]] · Merge Sort [[06-Merge Sort (1).pdf#page=26|p. 24]], [[06-Merge Sort (1).pdf#page=31|p. 29]] · Quicksort [[07-Quicksort 1.pdf#page=14|p. 14]]

- [[lezione-03-analisi-di-algoritmi]], [[lezione-06-merge-sort]], [[lezione-07-quicksort]]

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_
_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf e 07-Quicksort.pdf_
_Aggiornato: 2026-10-10 — link ripuntati alla versione aggiornata delle slide 06-Merge Sort (1).pdf_
_Aggiornato: 2026-10-14 — link ripuntati alla versione aggiornata delle slide 07-Quicksort 1.pdf_

<!-- nav:inizio -->
---
**Lezione 03 · pagina 12 di 13** · ← [[analisi-del-costo-riga-per-riga|Analisi del costo riga per riga]] · [[lezioni|Indice]] · [[risoluzione-ricorrenze|Scrivere e risolvere equazioni di ricorrenza]] →
<!-- nav:fine -->
