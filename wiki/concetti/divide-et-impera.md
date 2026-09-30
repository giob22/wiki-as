---
tipo: concetto
importanza_esame: alta
prerequisiti: ["paradigmi-di-progettazione", "iterazione-e-ricorsione"]
fonti_pdf: ["03-Analisi di algoritmi.pdf#page=4"]
---

# Divide et impera

## Definizione

> 📄 Fonte: [[03-Analisi di algoritmi.pdf#page=4]]

Gli algoritmi divide et impera **scompongono** il problema in sottoproblemi **simili e più piccoli**, li **risolvono** (spesso in modo ricorsivo) e **combinano** le soluzioni. Funzionano bene quando la divisione è naturale e il «merge» (la combinazione) è efficiente.

Schema: **divide → conquer → combine**, con **casi base** ben definiti.

## Spiegazione

Caratteristiche della soluzione ([[03-Analisi di algoritmi.pdf#page=4]]):
- spesso efficienti se la **partizione è bilanciata** (sottoproblemi di dimensione simile);
- buona **parallelizzabilità** dei sottoproblemi (sono indipendenti);
- **overhead** nel passo di combinazione; attenzione al **bilanciamento**.

Esempi classici citati: **ordinamento**, **ricerca**, «…».

> 🧩 Derivazione mia: la stima del costo di un algoritmo divide et impera porta naturalmente a un'[[equazioni-di-ricorrenza|equazione di ricorrenza]] (costo del problema = costo dei sottoproblemi + costo di divisione e combinazione), che è il motivo per cui la lezione 03 introduce le ricorrenze sul caso semplice di [[somma-ricorsiva]]. Esempi specifici di algoritmi divide et impera non sono ancora stati presentati nelle fonti ingerite (TODO: da espandere quando arriverà la lezione dedicata, [[00-Presentazione.pdf#page=5]]).

Il merge sort, citato in [[01-Introduzione.pdf#page=11]] come algoritmo di costo $n\log n$, è l'esempio che la fonte usa per l'ordinamento efficiente.

## Perché importa

È la prima tecnica di progettazione del programma ([[00-Presentazione.pdf#page=5]]).

## Connessioni

- [[paradigmi-di-progettazione]] — confronto con ricerca combinatoria ed euristiche
- [[iterazione-e-ricorsione]] — la forma ricorsiva rende il codice «spesso più chiaro per divide-et-impera» ([[03-Analisi di algoritmi.pdf#page=9]])
- [[correttezza-per-induzione]] — la correttezza di un algoritmo ricorsivo si prova per induzione
- [[equazioni-di-ricorrenza]] — strumento di analisi del costo

## Fonti

- [[lezione-03-analisi-di-algoritmi]]
- [[03-Analisi di algoritmi.pdf#page=4]]

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_
