---
tipo: entità
categoria: algoritmo
paradigma: "ricorsione lungo i predecessori"
fonti_pdf: ["13 - Algoritmi di visita di un grafo.pdf#page=22", "13 - Algoritmi di visita di un grafo.pdf#page=23"]
---

# Print-Path

## Problema risolto · [[13 - Algoritmi di visita di un grafo.pdf#page=22|p. 22]]

Stampare i vertici lungo uno **shortest path da $s$ a $y$** (nella slide, $y$ è il vertice evidenziato; il parametro generale è $v$), **assumendo di aver eseguito [[visita-in-ampiezza|BFS]] in precedenza**: l'algoritmo legge i predecessori $\pi$ calcolati dalla BFS.

## Idea · [[13 - Algoritmi di visita di un grafo.pdf#page=22|p. 22]]

Il percorso dalla sorgente al vertice si ricostruisce risalendo i predecessori, da $v$ a $s$ (la **ricorsione va verso $s$**); la stampa avviene al ritorno delle chiamate, quindi in ordine **da $s$ a $v$**. Se $\pi[v]$ è NIL (e $v \ne s$) il vertice non è stato raggiunto: il percorso non esiste.

## Pseudocodice · [[13 - Algoritmi di visita di un grafo.pdf#page=22|p. 22]]

```
Print-Path (G,s,v)
1  if v = s
2      then print s
3      else if π[v] = NIL
4          then print "no path from s to v exists"
5          else Print-Path (G,s,π[v])
6               print v
```

> ⚠️ Contraddizione (refuso di impaginazione): nel testo estratto dal PDF le righe compaiono in ordine mescolato; l'ordine qui sopra è quello della figura (p. 22, con il grafo $r, s, t, u, v, w, x, y$ e le legende «ricorsione: verso $s$» e «stampa: da $s$»). Le pp. 22 e 23 hanno lo stesso contenuto.

![[13-visite-grafi-p22-print-path.png]]

## Esempio di esecuzione · [[13 - Algoritmi di visita di un grafo.pdf#page=22|p. 22]]

![[animazione-print-path.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo Print-Path $(G, s, y)$ sull'albero BFS del grafo di p. 11, costruito da me ([[visita-in-ampiezza]]): la slide evidenzia $y$ ma non mostra i valori di $\pi$.

Traccia (verificata con [[visite_di_grafi.py]]), con $\pi[y] = x$, $\pi[x] = w$, $\pi[w] = s$:

| Chiamata | Cosa fa | Stampato |
|---|---|---|
| Print-Path (G,s,$y$) | $\pi[y] = x \ne$ NIL: chiama Print-Path (G,s,$x$) | |
| Print-Path (G,s,$x$) | chiama Print-Path (G,s,$w$) | |
| Print-Path (G,s,$w$) | chiama Print-Path (G,s,$s$) | |
| Print-Path (G,s,$s$) | $v = s$: stampa $s$ | $s$ |
| ritorno in $w$ | stampa $w$ | $s\ w$ |
| ritorno in $x$ | stampa $x$ | $s\ w\ x$ |
| ritorno in $y$ | stampa $y$ | $s\ w\ x\ y$ |

Per un vertice non raggiungibile ($z$ senza archi) si stampa «no path from s to v exists» (verificato).

## Correttezza · [[13 - Algoritmi di visita di un grafo.pdf#page=22|p. 22]]

> 🧩 Derivazione mia, per induzione sulla lunghezza $k$ del percorso nell'albero BFS da $s$ a $v$. *Base* ($k = 0$, $v = s$): stampa $s$. *Passo:* per ipotesi Print-Path (G,s,$\pi[v]$) stampa il percorso da $s$ a $\pi[v]$ (lunghezza $k - 1$); la riga 6 aggiunge $v$ in fondo. Per il teorema di [[visita-in-ampiezza]] questo è uno shortest path da $s$ a $v$.

## Complessità · [[13 - Algoritmi di visita di un grafo.pdf#page=22|p. 22]]

Il tempo di esecuzione è **lineare nel numero di vertici sul percorso** (slide). 🧩 Ogni chiamata ricorsiva sale di un predecessore e fa lavoro costante (due confronti e una stampa): se il percorso ha $k + 1$ vertici ci sono $k + 1$ chiamate, quindi $T = \Theta(k)$, cioè $O(V)$ nel caso peggiore.

## Connessioni

- [[visita-in-ampiezza]] — fornisce $\pi$
- [[visita-di-un-grafo]] — il contesto

## Fonti · [[13 - Algoritmi di visita di un grafo.pdf#page=22|p. 22]], [[13 - Algoritmi di visita di un grafo.pdf#page=23|23]]

- [[lezione-13-algoritmi-di-visita-di-un-grafo]]

_Aggiornato: 2026-11-26 — ingest 13 - Algoritmi di visita di un grafo.pdf_

<!-- nav:inizio -->
---
**Lezione 13 · pagina 4 di 7** · ← [[visita-in-ampiezza|Visita in ampiezza (BFS)]] · [[lezioni|Indice]] · [[visita-in-profondita|Visita in profondità (DFS)]] →
<!-- nav:fine -->
