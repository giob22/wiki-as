---
tipo: concetto
importanza_esame: media
prerequisiti: ["algoritmo-e-problema"]
fonti_pdf: ["03-Analisi di algoritmi.pdf#page=8", "03-Analisi di algoritmi.pdf#page=9", "03-Analisi di algoritmi.pdf#page=11"]
---

# Iterazione e ricorsione

## Definizione · [[03-Analisi di algoritmi.pdf#page=7|p. 7]]–[[03-Analisi di algoritmi.pdf#page=9|9]]

Due stili con lo **stesso potere espressivo**: la scelta dipende da chiarezza, costi e vincoli.

|  | Approccio iterativo | Approccio ricorsivo |
|---|---|---|
| Meccanismo | usa cicli (`for`, `while`) e **stato esplicito** passo dopo passo | definisce il problema per **auto-somiglianza**: casi base + chiamate a sottoproblemi |
| Costi | in genere più **prevedibile** su tempo e memoria; poco overhead | **overhead di chiamata** e rischio di **stack overflow** senza tail-call/limiti |
| Quando | ottimo quando l'aggiornamento è lineare e la condizione di arresto è semplice | codice spesso più chiaro per **divide-et-impera** e **backtracking** |
| Altro | facile da ottimizzare e testare; adatto ad ambienti con limiti di stack | elegante, ma va progettata la **combinazione dei risultati** |

La sezione è introdotta dall'intestazione «Caratterizzazione degli algoritmi».

## Spiegazione · [[03-Analisi di algoritmi.pdf#page=10|p. 10]], [[03-Analisi di algoritmi.pdf#page=11|11]], [[03-Analisi di algoritmi.pdf#page=28|p. 28]], [[03-Analisi di algoritmi.pdf#page=33|p. 33]]

Esempio della fonte: somma dei primi $n$ numeri $1 + 2 + \dots + n$.

![[03-analisi-algoritmi-p11-somma-iterativa-ricorsiva.png]]
*Le due versioni affiancate.*

| | [[somma-iterativa]] | [[somma-ricorsiva]] |
|---|---|---|
| Correttezza si prova con | [[invariante-di-ciclo]] | [[correttezza-per-induzione]] |
| Tempo | $2n + 4 = O(n)$ | $1 + cn = O(n)$ |
| Spazio (🧩 mio) | $\Theta(1)$ | $\Theta(n)$ — $n+1$ record di attivazione sulla pila |

> 🧩 Derivazione mia: la colonna «spazio» spiega concretamente il «rischio di stack overflow»: per $n$ molto grande la versione ricorsiva esaurisce la pila di sistema, quella iterativa no (dettagli in [[tempo-di-esecuzione]] § complessità spaziale).

## Perché importa

La forma dell'algoritmo determina **come** se ne dimostra la correttezza (invariante vs induzione) e **come** se ne calcola il costo (somma riga per riga vs [[equazioni-di-ricorrenza]]).

## Connessioni

- [[divide-et-impera]] — naturalmente ricorsivo
- [[invariante-di-ciclo]], [[correttezza-per-induzione]] — le due tecniche di prova
- [[tempo-di-esecuzione]], [[equazioni-di-ricorrenza]] — le due tecniche di analisi

## Fonti · [[03-Analisi di algoritmi.pdf#page=7|p. 7]], [[03-Analisi di algoritmi.pdf#page=11|p. 11]]

- [[lezione-03-analisi-di-algoritmi]]

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_

<!-- nav:inizio -->
---
**Lezione 03 · pagina 4 di 13** · ← [[divide-et-impera|Divide et impera]] · [[lezioni|Indice]] · [[somma-iterativa|somma_iterativa — somma dei primi n interi (versione iterativa)]] →
<!-- nav:fine -->
