---
tipo: entità
categoria: struttura-dati
fonti_pdf: ["08-Grafi e alberi.pdf#page=28", "08-Grafi e alberi.pdf#page=29", "08-Grafi e alberi.pdf#page=30", "08-Grafi e alberi.pdf#page=31", "08-Grafi e alberi.pdf#page=32", "08-Grafi e alberi.pdf#page=33", "08-Grafi e alberi.pdf#page=34", "08-Grafi e alberi.pdf#page=35"]
---

# Liste di adiacenza

Le sezioni seguono le slide: definizione (p. 28), appunti (p. 29), confronto con la matrice (p. 30), implementazione in C (pp. 31–35).

## Cos'è

> 📄 Fonte: [[08-Grafi e alberi.pdf#page=28]]

Una **lista di adiacenza** è un array di $N \times 1$ puntatori, in cui l'$i$-esimo elemento punta a una [[lista-concatenata]] degli archi incidenti sul vertice $i$.

- Per verificare se l'arco $(i, j)$ è nel grafo si cerca $j$ nella lista $i$-esima, in tempo $O(d_i)$, dove $d_i$ è il **grado** dell'$i$-esimo vertice.
- $d_i$ può essere molto minore di $n$ quando il grafo è sparso.
- Se necessario, le due **copie** di ogni arco possono essere collegate da un puntatore per facilitare le cancellazioni.

![[08-grafi-e-alberi-p28-liste-di-adiacenza.png]]
*Grafo non orientato con 5 vertici e 7 archi e le sue liste: 1 → 2, 5; 2 → 1, 5, 4, 3; 3 → 2, 4; 4 → 5, 2, 3; 5 → 1, 2, 4. Ogni arco compare in due liste. ([[08-Grafi e alberi.pdf#page=28]])*

Appunto a mano di [[08-Grafi e alberi.pdf#page=29]] (pagina a righe): «modalità di navigazione → come scorro il grafo partendo da un nodo». La lista del vertice $v$ dà direttamente i vicini di $v$, cioè i passi possibili da $v$.

![[08-grafi-e-alberi-p29-appunti-navigazione.png]]

## Confronto con la matrice di adiacenza

> 📄 Fonte: [[08-Grafi e alberi.pdf#page=30]]

| Confronto | Vincitore |
|-----------|-----------|
| più veloce verificare se $(x, y)$ esiste? | matrici |
| più veloce trovare il grado di un vertice? | liste |
| meno memoria su grafi piccoli? | liste ($m + n$ contro $n^2$) |
| meno memoria su grafi grandi? | matrici (vittoria di poco) |
| inserimento o cancellazione di un arco? | matrici, $O(1)$ |
| più veloce attraversare il grafo? | liste ($m + n$ contro $n^2$) |
| migliori per la maggior parte dei problemi? | liste |

Entrambe le rappresentazioni sono molto utili e hanno proprietà diverse, anche se le liste di adiacenza sono probabilmente migliori per la maggior parte dei problemi.

![[08-grafi-e-alberi-p30-confronto-rappresentazioni.png]]

### Derivazione — i costi della tabella
> 🧩 Derivazione mia, riga per riga (matrice: → [[matrice-di-adiacenza]]):

| Confronto | Matrice | Liste | Perché |
|-----------|---------|-------|--------|
| test $(x, y)$ | $O(1)$ | $O(d_x)$ | la matrice accede direttamente a $M[x, y]$; la lista va scorsa |
| grado | $\Theta(n)$ | $O(1)$ | la riga va scorsa tutta; con le liste il grado è un campo della struttura (`degree[x]`, p. 32) |
| spazio | $\Theta(n^2)$ | $\Theta(n + m)$ | liste: $n$ puntatori più $\sum_v d_v = 2m$ nodi di lista (non orientato, [[grafo]] § Formule) |
| inserimento / cancellazione | $O(1)$ / $O(1)$ | $O(1)$ / $O(d_x)$ | inserire in testa a una lista è costante (`insert_edge`, p. 35); cancellare richiede di cercare l'arco |
| attraversamento | $\Theta(n^2)$ | $\Theta(n + m)$ | per elencare i vicini di tutti i vertici: $n$ righe di $n$ celle, contro $n$ liste di lunghezza totale $2m$ |

> Sui **grafi grandi e densi** ($m \approx n^2/2$) le liste contengono circa $n^2$ nodi, ognuno con un intero e un puntatore, mentre la matrice può usare un solo bit per cella (la «bitmap» degli appunti di p. 27): per questo lì vince la matrice, «di poco» perché l'ordine di grandezza è lo stesso, $\Theta(n^2)$.
>
> **Sanity check** ([[grafi_e_alberi.py]]): sul grafo di p. 28 le liste contengono 14 nodi $= 2m$; con $n = 1000$, $m = 499\,500$ (grafo completo) le voci delle liste sono $n + 2m = 10^6$, quante le celle della matrice.

## Implementazione in C

> 📄 Fonte: [[08-Grafi e alberi.pdf#page=31]]–[[08-Grafi e alberi.pdf#page=35]] (codice riportato fedelmente)

**Archi** (p. 31):
```c
typedef struct edgenode {
    int y;                    /* adjacency info */
    int weight;               /* edge weight, if any */
    struct edgenode *next;    /* next edge in list */
} edgenode;
```

**Grafo** ([[08-Grafi e alberi.pdf#page=32|p. 32]]):
```c
typedef struct {
    edgenode *edges[MAXV+1];  /* adjacency info */
    int degree[MAXV+1];       /* outdegree of each vertex */
    int nvertices;            /* number of vertices in the graph */
    int nedges;               /* number of edges in the graph */
    int directed;             /* is the graph directed? */
} graph;
```

Il campo `degree` conta il numero di voci significative per il vertice dato. Un arco non orientato $(x, y)$ compare **due volte** in qualunque struttura basata sull'adiacenza: una volta come $y$ nella lista di $x$ e una volta come $x$ nella lista di $y$.

**Inizializzazione** ([[08-Grafi e alberi.pdf#page=33|p. 33]]):
```c
void initialize_graph(graph *g, bool directed) {
    int i;                    /* counter */
    g->nvertices = 0;
    g->nedges = 0;
    g->directed = directed;
    for (i = 1; i <= MAXV; i++) {
        g->degree[i] = 0;
    }
    for (i = 1; i <= MAXV; i++) {
        g->edges[i] = NULL;
    }
}
```

**Lettura** ([[08-Grafi e alberi.pdf#page=34|p. 34]]): un formato tipico ha una prima riga con il numero di vertici e di archi, seguita dall'elenco degli archi, una coppia di vertici per riga.
```c
void read_graph(graph *g, bool directed) {
    int i;                    /* counter */
    int m;                    /* number of edges */
    int x, y;                 /* vertices in edge (x,y) */
    initialize_graph(g, directed);
    scanf("%d %d", &(g->nvertices), &m);
    for (i = 1; i <= m; i++) {
        scanf("%d %d", &x, &y);
        insert_edge(g, x, y, directed);
    }
}
```

**Inserimento di un arco** (p. 35):
```c
void insert_edge(graph *g, int x, int y, bool directed) {
    edgenode *p;              /* temporary pointer */
    p = malloc(sizeof(edgenode));   /* allocate edgenode storage */
    p->weight = 0;
    p->y = y;
    p->next = g->edges[x];
    g->edges[x] = p;          /* insert at head of list */
    g->degree[x]++;
    if (!directed) {
        insert_edge(g, y, x, true);
    } else {
        g->nedges++;
    }
}
```

> 🧩 Come funziona `insert_edge`: il nuovo nodo viene messo **in testa** alla lista di $x$ (due assegnamenti di puntatori, come l'inserimento in testa di [[lista-concatenata]]). Se il grafo non è orientato, la funzione **richiama sé stessa** con i ruoli scambiati e `directed = true`, per inserire la seconda copia $x$ nella lista di $y$. Il contatore `nedges` viene incrementato una sola volta, nella chiamata «orientata»: un arco non orientato conta come un solo arco pur occupando due nodi.

## Esempio di esecuzione

![[animazione-liste-di-adiacenza.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero `insert_edge` sui 7 archi del grafo di p. 28, nell'ordine (1,2), (1,5), (2,3), (2,4), (2,5), (3,4), (4,5). Per ogni arco si vedono i due nodi inseriti in testa (in giallo) e i gradi aggiornati. L'ordine dei nodi nelle liste dipende dall'ordine di inserimento: per questo può differire dalla figura della slide.

## Costo delle operazioni

> 🧩 Derivazione mia:
> - `initialize_graph`: due cicli di `MAXV` iterazioni ⇒ $\Theta(\texttt{MAXV})$, cioè $\Theta(n)$ se `MAXV` è dell'ordine di $n$;
> - `insert_edge`: numero costante di assegnamenti, più al più una chiamata ricorsiva che non ne fa altre ⇒ $O(1)$;
> - `read_graph`: inizializzazione più $m$ chiamate a `insert_edge` a costo costante ⇒ $\Theta(\texttt{MAXV} + m)$.

## Connessioni

- [[matrice-di-adiacenza]] — l'altra rappresentazione
- [[lista-concatenata]] — ogni lista è una lista concatenata con inserimento in testa
- [[grafo]] — somma dei gradi $= 2m$, da cui lo spazio $\Theta(n + m)$
- [[tipi-di-grafo]] — sui grafi sparsi le liste sono la scelta naturale

## Fonti

- [[lezione-08-grafi-e-alberi]]
- [[08-Grafi e alberi.pdf#page=28]]–[[08-Grafi e alberi.pdf#page=36]]

_Aggiornato: 2026-10-28 — ingest 08-Grafi e alberi.pdf_

<!-- nav:inizio -->
---
**Lezione 08 · pagina 5 di 6** · ← [[matrice-di-adiacenza|Matrice di adiacenza]] · [[lezioni|Indice]] · [[albero|Albero]] →
<!-- nav:fine -->
