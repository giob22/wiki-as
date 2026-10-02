---
tipo: concetto
importanza_esame: alta
prerequisiti: ["paradigmi-di-progettazione", "iterazione-e-ricorsione"]
fonti_pdf: ["03-Analisi di algoritmi.pdf#page=4", "06-Merge Sort.pdf#page=14", "07-Quicksort.pdf#page=3"]
---

# Divide et impera

## Definizione

> 📄 Fonte: [[03-Analisi di algoritmi.pdf#page=4]]

Gli algoritmi divide et impera **scompongono** il problema in sottoproblemi **simili e più piccoli**, li **risolvono** (spesso in modo ricorsivo) e **combinano** le soluzioni. Funzionano bene quando la divisione è naturale e il «merge» (la combinazione) è efficiente.

Schema: **divide → conquer → combine**, con **casi base** ben definiti.

## Spiegazione

Caratteristiche della soluzione ([[03-Analisi di algoritmi.pdf#page=4]]):
- spesso efficienti se la **partizione è bilanciata** (sottoproblemi di dimensione simile);
- buona **parallelizzabilità** dei sottoproblemi (sono indipendenti);
- **overhead** nel passo di combinazione; attenzione al **bilanciamento**.

Esempi classici citati: **ordinamento**, **ricerca**, «…».

> 🧩 Derivazione mia: la stima del costo di un algoritmo divide et impera porta naturalmente a un'[[equazioni-di-ricorrenza|equazione di ricorrenza]] (costo del problema = costo dei sottoproblemi + costo di divisione e combinazione), che è il motivo per cui la lezione 03 introduce le ricorrenze sul caso semplice di [[somma-ricorsiva]].

### La ricorrenza del divide et impera
> 📄 Fonte: [[06-Merge Sort.pdf#page=14]]

Per un approccio divide et impera, detti $\Theta(1)$ il tempo per risolvere il caso «banale», $D(n)$ il tempo per suddividere un problema, $C(n)$ il tempo per ricombinare le soluzioni dei sottoproblemi, $a$ il numero di sottoproblemi in cui si divide un problema e $1/b$ il fattore di riduzione della dimensione di un problema, la complessità è esprimibile in forma di ricorrenza:

> 🧮 Formula chiave:
$$
T(n) = \begin{cases} \Theta(1) & \text{nel caso banale } n = 1 \\ aT(n/b) + D(n) + C(n) & \text{altrimenti } (n > 1) \end{cases}
$$

Si risolve con i tre metodi della lezione 06: [[metodo-di-sostituzione]], [[metodo-albero-di-ricorrenza]], [[teorema-dell-esperto]] ([[06-Merge Sort.pdf#page=17]]).

### Gli esempi delle lezioni 06–07

| Algoritmo | Divide | Conquer | Combine | Ricorrenza | Costo |
|-----------|--------|---------|---------|------------|-------|
| [[merge-sort]] | calcolo del punto medio, $D(n) = \Theta(1)$ | 2 metà | [[merge]], $C(n) = \Theta(n)$ | $2T(n/2) + \Theta(n)$ | $\Theta(n\lg n)$ ([[06-Merge Sort.pdf#page=15]]) |
| [[quicksort]] | [[partition]] attorno al pivot, $\Theta(n)$ | 2 parti, anche sbilanciate | niente da fare ([[07-Quicksort.pdf#page=3]]) | da $2T(n/2) + \Theta(n)$ a $T(n-1) + \Theta(n)$ | da $\Theta(n\lg n)$ a $\Theta(n^2)$ |
| [[torre-di-hanoi]] (🧩) | — | 2 sottoproblemi di $n - 1$ dischi + 1 mossa | — | $2M(n-1) + 1$ | $2^n - 1$ mosse |
| [[nuts-and-bolts]] (🧩) | Partition dei bulloni e dei dadi | 2 sottoinsiemi | — | come quicksort randomizzato | $O(n\log n)$ atteso |

> 🧩 Dove sta il lavoro: in merge sort nel Combine, in quicksort nel Divide. La [[torre-di-hanoi]] mostra che il paradigma da solo non garantisce efficienza: con sottoproblemi di dimensione $n - 1$ invece di $n/2$ il costo diventa esponenziale. Lo stesso vale per il caso peggiore di quicksort, dove la partizione sbilanciata trasforma $\Theta(n\lg n)$ in $\Theta(n^2)$: è l'«attenzione al bilanciamento» di [[03-Analisi di algoritmi.pdf#page=4]].

Il [[massimo-sottoarray]] è posto come ulteriore problema nella lezione 06 ([[06-Merge Sort.pdf#page=16]]), con rimando al libro.

## Perché importa

È la prima tecnica di progettazione del programma ([[00-Presentazione.pdf#page=5]]).

## Connessioni

- [[paradigmi-di-progettazione]] — confronto con ricerca combinatoria ed euristiche
- [[iterazione-e-ricorsione]] — la forma ricorsiva rende il codice «spesso più chiaro per divide-et-impera» ([[03-Analisi di algoritmi.pdf#page=9]])
- [[correttezza-per-induzione]] — la correttezza di un algoritmo ricorsivo si prova per induzione
- [[equazioni-di-ricorrenza]] — strumento di analisi del costo
- [[merge-sort]], [[quicksort]], [[quicksort-randomizzato]] — gli algoritmi divide et impera delle lezioni 06–07
- [[teorema-dell-esperto]] — risolve direttamente $aT(n/b) + f(n)$
- [[progettazione-divide-et-impera]] — esercizi di progettazione (Torre di Hanoi, Nuts and Bolts)

## Fonti

- [[lezione-03-analisi-di-algoritmi]], [[lezione-06-merge-sort]], [[lezione-07-quicksort]]
- [[03-Analisi di algoritmi.pdf#page=4]], [[06-Merge Sort.pdf#page=14]], [[07-Quicksort.pdf#page=3]]

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_
_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf e 07-Quicksort.pdf_
