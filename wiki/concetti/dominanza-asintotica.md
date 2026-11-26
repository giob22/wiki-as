---
tipo: concetto
importanza_esame: alta
prerequisiti: ["notazione-asintotica"]
fonti_pdf: ["02-Notazione asintotica.pdf#page=30", "02-Notazione asintotica.pdf#page=31", "02-Notazione asintotica.pdf#page=34", "02-Notazione asintotica.pdf#page=35", "02-Notazione asintotica.pdf#page=36", "02-Notazione asintotica.pdf#page=37"]
---

# Dominanza asintotica, little-o e crescita delle funzioni

## Definizione · [[02-Notazione asintotica.pdf#page=34|p. 34]], [[02-Notazione asintotica.pdf#page=36|p. 36]], [[02-Notazione asintotica.pdf#page=37|37]]

> 📄 Fonte: p. 34 — *Testing Dominance*

$f(n)$ **domina** $g(n)$ se
$$ \lim_{n\to\infty} \frac{g(n)}{f(n)} = 0 $$
il che equivale a dire $g(n) = o(f(n))$. Il **little-oh** significa «cresce **strettamente** più lentamente di».

Notazione: $f \gg g$ indica che $f$ domina $g$.

## Formule · [[02-Notazione asintotica.pdf#page=35|p. 35]]–[[02-Notazione asintotica.pdf#page=37|37]]

> 📄 Fonte: p. 35 — *Properties of Dominance*

- $n^a$ domina $n^b$ se $a > b$, poiché $\displaystyle\lim_{n\to\infty} n^b / n^a = n^{b-a} \to 0$.
- $n^a + o(n^a)$ **non** domina $n^a$, poiché $\displaystyle\lim_{n\to\infty} n^a / (n^a + o(n^a)) \to 1$.

> 📄 Classifica di base

> 🧮 Formula chiave:
$$ n! \gg 2^n \gg n^3 \gg n^2 \gg n \log n \gg n \gg \log n \gg 1 $$

> 📄 Fonte: p. 37 — *Advanced Dominance Rankings* (funzioni che compaiono in analisi più sofisticate di quelle del corso)
$$
n! \gg c^n \gg n^3 \gg n^2 \gg n^{1+\epsilon} \gg n\log n \gg n \gg \sqrt n \gg \log^2 n \gg \log n \gg \frac{\log n}{\log\log n} \gg \log\log n \gg \alpha(n) \gg 1
$$
> 📚 Fonte esterna: $\alpha(n)$ non è definita nelle slide; è l'inversa della funzione di Ackermann, di crescita lentissima (Cormen, 3ª ed., cap. 21, insiemi disgiunti).

## Derivazioni

### Derivazione — le due proprietà di p. 35 · [[02-Notazione asintotica.pdf#page=35|p. 35]]

$$
\begin{aligned}
\frac{n^b}{n^a} &= n^{b-a} && \text{proprietà delle potenze} \\
&= \frac{1}{n^{a-b}} \xrightarrow[n\to\infty]{} 0 && a - b > 0 \\[6pt]
\frac{n^a}{n^a + h(n)} &= \frac{1}{1 + h(n)/n^a} && h(n) = o(n^a),\ \text{divido per } n^a \\
&\xrightarrow[n\to\infty]{} \frac{1}{1 + 0} = 1 && h(n)/n^a \to 0 \text{ per definizione di } o
\end{aligned}
$$

Un limite pari a 1 (diverso da 0) significa che le due funzioni crescono allo stesso modo: aggiungere termini di ordine inferiore **non cambia** l'ordine di crescita.

> 🧩 Derivazione mia (collegamento con $\Theta$): se $\lim g/f = L$ con $0 < L < \infty$, allora per $n$ grande $\frac{L}{2} f \le g \le 2L f$, cioè $g = \Theta(f)$. Se $L = 0$, $g = o(f)$ e quindi $g = O(f)$ ma $g \ne \Omega(f)$.

### Derivazione — razzo contro vela solare · [[02-Notazione asintotica.pdf#page=30|p. 30]]
**Fonte:** il razzo raggiunge un'alta velocità prima di finire il carburante, poi prosegue a velocità costante $v_r$; la vela solare accelera lentamente per la radiazione/vento solare, ma la sua velocità $v_s = a\,t$ deve prima o poi superare quella del razzo. «This is asymptotic dominance in action.»

> 🧩 Derivazione mia: $v_s(t) > v_r \iff a\,t > v_r \iff t > v_r / a$. Per quanto grande sia $v_r$ (la «costante» del razzo), esiste sempre un istante oltre il quale vince la vela: una funzione che cresce ($a\,t$) domina una costante.

![[grafico-razzo-vela-solare.svg]]
> 🧩 Grafico generato da me con valori illustrativi ($v_r = 10$, $a = 0.5$): il sorpasso avviene a $t = v_r/a = 20$.

## Spiegazione · [[02-Notazione asintotica.pdf#page=31|p. 31]], [[02-Notazione asintotica.pdf#page=36|p. 36]]

> 📄 Fonte: p. 36 — *Crescita delle funzioni* (tempo di esecuzione se ogni operazione costa 1 ns)

| $n$ | $\lg n$ | $n$ | $n \lg n$ | $n^2$ | $2^n$ | $n!$ |
|---|---|---|---|---|---|---|
| 10 | 0.003 µs | 0.01 µs | 0.033 µs | 0.1 µs | 1 µs | 3.63 ms |
| 20 | 0.004 µs | 0.02 µs | 0.086 µs | 0.4 µs | 1 ms | 77.1 years |
| 30 | 0.005 µs | 0.03 µs | 0.147 µs | 0.9 µs | 1 sec | 8.4 × 10¹⁵ yrs |
| 40 | 0.005 µs | 0.04 µs | 0.213 µs | 1.6 µs | 18.3 min | |
| 50 | 0.006 µs | 0.05 µs | 0.282 µs | 2.5 µs | 13 days | |
| 100 | 0.007 µs | 0.1 µs | 0.644 µs | 10 µs | 4 × 10¹³ yrs | |
| 1,000 | 0.010 µs | 1.00 µs | 9.966 µs | 1 ms | | |
| 10,000 | 0.013 µs | 10 µs | 130 µs | 100 ms | | |
| 100,000 | 0.017 µs | 0.10 ms | 1.67 ms | 10 sec | | |
| 1,000,000 | 0.020 µs | 1 ms | 19.93 ms | 16.7 min | | |
| 10,000,000 | 0.023 µs | 0.01 sec | 0.23 sec | 1.16 days | | |
| 100,000,000 | 0.027 µs | 0.10 sec | 2.66 sec | 115.7 days | | |
| 1,000,000,000 | 0.030 µs | 1 sec | 29.90 sec | 31.7 years | | |

![[02-notazione-asintotica-p36-tabella-crescita-funzioni.png]]

> 🧩 Verifica mia: ricalcolata con [[tempi_crescita.py]] (1 ns per operazione, anno di 365 giorni); tutte le celle coincidono a meno di arrotondamenti ($n \lg n$ con $n = 10^4$: 132.9 µs, la slide scrive 130; con $n = 10^5$: 1.66 ms contro 1.67). Esempio di calcolo: $2^{40}$ ns $= 1.0995\cdot10^{12}$ ns $= 1099.5$ s $= 18.3$ min.

**Take-Home Lesson**: «Although esoteric functions arise in advanced algorithm analysis, a small variety of time complexities suffice and account for most algorithms that are widely used in practice.»

> 📄 Fonte: p. 31 — *Implications of Dominance*
- Gli algoritmi **esponenziali** diventano senza speranza molto in fretta.
- Gli algoritmi **quadratici** diventano senza speranza a (o prima di) $1\,000\,000$.
- $O(n\log n)$ è praticabile fino a circa **un miliardo**.
- $O(\log n)$ «never sweats».

> 🧩 Derivazione mia: sono le righe della tabella: $n^2$ con $n = 10^6$ → 16.7 min; $n\lg n$ con $n = 10^9$ → 29.9 s; $2^n$ già a $n = 50$ → 13 giorni; $\lg n$ con $n = 10^9$ → 0.03 µs.

![[grafico-crescita-funzioni.svg]]
> 🧩 Grafico generato da me: le funzioni della classifica in scala logaritmica per $1 \le n \le 50$. In scala log i polinomi $n^k$ crescono sempre più piano, $2^n$ è una retta, $n!$ piega verso l'alto: l'ordine delle curve a destra è la classifica di p. 36.

## Perché importa

Il test del limite è il modo più rapido per confrontare due funzioni di costo; la classifica serve a riconoscere a colpo d'occhio il termine dominante.

> 🎯 Esame: ordinare un elenco di funzioni per crescita; usare il limite del rapporto per decidere $o$, $\Theta$ o dominanza.

## Connessioni · 05-Insertion sort.pdf [[05-Insertion sort.pdf#page=37|p. 37]], [[05-Insertion sort.pdf#page=38|38]] · 01-Introduzione.pdf [[01-Introduzione.pdf#page=12|p. 12]]

- [[logaritmi-nell-analisi]] — da dove nascono i $\log n$ e perché la base non conta

- [[notazione-asintotica]] — $o$ è la versione stretta di $O$
- [[efficienza-degli-algoritmi]] — la tabella di p. 12 è il problema inverso (dato il tempo, trovare $n$)
- [[stima-dei-tempi-di-esecuzione]] — esercizi numerici
- [[ricerca-combinatoria]] — $n! \gg 2^n$

## Fonti · [[02-Notazione asintotica.pdf#page=29|p. 29]]–[[02-Notazione asintotica.pdf#page=31|31]], [[02-Notazione asintotica.pdf#page=33|p. 33]], [[02-Notazione asintotica.pdf#page=34|34]], [[02-Notazione asintotica.pdf#page=37|p. 37]]

- [[lezione-02-notazione-asintotica]]

_Aggiornato: 2026-09-26 — ingest 02-Notazione asintotica.pdf_

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_

<!-- nav:inizio -->
---
**Lezione 02 · pagina 8 di 8** · ← [[regole-di-calcolo-asintotico|Regole di calcolo con la notazione asintotica]] · [[lezioni|Indice]] · [[lezione-03-analisi-di-algoritmi|Lezione 03: introduzione e riepilogo]] →
<!-- nav:fine -->
