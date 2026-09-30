---
tipo: concetto
importanza_esame: alta
prerequisiti: ["algoritmo-e-problema", "paradigmi-di-progettazione"]
fonti_pdf: ["03-Analisi di algoritmi.pdf#page=6", "01-Introduzione.pdf#page=35"]
---

# Metodi euristici (e differenza tra algoritmi ed euristiche)

## Definizione

> 📄 Fonte: [[03-Analisi di algoritmi.pdf#page=6]]

I metodi euristici sono **regole pratiche** o strategie di ricerca che trovano soluzioni **«abbastanza buone»** in **tempi ragionevoli**, **senza garanzie di ottimalità**. Sono utili per problemi difficili o di grande scala, o quando il tempo è limitato.

Esempi classici: **commesso viaggiatore**, **zaino**, «…». Caratteristiche della soluzione:
- tempi in genere **polinomiali per iterazione**;
- **nessuna garanzia** di ottimalità o completezza;
- **valutazione empirica**.

> 📄 Fonte: [[01-Introduzione.pdf#page=35]] — *Take-Home Lesson #1*

> There is a fundamental difference between **algorithms**, which always produce a correct result, and **heuristics**, which may usually do a good job but without providing any guarantee.

## Spiegazione

Un'euristica può dare il risultato giusto **molto spesso** e sembrare corretta; ma per il [[algoritmo-e-problema|concetto di correttezza]] serve che funzioni su **ogni** istanza. Le euristiche viste nella lezione 01 e la loro sorte:

| Euristica | Problema | Idea | Esito | Pagina |
|-----------|----------|------|-------|--------|
| [[nearest-neighbor]] | [[robot-tour-optimization]] | vai sempre al punto non visitato più vicino | «semplice ed efficiente ma … completamente sbagliata!» | [[01-Introduzione.pdf#page=24]] |
| [[closest-pair]] | [[robot-tour-optimization]] | unisci sempre la coppia di estremi più vicina | «più complessa, ma "sembra" risolvere il problema» — poi controesempio | [[01-Introduzione.pdf#page=27]], [[01-Introduzione.pdf#page=28]] |
| [[earliest-job-first]] | [[movie-scheduling]] | accetta il job che inizia prima | un job lungo iniziale blocca molti altri | [[01-Introduzione.pdf#page=46]] |
| [[shortest-job-first]] | [[movie-scheduling]] | accetta il job più corto | il job più corto può bloccarne due | [[01-Introduzione.pdf#page=55]] |

Per il [[movie-scheduling]] esiste invece una regola corretta **ed** efficiente: [[optimal-scheduling]] (accetta il job che **termina** prima) ([[01-Introduzione.pdf#page=60]]). Per il [[robot-tour-optimization]] (commesso viaggiatore) la slide rimanda la soluzione: «Soluzione? Ne discuteremo ….» ([[01-Introduzione.pdf#page=35]]).

> 💡 Connessione: tutte e quattro le euristiche sono **golose** (greedy): fanno la scelta localmente migliore e non la rivedono più. La [[ricerca-di-controesempi]] suggerisce proprio di attaccare le greedy con istanze a parità o estreme ([[03-Analisi di algoritmi.pdf#page=14]]).

## Perché importa

> 🎯 Esame: distinguere **algoritmo** (garanzia su ogni istanza) da **euristica** (buona in pratica, nessuna garanzia) e saper mostrare con un controesempio che una regola greedy «ragionevole» è sbagliata.

## Connessioni

- [[ricerca-combinatoria]] — l'alternativa esatta ma esponenziale
- [[ricerca-di-controesempi]] — lo strumento per smascherare un'euristica
- [[controesempi-per-euristiche]] — esercizi svolti e verificati

## Fonti

- [[lezione-03-analisi-di-algoritmi]], [[lezione-01-introduzione]]
- [[03-Analisi di algoritmi.pdf#page=6]], [[01-Introduzione.pdf#page=35]], [[01-Introduzione.pdf#page=60]]

_Aggiornato: 2026-09-26 — ingest 01-Introduzione.pdf e 03-Analisi di algoritmi.pdf_
