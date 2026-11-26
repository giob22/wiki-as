---
tipo: entità
categoria: algoritmo
paradigma: "[[divide-et-impera]]"
fonti_pdf: ["06-Merge Sort (1).pdf#page=7", "06-Merge Sort (1).pdf#page=9", "06-Merge Sort (1).pdf#page=10", "06-Merge Sort (1).pdf#page=14", "06-Merge Sort (1).pdf#page=16", "06-Merge Sort (1).pdf#page=23", "06-Merge Sort (1).pdf#page=24", "06-Merge Sort (1).pdf#page=26", "06-Merge Sort (1).pdf#page=27", "06-Merge Sort (1).pdf#page=29"]
---

# Merge sort

Le sezioni seguono l'ordine delle slide: idea (p. 7) → funzionamento su un esempio (p. 8) → primo pseudocodice con i vettori $L$ e $R$ e sue criticità (pp. 9–12) → miglioramento con gli indici (pp. 13–15) → la funzione [[merge]] (pp. 15–21) → pseudocodice definitivo (p. 22) → analisi di complessità (pp. 23–25).

## Problema risolto

[[ordinamento]]: data una sequenza di $n$ valori, restituirne la permutazione ordinata in senso crescente.

## Idea · [[06-Merge Sort (1).pdf#page=7|p. 7]], [[06-Merge Sort (1).pdf#page=17|p. 17]]

- Approccio **[[divide-et-impera]]**:
  - **suddivide** una sequenza di $n$ elementi in due sottosequenze di $n/2$ elementi;
  - **ordina** le sottosequenze ricorsivamente,
  - fino ad ottenere una sottosequenza di lunghezza 1, che è ordinata;
  - **combina** («merge») due sottosequenze ordinate per produrre l'intera sequenza ordinata.
- Due funzioni:
  - **[[merge|Merge]]** combina due sottosequenze ordinate in una sequenza ordinata;
  - **Merge-Sort** ordina una sequenza suddividendola in due sottosequenze, ordinando ciascuna sottosequenza (mediante chiamata ricorsiva) e invocando la funzione Merge per ottenere la sequenza ordinata.
- **Non** effettua un ordinamento sul posto (**ATTENZIONE!!!**, in rosso nella slide).

Annotazioni a mano sulla slide:
- «array dinamico è solo una forma di gestione dell'array»: usare un [[array-dinamico]] non rende l'ordinamento «sul posto», cambia solo come si gestisce la memoria;
- «Perché dividiamo in due i sottoarray? perché non dividiamo per $n$?» con la risposta «l'algoritmo ricorsivo si riduce ad un for e chiamata a funzione → la fase crescente».

> 🧩 Spiegazione mia della risposta. Dividendo in $n$ parti invece che in 2, ogni parte ha un solo elemento: la ricorsione si ferma subito al caso base, e la «discesa» è solo un ciclo `for` che chiama la funzione su ogni elemento. Tutto il lavoro resta nella fase di risalita, che deve fondere $n$ sequenze di un elemento: scegliere ogni volta il minimo tra $n$ candidati è esattamente [[selection-sort]], $\Theta(n^2)$. Il guadagno di merge sort viene proprio dal dividere in **poche** parti grandi: $\lg n$ livelli invece di uno.

> 🧩 Spiegazione mia — dove sta il lavoro: il Divide è banale (calcolare il punto medio), tutto il lavoro è nel Combine. In [[quicksort]] è il contrario: il lavoro è nel Divide ([[partition]]) e il Combine è vuoto.

## Dal primo pseudocodice alla versione con indici

Le slide costruiscono lo pseudocodice in tre tappe: una prima versione con vettori nuovi (pp. 9–12), il passaggio agli indici (pp. 13–14), lo spostamento della memoria ausiliaria dentro Merge (p. 15).

### Prima versione: vettori $L$ e $R$ · [[06-Merge Sort (1).pdf#page=10|p. 10]]–[[06-Merge Sort (1).pdf#page=13|13]]

```
MergeSort(A)
1  se A ha un solo elemento
2      ritorna A
3  dividi A in L e R
4  L ← MergeSort(L)
5  R ← MergeSort(R)
6  ritorna Merge(L, R)
```

Accanto allo pseudocodice la slide schematizza le tre fasi dell'esecuzione:
1. **Discesa** — se non sono nel caso base, divido il problema e richiamo la stessa funzione;
2. **Caso base** — un vettore con un solo elemento è già ordinato: non c'è nulla da fare;
3. **Risalita** — quando i sottoproblemi sono ordinati, li fondo con un merge ordinato.

![[06-merge-sort-p9-pseudocodice-con-vettori.png]]

Annotazioni a mano: «Caso base — fase ascendente» accanto alle righe 1–2, «Caso ricorsivo — fase decrescente» accanto alle righe 3–6; a p. 12, tra le righe 5 e 6, «qui $L$ e $R$ arrivano ordinati».

> 🧩 Lettura mia delle annotazioni: il caso base è il punto in cui la discesa finisce e comincia la risalita. Nel caso ricorsivo le righe 3–5 appartengono alla discesa; la riga 6 (Merge) viene eseguita solo al ritorno delle chiamate, cioè in risalita, quando $L$ e $R$ sono già ordinati.

> ⚠️ Contraddizione (di notazione): questa prima versione è uno schizzo in italiano («se», «ritorna», «dividi A in L e R») e non segue le [[pseudocodice|convenzioni del corso]]; la slide stessa la presenta con un punto interrogativo. La versione definitiva è quella di p. 23.

**Criticità?**:
- il caso base non fa praticamente nessuna operazione;
- ho necessità di una seconda funzione (non ricorsiva) che fonda $L$ e $R$ in maniera ordinata;
- $L$ e $R$ sono due **nuovi vettori** allocati da Merge-Sort e poi passati ricorsivamente a Merge-Sort e poi nuovamente a Merge.

**Posso migliorare qualcosa?**

> 🧩 Perché è una criticità: ogni chiamata copia la propria porzione in due vettori nuovi prima ancora di cominciare a fondere. A ogni livello dell'albero delle chiamate si copiano così tutti gli $n$ elementi, solo per dividere, e i vettori creati vanno poi restituiti e ricopiati da Merge.

### Miglioramento: dal vettore agli indici · [[06-Merge Sort (1).pdf#page=14|p. 14]], [[06-Merge Sort (1).pdf#page=15|15]]

**Un sottoproblema non è un nuovo array: è una porzione dell'array originale.** La figura mostra $A = \langle 5, 2, 8, 1, 4, 7, 3, 6 \rangle$ con la metà sinistra $A[p..q] = \langle 5, 2, 8, 1 \rangle$ (in blu) e la destra $A[q+1..r] = \langle 4, 7, 3, 6 \rangle$ (in rosso).

```
MergeSort(A, p, r)
1  se p = r
2      ritorna
3  q ← floor((p + r) / 2)
4  MergeSort(A, p, q)
5  MergeSort(A, q+1, r)
6  Merge(A, p, q, r)
```

- $p = r$ indica un sottovettore di un solo elemento;
- $q$ è lo **split** che divide logicamente $A[p..r]$ in due metà;
- le chiamate ricorsive ordinano **direttamente** le due porzioni di $A$;
- Merge viene chiamato solo dopo che entrambe le metà sono ordinate;
- il caso base resta identico;
- ho sempre bisogno della funzione merge;
- sia Merge che Merge-Sort operano sempre e solo su $A$, usando **indici** per la gestione dei sotto-array.

![[06-merge-sort-p13-merge-sort-con-indici.png]]

**Tutto troppo bello?**

### Sotto-array e merge: dove nasce il «non in-place» · [[06-Merge Sort (1).pdf#page=16|p. 16]]

Merge deve utilizzare **memoria accessoria** per copiare il contenuto dei sotto-vettori, per evitare perdite durante l'inserimento in $A$, che a questo punto è una **sovrascrittura**. La creazione effettiva di $L$ e $R$ è **spostata da Merge-Sort a Merge**; il ciclo di Merge fa un «pop» da $L$ e $R$ e inserisce con sovrascrittura in $A$ (pseudocodice in [[merge]]).

**Qui nasce il «non in-place»**: la memoria ausiliaria non serve solo per dividere, ma per fondere in modo semplice e sicuro.

> 🧩 Esempio mio della «perdita»: con $A[p..r] = \langle 5, 8 \mid 1, 2 \rangle$, fondere scrivendo direttamente in $A$ metterebbe 1 in $A[p]$ e cancellerebbe il 5 prima che sia stato collocato. Copiando prima le due metà in $L = \langle 5, 8 \rangle$ e $R = \langle 1, 2 \rangle$, $A$ si può sovrascrivere senza perdere nulla.

## Pseudocodice (versione definitiva) · [[06-Merge Sort (1).pdf#page=23|p. 23]]

```
Merge-Sort (A,p,r)
1  if p<r
2      q ← ⌊(p+r)/2⌋
3      Merge-Sort (A,p,q)
4      Merge-Sort (A,q+1,r)
5      Merge (A,p,q,r)
```

Invochiamo `Merge-Sort(A,1,n)` per ordinare l'intera sequenza.

Annotazioni a mano accanto allo pseudocodice: «Restituisci $A$ ⇒ non operare su $A$ se devi considerare il singolo elemento di $A$» e «L'ottimizzazione della firma ci ha portato a tutti questi benefici».

> 🧩 Confronto mio con la versione di p. 14: la «firma» è passata da `MergeSort(A)` a `Merge-Sort(A,p,r)`, e non serve più restituire un vettore. Il caso base è scritto al contrario: «se $p = r$ ritorna» (p. 14) contro «if $p<r$ … » (p. 23). Le due forme sono equivalenti perché le chiamate hanno sempre $p \le r$; con $p \ge r$ non si fa nulla.

![[06-merge-sort-p22-pseudocodice-merge-sort.png]]

Significato dei simboli: $p$, $r$ = estremi del sotto-array $A[p..r]$ da ordinare; $q$ = punto di divisione; [[merge|Merge]] fonde $A[p..q]$ e $A[q+1..r]$.

> 🧩 Derivazione mia — dimensioni delle due metà. Con $n = r - p + 1$:
$$
\begin{aligned}
q - p + 1 &= \left\lfloor \tfrac{p+r}{2} \right\rfloor - p + 1 = \left\lfloor \tfrac{r-p}{2} \right\rfloor + 1 && p \text{ intero, esce dalla parte intera} \\
          &= \left\lfloor \tfrac{n-1}{2} \right\rfloor + 1 = \left\lceil \tfrac{n}{2} \right\rceil && r - p = n - 1 \\
r - q     &= n - \left\lceil \tfrac{n}{2} \right\rceil = \left\lfloor \tfrac{n}{2} \right\rfloor && \text{il resto}
\end{aligned}
$$
> Per $n \ge 2$ entrambe le metà hanno almeno un elemento e meno di $n$ elementi: la ricorsione termina. Con $n = 11$ (l'esempio di p. 9) si ottengono 6 e 5 elementi.

## Esempio di esecuzione · [[06-Merge Sort (1).pdf#page=9|p. 9]]

![[animazione-merge-sort.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo sulla sequenza della slide 06 p. 9, ⟨5, 2, 8, 0, 4, 7, 1, 9, 3, 2, 6⟩. Mostra l'albero delle chiamate: ogni nodo è un sotto-array $A[p..r]$ (indici sopra il riquadro), bianco finché è da ordinare, rosso quando è la chiamata attiva, verde quando è ordinato dopo Merge. Si vedono la riga di pseudocodice corrente e il risultato di ogni Merge; l'albero ha $\lceil \lg 11 \rceil + 1 = 5$ livelli.

La slide mostra l'albero di ricorsione su ⟨5, 2, 8, 0, 4, 7, 1, 9, 3, 2, 6⟩ ($n = 11$): in discesa le divisioni, fino a sequenze di un elemento; in risalita le fusioni.

![[06-merge-sort-p8-albero-merge-sort.png]]
*Albero delle fusioni: dalle foglie (un elemento) fino alla sequenza ordinata ⟨0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9⟩.*

| Profondità | Sotto-sequenze dopo la divisione | Risultato delle fusioni a quel livello |
|---|---|---|
| 0 | ⟨5, 2, 8, 0, 4, 7, 1, 9, 3, 2, 6⟩ | ⟨0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9⟩ |
| 1 | ⟨5, 2, 8, 0, 4, 7⟩, ⟨1, 9, 3, 2, 6⟩ | ⟨0, 2, 4, 5, 7, 8⟩, ⟨1, 2, 3, 6, 9⟩ |
| 2 | ⟨5, 2, 8⟩, ⟨0, 4, 7⟩, ⟨1, 9, 3⟩, ⟨2, 6⟩ | ⟨2, 5, 8⟩, ⟨0, 4, 7⟩, ⟨1, 3, 9⟩, ⟨2, 6⟩ |
| 3 | ⟨5, 2⟩, ⟨8⟩, ⟨0, 4⟩, ⟨7⟩, ⟨1, 9⟩, ⟨3⟩, ⟨2⟩, ⟨6⟩ | ⟨2, 5⟩, ⟨0, 4⟩, ⟨1, 9⟩ (le altre sono singoli) |
| 4 | ⟨5⟩, ⟨2⟩, ⟨0⟩, ⟨4⟩, ⟨1⟩, ⟨9⟩ | foglie |

> 🧩 Verificato con [[divide_et_impera.py]], che stampa le sequenze prodotte a ogni profondità: coincidono con la figura. Le metà sinistre sono sempre quelle con un elemento in più ($\lceil n/2 \rceil$), come previsto dalla derivazione sopra.

## Correttezza · [[06-Merge Sort (1).pdf#page=7|p. 7]], [[06-Merge Sort (1).pdf#page=20|p. 20]], [[06-Merge Sort (1).pdf#page=21|21]]

La slide non dimostra la correttezza di Merge-Sort; dimostra quella di [[merge]].

> 🧩 Derivazione mia — [[correttezza-per-induzione]] forte sulla dimensione $n = r - p + 1$.
> - **Specifica:** pre $A[p..r]$ qualsiasi; post $A[p..r]$ contiene gli stessi elementi, ordinati.
> - **Base** ($n \le 1$, cioè $p \ge r$): la condizione `p<r` è falsa e non si fa nulla; una sequenza di lunghezza 0 o 1 è ordinata (p. 7: «sottosequenza di lunghezza 1, che è ordinata»).
> - **Passo** ($n \ge 2$): le due chiamate delle righe 3–4 lavorano su $\lceil n/2 \rceil < n$ e $\lfloor n/2 \rfloor < n$ elementi, quindi per ipotesi induttiva al ritorno $A[p..q]$ e $A[q+1..r]$ sono ordinati. È la pre-condizione di Merge, che ([[merge]] § Correttezza) lascia $A[p..r]$ ordinato.
> - **Terminazione:** la misura $n$ scende strettamente a ogni chiamata.

## Complessità

### Ricorrenza del divide et impera · [[06-Merge Sort (1).pdf#page=24|p. 24]], [[06-Merge Sort (1).pdf#page=26|26]], [[06-Merge Sort (1).pdf#page=29|p. 29]]

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

A p. 24 la slide chiede «Nel caso di Merge Sort: $D(n) = $ ?, $C(n) = $ ?, $a = b = $ ?». Annotazioni a mano: «Ricorrenza: formula matematica» (su $T(n)$), «Potrei avere più casi base» (su $\Theta(1)$), «equivale al costo dell'operazione per ottenere $q$» (sotto $D(n)$).

![[06-merge-sort-p23-ricorrenza-domande.png]]

Risposta: nel caso di merge sort $D(n) = \Theta(1)$, $C(n) = \Theta(n)$, $a = b = 2$.

> 🧩 Derivazione mia — da dove vengono i tre valori, riga per riga:
> - $D(n) = \Theta(1)$: la riga 2 calcola solo $q$;
> - $a = b = 2$: righe 3–4, due chiamate su metà del problema ($\lceil n/2 \rceil$ e $\lfloor n/2 \rfloor$, approssimate con $n/2$);
> - $C(n) = \Theta(n)$: la riga 5 chiama [[merge]], che è $\Theta(n)$.
>
> Sostituendo: $T(n) = 2T(n/2) + \Theta(1) + \Theta(n) = 2T(n/2) + \Theta(n)$, perché $\Theta(1) + \Theta(n) = \Theta(n)$ ([[regole-di-calcolo-asintotico]]). È la ricorrenza scritta in p. 29.

![[06-merge-sort-p24-ricorrenza-divide-et-impera.png]]

### Soluzione con l'albero di ricorsione · [[06-Merge Sort (1).pdf#page=27|p. 27]]

Supponendo che $n$ sia una potenza di 2 e
$$
T(n) = \begin{cases} c & \text{nel caso banale } n = 1 \\ 2T(n/2) + cn & \text{altrimenti } (n > 1) \end{cases}
$$
l'albero ha costo $cn$ a ogni livello e $\lg n + 1$ livelli. Il costo totale è
$$ cn(\lg n + 1) = cn\lg n + cn = \Theta(n \lg n). $$

![[06-merge-sort-p25-albero-ricorsione-merge-sort.png]]
*Radice $cn$, due figli $cn/2$, quattro nipoti $cn/4$, …, $n$ foglie di costo $c$: ogni livello somma a $cn$.*

### Derivazione — $T(n) = cn(\lg n + 1)$ · [[06-Merge Sort (1).pdf#page=27|p. 27]], [[06-Merge Sort (1).pdf#page=33|p. 33]], [[06-Merge Sort (1).pdf#page=44|p. 44]]
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

> 🧩 Verifica per induzione (il metodo dell'albero dà una soluzione di tentativo):
$$
\begin{aligned}
T(1) &= c = c \cdot 1 \cdot (\lg 1 + 1) && \lg 1 = 0 \\
T(n) &= 2T(n/2) + cn = 2 \cdot c\tfrac{n}{2}\left(\lg\tfrac{n}{2} + 1\right) + cn && \text{ipotesi induttiva su } n/2 \\
     &= cn(\lg n - 1 + 1) + cn = cn(\lg n + 1) && \lg\tfrac{n}{2} = \lg n - 1
\end{aligned}
$$

**Sanity check:** [[divide_et_impera.py]] conta le iterazioni del ciclo di fusione di Merge (il termine $cn$ con $c = 1$): per $n = 2, 8, 64, 1024$ sono esattamente $n \lg n = 2, 24, 384, 10240$. Manca il $+cn$ perché il caso base non esegue Merge.
**Ipotesi:** $n$ potenza di 2, così ogni divisione è esatta e tutti i nodi di un livello hanno la stessa dimensione. Senza questa ipotesi le due metà differiscono di 1 e il risultato $\Theta(n\lg n)$ si conferma con il [[teorema-dell-esperto]] (caso 2, $a = b = 2$, $f(n) = \Theta(n)$), che ammette sia $\lfloor n/2 \rfloor$ che $\lceil n/2 \rceil$.

> 🎯 Esame: scrivere la ricorrenza di merge sort leggendo lo pseudocodice ($D$, $C$, $a$, $b$) e risolverla con l'albero: $\lg n + 1$ livelli di costo $cn$.

### Casi migliore, peggiore, medio

> 🧩 Derivazione mia: la ricorrenza non dipende dai valori dell'input. Le divisioni dipendono solo da $p$ e $r$, e [[merge]] costa $\Theta(n)$ in ogni caso. Quindi caso migliore, peggiore e medio coincidono: $\Theta(n \lg n)$. È il contrasto con [[insertion-sort]] ($\Theta(n)$–$\Theta(n^2)$) e con [[quicksort]] ($\Theta(n\lg n)$–$\Theta(n^2)$).

### Spazio · [[06-Merge Sort (1).pdf#page=7|p. 7]]

> 🧩 Derivazione mia: ogni Merge alloca $L$ e $R$ di $n + 2$ celle in totale. Al più una fusione per volta è attiva e le sue celle si liberano al ritorno, quindi il massimo è quello della fusione alla radice: $\Theta(n)$. A questo si somma la pila delle chiamate, profonda $\lceil \lg n \rceil + 1$: $\Theta(\lg n)$. Totale $\Theta(n)$ di memoria aggiuntiva, cioè **non sul posto**.

## Proprietà · [[06-Merge Sort (1).pdf#page=7|p. 7]]

- **Non sul posto**.
- **Stabile** — 🧩 derivabile: Merge a parità sceglie l'elemento della metà sinistra ([[merge]] § Proprietà), e la metà sinistra contiene gli elementi che stavano prima.
- **Non adattivo** — 🧩 derivabile: il costo è $\Theta(n\lg n)$ anche su input già ordinato.

## Connessioni · [[01-Introduzione.pdf#page=11|p. 11]]

- [[merge]] — il passo Combine, $\Theta(n)$
- [[divide-et-impera]] — merge sort è l'esempio della ricorrenza generale $aT(n/b) + D(n) + C(n)$
- [[equazioni-di-ricorrenza]], [[metodo-albero-di-ricorrenza]], [[teorema-dell-esperto]] — i tre modi di risolvere $2T(n/2) + \Theta(n)$
- [[quicksort]] — stesso paradigma, lavoro nel Divide anziché nel Combine; sul posto ma con caso peggiore quadratico
- [[efficienza-degli-algoritmi]] — il confronto $n^2$ contro $n \lg n$ di p. 11
- [[ordinamento]] — tabella comparativa degli algoritmi

## Fonti · [[06-Merge Sort (1).pdf#page=6|p. 6]], [[06-Merge Sort (1).pdf#page=16|p. 16]], [[06-Merge Sort (1).pdf#page=23|p. 23]], [[06-Merge Sort (1).pdf#page=27|p. 27]]

- [[lezione-06-merge-sort]]

_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf_
_Aggiornato: 2026-10-10 — nuova versione delle slide (06-Merge Sort (1).pdf): primo pseudocodice con L e R, versione con indici, annotazioni_

<!-- nav:inizio -->
---
**Lezione 06 · pagina 3 di 8** · ← [[torre-di-hanoi|Torre di Hanoi · 06-Merge Sort (1).pdf#page=2p. 2]] · [[lezioni|Indice]] · [[merge|Merge (fusione di sequenze ordinate)]] →
<!-- nav:fine -->
