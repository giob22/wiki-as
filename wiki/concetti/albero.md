---
tipo: concetto
importanza_esame: alta
prerequisiti: ["grafo", "tipi-di-grafo", "logaritmi-nell-analisi"]
fonti_pdf: ["08-Grafi e alberi.pdf#page=37", "08-Grafi e alberi.pdf#page=38", "08-Grafi e alberi.pdf#page=39", "08-Grafi e alberi.pdf#page=40", "08-Grafi e alberi.pdf#page=41", "08-Grafi e alberi.pdf#page=42", "08-Grafi e alberi.pdf#page=43", "08-Grafi e alberi.pdf#page=44"]
---

# Albero

## Definizione · [[08-Grafi e alberi.pdf#page=37|p. 37]], [[08-Grafi e alberi.pdf#page=38|38]]

Riprendendo tre caratteristiche dei [[tipi-di-grafo]]:
- **non orientato**: gli archi non hanno un verso;
- **connesso**: ogni coppia di nodi è collegata da un cammino;
- **aciclico**: non contiene cicli.

Quando tutte e tre le proprietà sono presenti insieme, il grafo prende il nome di **albero**: *un albero è un grafo non orientato, connesso e privo di cicli*.

La slide di p. 38 chiede quale di tre grafi sia un albero: il grafo 1 no (c'è un ciclo), il grafo 2 no (non è connesso), il grafo 3 sì.

![[08-grafi-e-alberi-p37-albero-definizione.png]]
![[08-grafi-e-alberi-p38-quale-e-albero.png]]

## Tre conseguenze della definizione · [[08-Grafi e alberi.pdf#page=39|p. 39]]

1. **Cammino unico:** tra due nodi esiste un solo cammino semplice (in figura il percorso arancione collega E e G).
2. **Archi essenziali:** se si rimuove un arco, il grafo si disconnette.
3. **$n - 1$ archi:** con $n$ nodi gli archi sono sempre $n - 1$ (in figura 7 nodi e 6 archi).

Annotazione a mano sotto la slide: «la complessità spaziale dipende dalla struttura fisica → struttura dati utilizzata».

![[08-grafi-e-alberi-p39-conseguenze-definizione.png]]

### Derivazione — perché valgono le tre conseguenze · [[08-Grafi e alberi.pdf#page=39|p. 39]]

> 🧩 Derivazione mia:
> 1. **Cammino unico.** Un cammino esiste perché l'albero è connesso. Se ce ne fossero due diversi tra $u$ e $v$, partendo da $u$ si potrebbe seguire il primo fino a dove i due si separano e tornare indietro lungo il secondo fino a dove si ricongiungono: si otterrebbe un **ciclo**, contro l'aciclicità.
> 2. **Archi essenziali.** Se togliendo l'arco $(u, v)$ il grafo restasse connesso, ci sarebbe un altro cammino tra $u$ e $v$; aggiungendo l'arco si chiuderebbe un ciclo. Quindi la rimozione disconnette.
> 3. **$n - 1$ archi**, per [[correttezza-per-induzione|induzione]] su $n$.
>    - *Base* ($n = 1$): un solo nodo, 0 archi.
>    - *Passo:* un albero con $n \ge 2$ nodi ha almeno una **foglia**, cioè un nodo di grado 1: partendo da un nodo qualsiasi e camminando senza mai tornare indietro, in un grafo finito e aciclico ci si deve fermare in un nodo senza altri archi. Togliendo la foglia e il suo arco resta un albero con $n - 1$ nodi (ancora connesso e aciclico), che per ipotesi induttiva ha $n - 2$ archi. Rimettendo l'arco tolto: $n - 1$ ✓.
>
> **Sanity check:** figura di p. 39, 7 nodi e 6 archi ([[grafi_e_alberi.py]]).

## Radice, profondità, altezza · [[08-Grafi e alberi.pdf#page=40|p. 40]], [[08-Grafi e alberi.pdf#page=41|41]]

**La radice è una scelta (quasi) arbitraria** (p. 40): con una radice si può leggere lo stesso grafo come una **gerarchia**. Nell'esempio, scegliendo A come radice: B, C, D sono i **figli** di A; C, E, F, G sono le **foglie**.

Dopo aver scelto una radice si misura la distanza dei nodi da essa (p. 41):
- **profondità di un nodo:** numero di archi dalla radice al nodo; la radice ha profondità 0;
- **altezza dell'albero:** massima profondità tra tutti i nodi;
- **livelli:** nodi con la stessa profondità appartengono allo stesso livello.

Nell'esempio di p. 41 (A radice; B, C a profondità 1; D, E, F, G a profondità 2): profondità(G) = 2, altezza dell'albero $h = 2$.

![[08-grafi-e-alberi-p40-radice.png]]
![[08-grafi-e-alberi-p41-profondita-altezza.png]]

## Bilanciamento · 08-Grafi e alberi.pdf [[08-Grafi e alberi.pdf#page=42|p. 42]] · 09-Alberi binari ricerca.pdf [[09-Alberi binari ricerca.pdf#page=6|p. 6]]

Due alberi binari con 7 nodi, ma con altezze molto diverse:
- **bilanciato**: 7 nodi, altezza 2, $h = \Theta(\log n)$;
- **degenere** (una catena A–B–C–D–E–F–G): 7 nodi, altezza 6, $h = \Theta(n)$.

**Un algoritmo che percorre un solo ramo impiega $O(h)$ passi.**

![[08-grafi-e-alberi-p42-bilanciamento.png]]

> 🧩 Derivazione mia: nel caso degenere ogni nodo ha un solo figlio, quindi i livelli sono $n$ e $h = n - 1$ (per 7 nodi, 6). Nel caso bilanciato il livello $i$ è pieno con $2^i$ nodi, quindi $n = 2^{h+1} - 1$ e $h = \lg(n + 1) - 1$ (per 7 nodi, 2). È la formula generale qui sotto con $k = 2$. Questa differenza è il motivo per cui le operazioni sugli [[albero-binario-di-ricerca|alberi binari di ricerca]] costano $O(h)$: da $\Theta(\lg n)$ a $\Theta(n)$ a seconda della forma.

## La base del logaritmo: perché $\log_k n$ · [[08-Grafi e alberi.pdf#page=43|p. 43]]

La base dipende dal **fattore di ramificazione** $k$ (figli per nodo), se l'albero è sufficientemente bilanciato:
- binario (2 figli per nodo): $h = \Theta(\log_2 n)$;
- ternario (3 figli per nodo): $h = \Theta(\log_3 n)$;
- $k$-ario ($k$ figli per nodo): $h = \Theta(\log_k n)$.

**Albero $k$-ario perfetto:** ogni nodo interno ha esattamente $k$ figli e tutte le foglie sono alla stessa profondità. Al livello $i$ ci sono $k^i$ nodi, quindi con altezza $h$:
$$
n = 1 + k + k^2 + \dots + k^h = \frac{k^{h+1} - 1}{k - 1} \qquad\Longrightarrow\qquad h = \log_k\big(n(k-1) + 1\big) - 1
$$
Con $k$ costante: $h = \Theta(\log_k n)$. La stessa crescita vale per alberi $k$-ari sufficientemente bilanciati.

![[08-grafi-e-alberi-p43-base-logaritmo.png]]

### Derivazione — da $n$ ad $h$
> 🧩 Derivazione mia dei passaggi della slide:
$$
\begin{aligned}
n &= \sum_{i=0}^{h} k^i = \frac{k^{h+1} - 1}{k - 1} && \text{serie geometrica di ragione } k \\
n(k-1) + 1 &= k^{h+1} && \text{moltiplico per } k - 1 \text{ e sommo } 1 \\
h + 1 &= \log_k\big(n(k-1) + 1\big) && \text{logaritmo in base } k \\
h &= \log_k\big(n(k-1) + 1\big) - 1 = \Theta(\log_k n) && n(k-1) + 1 = \Theta(n) \text{ per } k \text{ costante}
\end{aligned}
$$
> Con $k$ costante, $\log_k n = \lg n / \lg k$: cambia solo una costante, come per la base del logaritmo in [[logaritmi-nell-analisi]].
>
> **Sanity check** ([[grafi_e_alberi.py]]): $k = 2$, $h = 2$ dà $n = 7$ e la formula restituisce $h = 2$; $k = 3$, $h = 3$ dà $n = 40$ e la formula restituisce $h = 3$.

## Dove ritroviamo gli alberi · [[08-Grafi e alberi.pdf#page=44|p. 44]]

- **Gerarchie di cartelle**: progetto → src, test → main.c, test.c.
- **Alberi di espressione**: $(a + b) \times c$, con gli operatori nei nodi interni e gli operandi nelle foglie.
- **Alberi di ricorsione**: $T(n)$ → due $T(n/2)$ → quattro $T(n/4)$, come in [[merge-sort]] (→ [[metodo-albero-di-ricorrenza]]).

«Stessa struttura matematica, interpretazioni differenti.»

![[08-grafi-e-alberi-p44-dove-alberi.png]]

## Perché importa

> 🎯 Esame: definizione di albero, le tre conseguenze (con il perché), profondità e altezza, $h = \Theta(\log n)$ contro $\Theta(n)$, formula dell'altezza dell'albero $k$-ario perfetto.

## Connessioni

- [[grafo]], [[tipi-di-grafo]] — l'albero è un grafo non orientato, connesso, aciclico
- [[albero-binario-di-ricerca]] — le operazioni costano $O(h)$: il bilanciamento decide tutto
- [[metodo-albero-di-ricorrenza]] — gli alberi di ricorsione di p. 44
- [[logaritmi-nell-analisi]] — la base del logaritmo cambia solo la costante

## Fonti · [[08-Grafi e alberi.pdf#page=37|p. 37]], [[08-Grafi e alberi.pdf#page=44|p. 44]]

- [[lezione-08-grafi-e-alberi]]

_Aggiornato: 2026-10-28 — ingest 08-Grafi e alberi.pdf_

<!-- nav:inizio -->
---
**Lezione 08 · pagina 6 di 6** · ← [[liste-di-adiacenza|Liste di adiacenza]] · [[lezioni|Indice]] · [[lezione-09-alberi-binari-di-ricerca|Lezione 09: introduzione e riepilogo]] →
<!-- nav:fine -->
