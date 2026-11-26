---
tipo: entità
categoria: struttura-dati
fonti_pdf: ["04-Strutture dati elementari.pdf#page=8", "04-Strutture dati elementari.pdf#page=9"]
---

# Array

## Cos'è · [[04-Strutture dati elementari.pdf#page=8|p. 8]]

Un **array** è una struttura di record di dati di **dimensione fissa** tali che ogni elemento può essere localizzato efficientemente tramite il suo **indice** o, equivalentemente, il suo **indirizzo**. È la struttura contigua per eccellenza ([[strutture-contigue-e-collegate]]).

## Rappresentazione in memoria · [[04-Strutture dati elementari.pdf#page=9|p. 9]]

![[04-strutture-dati-p9-array.png]]
*Array $S[1..7]$ con $S = \langle 15, 6, 2, 9 \rangle$ nelle prime 4 celle e 3 celle libere (grigie).*

> 🧩 Derivazione mia (perché l'accesso è costante): se l'array inizia all'indirizzo $b$ e ogni record occupa $w$ byte, con indici da 1 l'elemento $i$ sta all'indirizzo $b + (i-1)\,w$: un'operazione aritmetica e un accesso, cioè $\Theta(1)$ nel [[modello-ram]].

## Operazioni e costi · [[04-Strutture dati elementari.pdf#page=8|p. 8]], [[04-Strutture dati elementari.pdf#page=10|p. 10]]

| Operazione | Costo | Fonte |
|---|---|---|
| accesso a $A[i]$ dato l'indice | tempo costante | p. 8 |
| crescita oltre la dimensione iniziale | impossibile per un array semplice | p. 10 → [[array-dinamico]] |

## Vantaggi · [[04-Strutture dati elementari.pdf#page=8|p. 8]]

- accesso in **tempo costante** dato l'indice;
- gli array consistono **solo di dati**: nessuno spazio sprecato per collegamenti o informazioni di formato;
- la **continuità fisica** (località della memoria) tra accessi successivi aiuta a sfruttare la **cache** ad alta velocità delle architetture moderne.

## Svantaggi · [[04-Strutture dati elementari.pdf#page=10|p. 10]]

«Unfortunately we cannot adjust the size of simple arrays in the middle of a program's execution» e allocare array enormi per compensare spreca molto spazio.

## Nel corso · Pseudocodice [[a1-indicazioni_psuedocodice.pdf#page=2|p. 2]] · 04-Strutture dati elementari.pdf [[04-Strutture dati elementari.pdf#page=26|p. 26]], [[04-Strutture dati elementari.pdf#page=27|27]]

- Convenzioni dello pseudocodice: indici **da 1**, sotto-array $A[i..j]$, `length[A]` → [[pseudocodice]].
- Base delle implementazioni di [[pila]] e [[coda]].

## Connessioni

- [[array-dinamico]], [[lista-concatenata]], [[strutture-contigue-e-collegate]]

## Fonti · [[04-Strutture dati elementari.pdf#page=7|p. 7]]–[[04-Strutture dati elementari.pdf#page=9|9]]

- [[lezione-04-strutture-dati-elementari]]

_Aggiornato: 2026-09-26 — ingest 04-Strutture dati elementari.pdf_

<!-- nav:inizio -->
---
**Lezione 04 · pagina 4 di 9** · ← [[strutture-contigue-e-collegate|Strutture dati contigue e collegate (e puntatori)]] · [[lezioni|Indice]] · [[array-dinamico|Array dinamico (raddoppio della capacità)]] →
<!-- nav:fine -->
