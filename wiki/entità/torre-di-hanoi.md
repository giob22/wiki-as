---
tipo: entità
categoria: problema
paradigma: "[[divide-et-impera]] (soluzione ricorsiva)"
fonti_pdf: ["06-Merge Sort.pdf#page=2", "06-Merge Sort.pdf#page=3", "06-Merge Sort.pdf#page=4"]
---

# Torre di Hanoi

Problema «Stop & Think» che apre la lezione sul divide et impera ([[06-Merge Sort.pdf#page=2]]). Le slide danno il problema e la sequenza di mosse per tre dischi, **senza** algoritmo: la soluzione ricorsiva e la sua analisi sono mie (🧩).

## Definizione formale

> 📄 Fonte: [[06-Merge Sort.pdf#page=2]], [[06-Merge Sort.pdf#page=3]]

La slide rimanda all'esercizio interattivo di Khan Academy «move three disks in Towers of Hanoi» (link in [[06-Merge Sort.pdf#page=2]]). La figura di p. 3 mostra tre pioli (*Tower*) e una pila di dischi (*Disks*) di dimensione decrescente, dal più grande (*Largest*) in basso al più piccolo (*Smallest*) in alto.

![[06-merge-sort-p3-torre-di-hanoi.png]]

> 📚 Fonte esterna (regole del gioco, non scritte nelle slide; sono quelle dell'esercizio Khan Academy citato a p. 2):
> - **Input:** $n$ dischi impilati sul piolo A dal più grande al più piccolo; pioli vuoti B e C.
> - **Output:** la sequenza di mosse che porta tutti i dischi su C.
> - **Vincoli:** si sposta un disco alla volta, il disco in cima a un piolo; un disco non va mai sopra un disco più piccolo.

## Sequenza delle mosse per tre dischi

> 📄 Fonte: [[06-Merge Sort.pdf#page=4]]

La slide mostra otto configurazioni numerate da 1 a 8: lo stato iniziale e i sette stati dopo ogni mossa.

![[06-merge-sort-p4-hanoi-mosse.png]]

> 🧩 Lettura mia della figura (dischi 1 = piccolo/arancio, 2 = medio/bianco, 3 = grande/verde):

| Stato | Mossa che lo produce | A | B | C |
|-------|----------------------|---|---|---|
| 1 | — | 3, 2, 1 | — | — |
| 2 | disco 1: A → C | 3, 2 | — | 1 |
| 3 | disco 2: A → B | 3 | 2 | 1 |
| 4 | disco 1: C → B | 3 | 2, 1 | — |
| 5 | disco 3: A → C | — | 2, 1 | 3 |
| 6 | disco 1: B → A | 1 | 2 | 3 |
| 7 | disco 2: B → C | 1 | — | 3, 2 |
| 8 | disco 1: A → C | — | — | 3, 2, 1 |

## Algoritmo ricorsivo

> 🧩 Soluzione mia (divide et impera). Per spostare $n$ dischi da A a C:
> 1. sposta i primi $n - 1$ dischi da A a B, usando C come appoggio (sottoproblema di dimensione $n - 1$);
> 2. sposta il disco $n$, il più grande, da A a C (ora C è vuoto e A ha solo lui);
> 3. sposta gli $n - 1$ dischi da B a C, usando A come appoggio.
>
> Nella tabella: le mosse 1–3 sono il passo 1 (due dischi da A a B), la mossa 4 è il passo 2, le mosse 5–7 sono il passo 3.

```
HANOI(n, da, a, via)
1  if n > 0
2      HANOI(n−1, da, via, a)
3      sposta disco n: da → a
4      HANOI(n−1, via, a, da)
```

Simboli: $n$ = numero di dischi da spostare (i più piccoli, numerati $1..n$); `da`, `a`, `via` = piolo di partenza, di arrivo e di appoggio. Per il problema della slide: `HANOI(3, A, C, B)`.

## Esempio di esecuzione

![[animazione-torre-di-hanoi.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero `HANOI(3, A, C, B)`: un fotogramma per mossa, con il contatore delle mosse, la chiamata ricorsiva che la esegue e la riga 3 evidenziata. Le sette mosse coincidono con la sequenza di [[06-Merge Sort.pdf#page=4]] (verificato anche in [[divide_et_impera.py]]).

## Correttezza

> 🧩 Derivazione mia — [[correttezza-per-induzione]] su $n$, con la post-condizione «i dischi $1..n$ passano da `da` ad `a` senza mai violare i vincoli, e i dischi più grandi di $n$ non vengono toccati»:
> - **Base** ($n = 0$): nessuna mossa.
> - **Passo:** per ipotesi induttiva la riga 2 porta $1..n-1$ su `via` senza toccare il disco $n$. Allora $n$ è in cima a `da`, e `a` non contiene dischi più piccoli di $n$ (sono tutti su `via`): la mossa della riga 3 è lecita. La riga 4, ancora per ipotesi induttiva, porta $1..n-1$ sopra $n$, che è più grande di tutti loro.
> - **Terminazione:** ogni chiamata ha $n - 1 < n$.

## Complessità

### Derivazione — numero di mosse $M(n) = 2^n - 1$
**Si parte da:** lo pseudocodice: due chiamate su $n - 1$ dischi più una mossa → [[equazioni-di-ricorrenza]]

> 🧩 Derivazione mia:

$$
\begin{aligned}
M(0) &= 0, \qquad M(n) = 2M(n-1) + 1 && \text{righe 2, 3, 4} \\
M(n) &= 2\big(2M(n-2) + 1\big) + 1 = 4M(n-2) + 2 + 1 && \text{ricorrenza su } n-1 \\
     &= 2^k M(n-k) + \textstyle\sum_{m=0}^{k-1} 2^m && \text{dopo } k \text{ passi} \\
     &= 2^n M(0) + (2^n - 1) && k = n,\ \text{serie geometrica } \textstyle\sum_{m=0}^{n-1} 2^m = 2^n - 1 \\
     &= 2^n - 1 = \Theta(2^n)
\end{aligned}
$$

**Sanity check:** $M(3) = 7$, come le sette mosse di [[06-Merge Sort.pdf#page=4]]; [[divide_et_impera.py]] conta 1, 3, 7, 15, 1023 mosse per $n = 1, 2, 3, 4, 10$.

> 🧩 Questo algoritmo è **esponenziale** pur essendo divide et impera: i due sottoproblemi hanno dimensione $n - 1$, non $n/2$. Ridurre la dimensione di una costante anziché di un fattore porta a $2^n$. È lo stesso contrasto tra ricorsione «$n - 1$» e «$n/2$» delle [[equazioni-di-ricorrenza]].

**Spazio:** profondità della ricorsione $n + 1$ ⇒ $\Theta(n)$ (🧩).

## Connessioni

- [[divide-et-impera]] — esempio introduttivo della lezione 06
- [[correttezza-per-induzione]] — la correttezza è un'induzione sul numero di dischi
- [[merge-sort]] — divide et impera con sottoproblemi dimezzati: $\Theta(n\lg n)$ invece di esponenziale
- [[progettazione-divide-et-impera]] — il problema come esercizio di progettazione

## Fonti

- [[lezione-06-merge-sort]]
- [[06-Merge Sort.pdf#page=2]]–[[06-Merge Sort.pdf#page=4]]

_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf_
