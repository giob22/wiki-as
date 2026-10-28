---
tipo: esercizio
argomento: "correttezza con invariante di ciclo e induzione"
difficoltà: media
---

# Dimostrazioni di correttezza (invariante e induzione)

## Metodo

**Algoritmo iterativo** ([[03-Analisi di algoritmi.pdf#page=16]]):
1. Scrivere pre- e post-condizione.
2. Proporre un invariante che, unito alla condizione d'uscita, implichi la post-condizione.
3. Dimostrare **inizializzazione**, **conservazione**, **conclusione**.
4. Dimostrare la **terminazione** con una funzione variante intera $\ge 0$ strettamente decrescente.

**Algoritmo ricorsivo** ([[03-Analisi di algoritmi.pdf#page=18]]):
1. Specifiche (pre/post).
2. Misura ben fondata che decresce a ogni chiamata.
3. Casi base corretti.
4. Passo induttivo: assumendo corrette le chiamate su input più piccoli, dimostrare corretto il risultato.
5. Terminazione dalla decrescita della misura.

## Strumenti usati

- [[invariante-di-ciclo]], [[correttezza-per-induzione]]

## Casi svolti

### Caso 1 — somma iterativa ([[03-Analisi di algoritmi.pdf#page=17]])
- Pre: $n \in \mathbb N$. Post: restituisce $\sum_{k=1}^n k$.
- Invariante: all'inizio dell'iterazione $i$, $s = \sum_{k=1}^{i-1} k$.
- Inizializzazione: $i = 1$, $s = 0$ = somma vuota ✓ (la slide scrive «$i = 0$»: refuso).
- Conservazione: $s \leftarrow s + i$ porta $s$ a $\sum_{k=1}^{i} k$, invariante per $i + 1$ ✓.
- Conclusione: all'uscita $i = n + 1$, quindi $s = \sum_{k=1}^{n} k$ ✓.
- Terminazione: $v = n - i + 1$, cala di 1 a ogni iterazione, il ciclo esce a $v = 0$ ✓.

### Caso 2 — somma ricorsiva ([[03-Analisi di algoritmi.pdf#page=19]])
- Misura $n$; base $S(0) = 0$ ✓; passo: $S(n) = n + S(n-1) = n + \frac{(n-1)n}{2} = \frac{n(n+1)}{2}$ ✓; terminazione: $n - 1 < n$ ✓. Passaggi in [[correttezza-per-induzione]].

### Caso 3 — OptimalTSP ed ExhaustiveScheduling
> 🧩 Mio. Invariante del ciclo sulle possibilità (permutazioni / sottoinsiemi): «la migliore soluzione trovata finora è ottima tra quelle esaminate». Inizializzazione banale (nessuna esaminata, $d = \infty$ o $j = 0$), conservazione per l'aggiornamento condizionale, conclusione perché alla fine sono state esaminate tutte, terminazione perché sono in numero finito ($n!$ o $2^n$). → [[optimal-tsp]], [[exhaustive-scheduling]]

### Caso 4 — OptimalScheduling
> 🧩 Mio. Induzione sul numero di intervalli con argomento di scambio: esiste sempre una soluzione ottima che contiene il job che finisce per primo. → [[optimal-scheduling]]

### Caso 5 — insertion sort ([[05-Insertion sort.pdf#page=16]])
- Invariante (dalla slide): all'inizio di ogni iterazione del `for`, $A[1..j-1]$ contiene gli elementi originali di $A[1..j-1]$, ordinati.
- Inizializzazione: $j = 2$, $A[1..1]$ ha un solo elemento ✓. Conservazione: $A[j]$ è inserito mantenendo ordinato $A[1..j]$ ✓. Conclusione: all'uscita $j = n + 1$, $A[1..n]$ è ordinato ✓.
- Passaggi della conservazione e terminazione del `while` → [[insertion-sort]] § Correttezza.

### Caso 6 — selection sort (esercizio 2.2.2, [[05-Insertion sort.pdf#page=26]])
> 🧩 Mio (la slide chiede «Dimostrarne la correttezza» senza soluzione). Invariante esterno: $A[1..i-1]$ contiene gli $i - 1$ elementi più piccoli, ordinati; invariante interno: $A[min]$ è il minimo di $A[i..j-1]$. Dimostrazione completa, e perché basta arrivare a $n - 1$ → [[selection-sort]] § Correttezza.

### Caso 7 — Merge ([[06-Merge Sort (1).pdf#page=19]], [[06-Merge Sort (1).pdf#page=20]])
- Pre: $A[p..q]$ e $A[q+1..r]$ ordinati. Post: $A[p..r]$ ordinato con gli stessi elementi.
- Invariante (dalla slide): all'inizio di ogni iterazione del `for` finale, $A[p..k-1]$ contiene i $k - p$ elementi più piccoli di $L$ ed $R$, ordinati; $L[i]$ e $R[j]$ sono i più piccoli non ancora ricopiati.
- Inizializzazione: $k = p$, sottosequenza vuota; $L[1]$, $R[1]$ minimi ✓. Conservazione: si copia $\min(L[i], R[j])$, che è il minimo dei rimasti ✓. Conclusione: $k = r + 1$, $A[p..r]$ contiene tutti gli $r - p + 1$ elementi ordinati; in $L$ e $R$ restano le sentinelle ✓.
- Perché il minimo dei rimasti è $\min(L[i], R[j])$ e perché le sentinelle non vengono copiate (🧩) → [[merge]] § Correttezza.

### Caso 8 — Merge-Sort (🧩, la slide non lo dimostra)
- Induzione forte su $n = r - p + 1$: base $n \le 1$ (già ordinato); passo: le metà hanno $\lceil n/2 ceil$ e $\lfloor n/2 floor$ elementi, meno di $n$, quindi sono ordinate per ipotesi induttiva e Merge le fonde. → [[merge-sort]] § Correttezza.

### Caso 9 — Partition ([[07-Quicksort 1.pdf#page=13]])
- Invariante (dalla slide): $A[k] \le x$ per $p \le k \le i$; $A[k] > x$ per $i+1 \le k \le j-1$; $A[k] = x$ per $k = r$.
- Inizializzazione: $i = p - 1$, $j = p$, prime due aree vuote ✓.
- Conservazione (🧩, la slide la enuncia soltanto): se $A[j] > x$ cresce solo la 2ª area; se $A[j] \le x$, $i$ avanza e lo scambio porta $A[j]$ in coda alla 1ª area e il primo elemento della 2ª in coda alla 2ª ✓.
- Conclusione: $j = r$; lo scambio $A[i+1] \leftrightarrow A[r]$ mette il pivot tra le due parti, $q = i + 1$ ✓. → [[partition]] § Correttezza.

### Caso 10 — Quicksort, Torre di Hanoi, Nuts and Bolts (🧩)
- Quicksort: induzione forte su $n$, usando la proprietà di Partition; il pivot è escluso dalle chiamate, quindi la dimensione cala → [[quicksort]] § Correttezza.
- Torre di Hanoi: induzione su $n$; la mossa del disco $n$ è lecita perché gli altri sono tutti su `via` → [[torre-di-hanoi]] § Correttezza.
- Nuts and Bolts: invariante del metodo quadratico; induzione per il randomizzato, con $|D_<| = |B_<|$ → [[nuts-and-bolts]].

### Caso 11 — alberi e BST (lezioni 08–09)
- **Albero con $n$ nodi ha $n - 1$ archi:** induzione su $n$, togliendo una foglia (🧩) → [[albero]] § Derivazione.
- **Visita in ordine ordinata:** induzione sul numero di nodi, con la proprietà del BST ([[09-Alberi binari ricerca.pdf#page=7]]) → [[inorder-tree-walk]] § Correttezza.
- **Tree-Search:** induzione sull'altezza; invariante della versione iterativa «se la chiave c'è, è nel sottoalbero di $x$» → [[tree-search]] § Correttezza.
- **Tree-Minimum:** invariante «il minimo è nel sottoalbero di $x$» → [[tree-minimum-maximum]] § Correttezza.
- **Tree-Insert e Tree-Delete:** la proprietà del BST resta vera; nel terzo caso di Delete la chiave del successore è $\ge$ del sottoalbero sinistro e $\le$ del destro → [[tree-insert]], [[tree-delete]] § Correttezza.

## Trappole

- Dimenticare la terminazione (si ottiene solo la correttezza parziale).
- Invariante troppo debole: la conclusione non dà la post-condizione.
- Valori iniziali sbagliati dell'indice (vedi il refuso «$i = 0$»).
- Usare esempi o test come se fossero una dimostrazione ([[03-Analisi di algoritmi.pdf#page=15]]).
- Invariante con più affermazioni (Merge, Partition): la conservazione va dimostrata per **ciascuna**, in **ciascun** ramo dell'`if`.
- Dimenticare il passo dopo il ciclo (lo scambio finale di Partition) nella conclusione.

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_
_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf e 07-Quicksort.pdf (casi 7–10)_
_Aggiornato: 2026-10-10 — link ripuntati alla versione aggiornata delle slide 06-Merge Sort (1).pdf_
_Aggiornato: 2026-10-14 — link ripuntati alla versione aggiornata delle slide 07-Quicksort 1.pdf_
_Aggiornato: 2026-10-28 — ingest 08-Grafi e alberi.pdf e 09-Alberi binari ricerca.pdf_

<!-- nav:inizio -->
---
**Lezione 03 · pagina 10 di 13** · ← [[correttezza-per-induzione|Correttezza degli algoritmi ricorsivi (per induzione)]] · [[lezioni|Indice]] · [[analisi-del-costo-riga-per-riga|Analisi del costo riga per riga]] →
<!-- nav:fine -->
