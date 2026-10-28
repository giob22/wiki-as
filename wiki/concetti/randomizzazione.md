---
tipo: concetto
importanza_esame: media
prerequisiti: ["casi-di-complessita", "quicksort"]
fonti_pdf: ["07-Quicksort 1.pdf#page=19", "07-Quicksort 1.pdf#page=20", "07-Quicksort 1.pdf#page=23"]
---

# Randomizzazione

## Definizione

> 📄 Fonte: [[07-Quicksort 1.pdf#page=19]]

La slide cita (in inglese) che la randomizzazione è «a powerful tool to improve algorithms» con **caso peggiore cattivo** ma **caso medio buono**. Tre usi elencati:
- *random sampling* (campionamento casuale);
- *randomized hashing* (hashing randomizzato);
- *random search* (ricerca casuale).

> 🧩 Definizione operativa mia: un algoritmo **randomizzato** prende alcune decisioni in base a valori estratti a caso durante l'esecuzione (in [[quicksort-randomizzato]], `Random(p,r)`). A parità di input, esecuzioni diverse possono seguire percorsi e avere costi diversi.

## Formule

> 📄 Fonte: [[07-Quicksort 1.pdf#page=23]]

Per un algoritmo randomizzato interessa il **tempo di esecuzione atteso**: per quicksort randomizzato si dimostra che è $O(n\log n)$ (dimostrazione sul libro di testo).

> 🧩 Precisazione mia sui simboli: per un input fissato $I$ di dimensione $n$, il tempo $T(I)$ è una **variabile aleatoria**, perché dipende dalle scelte casuali. Il tempo atteso è il suo valore medio $\mathbb{E}[T(I)]$, e il risultato vale **per ogni** $I$:
$$ \max_{|I| = n} \mathbb{E}[T(I)] = O(n \log n) $$
> Nel «caso medio» di [[casi-di-complessita]], invece, la media è fatta sugli **input**, secondo una distribuzione da ipotizzare.

## Spiegazione

> 📄 Fonte: [[07-Quicksort 1.pdf#page=20]]

L'esempio della lezione è **quicksort**: scegliere il pivot in maniera aleatoria aumenta la probabilità che in media il partizionamento sia ben bilanciato, e la versione randomizzata è ritenuta la scelta migliore per ordinare array di grosse dimensioni.

> 🧩 Spiegazione mia — perché funziona proprio per algoritmi con «caso peggiore cattivo, caso medio buono»:
> - il [[quicksort]] deterministico ha caso medio $\Theta(n\lg n)$ ma caso peggiore $\Theta(n^2)$, e il caso peggiore è un input **comune**: l'array già ordinato ([[07-Quicksort 1.pdf#page=14]]);
> - con il pivot casuale il costo non dipende più dall'ordine dell'input ma dalle estrazioni: l'array ordinato si comporta come un input qualsiasi;
> - il caso peggiore $\Theta(n^2)$ resta possibile, ma richiede estrazioni sfortunate a quasi ogni livello, ed è molto improbabile.
>
> Misura ([[divide_et_impera.py]], input ordinato, $n = 10\,000$): 156 787 confronti medi con il pivot casuale, contro 49 995 000 con il pivot fisso $A[r]$.

## Perché importa

> 🎯 Esame: distinguere tempo **atteso** (media sulle scelte dell'algoritmo, input qualsiasi) da tempo **medio** (media sugli input); spiegare perché Randomized-Quicksort elimina gli input sistematicamente cattivi.

## Connessioni

- [[quicksort-randomizzato]] — l'applicazione vista a lezione
- [[nuts-and-bolts]] — stesso uso del pivot casuale, su dadi e bulloni
- [[casi-di-complessita]] — tempo atteso contro caso medio e caso peggiore
- [[metodi-euristici]] — 🧩 entrambi rinunciano a qualcosa: l'euristica alla garanzia di ottimalità, l'algoritmo randomizzato alla garanzia sul tempo nel caso peggiore (ma il risultato resta sempre corretto)

## Fonti

- [[lezione-07-quicksort]]
- [[07-Quicksort 1.pdf#page=19]], [[07-Quicksort 1.pdf#page=20]], [[07-Quicksort 1.pdf#page=23]]

_Aggiornato: 2026-10-01 — ingest 07-Quicksort.pdf_
_Aggiornato: 2026-10-14 — link ripuntati alla versione aggiornata delle slide 07-Quicksort 1.pdf_

<!-- nav:inizio -->
---
**Lezione 07 · pagina 4 di 7** · ← [[partition|Partition]] · [[lezioni|Indice]] · [[quicksort-randomizzato|Quicksort randomizzato]] →
<!-- nav:fine -->
