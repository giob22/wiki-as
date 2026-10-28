---
tipo: entità
categoria: struttura-dati
fonti_pdf: ["09-Alberi binari ricerca.pdf#page=6", "09-Alberi binari ricerca.pdf#page=7"]
---

# Albero binario di ricerca (BST)

## Cos'è

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=6]]

- Gli alberi di ricerca sono strutture dati che supportano molte delle operazioni definite su **insiemi dinamici**: *Search, Minimum, Maximum, Predecessor, Successor, Insert, Delete*.
- Possono essere usati sia come **dizionario** sia come **coda a priorità** (→ [[coda-di-priorita]]).
- Le operazioni base richiedono un tempo **proporzionale all'altezza** $h$:
  - $\lg n$ se l'albero è completo;
  - $n$ nel caso degenere di [[lista-concatenata]].
- L'altezza attesa di un albero costruito in maniera aleatoria è $\lg n$...
- ...ma non sempre è possibile costruire l'albero in questa maniera.
- Alcuni tipi particolari di alberi di ricerca presentano nel caso peggiore un tempo di esecuzione «buono».

## Proprietà (invariante della struttura)

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=7]]

Un albero binario di ricerca soddisfa la seguente proprietà. Sia $x$ un nodo dell'albero:
- se $y$ è nel **sottoalbero sinistro** di $x$, allora $key[y] \le key[x]$;
- se $y$ è nel **sottoalbero destro** di $x$, allora $key[y] \ge key[x]$.

Esempio della slide: radice 5; figlio sinistro 3, con figli 2 e 5; figlio destro 7, con figlio destro 8.

![[09-alberi-binari-ricerca-p7-proprieta-bst.png]]

> 🧩 Precisazioni mie:
> - la proprietà riguarda **tutto** il sottoalbero, non solo i figli: nell'esempio il 5 in basso a sinistra è nel sottoalbero sinistro della radice 5, e infatti $5 \le 5$;
> - con le disuguaglianze non strette sono ammesse chiavi ripetute. [[tree-insert|Tree-Insert]] manda una chiave uguale a destra (`if key[z] < key[x] then … else x ← right[x]`).

## Rappresentazione in memoria

> 🧩 Dai campi usati nello pseudocodice delle slide (pp. 8–20): ogni nodo $x$ ha
> - $key[x]$, la chiave, più eventuali **dati satellite** ([[09-Alberi binari ricerca.pdf#page=20]]);
> - $left[x]$, $right[x]$, puntatori al figlio sinistro e destro;
> - $p[x]$, puntatore al padre.
>
> I puntatori mancanti valgono `NIL`; l'albero $T$ ha il campo $root[T]$ ([[09-Alberi binari ricerca.pdf#page=16]]). È una struttura **collegata**, come la [[lista-concatenata]] (→ [[strutture-contigue-e-collegate]]).

## Operazioni

| Operazione | Pagina wiki | Costo | Slide |
|------------|-------------|-------|-------|
| visita in ordine (stampa ordinata) | [[inorder-tree-walk]] | $\Theta(n)$ | pp. 8–9 |
| ricerca (ricorsiva e iterativa) | [[tree-search]] | $O(h)$ | pp. 10–11 |
| minimo e massimo | [[tree-minimum-maximum]] | $O(h)$ | p. 12 |
| successore | [[tree-successor]] | $O(h)$ | pp. 13–15 |
| inserimento | [[tree-insert]] | $O(h)$ | pp. 16–18 |
| eliminazione | [[tree-delete]] | $O(h)$ | pp. 19–21 |

> 🧩 Perché quasi tutte costano $O(h)$: scendono (o salgono) lungo **un solo ramo**, un livello per passo, con lavoro costante a ogni livello. Un ramo ha al più $h + 1$ nodi ([[08-Grafi e alberi.pdf#page=42]]: «un algoritmo che percorre un solo ramo impiega $O(h)$ passi»). Fa eccezione la visita in ordine, che tocca tutti i nodi.

### Derivazione — $h$ nel caso completo e nel caso degenere
**Fonte:** [[09-Alberi binari ricerca.pdf#page=6]] («$\lg n$ se completo, $n$ se degenere»)

> 🧩 Derivazione mia (→ [[albero]] § Bilanciamento):
> - **completo:** i livelli $0, \dots, h - 1$ sono pieni, quindi $n \ge 1 + 2 + \dots + 2^{h-1} + 1 = 2^h$, da cui $h \le \lg n$, cioè $h = \lfloor \lg n \rfloor = \Theta(\lg n)$;
> - **degenere:** ogni nodo ha un solo figlio, l'albero è una catena di $n$ nodi e $h = n - 1 = \Theta(n)$. Si ottiene, ad esempio, inserendo chiavi già ordinate.
>
> **Sanity check** ([[grafi_e_alberi.py]]): inserendo 4, 2, 6, 1, 3, 5, 7 si ottiene un albero di altezza 2; inserendo 1, 2, …, 7 un albero di altezza 6.

L'affermazione sull'altezza attesa di un albero costruito in modo aleatorio è enunciata senza dimostrazione (📚 Cormen, 3ª ed., §12.4).

## Connessioni

- [[albero]] — profondità, altezza, bilanciamento
- [[coda-di-priorita]] — il BST come coda di priorità
- [[lista-concatenata]] — il caso degenere
- [[quicksort]] — 🧩 come per quicksort, l'input ordinato è il caso peggiore: produce l'albero degenere

## Fonti

- [[lezione-09-alberi-binari-di-ricerca]]
- [[09-Alberi binari ricerca.pdf#page=6]], [[09-Alberi binari ricerca.pdf#page=7]]

_Aggiornato: 2026-10-28 — ingest 09-Alberi binari ricerca.pdf_

<!-- nav:inizio -->
---
**Lezione 09 · pagina 3 di 9** · ← [[coda-di-priorita|Coda di priorità]] · [[lezioni|Indice]] · [[inorder-tree-walk|Inorder-Tree-Walk (visita in ordine)]] →
<!-- nav:fine -->
