---
tipo: entità
categoria: algoritmo
paradigma: "discesa lungo un ramo"
fonti_pdf: ["09-Alberi binari ricerca.pdf#page=12"]
---

# Tree-Minimum e Tree-Maximum

## Problema risolto

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=12]]

Trovare il nodo con la chiave minima (massima) nel sottoalbero di radice $x$ di un [[albero-binario-di-ricerca]].

## Idea

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=12]]

- L'elemento **minimo** può essere trovato percorrendo, a partire dalla radice, sempre il sottoalbero di **sinistra**.
- L'elemento **massimo** può essere trovato percorrendo, a partire dalla radice, sempre il sottoalbero di **destra**.

## Pseudocodice

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=12]] (riportato fedelmente, numeri di riga miei)

```
Tree-Minimum (x)
1  while left[x]≠NIL
2      do x ← left[x]
3  return x

Tree-Maximum (x)
4  while right[x]≠NIL
5      do x ← right[x]
6  return x
```

![[09-alberi-binari-ricerca-p12-minimo-massimo.png]]

## Esempio di esecuzione

![[animazione-tree-minimum-maximum.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero le due procedure sull'albero di [[09-Alberi binari ricerca.pdf#page=13]]: il minimo si trova scendendo 15 → 6 → 3 → 2, il massimo scendendo 15 → 18 → 20. Verificato con [[grafi_e_alberi.py]] (minimo 2, massimo 20).

## Correttezza

> 🧩 Derivazione mia (minimo; il massimo è simmetrico). **Invariante** del `while`: il minimo dell'albero di partenza sta nel sottoalbero di radice $x$.
> - **Inizializzazione:** $x$ è la radice del sottoalbero di partenza.
> - **Conservazione:** se $left[x] \ne$ `NIL`, tutte le chiavi di $x$ e del suo sottoalbero destro sono $\ge$ di quelle del sottoalbero sinistro (proprietà del BST, [[09-Alberi binari ricerca.pdf#page=7]]): il minimo è nel sottoalbero sinistro, e $x \leftarrow left[x]$ conserva l'invariante.
> - **Conclusione:** quando $left[x] = $ `NIL`, il sottoalbero di $x$ è $x$ più il suo sottoalbero destro, le cui chiavi sono $\ge key[x]$: il minimo è $x$.
> - **Terminazione:** a ogni iterazione si scende di un livello.

## Complessità

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=12]] — «Il tempo di esecuzione è $O(h)$»

> 🧩 Derivazione mia: ogni iterazione del `while` scende di un livello lungo il ramo più a sinistra (più a destra), quindi le iterazioni sono al più $h$, ciascuna a costo costante, più il test finale e il `return`: $O(h)$. Nell'esempio: 3 iterazioni per il minimo, 2 per il massimo.

## Connessioni

- [[tree-successor]] — nel caso 1 il successore è Tree-Minimum del sottoalbero destro
- [[tree-delete]] — usa il successore, quindi Tree-Minimum
- [[coda-di-priorita]] — Find-Minimum e Find-Maximum su un BST

## Fonti

- [[lezione-09-alberi-binari-di-ricerca]]
- [[09-Alberi binari ricerca.pdf#page=12]]

_Aggiornato: 2026-10-28 — ingest 09-Alberi binari ricerca.pdf_

<!-- nav:inizio -->
---
**Lezione 09 · pagina 6 di 9** · ← [[tree-search|Tree-Search (ricerca in un BST)]] · [[lezioni|Indice]] · [[tree-successor|Tree-Successor (successore di un nodo)]] →
<!-- nav:fine -->
