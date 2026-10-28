---
tipo: entità
categoria: struttura-dati
fonti_pdf: ["04-Strutture dati elementari.pdf#page=10", "04-Strutture dati elementari.pdf#page=11", "04-Strutture dati elementari.pdf#page=12"]
---

# Array dinamico (raddoppio della capacità)

## Cos'è

> 📄 Fonte: [[04-Strutture dati elementari.pdf#page=10]]

Un array semplice non può cambiare dimensione durante l'esecuzione e allocarne uno enorme spreca spazio. Con gli **array dinamici** si parte da un array di **dimensione 1** e se ne **raddoppia** la dimensione da $m$ a $2m$ ogni volta che lo spazio finisce (allocando il nuovo array e ricopiando i vecchi elementi).

## Formule

> 🧮 Formula chiave: numero di raddoppi per $n$ elementi $= \lceil \log_2 n \rceil$ ([[04-Strutture dati elementari.pdf#page=10]]); spostamenti totali
$$ M = \sum_{i=1}^{\lg n} i \cdot \frac{n}{2^i} = n \sum_{i=1}^{\lg n} \frac{i}{2^i} \le n \sum_{i=1}^{\infty} \frac{i}{2^i} = 2n $$

(formula di [[04-Strutture dati elementari.pdf#page=11]])

Simboli: $n$ = elementi inseriti; $m$ = capacità corrente; $M$ = numero totale di spostamenti (copie) di elementi.

## Derivazioni

### Derivazione — numero di raddoppi $\lceil \lg n \rceil$
**Fonte:** [[04-Strutture dati elementari.pdf#page=10]] («Only $\lceil \log_2 n \rceil$»)

$$
\begin{aligned}
&\text{capacità dopo } k \text{ raddoppi} = 2^k && \text{si parte da } 1 = 2^0 \\
&\text{servono } k \text{ raddoppi con } 2^k \ge n \text{ e } 2^{k-1} < n && k \text{ minimo} \\
&\iff k \ge \lg n \ \text{ e } \ k - 1 < \lg n \iff k = \lceil \lg n \rceil && \text{prendo } \lg \text{ (crescente)}
\end{aligned}
$$

### Derivazione — lavoro totale $M \le 2n$
**Fonte:** [[04-Strutture dati elementari.pdf#page=11]] — «If half the elements move once, a quarter of the elements twice, and so on»

$$
\begin{aligned}
M &= \sum_{i=1}^{\lg n} i \cdot \frac{n}{2^i} && \frac{n}{2^i} \text{ elementi spostati } i \text{ volte} \\
  &= n \sum_{i=1}^{\lg n} \frac{i}{2^i} && n \text{ non dipende da } i \\
  &\le n \sum_{i=1}^{\infty} \frac{i}{2^i} && \text{aggiungo termini positivi} \\
  &= n \cdot \frac{1/2}{(1 - 1/2)^2} = 2n && \textstyle\sum_{i\ge1} i x^i = \frac{x}{(1-x)^2},\ x = \tfrac12
\end{aligned}
$$

> 🧩 Derivazione mia — la serie $\sum_{i \ge 1} i x^i$ per $|x| < 1$: derivando $\sum_{i\ge0} x^i = \frac{1}{1-x}$ si ha $\sum_{i \ge 1} i x^{i-1} = \frac{1}{(1-x)^2}$; moltiplicando per $x$: $\sum_{i\ge1} i x^i = \frac{x}{(1-x)^2}$. Con $x = 1/2$: $\frac{1/2}{1/4} = 2$.

> 🧩 Conteggio alternativo (stesso limite): i raddoppi avvengono a capacità $1, 2, 4, \dots, 2^{k-1}$ e ricopiano ogni volta tutti gli elementi presenti, quindi le copie totali sono $1 + 2 + \dots + 2^{k-1} = 2^k - 1$ con $k = \lceil \lg n\rceil$, e $2^k - 1 < 2n$ perché $2^{k-1} < n$.

**Sanity check** ([[strutture_elementari.py]]): $n = 1000$ → 10 raddoppi, 1023 copie $\le 2000$; $n = 1025$ → 11 raddoppi, 2047 copie $\le 2050$ (caso quasi peggiore: appena superata una potenza di 2); $n = 10^6$ → 20 raddoppi, 1 048 575 copie.

![[04-strutture-dati-p11-array-dinamico-lavoro-totale.png]]

**Conclusione della fonte:** ognuno degli $n$ elementi si sposta **in media solo due volte**, e il lavoro totale di gestione dell'array dinamico è lo stesso $O(n)$ di un array semplice. «Geometric series convergence is the free lunch of algorithm analysis.» ([[04-Strutture dati elementari.pdf#page=11]])

![[grafico-array-dinamico.svg]]
> 🧩 Grafico generato da me: le copie totali (a gradini, un salto a ogni raddoppio in $n = 2^k + 1$) restano sempre sotto la retta $2n$ di p. 11.

## Nota: «free lunch» e teorema *no free lunch*

> 📄 Fonte: [[04-Strutture dati elementari.pdf#page=12]]

Nel contesto della complessità computazionale e dell'ottimizzazione, il teorema **«no free lunch» (NFL)** afferma che, per certi tipi di problemi matematici, il costo computazionale per trovare una soluzione, **mediato su tutti i problemi della classe**, è lo stesso per qualsiasi metodo di soluzione. Il nome allude al detto «no such thing as a free lunch»: nessun metodo offre una «scorciatoia». La slide lo accosta per contrasto al «free lunch» della serie geometrica.

## Connessioni

- [[array]] — la struttura di base
- [[notazione-asintotica]] — $M = O(n)$
- [[strutture-contigue-e-collegate]] — alternativa alla lista quando serve crescere

## Fonti

- [[lezione-04-strutture-dati-elementari]]
- [[04-Strutture dati elementari.pdf#page=10]], [[04-Strutture dati elementari.pdf#page=11]], [[04-Strutture dati elementari.pdf#page=12]]

_Aggiornato: 2026-09-26 — ingest 04-Strutture dati elementari.pdf_

<!-- nav:inizio -->
---
**Lezione 04 · pagina 5 di 9** · ← [[array|Array]] · [[lezioni|Indice]] · [[lista-concatenata|Lista concatenata (semplice e doppia)]] →
<!-- nav:fine -->
