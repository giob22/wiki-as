---
tipo: entità
categoria: problema
fonti_pdf: ["01-Introduzione.pdf#page=13", "01-Introduzione.pdf#page=14", "01-Introduzione.pdf#page=35"]
---

# Robot Tour Optimization (problema del commesso viaggiatore, TSP)

## Definizione formale

> 📄 Fonte: [[01-Introduzione.pdf#page=14]]

- **Problem:** Robot Tour Optimization
- **Input:** un insieme $S$ di $n$ punti nel piano
- **Output:** qual è il **ciclo più corto** che visita ogni punto dell'insieme $S$?

Il problema è introdotto come «S&T» (*Stop & Think*): Problema 1 ([[01-Introduzione.pdf#page=13]]). Le figure delle pp. 14–15 ([[01-Introduzione.pdf#page=14]], [[01-Introduzione.pdf#page=15]]) mostrano un robot (un aspirapolvere) che deve muoversi tra le stanze di una pianta: l'obiettivo è il giro più breve. È il famoso **problema del commesso viaggiatore** (*Traveling Salesman Problem*) ([[01-Introduzione.pdf#page=35]]).

> 🧩 Derivazione mia (formalizzazione): un giro è una permutazione $\pi$ dei punti; la sua lunghezza è $\text{cost}(\pi) = \sum_{i=1}^{n-1} d(p_{\pi(i)}, p_{\pi(i+1)}) + d(p_{\pi(n)}, p_{\pi(1)})$, con $d$ = distanza euclidea. Si cerca $\pi$ che minimizza $\text{cost}(\pi)$.

## Algoritmi che lo risolvono (lezione 01)

| Soluzione | Algoritmo | Corretto? | Efficiente? | Pagina |
|-----------|-----------|-----------|-------------|--------|
| 1 | [[nearest-neighbor]] | **no** — controesempio sulla retta | sì | [[01-Introduzione.pdf#page=18]], [[01-Introduzione.pdf#page=24]] |
| 2 | [[closest-pair]] | **no** — controesempio a due file di punti | sì (più complessa) | [[01-Introduzione.pdf#page=26]], [[01-Introduzione.pdf#page=28]] |
| 3 | [[optimal-tsp]] | **sì** | **no** — $n!$ permutazioni | [[01-Introduzione.pdf#page=29]], [[01-Introduzione.pdf#page=33]] |

Figure delle istanze:

![[01-introduzione-p17-nearest-neighbor-caso-buono.png]]
*Punti su una circonferenza (p. 16–17): qui [[nearest-neighbor]] trova il giro giusto 0→1→…→8→0. ([[01-Introduzione.pdf#page=17]])*

![[01-introduzione-p21-nearest-neighbor-punti-casuali.png]]
*Punti sparsi (pp. 20–21) e giro prodotto da nearest-neighbor, con incroci evidenti. ([[01-Introduzione.pdf#page=21]])*

«Soluzione? Ne discuteremo ….» ([[01-Introduzione.pdf#page=35]]): la lezione non presenta un algoritmo corretto ed efficiente. La slide cita (Skiena) che per 20 punti nemmeno un calcolatore potente enumererebbe le $20!$ permutazioni in un giorno e che per circuiti reali con $n \approx 1000$ tutti i computer del mondo non finirebbero prima della fine dell'universo ([[01-Introduzione.pdf#page=34]]).

> 🎯 Esame: Take-Home Lesson #1 — differenza tra **algoritmi** (sempre corretti) ed **euristiche** (spesso buone, nessuna garanzia) → [[metodi-euristici]].

## Connessioni

- [[ricerca-combinatoria]], [[metodi-euristici]] — il commesso viaggiatore è esempio di entrambe ([[03-Analisi di algoritmi.pdf#page=5]], [[03-Analisi di algoritmi.pdf#page=6]])
- [[controesempi-per-euristiche]] — controesempi svolti e verificati

## Fonti

- [[lezione-01-introduzione]]
- [[01-Introduzione.pdf#page=13]]–[[01-Introduzione.pdf#page=35]]

_Aggiornato: 2026-09-26 — ingest 01-Introduzione.pdf_

<!-- nav:inizio -->
---
**Lezione 01 · pagina 6 di 18** · ← [[stima-dei-tempi-di-esecuzione|Stima dei tempi di esecuzione e dell'n massimo risolvibile]] · [[lezioni|Indice]] · [[nearest-neighbor|NearestNeighbor (Soluzione 1 del Robot Tour)]] →
<!-- nav:fine -->
