---
tipo: concetto
importanza_esame: alta
prerequisiti: ["equazioni-di-ricorrenza", "notazione-asintotica", "metodo-albero-di-ricorrenza"]
fonti_pdf: ["06-Merge Sort.pdf#page=28", "06-Merge Sort.pdf#page=29", "06-Merge Sort.pdf#page=30", "07-Quicksort.pdf#page=15"]
---

# Teorema dell'esperto (metodo dell'esperto)

## Definizione

> 📄 Fonte: [[06-Merge Sort.pdf#page=28]]

Il **metodo dell'esperto** si basa sul **teorema dell'esperto** (*master theorem*).

Siano $a \ge 1$ e $b > 1$ costanti, $f(n)$ una funzione e
$$ T(n) = aT(n/b) + f(n) $$
dove $n/b$ può essere interpretato sia come $\lfloor n/b \rfloor$ che come $\lceil n/b \rceil$. Allora:

1. se $f(n) = O\!\left(n^{\log_b a - \epsilon}\right)$ per un dato $\epsilon > 0$, allora $T(n) = \Theta\!\left(n^{\log_b a}\right)$;
2. se $f(n) = \Theta\!\left(n^{\log_b a}\right)$, allora $T(n) = \Theta\!\left(n^{\log_b a} \lg n\right)$;
3. se $f(n) = \Omega\!\left(n^{\log_b a + \epsilon}\right)$ per un dato $\epsilon > 0$ **e** $af(n/b) \le cf(n)$ per una data $c < 1$ ed $n$ sufficientemente grande, allora $T(n) = \Theta(f(n))$.

**Osservazioni:**
- intuitivamente, la soluzione è data dalla **più grande** tra $f(n)$ e $n^{\log_b a}$;
- $f(n)$ deve essere **polinomialmente** più piccola (grande) di $n^{\log_b a}$ (c'è $\epsilon$);
- ⇒ c'è un **gap** tra il caso 1) e 2) e tra il caso 2) e 3).

![[06-merge-sort-p28-teorema-esperto.png]]

## Formule

> 🧮 Formula chiave — il confronto da fare sempre:
$$ f(n) \quad \text{contro} \quad n^{\log_b a} $$
Simboli: $a$ = numero di sottoproblemi; $n/b$ = dimensione di ciascuno ($1/b$ = fattore di riduzione, come in [[06-Merge Sort.pdf#page=14]]); $f(n)$ = costo di divisione e ricombinazione, $D(n) + C(n)$ nella ricorrenza del [[divide-et-impera]]; $n^{\log_b a}$ = numero di foglie dell'albero di ricorrenza; $\epsilon$ = margine polinomiale; $c$ = costante della **condizione di regolarità** del caso 3.

> 🧩 Spiegazione mia — da dove viene il confronto, con il [[metodo-albero-di-ricorrenza]]: la radice costa $f(n)$, le foglie sono $a^{\log_b n} = n^{\log_b a}$ e costano $\Theta(1)$ ciascuna.
> - **Caso 1:** i livelli crescono geometricamente verso le foglie ⇒ dominano le foglie: $\Theta(n^{\log_b a})$.
> - **Caso 2:** tutti i $\log_b n + 1$ livelli costano circa $n^{\log_b a}$ ⇒ costo per livello × numero di livelli: $\Theta(n^{\log_b a}\lg n)$.
> - **Caso 3:** i livelli decrescono geometricamente dalla radice ⇒ domina la radice: $\Theta(f(n))$. La condizione $af(n/b) \le cf(n)$ dice proprio che il livello 1 costa al più $c < 1$ volte il livello 0.

## Derivazioni

### Esempi della slide
> 📄 Fonte: [[06-Merge Sort.pdf#page=29]] (enunciati e caso applicato); commenti 🧩 miei

![[06-merge-sort-p29-esempi-esperto.png]]

**Esempio 1 — $T(n) = 9T(n/3) + n$**

$$
\begin{aligned}
&a = 9,\ b = 3,\ f(n) = n,\quad n^{\log_b a} = n^{\log_3 9} = n^2 && \log_3 9 = 2 \text{ perché } 3^2 = 9 \\
&n = f(n) = O\!\left(n^{\log_3 9 - \epsilon}\right) = O(n^{2-\epsilon}) \text{ con } \epsilon = 1 && n \le 1 \cdot n^{1}\text{: } c = 1,\ n_0 = 1 \\
&\Rightarrow \text{caso 1:}\ \ T(n) = \Theta(n^2)
\end{aligned}
$$

> **Sanity check** ([[divide_et_impera.py]], $T(1) = 1$, $n$ potenza di 3): $T(n)/n^2 = 1.4979,\ 1.4999,\ 1.5000$ per $n = 3^5, 3^8, 3^{11}$. 🧩 La soluzione esatta è $T(n) = \frac{3}{2}n^2 - \frac{1}{2}n$: provando $T(n) = An^2 + Bn$ nella ricorrenza si trova $B = 3B + 1$, cioè $B = -\frac12$, e $T(1) = 1$ dà $A = \frac32$.

**Esempio 2 — $T(n) = T(2n/3) + 1$**

$$
\begin{aligned}
&a = 1,\ b = 3/2,\ f(n) = 1,\quad n^{\log_b a} = n^{\log_{3/2} 1} = n^0 = 1 && \log_b 1 = 0 \text{ per ogni base} \\
&1 = f(n) = \Theta\!\left(n^{\log_b a}\right) = \Theta(1) \\
&\Rightarrow \text{caso 2:}\ \ T(n) = \Theta(n^0 \lg n) = \Theta(\lg n)
\end{aligned}
$$

> 🧩 Nota: $b = 3/2$ perché $2n/3 = n/(3/2)$. Srotolando, $T(n) = T(1) + \log_{3/2} n$, cioè $\approx 1.71 \lg n$. È la ricorrenza di una ricerca che scarta un terzo dei candidati a ogni passo (lo «split sbilanciato» di [[05-Insertion sort.pdf#page=33]], → [[logaritmi-nell-analisi]]). [[divide_et_impera.py]]: $T(n)/\lg n = 1.61,\ 1.66,\ 1.67$ per $n = 10^3, 10^6, 10^9$, verso $1/\lg(3/2) \approx 1.71$.

**Esempio 3 — $T(n) = 3T(n/4) + n\lg n$**

$$
\begin{aligned}
&a = 3,\ b = 4,\ f(n) = n\lg n,\quad n^{\log_b a} = n^{\log_4 3} && \log_4 3 \approx 0.793 \\
&n\lg n = f(n) = \Omega\!\left(n^{\log_4 3 + \epsilon}\right) \text{ con } \epsilon \approx 0.2 && n\lg n \ge n = n^{0.793 + 0.207} \text{ per } n \ge 2 \\
&af(n/b) = 3\,\tfrac{n}{4}\lg\tfrac{n}{4} \le \tfrac{3}{4}\, n\lg n = cf(n) \text{ con } c = 3/4 && \lg\tfrac{n}{4} = \lg n - 2 \le \lg n \\
&\Rightarrow \text{caso 3:}\ \ T(n) = \Theta(n\lg n)
\end{aligned}
$$

> **Sanity check** ([[divide_et_impera.py]]): $T(n)/(n\lg n) = 2.19,\ 2.66,\ 2.96$ per $n = 4^5, 4^8, 4^{11}$: cresce lentamente verso una costante. 🧩 Con l'albero si trova $T(n) \approx 4n\lg n - 24n$ (serie $\sum (3/4)^i = 4$ e $\sum i(3/4)^i = 12$), quindi il rapporto è $\approx 4 - 24/\lg n$; per $n = 4^{20}$ e $4^{40}$ il calcolo dà 3.40 e 3.70, come previsto.

### Esempio fuori dal teorema: il gap tra i casi 2 e 3
> 📄 Fonte: [[06-Merge Sort.pdf#page=30]]

$T(n) = 2T(n/2) + n\lg n$:
- $a = 2$, $b = 2$, $f(n) = n\lg n$, $n^{\log_b a} = n^{\log_2 2} = n$;
- $f(n) = n\lg n$ **non** è polinomialmente più grande di $n$;
- $f(n)/n^{\log_b a} = n\lg n / n = \lg n$ è asintoticamente più piccolo di $n^\epsilon$, per ogni $\epsilon > 0$;
- questa ricorrenza ricade nel **gap tra i casi 2) e 3)**.

> 🧩 Derivazione mia — perché nessun caso si applica:
> - caso 3 richiederebbe $n\lg n \ge c'\,n^{1+\epsilon}$, cioè $\lg n \ge c'\,n^\epsilon$: falso, perché $\lim_{n\to\infty} \lg n / n^\epsilon = 0$ per ogni $\epsilon > 0$ ([[dominanza-asintotica]]);
> - caso 2 richiederebbe $n\lg n = \Theta(n)$: falso, perché $\lg n \to \infty$.
>
> Il teorema non si applica, ma l'albero sì. Al livello $i$ ci sono $2^i$ nodi su $n/2^i$ elementi:
$$
\begin{aligned}
\text{costo del livello } i &= 2^i \cdot \tfrac{n}{2^i}\lg\tfrac{n}{2^i} = n(\lg n - i) && \lg\tfrac{n}{2^i} = \lg n - i \\
T(n) &\approx \sum_{i=0}^{\lg n - 1} n(\lg n - i) = n\sum_{k=1}^{\lg n} k && k = \lg n - i \\
     &= n\,\frac{\lg n(\lg n + 1)}{2} = \Theta(n\lg^2 n) && \text{somma di Gauss}
\end{aligned}
$$
> Verifica ([[divide_et_impera.py]]): $T(n)/(n\lg^2 n) = 0.560,\ 0.528,\ 0.513$ per $n = 2^{10}, 2^{20}, 2^{40}$, verso $\frac12$; $T(n)/(n\lg n)$ invece cresce senza limite (5.6, 10.6, 20.5).

### Applicazioni nelle lezioni

| Ricorrenza | $a$, $b$, $f(n)$ | $n^{\log_b a}$ | Caso | Soluzione | Fonte |
|------------|------------------|----------------|------|-----------|-------|
| [[merge-sort]]: $2T(n/2) + \Theta(n)$ | 2, 2, $\Theta(n)$ | $n$ | 2 | $\Theta(n\lg n)$ | 🧩 da [[06-Merge Sort.pdf#page=17]] |
| [[quicksort]], caso migliore: $T(n) \le 2T(n/2) + \Theta(n)$ | 2, 2, $\Theta(n)$ | $n$ | 2 | $O(n\lg n)$ | [[07-Quicksort.pdf#page=15]] |
| $3T(\lfloor n/4 \rfloor) + \Theta(n^2)$ | 3, 4, $\Theta(n^2)$ | $n^{0.79}$ | 3 (🧩, regolarità con $c = 3/16$) | $\Theta(n^2)$ | 🧩, confronta [[06-Merge Sort.pdf#page=27]] |

> 🧩 Il teorema **non** si applica alle ricorrenze con sottoproblemi di dimensione $n - 1$ ($b$ non è una costante $> 1$): ad esempio il caso peggiore di quicksort, $T(n-1) + \Theta(n)$ ([[07-Quicksort.pdf#page=14]]), o la [[torre-di-hanoi]]. Per quelle si srotola la ricorrenza ([[equazioni-di-ricorrenza]]).

## Spiegazione

Procedura d'uso (🧩):
1. riconoscere la forma $aT(n/b) + f(n)$, con $a \ge 1$ e $b > 1$ **costanti**;
2. calcolare $n^{\log_b a}$;
3. confrontare $f(n)$ con $n^{\log_b a}$: più piccola di un fattore $n^\epsilon$ (caso 1), dello stesso ordine (caso 2), più grande di un fattore $n^\epsilon$ **e** regolare (caso 3);
4. se $f$ cade nel gap (differisce solo per fattori logaritmici), il teorema non dice nulla: usare l'albero o la sostituzione.

## Perché importa

> 🎯 Esame: applicare il teorema esplicitando $a$, $b$, $f(n)$, $n^{\log_b a}$, il caso, $\epsilon$ e (nel caso 3) la costante $c$ della condizione di regolarità; riconoscere quando non si applica (esempio $2T(n/2) + n\lg n$).

## Connessioni

- [[metodo-albero-di-ricorrenza]] — i tre casi sono i tre comportamenti dell'albero
- [[metodo-di-sostituzione]] — serve quando il teorema non si applica o per dimostrarlo
- [[divide-et-impera]] — la ricorrenza $aT(n/b) + D(n) + C(n)$ ha esattamente questa forma
- [[dominanza-asintotica]] — «polinomialmente più grande» si decide con i limiti tra potenze e logaritmi
- [[logaritmi-nell-analisi]] — $n^{\log_b a}$ e il cambio di base
- [[risoluzione-ricorrenze]] — esercizi

## Fonti

- [[lezione-06-merge-sort]], [[lezione-07-quicksort]]
- [[06-Merge Sort.pdf#page=28]]–[[06-Merge Sort.pdf#page=30]], [[07-Quicksort.pdf#page=15]]

_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf e 07-Quicksort.pdf_
