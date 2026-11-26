---
tipo: entità
categoria: struttura-dati
fonti_pdf: ["04-Strutture dati elementari.pdf#page=25", "04-Strutture dati elementari.pdf#page=27", "04-Strutture dati elementari.pdf#page=28"]
---

# Coda (queue) — FIFO

## Cos'è · [[04-Strutture dati elementari.pdf#page=25|p. 25]]

Una **coda** supporta operazioni **first-in, first-out** (FIFO):
- $Enqueue(x, q)$ — inserisce l'elemento $x$ **in fondo** alla coda $q$;
- $Dequeue(q)$ — restituisce (e rimuove) l'elemento **in testa** alla coda $q$.

## Rappresentazione in memoria · [[04-Strutture dati elementari.pdf#page=27|p. 27]], [[04-Strutture dati elementari.pdf#page=28|28]]

Le code si rappresentano più facilmente con una **lista concatenata**, con enqueue/dequeue che operano alle **estremità opposte** della lista. Tutte le operazioni costano $O(1)$, sia con array sia con liste.

Implementazione su **array circolare** (Figura 10.2 del Cormen):

![[04-strutture-dati-p27-coda-su-array.png]]

Didascalia della figura (tradotta): una coda implementata con un array $Q[1..12]$. Gli elementi della coda sono solo nelle posizioni in grigio chiaro. (a) La coda ha 5 elementi, nelle posizioni $Q[7..11]$. (b) La configurazione dopo le chiamate $\text{ENQUEUE}(Q, 17)$, $\text{ENQUEUE}(Q, 3)$ ed $\text{ENQUEUE}(Q, 5)$. (c) La configurazione dopo la chiamata $\text{DEQUEUE}(Q)$, che restituisce la chiave 15, prima in testa alla coda. La nuova testa ha chiave 6.

## Esempio di esecuzione

$Q.head$ = posizione del primo elemento, $Q.tail$ = **prima cella libera** (dove andrà il prossimo elemento); dopo la posizione 12 si riparte dalla 1.

| Stato | Celle occupate | $Q.head$ | $Q.tail$ | Contenuto (dalla testa) |
|---|---|---|---|---|
| (a) | $Q[7..11]$ | 7 | 12 | ⟨15, 6, 9, 8, 4⟩ |
| (b) dopo ENQUEUE 17, 3, 5 | $Q[7..12]$, $Q[1..2]$ | 7 | 3 | ⟨15, 6, 9, 8, 4, 17, 3, 5⟩ |
| (c) dopo DEQUEUE → 15 | $Q[8..12]$, $Q[1..2]$ | 8 | 3 | ⟨6, 9, 8, 4, 17, 3, 5⟩ |

> 🧩 Derivazione mia (passaggio (a)→(b)): 17 va in $Q[12]$ e $tail$ passa da 12 a 1 (giro circolare); 3 va in $Q[1]$, $tail = 2$; 5 va in $Q[2]$, $tail = 3$. Verificato con [[strutture_elementari.py]].

## Operazioni (pseudocodice) · [[04-Strutture dati elementari.pdf#page=28|p. 28]]

> 📚 Fonte esterna: Cormen, 3ª ed., § 10.1 (libro di testo del corso), nelle [[pseudocodice|convenzioni del corso]]; le slide mostrano solo la figura. Come nel libro, i controlli di overflow/underflow sono omessi.

```
ENQUEUE(Q, x)
1  Q[Q.tail] ← x
2  if Q.tail = length[Q]
3      Q.tail ← 1
4  else Q.tail ← Q.tail + 1

DEQUEUE(Q)
1  x ← Q[Q.head]
2  if Q.head = length[Q]
3      Q.head ← 1
4  else Q.head ← Q.head + 1
5  return x
```

Numero costante di righe → $O(1)$.

> 🧩 Derivazione mia: con questa convenzione la coda è vuota quando $Q.head = Q.tail$; per distinguere «piena» da «vuota» si lascia sempre una cella libera, quindi un array di $n$ celle contiene al più $n - 1$ elementi.

## Perché pile e code · [[04-Strutture dati elementari.pdf#page=29|p. 29]]

Le file in banca sono code; la differenza tra BFS e DFS è solo se i vertici da elaborare stanno in una coda o in una pila → [[pila]].

## Connessioni · [[09-Alberi binari ricerca.pdf#page=4|p. 4]]

- [[pila]], [[lista-concatenata]], [[array]]
- [[tracce-pila-e-coda]] — esercizi
- [[coda-di-priorita]] — simile a una coda, ma l'ordine è dato dalla priorità

## Fonti · [[04-Strutture dati elementari.pdf#page=25|p. 25]], [[04-Strutture dati elementari.pdf#page=27|p. 27]]–[[04-Strutture dati elementari.pdf#page=29|29]]

- [[lezione-04-strutture-dati-elementari]]

_Aggiornato: 2026-09-26 — ingest 04-Strutture dati elementari.pdf_
_Aggiornato: 2026-10-28 — collegamenti alle lezioni 08–09_

<!-- nav:inizio -->
---
**Lezione 04 · pagina 8 di 9** · ← [[pila|Pila (stack) — LIFO]] · [[lezioni|Indice]] · [[tracce-pila-e-coda|Tracce di operazioni su pila e coda (su array)]] →
<!-- nav:fine -->
