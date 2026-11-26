---
tipo: entità
categoria: algoritmo
paradigma: "ricorsione su albero (e versione iterativa)"
fonti_pdf: ["09-Alberi binari ricerca.pdf#page=10", "09-Alberi binari ricerca.pdf#page=11"]
---

# Tree-Search (ricerca in un BST)

## Problema risolto · [[09-Alberi binari ricerca.pdf#page=10|p. 10]]

Dato il puntatore alla radice e una chiave, restituisce il puntatore all'elemento con la data chiave, se esiste, e `NIL` altrimenti.

## Idea · [[09-Alberi binari ricerca.pdf#page=10|p. 10]]

I nodi incontrati nella ricerca formano un **percorso verso il basso** dalla radice: a ogni nodo il confronto con $key[x]$ dice in quale dei due sottoalberi può trovarsi la chiave, e l'altro viene scartato.

## Pseudocodice · [[09-Alberi binari ricerca.pdf#page=10|p. 10]], [[09-Alberi binari ricerca.pdf#page=11|11]]

> 📄 Fonte: p. 10 (versione ricorsiva) e p. 11 (versione iterativa, «tipicamente più efficiente»); riportati fedelmente, numeri di riga miei

```
Tree-Search (x,k)
1  if x=NIL or key[x]=k
2     then return x
3  if k < key[x]
4     then return Tree-Search (left[x],k)
5     else return Tree-Search (right[x],k)
```

```
Iterative-Tree-Search (x,k)
1  while x≠NIL and key[x]≠k
2      if k < key[x]
3         then x ← left[x]
4         else x ← right[x]
5  return x
```

![[09-alberi-binari-ricerca-p10-tree-search.png]]
![[09-alberi-binari-ricerca-p11-iterative-tree-search.png]]

> 🧩 Il corto circuito di `or` e `and` (→ [[pseudocodice]]) è essenziale: con $x = $ `NIL` il confronto su $key[x]$ non viene valutato.

## Esempio di esecuzione · [[09-Alberi binari ricerca.pdf#page=13|p. 13]]

![[animazione-tree-search.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero la versione ricorsiva sull'albero di p. 13, prima con la chiave 13 (trovata) e poi con la chiave 11 (assente). Il nodo corrente è in giallo, quelli già attraversati in azzurro, il nodo trovato in verde.

> 🧩 Traccia mia (verificata con [[grafi_e_alberi.py]]):

| $k$ | Percorso | Risultato |
|---|---|---|
| 13 | 15 → 6 (13 < 15) → 7 (13 > 6) → 13 (13 > 7) | nodo 13, dopo 4 nodi |
| 11 | 15 → 6 → 7 → 13 → 9 (11 < 13) → `NIL` (11 > 9) | `NIL`, dopo 5 nodi |

## Correttezza · [[09-Alberi binari ricerca.pdf#page=7|p. 7]]

> 🧩 Derivazione mia, per induzione sull'altezza del sottoalbero di radice $x$:
> - se $x = $ `NIL` la chiave non c'è; se $key[x] = k$ il nodo è quello cercato (righe 1–2);
> - se $k < key[x]$, per la proprietà del BST tutte le chiavi del sottoalbero destro sono $\ge key[x] > k$: $k$ può stare solo a sinistra, e la riga 4 lo cerca lì. Il caso $k > key[x]$ è simmetrico (riga 5);
> - la chiamata ricorsiva lavora su un sottoalbero di altezza minore: per ipotesi induttiva restituisce il nodo giusto o `NIL`.
>
> La versione iterativa fa le stesse scelte; **invariante** del `while`: se la chiave è nell'albero, è nel sottoalbero di radice $x$.

## Complessità · [[09-Alberi binari ricerca.pdf#page=10|p. 10]]

> 📄 Fonte: p. 10 — «Il tempo di esecuzione è $O(h)$ dove $h$ è l'altezza dell'albero»

### Derivazione — $O(h)$
> 🧩 Derivazione mia.

**Versione ricorsiva: la ricorrenza.** Ogni chiamata fa un lavoro costante $c$ (due confronti) e al più **una** chiamata ricorsiva, su un figlio, cioè un livello più in basso. Detto $T(h)$ il tempo su un sottoalbero di altezza $h$:
$$ T(h) \le T(h - 1) + c, \qquad T(-1) = c \ (\text{sottoalbero vuoto, } x = \texttt{NIL}) $$
La dimensione cala di **1** a ogni passo, quindi si **srotola** (→ [[equazioni-di-ricorrenza]]):
$$
\begin{aligned}
T(h) &\le T(h-1) + c \le T(h-2) + 2c \le \dots && \text{sostituisco ripetutamente} \\
     &\le T(h - j) + jc && \text{dopo } j \text{ passi} \\
     &\le T(-1) + (h+1)\,c = (h + 2)\,c && j = h + 1 \text{: si arriva a NIL} \\
     &= O(h)
\end{aligned}
$$

**Versione iterativa: si contano le iterazioni.** Ogni iterazione del `while` scende di un livello, quindi le iterazioni sono al più $h + 1$, ciascuna a costo costante: $O(h)$.

È $O$ e non $\Theta$: se la chiave sta nella radice basta un confronto.

> 🧩 Perché l'iterativa è «tipicamente più efficiente» (p. 11): fa le stesse scelte, ma senza il costo delle chiamate ricorsive e senza la pila delle chiamate. Lo spazio è $O(1)$ invece di $O(h)$ (→ [[iterazione-e-ricorsione]]).

## Connessioni

- [[albero-binario-di-ricerca]] — la proprietà che permette di scartare un sottoalbero
- [[tree-insert]] — scende con le stesse regole per trovare dove inserire
- [[iterazione-e-ricorsione]] — le due versioni dello stesso algoritmo
- [[albero]] — $h$ da $\Theta(\lg n)$ a $\Theta(n)$

## Fonti · [[09-Alberi binari ricerca.pdf#page=10|p. 10]], [[09-Alberi binari ricerca.pdf#page=11|11]]

- [[lezione-09-alberi-binari-di-ricerca]]

_Aggiornato: 2026-10-28 — ingest 09-Alberi binari ricerca.pdf_

<!-- nav:inizio -->
---
**Lezione 09 · pagina 5 di 9** · ← [[inorder-tree-walk|Inorder-Tree-Walk (visita in ordine)]] · [[lezioni|Indice]] · [[tree-minimum-maximum|Tree-Minimum e Tree-Maximum]] →
<!-- nav:fine -->
