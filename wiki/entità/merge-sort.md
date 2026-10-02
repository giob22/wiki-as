---
tipo: entità
categoria: algoritmo
paradigma: "[[divide-et-impera]]"
fonti_pdf: ["06-Merge Sort.pdf#page=6", "06-Merge Sort.pdf#page=7", "06-Merge Sort.pdf#page=13", "06-Merge Sort.pdf#page=14", "06-Merge Sort.pdf#page=15", "06-Merge Sort.pdf#page=17"]
---

# Merge sort

Le sezioni seguono l'ordine delle slide: idea (p. 6) → esempio (p. 7) → la funzione [[merge]] (pp. 8–12) → pseudocodice di Merge-Sort (p. 13) → analisi di complessità (pp. 14–15).

## Problema risolto

[[ordinamento]]: data una sequenza di $n$ valori, restituirne la permutazione ordinata in senso crescente.

## Idea

> 📄 Fonte: [[06-Merge Sort.pdf#page=6]] (ripetuta in [[06-Merge Sort.pdf#page=8]])

- Approccio **[[divide-et-impera]]**:
  - **suddivide** una sequenza di $n$ elementi in due sottosequenze di $n/2$ elementi;
  - **ordina** le sottosequenze ricorsivamente,
  - fino ad ottenere una sottosequenza di lunghezza 1, che è ordinata;
  - **combina** («merge») due sottosequenze ordinate per produrre l'intera sequenza ordinata.
- Due funzioni:
  - **[[merge|Merge]]** combina due sottosequenze ordinate in una sequenza ordinata;
  - **Merge-Sort** ordina una sequenza suddividendola in due sottosequenze, ordinando ciascuna sottosequenza (mediante chiamata ricorsiva) e invocando la funzione Merge per ottenere la sequenza ordinata.
- **Non** effettua un ordinamento sul posto.

> 🧩 Spiegazione mia — dove sta il lavoro: il Divide è banale (calcolare il punto medio), tutto il lavoro è nel Combine. In [[quicksort]] è il contrario: il lavoro è nel Divide ([[partition]]) e il Combine è vuoto.

## Pseudocodice

> 📄 Fonte: [[06-Merge Sort.pdf#page=13]] (riportato fedelmente, numeri di riga miei)

```
Merge-Sort (A,p,r)
1  if p<r
2      q ← ⌊(p+r)/2⌋
3      Merge-Sort (A,p,q)
4      Merge-Sort (A,q+1,r)
5      Merge (A,p,q,r)
```

Invochiamo `Merge-Sort(A,1,n)` per ordinare l'intera sequenza.

![[06-merge-sort-p13-pseudocodice-merge-sort.png]]

Significato dei simboli: $p$, $r$ = estremi del sotto-array $A[p..r]$ da ordinare; $q$ = punto di divisione; [[merge|Merge]] fonde $A[p..q]$ e $A[q+1..r]$.

> 🧩 Derivazione mia — dimensioni delle due metà. Con $n = r - p + 1$:
$$
\begin{aligned}
q - p + 1 &= \left\lfloor \tfrac{p+r}{2} \right\rfloor - p + 1 = \left\lfloor \tfrac{r-p}{2} \right\rfloor + 1 && p \text{ intero, esce dalla parte intera} \\
          &= \left\lfloor \tfrac{n-1}{2} \right\rfloor + 1 = \left\lceil \tfrac{n}{2} \right\rceil && r - p = n - 1 \\
r - q     &= n - \left\lceil \tfrac{n}{2} \right\rceil = \left\lfloor \tfrac{n}{2} \right\rfloor && \text{il resto}
\end{aligned}
$$
> Per $n \ge 2$ entrambe le metà hanno almeno un elemento e meno di $n$ elementi: la ricorsione termina. Con $n = 11$ (l'esempio di p. 7) si ottengono 6 e 5 elementi.

## Esempio di esecuzione

![[animazione-merge-sort.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo sulla sequenza della slide 06 p. 7, ⟨5, 2, 8, 0, 4, 7, 1, 9, 3, 2, 6⟩. Mostra l'albero delle chiamate: ogni nodo è un sotto-array $A[p..r]$ (indici sopra il riquadro), bianco finché è da ordinare, rosso quando è la chiamata attiva, verde quando è ordinato dopo Merge. Si vedono la riga di pseudocodice corrente e il risultato di ogni Merge; l'albero ha $\lceil \lg 11 \rceil + 1 = 5$ livelli.

> 📄 Fonte: [[06-Merge Sort.pdf#page=7]]

La slide mostra l'albero di ricorsione su ⟨5, 2, 8, 0, 4, 7, 1, 9, 3, 2, 6⟩ ($n = 11$): in discesa le divisioni, fino a sequenze di un elemento; in risalita le fusioni.

![[06-merge-sort-p7-albero-merge-sort.png]]
*Albero delle fusioni: dalle foglie (un elemento) fino alla sequenza ordinata ⟨0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9⟩. ([[06-Merge Sort.pdf#page=7]])*

| Profondità | Sotto-sequenze dopo la divisione | Risultato delle fusioni a quel livello |
|------------|----------------------------------|----------------------------------------|
| 0 | ⟨5, 2, 8, 0, 4, 7, 1, 9, 3, 2, 6⟩ | ⟨0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9⟩ |
| 1 | ⟨5, 2, 8, 0, 4, 7⟩, ⟨1, 9, 3, 2, 6⟩ | ⟨0, 2, 4, 5, 7, 8⟩, ⟨1, 2, 3, 6, 9⟩ |
| 2 | ⟨5, 2, 8⟩, ⟨0, 4, 7⟩, ⟨1, 9, 3⟩, ⟨2, 6⟩ | ⟨2, 5, 8⟩, ⟨0, 4, 7⟩, ⟨1, 3, 9⟩, ⟨2, 6⟩ |
| 3 | ⟨5, 2⟩, ⟨8⟩, ⟨0, 4⟩, ⟨7⟩, ⟨1, 9⟩, ⟨3⟩, ⟨2⟩, ⟨6⟩ | ⟨2, 5⟩, ⟨0, 4⟩, ⟨1, 9⟩ (le altre sono singoli) |
| 4 | ⟨5⟩, ⟨2⟩, ⟨0⟩, ⟨4⟩, ⟨1⟩, ⟨9⟩ | foglie |

> 🧩 Verificato con [[divide_et_impera.py]], che stampa le sequenze prodotte a ogni profondità: coincidono con la figura. Le metà sinistre sono sempre quelle con un elemento in più ($\lceil n/2 \rceil$), come previsto dalla derivazione sopra.

## Correttezza

La slide non dimostra la correttezza di Merge-Sort; dimostra quella di [[merge]] ([[06-Merge Sort.pdf#page=10]], [[06-Merge Sort.pdf#page=11]]).

> 🧩 Derivazione mia — [[correttezza-per-induzione]] forte sulla dimensione $n = r - p + 1$.
> - **Specifica:** pre $A[p..r]$ qualsiasi; post $A[p..r]$ contiene gli stessi elementi, ordinati.
> - **Base** ($n \le 1$, cioè $p \ge r$): la condizione `p<r` è falsa e non si fa nulla; una sequenza di lunghezza 0 o 1 è ordinata ([[06-Merge Sort.pdf#page=6]]: «sottosequenza di lunghezza 1, che è ordinata»).
> - **Passo** ($n \ge 2$): le due chiamate delle righe 3–4 lavorano su $\lceil n/2 \rceil < n$ e $\lfloor n/2 \rfloor < n$ elementi, quindi per ipotesi induttiva al ritorno $A[p..q]$ e $A[q+1..r]$ sono ordinati. È la pre-condizione di Merge, che ([[merge]] § Correttezza) lascia $A[p..r]$ ordinato.
> - **Terminazione:** la misura $n$ scende strettamente a ogni chiamata.

## Complessità

### Ricorrenza del divide et impera
> 📄 Fonte: [[06-Merge Sort.pdf#page=14]]

Per un approccio [[divide-et-impera]], detti:
- $\Theta(1)$ il tempo per risolvere il caso «banale»;
- $D(n)$ il tempo per suddividere un problema;
- $C(n)$ il tempo per ricombinare le soluzioni dei sottoproblemi;
- $a$ il numero di sottoproblemi in cui si divide un problema;
- $1/b$ il fattore di riduzione della dimensione di un problema,

la complessità è esprimibile in forma di ricorrenza:

$$
T(n) = \begin{cases} \Theta(1) & \text{nel caso banale } n = 1 \\ aT(n/b) + D(n) + C(n) & \text{altrimenti } (n > 1) \end{cases}
$$

Nel caso di merge sort: $D(n) = \Theta(1)$, $C(n) = \Theta(n)$, $a = b = 2$.

> 🧩 Derivazione mia — da dove vengono i tre valori, riga per riga:
> - $D(n) = \Theta(1)$: la riga 2 calcola solo $q$;
> - $a = b = 2$: righe 3–4, due chiamate su metà del problema ($\lceil n/2 \rceil$ e $\lfloor n/2 \rfloor$, approssimate con $n/2$);
> - $C(n) = \Theta(n)$: la riga 5 chiama [[merge]], che è $\Theta(n)$.
>
> Sostituendo: $T(n) = 2T(n/2) + \Theta(1) + \Theta(n) = 2T(n/2) + \Theta(n)$, perché $\Theta(1) + \Theta(n) = \Theta(n)$ ([[regole-di-calcolo-asintotico]]). È la ricorrenza scritta in [[06-Merge Sort.pdf#page=17]].

![[06-merge-sort-p14-ricorrenza-divide-et-impera.png]]

### Soluzione con l'albero di ricorsione
> 📄 Fonte: [[06-Merge Sort.pdf#page=15]]

Supponendo che $n$ sia una potenza di 2 e
$$
T(n) = \begin{cases} c & \text{nel caso banale } n = 1 \\ 2T(n/2) + cn & \text{altrimenti } (n > 1) \end{cases}
$$
l'albero ha costo $cn$ a ogni livello e $\lg n + 1$ livelli. Il costo totale è
$$ cn(\lg n + 1) = cn\lg n + cn = \Theta(n \lg n). $$

![[06-merge-sort-p15-albero-ricorsione-merge-sort.png]]
*Radice $cn$, due figli $cn/2$, quattro nipoti $cn/4$, …, $n$ foglie di costo $c$: ogni livello somma a $cn$. ([[06-Merge Sort.pdf#page=15]])*

### Derivazione — $T(n) = cn(\lg n + 1)$
**Fonte:** [[06-Merge Sort.pdf#page=15]] (albero disegnato, somma data senza passaggi)
**Si parte da:** [[metodo-albero-di-ricorrenza]] — si somma il costo di tutti i nodi, livello per livello

> 🧩 Derivazione mia:

$$
\begin{aligned}
&\text{livello } i:\ 2^i \text{ nodi, ciascuno su } n/2^i \text{ elementi} && \text{ogni nodo ha 2 figli di metà dimensione} \\
&\text{costo di un nodo al livello } i:\ c \cdot \tfrac{n}{2^i} && \text{termine } cn \text{ della ricorrenza} \\
&\text{costo del livello } i:\ 2^i \cdot c\tfrac{n}{2^i} = cn && \text{indipendente da } i \\
&\text{ultimo livello: } \tfrac{n}{2^i} = 1 \iff i = \lg n && \text{foglie: } 2^{\lg n} = n \text{ nodi di costo } c \text{, totale } cn \\
&\text{livelli: } i = 0, 1, \dots, \lg n \ \Rightarrow\ \lg n + 1 && \\
T(n) &= \sum_{i=0}^{\lg n} cn = cn(\lg n + 1) = cn\lg n + cn && \text{somma di } \lg n + 1 \text{ termini uguali} \\
     &= \Theta(n \lg n) && cn\lg n \text{ domina } cn
\end{aligned}
$$

> 🧩 Verifica per induzione (il metodo dell'albero dà una soluzione di tentativo, [[06-Merge Sort.pdf#page=21]]):
$$
\begin{aligned}
T(1) &= c = c \cdot 1 \cdot (\lg 1 + 1) && \lg 1 = 0 \\
T(n) &= 2T(n/2) + cn = 2 \cdot c\tfrac{n}{2}\left(\lg\tfrac{n}{2} + 1\right) + cn && \text{ipotesi induttiva su } n/2 \\
     &= cn(\lg n - 1 + 1) + cn = cn(\lg n + 1) && \lg\tfrac{n}{2} = \lg n - 1
\end{aligned}
$$

**Sanity check:** [[divide_et_impera.py]] conta le iterazioni del ciclo di fusione di Merge (il termine $cn$ con $c = 1$): per $n = 2, 8, 64, 1024$ sono esattamente $n \lg n = 2, 24, 384, 10240$. Manca il $+cn$ perché il caso base non esegue Merge.
**Ipotesi:** $n$ potenza di 2, così ogni divisione è esatta e tutti i nodi di un livello hanno la stessa dimensione. Senza questa ipotesi le due metà differiscono di 1 e il risultato $\Theta(n\lg n)$ si conferma con il [[teorema-dell-esperto]] (caso 2, $a = b = 2$, $f(n) = \Theta(n)$), che ammette sia $\lfloor n/2 \rfloor$ che $\lceil n/2 \rceil$ ([[06-Merge Sort.pdf#page=28]]).

> 🎯 Esame: scrivere la ricorrenza di merge sort leggendo lo pseudocodice ($D$, $C$, $a$, $b$) e risolverla con l'albero: $\lg n + 1$ livelli di costo $cn$.

### Casi migliore, peggiore, medio

> 🧩 Derivazione mia: la ricorrenza non dipende dai valori dell'input. Le divisioni dipendono solo da $p$ e $r$, e [[merge]] costa $\Theta(n)$ in ogni caso. Quindi caso migliore, peggiore e medio coincidono: $\Theta(n \lg n)$. È il contrasto con [[insertion-sort]] ($\Theta(n)$–$\Theta(n^2)$) e con [[quicksort]] ($\Theta(n\lg n)$–$\Theta(n^2)$).

### Spazio

> 🧩 Derivazione mia: ogni Merge alloca $L$ e $R$ di $n + 2$ celle in totale. Al più una fusione per volta è attiva e le sue celle si liberano al ritorno, quindi il massimo è quello della fusione alla radice: $\Theta(n)$. A questo si somma la pila delle chiamate, profonda $\lceil \lg n \rceil + 1$: $\Theta(\lg n)$. Totale $\Theta(n)$ di memoria aggiuntiva, cioè **non sul posto** ([[06-Merge Sort.pdf#page=6]]).

## Proprietà

- **Non sul posto** ([[06-Merge Sort.pdf#page=6]]).
- **Stabile** — 🧩 derivabile: Merge a parità sceglie l'elemento della metà sinistra ([[merge]] § Proprietà), e la metà sinistra contiene gli elementi che stavano prima.
- **Non adattivo** — 🧩 derivabile: il costo è $\Theta(n\lg n)$ anche su input già ordinato.

## Connessioni

- [[merge]] — il passo Combine, $\Theta(n)$
- [[divide-et-impera]] — merge sort è l'esempio della ricorrenza generale $aT(n/b) + D(n) + C(n)$
- [[equazioni-di-ricorrenza]], [[metodo-albero-di-ricorrenza]], [[teorema-dell-esperto]] — i tre modi di risolvere $2T(n/2) + \Theta(n)$
- [[quicksort]] — stesso paradigma, lavoro nel Divide anziché nel Combine; sul posto ma con caso peggiore quadratico
- [[efficienza-degli-algoritmi]] — il confronto $n^2$ contro $n \lg n$ di [[01-Introduzione.pdf#page=11]]
- [[ordinamento]] — tabella comparativa degli algoritmi

## Fonti

- [[lezione-06-merge-sort]]
- [[06-Merge Sort.pdf#page=5]]–[[06-Merge Sort.pdf#page=7]], [[06-Merge Sort.pdf#page=13]]–[[06-Merge Sort.pdf#page=15]]

_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf_
