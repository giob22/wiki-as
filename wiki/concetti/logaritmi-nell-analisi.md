---
tipo: concetto
importanza_esame: alta
prerequisiti: ["dominanza-asintotica"]
fonti_pdf: ["05-Insertion sort.pdf#page=32", "05-Insertion sort.pdf#page=33"]
---

# L'importanza dei logaritmi

## Definizione

> 📄 Fonte: [[05-Insertion sort.pdf#page=32]] — «Crescita delle funzioni: l'importanza dei logaritmi»

*«Logarithms arise in any process where things are repeatedly halved.»* I logaritmi compaiono in ogni processo in cui qualcosa viene **ripetutamente dimezzato** (o diviso per una costante).

> 🧩 Derivazione mia (perché): se a ogni passo la dimensione passa da $n$ a $n/2$, dopo $k$ passi è $n/2^k$. Il processo finisce quando $n/2^k \le 1$, cioè $k \ge \lg n$: il numero di passi è $\lceil \lg n \rceil$. Qui e nel resto del wiki $\lg = \log_2$.

## Formule

Esempi elencati nella slide ([[05-Insertion sort.pdf#page=32]]), con i passaggi che la slide lascia impliciti:

| Esempio (slide) | Risultato | Derivazione (🧩 mia dove la slide non la dà) |
|-----------------|-----------|--------------------------------------------|
| **Binary Search** | $O(\lg n)$ confronti | ogni confronto dimezza l'intervallo di ricerca (vedi p. 33, sotto) |
| **Trees** — altezza $h$ di un albero con $d$ figli per nodo e $n$ foglie | $h = \log_d n$ | un albero completo di altezza $h$ ha $d^h$ foglie: $d^h = n \Rightarrow h = \log_d n$ |
| **Bits** — quanti bit servono per rappresentare una qualunque tra $n$ possibilità? | $\lceil \lg n \rceil$ | con $b$ bit si distinguono $2^b$ valori: serve $2^b \ge n \Rightarrow b = \lceil \lg n \rceil$ |
| **Multiplication** | $a^b = \exp(\ln(a^b)) = \exp(b \ln a)$ | proprietà $\ln(a^b) = b \ln a$: il logaritmo trasforma potenze in prodotti (e prodotti in somme) |
| **Fast exponentiation** | $O(\lg n)$ moltiplicazioni | vedi [[potenza-veloce]] |
| **Summation** — numeri armonici | $H(n) = \sum_{i=1}^{n} \frac{1}{i} \sim \ln n$ | vedi derivazione sotto |

**Numeri (🧩, calcolati con [[stringhe_e_logaritmi.py]]):** albero binario con 8 foglie → $h = 3$; albero con $d = 10$ e $10^6$ foglie → $h = 6$; per $n = 10^6$ possibilità servono 20 bit.

![[05-insertion-sort-p32-logaritmi.png]]

## Derivazioni

### Derivazione — $H(n) \sim \ln n$
**Fonte:** [[05-Insertion sort.pdf#page=32]] (risultato dato senza passaggi)
**Si parte da:** confronto tra la somma e l'integrale di $1/x$, che è decrescente

> 🧩 Derivazione mia:
$$
\begin{aligned}
\frac{1}{i} &\le \int_{i-1}^{i} \frac{dx}{x} \quad (i \ge 2) && 1/x \ge 1/i \text{ su } [i-1, i] \\
H(n) &= 1 + \sum_{i=2}^{n} \frac1i \le 1 + \int_{1}^{n} \frac{dx}{x} = 1 + \ln n && \text{sommo le disuguaglianze} \\
\frac{1}{i} &\ge \int_{i}^{i+1} \frac{dx}{x} && 1/x \le 1/i \text{ su } [i, i+1] \\
H(n) &\ge \int_{1}^{n+1} \frac{dx}{x} = \ln(n+1) && \text{sommo per } i = 1..n \\
\Rightarrow\ \ln(n+1) &\le H(n) \le \ln n + 1 && \text{quindi } H(n)/\ln n \to 1
\end{aligned}
$$
**Sanity check:** $H(10^6) = 14.3927$, $\ln 10^6 = 13.8155$: la differenza $0.577$ resta limitata (tende alla costante di Eulero–Mascheroni $\gamma \approx 0.5772$), come prevede $H(n) = \ln n + O(1)$.

### Derivazione — l'importanza di uno split equilibrato
**Fonte:** [[05-Insertion sort.pdf#page=33]] — *S&T: Importance of an Even Split*

> **Problem:** quante domande richiede la ricerca binaria sull'elenco telefonico di Manhattan da un milione di nomi, se ogni divisione fosse 1/3–2/3 invece di 1/2–1/2?

Risposta della slide:
- $\log_{3/2}(1{,}000{,}000) \approx 35$ chiamate nel caso peggiore;
- $\log_{2}(1{,}000{,}000) \approx 20$ chiamate nel caso peggiore.

> **Take-home lesson:** *The power of binary search comes from its logarithmic complexity, not the base of the log.*

> 🧩 Derivazione mia:
$$
\begin{aligned}
&\text{caso peggiore: si prosegue sempre nella parte da } 2/3 && \text{dopo } k \text{ domande restano } n\,(2/3)^k \\
&n\left(\tfrac23\right)^k \le 1 \iff k \ge \log_{3/2} n && \text{prendo il logaritmo in base } 3/2 \\
&\log_{3/2} 10^6 = \frac{\ln 10^6}{\ln 1.5} = \frac{13.8155}{0.4055} = 34.07 \to 35 && \text{arrotondo per eccesso} \\
&\lg 10^6 = 19.93 \to 20 \\
&\log_{3/2} n = \frac{\lg n}{\lg(3/2)} = 1.71\,\lg n && \text{cambio di base: fattore costante}
\end{aligned}
$$
>
> Lo split sbilanciato costa circa il 71 % di domande in più, ma resta **logaritmico**. Il cambio di base moltiplica per una costante, e la [[notazione-asintotica]] ignora le costanti: $\log_{3/2} n = \Theta(\lg n)$. Per questo dentro $O(\cdot)$ la base del logaritmo si omette.
>
> **Sanity check:** una simulazione in [[stringhe_e_logaritmi.py]] che scarta a ogni domanda anche l'elemento interrogato dà 33 domande (1/3–2/3) e 20 (1/2–1/2). Il valore «≈ 35» della slide è la stima $\lceil \log_{3/2} 10^6 \rceil$; l'ordine di grandezza e il rapporto ≈ 1.7 coincidono.

![[05-insertion-sort-p33-split-ricerca-binaria.png]]

## Spiegazione

Nella classifica di [[dominanza-asintotica]] $\log n$ sta appena sopra le costanti: «$O(\log n)$ never sweats» ([[02-Notazione asintotica.pdf#page=31]]). Questa lezione mostra *da dove* nascono i logaritmi: dal dimezzamento ripetuto (ricerca binaria, potenza veloce), dagli alberi e dalla rappresentazione binaria.

## Perché importa

> 🎯 Esame: riconoscere il dimezzamento ripetuto come fonte di $\lg n$; spiegare perché la base del logaritmo non conta asintoticamente (take-home lesson di p. 33).

## Connessioni

- [[potenza-veloce]] — esempio di algoritmo $O(\lg n)$
- [[dominanza-asintotica]] — posizione di $\log n$ nella classifica
- [[notazione-asintotica]] — il cambio di base è un fattore costante

## Fonti

- [[lezione-05-insertion-sort]]
- [[05-Insertion sort.pdf#page=32]], [[05-Insertion sort.pdf#page=33]]

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_
