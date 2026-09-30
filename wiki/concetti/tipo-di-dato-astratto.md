---
tipo: concetto
importanza_esame: media
prerequisiti: ["algoritmo-e-problema"]
fonti_pdf: ["04-Strutture dati elementari.pdf#page=3", "04-Strutture dati elementari.pdf#page=4"]
---

# Astrazione dei dati (operazioni astratte vs implementazione)

## Definizione

> 📄 Fonte: [[04-Strutture dati elementari.pdf#page=3]]

«Mankind's progress is measured by the number of things we can do without thinking.» Le **strutture dati elementari** — pile, code, liste, heap — sono i componenti «pronti all'uso» (*off-the-shelf*) con cui si costruiscono gli algoritmi.

Ogni struttura dati ha **due aspetti**:
1. le **operazioni astratte** che supporta;
2. l'**implementazione** di queste operazioni.

> 📄 Fonte: [[04-Strutture dati elementari.pdf#page=4]] — *Data Abstraction*

Poter descrivere il comportamento delle strutture dati in termini di operazioni astratte è il motivo per cui possiamo usarle «senza pensare». Esempio (pila):
- $Push(x, s)$ — inserisce l'elemento $x$ in cima alla pila $s$;
- $Pop(s)$ — restituisce (e rimuove) l'elemento in cima alla pila $s$.

Il fatto che esistano **implementazioni diverse** delle stesse operazioni astratte permette di **ottimizzare le prestazioni** in circostanze diverse.

## Spiegazione

> 🧩 Esempio mio dal materiale della lezione: la [[pila]] si implementa con un [[array]] (contatore `top`) o con una [[lista-concatenata]]; la [[coda]] con un array circolare o con una lista ([[04-Strutture dati elementari.pdf#page=28]]). Chi usa $Push$/$Pop$ non vede la differenza; chi implementa sceglie in base a memoria, località e necessità di crescere.

La definizione di struttura dati della lezione 01 («modalità di memorizzazione e organizzazione dei dati pensata per facilitare l'accesso e la manipolazione», [[01-Introduzione.pdf#page=10]]) riguarda l'aspetto 2; le operazioni astratte l'aspetto 1.

## Perché importa

Separare **cosa** fa una struttura da **come** lo fa è il presupposto per analizzare un algoritmo senza fissarne subito l'implementazione, e per poi scegliere quella più efficiente.

## Connessioni

- [[strutture-contigue-e-collegate]] — le due grandi famiglie di implementazione
- [[pila]], [[coda]] — esempi di contenitori definiti dalle operazioni
- [[algoritmo-e-problema]] — definizione di struttura dati

## Fonti

- [[lezione-04-strutture-dati-elementari]]
- [[04-Strutture dati elementari.pdf#page=2]] (intestazione), [[04-Strutture dati elementari.pdf#page=3]], [[04-Strutture dati elementari.pdf#page=4]]

_Aggiornato: 2026-09-26 — ingest 04-Strutture dati elementari.pdf_
