---
tipo: concetto
importanza_esame: alta
prerequisiti: ["grafo"]
fonti_pdf: ["08-Grafi e alberi.pdf#page=8", "08-Grafi e alberi.pdf#page=9", "08-Grafi e alberi.pdf#page=10", "08-Grafi e alberi.pdf#page=11", "08-Grafi e alberi.pdf#page=12", "08-Grafi e alberi.pdf#page=13", "08-Grafi e alberi.pdf#page=14", "08-Grafi e alberi.pdf#page=15"]
---

# Tipi di grafo («flavors of graphs»)

## Definizione

> 📄 Fonte: [[08-Grafi e alberi.pdf#page=8]], [[08-Grafi e alberi.pdf#page=9]]

Il primo passo in ogni problema su grafi è capire **con che tipo di grafo** si ha a che fare: il tipo di grafo ha un grande impatto su quali algoritmi sono appropriati ed efficienti. Imparare il vocabolario («talk the talk») è parte importante del saperli usare («walk the walk»).

Annotazione a mano su p. 8: i grafi «permettono di rappresentare relazioni fra un dato e i suoi simili».

| Coppia | Definizione (slide) | Esempi (slide) | Pagina |
|--------|---------------------|----------------|--------|
| **orientato / non orientato** | $G$ è non orientato se $(x, y) \in E$ implica $(y, x) \in E$ | reti stradali **tra** città: non orientate; reti di strade **dentro** una città: quasi sempre orientate, per i sensi unici. La maggior parte dei grafi di interesse teorico è non orientata | [[08-Grafi e alberi.pdf#page=10\|p. 10]] |
| **pesato / non pesato** | nei grafi pesati a ogni arco (o vertice) è assegnato un valore numerico, il **peso** | gli archi di una rete stradale possono pesare quanto la lunghezza, il tempo di percorrenza o il limite di velocità; nei grafi non pesati non c'è distinzione di costo tra archi e vertici | [[08-Grafi e alberi.pdf#page=11\|p. 11]] |
| **semplice / non semplice** | un **cappio** (*self-loop*) è un arco $(x, x)$ con un solo vertice; un arco $(x, y)$ è un **multi-arco** se compare più di una volta. Un grafo senza queste strutture è **semplice** | «Sei amico di te stesso?» | [[08-Grafi e alberi.pdf#page=12\|p. 12]] |
| **sparso / denso** | sparso quando solo una piccola frazione delle possibili coppie di vertici ha un arco | i grafi sono di solito sparsi per vincoli applicativi: le reti stradali devono essere sparse per via degli incroci. Tipicamente i grafi densi hanno un numero **quadratico** di archi, quelli sparsi sono di dimensione **lineare** | [[08-Grafi e alberi.pdf#page=13\|p. 13]] |
| **ciclico / aciclico** | un grafo aciclico non contiene cicli. Gli **alberi** sono grafi non orientati, connessi e aciclici | i grafi orientati aciclici si chiamano **DAG**: compaiono nei problemi di scheduling, dove un arco orientato $(x, y)$ indica che $x$ deve avvenire prima di $y$ | [[08-Grafi e alberi.pdf#page=14\|p. 14]] |
| **immerso / topologico** | un grafo è **immerso** (*embedded*) se ai vertici e agli archi sono state assegnate posizioni geometriche | conta un disegno del grafo, come nelle reti stradali e nei circuiti? Esempi: TSP o cammino minimo su punti del piano; grafi a griglia e grafi planari | [[08-Grafi e alberi.pdf#page=15\|p. 15]] |

Annotazione a mano su p. 12: un grafo è «complesso» (cioè non semplice) se due nodi sono collegati direttamente con due archi diversi (l'ultima parola è di lettura incerta).

![[08-grafi-e-alberi-p10-orientato.png]]
![[08-grafi-e-alberi-p11-pesato.png]]
![[08-grafi-e-alberi-p12-non-semplice.png]]
![[08-grafi-e-alberi-p13-denso.png]]
![[08-grafi-e-alberi-p14-aciclico.png]]
![[08-grafi-e-alberi-p15-topologico.png]]

## Formule

### Derivazione — «denso = quadratico, sparso = lineare»
**Fonte:** [[08-Grafi e alberi.pdf#page=13]] (affermazione senza conteggio)

> 🧩 Derivazione mia: in un grafo **semplice** non orientato ogni arco è una coppia non ordinata di vertici distinti, quindi il numero massimo di archi è il numero di tali coppie:
$$
m_{\max} = \binom{n}{2} = \frac{n(n-1)}{2} = \Theta(n^2) \qquad \text{(orientato: } n(n-1)\text{ coppie ordinate)}
$$
> Un grafo **denso** ha $m = \Theta(n^2)$ archi, una frazione costante del massimo. Un grafo **sparso** ne ha $m = O(n)$: ad esempio in una rete stradale ogni incrocio ha pochi archi, il grado è limitato da una costante $g$, quindi $m = \frac{1}{2}\sum \text{grado} \le \frac{gn}{2}$ (→ [[grafo]] § Formule).

La distinzione decide la rappresentazione: con $m \ll n^2$ la [[matrice-di-adiacenza]] spreca spazio, le [[liste-di-adiacenza]] no ([[08-Grafi e alberi.pdf#page=26]], [[08-Grafi e alberi.pdf#page=30]]).

## Perché importa

> 🎯 Esame: riconoscere il tipo di grafo di un problema (orientato? pesato? denso?) e collegarlo alla scelta della struttura dati.

## Connessioni

- [[grafo]] — definizione e terminologia
- [[albero]] — il caso aciclico, connesso, non orientato
- [[matrice-di-adiacenza]], [[liste-di-adiacenza]] — sparso contro denso decide la rappresentazione

## Fonti

- [[lezione-08-grafi-e-alberi]]
- [[08-Grafi e alberi.pdf#page=8]]–[[08-Grafi e alberi.pdf#page=16]]

_Aggiornato: 2026-10-28 — ingest 08-Grafi e alberi.pdf_

<!-- nav:inizio -->
---
**Lezione 08 · pagina 3 di 6** · ← [[grafo|Grafo]] · [[lezioni|Indice]] · [[matrice-di-adiacenza|Matrice di adiacenza]] →
<!-- nav:fine -->
