---
tipo: concetto
importanza_esame: alta
prerequisiti: ["algoritmo-e-problema"]
fonti_pdf: ["01-Introduzione.pdf#page=9", "03-Analisi di algoritmi.pdf#page=16", "03-Analisi di algoritmi.pdf#page=18"]
---

# Correttezza parziale e correttezza totale

## Definizione · 01-Introduzione.pdf [[01-Introduzione.pdf#page=9|p. 9]] · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=16|p. 16]]

Un algoritmo è **corretto** se, **per ogni istanza** del problema, **termina** fornendo l'insieme corretto di valori in uscita. Un algoritmo incorretto, su alcune istanze, può **non terminare** oppure terminare con un'**uscita sbagliata**.

La definizione contiene quindi due richieste distinte: (1) l'uscita è giusta, (2) l'algoritmo si ferma. Separandole si ottengono due livelli di correttezza.

- L'invariante di ciclo dimostra la **correttezza parziale**.
- Per la **correttezza totale** serve anche la **terminazione**: di solito si introduce una **funzione variante** (misura intera $\ge 0$) che diminuisce a ogni iterazione.

> 🧩 Definizioni esplicite (mie, ricavate dalle due slide):
> - **Correttezza parziale:** *se* l'algoritmo termina, allora l'uscita è corretta. Non garantisce che termini.
> - **Correttezza totale:** correttezza parziale **e** terminazione su ogni istanza. Coincide con la definizione di «algoritmo corretto» di p. 9.

## Formule · [[03-Analisi di algoritmi.pdf#page=16|p. 16]], [[03-Analisi di algoritmi.pdf#page=18|p. 18]]

> 🧩 Formalizzazione mia. Le slide usano le nozioni di pre-condizione e post-condizione; qui le scrivo in simboli.

Siano $P$ la **pre-condizione** (cosa vale sull'input, es. «$A$ è un array di $n$ numeri») e $Q$ la **post-condizione** (cosa deve valere sull'output, es. «$A$ contiene gli stessi elementi, in ordine crescente»).

$$
\begin{aligned}
&\textbf{parziale:} && \forall\, x \text{ con } P(x):\quad \text{se l'algoritmo su } x \text{ termina, allora l'output soddisfa } Q \\
&\textbf{totale:} && \forall\, x \text{ con } P(x):\quad \text{l'algoritmo su } x \text{ termina } \textbf{e} \text{ l'output soddisfa } Q
\end{aligned}
$$

$$ \text{correttezza totale} = \text{correttezza parziale} + \text{terminazione} $$

## Spiegazione

### Perché distinguerle · [[03-Analisi di algoritmi.pdf#page=16|p. 16]], [[03-Analisi di algoritmi.pdf#page=17|17]]
Un algoritmo che va in **ciclo infinito** su un'istanza non restituisce mai un'uscita, quindi non ne restituisce mai una sbagliata: rispetto a quell'istanza è parzialmente corretto «a costo zero». La correttezza parziale da sola non basta; per questo la slide chiede esplicitamente anche la terminazione.

> 🧩 Esempio mio di algoritmo **parzialmente corretto ma non totalmente**. Si vuole sommare $1 + 2 + \dots + n$, con pre-condizione $P$: «$n$ è un intero» (quindi anche negativo):
>
> ```
> SOMMA-FINO-A(n)
> 1  s ← 0
> 2  i ← 1
> 3  while i ≠ n + 1
> 4      s ← s + i
> 5      i ← i + 1
> 6  return s
> ```
>
> - Se $n \ge 0$, $i$ arriva esattamente a $n + 1$ e il risultato è $1 + \dots + n$: **quando termina, è giusto** → correttezza parziale ✓.
> - Se $n = -3$, $i$ vale 1, 2, 3, … e non vale mai $n + 1 = -2$: il ciclo **non termina** → correttezza totale ✗.
> - Con la pre-condizione più forte «$n \ge 0$» (quella di `somma_iterativa`) lo stesso codice diventa totalmente corretto: la variante $v = n + 1 - i$ è $\ge 0$ e cala di 1 a ogni iterazione. La terminazione dipende anche dalla pre-condizione.

### Come si valuta la correttezza · [[03-Analisi di algoritmi.pdf#page=13|p. 13]], [[03-Analisi di algoritmi.pdf#page=15|p. 15]], [[03-Analisi di algoritmi.pdf#page=16|16]], [[03-Analisi di algoritmi.pdf#page=18|p. 18]]

| Obiettivo | Strumento | Cosa dimostra | Slide |
|---|---|---|---|
| dimostrare che è **sbagliato** | un **controesempio** (una sola istanza che fallisce) | che non vale la correttezza (né parziale né totale su quell'istanza) | p. 13–p. 15 |
| algoritmo **iterativo** | **invariante di ciclo** (inizializzazione, conservazione, conclusione) | correttezza **parziale** | p. 16 |
|  | **funzione variante** | **terminazione** → con l'invariante, correttezza **totale** | p. 16 |
| algoritmo **ricorsivo** | **induzione**: casi base + passo induttivo | correttezza **parziale** | p. 18 |
|  | **misura ben fondata** che decresce a ogni chiamata | **terminazione** → correttezza **totale** | p. 18 |

Non trovare controesempi **non** dimostra la correttezza: i test coprono un numero finito di istanze, la correttezza parla di tutte.

### Esempio completo: somma_iterativa · [[03-Analisi di algoritmi.pdf#page=17|p. 17]]

```
funzione somma_iterativa(n)
1  s ← 0
2  per i da 1 a n
3      s ← s + i
4  ritorna s
```

- **Parziale** (invariante: all'inizio dell'iterazione $i$, $s = \sum_{k=1}^{i-1} k$): vale all'inizio ($i = 1$, somma vuota = 0), si conserva ($s + i = \sum_{k=1}^{i} k$), all'uscita ($i = n+1$) dà $s = 1 + \dots + n$. Quindi, **se** il ciclo termina, il risultato è giusto.
- **Terminazione** (variante $v = n - i + 1$): è un intero $\ge 0$, vale $n$ all'inizio e cala di 1 a ogni iterazione; quando arriva a 0 il ciclo esce. Quindi il ciclo **termina sempre**.
- Insieme: correttezza **totale**.

Dimostrazione con tutti i passaggi → [[invariante-di-ciclo]]. Lo stesso schema per insertion sort (con la variante $n - j + 1$ per il `for` e $i$ per il `while`) → [[insertion-sort]] § Correttezza.

### Nel caso ricorsivo: somma_ricorsiva · [[03-Analisi di algoritmi.pdf#page=19|p. 19]]

- **Parziale:** caso base $S(0) = 0$ corretto; passo induttivo: se $S(n-1)$ è corretto, allora $S(n) = n + S(n-1)$ è corretto.
- **Terminazione:** ogni chiamata usa $n - 1 < n$ (misura ben fondata), quindi da $n$ si arriva a 0 in $n$ passi.
- Insieme: correttezza **totale**. La pre-condizione $n \ge 0$ è essenziale: con $n = -1$ la misura non raggiunge mai il caso base e la ricorsione non termina (🧩).

Passaggi → [[correttezza-per-induzione]].

## Perché importa

> 🎯 Esame: distinguere correttezza parziale e totale; per un algoritmo dato, indicare **quale** strumento dimostra ciascuna delle due parti (invariante o induzione per la parziale, variante o misura ben fondata per la terminazione).

## Connessioni

- [[algoritmo-e-problema]] — la definizione di algoritmo corretto (01 p. 9) è la correttezza totale
- [[invariante-di-ciclo]] — dimostra la parte parziale degli algoritmi iterativi, con la funzione variante per la terminazione
- [[correttezza-per-induzione]] — lo stesso per gli algoritmi ricorsivi
- [[ricerca-di-controesempi]] — l'altra faccia: dimostrare che un algoritmo non è corretto
- [[dimostrazioni-di-correttezza]] — esercizi svolti

## Fonti · 01-Introduzione.pdf [[01-Introduzione.pdf#page=9|p. 9]] · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=15|p. 15]]–[[03-Analisi di algoritmi.pdf#page=19|19]]

- [[lezione-01-introduzione]], [[lezione-03-analisi-di-algoritmi]]

_Aggiornato: 2026-10-01 — creata dalla spiegazione in chat su correttezza parziale e totale_

<!-- nav:inizio -->
---
**Lezione 03 · pagina 7 di 13** · ← [[somma-ricorsiva|somma_ricorsiva — somma dei primi n interi (versione ricorsiva)]] · [[lezioni|Indice]] · [[invariante-di-ciclo|Invariante di ciclo (correttezza degli algoritmi iterativi)]] →
<!-- nav:fine -->
