---
tipo: concetto
importanza_esame: alta
prerequisiti: ["tipo-di-dato-astratto"]
fonti_pdf: ["08-Grafi e alberi.pdf#page=3", "08-Grafi e alberi.pdf#page=4", "08-Grafi e alberi.pdf#page=5", "08-Grafi e alberi.pdf#page=6", "08-Grafi e alberi.pdf#page=18", "08-Grafi e alberi.pdf#page=19", "08-Grafi e alberi.pdf#page=20", "08-Grafi e alberi.pdf#page=21", "08-Grafi e alberi.pdf#page=22", "08-Grafi e alberi.pdf#page=23"]
---

# Grafo

Le sezioni seguono le slide: definizione ed esempi (pp. 2–7), poi la terminologia introdotta con il grafo delle amicizie (pp. 17–24). I tipi di grafo (pp. 8–16) sono in [[tipi-di-grafo]].

## Definizione · [[08-Grafi e alberi.pdf#page=3|p. 3]], [[08-Grafi e alberi.pdf#page=26|p. 26]]

I grafi sono uno dei temi unificanti dell'informatica. Un **grafo** $G = (V, E)$ è definito da un insieme di **vertici** $V$ e da un insieme di **archi** $E$, formato da coppie **ordinate** o **non ordinate** di vertici di $V$.

Annotazione a mano sulla slide: il grafo è uno «strumento per formalizzare problemi, mantenere informazioni».

Simboli usati nelle slide successive: $n = |V|$ numero di vertici, $m = |E|$ numero di archi.

## Esempi di modellazione · [[08-Grafi e alberi.pdf#page=4|p. 4]]–[[08-Grafi e alberi.pdf#page=6|6]]

- **Reti stradali** (p. 4): i vertici rappresentano città o incroci, alcune coppie dei quali sono collegate da strade (gli archi). La figura mostra 8 località di Long Island: Stony Brook, Greenport, Orient Point, Riverhead, Shelter Island, Islip, Sag Harbor, Montauk.
- **Circuiti elettronici**: le giunzioni sono i vertici, i componenti sono gli archi.
- **Altri grafi e reti** (p. 6): reti sociali, il World Wide Web, il flusso di controllo di un programma, le similarità a coppie tra oggetti.

![[08-grafi-e-alberi-p4-rete-stradale.png]]
![[08-grafi-e-alberi-p5-circuito.png]]

## Terminologia: il grafo delle amicizie · [[08-Grafi e alberi.pdf#page=18|p. 18]]

Si considera il grafo in cui i vertici sono persone e c'è un arco tra due persone **se e solo se** sono amiche. È ben definito su qualunque insieme di persone (Stony Brook, New York, il mondo). Che domande ci si può porre su questo grafo? Ognuna introduce un concetto.

![[08-grafi-e-alberi-p18-grafo-amicizie.png]]
*Hermione Granger, Ron Weasley, Harry Potter e Dobby sono collegati; Voldemort è un vertice isolato, senza archi.*

| Domanda (slide) | Concetto | Definizione |
|---|---|---|
| «Se io sono tuo amico, tu sei mio amico?» ([[08-Grafi e alberi.pdf#page=19\|p. 19]]) | grafo **non orientato** / **orientato** | non orientato se $(x, y) \in E$ implica $(y, x) \in E$; altrimenti orientato |
| «Sono collegato a una celebrità da una catena di amici?» ([[08-Grafi e alberi.pdf#page=20\|p. 20]]) | **cammino** | sequenza di archi che collega due vertici |
| «C'è un cammino di amici tra due persone qualsiasi?» ([[08-Grafi e alberi.pdf#page=21\|p. 21]]) | grafo **connesso** / **fortemente connesso** | connesso se c'è un cammino tra due vertici qualsiasi; un grafo orientato è fortemente connesso se c'è un cammino orientato tra due vertici qualsiasi |
| «Chi ha più amici?» ([[08-Grafi e alberi.pdf#page=22\|p. 22]]) | **grado** | numero di archi adiacenti al vertice |
| «Qual è la cricca più grande?» (p. 23) | **cricca** (*clique*) | sottografo completo: ogni coppia dei suoi vertici è collegata da un arco |

Dettagli delle slide:
- p. 19: il grafo «ha sentito parlare di» è **orientato**, perché moltissime persone famose non hanno mai sentito parlare dell'autore; un grafo che richiede un partner è presumibilmente **non orientato**.
- p. 20: per impressionare qualcuno con la vicinanza al Presidente conviene dire che un membro del proprio club del libro lo conosce, piuttosto che spiegare come si è entrati nel club. Interessa quindi il **cammino minimo** tra due nodi. La figura collega Steve a Joe Biden passando per Mark Fasciano, Michael Ashner, Donald Trump e Steve Israel.
- p. 21: l'idea dei «sei gradi di separazione» presuppone che la rete sociale mondiale sia un grafo **connesso**.
- p. 23: una cricca sociale è un gruppo di amici reciproci che stanno insieme. Le cricche sono i sottografi **più densi possibile**; nel grafo delle amicizie ci si aspetta che le cricche grandi corrispondano a luoghi di lavoro, quartieri, organizzazioni religiose, scuole.

![[08-grafi-e-alberi-p20-cammino.png]]

## Formule · [[08-Grafi e alberi.pdf#page=28|p. 28]]

> 🧩 Derivazione mia (relazione tra gradi e archi, usata nelle [[liste-di-adiacenza]]): in un grafo non orientato ogni arco $(x, y)$ conta 1 nel grado di $x$ e 1 nel grado di $y$, quindi
$$ \sum_{v \in V} \text{grado}(v) = 2m $$
Verifica sul grafo di p. 28 ($n = 5$, $m = 7$): gradi 2, 4, 2, 3, 3, somma 14 $= 2 \cdot 7$ ([[grafi_e_alberi.py]]).

## Perché importa

I grafi sono la struttura con cui si formalizzano molti problemi: il [[robot-tour-optimization|commesso viaggiatore]] e i cammini minimi sono problemi su grafi. Prima di scegliere un algoritmo bisogna capire che tipo di grafo si ha ([[tipi-di-grafo]]) e come rappresentarlo in memoria ([[matrice-di-adiacenza]], [[liste-di-adiacenza]]).

> 🎯 Esame: definire grafo, cammino, grafo connesso e fortemente connesso, grado, cricca.

## Connessioni

- [[tipi-di-grafo]] — le caratteristiche che distinguono i grafi
- [[matrice-di-adiacenza]], [[liste-di-adiacenza]] — le due rappresentazioni
- [[albero]] — il grafo non orientato, connesso e aciclico
- [[robot-tour-optimization]] — il TSP è un problema su un grafo pesato

## Fonti · [[08-Grafi e alberi.pdf#page=2|p. 2]], [[08-Grafi e alberi.pdf#page=7|p. 7]], [[08-Grafi e alberi.pdf#page=17|p. 17]], [[08-Grafi e alberi.pdf#page=24|p. 24]]

- [[lezione-08-grafi-e-alberi]]

_Aggiornato: 2026-10-28 — ingest 08-Grafi e alberi.pdf_

<!-- nav:inizio -->
---
**Lezione 08 · pagina 2 di 6** · ← [[lezione-08-grafi-e-alberi|Lezione 08: introduzione e riepilogo]] · [[lezioni|Indice]] · [[tipi-di-grafo|Tipi di grafo («flavors of graphs»)]] →
<!-- nav:fine -->
