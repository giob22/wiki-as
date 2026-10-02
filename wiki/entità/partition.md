---
tipo: entità
categoria: algoritmo
paradigma: "[[divide-et-impera]] (passo Divide di quicksort)"
fonti_pdf: ["07-Quicksort.pdf#page=5", "07-Quicksort.pdf#page=6", "07-Quicksort.pdf#page=7", "07-Quicksort.pdf#page=11", "07-Quicksort.pdf#page=12", "07-Quicksort.pdf#page=13"]
---

# Partition

Le sezioni seguono l'ordine delle slide: idea e quattro aree (pp. 5–6) → traccia passo per passo (pp. 7–11) → pseudocodice e costo (p. 12) → correttezza (p. 13).

## Problema risolto

> 📄 Fonte: [[07-Quicksort.pdf#page=3]]

È il passo **Divide** di [[quicksort]]: scelto un elemento $x$, detto **pivot**, partiziona l'array $A[p..r]$ in due sottoarray tali che $A[p..q-1]$ contiene gli elementi $\le x$ e $A[q+1..r]$ contiene gli elementi $> x$; il pivot va in $A[q]$.

- **Input:** array $A$, indici $p \le r$.
- **Output:** l'indice $q$; $A[p..r]$ riordinato come sopra.

## Idea

> 📄 Fonte: [[07-Quicksort.pdf#page=5]], [[07-Quicksort.pdf#page=6]]

La funzione Partition utilizza come pivot l'**ultimo elemento** del sottoarray ($x = A[r]$). Analizza, uno ad uno e a partire dal primo, tutti gli elementi compresi tra $p$ e $r - 1$, suddividendo il vettore in **quattro aree**:

| Area | Posizioni | Contenuto | Colore nelle slide |
|------|-----------|-----------|--------------------|
| 1ª | $p..i$ | elementi $\le$ del pivot | giallo |
| 2ª | $i+1..j-1$ | elementi $>$ del pivot | rosso |
| 3ª | $j..r-1$ | elementi non ancora analizzati | bianco |
| 4ª | $r$ | il pivot | — |

![[07-quicksort-p5-quattro-aree.png]]
*Le quattro aree separate da barriere: $i$ chiude la prima, $j$ apre la terza. ([[07-Quicksort.pdf#page=5]])*

L'elemento di posto $j$ (il primo non analizzato) viene confrontato con il pivot ([[07-Quicksort.pdf#page=6]]):
- se è **maggiore**, è sufficiente incrementare la barriera tra 2ª e 3ª area, ovvero incrementare $j$;
- se è **minore o uguale**, deve essere spostato nella prima area:
  - si incrementa $i$ (si sposta la barriera tra 1ª e 2ª area);
  - si scambia $A[i]$ con $A[j]$;
  - si incrementa $j$ (si sposta la barriera tra 2ª e 3ª area).

> 🧩 Spiegazione mia dello scambio: dopo $i \leftarrow i+1$, $A[i]$ è il **primo** elemento della 2ª area (un elemento $> x$), oppure è $A[j]$ stesso se la 2ª area è vuota. Scambiandolo con $A[j]$, l'elemento piccolo entra in coda alla 1ª area e quello grande passa in coda alla 2ª. La 2ª area «scorre» di una posizione senza dover spostare tutti i suoi elementi.

## Pseudocodice

> 📄 Fonte: [[07-Quicksort.pdf#page=12]] (riportato fedelmente, numeri di riga miei)

```
Partition (A,p,r)
1  x ← A[r]
2  i ← p-1
3  for j ← p to r-1
4      if A[j] ≤ x
5          i ← i+1
6          exchange A[i] ↔ A[j]
7  exchange A[i+1] ↔ A[r]
8  return i+1
```

![[07-quicksort-p12-pseudocodice-partition.png]]
*Pseudocodice e stato finale del ciclo (prima dello scambio della riga 7), con le barriere tra le aree. ([[07-Quicksort.pdf#page=12]])*

Simboli: $x$ = pivot; $i$ = ultima posizione della 1ª area (vale $p - 1$ quando l'area è vuota); $j$ = primo elemento non analizzato; `exchange` = scambio di due elementi; il valore restituito $i + 1$ è la posizione finale $q$ del pivot.

## Esempio di esecuzione

![[animazione-partition.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo sull'array delle slide 07 pp. 5–12, ⟨2, 8, 7, 1, 3, 5, 6, 4⟩ con pivot $x = 4$. I colori sono quelli delle slide (giallo $\le$ pivot, rosso $>$ pivot, bianco non analizzato, azzurro il pivot); si vedono i puntatori $i$ e $j$, il confronto $A[j] \le x$ e la riga di pseudocodice corrente.

> 📄 Fonte: [[07-Quicksort.pdf#page=7]]–[[07-Quicksort.pdf#page=11]]

Array iniziale $A[1..8] = \langle 2, 8, 7, 1, 3, 5, 6, 4 \rangle$, $p = 1$, $r = 8$, $x = A[8] = 4$. Inizialmente le due barriere (tra 1ª e 2ª area e tra 2ª e 3ª area) coincidono: $i = 0$, $j = 1$ ([[07-Quicksort.pdf#page=7]]).

| Slide | $j$ | $A[j]$ | $A[j] \le 4$? | Azione | $i$ dopo | $A$ dopo |
|-------|-----|--------|---------------|--------|----------|----------|
| [[07-Quicksort.pdf#page=7\|p. 7]] | 1 | 2 | sì | $i \leftarrow 1$, scambio $A[1] \leftrightarrow A[1]$ | 1 | ⟨2, 8, 7, 1, 3, 5, 6, 4⟩ |
| [[07-Quicksort.pdf#page=8\|p. 8]] | 2 | 8 | no | solo $j$ avanza | 1 | invariato |
| [[07-Quicksort.pdf#page=8\|p. 8]] | 3 | 7 | no | solo $j$ avanza | 1 | invariato |
| [[07-Quicksort.pdf#page=9\|p. 9]] | 4 | 1 | sì | $i \leftarrow 2$, scambio $A[2] \leftrightarrow A[4]$ | 2 | ⟨2, 1, 7, 8, 3, 5, 6, 4⟩ |
| [[07-Quicksort.pdf#page=10\|p. 10]] | 5 | 3 | sì | $i \leftarrow 3$, scambio $A[3] \leftrightarrow A[5]$ | 3 | ⟨2, 1, 3, 8, 7, 5, 6, 4⟩ |
| [[07-Quicksort.pdf#page=10\|p. 10]] | 6 | 5 | no | solo $j$ avanza | 3 | invariato |
| [[07-Quicksort.pdf#page=11\|p. 11]] | 7 | 6 | no | solo $j$ avanza | 3 | invariato |
| [[07-Quicksort.pdf#page=11\|p. 11]] | — | — | — | il ciclo è finito ($j = r$): scambio $A[i+1] \leftrightarrow A[r]$ | 3 | ⟨2, 1, 3, **4**, 7, 5, 6, 8⟩ |

Return $q = i + 1 = 4$: a sinistra ⟨2, 1, 3⟩ (tutti $\le 4$), a destra ⟨7, 5, 6, 8⟩ (tutti $> 4$). Verificato con [[divide_et_impera.py]].

![[07-quicksort-p7-partition-passo-1.png]]
*Passo 1: $A[1] = 2 \le 4$, $i$ e $j$ avanzano insieme. ([[07-Quicksort.pdf#page=7]])*

![[07-quicksort-p8-partition-passi-2-3.png]]
*Passi 2–3: 8 e 7 sono maggiori del pivot, avanza solo $j$ e la 2ª area cresce. ([[07-Quicksort.pdf#page=8]])*

![[07-quicksort-p9-partition-passo-4.png]]
*Passo 4: 1 ≤ 4, si incrementa $i$ e si scambia $A[2] \leftrightarrow A[4]$. ([[07-Quicksort.pdf#page=9]])*

![[07-quicksort-p10-partition-passi-5-6.png]]
*Passi 5–6: 3 entra nella 1ª area, 5 resta nella 2ª. ([[07-Quicksort.pdf#page=10]])*

![[07-quicksort-p11-partition-fine.png]]
*Passo 7 e fine: 6 > 4; ciclo finito, il pivot va in $A[i+1] = A[4]$. ([[07-Quicksort.pdf#page=11]])*

> 🧩 Osservazione mia sull'ultimo stato: l'8, che stava in $A[i+1]$ (primo della 2ª area), finisce in $A[r]$. Partition **non** ordina le due parti; le separa soltanto.

## Correttezza

> 📄 Fonte: [[07-Quicksort.pdf#page=13]]

**Invariante** — all'inizio di ogni iterazione del ciclo `for`:
1. $A[k] \le x$ per $p \le k \le i$;
2. $A[k] > x$ per $i + 1 \le k \le j - 1$;
3. $A[k] = x$ se $k = r$.

- **Inizializzazione** — vero prima della prima iterazione ($i = p - 1$ e $j = p$) perché la 1ª e la 2ª area sono entrambe vuote.
- **Conservazione** — il ciclo conserva l'invariante.
- **Conclusione** — al termine ($j = r$), l'array è suddiviso in tre insiemi: elementi minori o uguali al pivot, pivot, elementi maggiori del pivot.

![[07-quicksort-p13-invariante-partition.png]]

> 🧩 Derivazione mia — la conservazione (la slide la enuncia senza dimostrarla), nei due casi di [[07-Quicksort.pdf#page=6]]:
> - **$A[j] > x$:** si incrementa solo $j$. La 1ª area non cambia; la 2ª area diventa $A[i+1..j]$ e il nuovo elemento $A[j]$ è $> x$: la condizione 2 vale per $j + 1$.
> - **$A[j] \le x$:** $i \leftarrow i + 1$ e scambio $A[i] \leftrightarrow A[j]$. Ora $A[i] \le x$, quindi la condizione 1 vale fino al nuovo $i$. Se la 2ª area era non vuota, il vecchio $A[i]$ (il suo primo elemento, $> x$) è finito in $A[j]$, in coda alla 2ª area, che diventa $A[i+1..j]$: la condizione 2 vale per $j + 1$. Se era vuota, $i = j$ e lo scambio non fa nulla.
> - In entrambi i casi $A[r]$ non viene toccato ($j \le r - 1$): la condizione 3 resta vera.
>
> **Conclusione completa:** con $j = r$ l'invariante dice $A[p..i] \le x$, $A[i+1..r-1] > x$, $A[r] = x$. La riga 7 scambia $A[i+1]$ (primo elemento $> x$, oppure il pivot stesso se $i + 1 = r$) con il pivot. Con $q = i + 1$: $A[p..q-1] \le x$, $A[q] = x$, $A[q+1..r] > x$. È la specifica del Divide di [[07-Quicksort.pdf#page=3]].
>
> **Terminazione:** $j$ va da $p$ a $r - 1$: esattamente $r - p$ iterazioni (variante $r - j$).

## Complessità

> 📄 Fonte: [[07-Quicksort.pdf#page=12]]

Il tempo di esecuzione è $\Theta(n)$, con $n = r - p + 1$: $n$ iterazioni, ciascuna delle quali impiega un tempo costante.

### Derivazione — Partition è $\Theta(n)$
**Si parte da:** [[tempo-di-esecuzione]] — costo × numero di esecuzioni per riga

> 🧩 Derivazione mia (sia $m$ il numero di elementi di $A[p..r-1]$ che sono $\le x$, con $0 \le m \le n - 1$):

| Riga | Costo | Esecuzioni |
|------|-------|------------|
| 1, 2 | $c_1$, $c_2$ | 1 |
| 3 | $c_3$ | $(r - p) + 1 = n$ |
| 4 | $c_4$ | $n - 1$ |
| 5, 6 | $c_5$, $c_6$ | $m$ |
| 7, 8 | $c_7$, $c_8$ | 1 |

$$
\begin{aligned}
T(n) &= c_1 + c_2 + c_3 n + c_4(n-1) + (c_5 + c_6)m + c_7 + c_8 && \text{somma riga per riga} \\
T(n) &\ge c_3 n + c_4(n-1) = \Omega(n) && m = 0 \text{ (nessun elemento} \le x\text{)} \\
T(n) &\le (c_3 + c_4 + c_5 + c_6)\, n + (c_1 + c_2 + c_7 + c_8) = O(n) && m \le n - 1 \le n \\
T(n) &= \Theta(n) && \text{entrambi i limiti}
\end{aligned}
$$

La slide conta «$n$ iterazioni»: precisamente il corpo del `for` si esegue $n - 1$ volte e il test $n$ volte; non cambia l'ordine di grandezza.

**Sanity check:** nella traccia $n = 8$, 7 confronti $A[j] \le x$, $m = 3$ scambi nel ciclo più quello finale.

**Spazio:** $\Theta(1)$ — solo $x$, $i$, $j$: Partition lavora **sul posto** (🧩, da cui «Ordina sul posto» di [[07-Quicksort.pdf#page=2]]).

## Proprietà

- **Sul posto** (🧩 derivabile dallo pseudocodice).
- **Non stabile** — 🧩 derivabile: gli scambi spostano il primo elemento della 2ª area in fondo, scavalcando i suoi uguali. Ad esempio con ⟨$5_a$, $5_b$, 3⟩ e pivot 3: il ciclo non scambia nulla, la riga 7 scambia $A[1] = 5_a$ con $A[3]$ e si ottiene ⟨3, $5_b$, $5_a$⟩.

## Connessioni

- [[quicksort]] — Partition è il suo Divide; la posizione $q$ restituita decide il bilanciamento
- [[quicksort-randomizzato]] — Randomized-Partition sceglie il pivot a caso e poi chiama Partition
- [[nuts-and-bolts]] — la soluzione randomizzata è Partition applicata due volte
- [[merge]] — l'altra procedura lineare del divide et impera, ma nel Combine e non sul posto
- [[invariante-di-ciclo]] — invariante con tre condizioni (le aree)
- [[dimostrazioni-di-correttezza]] — esercizi

## Fonti

- [[lezione-07-quicksort]]
- [[07-Quicksort.pdf#page=3]], [[07-Quicksort.pdf#page=5]]–[[07-Quicksort.pdf#page=13]]

_Aggiornato: 2026-10-01 — ingest 07-Quicksort.pdf_
