---
tipo: concetto
importanza_esame: alta
prerequisiti: []
fonti_pdf: ["a1-indicazioni_psuedocodice.pdf#page=2", "a1-indicazioni_psuedocodice.pdf#page=3", "a1-indicazioni_psuedocodice.pdf#page=4"]
---

# Convenzioni per lo pseudocodice

## Definizione · [[a1-indicazioni_psuedocodice.pdf#page=2|p. 2]]–[[a1-indicazioni_psuedocodice.pdf#page=4|4]]

Regole di scrittura dello pseudocodice fissate dal docente per le lezioni e **per gli esercizi d'esame** (sono le convenzioni del Cormen, libro di testo del corso).

- L'**indentazione** indica la struttura dei blocchi (niente parentesi).
- I costrutti iterativi e di condizione hanno significato analogo ai linguaggi di alto livello. Costrutti di controllo disponibili: **while, for, if-else**.
- La notazione $i \leftarrow j$ indica che il valore di $j$ viene **assegnato** a $i$.
- L'operatore `[]` indica sia l'accesso ai singoli elementi di un array sia l'accesso ai campi di un oggetto (es. `length[A]`).
- Si assume che gli **indici inizino da 1**.
- Sono disponibili i **sotto-array** (*slices*) come in Fortran, Matlab, Python: $A[i..j]$ è la porzione di array che inizia dall'$i$-esimo elemento e termina al $j$-esimo.

- Sono presenti **aggregati eterogenei** (= strutture C):
  - l'accesso a un campo si fa sia con l'operatore `.` (`A.campo1`) sia con `[]` (`campo1[A]`);
  - diversamente dal C, una variabile di tipo aggregato è un **puntatore alla struttura**; un puntatore non riferito ad alcuna struttura ha valore **NIL**;
  - attenzione: `y ← x` seguito da `x.f ← 3` modifica **anche** `y`.
- I parametri **non aggregati** sono passati **per valore** alle procedure.
- I parametri **aggregati** (strutture) sono passati **per riferimento** (come in Java).
- Tutte le variabili sono **locali** alla procedura descritta.

- Operatori di confronto: $<$, $\le$, $=$, $\ge$, $>$, $\ne$.
- Gli operatori booleani **and** e **or** sono valutati con la tecnica del **corto circuito** (come nella maggior parte dei linguaggi).
- **Commenti** mono-riga con $\triangleright$; i blocchi sono dati dall'indentazione.
- Non è necessario esplicitare il **tipo** delle variabili: può essere inferito dall'uso.
- **Funzioni di libreria:** sarà esplicitato nell'esercizio in quali casi è consentito usare «funzioni di libreria» assunte presenti (ad esempio «sort»).

## Spiegazione · 02-Notazione asintotica.pdf [[02-Notazione asintotica.pdf#page=7|p. 7]], [[02-Notazione asintotica.pdf#page=11|p. 11]] · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=11|p. 11]] · 04-Strutture dati elementari.pdf [[04-Strutture dati elementari.pdf#page=17|p. 17]] · Pseudocodice [[a1-indicazioni_psuedocodice.pdf#page=1|p. 1]]

> 🧩 Esempio mio che usa tutte le regole principali:

```
CERCA-MASSIMO(A)               ▷ A[1..n], indici da 1
1  max ← A[1]
2  for i ← 2 to length[A]
3      if A[i] > max
4          max ← A[i]
5  return max
```

Due trappole frequenti:
1. **Aliasing:** dopo `y ← x` le due variabili puntano alla **stessa** struttura (è un puntatore, non una copia): modificare un campo tramite `x` si vede tramite `y`.
2. **Corto circuito:** in `while x ≠ NIL and x.key ≠ k` il secondo test non viene valutato quando `x = NIL`, quindi non si accede a un campo di `NIL` (usato in [[lista-concatenata]]).

> ⚠️ Contraddizione (lieve): le slide delle lezioni non sempre seguono queste convenzioni — la lezione 02 usa `ALGORITMO … SE … ALTRIMENTI … PER i = 0.. n FAI` con commenti `//`, la lezione 03 `funzione … per i da 1 a n … ritorna`, la lezione 04 codice C. Nel wiki lo pseudocodice delle slide è riportato fedelmente; quando utile si aggiunge una traduzione 🧩 nelle convenzioni di questa pagina.

Nota: le slide delle convenzioni riportano «a.a. 25/26».

## Perché importa

> 🎯 Esame: gli esercizi di progettazione chiedono pseudocodice in **questa** notazione; `sort` e simili solo se l'esercizio lo permette.

## Connessioni

- [[modello-ram]] — ogni riga di pseudocodice ha costo costante, salvo chiamate a sottoprocedure come `sort`
- [[tempo-di-esecuzione]] — la numerazione delle righe serve per la tabella dei costi
- [[array]], [[lista-concatenata]] — indici da 1, puntatori e NIL

## Fonti · [[a1-indicazioni_psuedocodice.pdf#page=1|p. 1]], [[a1-indicazioni_psuedocodice.pdf#page=4|p. 4]]

- [[convenzioni-per-lo-pseudocodice]]

_Aggiornato: 2026-09-26 — ingest a1-indicazioni_psuedocodice.pdf_

<!-- nav:inizio -->
---
**Materiale di supporto · pagina 2 di 2** · ← [[convenzioni-per-lo-pseudocodice|Materiale di supporto: introduzione e riepilogo]] · [[lezioni|Indice]] · [[lezione-01-introduzione|Lezione 01: introduzione e riepilogo]] →
<!-- nav:fine -->
