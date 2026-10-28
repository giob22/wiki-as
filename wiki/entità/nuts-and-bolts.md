---
tipo: entità
categoria: problema
paradigma: "[[divide-et-impera]] + [[randomizzazione]]"
fonti_pdf: ["07-Quicksort 1.pdf#page=24", "07-Quicksort 1.pdf#page=25"]
---

# Nuts and Bolts (dadi e bulloni)

Problema «Stop and Think» che chiude la lezione su quicksort ([[07-Quicksort 1.pdf#page=24]]). La slide dà solo il testo e chiede due algoritmi; le soluzioni, le analisi e le animazioni sono mie (🧩).

## Definizione formale

> 📄 Fonte: [[07-Quicksort 1.pdf#page=25]] (testo in inglese nella slide; qui riassunto in italiano)

- Sono dati $n$ **bulloni** di larghezze diverse e gli $n$ **dadi** corrispondenti.
- L'unica operazione ammessa è **provare un dado su un bullone**: si scopre se il dado è troppo largo, troppo stretto o se combacia esattamente.
- Le differenze di misura sono troppo piccole per vederle a occhio: **non** si possono confrontare direttamente due dadi tra loro, né due bulloni tra loro.
- Bisogna accoppiare ogni bullone con il suo dado.

**Consegna:** dare un algoritmo $O(n^2)$, poi un algoritmo **randomizzato** con tempo **atteso** $O(n \log n)$.

![[07-quicksort-p25-nuts-and-bolts.png]]

> 🧩 Modello di costo mio: si conta il numero di **test dado–bullone**, l'unica operazione di confronto disponibile (come i confronti negli algoritmi di [[ordinamento]]). Nelle animazioni e nel codice le larghezze sono numeri $1..n$ e «combaciare» vuol dire avere lo stesso numero, ma l'algoritmo può solo confrontare un dado con un bullone.

## Algoritmo 1 — $O(n^2)$

> 🧩 Soluzione mia: per ogni bullone si provano i dadi rimasti, uno alla volta, finché non si trova quello giusto. $D[1..n]$ = dadi, $B[1..n]$ = bulloni; i dadi già accoppiati vengono spostati in testa a $D$.

```
NUTS-BOLTS-QUADRATICO(D, B)
1  for i ← 1 to n
2      j ← i
3      while D[j] non combacia con B[i]
4          j ← j+1
5      exchange D[i] ↔ D[j]
```

### Esempio di esecuzione

![[animazione-nuts-and-bolts-quadratico.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo su un'istanza mia di 6 coppie: dadi ⟨4, 1, 6, 3, 5, 2⟩, bulloni ⟨3, 6, 2, 5, 1, 4⟩. A ogni passo un test tra $D[j]$ e $B[i]$ (rosso = non combaciano, azzurro = combaciano), poi lo scambio che porta il dado accanto al suo bullone; in verde le coppie già formate. Totale: 15 test.

### Correttezza

> 🧩 **Invariante** del `for`: all'inizio dell'iterazione $i$, $D[k]$ combacia con $B[k]$ per ogni $k < i$, e $D[i..n]$ contiene esattamente i dadi dei bulloni $B[i..n]$.
> - **Inizializzazione:** $i = 1$, nessuna coppia; $D[1..n]$ contiene tutti i dadi.
> - **Conservazione:** il dado di $B[i]$ è in $D[i..n]$, quindi il `while` lo trova con $j \le n$; lo scambio lo porta in $D[i]$ e il dado che stava in $D[i]$ resta in $D[i+1..n]$.
> - **Conclusione:** con $i = n + 1$ tutte le coppie $D[k]$, $B[k]$ combaciano.
> - **Terminazione:** il `while` termina perché il dado cercato esiste in $D[i..n]$; il `for` fa $n$ iterazioni.

### Complessità

> 🧩 Derivazione mia — numero di test nel caso peggiore:

$$
\begin{aligned}
\text{test per il bullone } i &\le n - i + 1 && \text{al più tutti i dadi di } D[i..n] \\
\text{test totali} &\le \sum_{i=1}^{n} (n - i + 1) = \sum_{m=1}^{n} m = \frac{n(n+1)}{2} && m = n - i + 1,\ \text{somma di Gauss} \\
&= O(n^2)
\end{aligned}
$$

Il limite è raggiunto quando il dado giusto è sempre l'ultimo tra i rimasti, ad esempio bulloni ⟨1, 2, …, n⟩ e dadi ⟨2, 3, …, n, 1⟩. **Sanity check** ([[divide_et_impera.py]]): 15 test sull'istanza dell'animazione (massimo 21 per $n = 6$); su istanze casuali circa $n^2/4$ (253 746 per $n = 1000$, contro il massimo 500 500).

## Algoritmo 2 — randomizzato, $O(n \log n)$ atteso

> 🧩 Soluzione mia: è [[partition]] di [[quicksort-randomizzato]] applicata **due volte**. Un dado non si può confrontare con un altro dado, ma si può usare come pivot per i **bulloni**; il bullone gemello trovato così fa da pivot per i **dadi**.

```
NUTS-BOLTS(D, B)
1  if D = ∅ return
2  d ← dado scelto a caso in D
3  dividi B con d: B<, b, B>
4  dividi D con b: D<, D>
5  accoppia d con b
6  NUTS-BOLTS(D<, B<)
7  NUTS-BOLTS(D>, B>)
```

Significato delle righe:
- riga 3: si prova $d$ su ogni bullone di $B$. $B_<$ = bulloni più stretti di $d$, $B_>$ = più larghi, $b$ = quello che combacia ($|B|$ test);
- riga 4: si prova $b$ su ogni dado di $D$ tranne $d$. $D_<$ = dadi più stretti di $b$, $D_>$ = più larghi ($|D| - 1$ test);
- righe 6–7: i dadi di $D_<$ combaciano tutti e soli con i bulloni di $B_<$ (larghezze minori di quella di $d$), quindi i due sottoproblemi sono **istanze dello stesso problema**.

### Esempio di esecuzione

![[animazione-nuts-and-bolts.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo sulla stessa istanza mia di 6 coppie, con un generatore casuale a seme fisso. Per ogni sottoproblema si vedono il dado scelto a caso, la divisione dei bulloni, quella dei dadi con il bullone gemello, le coppie trovate e il contatore dei test. Su un'istanza così piccola il metodo randomizzato fa più test (36) del quadratico (15): il vantaggio è **asintotico** (vedi sotto).

### Correttezza

> 🧩 [[correttezza-per-induzione]] su $n = |D| = |B|$. Base $n = 0$: nulla da accoppiare. Passo: $d$ e $b$ combaciano per costruzione; per l'osservazione sulle righe 6–7, $(D_<, B_<)$ e $(D_>, B_>)$ sono istanze valide con meno di $n$ coppie, e per ipotesi induttiva vengono accoppiate. Terminazione: $|D_<|, |D_>| \le n - 1$.

### Complessità

> 🧩 Derivazione mia. Con $n$ coppie, una chiamata fa $n + (n-1) = 2n - 1$ test (righe 3–4). Se $d$ è il $(k+1)$-esimo dado per larghezza:
$$ T(n) = T(k) + T(n - k - 1) + (2n - 1), \qquad k \in \{0, \dots, n-1\} $$
> È la ricorrenza di [[quicksort]] ([[07-Quicksort 1.pdf#page=21]]) con costo locale $2n - 1$ invece di $\Theta(n)$:
> - caso peggiore (dado scelto sempre il più stretto o il più largo): $\Theta(n^2)$, come la serie aritmetica di [[07-Quicksort 1.pdf#page=14]];
> - scelta casuale: $k$ è uniforme come per [[quicksort-randomizzato]], quindi il tempo atteso è $O(n \log n)$ per lo stesso argomento ([[07-Quicksort 1.pdf#page=23]]; 📚 Cormen, 3ª ed., §7.4.2).
>
> **Sanity check** ([[divide_et_impera.py]], media su 20 esecuzioni): 57, 1 365, 22 730 test per $n = 10, 100, 1000$, contro 23, 2 678, 253 746 del metodo quadratico. Il randomizzato vince da $n = 100$ in su.

> 🎯 Esame: riconoscere che il vincolo «niente confronti dado–dado» si aggira usando un elemento dell'altro insieme come pivot; ricondurre l'analisi a quella di quicksort randomizzato.

## Connessioni

- [[partition]], [[quicksort-randomizzato]] — la soluzione randomizzata ne è un adattamento
- [[randomizzazione]] — il pivot casuale rende improbabile il caso peggiore
- [[ordinamento]] — accoppiare dadi e bulloni equivale a ordinarli entrambi
- [[progettazione-divide-et-impera]] — il problema come esercizio di progettazione

## Fonti

- [[lezione-07-quicksort]]
- [[07-Quicksort 1.pdf#page=24]], [[07-Quicksort 1.pdf#page=25]]

_Aggiornato: 2026-10-01 — ingest 07-Quicksort.pdf_
_Aggiornato: 2026-10-14 — link ripuntati alla versione aggiornata delle slide 07-Quicksort 1.pdf_

<!-- nav:inizio -->
---
**Lezione 07 · pagina 6 di 7** · ← [[quicksort-randomizzato|Quicksort randomizzato]] · [[lezioni|Indice]] · [[progettazione-divide-et-impera|Progettazione di algoritmi divide et impera]] →
<!-- nav:fine -->
