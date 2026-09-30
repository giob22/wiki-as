---
tipo: entità
categoria: algoritmo
paradigma: "forza bruta"
fonti_pdf: ["05-Insertion sort.pdf#page=31"]
---

# findmatch — pattern matching a forza bruta

## Problema risolto

[[substring-pattern-matching]]: trovare la posizione del pattern $p$ (lunghezza $m$) nel testo $t$ (lunghezza $n$).

## Idea

Provare **ogni posizione di partenza** $i$ del testo e confrontare carattere per carattere $t[i..i+m-1]$ con $p$, fermandosi al primo carattere diverso.

## Pseudocodice

> 📄 Fonte: [[05-Insertion sort.pdf#page=31]] (codice C riportato fedelmente; righe numerate da me)

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

## Esempio di esecuzione

![[animazione-findmatch.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo, sull'esempio di p. 30 ($p$ = abba, $t$ = aababba): il pattern scorre sotto il testo, ogni confronto di caratteri è verde se uguale e rosso se diverso, fino all'occorrenza in posizione 3 dopo 10 confronti. Ogni fotogramma riporta in basso il numero del passo e cosa succede.


Sull'esempio di [[05-Insertion sort.pdf#page=30]] ($p = abba$, $t = aababba$, $n = 7$, $m = 4$): la riga 5 prova $i = 0, 1, 2, 3$ (fino a $n - m = 3$); il `while` confronta 2, 3, 1 e 4 caratteri; a $i = 3$ si ha $j = m$ e la funzione restituisce 3. Tabella dei tentativi in [[substring-pattern-matching]].

## Correttezza

> 🧩 Derivazione mia: il ciclo esterno esamina in ordine **tutte** le posizioni in cui $p$ può iniziare restando dentro $t$ ($0 \le i \le n - m$); il `while` arriva a $j = m$ se e solo se $t[i+k] = p[k]$ per ogni $k = 0, \dots, m-1$. Quindi il primo $i$ restituito è la prima occorrenza, e $-1$ significa che non ce n'è nessuna. Il corto circuito di `&&` alla riga 7 evita di leggere $p[m]$ quando $j = m$.

## Complessità

> 📄 Fonte: [[05-Insertion sort.pdf#page=31]] — consegna «Valutare l'efficienza asintotica» (senza soluzione)

> 🧩 Derivazione mia:
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

## Connessioni

- [[substring-pattern-matching]] — il problema
- [[tempo-di-esecuzione]], [[casi-di-complessita]] — il costo dipende sia da $n$ sia da $m$ e dall'istanza

## Fonti

- [[lezione-05-insertion-sort]]
- [[05-Insertion sort.pdf#page=30]], [[05-Insertion sort.pdf#page=31]]

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_
_Aggiornato: 2026-10-01 — aggiunta l'animazione dell'algoritmo_
