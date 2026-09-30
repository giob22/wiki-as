---
tipo: concetto
importanza_esame: alta
prerequisiti: ["algoritmo-e-problema"]
fonti_pdf: ["01-Introduzione.pdf#page=11", "01-Introduzione.pdf#page=12"]
---

# Efficienza degli algoritmi («Algorithms as a technology»)

## Definizione

> 📄 Fonte: [[01-Introduzione.pdf#page=11]]

L'**efficienza** di un algoritmo è solitamente misurata in termini di **numero di operazioni**, espresso in funzione della **dimensione dei dati in ingresso**, richieste per produrre i dati in uscita.

Oltre a **correttezza** ed **efficienza**, una terza proprietà, non meno importante, è la **facilità di implementazione** ([[01-Introduzione.pdf#page=11]]).

## Formule

Se un algoritmo esegue $f(n)$ operazioni su un'istanza di dimensione $n$ e il calcolatore esegue $v$ operazioni al secondo, il tempo è

$$ t = \frac{f(n)}{v} $$

- $n$ = dimensione dell'ingresso (per l'ordinamento: numero di elementi)
- $f(n)$ = numero di operazioni (adimensionale)
- $v$ = operazioni al secondo (nella slide $v = 10^9$ op/s)
- $t$ = tempo in secondi

Esempi della fonte: [[insertion-sort]] ha costo proporzionale a $n^2$, merge sort a $n\log n$ ([[01-Introduzione.pdf#page=11]]).

## Derivazioni

### Derivazione — insertion sort vs merge sort su un milione di elementi
**Fonte:** [[01-Introduzione.pdf#page=11]] (risultati «1000 secondi ~= 16 minuti» e «0,02 secondi»)
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

## Spiegazione

L'esercizio di [[01-Introduzione.pdf#page=12]] chiede, per ogni funzione $f(n) \in \{\lg n, \sqrt n, n, n\lg n, n^2, n^3, 2^n, n!\}$ e per ogni tempo $t \in$ {1 secondo, minuto, ora, giorno, mese, anno, secolo}, la **massima dimensione $n$** risolvibile in tempo $t$ se l'algoritmo impiega $f(n)$ microsecondi. La tabella è vuota nella slide: è svolta in [[stima-dei-tempi-di-esecuzione]].

Il risultato chiave dello svolgimento: in un secolo un algoritmo $2^n$ risolve solo $n \approx 51$ e un algoritmo $n!$ solo $n \approx 17$; un algoritmo lineare arriva a $\sim 3 \cdot 10^{15}$. Aumentare il tempo disponibile di un fattore enorme sposta di pochissimo $n$ per le funzioni esponenziali.

## Perché importa

Motiva lo studio dell'analisi asintotica ([[notazione-asintotica]], [[tempo-di-esecuzione]]): scegliere l'algoritmo giusto conta più che comprare un calcolatore più veloce.

## Connessioni

- [[algoritmo-e-problema]] — correttezza, la prima proprietà
- [[tempo-di-esecuzione]] — come si conta formalmente il numero di operazioni
- [[dominanza-asintotica]] — tabella dei tempi di [[02-Notazione asintotica.pdf#page=36]], stessa idea con 1 ns per operazione
- [[stima-dei-tempi-di-esecuzione]] — esercizi numerici

## Fonti

- [[lezione-01-introduzione]]
- [[01-Introduzione.pdf#page=11]], [[01-Introduzione.pdf#page=12]]

_Aggiornato: 2026-09-26 — ingest 01-Introduzione.pdf_

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_
