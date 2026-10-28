---
tipo: entità
categoria: algoritmo
paradigma: "ricorsione su albero"
fonti_pdf: ["09-Alberi binari ricerca.pdf#page=8", "09-Alberi binari ricerca.pdf#page=9"]
---

# Inorder-Tree-Walk (visita in ordine)

## Problema risolto

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=8]]

La proprietà di un [[albero-binario-di-ricerca]] consente di **stampare tutte le chiavi in ordine crescente** mediante una visita in ordine dell'albero.

- **Input:** un nodo $x$ (per l'intero albero, la radice).
- **Output:** le chiavi del sottoalbero di radice $x$, stampate in ordine non decrescente.

## Idea

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=9]]

Visita in ordine: **sinistra → nodo → destra**. Prima si visita tutto il sottoalbero sinistro, poi si stampa la chiave del nodo, poi si visita il sottoalbero destro.

## Pseudocodice

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=8]] (riportato fedelmente, numeri di riga miei)

```
Inorder-Tree-Walk (x)
1  if x≠NIL
2     then Inorder-Tree-Walk (left[x])
3          print key[x]
4          Inorder-Tree-Walk (right[x])
```

![[09-alberi-binari-ricerca-p8-inorder-pseudocodice.png]]

> ⚠️ Contraddizione (di notazione): `then` e l'assenza di blocchi espliciti sono nello stile della 2ª edizione del Cormen, non nelle [[pseudocodice|convenzioni del corso]]. Le righe 2–4 sono tutte il corpo dell'`if`.

## Esempio di esecuzione

![[animazione-inorder-tree-walk.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo sull'albero di [[09-Alberi binari ricerca.pdf#page=7]] (radice 5; 3 con figli 2 e 5; 7 con figlio destro 8). Si vedono la chiamata attiva ($x$), la pila delle chiamate, le chiavi già stampate (in verde) e il contatore delle chiamate, comprese quelle su `NIL`.

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=9]] (fotogramma iniziale di un'animazione della slide: «chiavi stampate:» ancora vuoto)

![[09-alberi-binari-ricerca-p9-visita-in-ordine.png]]

> 🧩 Traccia mia (verificata con [[grafi_e_alberi.py]]):

| Chiamata su | Cosa fa | Stampato finora |
|-------------|---------|-----------------|
| 5 | scende a sinistra | — |
| 3 | scende a sinistra | — |
| 2 | sinistra NIL, stampa 2, destra NIL | 2 |
| 3 (ritorno) | stampa 3, scende a destra | 2 3 |
| 5 (figlio di 3) | sinistra NIL, stampa 5, destra NIL | 2 3 5 |
| 5 (radice, ritorno) | stampa 5, scende a destra | 2 3 5 5 |
| 7 | sinistra NIL, stampa 7, scende a destra | 2 3 5 5 7 |
| 8 | sinistra NIL, stampa 8, destra NIL | 2 3 5 5 7 8 |

Chiamate totali: 13, di cui 6 su nodi e 7 su `NIL`.

## Correttezza

> 🧩 Derivazione mia — [[correttezza-per-induzione]] sul numero di nodi $n$ del sottoalbero di radice $x$. Post-condizione: le chiavi del sottoalbero sono stampate in ordine non decrescente.
> - **Base** ($n = 0$, $x = $ `NIL`): non si stampa nulla, corretto.
> - **Passo:** i sottoalberi sinistro e destro hanno meno di $n$ nodi, quindi per ipotesi induttiva la riga 2 stampa in ordine le chiavi di sinistra e la riga 4 quelle di destra. Per la proprietà del BST ([[09-Alberi binari ricerca.pdf#page=7]]) ogni chiave di sinistra è $\le key[x]$ e ogni chiave di destra è $\ge key[x]$. Stampare sinistra, poi $key[x]$, poi destra dà quindi una sequenza ordinata.
> - **Terminazione:** ogni chiamata ricorsiva lavora su un sottoalbero strettamente più piccolo.

## Complessità

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=9]] — «Dimostriamo che impiega un tempo $\Theta(n)$» (senza svolgimento)

### Derivazione — Inorder-Tree-Walk è $\Theta(n)$

> 🧩 Derivazione mia, con i metodi per le ricorrenze della lezione 06.

**1. Scrivere la ricorrenza dallo pseudocodice.** Sia $T(n)$ il tempo su un sottoalbero di $n$ nodi.
- Se $x = $ `NIL` ($n = 0$) si esegue solo il test della riga 1: costo costante $c$.
- Altrimenti il sottoalbero sinistro ha $k$ nodi e il destro $n - k - 1$ (il nodo $x$ è escluso). Oltre alle due chiamate si eseguono il test e la stampa, a costo costante $d$:
$$ T(0) = c, \qquad T(n) = T(k) + T(n - k - 1) + d \quad (n \ge 1,\ 0 \le k \le n - 1) $$

**2. Scegliere il metodo.**
- Il [[teorema-dell-esperto]] non si applica: $k$ dipende dalla forma dell'albero, non c'è un fattore di riduzione $b$ fisso.
- Lo srotolamento non è comodo: le due chiamate hanno dimensioni diverse e arbitrarie.
- Si usa il [[metodo-di-sostituzione]]: si **ipotizza** la soluzione e la si **verifica per induzione**, per **ogni** valore di $k$.

**3. Ipotizzare la soluzione.** Ogni nodo genera una chiamata, e ogni chiamata su un nodo genera due chiamate figlie: le chiamate sono $n$ su nodi e $n + 1$ su `NIL` (un albero binario con $n$ nodi ha $n + 1$ puntatori `NIL`: $2n$ puntatori in tutto, di cui $n - 1$ usati per gli archi). Questo suggerisce
$$ T(n) = (c + d)\,n + c $$

**4. Verificare per induzione forte.**
$$
\begin{aligned}
&\textbf{Base:}\ \ T(0) = c = (c+d)\cdot 0 + c && \text{caso NIL} \\
&\textbf{Passo:}\ \ T(n) = T(k) + T(n-k-1) + d && \text{ricorrenza} \\
&\qquad = \big[(c+d)k + c\big] + \big[(c+d)(n-k-1) + c\big] + d && \text{ipotesi induttiva su } k \text{ e } n-k-1 \text{, entrambi} < n \\
&\qquad = (c+d)(n-1) + 2c + d && k \text{ si elimina: vale per ogni forma dell'albero} \\
&\qquad = (c+d)\,n + c && \text{raccolgo}
\end{aligned}
$$

**5. Risultato.** $T(n) = (c + d)\,n + c = \Theta(n)$, **qualunque** sia la forma dell'albero (bilanciato o degenere), perché $k$ è sparito.

> **Sanity check** ([[grafi_e_alberi.py]]): l'albero di p. 7 ($n = 6$) fa 13 chiamate $= 2n + 1$; su alberi casuali con $n = 10, 100, 1000$ le chiamate sono 21, 201, 2001.
> **Ipotesi:** [[modello-ram]]; la stampa di una chiave costa un tempo costante.

## Proprietà

- 🧩 Visita **tutti** i nodi: è l'unica operazione del BST che non costa $O(h)$.
- 🧩 Su un BST produce le chiavi ordinate: costruire il BST e poi visitarlo è un modo di ordinare.

## Connessioni

- [[albero-binario-di-ricerca]] — la proprietà che rende ordinata la visita
- [[tree-successor]] — il successore è il nodo che segue nella visita in ordine
- [[metodo-di-sostituzione]] — il metodo usato per il $\Theta(n)$
- [[correttezza-per-induzione]] — la correttezza per induzione sulla dimensione del sottoalbero

## Fonti

- [[lezione-09-alberi-binari-di-ricerca]]
- [[09-Alberi binari ricerca.pdf#page=8]], [[09-Alberi binari ricerca.pdf#page=9]]

_Aggiornato: 2026-10-28 — ingest 09-Alberi binari ricerca.pdf_

<!-- nav:inizio -->
---
**Lezione 09 · pagina 4 di 9** · ← [[albero-binario-di-ricerca|Albero binario di ricerca (BST)]] · [[lezioni|Indice]] · [[tree-search|Tree-Search (ricerca in un BST)]] →
<!-- nav:fine -->
