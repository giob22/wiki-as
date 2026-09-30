---
tipo: concetto
importanza_esame: alta
prerequisiti: ["iterazione-e-ricorsione", "invariante-di-ciclo"]
fonti_pdf: ["03-Analisi di algoritmi.pdf#page=18", "03-Analisi di algoritmi.pdf#page=19"]
---

# Correttezza degli algoritmi ricorsivi (per induzione)

## Definizione

> 📄 Fonte: [[03-Analisi di algoritmi.pdf#page=18]]

Per la ricorsione la prova di correttezza è strettamente legata all'**induzione** (spesso induzione **forte** o **strutturale**). È «simile nello spirito» agli invarianti di ciclo, ma la forma tipica è:

1. **Specifiche** — si definiscono **pre/post-condizioni** dell'algoritmo.
2. **Misura ben fondata** (es. dimensione dell'input) che **decresce** a ogni chiamata ricorsiva.
3. **Casi base** — si mostra che per gli input minimi il risultato è corretto.
4. **Passo induttivo** (induzione forte) — supposte corrette tutte le chiamate ricorsive su input «più piccoli» (**ipotesi induttiva**), si dimostra che, usando quei risultati, la funzione produce l'output corretto.
5. **Terminazione** — le chiamate ricorsive avvengono solo su input con misura strettamente minore ⇒ catena finita ⇒ termina.

## Derivazioni

### Derivazione — correttezza di [[somma-ricorsiva]]
**Fonte:** [[03-Analisi di algoritmi.pdf#page=19]]

```
funzione somma_ricorsiva(n)
1  se n = 0
2      ritorna 0
3  altrimenti
4      ritorna n + somma_ricorsiva(n − 1)
```

Dalla slide: **Misura:** $n$. **Base:** $n = 0 \Rightarrow S(0) = 0$ corretto. **Induzione:** se $S(n-1)$ è corretto, allora $S(n) = n + S(n-1)$ è corretto. **Terminazione:** ogni chiamata usa $n - 1 < n$.

> 🧩 Derivazione mia (passaggi espliciti, con post-condizione $S(n) = \sum_{k=1}^{n} k = \frac{n(n+1)}{2}$ e pre-condizione $n \in \mathbb N$):

$$
\begin{aligned}
&\textbf{Base } (n = 0):\ \ S(0) = 0 = \tfrac{0 \cdot 1}{2} && \text{righe 1–2} \\
&\textbf{Ipotesi induttiva:}\ \ S(n-1) = \tfrac{(n-1)n}{2} \\
&\textbf{Passo } (n \ge 1):\ \ S(n) = n + S(n-1) && \text{riga 4} \\
&\qquad = n + \tfrac{(n-1)n}{2} && \text{ipotesi induttiva} \\
&\qquad = \tfrac{2n + n^2 - n}{2} = \tfrac{n(n+1)}{2} && \text{algebra} \\
&\textbf{Terminazione:}\ \ n, n-1, \dots, 1, 0 \text{ è una catena finita di } n+1 \text{ chiamate}
\end{aligned}
$$

![[03-analisi-algoritmi-p19-induzione-somma-ricorsiva.png]]

## Spiegazione

Qui basta l'induzione **semplice** (si usa solo $S(n-1)$); l'induzione **forte** serve quando la funzione richiama sé stessa su input più piccoli qualsiasi (es. metà dell'input, tipico del [[divide-et-impera]]). La pre-condizione $n \ge 0$ è essenziale: con $n < 0$ la misura non raggiunge mai il caso base e la ricorsione non termina.

> 🧩 Derivazione mia (ultima frase): con $n = -1$ le chiamate sarebbero $-1, -2, \dots$, misura non ben fondata.

## Perché importa

> 🎯 Esame: per un algoritmo ricorsivo scrivere pre/post-condizioni, misura, caso base, passo induttivo e terminazione.

## Connessioni

- [[correttezza-parziale-e-totale]] — casi base e passo induttivo danno la correttezza **parziale**, la misura che decresce la terminazione
- [[invariante-di-ciclo]] — l'invariante è un'induzione sul numero di iterazioni
- [[equazioni-di-ricorrenza]] — stessa struttura (caso base + passo) usata per il costo
- [[optimal-scheduling]] — dimostrazione per induzione sul numero di intervalli
- [[dimostrazioni-di-correttezza]] — esercizi

## Fonti

- [[lezione-03-analisi-di-algoritmi]]
- [[03-Analisi di algoritmi.pdf#page=18]], [[03-Analisi di algoritmi.pdf#page=19]]

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_
_Aggiornato: 2026-10-01 — collegamento a correttezza-parziale-e-totale_
