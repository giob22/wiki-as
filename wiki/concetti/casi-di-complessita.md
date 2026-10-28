---
tipo: concetto
importanza_esame: alta
prerequisiti: ["tempo-di-esecuzione"]
fonti_pdf: ["02-Notazione asintotica.pdf#page=7", "02-Notazione asintotica.pdf#page=9", "02-Notazione asintotica.pdf#page=10", "02-Notazione asintotica.pdf#page=11", "02-Notazione asintotica.pdf#page=12"]
---

# Caso peggiore, migliore e medio

## Definizione

> 📄 Fonte: [[02-Notazione asintotica.pdf#page=9]], [[02-Notazione asintotica.pdf#page=10]]

- La **complessità nel caso peggiore** (*worst case*) di un algoritmo è la funzione definita dal **massimo** numero di passi eseguiti su una qualunque istanza di dimensione $n$.
- La **complessità nel caso migliore** (*best case*) è la funzione definita dal **minimo** numero di passi eseguiti su una qualunque istanza di dimensione $n$.
- La **complessità nel caso medio** (*average case*) è la funzione definita da un numero **medio** di passi eseguiti sulle istanze di dimensione $n$.

«Each of these complexities defines a numerical function: time vs. size!» ([[02-Notazione asintotica.pdf#page=10]])

## Formule

> 🧩 Derivazione mia (scrittura formale delle definizioni a parole): indicando con $I_n$ l'insieme delle istanze di dimensione $n$ e con $\text{passi}(x)$ i passi eseguiti sull'istanza $x$,
$$
T_{worst}(n) = \max_{x \in I_n} \text{passi}(x), \qquad
T_{best}(n) = \min_{x \in I_n} \text{passi}(x), \qquad
T_{avg}(n) = \sum_{x \in I_n} \Pr[x]\, \text{passi}(x)
$$
Il caso medio richiede quindi un'**ipotesi sulla distribuzione** $\Pr[x]$ delle istanze. Per costruzione $T_{best}(n) \le T_{avg}(n) \le T_{worst}(n)$ per ogni $n$.

![[02-notazione-asintotica-p9-casi-peggiore-medio-migliore.png]]
*Per ogni dimensione $n$ i punti in verticale sono le istanze; la curva alta (worst) ne unisce i massimi, la bassa (best) i minimi, quella intermedia (average) le medie. ([[02-Notazione asintotica.pdf#page=9]])*

## Spiegazione

Esempi della fonte (pseudocodice in stile italiano della slide):

> 📄 Fonte: [[02-Notazione asintotica.pdf#page=7]]

```
ALGORITMO Base()
   SE CONDIZIONE_VERA ALLORA          // caso fortunato
       ISTR_A_1                       // 1
       ISTR_A_2                       // 2
       RESTITUISCI
   ALTRIMENTI                         // caso sfortunato
       ISTR_B_1                       // 1
       ...                            // ...
       ISTR_B_10                      // 10
       RESTITUISCI
FINE
```

> 🧩 Derivazione mia: il caso migliore esegue il ramo fortunato (test + 2 istruzioni + return = 4 passi), il peggiore il ramo sfortunato (test + 10 istruzioni + return = 12 passi). Entrambi sono **costanti** ($\Theta(1)$): i casi cambiano il numero di passi ma non l'ordine di crescita.

> 📄 Fonte: [[02-Notazione asintotica.pdf#page=11]]

```
ALGORITMO Base2(n)
   SE CONDIZIONE_VERA ALLORA          // best case
       ISTR_A_1
       ISTR_A_2
       RESTITUISCI
   ALTRIMENTI                         // worst case
       PER i = 0 .. n FAI
           ISTR_B
       FINEPER
       RESTITUISCI
FINE
```

> 🧩 Derivazione mia: caso migliore $T_{best}(n) = 4 = \Theta(1)$; caso peggiore: il ciclo `PER i = 0 .. n` esegue il corpo per $i = 0, 1, \dots, n$, cioè $n+1$ volte, e il test $n+2$ volte, quindi $T_{worst}(n) = 1 + 1 + (n+2) + (n+1) + 1 = 2n + 6 = \Theta(n)$ (stesso conteggio di [[analisi-del-costo-riga-per-riga]]). Qui i due casi hanno **ordini di crescita diversi**. Nota: il ciclo parte da 0, mentre le [[pseudocodice|convenzioni del corso]] fanno partire da 1 gli *indici degli array* (qui $i$ è solo un contatore).

### La posizione del corso

> 📄 Fonte: [[02-Notazione asintotica.pdf#page=12]]

- Domanda: quale sarebbe il ragionamento sull'acquisto di un **biglietto della lotteria** in base ai casi migliore, peggiore e medio?
- In generale si userà la **complessità nel caso peggiore** come misura preferita dell'efficienza.
- L'analisi del caso peggiore è in genere facile da fare e «di solito» riflette il caso medio.
- **«Assume I am asking for worst-case analysis unless otherwise specified!»**
- Gli **algoritmi randomizzati** sono di importanza crescente e richiedono un'analisi di tipo caso medio per mostrare i loro meriti.

> 🧩 Derivazione mia (risposta alla domanda della lotteria): nel caso **migliore** si vince sempre → comprare; nel **peggiore** si perde sempre → non comprare; nel **medio** il guadagno atteso di una lotteria è negativo (il banco trattiene una parte) → non comprare. Il caso migliore è il più ingannevole: descrive un evento raro.

## Perché importa

> 🎯 Esame: salvo indicazione contraria, «analizza l'algoritmo» significa **caso peggiore**. Saper indicare *quale* istanza realizza il caso migliore e il peggiore (es. per la ricerca in una [[lista-concatenata]]: elemento in testa vs. ultimo o assente, [[04-Strutture dati elementari.pdf#page=18]]).

## Connessioni

- [[insertion-sort]] — esempio completo: caso migliore $\Theta(n)$ con l'array già ordinato, caso peggiore $\Theta(n^2)$ con l'array decrescente ([[05-Insertion sort.pdf#page=20]], [[05-Insertion sort.pdf#page=22]]); [[selection-sort]] invece ha caso migliore = caso peggiore

- [[quicksort]] — tre casi con ordini diversi: migliore e medio $\Theta(n\lg n)$, peggiore $\Theta(n^2)$ sul vettore ordinato ([[07-Quicksort 1.pdf#page=14]]–[[07-Quicksort 1.pdf#page=18]]); [[merge-sort]] invece è $\Theta(n\lg n)$ in ogni caso
- [[randomizzazione]], [[quicksort-randomizzato]] — gli «algoritmi randomizzati» di p. 12: per loro si studia il tempo **atteso** (media sulle scelte casuali, input qualsiasi), che non richiede ipotesi sulla distribuzione degli input ([[07-Quicksort 1.pdf#page=23]])
- [[notazione-asintotica]] — ciascun caso è una funzione di $n$ che si descrive con $O$, $\Omega$, $\Theta$
- [[lista-concatenata]] — best/worst case di ricerca e cancellazione
- [[tempo-di-esecuzione]]

## Fonti

- [[lezione-02-notazione-asintotica]]
- [[02-Notazione asintotica.pdf#page=4]] (intestazione «Algorithmic Time Complexity»), [[02-Notazione asintotica.pdf#page=7]], [[02-Notazione asintotica.pdf#page=9]], [[02-Notazione asintotica.pdf#page=10]], [[02-Notazione asintotica.pdf#page=11]], [[02-Notazione asintotica.pdf#page=12]]

_Aggiornato: 2026-09-26 — ingest 02-Notazione asintotica.pdf_

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_
_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf e 07-Quicksort.pdf_
_Aggiornato: 2026-10-14 — link ripuntati alla versione aggiornata delle slide 07-Quicksort 1.pdf_

<!-- nav:inizio -->
---
**Lezione 02 · pagina 4 di 8** · ← [[tempo-di-esecuzione|Analisi di un algoritmo: tempo di esecuzione (e spazio)]] · [[lezioni|Indice]] · [[notazione-asintotica|Notazione asintotica: O, Ω, Θ]] →
<!-- nav:fine -->
