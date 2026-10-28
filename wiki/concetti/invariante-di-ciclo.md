---
tipo: concetto
importanza_esame: alta
prerequisiti: ["algoritmo-e-problema", "iterazione-e-ricorsione"]
fonti_pdf: ["03-Analisi di algoritmi.pdf#page=16", "03-Analisi di algoritmi.pdf#page=17"]
---

# Invariante di ciclo (correttezza degli algoritmi iterativi)

## Definizione

> 📄 Fonte: [[03-Analisi di algoritmi.pdf#page=16]]

Per gli algoritmi **iterativi** si usa l'approccio basato sull'**invariante di ciclo**: una proprietà delle variabili che vale a ogni iterazione. L'invariante dimostra la **correttezza parziale** in tre passi:

1. **Inizializzazione** — l'invariante vale prima della prima iterazione.
2. **Conservazione** — se vale all'inizio di un'iterazione, vale anche alla successiva.
3. **Conclusione** — quando la condizione di ciclo è falsa, invariante + condizione d'uscita ⇒ **post-condizione**.

Per la **correttezza totale** serve anche la **terminazione**: di solito si introduce una **funzione variante** (misura intera $\ge 0$) che diminuisce a ogni iterazione.

## Formule

> 🧩 Derivazione mia (schema formale): con invariante $P$, condizione del ciclo $B$, post-condizione $Q$ e variante $v$:
$$
\begin{aligned}
&\text{(1)}\ \ \{\text{pre}\}\ \text{inizializzazione}\ \Rightarrow P \\
&\text{(2)}\ \ P \wedge B\ \ \{\text{corpo}\}\ \Rightarrow P \\
&\text{(3)}\ \ P \wedge \neg B \Rightarrow Q \\
&\text{(T)}\ \ v \in \mathbb{N},\ \ v \text{ decresce strettamente a ogni iterazione}
\end{aligned}
$$
(T) garantisce che il ciclo esegua al più $v_{iniziale}$ iterazioni: una successione strettamente decrescente di naturali è finita.

## Derivazioni

### Derivazione — correttezza di [[somma-iterativa]]
**Fonte:** [[03-Analisi di algoritmi.pdf#page=17]]

```
funzione somma_iterativa(n)
1  s ← 0
2  per i da 1 a n
3      s ← s + i
4  ritorna s
```

**Invariante** (dalla slide): all'inizio dell'iterazione $i$, $\displaystyle s = \sum_{k=1}^{i-1} k$.

$$
\begin{aligned}
&\textbf{Inizializzazione:}\ \ i = 1,\ s = 0 = \sum_{k=1}^{0} k && \text{somma vuota} \\
&\textbf{Conservazione:}\ \ s = \sum_{k=1}^{i-1} k \ \xrightarrow{\ s \leftarrow s + i\ }\ s = \sum_{k=1}^{i-1} k + i = \sum_{k=1}^{i} k && \text{è l'invariante per } i+1 \\
&\textbf{Conclusione:}\ \ i = n + 1 \Rightarrow s = \sum_{k=1}^{n} k = 1 + 2 + \dots + n && \text{post-condizione} \\
&\textbf{Terminazione:}\ \ v = n - i + 1 \ge 0,\ \text{cala di 1 per iterazione; il ciclo esce quando } i > n
\end{aligned}
$$

> ⚠️ Contraddizione: la slide scrive «Inizializzazione: **i = 0**, s = 0 ⇒ vero», ma il ciclo parte da $i = 1$ e con $i = 0$ l'invariante darebbe $\sum_{k=1}^{-1} k$, non definita nel senso usuale. Il valore corretto è $i = 1$ (somma vuota = 0). Probabile refuso.

La slide indica come terminazione «$i > n$» (condizione d'uscita); la funzione variante $v = n - i + 1$ è mia (🧩), secondo lo schema di p. 16.

> **Sanity check:** [[somma_primi_n.py]] verifica l'invariante con un `assert` all'inizio di ogni iterazione, per $n \in \{0, 1, 2, 5, 10, 100\}$.

![[03-analisi-algoritmi-p17-invariante-somma-iterativa.png]]

## Spiegazione

L'invariante va scelto in modo che la **conclusione** dia esattamente la post-condizione: qui «$s$ contiene la somma dei numeri già visti», che a fine ciclo sono tutti. Conservazione e inizializzazione sono un'**induzione sul numero di iterazioni**: (1) è il caso base, (2) il passo induttivo.

## Perché importa

> 🎯 Esame: scrivere invariante, inizializzazione, conservazione, conclusione **e** terminazione per un ciclo dato. Senza terminazione si ha solo correttezza parziale.

## Connessioni

- [[correttezza-parziale-e-totale]] — l'invariante dà la correttezza **parziale**, la funzione variante la terminazione: insieme la **totale**
- [[insertion-sort]] — l'invariante di [[05-Insertion sort.pdf#page=16]] («$A[1..j-1]$ contiene gli elementi originali di $A[1..j-1]$, ordinati») è l'esempio canonico del metodo
- [[merge]] — invariante con due affermazioni: prefisso $A[p..k-1]$ ordinato e puntatori $i$, $j$ sui minimi rimasti ([[06-Merge Sort (1).pdf#page=19]])
- [[partition]] — invariante con tre condizioni, una per area ([[07-Quicksort 1.pdf#page=13]])
- [[selection-sort]] — invariante con due cicli annidati (esercizio 2.2.2, [[05-Insertion sort.pdf#page=26]])

- [[correttezza-per-induzione]] — l'analogo per la ricorsione, «simile nello spirito» ([[03-Analisi di algoritmi.pdf#page=18]])
- [[algoritmo-e-problema]] — le due condizioni della definizione di correttezza (uscita corretta, terminazione) corrispondono a conclusione e variante
- [[dimostrazioni-di-correttezza]] — esercizi

## Fonti

- [[lezione-03-analisi-di-algoritmi]]
- [[03-Analisi di algoritmi.pdf#page=16]], [[03-Analisi di algoritmi.pdf#page=17]]

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_
_Aggiornato: 2026-10-01 — collegamento a correttezza-parziale-e-totale_
_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf e 07-Quicksort.pdf_
_Aggiornato: 2026-10-10 — link ripuntati alla versione aggiornata delle slide 06-Merge Sort (1).pdf_
_Aggiornato: 2026-10-14 — link ripuntati alla versione aggiornata delle slide 07-Quicksort 1.pdf_

<!-- nav:inizio -->
---
**Lezione 03 · pagina 8 di 13** · ← [[correttezza-parziale-e-totale|Correttezza parziale e correttezza totale]] · [[lezioni|Indice]] · [[correttezza-per-induzione|Correttezza degli algoritmi ricorsivi (per induzione)]] →
<!-- nav:fine -->
