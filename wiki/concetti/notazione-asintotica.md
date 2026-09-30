---
tipo: concetto
importanza_esame: alta
prerequisiti: ["tempo-di-esecuzione", "casi-di-complessita"]
fonti_pdf: ["02-Notazione asintotica.pdf#page=15", "02-Notazione asintotica.pdf#page=16", "02-Notazione asintotica.pdf#page=17", "02-Notazione asintotica.pdf#page=18", "02-Notazione asintotica.pdf#page=21", "02-Notazione asintotica.pdf#page=22", "02-Notazione asintotica.pdf#page=23", "02-Notazione asintotica.pdf#page=27"]
---

# Notazione asintotica: $O$, $\Omega$, $\Theta$

## Definizione

> 📄 Fonte: [[02-Notazione asintotica.pdf#page=15]] — *Exact Analysis is Hard!*

I casi migliore, peggiore e medio sono difficili da trattare perché i dettagli **precisi** delle funzioni sono molto complicati. È più facile parlare di **limiti superiori e inferiori** della funzione. Le notazioni asintotiche ($O$, $\Theta$, $\Omega$) sono il meglio che si possa praticamente fare con le funzioni di complessità.

![[02-notazione-asintotica-p15-upper-lower-bound.png]]
*Una $f(n)$ irregolare, stretta da oltre $n_0$ tra un limite superiore (blu) e uno inferiore (rosso). ([[02-Notazione asintotica.pdf#page=15]])*

> 📄 Fonte: [[02-Notazione asintotica.pdf#page=16]] — *Names of Bounding Functions*

- $f(n) = O(g(n))$ significa che $C \times g(n)$ è un **limite superiore** (*upper bound*) di $f(n)$.
- $f(n) = \Omega(g(n))$ significa che $C \times g(n)$ è un **limite inferiore** (*lower bound*) di $f(n)$.
- $f(n) = \Theta(g(n))$ significa che $C_1 \times g(n)$ è un limite superiore e $C_2 \times g(n)$ un limite inferiore di $f(n)$.

$C$, $C_1$, $C_2$ sono costanti **indipendenti da $n$**.

> 📄 Fonte: [[02-Notazione asintotica.pdf#page=17]]

Le definizioni implicano una costante $n_0$ **oltre la quale** sono soddisfatte: non interessano i piccoli valori di $n$.

![[02-notazione-asintotica-p17-o-omega-theta-grafici.png]]
*(a) $f(n) = O(g(n))$: da $n_0$ in poi $f$ sta sotto $c\,g$; (b) $f(n) = \Omega(g(n))$: da $n_0$ in poi sta sopra; (c) $f(n) = \Theta(g(n))$: tra $c_2\,g$ e $c_1\,g$. ([[02-Notazione asintotica.pdf#page=17]])*

## Formule

> 📄 Fonte: [[02-Notazione asintotica.pdf#page=18]] — *Formal Definitions*

> 🧮 Formula chiave:
- $f(n) = O(g(n))$ se esistono costanti positive $n_0$ e $c$ tali che, a destra di $n_0$, il valore di $f(n)$ sta sempre **su o sotto** $c \cdot g(n)$:
$$ \exists\, c > 0,\ n_0 > 0 :\ \ f(n) \le c\,g(n)\quad \forall n \ge n_0 $$
- $f(n) = \Omega(g(n))$ se esistono costanti positive $n_0$ e $c$ tali che, a destra di $n_0$, $f(n)$ sta sempre **su o sopra** $c \cdot g(n)$:
$$ \exists\, c > 0,\ n_0 > 0 :\ \ f(n) \ge c\,g(n)\quad \forall n \ge n_0 $$
- $f(n) = \Theta(g(n))$ se esistono costanti positive $n_0$, $c_1$, $c_2$ tali che, a destra di $n_0$, $f(n)$ sta sempre **tra** $c_1 \cdot g(n)$ e $c_2 \cdot g(n)$ inclusi:
$$ \exists\, c_1, c_2 > 0,\ n_0 > 0 :\ \ c_1\,g(n) \le f(n) \le c_2\,g(n)\quad \forall n \ge n_0 $$

Simboli: $f, g$ = funzioni da interi positivi a reali (qui: numeri di passi); $n$ = dimensione dell'ingresso; $c, c_1, c_2$ = costanti moltiplicative; $n_0$ = soglia.

> ⚠️ Contraddizione (solo di nomi): nella slide p. 16 $C_1$ è la costante del limite **superiore** e $C_2$ dell'inferiore; nella p. 18 $c_1$ è quella del limite **inferiore** e $c_2$ del superiore. La figura (c) di p. 17 segue la convenzione di p. 16 ($c_1 g$ sopra). Nel wiki si usa la convenzione di p. 18.

**NOTA** ([[02-Notazione asintotica.pdf#page=21]]): l'uguaglianza va pensata come **appartenenza a un insieme di funzioni**: $f(n) = O(g(n))$ significa $f(n) \in O(g(n))$, dove $O(g(n))$ è l'insieme di tutte le funzioni limitate superiormente da un multiplo di $g$.

> 📄 Fonte: [[02-Notazione asintotica.pdf#page=27]] — *Notazioni asintotiche*

Quando una notazione asintotica compare in un'**equazione**, va interpretata come una **funzione ignota che non ci interessa specificare**. Esempio: $2n^2 + 3n + 1 = 2n^2 + \Theta(n)$ equivale a $2n^2 + 3n + 1 = 2n^2 + f(n)$, dove $f(n)$ è una qualunque funzione nell'insieme $\Theta(n)$ (qui $f(n) = 3n + 1$).

**Proprietà** ([[02-Notazione asintotica.pdf#page=27]]):

| Proprietà | Enunciato | Vale per |
|-----------|-----------|----------|
| Transitiva | $f(n) = O(g(n))$ e $g(n) = O(h(n)) \Rightarrow f(n) = O(h(n))$ | $O$, $\Theta$, $\Omega$ |
| Riflessiva | $f(n) = O(f(n))$ | $O$, $\Theta$, $\Omega$ |
| Simmetrica | $f(n) = \Theta(g(n)) \Leftrightarrow g(n) = \Theta(f(n))$ | $\Theta$ |
| «Anti-simmetrica» | $f(n) = O(g(n)) \Leftrightarrow g(n) = \Omega(f(n))$ | $O$/$\Omega$ |

![[02-notazione-asintotica-p27-proprieta-notazioni.png]]

> 📚 Fonte esterna: nel Cormen (3ª ed., § 3.1) l'ultima proprietà si chiama *simmetria trasposta*. Il nome «anti-simmetrica» della slide non va confuso con l'antisimmetria delle relazioni d'ordine.

## Derivazioni

### Derivazione — le proprietà di p. 27
**Fonte:** [[02-Notazione asintotica.pdf#page=27]] (enunciate senza dimostrazione)

> 🧩 Derivazione mia:
- **Transitiva ($O$):** $f \le c_1 g$ per $n \ge n_1$ e $g \le c_2 h$ per $n \ge n_2$. Per $n \ge \max(n_1, n_2)$: $f \le c_1 g \le c_1 c_2 h$ → costante $c_1 c_2$, soglia $\max(n_1,n_2)$. Identica per $\Omega$ con le disuguaglianze rovesciate; per $\Theta$ si applicano entrambe.
- **Riflessiva:** $f(n) \le 1\cdot f(n)$ e $f(n) \ge 1 \cdot f(n)$ per ogni $n$: $c = 1$, $n_0 = 1$.
- **Simmetrica ($\Theta$):** da $c_1 g \le f \le c_2 g$ si ricava $\frac{1}{c_2} f \le g \le \frac{1}{c_1} f$: costanti $1/c_2$ e $1/c_1$, positive.
- **Trasposta:** $f \le c\,g \iff g \ge \frac1c f$, stessa soglia $n_0$.

### Derivazione — esempi di $O$ ([[02-Notazione asintotica.pdf#page=21]])
Sia $f(n) = 3n^2 - 100n + 6$.

1. **$f(n) = O(n^2)$** perché $3n^2 > 3n^2 - 100n + 6$.
$$
3n^2 - 100n + 6 \le 3n^2 \iff -100n + 6 \le 0 \iff n \ge 0.06 \qquad \Rightarrow\ c = 3,\ n_0 = 1
$$
2. **$f(n) = O(n^3)$** perché $0.01\,n^3 > 3n^2 - 100n + 6$.
$$
\begin{aligned}
0.01\,n^3 &\ge 3n^2 \iff n \ge 300 && \text{divido per } 0.01\,n^2 > 0 \\
3n^2 &> 3n^2 - 100n + 6 \ \ \forall n \ge 1 && \text{punto 1} \\
\Rightarrow\ c &= 0.01,\ n_0 = 300
\end{aligned}
$$
3. **$f(n) \ne O(n)$** perché $c \cdot n < 3n^2$ quando $n > c$. Versione precisa:
$$
\begin{aligned}
&\text{suppongo per assurdo } 3n^2 - 100n + 6 \le c\,n \quad \forall n \ge n_0 \\
&\iff 3n^2 - (100 + c)\,n + 6 \le 0 && \text{porto tutto a sinistra} \\
&\text{ma per } n > \tfrac{100 + c}{3}:\ 3n^2 - (100+c)\,n = n\,\big(3n - (100+c)\big) > 0 && \text{il primo membro è } > 6 > 0
\end{aligned}
$$
quindi nessuna coppia $(c, n_0)$ funziona. La slide scrive «$c \cdot n < 3n^2$ when $n > c$», che trascura i termini $-100n + 6$: il ragionamento è lo stesso.

![[02-notazione-asintotica-p21-big-oh-esempio-grafico.png]]
*Slide originale con il grafico delle tre funzioni. ([[02-Notazione asintotica.pdf#page=21]])*

![[grafico-big-oh-esempio.svg]]
> 🧩 Grafico generato da me ([[genera_grafici_as.py]]), riproduce [[02-Notazione asintotica.pdf#page=21]]: $3n^2$ sta sempre sopra $f$; $0.01n^3$ supera $f$ poco dopo $n \approx 262$ e supera anche $3n^2$ da $n = 300$, la soglia $n_0$ scelta sopra.

### Derivazione — esempi di $\Omega$ ([[02-Notazione asintotica.pdf#page=22]])
1. **$f(n) = \Omega(n^2)$** perché $2.99\,n^2 < 3n^2 - 100n + 6$.
$$
\begin{aligned}
2.99\,n^2 \le 3n^2 - 100n + 6 &\iff 0.01\,n^2 - 100\,n + 6 \ge 0 \\
&\iff n \ge \frac{100 + \sqrt{100^2 - 4(0.01)(6)}}{2(0.01)} \approx 9999.94 && \text{radice maggiore} \\
&\Rightarrow\ c = 2.99,\ n_0 = 10^4
\end{aligned}
$$
2. **$f(n) \ne \Omega(n^3)$** perché $3n^2 - 100n + 6 < n^3$. Versione precisa: per ogni $c > 0$, per $n \ge 1$ vale $f(n) < 3n^2 + 6 \le 9n^2$, e $9n^2 < c\,n^3$ appena $n > 9/c$: nessuna costante $c$ può stare sotto $f$ per sempre.
3. **$f(n) = \Omega(n)$** perché $10^{10^{10}}\, n < 3n^2 - 100n + 6$: la costante può essere enorme, conta solo che esista. Con $K = 10^{10^{10}}$: $3n^2 - (100 + K)n + 6 > 0$ per $n > (100 + K)/3$, che è la soglia $n_0$.

### Derivazione — esempi di $\Theta$ ([[02-Notazione asintotica.pdf#page=23]])
- $f(n) = \Theta(n^2)$ perché vale sia $O$ sia $\Omega$: con $c_1 = 2.99$, $c_2 = 3$, $n_0 = 10^4$ (dai punti precedenti; per $n \ge 10^4$ entrambe le disuguaglianze valgono).
- $f(n) \ne \Theta(n^3)$ perché vale **solo** $O$.
- $f(n) \ne \Theta(n)$ perché vale **solo** $\Omega$.

![[grafico-theta-rapporto.svg]]
> 🧩 Grafico generato da me: il rapporto $f(n)/n^2 = 3 - 100/n + 6/n^2$ tende a 3 dal basso; da $n_0 = 10^4$ resta nella fascia $[2.99,\ 3]$, che è esattamente $\Theta(n^2)$ con $c_1 = 2.99$, $c_2 = 3$ ([[02-Notazione asintotica.pdf#page=22]]).

**Sanity check:** $f(10^4) = 3\cdot10^8 - 10^6 + 6 = 299\,000\,006 \ge 2.99\cdot 10^8 = 299\,000\,000$ ✓ (di poco, come atteso alla soglia).

## Spiegazione

$O$ è un «≤» asintotico, $\Omega$ un «≥», $\Theta$ un «=» tra ordini di crescita. Con i [[casi-di-complessita]]: «l'algoritmo è $O(n^2)$» è un'affermazione sul caso peggiore che vale per tutti gli input; «è $\Omega(n)$» sul caso migliore vale anch'essa per tutti gli input.

## Perché importa

È il linguaggio con cui si esprime ogni risultato di complessità del corso.

> 🎯 Esame: dimostrare $f = O/\Omega/\Theta(g)$ esibendo $c$ e $n_0$; dimostrare $f \ne O(g)$ per assurdo.

## Connessioni

- [[regole-di-calcolo-asintotico]] — somma, differenza, prodotto
- [[dominanza-asintotica]] — il confronto stretto ($o$) e il test del limite
- [[dimostrazioni-notazione-asintotica]] — esercizi svolti

## Fonti

- [[lezione-02-notazione-asintotica]]
- [[02-Notazione asintotica.pdf#page=14]] (intestazione «The Big Oh Notation»), [[02-Notazione asintotica.pdf#page=15]]–[[02-Notazione asintotica.pdf#page=18]], [[02-Notazione asintotica.pdf#page=20]] (intestazione «Working with the Big Oh»), [[02-Notazione asintotica.pdf#page=21]]–[[02-Notazione asintotica.pdf#page=23]], [[02-Notazione asintotica.pdf#page=27]]

_Aggiornato: 2026-09-26 — ingest 02-Notazione asintotica.pdf_
