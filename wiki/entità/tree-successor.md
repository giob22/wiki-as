---
tipo: entità
categoria: algoritmo
paradigma: "discesa o risalita lungo un ramo"
fonti_pdf: ["09-Alberi binari ricerca.pdf#page=13", "09-Alberi binari ricerca.pdf#page=14", "09-Alberi binari ricerca.pdf#page=15"]
---

# Tree-Successor (successore di un nodo)

## Problema risolto

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=13]]

Dato un nodo, il suo **successore** è quello che lo segue nella visita in ordine dell'albero (→ [[inorder-tree-walk]]). Se il nodo ha la chiave massima, il successore è `NIL`.

## Idea

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=13]]

Due casi:
1. **Se il nodo ha un figlio destro**, il successore è il **minimo del sottoalbero destro**. Esempio: il successore di 6 è 7.
2. **Altrimenti**, è il più «basso» antenato di $x$ il cui **figlio sinistro è un antenato di $x$**. Esempio: il successore di 13 è 15.

![[09-alberi-binari-ricerca-p13-successore-casi.png]]

> 🧩 Spiegazione mia del caso 2: se $x$ non ha figlio destro, nella visita in ordine dopo $x$ non c'è più nulla del suo sottoalbero. Si risale finché si sale da **destra** (quei padri sono già stati stampati prima di $x$); il primo padre raggiunto salendo da **sinistra** è il prossimo nodo stampato. Albero di p. 13: da 13 si sale a 7 (13 è figlio destro), poi a 6 (7 è figlio destro), poi a 15 (6 è figlio sinistro): il successore è 15.

## Pseudocodice

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=14]] (riportato fedelmente, numeri di riga miei)

```
Tree-Successor (x)
1  if right[x]≠NIL
2     then return Tree-Minimum(right[x])
3  y ← p[x]
4  while y≠NIL and x=right[y]
5      do x ← y
6         y ← p[y]
7  return y
```

[[tree-minimum-maximum|Tree-Minimum]] è la procedura di p. 12.

![[09-alberi-binari-ricerca-p14-tree-successor.png]]

## Esempio di esecuzione

![[animazione-tree-successor.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo sull'albero di [[09-Alberi binari ricerca.pdf#page=13]], per i due esempi della slide: il successore di 6 (caso 1, risultato 7) e di 13 (caso 2, risalita fino a 15). Il nodo dato è in rosa, $x$ in giallo, $y$ in azzurro, il successore in verde.

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=15]] (fotogramma iniziale di un'animazione della slide: «Due casi dello stesso algoritmo: se esiste un figlio destro, cerco il minimo; altrimenti risalgo»)

![[09-alberi-binari-ricerca-p15-successore-animazione.png]]

> 🧩 Traccia del caso 2 per $x = 13$ (verificata con [[grafi_e_alberi.py]]):

| Passo | $x$ | $y$ | $x = right[y]$? |
|-------|-----|-----|-----------------|
| riga 3 | 13 | 7 | sì → si sale |
| righe 5–6 | 7 | 6 | sì → si sale |
| righe 5–6 | 6 | 15 | no: 6 è figlio sinistro di 15 |
| riga 7 | | | return 15 |

## Correttezza

> 🧩 Derivazione mia, dalla visita in ordine (sinistra → nodo → destra):
> - **caso 1:** dopo aver stampato $x$, la visita entra nel sottoalbero destro e stampa per primo il suo nodo più a sinistra, cioè il minimo ([[tree-minimum-maximum]]);
> - **caso 2:** senza sottoalbero destro, la visita di $x$ è finita e la ricorsione risale. Ogni antenato da cui si sale da destra ha già stampato la sua chiave prima di entrare nel sottoalbero di $x$. Il primo antenato da cui si sale da sinistra stava visitando il suo sottoalbero sinistro: la sua chiave è la prossima stampata. Se non esiste (si arriva a $y = $ `NIL`), $x$ era il massimo.

## Complessità

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=14]] — «Il tempo di esecuzione è $O(h)$»

> 🧩 Derivazione mia:
> - **caso 1:** Tree-Minimum scende lungo un ramo: $O(h)$;
> - **caso 2:** ogni iterazione del `while` sale di un livello, quindi le iterazioni sono al più $h$: $O(h)$.
>
> Nei due casi si percorre un solo ramo, verso il basso o verso l'alto: $O(h)$.

## Connessioni

- [[inorder-tree-walk]] — il successore è definito dalla visita in ordine
- [[tree-minimum-maximum]] — usato nel caso 1
- [[tree-delete]] — nel caso con due figli si taglia fuori il successore

## Fonti

- [[lezione-09-alberi-binari-di-ricerca]]
- [[09-Alberi binari ricerca.pdf#page=13]]–[[09-Alberi binari ricerca.pdf#page=15]]

_Aggiornato: 2026-10-28 — ingest 09-Alberi binari ricerca.pdf_

<!-- nav:inizio -->
---
**Lezione 09 · pagina 7 di 9** · ← [[tree-minimum-maximum|Tree-Minimum e Tree-Maximum]] · [[lezioni|Indice]] · [[tree-insert|Tree-Insert (inserimento in un BST)]] →
<!-- nav:fine -->
