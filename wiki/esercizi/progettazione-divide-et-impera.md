---
tipo: esercizio
argomento: "progettazione di algoritmi divide et impera"
difficoltà: media
---

# Progettazione di algoritmi divide et impera

## Metodo

> 🧩 Procedura mia, ricavata dallo schema delle lezioni 06–07 ([[06-Merge Sort.pdf#page=14]], [[07-Quicksort.pdf#page=3]]):
1. **Specifica:** input, output, operazioni ammesse (es. solo confronti dado–bullone).
2. **Divide:** come si ottengono sottoproblemi **dello stesso tipo** e più piccoli; quanti ($a$) e di che dimensione ($n/b$, oppure $n - 1$).
3. **Conquer:** chiamate ricorsive; **caso base** esplicito.
4. **Combine:** come si ricompongono le soluzioni; costo $C(n)$.
5. **Pseudocodice** secondo le [[pseudocodice|convenzioni del corso]].
6. **Correttezza** per [[correttezza-per-induzione|induzione]] sulla dimensione.
7. **Complessità:** ricorrenza $T(n) = aT(n/b) + D(n) + C(n)$ e soluzione con [[teorema-dell-esperto]], [[metodo-albero-di-ricorrenza]] o srotolamento.

## Strumenti usati

- [[divide-et-impera]], [[equazioni-di-ricorrenza]], [[correttezza-per-induzione]]
- [[partition]] come «mattone» per dividere attorno a un pivot; [[randomizzazione]] per il pivot

## Casi svolti

### Caso 1 — Torre di Hanoi
**Traccia:** [[06-Merge Sort.pdf#page=2]]–[[06-Merge Sort.pdf#page=4]] (S&T: spostare tre dischi da A a C; nelle slide c'è solo la sequenza delle mosse).

> 🧩 Svolgimento mio.
> 1. **Specifica:** $n$ dischi su A, dal più grande al più piccolo; un disco per volta, mai su uno più piccolo; arrivo su C.
> 2. **Divide:** il disco più grande può muoversi solo quando gli altri $n - 1$ sono tutti sul terzo piolo. Quindi: $n - 1$ dischi da A a B, il disco $n$ da A a C, $n - 1$ dischi da B a C. Due sottoproblemi di dimensione $n - 1$.
> 3. **Caso base:** $n = 0$, nessuna mossa.
> 4. **Combine:** nessuno, la soluzione è la sequenza delle mosse.
> 5. **Pseudocodice:** `HANOI(n, da, a, via)` in [[torre-di-hanoi]].
> 6. **Correttezza:** induzione su $n$ ([[torre-di-hanoi]] § Correttezza).
> 7. **Complessità:** $M(n) = 2M(n-1) + 1$, $M(0) = 0$ ⇒ $M(n) = 2^n - 1$ (srotolamento e serie geometrica, in [[torre-di-hanoi]] § Complessità). Il teorema dell'esperto **non** si applica: la dimensione cala di 1, non di un fattore $b$.

**Risultato:** 7 mosse per 3 dischi, come nella figura di [[06-Merge Sort.pdf#page=4]]; $\Theta(2^n)$ in generale.

### Caso 2 — Nuts and Bolts
**Traccia:** [[07-Quicksort.pdf#page=25]] (algoritmo $O(n^2)$, poi randomizzato $O(n\log n)$ atteso).

> 🧩 Svolgimento mio.
> 1. **Specifica:** $n$ dadi e $n$ bulloni di larghezze diverse, a coppie corrispondenti; unico test ammesso dado contro bullone (più largo / più stretto / combacia).
> 2. **Soluzione $O(n^2)$** (non divide et impera): per ogni bullone si provano i dadi rimasti; al più $\sum_{m=1}^{n} m = \frac{n(n+1)}{2}$ test.
> 3. **Divide (randomizzato):** un dado $d$ a caso fa da pivot per i bulloni ($B_<$, gemello $b$, $B_>$); il gemello $b$ fa da pivot per i dadi ($D_<$, $D_>$). È [[partition]] due volte.
> 4. **Conquer:** $(D_<, B_<)$ e $(D_>, B_>)$ sono istanze dello stesso problema; caso base: insiemi vuoti.
> 5. **Combine:** nessuno (come in [[quicksort]]).
> 6. **Correttezza:** induzione su $n$; l'osservazione chiave è $|D_<| = |B_<|$ con le stesse larghezze.
> 7. **Complessità:** $T(n) = T(k) + T(n-k-1) + (2n-1)$ con $k$ casuale uniforme: è la ricorrenza di [[quicksort-randomizzato]], tempo atteso $O(n\log n)$; caso peggiore $\Theta(n^2)$.

Pseudocodice, animazioni e misure in [[nuts-and-bolts]].

**Risultato:** $O(n^2)$ deterministico; $O(n\log n)$ atteso con il pivot casuale.

### Caso 3 — Massimo sottoarray
**Traccia:** [[06-Merge Sort.pdf#page=16]] (S&T, solo titolo e rimando al libro, cap. 4.1).

Non svolto: le slide non danno né il testo né la soluzione. Enunciato (📚 Cormen §4.1) in [[massimo-sottoarray]]. TODO: da espandere se una lezione presenterà la soluzione.

## Trappole

- Sottoproblemi che **non** sono istanze dello stesso problema: in Nuts and Bolts bisogna verificare che $D_<$ e $B_<$ si corrispondano esattamente.
- Dimenticare il caso base, o sceglierne uno che la divisione non raggiunge.
- Applicare il teorema dell'esperto a ricorrenze con $T(n-1)$ (Hanoi, quicksort sbilanciato): $b$ deve essere una costante $> 1$.
- Confondere tempo **atteso** (randomizzato, ogni input) con caso **medio** (media sugli input) → [[randomizzazione]].

_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf e 07-Quicksort.pdf_
