---
tipo: esercizio
argomento: "notazione asintotica O, Ω, Θ, o"
difficoltà: media
---

# Dimostrare (o confutare) $f = O/\Omega/\Theta(g)$

## Metodo

- **Per dimostrare $f = O(g)$:** trovare $c > 0$ e $n_0$ con $f(n) \le c\,g(n)$ per ogni $n \ge n_0$. Tecnica: maggiorare i termini negativi con 0 e i termini positivi di ordine inferiore con multipli di $g$.
- **Per dimostrare $f = \Omega(g)$:** trovare $c > 0$ e $n_0$ con $f(n) \ge c\,g(n)$; scegliere $c$ un po' più piccolo del coefficiente dominante e risolvere la disequazione per trovare $n_0$.
- **Per $\Theta$:** entrambe (con le stesse $n_0$, prendendo il massimo).
- **Per confutare $f = O(g)$:** per assurdo, supporre $f \le c\,g$ da $n_0$ in poi e mostrare che per $n$ abbastanza grande (dipendente da $c$) la disuguaglianza fallisce.
- **Scorciatoia col limite** ([[02-Notazione asintotica.pdf#page=34]]): $\lim g/f = 0 \Rightarrow g = o(f)$ (quindi $g = O(f)$, $g \ne \Omega(f)$); limite finito positivo $\Rightarrow \Theta$.

## Strumenti usati

- [[notazione-asintotica]] — definizioni formali ([[02-Notazione asintotica.pdf#page=18]])
- [[regole-di-calcolo-asintotico]], [[dominanza-asintotica]]

## Casi svolti

**Traccia comune:** $f(n) = 3n^2 - 100n + 6$ ([[02-Notazione asintotica.pdf#page=21]]–[[02-Notazione asintotica.pdf#page=23]]).

| Affermazione | Giustificazione della slide | Costanti (🧩 mie) |
|--------------|-----------------------------|-------------------|
| $f = O(n^2)$ | $3n^2 > f(n)$ | $c = 3$, $n_0 = 1$ |
| $f = O(n^3)$ | $0.01n^3 > f(n)$ | $c = 0.01$, $n_0 = 300$ |
| $f \ne O(n)$ | $c\,n < 3n^2$ quando $n > c$ | assurdo per $n > (100 + c)/3$ |
| $f = \Omega(n^2)$ | $2.99n^2 < f(n)$ | $c = 2.99$, $n_0 = 10^4$ |
| $f \ne \Omega(n^3)$ | $f(n) < n^3$ | per ogni $c$, fallisce per $n > 9/c$ |
| $f = \Omega(n)$ | $10^{10^{10}} n < f(n)$ | $c = 10^{10^{10}}$, $n_0 > (100 + c)/3$ |
| $f = \Theta(n^2)$ | $O$ e $\Omega$ | $c_1 = 2.99$, $c_2 = 3$, $n_0 = 10^4$ |
| $f \ne \Theta(n^3)$ | solo $O$ | — |
| $f \ne \Theta(n)$ | solo $\Omega$ | — |

Svolgimento completo di ogni riga (disequazioni e radici) in [[notazione-asintotica]] § Derivazioni.

### Caso — $\Omega(n^2)$ passo per passo
$$
\begin{aligned}
2.99\,n^2 &\le 3n^2 - 100n + 6 \\
0 &\le 0.01\,n^2 - 100\,n + 6 && \text{sottraggo } 2.99n^2 \\
n &\ge \frac{100 + \sqrt{10^4 - 0.24}}{0.02} \approx 9999.94 && \text{formula risolutiva, radice maggiore}
\end{aligned}
$$
**Risultato:** $c = 2.99$, $n_0 = 10\,000$. **Sanity check:** $f(10^4) = 299\,000\,006 \ge 2.99\cdot10^8$ ✓; $f(9999) = 299\,940\,003 - 999\,900 + 6 = 298\,940\,109$ contro $2.99 \cdot 9999^2 = 298\,940\,202.99$: ✗, quindi $n_0 = 10^4$ è davvero la soglia minima intera.

### Caso — somma e differenza ([[02-Notazione asintotica.pdf#page=24]])
$f = O(n^2)$, $g = O(n^2)$ ⇒ $f + g = O(n^2)$ e $f - |g| = O(n^2)$; nulla sui limiti inferiori. Esempi: $5n^2 - 150n^2 = -145n^2$ (non $\Omega(n^2)$) contro $500n^2 - 150n^2 = 350n^2 = \Theta(n^2)$ → [[regole-di-calcolo-asintotico]].

### Caso — dominanza tra potenze ([[02-Notazione asintotica.pdf#page=35]])
$n^3$ contro $n^2$: $\lim n^2/n^3 = \lim 1/n = 0$ ⇒ $n^2 = o(n^3)$, $n^3$ domina. $n^2 + 5n$ contro $n^2$: $\lim n^2/(n^2 + 5n) = 1$ ⇒ nessuna dominanza, stesso ordine $\Theta(n^2)$.

## Trappole

- Le costanti devono essere **indipendenti da $n$**: «$c = n$» non è ammesso.
- $O$ non è «uguale»: $f = O(n^3)$ è vero anche se $f$ è quadratica.
- Confondere $c_1$/$c_2$ tra le slide p. 16 e p. 18 ([[notazione-asintotica]]).
- Nella differenza il limite inferiore si perde.

_Aggiornato: 2026-09-26 — ingest 02-Notazione asintotica.pdf_

<!-- nav:inizio -->
---
**Lezione 02 · pagina 6 di 8** · ← [[notazione-asintotica|Notazione asintotica: O, Ω, Θ]] · [[lezioni|Indice]] · [[regole-di-calcolo-asintotico|Regole di calcolo con la notazione asintotica]] →
<!-- nav:fine -->
