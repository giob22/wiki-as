---
tipo: concetto
importanza_esame: alta
prerequisiti: ["equazioni-di-ricorrenza", "notazione-asintotica", "correttezza-per-induzione"]
fonti_pdf: ["06-Merge Sort (1).pdf#page=28", "06-Merge Sort (1).pdf#page=29", "06-Merge Sort (1).pdf#page=30", "06-Merge Sort (1).pdf#page=39", "07-Quicksort 1.pdf#page=21"]
---

# Metodo di sostituzione

## Definizione

> 📄 Fonte: [[06-Merge Sort (1).pdf#page=28]]

Il metodo di sostituzione per risolvere una [[equazioni-di-ricorrenza|ricorrenza]] consiste di due passi:
1. **ipotizzare la forma della soluzione**;
2. **verificarla tramite principio di induzione**.

Può essere usato per derivare sia **limiti superiori** che **limiti inferiori** su una ricorrenza.

È il primo dei tre metodi della lezione 06, insieme al [[metodo-albero-di-ricorrenza]] e al [[teorema-dell-esperto]] ([[06-Merge Sort (1).pdf#page=27]]).

> 🧩 Spiegazione mia — cosa si dimostra davvero. Per provare $T(n) = O(g(n))$ si fissa una costante $c > 0$ e si dimostra per induzione su $n$ che $T(n) \le c\, g(n)$ per ogni $n \ge n_0$. L'ipotesi induttiva si applica ai termini $T(\cdot)$ sul lato destro della ricorrenza, che hanno argomento più piccolo. Alla fine si deve ottenere **esattamente** $\le c\, g(n)$ con la **stessa** $c$: concludere «$\le c\,g(n) + n$, quindi $O(g(n))$» non è valido, perché la costante crescerebbe a ogni passo dell'induzione.

## Formule

> 🧮 Formula chiave — schema per un limite superiore:
$$
\exists\, c > 0,\ \exists\, n_0:\quad \underbrace{T(k) \le c\,g(k)\ \ \forall k < n}_{\text{ipotesi induttiva}} \ \Longrightarrow\ T(n) \le c\,g(n), \qquad \text{più i casi base } n_0 \le n < n_1
$$
Simboli: $T(n)$ = soluzione della ricorrenza; $g(n)$ = forma ipotizzata (es. $n\lg n$); $c$ = costante da determinare; $n_0$ = da dove deve valere la disuguaglianza ([[notazione-asintotica]]); i casi base sono i valori di $n$ su cui l'induzione si appoggia.

## Derivazioni

### Derivazione — $T(n) = 2T(\lfloor n/2 \rfloor) + n$ è $O(n \lg n)$
**Fonte:** [[06-Merge Sort (1).pdf#page=28]], [[06-Merge Sort (1).pdf#page=29]]
**Si parte da:** la ricorrenza $T(n) = 2T(\lfloor n/2 \rfloor) + n$ con $T(1) = 1$ («consideriamo $T(1) = 1$ vera ai fini della verifica»). Si suppone che la soluzione sia $T(n) = O(n \lg n)$: occorre provare che $T(n) \le cn\lg n$ per una data costante $c$ e per $n$ sufficientemente grande.

**Passo induttivo** (assumiamo vero per $\lfloor n/2 \rfloor$, dimostriamo per $n$) — la catena è quella della slide, i commenti a destra sono miei (🧩):

$$
\begin{aligned}
T(n) &= 2T(\lfloor n/2 \rfloor) + n && \text{ricorrenza} \\
     &\le 2\big(c\lfloor n/2 \rfloor \lg(\lfloor n/2 \rfloor)\big) + n && \text{ipotesi induttiva su } \lfloor n/2 \rfloor < n \\
     &\le cn\lg(n/2) + n && 2\lfloor n/2 \rfloor \le n \text{ e } \lg \text{ crescente} \\
     &= cn\lg n - cn\lg 2 + n && \lg(a/b) = \lg a - \lg b \\
     &= cn\lg n - cn + n = cn\lg n - (c-1)n && \lg 2 = 1 \\
     &\le cn\lg n && \text{se } c \ge 1 \text{: il termine } (c-1)n \ge 0 \text{ si toglie}
\end{aligned}
$$

**Caso base** ([[06-Merge Sort (1).pdf#page=29]]):
- Per $n = 1$: $T(1) \le c \lg 1 = 0$, ma il tempo di esecuzione non può essere $\le 0$.
- Si utilizzano $T(2)$ e $T(3)$: $T(n) \le cn\lg n$ deve valere solo per $n \ge n_0$.
- Occorre mostrare che $T(2) = 4 \le c\,2\lg 2$ e $T(3) = 5 \le c\,3\lg 3$.
- È sufficiente che $c \ge 2$ per verificare i casi base.

![[06-merge-sort-p29-sostituzione-passi.png]]

> 🧩 Derivazione mia — i valori numerici:
$$
\begin{aligned}
T(2) &= 2T(\lfloor 2/2 \rfloor) + 2 = 2T(1) + 2 = 4, && 4 \le 2c \lg 2 = 2c \iff c \ge 2 \\
T(3) &= 2T(\lfloor 3/2 \rfloor) + 3 = 2T(1) + 3 = 5, && 5 \le 3c\lg 3 \approx 4.75\,c \iff c \ge 1.05 \\
c &= 2,\ n_0 = 2 && \text{soddisfa base } (c \ge 2) \text{ e passo } (c \ge 1)
\end{aligned}
$$
> **Sanity check** ([[divide_et_impera.py]]): calcolando $T(n)$ esattamente, $\max_{2 \le n \le 10^5} T(n)/(n\lg n) = 2.0000$, raggiunto in $n = 2$: con $c = 2$ la disuguaglianza vale ovunque e $c$ non si può abbassare.

### Perché due casi base
> 📄 Fonte: [[06-Merge Sort (1).pdf#page=30]]

![[06-merge-sort-p30-due-casi-base.png]]
*Due alberi: da 2 discendono 4, 5, poi 8–11, poi 16–23; da 3 discendono 6, 7, poi 12–15, poi 24–31. Ogni freccia va da $\lfloor n/2 \rfloor$ a $n$. ([[06-Merge Sort (1).pdf#page=30]])*

> 🧩 Spiegazione mia della figura. Il passo induttivo per $n$ usa il valore in $\lfloor n/2 \rfloor$. Partendo da un qualsiasi $n \ge 4$ e dimezzando ripetutamente si arriva a 2 oppure a 3, **mai** a 1: per $n \ge 4$ vale $\lfloor n/2 \rfloor \ge 2$. 4 e 5 scendono a 2, 6 e 7 scendono a 3, da 8 a 11 scendono a 4 o 5 e poi a 2, e così via. Quindi i due casi base $n = 2$ e $n = 3$ coprono **tutti** gli $n \ge 2$, e $n = 1$ (dove la disuguaglianza è falsa) non serve. Con un solo caso base, ad esempio $n = 2$, metà dei numeri (quelli dell'albero di 3) resterebbero scoperti.

### Altri usi nelle lezioni

- **Verifica di una soluzione di tentativo** dal [[metodo-albero-di-ricorrenza]]: $T(n) = 3T(\lfloor n/4 \rfloor) + \Theta(n^2) \le dn^2$ con $d \ge \frac{16}{13}c$ e $d \ge T(1)$ ([[06-Merge Sort (1).pdf#page=39]]). La catena completa è in [[metodo-albero-di-ricorrenza]].
- **Caso peggiore di quicksort:** $T(n) = \max_{0 \le q \le n-1}(T(q) + T(n-q-1)) + \Theta(n) \le cn^2$ ([[07-Quicksort 1.pdf#page=21]]). Qui l'ipotesi induttiva va applicata a **tutti** i $k < n$ (induzione forte), perché $q$ può essere qualsiasi. Passaggi in [[quicksort]] § Dimostrazione del caso peggiore.
- **Limiti inferiori:** stessa tecnica con $\ge$; ad esempio il caso peggiore di quicksort è anche $\Omega(n^2)$ ([[07-Quicksort 1.pdf#page=22]]).

## Spiegazione

Il metodo non trova la soluzione: la **verifica**. Serve un'ipotesi buona, che si ottiene dall'esperienza, da una ricorrenza simile già risolta o dal [[metodo-albero-di-ricorrenza]] ([[06-Merge Sort (1).pdf#page=31]]: l'albero genera «buone soluzioni di tentativo», da verificare con la sostituzione se si sono fatte ipotesi semplificative).

> 🧩 Trappole tipiche (dalle derivazioni sopra):
> - chiudere l'induzione con una costante diversa da quella dell'ipotesi;
> - dimenticare i casi base, o sceglierli dove la disuguaglianza è falsa ($n = 1$ con $n\lg n$);
> - applicare l'ipotesi induttiva a un argomento che non è nel dominio dell'induzione ($\lfloor n/2 \rfloor = 1$ quando il primo caso base è 2).

## Perché importa

> 🎯 Esame: verificare per sostituzione una soluzione data, esibendo $c$ e $n_0$; spiegare perché nell'esempio servono i casi base $T(2)$ e $T(3)$.

## Connessioni

- [[correttezza-per-induzione]] — stessa struttura: caso base + passo induttivo
- [[metodo-albero-di-ricorrenza]] — fornisce l'ipotesi da verificare
- [[teorema-dell-esperto]] — risolve direttamente le ricorrenze $aT(n/b) + f(n)$ che rientrano nei tre casi
- [[notazione-asintotica]] — la definizione di $O$ con $c$ e $n_0$ è quella che si dimostra
- [[risoluzione-ricorrenze]] — esercizi

## Fonti

- [[lezione-06-merge-sort]], [[lezione-07-quicksort]]
- [[06-Merge Sort (1).pdf#page=28]]–[[06-Merge Sort (1).pdf#page=30]], [[06-Merge Sort (1).pdf#page=39]], [[07-Quicksort 1.pdf#page=21]]

_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf e 07-Quicksort.pdf_
_Aggiornato: 2026-10-10 — nuova versione delle slide (06-Merge Sort (1).pdf): numeri di pagina aggiornati_
_Aggiornato: 2026-10-14 — link ripuntati alla versione aggiornata delle slide 07-Quicksort 1.pdf_

<!-- nav:inizio -->
---
**Lezione 06 · pagina 6 di 8** · ← [[massimo-sottoarray|Problema del massimo sottoarray]] · [[lezioni|Indice]] · [[metodo-albero-di-ricorrenza|Metodo dell'albero di ricorrenza]] →
<!-- nav:fine -->
