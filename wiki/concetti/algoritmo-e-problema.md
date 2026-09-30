---
tipo: concetto
importanza_esame: alta
prerequisiti: []
fonti_pdf: ["01-Introduzione.pdf#page=7", "01-Introduzione.pdf#page=9", "01-Introduzione.pdf#page=10"]
---

# Algoritmo, problema computazionale, istanza, correttezza, struttura dati

## Definizione

> 📄 Fonte: [[01-Introduzione.pdf#page=7]]

- Un **algoritmo** è una sequenza di passi computazionali che prende in *ingresso* un dato insieme di valori e produce un insieme di valori in *uscita*.
- Un algoritmo è uno strumento per risolvere un **problema computazionale** ben definito, cioè una relazione specificata tra ingresso e uscita.
- Un dato insieme di valori in ingresso costituisce un'**istanza** del problema.

> 📄 Fonte: [[01-Introduzione.pdf#page=9]], [[01-Introduzione.pdf#page=10]]

- Un algoritmo è **corretto** se, **per ogni istanza** del problema, **termina** fornendo l'insieme corretto di valori in uscita.
- Un algoritmo **incorretto** potrebbe, in corrispondenza di *alcune* istanze, non terminare oppure terminare con un'uscita non corretta.
- Una **struttura dati** è una modalità di memorizzazione e organizzazione dei dati pensata per facilitare l'accesso e la manipolazione dei dati.

La slide p. 8 introduce la definizione di correttezza lasciandola in sospeso («Un algoritmo è corretto se, …..»): è la versione "a comparsa" della p. 9.

## Formule

Il problema di esempio della fonte è l'[[ordinamento]] ([[01-Introduzione.pdf#page=7]]):

- **Input:** una sequenza di $n$ chiavi $\langle a_1, \dots, a_n \rangle$
- **Output:** la permutazione (riordinamento) $\langle a'_1, \dots, a'_n \rangle$ della sequenza d'ingresso tale che $a'_1 \le a'_2 \le \dots \le a'_n$

Simboli: $n$ = numero di chiavi (dimensione dell'istanza), $a_i$ = $i$-esima chiave in ingresso, $a'_i$ = $i$-esima chiave in uscita.

## Spiegazione

La definizione di correttezza ha **due** requisiti, entrambi quantificati su **tutte** le istanze:
1. **terminazione** — l'algoritmo si ferma;
2. **correttezza dell'uscita** — ciò che restituisce soddisfa la relazione ingresso/uscita del problema.

> 🧩 Derivazione mia: la negazione logica di «per ogni istanza termina con l'uscita corretta» è «**esiste** un'istanza su cui non termina **o** restituisce un'uscita sbagliata». Per questo basta **un solo controesempio** per dimostrare che un algoritmo è incorretto, mentre per dimostrarne la correttezza serve un argomento che copra tutte le istanze (→ [[ricerca-di-controesempi]], [[invariante-di-ciclo]], [[correttezza-per-induzione]]).

Esempio concreto dal corso: [[nearest-neighbor]] per il [[robot-tour-optimization]] termina sempre, ma su alcune istanze (punti sulla retta di [[01-Introduzione.pdf#page=24]]) restituisce un giro non minimo → è **incorretto** per quel problema ([[01-Introduzione.pdf#page=24]]).

## Perché importa

Tutto il corso ruota intorno ad **analisi** (correttezza, complessità) e **progettazione** di algoritmi ([[00-Presentazione.pdf#page=6]]): queste definizioni fissano cosa va dimostrato quando si dice che un algoritmo «funziona».

> 🎯 Esame: saper enunciare con precisione «algoritmo corretto» (per **ogni** istanza, **termina**, uscita **corretta**) e la definizione di struttura dati.

## Connessioni

- [[efficienza-degli-algoritmi]] — dopo la correttezza, la seconda proprietà richiesta ([[01-Introduzione.pdf#page=11]])
- [[metodi-euristici]] — procedure che non garantiscono l'uscita corretta su ogni istanza: per definizione non sono algoritmi corretti per il problema
- [[ricerca-di-controesempi]] — come si dimostra l'incorrettezza
- [[tipo-di-dato-astratto]] — la struttura dati vista attraverso le operazioni che supporta

## Fonti

- [[lezione-01-introduzione]]
- [[01-Introduzione.pdf#page=7]], [[01-Introduzione.pdf#page=8]], [[01-Introduzione.pdf#page=9]], [[01-Introduzione.pdf#page=10]]

_Aggiornato: 2026-09-26 — ingest 01-Introduzione.pdf_
