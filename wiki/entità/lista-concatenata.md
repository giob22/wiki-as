---
tipo: entità
categoria: struttura-dati
fonti_pdf: ["04-Strutture dati elementari.pdf#page=16", "04-Strutture dati elementari.pdf#page=17", "04-Strutture dati elementari.pdf#page=18", "04-Strutture dati elementari.pdf#page=19", "04-Strutture dati elementari.pdf#page=20", "04-Strutture dati elementari.pdf#page=22"]
---

# Lista concatenata (semplice e doppia)

## Cos'è

Struttura **collegata**: ogni nodo contiene un dato e un puntatore al successore; l'ultimo punta a `NIL` ([[04-Strutture dati elementari.pdf#page=16]]). → [[strutture-contigue-e-collegate]]

## Rappresentazione in memoria

> 📄 Fonte: [[04-Strutture dati elementari.pdf#page=16]] (codice C riportato fedelmente)

```c
typedef struct list {
    item_type item;        /* data item */
    struct list *next;     /* point to successor */
} list;
```

![[04-strutture-dati-p16-lista-concatenata.png]]
*Lista Turing → Knuth → Karp → NIL; il cerchio grigio è il puntatore alla testa. ([[04-Strutture dati elementari.pdf#page=16]])*

## Operazioni

### Inserimento in testa
> 📄 Fonte: [[04-Strutture dati elementari.pdf#page=17]]

Non serve mantenere un ordine particolare, quindi conviene inserire ogni nuovo elemento **in testa**.

```c
void insert_list(list **l, item_type x) {
    list *p;               /* temporary pointer */
    p = malloc(sizeof(list));
    p->item = x;
    p->next = *l;
    *l = p;
}
```

Nota il `**l`: la testa della lista cambia, quindi serve un puntatore al puntatore di testa. **Costo: $\Theta(1)$** ([[04-Strutture dati elementari.pdf#page=17]]).

### Ricerca
> 📄 Fonte: [[04-Strutture dati elementari.pdf#page=18]]

La ricerca si può fare in modo iterativo o ricorsivo; la slide mostra la versione ricorsiva:

```c
list *search_list(list *l, item_type x) {
    if (l == NULL) {
        return(NULL);
    }
    if (l->item == x) {
        return(l);
    } else {
        return(search_list(l->next, x));
    }
}
```

**Best case:** $\Theta(1)$ — il primo nodo è quello cercato. **Worst case:** $\Theta(n)$ — è l'ultimo o non c'è.

### Cancellazione — ricerca del predecessore
> 📄 Fonte: [[04-Strutture dati elementari.pdf#page=19]]

```c
list *item_ahead(list *l, list *x) {
    if ((l == NULL) || (l->next == NULL)) {
        return(NULL);
    }
    if ((l->next) == x) {
        return(l);
    } else {
        return(item_ahead(l->next, x));
    }
}
```

**Best case:** $\Theta(1)$ — il primo nodo è quello cercato (è il predecessore). **Worst case:** $\Theta(n)$ — è l'ultimo o non c'è.

### Cancellazione — rimozione del nodo
> 📄 Fonte: [[04-Strutture dati elementari.pdf#page=20]]

```c
void delete_list(list **l, list **x) {
    list *p;               /* item pointer */
    list *pred;            /* predecessor pointer */
    p = *l;
    pred = item_ahead(*l, *x);
    if (pred == NULL) {    /* splice out of list */
        *l = p->next;
    } else {
        pred->next = (*x)->next;
    }
    free(*x);              /* free memory used by node */
}
```

**Best case:** $\Theta(1)$ — «cancelli la testa o la trovi subito». **Worst case:** $\Theta(n)$ — tempo dominato dalla ricerca del predecessore.

> ⚠️ Contraddizione (🧩 osservazione mia sul codice): con **questo** `item_ahead`, cancellare la **testa** non costa $\Theta(1)$. Se `*x` è la testa, nessun nodo ha `next == x`, quindi `item_ahead` scorre tutta la lista prima di restituire `NULL`: $\Theta(n)$. Il caso $\Theta(1)$ si ha quando il predecessore è il primo nodo (cioè si cancella il secondo). Per avere la testa in $\Theta(1)$ bisognerebbe controllare `*l == *x` prima di chiamare `item_ahead`. Inoltre il codice presuppone che `*x` appartenga alla lista: se non c'è, `pred == NULL` e viene staccata la testa per errore.

> 🧩 Traduzione mia nelle [[pseudocodice|convenzioni del corso]] (puntatori come variabili aggregate, `NIL`, campi con `.`), con il controllo sulla testa:

```
LIST-SEARCH(L, k)
1  x ← L.head
2  while x ≠ NIL and x.key ≠ k        ▷ and in corto circuito
3      x ← x.next
4  return x

LIST-INSERT(L, x)                     ▷ inserimento in testa, Θ(1)
1  x.next ← L.head
2  L.head ← x

LIST-DELETE(L, x)                     ▷ x appartiene a L
1  if L.head = x
2      L.head ← x.next                ▷ testa: Θ(1)
3  else p ← L.head
4      while p.next ≠ x               ▷ ricerca del predecessore: O(n)
5          p ← p.next
6      p.next ← x.next
```

Il corto circuito di `and` alla riga 2 di LIST-SEARCH evita di leggere `x.key` quando `x = NIL` ([[a1-indicazioni_psuedocodice.pdf#page=4]]).

## Liste semplici e doppie

> 📄 Fonte: [[04-Strutture dati elementari.pdf#page=22]]

Con le **liste doppiamente concatenate** (ogni nodo punta anche al predecessore) si guadagna flessibilità nelle interrogazioni sul predecessore, al costo di **raddoppiare il numero di puntatori**. Poiché il costo extra in big-Oh è **zero**, di solito si assume che le liste siano mantenute doppie, anche se non sempre è necessario. «Singly linked to doubly-linked list is as a conga line is to a can-can line.»

![[04-strutture-dati-p22-lista-semplice-doppia.png]]
*Sopra: lista semplice A→…→F; sotto: lista doppia con puntatori in entrambi i versi. ([[04-Strutture dati elementari.pdf#page=22]])*

> 🧩 Derivazione mia: in una lista doppia il predecessore di $x$ è `x.prev`, quindi la cancellazione di un nodo di cui si ha il puntatore costa $\Theta(1)$ invece di $\Theta(n)$: è la «flessibilità sulle interrogazioni del predecessore».

## Costi riassunti

| Operazione | Lista semplice | Fonte |
|-----------|----------------|-------|
| inserimento in testa | $\Theta(1)$ | [[04-Strutture dati elementari.pdf#page=17]] |
| ricerca | best $\Theta(1)$, worst $\Theta(n)$ | [[04-Strutture dati elementari.pdf#page=18]] |
| predecessore | best $\Theta(1)$, worst $\Theta(n)$ | [[04-Strutture dati elementari.pdf#page=19]] |
| cancellazione | best $\Theta(1)$, worst $\Theta(n)$ | [[04-Strutture dati elementari.pdf#page=20]] |

## Connessioni

- [[array]] — confronto vantaggi/svantaggi ([[04-Strutture dati elementari.pdf#page=21]]) in [[strutture-contigue-e-collegate]]
- [[coda]] — implementazione naturale su lista ([[04-Strutture dati elementari.pdf#page=28]])
- [[casi-di-complessita]] — ogni operazione ha casi migliore e peggiore distinti
- [[iterazione-e-ricorsione]] — `search_list` e `item_ahead` sono ricorsive; LIST-SEARCH è la versione iterativa

## Fonti

- [[lezione-04-strutture-dati-elementari]]
- [[04-Strutture dati elementari.pdf#page=16]]–[[04-Strutture dati elementari.pdf#page=22]]

_Aggiornato: 2026-09-26 — ingest 04-Strutture dati elementari.pdf_
