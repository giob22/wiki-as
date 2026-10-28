---
tipo: concetto
importanza_esame: media
prerequisiti: ["notazione-asintotica"]
fonti_pdf: ["02-Notazione asintotica.pdf#page=24", "02-Notazione asintotica.pdf#page=25", "02-Notazione asintotica.pdf#page=26"]
---

# Regole di calcolo con la notazione asintotica

## Definizione

Regole per combinare stime asintotiche senza ripartire ogni volta dalle definizioni di [[notazione-asintotica]].

## Formule

> 📄 Fonte: [[02-Notazione asintotica.pdf#page=24]] — *Big Oh Addition/Subtraction*

Supponiamo $f(n) = O(n^2)$ e $g(n) = O(n^2)$.
- **Somma:** $g'(n) = f(n) + g(n)$. Sommando le costanti dei limiti si ottiene $g'(n) = O(n^2)$.
- **Differenza:** $g''(n) = f(n) - |g(n)|$. Poiché le costanti non si cancellano necessariamente, $g''(n) = O(n^2)$.
- Non sappiamo **nulla sui limiti inferiori** di $g'$ e $g''$, perché non sappiamo nulla sui limiti inferiori di $f$ e $g$.

Esempio della slide: $f(n) = 5n^2$ e $g(n) = 150n^2$ **contro** $f(n) = 500n^2$ e $g(n) = 150n^2$.

> 📄 Fonte: [[02-Notazione asintotica.pdf#page=25]] — *Multiplication by Constant*

La moltiplicazione per una costante non cambia l'andamento asintotico:
$$
O(c \cdot f(n)) \to O(f(n)), \qquad \Omega(c \cdot f(n)) \to \Omega(f(n)), \qquad \Theta(c \cdot f(n)) \to \Theta(f(n))
$$
La «vecchia costante» $C$ del Big Oh diventa $c \cdot C$.

> 📄 Fonte: [[02-Notazione asintotica.pdf#page=26]] — *Multiplication by Function*

Quando entrambe le funzioni di un prodotto sono crescenti, **contano entrambe**:
$$
O(f(n)) \cdot O(g(n)) \to O(f(n) \cdot g(n)), \quad \Omega(f(n)) \cdot \Omega(g(n)) \to \Omega(f(n) \cdot g(n)), \quad \Theta(f(n)) \cdot \Theta(g(n)) \to \Theta(f(n) \cdot g(n))
$$

## Derivazioni

### Derivazione — somma e differenza
**Fonte:** [[02-Notazione asintotica.pdf#page=24]]
**Si parte da:** $f(n) \le c_f\, n^2$ per $n \ge n_f$ e $g(n) \le c_g\, n^2$ per $n \ge n_g$ ([[notazione-asintotica]], p. 18)

$$
\begin{aligned}
g'(n) = f(n) + g(n) &\le c_f n^2 + c_g n^2 && n \ge \max(n_f, n_g) \\
&= (c_f + c_g)\, n^2 && \text{«adding the bounding constants»} \\[4pt]
g''(n) = f(n) - |g(n)| &\le f(n) && |g(n)| \ge 0 \\
&\le c_f\, n^2 && \text{limite di } f
\end{aligned}
$$

**Esempio numerico** (🧩 derivazione mia sui dati della slide):
- $f = 5n^2$, $g = 150n^2$: $g'' = 5n^2 - 150n^2 = -145n^2$ → è $O(n^2)$ (anzi è negativa) ma **non** è $\Omega(n^2)$: il limite inferiore è sparito.
- $f = 500n^2$, $g = 150n^2$: $g'' = 350n^2 = \Theta(n^2)$.
Stessi limiti superiori su $f$ e $g$, comportamento opposto sul limite inferiore: ecco perché «we know nothing about the lower bounds».

### Derivazione — costante e prodotto
> 🧩 Derivazione mia:
- **Costante:** se $h(n) \le C \cdot (c f(n))$ allora $h(n) \le (cC)\, f(n)$: stessa funzione di riferimento, costante $cC$ (è la frase in rosso di p. 25).
- **Prodotto ($O$):** se $f_1 \le C_1 f$ per $n \ge n_1$ e $g_1 \le C_2 g$ per $n \ge n_2$, con tutte le funzioni non negative, allora per $n \ge \max(n_1, n_2)$: $f_1 g_1 \le (C_1 C_2)\, f g$. Per $\Omega$ si rovesciano le disuguaglianze; $\Theta$ segue dai due.
- L'ipotesi di non negatività (qui: numeri di passi) è ciò che rende lecito moltiplicare membro a membro.

## Spiegazione

Uso tipico: un ciclo che esegue $O(n)$ iterazioni, ciascuna di costo $O(n)$, costa $O(n)\cdot O(n) = O(n^2)$ (es. [[nearest-neighbor]]); due fasi in sequenza di costo $O(n^2)$ e $O(n)$ costano complessivamente $O(n^2)$ (somma).

## Perché importa

Permette di analizzare algoritmi componendo i costi dei pezzi.

> 🎯 Esame: attenzione alla differenza — il limite superiore sopravvive, quello inferiore no.

## Connessioni

- [[notazione-asintotica]] — definizioni
- [[dominanza-asintotica]] — nella somma sopravvive il termine dominante
- [[dimostrazioni-notazione-asintotica]] — esercizi

## Fonti

- [[lezione-02-notazione-asintotica]]
- [[02-Notazione asintotica.pdf#page=24]], [[02-Notazione asintotica.pdf#page=25]], [[02-Notazione asintotica.pdf#page=26]]

_Aggiornato: 2026-09-26 — ingest 02-Notazione asintotica.pdf_

<!-- nav:inizio -->
---
**Lezione 02 · pagina 7 di 8** · ← [[dimostrazioni-notazione-asintotica|Dimostrare (o confutare) f = O/Ω/Θ(g)]] · [[lezioni|Indice]] · [[dominanza-asintotica|Dominanza asintotica, little-o e crescita delle funzioni]] →
<!-- nav:fine -->
