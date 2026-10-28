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

### Versione alternativa con `while` (indicazione del docente)

> 📄 Fonte: indicazione del docente a lezione, **non presente nel PDF**: il ciclo esterno `for` con `return` al suo interno non è ottimale per il calcolo della complessità; va sostituito con un `while` la cui condizione lo faccia terminare alla prima occorrenza di $p$.
> 🧩 Il codice qui sotto è una mia ricostruzione di questa indicazione (variabile `trovato` come flag di terminazione); righe numerate da me.

```c
int findmatch(char *p, char *t) {
1   int i,j;        /* counters */
2   int m, n;       /* string lengths */
3   int trovato=0;  /* 1 quando p e' stato trovato */
4   m = strlen(p);
5   n = strlen(t);
6   i = 0;
7   while ((i<=(n-m)) && (!trovato)) {
8       j=0;
9       while ((j<m) && (t[i+j]==p[j]))
10          j = j+1;
11      if (j == m) trovato = 1;
12      else i = i+1;
13  }
14  if (trovato) return(i);
15  return(-1);
}
```

Differenze rispetto alla versione del PDF:
- la riga 5 della versione originale (`for` su $i = 0, \dots, n-m$) diventa l'inizializzazione della riga 6 più il `while` della riga 7, la cui guardia contiene **anche** la condizione di arresto alla prima occorrenza (`!trovato`);
- il `return(i)` dentro il ciclo (riga 9 originale) diventa l'assegnamento `trovato = 1` (riga 11); il ciclo ha così un **solo punto di uscita**, la guardia, e la funzione restituisce il risultato dopo il ciclo (righe 14–15);
- l'incremento di $i$ (riga 12) avviene solo se non c'è occorrenza, così all'uscita $i$ è proprio la posizione trovata.

> 🧩 Le due versioni sono **equivalenti**: eseguono la stessa sequenza di confronti tra caratteri e restituiscono lo stesso valore (verificato su 2005 coppie $p$, $t$ con [[stringhe_e_logaritmi.py]]). Cambia solo come si scrive l'analisi: vedi «Complessità della versione con `while`» sotto. L'animazione qui sotto vale per entrambe.

## Esempio di esecuzione

![[animazione-findmatch.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo, sull'esempio di p. 30 ($p$ = abba, $t$ = aababba): il pattern scorre sotto il testo, ogni confronto di caratteri è verde se uguale e rosso se diverso, fino all'occorrenza in posizione 3 dopo 10 confronti. Ogni fotogramma riporta in basso il numero del passo e cosa succede.


Sull'esempio di [[05-Insertion sort.pdf#page=30]] ($p = abba$, $t = aababba$, $n = 7$, $m = 4$): la riga 5 prova $i = 0, 1, 2, 3$ (fino a $n - m = 3$); il `while` confronta 2, 3, 1 e 4 caratteri; a $i = 3$ si ha $j = m$ e la funzione restituisce 3. Tabella dei tentativi in [[substring-pattern-matching]].

## Correttezza

> 🧩 Derivazione mia: il ciclo esterno esamina in ordine **tutte** le posizioni in cui $p$ può iniziare restando dentro $t$ ($0 \le i \le n - m$); il `while` arriva a $j = m$ se e solo se $t[i+k] = p[k]$ per ogni $k = 0, \dots, m-1$. Quindi il primo $i$ restituito è la prima occorrenza, e $-1$ significa che non ce n'è nessuna. Il corto circuito di `&&` alla riga 7 evita di leggere $p[m]$ quando $j = m$.

> 🧩 Versione con `while`: **invariante** del ciclo esterno (riga 7) — all'inizio di ogni iterazione `trovato` $= 0$ e $p$ non compare in nessuna posizione $< i$.
> - **Inizializzazione:** $i = 0$, nessuna posizione precedente.
> - **Conservazione:** se il `while` interno arriva a $j = m$, $p$ compare in $i$ e si pone `trovato = 1` lasciando $i$ invariato; altrimenti $p$ non compare in $i$ e si passa a $i + 1$.
> - **Conclusione:** si esce perché `trovato` $= 1$ (allora $i$ è la **prima** occorrenza, per l'invariante) oppure perché $i > n - m$ (allora $p$ non compare in nessuna posizione ammissibile e si restituisce $-1$).
> - **Terminazione:** la funzione variante $v = (n - m + 1 - i) + (1 - \texttt{trovato})$ è $\ge 0$ e cala di 1 a ogni iterazione (o cresce $i$, o `trovato` passa da 0 a 1).

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

### Complessità della versione con `while`

> 🧩 Derivazione mia — perché il `while` rende l'analisi più pulita. Nelle tabelle costo × numero di esecuzioni ([[analisi-del-costo-riga-per-riga]], [[05-Insertion sort.pdf#page=17]]) si usa la regola «**la guardia di un ciclo viene valutata una volta in più delle iterazioni**». Nella versione con `for` la regola vale solo se $p$ **non** compare: se compare in posizione $q$, il `return` della riga 9 esce dal ciclo senza un ultimo test, e la guardia della riga 5 è valutata $q + 1$ volte, non $q + 2$; inoltre la riga 11 viene eseguita o no a seconda dell'esito. Con il `while` la regola vale **sempre**, perché l'unica uscita è la guardia.

Simboli: $k$ = numero di iterazioni del `while` esterno; $t_i$ = numero di test del `while` interno (riga 9) nell'iterazione con indice $i$ (stesso ruolo di $t_j$ in [[insertion-sort]]).

$$
k = \begin{cases} q + 1 & \text{se la prima occorrenza è in posizione } q \\ n - m + 1 & \text{se } p \text{ non compare} \end{cases}
\qquad\qquad 1 \le t_i \le m + 1
$$

($t_i = m + 1$ solo quando $p$ compare in $i$: $m$ test veri e quello con $j = m$; se c'è un carattere diverso, $t_i$ = caratteri uguali + 1.)

| Riga | Costo | Esecuzioni |
|------|-------|------------|
| 3–6 | $c_3, \dots, c_6$ | 1 (più il costo di `strlen`, righe 4–5) |
| 7 | $c_7$ | $k + 1$ |
| 8 | $c_8$ | $k$ |
| 9 | $c_9$ | $\sum_i t_i$ |
| 10 | $c_{10}$ | $\sum_i (t_i - 1)$ |
| 11 | $c_{11}$ | $k$ |
| 12 | $c_{12}$ | $k - 1$ se $p$ compare, $k$ altrimenti |
| 14 | $c_{14}$ | 1 |
| 15 | $c_{15}$ | 1 se $p$ non compare, 0 altrimenti |

$$
\begin{aligned}
T(n, m) &= a + b\,k + (c_9 + c_{10}) \sum_i t_i && \text{raccolgo: } a, b \text{ costanti} \\
T_{worst}(n, m) &\le a + b\,(n - m + 1) + (c_9 + c_{10})(n - m + 1)(m + 1) && k \le n - m + 1,\ t_i \le m + 1 \\
                &= O\big((n - m + 1)\,m\big) = O(nm) && m \ge 1 \\
T_{best}(n, m) &= a + b + (c_9 + c_{10})(m + 1) = \Theta(m) && p \text{ in posizione } 0\text{: } k = 1,\ t_0 = m + 1
\end{aligned}
$$

Sull'istanza peggiore della sezione precedente ($t = a^n$, $p = a^{m-1}b$): $k = n - m + 1$ e $t_i = m$ per ogni $i$, quindi $\sum_i t_i = (n - m + 1)\,m$ e il limite è raggiunto: $\Theta((n - m + 1)\,m)$, cioè $\Theta(n^2)$ per $m \approx n/2$. Stesso risultato della versione con `for`.

**Sanity check** ([[stringhe_e_logaritmi.py]]): istanza peggiore con $n = 1000$, $m = 500$: $k = 501$, test del `while` interno $= 250\,500 = (n - m + 1)\,m$; $p$ in posizione 0: $k = 1$, test $= m + 1$; esempio di p. 30: $k = 4$, 11 test (i 10 confronti di caratteri più il test finale con $j = m$).
**Ipotesi:** [[modello-ram]], confronto di caratteri in tempo costante; il costo di `strlen` (lineare in $n + m$) è a parte, come nella versione con `for`.

## Connessioni

- [[substring-pattern-matching]] — il problema
- [[tempo-di-esecuzione]], [[casi-di-complessita]] — il costo dipende sia da $n$ sia da $m$ e dall'istanza

## Fonti

- [[lezione-05-insertion-sort]]
- le stesse slide sono riprese nella versione aggiornata della lezione 06 ([[lezione-06-merge-sort]]): [[06-Merge Sort (1).pdf#page=45]], [[06-Merge Sort (1).pdf#page=46]]
- [[05-Insertion sort.pdf#page=30]], [[05-Insertion sort.pdf#page=31]]

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_
_Aggiornato: 2026-10-01 — aggiunta l'animazione dell'algoritmo_
_Aggiornato: 2026-10-02 — versione alternativa con while (indicazione del docente a lezione)_
_Aggiornato: 2026-10-10 — slide riprese nella versione aggiornata della lezione 06_

<!-- nav:inizio -->
---
**Lezione 05 · pagina 5 di 7** · ← [[substring-pattern-matching|Substring Pattern Matching (ricerca di una sottostringa)]] · [[lezioni|Indice]] · [[logaritmi-nell-analisi|L'importanza dei logaritmi]] →
<!-- nav:fine -->
