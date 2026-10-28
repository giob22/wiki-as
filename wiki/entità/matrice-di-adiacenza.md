---
tipo: entità
categoria: struttura-dati
fonti_pdf: ["08-Grafi e alberi.pdf#page=26", "08-Grafi e alberi.pdf#page=27", "08-Grafi e alberi.pdf#page=30"]
---

# Matrice di adiacenza

## Cos'è

> 📄 Fonte: [[08-Grafi e alberi.pdf#page=26]]

Ci sono due strutture dati principali per rappresentare i grafi: la matrice di adiacenza e le [[liste-di-adiacenza]]. Si assume che il grafo $G = (V, E)$ abbia $n$ vertici e $m$ archi.

Si può rappresentare $G$ con una matrice $M$ di dimensione $n \times n$, in cui l'elemento $M[i, j]$ vale, ad esempio, **1** se $(i, j)$ è un arco di $G$ e **0** se non lo è. Può però usare uno spazio eccessivo per grafi con molti vertici e relativamente pochi archi.

La slide chiede: si può risparmiare spazio (1) se il grafo è **non orientato**? (2) se il grafo è **sparso**? (risposte sotto).

## Appunti a mano della lezione

> 📄 Fonte: [[08-Grafi e alberi.pdf#page=27]] (pagina a righe con soli appunti scritti a mano)

- «Dobbiamo poter mantenere le informazioni degli archi, poiché su queste si basano le proprietà dei grafi».
- «Posso avere più nodi che archi → grafo non connesso».
- «Matrice come bitmap per memorizzare le interconnessioni», con l'esempio di una matrice $2 \times 2$ sui vertici $a$, $b$: riga $a$ = (0, 1), riga $b$ = (2, 0), dove il 2 è il «peso dell'arco». In rosso: «matrice di adiacenza».
- In verde: «con una matrice ho rappresentato l'intera struttura astratta del grafo → con una sola struttura dati».

![[08-grafi-e-alberi-p27-appunti-matrice.png]]

> ⚠️ Contraddizione (🧩, sul secondo appunto): avere meno archi che nodi non basta a dire che il grafo **non è connesso**. Un [[albero]] con $n$ nodi è connesso e ha $n - 1$ archi, cioè meno archi che nodi ([[08-Grafi e alberi.pdf#page=39]]). È vero che con **meno di $n - 1$** archi un grafo non può essere connesso: ogni arco aggiunto unisce al più due componenti, quindi partendo da $n$ vertici isolati servono almeno $n - 1$ archi per arrivare a una sola componente.

> 🧩 Nota sull'esempio della matrice: con un grafo **pesato** al posto di 1 si scrive il peso dell'arco ($M[b, a] = 2$), e la matrice non è simmetrica perché l'esempio è orientato ($M[a, b] = 1$, $M[b, a] = 2$).

## Rappresentazione in memoria e costi

> 🧩 Derivazione mia, dai costi confrontati in [[08-Grafi e alberi.pdf#page=30]] (tabella completa in [[liste-di-adiacenza]] § Confronto):

| Operazione | Costo | Perché |
|------------|-------|--------|
| spazio | $\Theta(n^2)$ | una cella per ogni coppia ordinata di vertici, archi presenti o no |
| test «$(x, y)$ è un arco?» | $O(1)$ | accesso diretto a $M[x, y]$ (array bidimensionale, → [[array]]) |
| inserimento o cancellazione di un arco | $O(1)$ | si scrive 1 o 0 in $M[x, y]$ |
| grado di un vertice | $\Theta(n)$ | si scorre l'intera riga |
| visita di tutto il grafo | $\Theta(n^2)$ | per trovare i vicini di ogni vertice si scorrono tutte le $n$ righe di $n$ celle |

**Risposte alle domande di p. 26** (🧩):
1. **Grafo non orientato:** $M$ è **simmetrica** ($M[i, j] = M[j, i]$), quindi basta memorizzare il triangolo superiore, diagonale compresa: $\frac{n(n+1)}{2}$ celle invece di $n^2$, cioè circa la metà. L'ordine resta $\Theta(n^2)$.
2. **Grafo sparso:** quasi tutte le celle valgono 0. Conviene memorizzare solo gli archi presenti, che è proprio ciò che fanno le [[liste-di-adiacenza]]: spazio $\Theta(n + m)$ invece di $\Theta(n^2)$.

**Sanity check** ([[grafi_e_alberi.py]]): per il grafo di p. 28 ($n = 5$, $m = 7$) la matrice ha 25 celle ed è simmetrica; per $n = 1000$ e $m = 3000$ servono $10^6$ celle contro le $n + 2m = 7000$ voci delle liste.

## Connessioni

- [[liste-di-adiacenza]] — l'altra rappresentazione e il confronto completo
- [[grafo]], [[tipi-di-grafo]] — sparso/denso, orientato/non orientato, pesato
- [[array]] — accesso diretto in tempo costante

## Fonti

- [[lezione-08-grafi-e-alberi]]
- [[08-Grafi e alberi.pdf#page=25]]–[[08-Grafi e alberi.pdf#page=27]], [[08-Grafi e alberi.pdf#page=30]]

_Aggiornato: 2026-10-28 — ingest 08-Grafi e alberi.pdf_

<!-- nav:inizio -->
---
**Lezione 08 · pagina 4 di 6** · ← [[tipi-di-grafo|Tipi di grafo («flavors of graphs»)]] · [[lezioni|Indice]] · [[liste-di-adiacenza|Liste di adiacenza]] →
<!-- nav:fine -->
