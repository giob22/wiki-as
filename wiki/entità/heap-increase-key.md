---
tipo: entità
categoria: algoritmo
paradigma: "risalita lungo un cammino verso la radice"
fonti_pdf: ["10 - Heap - Heapsort.pdf#page=42", "10 - Heap - Heapsort.pdf#page=45", "10 - Heap - Heapsort.pdf#page=46", "10 - Heap - Heapsort.pdf#page=47", "10 - Heap - Heapsort.pdf#page=48"]
---

# Heap-Increase-Key

## Problema risolto · [[10 - Heap - Heapsort.pdf#page=42|p. 42]]

Operazione **Increase-Key**$(S, x, k)$ della [[coda-di-priorita]]: incrementa la chiave di $x$ al valore $k$ (con un min-heap, Decrease-Key la decrementa). Su un max-heap: dati $A$, un indice $i$ e un valore $key \ge A[i]$, imposta $A[i] \leftarrow key$ e ripristina la proprietà di max-heap.

## Idea · [[10 - Heap - Heapsort.pdf#page=45|p. 45]]

Aumentare una chiave può violare la proprietà solo verso l'alto (il nodo potrebbe superare il padre). Si **fa risalire l'elemento di cui si cambia la chiave in direzione della radice fino a trovare la giusta collocazione**: finché il padre è minore, si scambia il nodo con il padre.

## Pseudocodice · [[10 - Heap - Heapsort.pdf#page=48|p. 48]]

```
Heap-Increase-Key (A,i,key)
1  if key < A[i]
2      error "new key is smaller"
3  A[i] ← key
4  while i > 1 and A[Parent(i)] < A[i]
5      exchange A[i] ↔ A[Parent(i)]
6      i ← Parent(i)
```

![[10-heap-heapsort-p48-heap-increase-key-codice.png]]

## Esempio di esecuzione · [[10 - Heap - Heapsort.pdf#page=45|p. 45]]–[[10 - Heap - Heapsort.pdf#page=48|48]]

![[animazione-heap-increase-key.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero l'algoritmo sull'heap di p. 45, $\langle 16, 14, 10, 8, 7, 9, 3, 2, 4, 1 \rangle$, con $i = 9$ (la chiave 4) e $key = 15$, come nelle slide.

![[10-heap-heapsort-p46-increase-key-chiave.png]]

Traccia (verificata con [[heap.py]]); p. 45 mostra l'heap di partenza, p. 46 la chiave $A[9] = 4$ portata a 15 (nodo arancione), p. 47 il primo scambio con il padre 8:

| Passo | $i$ | $A[\text{Parent}(i)]$ | Azione | Array |
|---|---|---|---|---|
| riga 3 | 9 | 8 | $A[9] \leftarrow 15$ | $\langle 16, 14, 10, 8, 7, 9, 3, 2, 15, 1 \rangle$ |
| righe 4–6 | 9 → 4 | $8 < 15$ | scambio con $A[4]$ (p. 47) | $\langle 16, 14, 10, 15, 7, 9, 3, 2, 8, 1 \rangle$ |
| righe 4–6 | 4 → 2 | $14 < 15$ | scambio con $A[2]$ | $\langle 16, 15, 10, 14, 7, 9, 3, 2, 8, 1 \rangle$ |
| riga 4 | 2 | $16 \ge 15$ | il ciclo termina | — |

> 🧩 Le slide si fermano al primo scambio (pp. 47–48, dove 15 è figlio di 14 e quindi l'heap non è ancora valido): lo svolgimento completo è quello della tabella.

## Correttezza · [[10 - Heap - Heapsort.pdf#page=48|p. 48]]

> 🧩 Derivazione mia. **Invariante** del `while`: all'inizio di ogni iterazione $A[1..heap\text{-}size]$ è un max-heap *tranne* al più una violazione, fra $A[i]$ e $A[\text{Parent}(i)]$ ($A[i]$ può essere maggiore del padre); inoltre, se $i$ ha figli, $A[\text{Parent}(i)] \ge$ ciascun figlio di $i$.
> - **Inizializzazione:** prima del ciclo l'heap era valido e solo $A[i]$ è aumentato: l'unica violazione possibile è con il padre. Il padre era già $\ge$ il vecchio $A[i] \ge$ i suoi figli, e se il nuovo $A[i]$ non è maggiore del padre la seconda condizione vale con $A[i]$ stesso.
> - **Conservazione:** sia $p = \text{Parent}(i)$ con $A[p] < A[i]$, e $s$ il fratello di $i$. Si scambiano $A[i]$ e $A[p]$. Dopo lo scambio:
>   - il nodo $i$ contiene il vecchio $A[p]$, che per la seconda condizione era $\ge$ i figli di $i$: fra $i$ e i suoi figli non c'è violazione;
>   - il nodo $p$ contiene la chiave aumentata, maggiore del vecchio $A[p]$, che era $\ge$ $A[s]$ (heap valido): $p$ è $\ge$ entrambi i figli $i$ e $s$;
>   - l'unica violazione possibile è fra $p$ e il suo padre; e il padre di $p$ è $\ge$ il vecchio $A[p]$ (heap valido prima), che ora è il contenuto di $i$, e $\ge$ $A[s]$: vale la seconda condizione. Con $i \leftarrow p$ l'invariante vale di nuovo.
> - **Conclusione:** il ciclo termina o per $i = 1$ (nessun padre) o perché $A[\text{Parent}(i)] \ge A[i]$: in entrambi i casi non ci sono più violazioni.

## Complessità · [[10 - Heap - Heapsort.pdf#page=48|p. 48]]

La slide dichiara tempo $O(\lg n)$, con $O(\lg n)$ scambi.

> 🧩 Derivazione mia: a ogni iterazione $i$ passa a $\lfloor i/2 \rfloor$, cioè sale di un livello; dalla posizione $i$ (livello $\lfloor \lg i \rfloor$) alla radice ci sono al più $\lfloor \lg i \rfloor \le \lfloor \lg n \rfloor$ iterazioni, ciascuna a costo costante. Totale $O(\lg n)$. Nell'esempio 2 scambi (da livello 3 a livello 1).

**Ipotesi:** modello RAM; $n = heap\text{-}size[A]$.

## Connessioni

- [[max-heap-insert]] — lo usa per inserire una chiave
- [[coda-di-priorita]] — Increase-Key
- [[max-heapify]] — l'operazione «verso il basso», duale di questa «verso l'alto»

## Fonti · [[10 - Heap - Heapsort.pdf#page=42|p. 42]], [[10 - Heap - Heapsort.pdf#page=45|45]]–[[10 - Heap - Heapsort.pdf#page=48|48]]

- [[lezione-10-heap-e-heapsort]]

_Aggiornato: 2026-11-26 — ingest 10 - Heap - Heapsort.pdf_

<!-- nav:inizio -->
---
**Lezione 10 · pagina 7 di 9** · ← [[heap-extract-max|Heap-Maximum e Heap-Extract-Max]] · [[lezioni|Indice]] · [[max-heap-insert|Max-Heap-Insert]] →
<!-- nav:fine -->
