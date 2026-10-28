---
tipo: entità
categoria: struttura-dati
fonti_pdf: ["04-Strutture dati elementari.pdf#page=25", "04-Strutture dati elementari.pdf#page=26", "04-Strutture dati elementari.pdf#page=28", "04-Strutture dati elementari.pdf#page=29"]
---

# Pila (stack) — LIFO

## Cos'è

> 📄 Fonte: [[04-Strutture dati elementari.pdf#page=25]]

A volte l'ordine con cui si recuperano i dati è **indipendente dal loro contenuto** e dipende solo da **quando sono arrivati**. Una **pila** supporta operazioni **last-in, first-out** (LIFO):
- $Push(x, s)$ — inserisce l'elemento $x$ **in cima** alla pila $s$;
- $Pop(s)$ — restituisce (e rimuove) l'elemento **in cima** alla pila $s$.

## Rappresentazione in memoria

> 📄 Fonte: [[04-Strutture dati elementari.pdf#page=28]]

Le pile si rappresentano più facilmente con un **array**, con push/pop che **incrementano/decrementano un contatore**. Tutte le operazioni costano $O(1)$, sia con array sia con liste.

![[04-strutture-dati-p26-stack-su-array.png]]
*Figura 10.1 del Cormen ([[04-Strutture dati elementari.pdf#page=26]]).*

Didascalia della figura (tradotta): implementazione di una pila $S$ con un array. Gli elementi della pila sono solo nelle posizioni in grigio chiaro. (a) $S$ ha 4 elementi; l'elemento in cima è 9. (b) $S$ dopo le chiamate $\text{PUSH}(S, 17)$ e $\text{PUSH}(S, 3)$. (c) $S$ dopo la chiamata $\text{POP}(S)$, che ha restituito l'elemento 3, il più recentemente inserito. L'elemento 3 compare ancora nell'array, ma non è più nella pila: la cima è l'elemento 17.

## Esempio di esecuzione

| Stato | $S[1..7]$ | $S.top$ | Contenuto della pila |
|-------|-----------|---------|----------------------|
| (a) | 15 6 2 9 · · · | 4 | ⟨15, 6, 2, 9⟩ |
| (b) dopo PUSH 17, PUSH 3 | 15 6 2 9 17 3 · | 6 | ⟨15, 6, 2, 9, 17, 3⟩ |
| (c) dopo POP → 3 | 15 6 2 9 17 3 · | 5 | ⟨15, 6, 2, 9, 17⟩ |

Verificata con [[strutture_elementari.py]].

## Operazioni (pseudocodice)

> 📚 Fonte esterna: le slide non riportano lo pseudocodice; quello qui sotto è del libro di testo del corso (Cormen, 3ª ed., § 10.1), scritto nelle [[pseudocodice|convenzioni del corso]]. Il controllo di underflow è del libro; quello di overflow è un'aggiunta mia (🧩).

```
STACK-EMPTY(S)
1  if S.top = 0
2      return true
3  else return false

PUSH(S, x)
1  if S.top = length[S]
2      error "overflow"          ▷ 🧩 controllo mio
3  S.top ← S.top + 1
4  S[S.top] ← x

POP(S)
1  if STACK-EMPTY(S)
2      error "underflow"
3  else S.top ← S.top − 1
4      return S[S.top + 1]
```

Ogni operazione esegue un numero costante di righe → $O(1)$, come dice [[04-Strutture dati elementari.pdf#page=28]].

## Perché pile e code

> 📄 Fonte: [[04-Strutture dati elementari.pdf#page=29]]

Entrambe sono adatte a un contenitore in cui l'ordine non conta, ma a volte conta. Le file in banca sono code, mentre «food in my refrigerator is treated as a stack». **L'intera differenza tra visita in profondità (DFS) e in ampiezza (BFS)** sta nel fatto che i vertici da elaborare siano tenuti in una **pila** o in una **coda**.

## Connessioni

- [[coda]] — il contenitore FIFO
- [[tipo-di-dato-astratto]] — Push/Pop sono l'esempio di operazioni astratte ([[04-Strutture dati elementari.pdf#page=4]])
- [[array]], [[lista-concatenata]] — implementazioni
- [[iterazione-e-ricorsione]] — la pila di sistema che contiene i record di attivazione delle chiamate ricorsive
- [[tracce-pila-e-coda]] — esercizi

## Fonti

- [[lezione-04-strutture-dati-elementari]]
- [[04-Strutture dati elementari.pdf#page=24]] (intestazione «Containers»), [[04-Strutture dati elementari.pdf#page=25]], [[04-Strutture dati elementari.pdf#page=26]], [[04-Strutture dati elementari.pdf#page=28]], [[04-Strutture dati elementari.pdf#page=29]]

_Aggiornato: 2026-09-26 — ingest 04-Strutture dati elementari.pdf_

<!-- nav:inizio -->
---
**Lezione 04 · pagina 7 di 9** · ← [[lista-concatenata|Lista concatenata (semplice e doppia)]] · [[lezioni|Indice]] · [[coda|Coda (queue) — FIFO]] →
<!-- nav:fine -->
