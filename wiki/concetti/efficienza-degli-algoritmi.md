---
tipo: concetto
importanza_esame: alta
prerequisiti: ["algoritmo-e-problema"]
fonti_pdf: ["01-Introduzione.pdf#page=11", "01-Introduzione.pdf#page=12"]
---

# Efficienza degli algoritmi («Algorithms as a technology»)

## Definizione · [[01-Introduzione.pdf#page=11|p. 11]]

L'**efficienza** di un algoritmo è solitamente misurata in termini di **numero di operazioni**, espresso in funzione della **dimensione dei dati in ingresso**, richieste per produrre i dati in uscita.

Oltre a **correttezza** ed **efficienza**, una terza proprietà, non meno importante, è la **facilità di implementazione**.

## Formule · 01-Introduzione.pdf [[01-Introduzione.pdf#page=11|p. 11]] · Merge Sort [[06-Merge Sort (1).pdf#page=29|p. 27]]

Se un algoritmo esegue $f(n)$ operazioni su un'istanza di dimensione $n$ e il calcolatore esegue $v$ operazioni al secondo, il tempo è

$$ t = \frac{f(n)}{v} $$

- $n$ = dimensione dell'ingresso (per l'ordinamento: numero di elementi)
- $f(n)$ = numero di operazioni (adimensionale)
- $v$ = operazioni al secondo (nella slide $v = 10^9$ op/s)
- $t$ = tempo in secondi

Esempi della fonte: [[insertion-sort]] ha costo proporzionale a $n^2$, [[merge-sort]] a $n\log n$ (dimostrato nella lezione 06).

## Derivazioni

### Derivazione — insertion sort vs merge sort su un milione di elementi · [[01-Introduzione.pdf#page=11|p. 11]]
**Si parte da:** $t = f(n)/v$ con $n = 10^6$, $v = 10^9$ op/s, costanti moltiplicative ignorate (come fa la slide)

$$
\begin{aligned}
t_{IS} &= \frac{n^2}{v} = \frac{(10^6)^2}{10^9}  && f(n) = n^2 \\
       &= \frac{10^{12}}{10^9} = 10^3\ \text{s}    && \text{potenze di 10} \\
       &= \frac{1000}{60}\ \text{min} \approx 16.7\ \text{min} && 1\ \text{min} = 60\ \text{s} \\[4pt]
t_{MS} &= \frac{n \lg n}{v} = \frac{10^6 \cdot \lg 10^6}{10^9} && f(n) = n\lg n,\ \text{log in base 2} \\
       &= \frac{10^6 \cdot 19.93}{10^9}              && \lg 10^6 = 6\,\lg 10 = 6 \cdot 3.3219 \\
       &\approx 0.0199\ \text{s} \approx 0.02\ \text{s}
\end{aligned}
$$

**Sanity check:** rapporto $t_{IS}/t_{MS} = n/\lg n = 10^6/19.93 \approx 5 \cdot 10^4$ — coerente con $1000\ \text{s} / 0.02\ \text{s} = 5\cdot 10^4$. Verificato con [[tempi_crescita.py]].
**Ipotesi:** costanti moltiplicative uguali a 1 per entrambi gli algoritmi; logaritmo in base 2 (se fosse in base 10, $\log_{10} 10^6 = 6$ darebbe $0.006$ s: la slide usa quindi la base 2); stesso calcolatore.

> 💡 Connessione: il messaggio della slide («per insiemi di valori in ingresso di dimensioni notevoli, la differenza in termini di efficienza è marcata») è l'idea della [[dominanza-asintotica]]: conta l'**ordine di crescita**, non la velocità della macchina.

## Spiegazione · [[01-Introduzione.pdf#page=12|p. 12]]

L'esercizio di p. 12 chiede, per ogni funzione $f(n) \in \{\lg n, \sqrt n, n, n\lg n, n^2, n^3, 2^n, n!\}$ e per ogni tempo $t \in$ {1 secondo, minuto, ora, giorno, mese, anno, secolo}, la **massima dimensione $n$** risolvibile in tempo $t$ se l'algoritmo impiega $f(n)$ microsecondi. La tabella è vuota nella slide: è svolta in [[stima-dei-tempi-di-esecuzione]].

Il risultato chiave dello svolgimento: in un secolo un algoritmo $2^n$ risolve solo $n \approx 51$ e un algoritmo $n!$ solo $n \approx 17$; un algoritmo lineare arriva a $\sim 3 \cdot 10^{15}$. Aumentare il tempo disponibile di un fattore enorme sposta di pochissimo $n$ per le funzioni esponenziali.

## Perché importa

Motiva lo studio dell'analisi asintotica ([[notazione-asintotica]], [[tempo-di-esecuzione]]): scegliere l'algoritmo giusto conta più che comprare un calcolatore più veloce.

## Connessioni · 02-Notazione asintotica.pdf [[02-Notazione asintotica.pdf#page=36|p. 36]] · Quicksort [[07-Quicksort 1.pdf#page=2|p. 2]]

- [[algoritmo-e-problema]] — correttezza, la prima proprietà
- [[tempo-di-esecuzione]] — come si conta formalmente il numero di operazioni
- [[dominanza-asintotica]] — tabella dei tempi di p. 36, stessa idea con 1 ns per operazione
- [[stima-dei-tempi-di-esecuzione]] — esercizi numerici
- [[quicksort]] — «tra i più efficienti» nella pratica perché i fattori nascosti in $\Theta(n\lg n)$ sono piccoli: a parità di ordine di crescita contano le costanti

## Fonti · [[01-Introduzione.pdf#page=11|p. 11]], [[01-Introduzione.pdf#page=12|12]]

- [[lezione-01-introduzione]]

_Aggiornato: 2026-09-26 — ingest 01-Introduzione.pdf_

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_
_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf e 07-Quicksort.pdf_
_Aggiornato: 2026-10-10 — link ripuntati alla versione aggiornata delle slide 06-Merge Sort (1).pdf_
_Aggiornato: 2026-10-14 — link ripuntati alla versione aggiornata delle slide 07-Quicksort 1.pdf_

<!-- nav:inizio -->
---
**Lezione 01 · pagina 4 di 18** · ← [[ordinamento|Problema dell'ordinamento (Sorting)]] · [[lezioni|Indice]] · [[stima-dei-tempi-di-esecuzione|Stima dei tempi di esecuzione e dell'n massimo risolvibile]] →
<!-- nav:fine -->
