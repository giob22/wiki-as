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

## Trappole

- Dimenticare la terminazione (si ottiene solo la correttezza parziale).
- Invariante troppo debole: la conclusione non dà la post-condizione.
- Valori iniziali sbagliati dell'indice (vedi il refuso «$i = 0$»).
- Usare esempi o test come se fossero una dimostrazione ([[03-Analisi di algoritmi.pdf#page=15]]).

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_
