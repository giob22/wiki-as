---
tipo: concetto
importanza_esame: alta
prerequisiti: ["algoritmo-e-problema"]
fonti_pdf: ["03-Analisi di algoritmi.pdf#page=13", "03-Analisi di algoritmi.pdf#page=14", "03-Analisi di algoritmi.pdf#page=15", "01-Introduzione.pdf#page=60"]
---

# Incorrettezza e ricerca di controesempi

## Definizione

> 📄 Fonte: [[03-Analisi di algoritmi.pdf#page=13]]

Per mostrare l'**incorrettezza** di un algoritmo: «Searching for **counterexamples** is the best way to disprove the correctness». Un **controesempio** è un'istanza del problema su cui l'algoritmo non termina o restituisce un'uscita sbagliata.

**Testing:** definire casi di test aiuta a scoprire malfunzionamenti, dimostrando l'incorrettezza dell'algoritmo; va usato **in congiunzione** con l'analisi formale di correttezza.

> 📄 Fonte: [[03-Analisi di algoritmi.pdf#page=15]]

Ma **fallire** nella ricerca di un controesempio **non è garanzia** di correttezza dell'algoritmo.

> 📄 Fonte: [[01-Introduzione.pdf#page=60]] — *Take-Home Lesson #2*

> Reasonable-looking algorithms can easily be incorrect. Algorithm correctness is a property that must be carefully demonstrated.

## Spiegazione

Suggerimenti per trovare controesempi ([[03-Analisi di algoritmi.pdf#page=14]]):

| Tip | Significato | Esempio nel corso |
|-----|-------------|-------------------|
| **Think small** | di solito esiste un esempio molto semplice su cui l'algoritmo fallisce | 3 intervalli bastano a battere [[shortest-job-first]] |
| **Think exhaustively** | per il più piccolo $n$ non banale le possibilità sono poche: si possono costruire tutte, controesempi inclusi | verifica esaustiva di [[optimal-scheduling]] su istanze piccole ([[controesempi_euristiche.py]]) |
| **Hunt for the weakness** | es. gli algoritmi greedy («prendi sempre il più grande») si rompono col tip successivo | [[earliest-job-first]]: la debolezza è il job lungo che inizia per primo |
| **Go for a tie** | per le greedy, istanze in cui tutto ha la stessa dimensione | punti della retta di [[nearest-neighbor]]: a ogni passo due punti equidistanti |
| **Seek extremes** | (boundary-value testing) mescolare enorme e minuscolo, sinistra e destra, pochi e molti, vicino e lontano | punti $-21 \dots 11$: distanze che raddoppiano, a sinistra e a destra |

> 🧩 Derivazione mia (colonna «Esempio nel corso»): associazione tra i tip della lezione 03 e i controesempi della lezione 01; i controesempi sono svolti in [[controesempi-per-euristiche]].

**Perché un controesempio basta e un test superato no:** la correttezza è un'affermazione universale («per ogni istanza»); un controesempio la falsifica, mentre un numero finito di test superati non copre le infinite istanze possibili. Per dimostrare la correttezza servono [[invariante-di-ciclo]] (algoritmi iterativi) o [[correttezza-per-induzione]] (algoritmi ricorsivi).

## Perché importa

> 🎯 Esame: dato un algoritmo greedy, costruire il controesempio più piccolo possibile; spiegare perché i test non dimostrano la correttezza.

## Connessioni

- [[metodi-euristici]] — i bersagli naturali dei controesempi
- [[invariante-di-ciclo]], [[correttezza-per-induzione]] — le dimostrazioni positive
- [[controesempi-per-euristiche]] — esercizi

## Fonti

- [[lezione-03-analisi-di-algoritmi]], [[lezione-01-introduzione]]
- [[03-Analisi di algoritmi.pdf#page=12]] (intestazione «Correttezza»), [[03-Analisi di algoritmi.pdf#page=13]], [[03-Analisi di algoritmi.pdf#page=14]], [[03-Analisi di algoritmi.pdf#page=15]], [[01-Introduzione.pdf#page=60]]

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_

<!-- nav:inizio -->
---
**Lezione 01 · pagina 17 di 18** · ← [[optimal-scheduling|OptimalScheduling (Soluzione 4 del Movie Scheduling)]] · [[lezioni|Indice]] · [[controesempi-per-euristiche|Trovare controesempi per euristiche (greedy)]] →
<!-- nav:fine -->
