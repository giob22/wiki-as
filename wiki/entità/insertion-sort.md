---
tipo: entità
categoria: algoritmo
paradigma: "incrementale (iterativo)"
fonti_pdf: ["05-Insertion sort.pdf#page=4", "05-Insertion sort.pdf#page=5", "05-Insertion sort.pdf#page=16", "05-Insertion sort.pdf#page=17", "05-Insertion sort.pdf#page=22", "05-Insertion sort.pdf#page=23"]
---

# Insertion sort

Le sezioni seguono l'ordine delle slide: idea (p. 4) → pseudocodice e traccia (pp. 5–15) → correttezza (p. 16) → analisi di complessità (pp. 17–22) → implementazione C++ (p. 23).

## Problema risolto

[[ordinamento]]: data una sequenza di $n$ valori $(a_1, \dots, a_n)$, determinare una permutazione $(a'_1, \dots, a'_n)$ tale che $a'_1 \le a'_2 \le \dots \le a'_n$ ([[05-Insertion sort.pdf#page=2]]).

## Idea

> 📄 Fonte: [[05-Insertion sort.pdf#page=4]]

- Insertion sort è un algoritmo che **considera un valore alla volta** e lo **inserisce nella corretta posizione tra i valori che lo precedono**.
- È un algoritmo che ordina i valori **sul posto** (*in place*): i valori sono riordinati all'interno dell'array stesso, con **al più un numero costante** di essi memorizzati al di fuori dell'array in ogni momento.

> 🧩 Esempio mio per fissare l'idea: è il modo in cui si ordinano le carte da gioco in mano. Si prende una carta alla volta e la si fa scorrere verso sinistra finché non trova il suo posto tra quelle già ordinate.

## Pseudocodice

> 📄 Fonte: [[05-Insertion sort.pdf#page=5]] (riportato fedelmente; numeri di riga come nella tabella dei costi di [[05-Insertion sort.pdf#page=17]], dove la riga 3 è il commento e non ha costo)

```
Insertion-Sort (A)
1  for j ← 2 to length[A]
2      do key ← A[j]
3         // Insert A[j] into A[1..j-1]
4         i ← j-1
5         while i>0 and A[i]>key
6             do A[i+1] ← A[i]
7                i ← i-1
8         A[i+1] ← key
```

Significato delle variabili:
- $j$ = indice dell'elemento da inserire (la «carta» presa in mano); il ciclo parte da 2 perché $A[1]$ da solo è già ordinato;
- $key$ = copia di $A[j]$, che durante gli spostamenti verrebbe sovrascritto;
- $i$ = indice che scorre verso sinistra in $A[1..j-1]$ cercando il posto di $key$.

La condizione `i>0 and A[i]>key` sfrutta il **corto circuito** di `and` ([[a1-indicazioni_psuedocodice.pdf#page=4]]): quando $i = 0$ il confronto `A[0] > key` non viene valutato, ed è giusto così perché $A[0]$ non esiste (indici da 1).

> ⚠️ Contraddizione (di notazione): la slide usa `do` e il commento `//` (stile della 2ª edizione del Cormen), mentre le [[pseudocodice|convenzioni del corso]] prevedono commenti con $\triangleright$ e nessun `do`. Il significato è lo stesso.

## Esempio di esecuzione

![[animazione-insertion-sort.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo, sull'array ⟨5, 2, 4, 6, 1, 3⟩ delle slide (pp. 5–15), un fotogramma per ogni riga eseguita: `key`, i puntatori `i` e `j`, il confronto del `while` (rosso = sposto, azzurro = mi fermo), la parte già ordinata $A[1..j-1]$ in verde (l'invariante di p. 16) e la riga di pseudocodice corrente evidenziata. Ogni fotogramma riporta in basso il numero del passo e cosa succede.


> 📄 Fonte: [[05-Insertion sort.pdf#page=5]]–[[05-Insertion sort.pdf#page=15]] (una slide per passo; in rosso l'elemento $key$ e la sua posizione)

Array iniziale: $A = \langle 5, 2, 4, 6, 1, 3 \rangle$.

![[05-insertion-sort-p5-traccia-inizio.png]]
*Stato iniziale: casella `key` vuota e array ⟨5, 2, 4, 6, 1, 3⟩. ([[05-Insertion sort.pdf#page=5]])*

| Slide | $j$ | $key$ | Cosa succede | $A$ dopo l'iterazione |
|-------|-----|-------|--------------|------------------------|
| [[05-Insertion sort.pdf#page=6\|p. 6]], [[05-Insertion sort.pdf#page=7\|7]] | 2 | 2 | 5 > 2: il 5 scorre a destra, 2 va in $A[1]$ | ⟨**2**, 5, 4, 6, 1, 3⟩ |
| [[05-Insertion sort.pdf#page=8\|p. 8]], [[05-Insertion sort.pdf#page=9\|9]] | 3 | 4 | 5 > 4 scorre; 2 ≤ 4 si ferma: 4 va in $A[2]$ | ⟨2, **4**, 5, 6, 1, 3⟩ |
| [[05-Insertion sort.pdf#page=10\|p. 10]], [[05-Insertion sort.pdf#page=11\|11]] | 4 | 6 | 5 ≤ 6: nessuno spostamento | ⟨2, 4, 5, **6**, 1, 3⟩ |
| [[05-Insertion sort.pdf#page=12\|p. 12]], [[05-Insertion sort.pdf#page=13\|13]] | 5 | 1 | 6, 5, 4, 2 scorrono tutti; $i$ arriva a 0 | ⟨**1**, 2, 4, 5, 6, 3⟩ |
| [[05-Insertion sort.pdf#page=14\|p. 14]], [[05-Insertion sort.pdf#page=15\|15]] | 6 | 3 | 6, 5, 4 scorrono; 2 ≤ 3 si ferma | ⟨1, 2, **3**, 4, 5, 6⟩ |

![[05-insertion-sort-p15-traccia-completa.png]]
*Traccia completa: ogni riga è lo stato dopo un'iterazione del `for`, con il valore di `key` a sinistra. ([[05-Insertion sort.pdf#page=15]])*

> 🧩 Derivazione mia — numero di test del `while` per ogni $j$ (servirà nell'analisi): $t_2 = 2$, $t_3 = 2$, $t_4 = 1$, $t_5 = 5$, $t_6 = 4$. Ogni test vero sposta un elemento; l'ultimo test, falso, ferma il ciclo. Per $j = 5$: quattro test veri (6, 5, 4, 2 > 1) più il test con $i = 0$. Verificato con [[ordinamento.py]], che controlla anche l'invariante a ogni iterazione.

## Correttezza

> 📄 Fonte: [[05-Insertion sort.pdf#page=16]]

**Invariante:** all'inizio di ciascuna iterazione del ciclo `for`, la sottosequenza $A[1..j-1]$ consiste degli **elementi originali** di $A[1..j-1]$, ma **ordinati** in senso crescente.

- **Inizializzazione** — l'invariante è vero prima della prima iterazione: per $j = 2$ la sottosequenza $A[1..j-1]$ è costituita solo da $A[1]$, che è ovviamente una sequenza ordinata.
- **Conservazione** — un'iterazione del ciclo conserva la verità dell'invariante: l'elemento $A[j]$ viene inserito in modo da mantenere la sequenza $A[1..j]$ ordinata.
- **Conclusione** — l'invariante prova che l'algoritmo è corretto: il ciclo termina quando $j = n + 1$, ovvero quando la sequenza $A[1..n]$ è ordinata.

![[05-insertion-sort-p16-invariante.png]]

> 🧩 Derivazione mia (la conservazione nella slide è detta a parole; ecco perché è vera). All'inizio dell'iterazione $j$, $A[1..j-1]$ è ordinato. Il `while` (righe 5–7) sposta di una posizione a destra, **conservandone l'ordine**, tutti gli elementi consecutivi di coda che sono $> key$, e si ferma al primo indice $i$ con $A[i] \le key$ (oppure a $i = 0$). A quel punto:
> - $A[1..i]$ contiene elementi $\le key$, già ordinati;
> - $A[i+2..j]$ contiene gli elementi spostati, tutti $> key$, ordinati;
> - la riga 8 mette $key$ in $A[i+1]$.
>
> Quindi $A[1..j]$ è ordinato e contiene esattamente gli elementi originali di $A[1..j]$ (nessuno perso: $A[j]$ era salvato in $key$). È l'invariante per $j + 1$.
>
> **Terminazione** ([[invariante-di-ciclo]] richiede anche questa): il `for` fa $n - 1$ iterazioni; il `while` termina perché $i$ cala di 1 a ogni giro e si ferma al più a $i = 0$ (variante: $i$).

## Complessità

### Tabella dei costi
> 📄 Fonte: [[05-Insertion sort.pdf#page=17]]

| Riga | Istruzione | Costo | Numero di esecuzioni |
|------|------------|-------|----------------------|
| 1 | `for j ← 2 to length[A]` | $c_1$ | $n$ |
| 2 | `do key ← A[j]` | $c_2$ | $n - 1$ |
| 3 | `// Insert A[j] into A[1..j-1]` | — | — |
| 4 | `i ← j-1` | $c_4$ | $n - 1$ |
| 5 | `while i>0 and A[i]>key` | $c_5$ | $\sum_{j=2}^{n} t_j$ |
| 6 | `do A[i+1] ← A[i]` | $c_6$ | $\sum_{j=2}^{n} (t_j - 1)$ |
| 7 | `i ← i-1` | $c_7$ | $\sum_{j=2}^{n} (t_j - 1)$ |
| 8 | `A[i+1] ← key` | $c_8$ | $n - 1$ |

**$t_j$ è il numero di volte che viene eseguito il test del ciclo `while`** (per quel valore di $j$).

![[05-insertion-sort-p17-tabella-costi.png]]

> 🧩 Derivazione mia — perché quei numeri di esecuzioni ([[tempo-di-esecuzione]]):
> - riga 1: il test del `for` è vero per $j = 2, \dots, n$ ($n - 1$ volte) e falso una volta ($j = n + 1$) → $n$;
> - righe 2, 4, 8: una volta per iterazione del `for` → $n - 1$;
> - righe 6, 7: il corpo del `while` si esegue una volta in meno del suo test (l'ultimo test è falso) → $t_j - 1$ per ogni $j$.

### Formula generale
> 📄 Fonte: [[05-Insertion sort.pdf#page=18]]

> 🧮 Formula chiave:
$$
T(n) = c_1 n + c_2 (n-1) + c_4 (n-1) + c_5 \sum_{j=2}^{n} t_j + c_6 \sum_{j=2}^{n} (t_j - 1) + c_7 \sum_{j=2}^{n} (t_j - 1) + c_8 (n-1)
$$

Il tempo dipende dall'**input**, non solo da $n$: le tre sommatorie (cerchiate in [[05-Insertion sort.pdf#page=19]]) dipendono da quanti elementi scorrono, cioè da quanto l'array è già in ordine.

### Caso migliore
> 📄 Fonte: [[05-Insertion sort.pdf#page=20]]

Il **caso migliore** si verifica quando il vettore è **già ordinato** ($t_j = 1$):
$$ T(n) = c_1 n + c_2(n-1) + c_4(n-1) + c_5(n-1) + c_8(n-1) = an + b $$
Il tempo di esecuzione è **funzione lineare** di $n$.

> 🧩 Derivazione mia:
$$
\begin{aligned}
t_j &= 1 && \text{il primo test trova } A[j-1] \le key \text{ e fallisce} \\
\textstyle\sum_{j=2}^{n} t_j &= n - 1, \qquad \textstyle\sum_{j=2}^{n} (t_j - 1) = 0 && \text{righe 6 e 7 mai eseguite} \\
T(n) &= (c_1 + c_2 + c_4 + c_5 + c_8)\, n - (c_2 + c_4 + c_5 + c_8) && \text{raccolgo } n \\
     &= an + b = \Theta(n) && a = c_1 + c_2 + c_4 + c_5 + c_8 > 0,\ b = -(c_2 + c_4 + c_5 + c_8)
\end{aligned}
$$

![[05-insertion-sort-p20-caso-migliore.png]]

### Caso peggiore
> 📄 Fonte: [[05-Insertion sort.pdf#page=21]], [[05-Insertion sort.pdf#page=22]]

Il **caso peggiore** si verifica quando il vettore è **ordinato in senso decrescente**. Si usano le due sommatorie ([[05-Insertion sort.pdf#page=21]]):
$$ \sum_{j=2}^{n} j = \frac{n(n+1)}{2} - 1 \qquad\qquad \sum_{j=2}^{n} (j-1) = \frac{n(n-1)}{2} $$
e si ottiene ([[05-Insertion sort.pdf#page=22]]):
$$
T(n) = c_1 n + c_2(n-1) + c_4(n-1) + c_5\left(\frac{n(n+1)}{2} - 1\right) + c_6 \frac{n(n-1)}{2} + c_7 \frac{n(n-1)}{2} + c_8(n-1)
$$
$$ T(n) = an^2 + bn + c $$
Il tempo di esecuzione è **funzione quadratica** di $n$.

> 🧩 Derivazione mia — perché $t_j = j$ e come si arriva ad $an^2 + bn + c$:
$$
\begin{aligned}
t_j &= j && key \text{ è minore di tutti i } j-1 \text{ elementi di } A[1..j-1]\text{: } j-1 \text{ test veri} + 1 \text{ falso } (i = 0) \\
\textstyle\sum_{j=2}^{n} j &= \textstyle\sum_{j=1}^{n} j - 1 = \frac{n(n+1)}{2} - 1 && \text{Gauss, tolgo il termine } j = 1 \\
\textstyle\sum_{j=2}^{n} (j-1) &= \textstyle\sum_{k=1}^{n-1} k = \frac{(n-1)n}{2} && k = j - 1 \\
T(n) &= \frac{c_5 + c_6 + c_7}{2}\, n^2 + \left(c_1 + c_2 + c_4 + \frac{c_5 - c_6 - c_7}{2} + c_8\right) n - (c_2 + c_4 + c_5 + c_8) && \text{sviluppo e raccolgo} \\
     &= an^2 + bn + c = \Theta(n^2) && a = \tfrac{c_5 + c_6 + c_7}{2} > 0
\end{aligned}
$$
>
> **Sanity check** ([[ordinamento.py]]): per $n = 5$ decrescente $\sum t_j = 14 = \frac{5\cdot6}{2} - 1$ e $\sum(t_j - 1) = 10 = \frac{5\cdot4}{2}$; per $n = 100$: 5049 e 4950. Sull'array della traccia $\sum t_j = 2+2+1+5+4 = 14$, un caso intermedio.
> **Ipotesi:** [[modello-ram]], costo costante $c_i$ per riga; caso peggiore = ogni $key$ è minore di tutti gli elementi che lo precedono.

![[05-insertion-sort-p22-caso-peggiore.png]]

![[grafico-insertion-sort-casi.svg]]
> 🧩 Grafico generato da me ([[genera_grafici_as.py]]) dalle formule di pp. 20–22: il numero totale di test del `while` è $n - 1$ nel caso migliore e $\frac{n(n+1)}{2} - 1$ nel peggiore, che per $n$ grande si sovrappone a $n^2/2$ (linea tratteggiata). È il confronto lineare/quadratico delle slide.

> 🎯 Esame: tabella dei costi, significato di $t_j$, caso migliore $\Theta(n)$ (già ordinato), caso peggiore $\Theta(n^2)$ (ordinato al contrario), con le due sommatorie. È il costo «proporzionale a $n^2$» citato in [[01-Introduzione.pdf#page=11]].

**Spazio:** $\Theta(1)$ oltre all'array ($key$, $i$, $j$) — è la proprietà «sul posto» di p. 4.

## Implementazione in C++

> 📄 Fonte: [[05-Insertion sort.pdf#page=23]] (codice riportato fedelmente, accanto allo pseudocodice)

```cpp
template <typename T>
void InsertionSort (vector<T> A)
{
    for (int j=1; j<A.size(); j++)
    {
        T key = A[j];
        // Insert A[j] into A[1..j-1]
        int i = j-1;
        while (i>=0 && A[i]>key)
        {
            A[i+1] = A[i];
            i--;
        }
        A[i+1] = key;
    }
}
```

> 🧩 Derivazione mia — traduzione degli indici: in C++ gli indici partono da 0, quindi `j` parte da 1 (il secondo elemento, come `j ← 2`), la guardia `i>0` diventa `i>=0` e il commento andrebbe letto come «A[0..j-1]».

> ⚠️ Contraddizione (🧩 osservazione mia sul codice della slide): `vector<T> A` è passato **per valore**, quindi la funzione ordina una **copia** e il vettore del chiamante resta invariato. Per ordinare davvero serve il passaggio per riferimento, `vector<T>& A`. Nello pseudocodice il problema non si pone: gli array sono aggregati passati per riferimento ([[a1-indicazioni_psuedocodice.pdf#page=3]]).

![[05-insertion-sort-p23-implementazione-cpp.png]]

## Proprietà

- **Sul posto** (in place) — dalla fonte ([[05-Insertion sort.pdf#page=4]]).
- **Stabile** — 🧩 derivabile dallo pseudocodice: il `while` sposta solo gli elementi **strettamente** maggiori di $key$ ($A[i] > key$), quindi un elemento uguale già a sinistra non viene scavalcato e le chiavi uguali mantengono l'ordine di partenza. Verificato in [[ordinamento.py]].
- **Adattivo** — 🧩 derivabile dall'analisi: più l'input è vicino a essere ordinato, più il costo si avvicina al caso migliore lineare.

## Connessioni

- [[selection-sort]] — l'altro ordinamento quadratico della lezione: costo $\Theta(n^2)$ anche nel caso migliore
- [[invariante-di-ciclo]] — l'invariante di p. 16 è l'esempio canonico
- [[analisi-del-costo-riga-per-riga]] — stessa tecnica della somma iterativa, ma qui $t_j$ dipende dall'input
- [[casi-di-complessita]] — caso migliore e peggiore con ordini di crescita diversi
- [[efficienza-degli-algoritmi]] — $n^2$ contro $n\log n$ di [[merge-sort]]
- [[quicksort]] — stesso caso peggiore $\Theta(n^2)$, ma sul vettore ordinato, che per insertion sort è il caso migliore ([[07-Quicksort.pdf#page=14]])

## Fonti

- [[lezione-05-insertion-sort]]
- [[05-Insertion sort.pdf#page=4]]–[[05-Insertion sort.pdf#page=23]]

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_
_Aggiornato: 2026-10-01 — aggiunta l'animazione dell'algoritmo_
_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf e 07-Quicksort.pdf_
