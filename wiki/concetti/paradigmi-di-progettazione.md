---
tipo: concetto
importanza_esame: alta
prerequisiti: ["algoritmo-e-problema"]
fonti_pdf: ["03-Analisi di algoritmi.pdf#page=3", "00-Presentazione.pdf#page=5"]
---

# Paradigmi (famiglie) di progettazione degli algoritmi

## Definizione

> 📄 Fonte: [[03-Analisi di algoritmi.pdf#page=3]]

I problemi possono essere affrontati in molti modi; qui si guarda **agli approcci**, non alle strutture dati. Ogni approccio bilancia tre grandezze: **tempo di calcolo**, **qualità della soluzione** e **scalabilità**. Le tre famiglie principali sono:

| Famiglia | Idea (dalla slide) | Pagina |
|----------|--------------------|--------|
| [[divide-et-impera]] | scomponi il problema, risolvi i sottoproblemi, combina i risultati | [[03-Analisi di algoritmi.pdf#page=4]] |
| [[ricerca-combinatoria]] | esplora lo spazio delle soluzioni con vincoli e potature verso l'ottimo | [[03-Analisi di algoritmi.pdf#page=5]] |
| [[metodi-euristici]] | trova soluzioni «abbastanza buone» rapidamente, senza garanzia d'ottimalità | [[03-Analisi di algoritmi.pdf#page=6]] |

La slide p. 2 è l'intestazione della sezione «Classificazione dei problemi» ([[03-Analisi di algoritmi.pdf#page=2]]).

## Spiegazione

> 🧩 Derivazione mia (lettura comparata delle slide pp. 4–6):

| | Divide et impera | Ricerca combinatoria | Metodi euristici |
|--|--|--|--|
| Garanzia di ottimo | sì (è un algoritmo esatto) | sì, se la ricerca non viene troncata | no |
| Costo tipico | spesso efficiente se la partizione è bilanciata | tipicamente esponenziale | polinomiale per iterazione |
| Quando usarlo | divisione naturale e «merge» efficiente | istanze piccole/medie, serve certificare l'ottimo | problemi difficili/grandi, tempo limitato |
| Esempi della fonte | ordinamento, ricerca | commesso viaggiatore, zaino | commesso viaggiatore, zaino |

Lo stesso problema può essere attaccato da più famiglie: il [[robot-tour-optimization]] (commesso viaggiatore) compare sia tra gli esempi di ricerca combinatoria sia tra quelli euristici. Nella lezione 01 lo si è visto concretamente: [[optimal-tsp]] (esaustivo, corretto ma lentissimo) contro [[nearest-neighbor]] e [[closest-pair]] (euristiche veloci ma sbagliate su alcune istanze).

Il programma del corso ([[00-Presentazione.pdf#page=5]]) prevede due blocchi di «tecniche di progettazione»: prima divide et impera e ricerca combinatoriale/metodi euristici, poi programmazione dinamica e grafi.

## Perché importa

Davanti a un problema non noto (obiettivo esplicito del corso, [[00-Presentazione.pdf#page=6]]) la prima scelta è **quale famiglia** usare, in base al compromesso tempo/qualità/scalabilità richiesto.

## Connessioni

- [[algoritmo-e-problema]] — solo divide et impera e ricerca combinatoria completa producono algoritmi *corretti* nel senso della definizione; le euristiche no
- [[iterazione-e-ricorsione]] — divide et impera si esprime naturalmente in forma ricorsiva ([[03-Analisi di algoritmi.pdf#page=9]])

## Fonti

- [[lezione-03-analisi-di-algoritmi]], [[presentazione-del-corso]]
- [[03-Analisi di algoritmi.pdf#page=2]], [[03-Analisi di algoritmi.pdf#page=3]]

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_
