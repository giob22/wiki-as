---
tipo: entità
categoria: struttura-dati
fonti_pdf: ["09-Alberi binari ricerca.pdf#page=2", "09-Alberi binari ricerca.pdf#page=3", "09-Alberi binari ricerca.pdf#page=4", "09-Alberi binari ricerca.pdf#page=5"]
---

# Coda di priorità

## Cos'è

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=2]], [[09-Alberi binari ricerca.pdf#page=4]]

Le code di priorità sono strutture dati che offrono una **flessibilità in più rispetto all'ordinamento**. È importante perché i lavori (*job*) entrano spesso in un sistema a intervalli arbitrari: è più conveniente inserire un nuovo job in una coda di priorità che riordinare tutto a ogni nuovo arrivo (p. 2).

Nella teoria delle code, una coda di priorità è una **struttura dati astratta** (→ [[tipo-di-dato-astratto]]), simile a una [[coda]] o a una [[pila]], ma diversa perché ogni elemento inserito possiede una sua **priorità** (p. 4):
- un elemento con priorità più alta viene posto prima di un elemento con priorità più bassa;
- l'elemento con priorità più alta si trova in **testa** alla coda, quello con priorità più bassa in **fondo**.

![[09-alberi-binari-ricerca-p2-code-priorita.png]]

## Operazioni

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=3]]

La coda di priorità di base supporta tre operazioni principali:
- **Insert($Q$, $x$)**: dato un elemento $x$ con chiave $k$, lo inserisce nella coda di priorità $Q$;
- **Find-Minimum($Q$)** o **Find-Maximum($Q$)**: restituisce un puntatore all'elemento la cui chiave è più piccola (più grande) di ogni altra chiave in $Q$;
- **Delete-Minimum($Q$)** o **Delete-Maximum($Q$)**: rimuove da $Q$ l'elemento con chiave minima (massima).

![[09-alberi-binari-ricerca-p3-operazioni-coda-priorita.png]]

## Esempio

> 📄 Fonte: [[09-Alberi binari ricerca.pdf#page=5]] («Implementation of Priority Queue»)

Input 1, 5, 3, 2, 6, dove un numero più alto ha priorità più alta. La coda è tenuta come sequenza **ordinata per priorità decrescente**:

| Operazione | Contenuto della coda (pq) |
|------------|---------------------------|
| enqueue(1) | 1 |
| enqueue(5) | 5, 1 |
| enqueue(3) | 5, 3, 1 |
| enqueue(2) | 5, 3, 2, 1 |
| enqueue(6) | 6, 5, 3, 2, 1 |

![[09-alberi-binari-ricerca-p5-implementazione-coda-priorita.png]]

## Costo delle operazioni

> 🧩 Derivazione mia per l'implementazione dell'esempio, un [[array]] ordinato con $n$ elementi:
> - **Insert:** bisogna trovare la posizione e spostare di un posto tutti gli elementi meno prioritari, come nel ciclo interno di [[insertion-sort]]: $O(n)$ nel caso peggiore;
> - **Find-Maximum:** l'elemento più prioritario è in testa: $O(1)$;
> - **Delete-Maximum:** $O(1)$ se l'array è tenuto in ordine crescente e si toglie l'ultimo elemento; con l'ordine decrescente della slide (massimo in posizione 1) bisognerebbe spostare tutti gli altri, $O(n)$.
>
> Gli [[albero-binario-di-ricerca|alberi binari di ricerca]] possono essere usati anche come coda di priorità ([[09-Alberi binari ricerca.pdf#page=6]]): Find-Minimum e Find-Maximum sono [[tree-minimum-maximum|Tree-Minimum e Tree-Maximum]], Insert è [[tree-insert|Tree-Insert]], Delete-Minimum è una ricerca del minimo seguita da [[tree-delete|Tree-Delete]], tutte in $O(h)$.

## Connessioni

- [[coda]], [[pila]] — le strutture a cui la slide la paragona
- [[tipo-di-dato-astratto]] — le operazioni sono quelle del tipo astratto, l'implementazione può cambiare
- [[albero-binario-di-ricerca]] — un'implementazione con operazioni $O(h)$
- [[ordinamento]] — una coda di priorità evita di riordinare a ogni inserimento

## Fonti

- [[lezione-09-alberi-binari-di-ricerca]]
- [[09-Alberi binari ricerca.pdf#page=2]]–[[09-Alberi binari ricerca.pdf#page=5]]

_Aggiornato: 2026-10-28 — ingest 09-Alberi binari ricerca.pdf_

<!-- nav:inizio -->
---
**Lezione 09 · pagina 2 di 9** · ← [[lezione-09-alberi-binari-di-ricerca|Lezione 09: introduzione e riepilogo]] · [[lezioni|Indice]] · [[albero-binario-di-ricerca|Albero binario di ricerca (BST)]] →
<!-- nav:fine -->
