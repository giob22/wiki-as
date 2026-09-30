---
tipo: entità
categoria: problema
fonti_pdf: ["01-Introduzione.pdf#page=36", "01-Introduzione.pdf#page=37", "01-Introduzione.pdf#page=60"]
---

# Movie Scheduling Problem (selezione di intervalli)

## Definizione formale

> 📄 Fonte: [[01-Introduzione.pdf#page=37]]

- **Problem:** Movie Scheduling Problem
- **Input:** un insieme $S$ di $n$ intervalli sulla retta
- **Output:** qual è il **più grande sottoinsieme** di intervalli **mutuamente non sovrapposti** che si può scegliere da $S$?

Introdotto come «S&T: Problema 2 — Movie scheduling» ([[01-Introduzione.pdf#page=36]]). Interpretazione: ogni intervallo è il periodo di riprese di un film; un attore può lavorare a un solo film alla volta e vuole girarne il maggior numero possibile. La slide invita: «Proponete soluzioni …».

> 🧩 Derivazione mia (formalizzazione): intervallo $I_j = [s_j, f_j)$ con inizio $s_j$ e fine $f_j$; $I_j$ e $I_k$ si sovrappongono se $s_j < f_k$ e $s_k < f_j$. Si cerca $A \subseteq S$ di cardinalità massima senza coppie sovrapposte.

## Istanza della lezione

![[01-introduzione-p37-movie-scheduling-istanza.png]]
*Nove intervalli (titoli di «film» a tema informatico): Tarjan of the Jungle, The Four Volume Problem, The President's Algorist, Steiner's Tree, Process Terminated, Halting State, Programming Challenges, "Discrete" Mathematics, Calculated Bets. ([[01-Introduzione.pdf#page=37]])*

## Algoritmi che lo risolvono

| Soluzione | Algoritmo | Corretto? | Costo | Pagina |
|-----------|-----------|-----------|-------|--------|
| 1 | [[earliest-job-first]] | no | polinomiale | [[01-Introduzione.pdf#page=38]] |
| 2 | [[shortest-job-first]] | no | polinomiale | [[01-Introduzione.pdf#page=47]] |
| 3 | [[exhaustive-scheduling]] | sì | $2^n$ sottoinsiemi — proibitivo | [[01-Introduzione.pdf#page=56]], [[01-Introduzione.pdf#page=58]] |
| 4 | [[optimal-scheduling]] | **sì** | **efficiente** | [[01-Introduzione.pdf#page=60]] |

«Soluzione 4 … esiste stavolta una sol corretta ed efficiente!» ([[01-Introduzione.pdf#page=60]]). A differenza del [[robot-tour-optimization]], qui una semplice regola greedy — **scegli il job che termina prima** — è corretta.

> 🎯 Esame: *Take-Home Lesson #2* — «Reasonable-looking algorithms can easily be incorrect. Algorithm correctness is a property that must be carefully demonstrated.» ([[01-Introduzione.pdf#page=60]]) → [[ricerca-di-controesempi]].

## Connessioni

- [[metodi-euristici]], [[ricerca-combinatoria]]
- [[controesempi-per-euristiche]] — controesempi minimi e verifica di [[optimal-scheduling]]

## Fonti

- [[lezione-01-introduzione]]
- [[01-Introduzione.pdf#page=36]]–[[01-Introduzione.pdf#page=60]]

_Aggiornato: 2026-09-26 — ingest 01-Introduzione.pdf_
