---
tipo: esercizio
argomento: "tracce di operazioni su pila e coda implementate con array"
difficoltà: bassa
---

# Tracce di operazioni su pila e coda (su array)

## Metodo

1. Disegnare l'array con gli indici **da 1** e segnare le celle che fanno parte della struttura.
2. **Pila:** `PUSH` incrementa `S.top` e scrive in `S[S.top]`; `POP` decrementa `S.top` e restituisce `S[S.top + 1]`. L'elemento «tolto» resta fisicamente nell'array.
3. **Coda circolare:** `ENQUEUE` scrive in `Q[Q.tail]` e avanza `tail`; `DEQUEUE` legge `Q[Q.head]` e avanza `head`; dopo l'ultima cella si torna alla 1.
4. A ogni passo scrivere: contenuto dell'array, puntatori, contenuto logico della struttura.

## Strumenti usati

- [[pila]], [[coda]]; script [[strutture_elementari.py]]

## Casi svolti

### Caso 1 — Figura 10.1 ([[04-Strutture dati elementari.pdf#page=26]])
Pila $S[1..7]$, inizialmente ⟨15, 6, 2, 9⟩, $S.top = 4$.

| Operazione | $S.top$ | Contenuto logico | Restituisce |
|-----------|---------|------------------|-------------|
| — | 4 | 15 6 2 9 | |
| PUSH(S, 17) | 5 | 15 6 2 9 17 | |
| PUSH(S, 3) | 6 | 15 6 2 9 17 3 | |
| POP(S) | 5 | 15 6 2 9 17 | 3 (resta in $S[6]$ ma è fuori dalla pila) |

### Caso 2 — Figura 10.2 ([[04-Strutture dati elementari.pdf#page=27]])
Coda $Q[1..12]$, inizialmente ⟨15, 6, 9, 8, 4⟩ in $Q[7..11]$, $head = 7$, $tail = 12$.

| Operazione | Scrive/legge | $head$ | $tail$ | Contenuto logico |
|-----------|--------------|--------|--------|------------------|
| — | | 7 | 12 | 15 6 9 8 4 |
| ENQUEUE(Q, 17) | $Q[12] = 17$ | 7 | 1 (giro) | 15 6 9 8 4 17 |
| ENQUEUE(Q, 3) | $Q[1] = 3$ | 7 | 2 | … 17 3 |
| ENQUEUE(Q, 5) | $Q[2] = 5$ | 7 | 3 | … 17 3 5 |
| DEQUEUE(Q) → 15 | legge $Q[7]$ | 8 | 3 | 6 9 8 4 17 3 5 |

Risultato coincidente con la figura: (b) $tail = 3$, $head = 7$; (c) $head = 8$, nuova testa 6.

## Trappole

- `Q.tail` indica la **prima cella libera**, non l'ultimo elemento.
- Dimenticare il ritorno circolare da 12 a 1.
- Credere che `POP` cancelli fisicamente l'elemento: cambia solo `top`.

_Aggiornato: 2026-09-26 — ingest 04-Strutture dati elementari.pdf_
