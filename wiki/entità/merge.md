---
tipo: entità
categoria: algoritmo
paradigma: "[[divide-et-impera]] (passo Combine di merge sort)"
fonti_pdf: ["06-Merge Sort (1).pdf#page=15", "06-Merge Sort (1).pdf#page=16", "06-Merge Sort (1).pdf#page=18", "06-Merge Sort (1).pdf#page=17", "06-Merge Sort (1).pdf#page=19", "06-Merge Sort (1).pdf#page=20", "06-Merge Sort (1).pdf#page=21"]
---

# Merge (fusione di sequenze ordinate)

Le sezioni seguono l'ordine delle slide: prima versione senza sentinelle (p. 15) → codice completo (p. 16) → esempio (p. 17) → correttezza (pp. 18–20) → complessità (p. 21).

## Problema risolto

> 📄 Fonte: [[06-Merge Sort (1).pdf#page=7]], [[06-Merge Sort (1).pdf#page=16]]

**Merge** combina due sottosequenze ordinate in una sequenza ordinata. È la prima delle «due funzioni» di [[merge-sort]]; l'altra, Merge-Sort, la invoca per ricombinare le metà ordinate.

- **Input:** un array $A$ e tre indici $p \le q < r$ tali che $A[p..q]$ e $A[q+1..r]$ sono **già ordinati**.
- **Output:** $A[p..r]$ contiene gli stessi elementi, **ordinati**.

> 🧩 Derivazione mia (pre-condizione resa esplicita): la slide non scrive l'ipotesi $p \le q < r$, ma è quella garantita da Merge-Sort, che la chiama solo con $p < r$ e $q = \lfloor (p+r)/2 \rfloor$ ([[06-Merge Sort (1).pdf#page=22]]). Così entrambe le metà sono non vuote: $n_1 \ge 1$ e $n_2 \ge 1$.

## Idea

> 🧩 Esempio mio per fissare l'idea: due mazzi di carte già ordinati, a faccia in su. A ogni passo si guarda la carta in cima a ciascun mazzo e si sposta la più piccola nel mazzo di uscita. Quando un mazzo finisce si prendono le carte rimaste nell'altro.

Lo pseudocodice della slide evita il controllo «un mazzo è finito?» con le **sentinelle**: in fondo a $L$ e $R$ mette $\infty$. Una sentinella non è mai minore di un elemento vero, quindi non viene scelta finché nell'altro array resta qualcosa.

## Prima versione (senza sentinelle)

> 📄 Fonte: [[06-Merge Sort (1).pdf#page=15]] (riportata fedelmente; numeri di riga miei)

Nel passaggio dalla prima versione di Merge-Sort a quella con gli indici (→ [[merge-sort]] § Dal primo pseudocodice alla versione con indici), la creazione di $L$ e $R$ viene **spostata da Merge-Sort a Merge**. Merge deve usare memoria accessoria per copiare i sotto-vettori, perché l'inserimento in $A$ è ora una **sovrascrittura** e senza copie si perderebbero elementi.

```
Merge(A, p, q, r)
1  copia A[p..q]   in L
2  copia A[q+1..r] in R
3  i ← 1
4  j ← 1
5  per k da p a r
6      se L[i] ≤ R[j]
7          A[k] ← L[i]
8          i ← i + 1
9      altrimenti
10         A[k] ← R[j]
11         j ← j + 1
```

- righe 1–2: **creazione effettiva di $L$ e $R$** (spostata da Merge-Sort a Merge);
- righe 5–11: **inserimento in ordine**, cioè «pop» da $L$ e $R$ e inserimento con sovrascrittura in $A$.

Qui nasce il «non in-place»: la memoria ausiliaria non serve solo per dividere, ma per fondere in modo semplice e sicuro.

![[06-merge-sort-p15-merge-semplificato.png]]

Annotazioni a mano: accanto alle righe 1–2 «faceva parte della fase discendente pre modifiche» (nella prima versione di Merge-Sort le copie si facevano dividendo, cioè in discesa); accanto al ciclo «fase ascendente».

> 🧩 Osservazione mia: questa versione non ha le sentinelle e non controlla se $L$ o $R$ sono finiti. Con $L = \langle 1, 2 \rangle$ e $R = \langle 3, 4 \rangle$, dopo due iterazioni $i = 3$ e il confronto della riga 6 leggerebbe $L[3]$, che non esiste. Il «codice completo» qui sotto risolve il problema con la sentinella $\infty$ in fondo a $L$ e $R$ (riga 8).

## Pseudocodice (codice completo)

> 📄 Fonte: [[06-Merge Sort (1).pdf#page=16]] (titolo «Merge: codice completo»; ripetuto in [[06-Merge Sort (1).pdf#page=17]] e [[06-Merge Sort (1).pdf#page=21]]); riportato fedelmente, numeri di riga miei

```
Merge (A,p,q,r)
1  n1 ← q-p+1
2  n2 ← r-q
3  // create L[1..n1+1] and R[1..n2+1]
4  for i ← 1 to n1
5      do L[i] ← A[p+i-1]
6  for j ← 1 to n2
7      do R[j] ← A[q+j]
8  L[n1+1] ← R[n2+1] ← ∞
9  i ← j ← 1
10 for k ← p to r
11     do if L[i] ≤ R[j]
12         then A[k] ← L[i]
13              i ← i+1
14         else A[k] ← R[j]
15              j ← j+1
```

Significato dei simboli:
- $n_1$, $n_2$ = lunghezze delle due metà $A[p..q]$ e $A[q+1..r]$; $n = n_1 + n_2 = r - p + 1$;
- $L$, $R$ = copie delle due metà, con una cella in più per la sentinella $\infty$;
- $i$, $j$ = indice del primo elemento di $L$ e di $R$ non ancora ricopiato in $A$;
- $k$ = posizione di $A$ da riempire.

Accanto al codice la slide ripete i punti dell'idea di merge sort e aggiunge ([[06-Merge Sort (1).pdf#page=16]]):
- **è una funzione iterativa!!** (Merge-Sort è ricorsiva, Merge no);
- **non** effettua un ordinamento sul posto: infatti non fa proprio ordinamento, ma piuttosto **inserisce elementi in $A$ in maniera ordinata**, prendendoli da $L$ e $R$.

![[06-merge-sort-p16-merge-codice-completo.png]]

> ⚠️ Contraddizione (di notazione): la slide usa `do`/`then`/`else` e il commento `//` (stile della 2ª edizione del Cormen), mentre le [[pseudocodice|convenzioni del corso]] prevedono commenti con $\triangleright$ e nessun `do`/`then`. Il significato è lo stesso. Anche l'assegnamento multiplo `L[n1+1] ← R[n2+1] ← ∞` (riga 8) e `i ← j ← 1` (riga 9) non è previsto dalle convenzioni: si legge come due assegnamenti.

## Esempio di esecuzione

![[animazione-merge.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo sull'istanza della slide 06 p. 17: $A[p..r] = \langle 2, 4, 5, 7, 1, 2, 3, 6 \rangle$ con $q$ a metà. Si vedono la copia in $L$ e $R$ con le sentinelle, i puntatori $i$, $j$, $k$, il confronto $L[i] \le R[j]$ (in azzurro l'elemento scelto), la parte già fusa $A[p..k-1]$ in verde (l'invariante di p. 19) e la riga di pseudocodice corrente.

> 📄 Fonte: [[06-Merge Sort (1).pdf#page=17]]

Stato iniziale della slide: $A[p..q] = \langle 2, 4, 5, 7 \rangle$, $A[q+1..r] = \langle 1, 2, 3, 6 \rangle$, quindi $n_1 = n_2 = 4$, $L = \langle 2, 4, 5, 7, \infty \rangle$, $R = \langle 1, 2, 3, 6, \infty \rangle$, $i = j = 1$.

![[06-merge-sort-p17-traccia-merge.png]]
*Le due metà copiate in $L$ e $R$ con le sentinelle; sopra, $A[p..r]$ già fuso. ([[06-Merge Sort (1).pdf#page=17]])*

> 🧩 Derivazione mia — traccia del ciclo delle righe 10–15 (la slide mostra solo lo stato iniziale e quello finale; verificata con [[divide_et_impera.py]]):

| $k$ | $i$ | $j$ | confronto $L[i] \le R[j]$ | scelta | $A[p..k]$ |
|-----|-----|-----|---------------------------|--------|-----------|
| 1 | 1 | 1 | $2 \le 1$? no | $R[1] = 1$ | ⟨1⟩ |
| 2 | 1 | 2 | $2 \le 2$? sì | $L[1] = 2$ | ⟨1, 2⟩ |
| 3 | 2 | 2 | $4 \le 2$? no | $R[2] = 2$ | ⟨1, 2, 2⟩ |
| 4 | 2 | 3 | $4 \le 3$? no | $R[3] = 3$ | ⟨1, 2, 2, 3⟩ |
| 5 | 2 | 4 | $4 \le 6$? sì | $L[2] = 4$ | ⟨1, 2, 2, 3, 4⟩ |
| 6 | 3 | 4 | $5 \le 6$? sì | $L[3] = 5$ | ⟨1, …, 4, 5⟩ |
| 7 | 4 | 4 | $7 \le 6$? no | $R[4] = 6$ | ⟨1, …, 5, 6⟩ |
| 8 | 4 | 5 | $7 \le \infty$? sì | $L[4] = 7$ | ⟨1, 2, 2, 3, 4, 5, 6, 7⟩ |

Alla fine $i = 5$ e $j = 5$: in $L$ e $R$ restano solo le due sentinelle, come dice [[06-Merge Sort (1).pdf#page=20]]. Al passo $k = 8$ la sentinella $R[5] = \infty$ fa scegliere $L[4]$ senza controllare che $R$ sia finito.

## Correttezza

> 📄 Fonte: [[06-Merge Sort (1).pdf#page=19]], [[06-Merge Sort (1).pdf#page=20]]

(La slide [[06-Merge Sort (1).pdf#page=18]] ha solo il titolo «Merge: analisi di correttezza» e la pagina vuota: l'analisi è nelle due slide successive.)

**Invariante:** all'inizio di ciascuna iterazione dell'ultimo ciclo `for` (righe 10–15), la sottosequenza $A[p..k-1]$ contiene i $k - p$ elementi più piccoli di $L$ ed $R$, ordinati. Inoltre $L[i]$ e $R[j]$ sono i più piccoli elementi dei loro array a non essere stati ricopiati in $A$.

- **Inizializzazione** — l'invariante è vero prima della prima iterazione: per $k = p$ la sottosequenza $A[p..k-1]$ è vuota ($k - p = 0$). $L[1]$ e $R[1]$ sono i più piccoli elementi dei loro array a non essere stati ricopiati in $A$.
- **Conservazione** — una iterazione del ciclo conserva la verità dell'invariante. Se $L[i] \le R[j]$, $L[i]$ viene ricopiato in $A[k]$, quindi $A[p..k]$ contiene i $k - p + 1$ elementi più piccoli di $L$ ed $R$, ordinati. Incrementando $k$ ed $i$ si ristabilisce l'invariante per la successiva iterazione. Analogo discorso se $R[j] < L[i]$.
- **Conclusione** — l'invariante prova che l'algoritmo è corretto. Il ciclo termina quando $k = r + 1$, quindi $A[p..k-1]$, cioè $A[p..r]$, contiene i $k - p = r - p + 1$ elementi più piccoli di $L$ e $R$, ordinati. Gli $r - p + 1$ elementi più piccoli di $L$ e $R$ coincidono con tutti gli elementi originariamente in $A[p..r]$. In $L$ e $R$ restano i due valori sentinella.

> 🧩 Derivazione mia — perché nella conservazione $A[k]$ riceve proprio il **più piccolo** tra i rimasti, e perché resta **ordinato**:
> 1. $L$ è ordinato (è la copia di $A[p..q]$, ordinata per ipotesi) e $L[i]$ è il primo non ricopiato, quindi $L[i] \le L[i'] $ per ogni $i' > i$. Lo stesso vale per $R[j]$.
> 2. Ogni elemento non ricopiato sta in $L[i..n_1]$ o in $R[j..n_2]$, quindi il più piccolo dei rimasti è $\min(L[i], R[j])$: è quello che le righe 11–15 copiano in $A[k]$.
> 3. $A[k] \ge A[k-1]$: $A[k-1]$ era il minimo dei rimasti al passo precedente, e i rimasti ora sono un sottoinsieme di quelli.
> 4. Le sentinelle non vengono mai copiate: nelle $n = n_1 + n_2$ iterazioni si copiano $n$ elementi, e una sentinella sarebbe scelta solo se anche l'altro array fosse esaurito, cioè dopo $n$ copie.
>
> **Terminazione:** il `for` delle righe 10–15 esegue esattamente $r - p + 1$ iterazioni (variante: $r + 1 - k$).

## Complessità

> 📄 Fonte: [[06-Merge Sort (1).pdf#page=21]]

La slide raggruppa le righe e assegna a ogni gruppo un costo:

| Righe | Istruzioni | Costo indicato nella slide |
|-------|------------|----------------------------|
| 1–2 | $n_1 \leftarrow q-p+1$, $n_2 \leftarrow r-q$ | tempo costante |
| 3–7 | creazione di $L$ e $R$, due cicli di copia | tempo proporzionale a $n = n_1 + n_2$ |
| 8–9 | sentinelle, $i \leftarrow j \leftarrow 1$ | tempo costante |
| 10–15 | ciclo di fusione | $n$ iterazioni, ciascuna richiedente un tempo costante ⇒ tempo proporzionale a $n$ |

![[06-merge-sort-p21-costo-merge.png]]

### Derivazione — Merge è $\Theta(n)$
**Fonte:** [[06-Merge Sort (1).pdf#page=21]] (costi per gruppi, senza conteggio esplicito)
**Si parte da:** [[tempo-di-esecuzione]] — $T(n) = \sum_i c_i \cdot (\text{n. esecuzioni riga } i)$, con $n = r - p + 1$

> 🧩 Derivazione mia — tabella costo × numero di esecuzioni:

| Riga | Costo | Esecuzioni | Perché |
|------|-------|------------|--------|
| 1, 2 | $c_1$, $c_2$ | 1 | fuori dai cicli |
| 4 | $c_4$ | $n_1 + 1$ | $n_1$ test veri e uno falso |
| 5 | $c_5$ | $n_1$ | |
| 6 | $c_6$ | $n_2 + 1$ | |
| 7 | $c_7$ | $n_2$ | |
| 8, 9 | $c_8$, $c_9$ | 1 | |
| 10 | $c_{10}$ | $n + 1$ | $k = p, \dots, r$ più il test finale |
| 11 | $c_{11}$ | $n$ | una volta per iterazione |
| 12–13 oppure 14–15 | $\le c_{12} + c_{13}$ (o $c_{14} + c_{15}$) | $n$ in totale | a ogni iterazione si esegue **uno** dei due rami |

$$
\begin{aligned}
T(n) &= c_1 + c_2 + c_4(n_1+1) + c_5 n_1 + c_6(n_2+1) + c_7 n_2 + c_8 + c_9 + c_{10}(n+1) + c_{11} n + \Theta(n) && \text{somma riga per riga} \\
     &\le (c_4 + c_5 + c_6 + c_7 + c_{10} + c_{11} + c_{\max})\, n + (c_1 + c_2 + c_4 + c_6 + c_8 + c_9 + c_{10}) && n_1, n_2 \le n,\ c_{\max} = \max(c_{12}+c_{13}, c_{14}+c_{15}) \\
     &= a n + b
\end{aligned}
$$

Anche il limite inferiore è lineare: il solo ciclo delle righe 10–15 esegue $n$ iterazioni, ciascuna con costo almeno $c_{11} > 0$. Quindi:

> 🧮 Formula chiave: $T_{\text{Merge}}(n) = \Theta(n)$, con $n = r - p + 1$, **in ogni caso**. Il numero di iterazioni non dipende dai valori, solo da $n$.

**Sanity check:** nella traccia di p. 17, $n = 8$: 8 iterazioni del ciclo di fusione, 4 + 4 copie iniziali.
**Ipotesi:** [[modello-ram]], costo costante per riga, compresa la creazione di $L$ e $R$ a meno della loro dimensione.

**Spazio:** $L$ e $R$ hanno $n_1 + 1 + n_2 + 1 = n + 2$ celle ⇒ $\Theta(n)$ memoria aggiuntiva (🧩). È il motivo per cui merge sort «**non** effettua un ordinamento sul posto» ([[06-Merge Sort (1).pdf#page=7]]).

## Proprietà

- **Non sul posto** — usa gli array ausiliari $L$ e $R$ ([[06-Merge Sort (1).pdf#page=7]]).
- **Stabile** — 🧩 derivabile dallo pseudocodice: a parità ($L[i] = R[j]$) la riga 11 sceglie $L[i]$, cioè l'elemento che stava prima in $A$. Nella traccia di p. 17 il 2 di $L$ finisce in $A[2]$, prima del 2 di $R$.

## Connessioni

- [[merge-sort]] — Merge è il suo passo Combine, con $C(n) = \Theta(n)$ ([[06-Merge Sort (1).pdf#page=23]])
- [[invariante-di-ciclo]] — invariante con due affermazioni (prefisso di $A$ e puntatori $i$, $j$)
- [[partition]] — il passo «lineare» di quicksort, che però lavora nel Divide e sul posto
- [[analisi-del-costo-riga-per-riga]] — stessa tecnica di insertion sort, ma qui il numero di esecuzioni non dipende dall'input
- [[dimostrazioni-di-correttezza]] — esercizi

## Fonti

- [[lezione-06-merge-sort]]
- [[06-Merge Sort (1).pdf#page=7]], [[06-Merge Sort (1).pdf#page=15]]–[[06-Merge Sort (1).pdf#page=21]]

_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf_
_Aggiornato: 2026-10-10 — nuova versione delle slide (06-Merge Sort (1).pdf): prima versione senza sentinelle, «codice completo»_

<!-- nav:inizio -->
---
**Lezione 06 · pagina 4 di 8** · ← [[merge-sort|Merge sort]] · [[lezioni|Indice]] · [[massimo-sottoarray|Problema del massimo sottoarray]] →
<!-- nav:fine -->
