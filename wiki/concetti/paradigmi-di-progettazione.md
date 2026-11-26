---
tipo: concetto
importanza_esame: alta
prerequisiti: ["algoritmo-e-problema"]
fonti_pdf: ["03-Analisi di algoritmi.pdf#page=3", "00-Presentazione.pdf#page=5"]
---

# Paradigmi (famiglie) di progettazione degli algoritmi

## Definizione · [[03-Analisi di algoritmi.pdf#page=2|p. 2]]–[[03-Analisi di algoritmi.pdf#page=6|6]]

I problemi possono essere affrontati in molti modi; qui si guarda **agli approcci**, non alle strutture dati. Ogni approccio bilancia tre grandezze: **tempo di calcolo**, **qualità della soluzione** e **scalabilità**. Le tre famiglie principali sono:

| Famiglia | Idea (dalla slide) |
|---|---|
| [[divide-et-impera]] | scomponi il problema, risolvi i sottoproblemi, combina i risultati |
| [[ricerca-combinatoria]] | esplora lo spazio delle soluzioni con vincoli e potature verso l'ottimo |
| [[metodi-euristici]] | trova soluzioni «abbastanza buone» rapidamente, senza garanzia d'ottimalità |

La slide p. 2 è l'intestazione della sezione «Classificazione dei problemi».

## Spiegazione · [[00-Presentazione.pdf#page=5|p. 5]]

> 🧩 Derivazione mia (lettura comparata delle slide pp. 4–6):

| | Divide et impera | Ricerca combinatoria | Metodi euristici |
|---|---|---|---|
| Garanzia di ottimo | sì (è un algoritmo esatto) | sì, se la ricerca non viene troncata | no |
| Costo tipico | spesso efficiente se la partizione è bilanciata | tipicamente esponenziale | polinomiale per iterazione |
| Quando usarlo | divisione naturale e «merge» efficiente | istanze piccole/medie, serve certificare l'ottimo | problemi difficili/grandi, tempo limitato |
| Esempi della fonte | ordinamento, ricerca | commesso viaggiatore, zaino | commesso viaggiatore, zaino |

Lo stesso problema può essere attaccato da più famiglie: il [[robot-tour-optimization]] (commesso viaggiatore) compare sia tra gli esempi di ricerca combinatoria sia tra quelli euristici. Nella lezione 01 lo si è visto concretamente: [[optimal-tsp]] (esaustivo, corretto ma lentissimo) contro [[nearest-neighbor]] e [[closest-pair]] (euristiche veloci ma sbagliate su alcune istanze).

Il programma del corso prevede due blocchi di «tecniche di progettazione»: prima divide et impera e ricerca combinatoriale/metodi euristici, poi programmazione dinamica e grafi.

## Perché importa · [[00-Presentazione.pdf#page=6|p. 6]]

Davanti a un problema non noto (obiettivo esplicito del corso) la prima scelta è **quale famiglia** usare, in base al compromesso tempo/qualità/scalabilità richiesto.

## Connessioni · [[03-Analisi di algoritmi.pdf#page=9|p. 9]]

- [[algoritmo-e-problema]] — solo divide et impera e ricerca combinatoria completa producono algoritmi *corretti* nel senso della definizione; le euristiche no
- [[iterazione-e-ricorsione]] — divide et impera si esprime naturalmente in forma ricorsiva

## Fonti · [[03-Analisi di algoritmi.pdf#page=2|p. 2]], [[03-Analisi di algoritmi.pdf#page=3|3]]

- [[lezione-03-analisi-di-algoritmi]], [[presentazione-del-corso]]

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_

<!-- nav:inizio -->
---
**Lezione 03 · pagina 2 di 13** · ← [[lezione-03-analisi-di-algoritmi|Lezione 03: introduzione e riepilogo]] · [[lezioni|Indice]] · [[divide-et-impera|Divide et impera]] →
<!-- nav:fine -->
