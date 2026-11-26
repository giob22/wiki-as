---
tipo: entità
categoria: struttura-dati
fonti_pdf: ["11 . Alberi rosso-neri.pdf#page=2", "11 . Alberi rosso-neri.pdf#page=10", "11 . Alberi rosso-neri.pdf#page=14", "11 . Alberi rosso-neri.pdf#page=15", "11 . Alberi rosso-neri.pdf#page=17"]
---

# Albero rosso-nero

## Perché un heap non basta · [[11 . Alberi rosso-neri.pdf#page=2|p. 2]]–[[11 . Alberi rosso-neri.pdf#page=9|9]]

La lezione parte dai limiti delle due strutture viste prima:
- Un max-[[heap]] garantisce altezza logaritmica $h = \Theta(\log n)$ e permette di accedere al massimo, nella radice, in $O(1)$. Però non mantiene l'ordinamento delle chiavi tipico di un BST: non vale «sinistra < nodo < destra». Per cercare una chiave arbitraria bisogna, nel caso peggiore, esaminare tutti i nodi: $O(n)$ (p. 2).
- Esempio (p. 3): cercando la chiave 30, dal confronto con la radice non si può scegliere un solo sottoalbero, perché 30 potrebbe trovarsi sia nel sinistro sia nel destro. Un heap risolve il problema dell'altezza ma non permette ricerche efficienti di chiavi arbitrarie.

![[11-alberi-rosso-neri-p3-heap-ricerca.png]]

- Un [[albero-binario-di-ricerca|BST]] permette di cercare, inserire ed eliminare una chiave in tempo proporzionale all'altezza $h$ (p. 5). Ma se le chiavi sono inserite in ordine (1, 2, 3, …) il BST degenera in una [[lista-concatenata]]: l'altezza diventa $\Theta(n)$ e le operazioni costano $O(n)$ nel caso peggiore (p. 6).
- Domanda delle slide (p. 7): si possono «fondere» le idee di un BST e di un heap per ottenere una struttura che conservi l'ordinamento del BST ma garantisca altezza logaritmica anche nel caso peggiore?

Gli **alberi rosso-neri** servono a questo (p. 8): mantenere un insieme di chiavi ordinato su cui si fanno inserimenti, cancellazioni e ricerche in modo veloce, tempo $O(\log n)$, **garantito nel caso pessimo** (non solo «in media») e con un'implementazione facile da scrivere. Nei BST «puri» (p. 9) le operazioni percorrono un cammino dalla radice a una foglia, con costo circa l'altezza; inserendo chiavi già ordinate (1, 2, 3, 4, 5, …) l'albero diventa una lista, $h = n$, e i tempi sono $O(n)$ invece di $O(\log n)$.

![[11-alberi-rosso-neri-p8-motivazione.png]]

## Definizione · [[11 . Alberi rosso-neri.pdf#page=10|p. 10]]

Un albero rosso-nero è un albero di ricerca in cui ogni nodo ha un attributo addizionale $color$, che vale rosso o nero; i puntatori a NIL sono sostituiti da **nodi foglia esterni**. Devono valere le cinque proprietà:
1. ogni nodo è rosso o nero;
2. la radice è nera;
3. ogni nodo foglia esterno (NIL) è nero;
4. se un nodo è rosso, entrambi i suoi figli sono neri;
5. per ogni nodo, tutti i percorsi dal nodo alle foglie contengono lo stesso numero di nodi neri.

Gli alberi rosso-neri garantiscono che nessun percorso dalla radice a una foglia è lungo più del doppio di un altro percorso.

![[11-alberi-rosso-neri-p10-definizione.png]]

## Esempio e sentinella · [[11 . Alberi rosso-neri.pdf#page=11|p. 11]]–[[11 . Alberi rosso-neri.pdf#page=13|13]]

L'albero di p. 11 ha radice 26 (nera); 17 rosso e 41 nero; 14 e 21 neri, 30 rosso e 47 nero; 10 rosso, 16, 19, 23, 28 e 38 neri; 7 e 12 neri, 15, 20, 35 e 39 rossi; 3 rosso. Tutti i puntatori nulli sono foglie esterne NIL nere.

![[11-alberi-rosso-neri-p11-esempio-albero.png]]

Nell'implementazione (p. 12) c'è **una sola sentinella** $nil[T]$ al posto di tutte le foglie esterne: il suo colore è nero, gli altri attributi sono indifferenti. Per comodità di visualizzazione la sentinella si omette nelle figure (p. 13), come nelle animazioni di questo wiki.

![[11-alberi-rosso-neri-p12-sentinella.png]]

## Black-height · [[11 . Alberi rosso-neri.pdf#page=14|p. 14]]

La **black-height** $bh(x)$ di un nodo $x$ è il numero di nodi neri lungo un qualunque percorso da $x$ a una foglia, **escludendo $x$** e **includendo la foglia esterna**; la black-height di un albero è quella della radice. È una misura parziale (solo i neri), mentre l'altezza conta tutti i nodi. In un albero rosso-nero l'altezza è al massimo il doppio della black-height della radice, ma in generale non sono uguali:

$$
bh(x) \le h(x) \le 2 \cdot bh(x)
$$

![[11-alberi-rosso-neri-p14-black-height.png]]

> 🧩 Perché vale la catena di disuguaglianze: ogni nodo nero del percorso più lungo conta sia in $h$ sia in $bh$, quindi $bh(x) \le h(x)$ (senza nodi rossi vale l'uguaglianza); per la proprietà 4 due nodi rossi non possono essere consecutivi, quindi su un percorso da $x$ a una foglia (con $h(x)$ nodi, escluso $x$) i rossi sono al più quanto i neri, cioè $h(x) \le 2\, bh(x)$.

## Derivazioni · [[11 . Alberi rosso-neri.pdf#page=15|p. 15]], [[11 . Alberi rosso-neri.pdf#page=16|16]]

![[11-alberi-rosso-neri-p15-altezza-dimostrazione.png]]

### Derivazione — un sottoalbero di radice $x$ ha almeno $2^{bh(x)} - 1$ nodi interni · [[11 . Alberi rosso-neri.pdf#page=15|p. 15]]
**Fonte:** dimostrata per induzione sull'altezza di $x$ nella slide.
**Si parte da:** la definizione di black-height (sopra) e le proprietà 4 e 5.

- **Base** (altezza 0): $x$ è una foglia esterna, $bh(x) = 0$, e $2^{bh(x)} - 1 = 2^0 - 1 = 0$: il sottoalbero non contiene nodi interni.
- **Passo:** sia $x$ un nodo interno di altezza $> 0$, con due figli. Ciascun figlio ha black-height $bh(x)$ se è rosso, $bh(x) - 1$ se è nero (un figlio nero conta un nodo nero in meno a partire da lui). Poiché l'altezza dei figli è minore di quella di $x$, si applica l'ipotesi induttiva: ogni figlio ha almeno $2^{bh(x)-1} - 1$ nodi interni.

$$
\begin{aligned}
n_x &\ge \left(2^{bh(x)-1} - 1\right) + \left(2^{bh(x)-1} - 1\right) + 1 && \text{due figli} + \text{il nodo } x \text{ stesso} \\
    &= 2 \cdot 2^{bh(x)-1} - 2 + 1 = 2^{bh(x)} - 1 && \text{raccolgo}
\end{aligned}
$$

> 🧩 Il caso peggiore usato è quello in cui entrambi i figli sono neri, perché è quello con meno nodi: se un figlio è rosso ha $bh(x)$, quindi $2^{bh(x)} - 1 \ge 2^{bh(x)-1} - 1$ nodi interni, e la stima scritta è una maggiorazione valida (un limite inferiore più debole).

**Sanity check** ([[alberi_rosso_neri.py]]): per l'albero di p. 37 (8 nodi interni, $bh = 2$) vale $8 \ge 2^2 - 1 = 3$; dopo $n = 1023$ inserimenti ordinati $bh = 9$ e $2^9 - 1 = 511 \le 1023$.
**Ipotesi:** albero con le proprietà 1–5.

### Derivazione — Teorema: l'altezza è al più $2 \lg(n+1)$ · [[11 . Alberi rosso-neri.pdf#page=15|p. 15]], [[11 . Alberi rosso-neri.pdf#page=16|16]]
**Fonte:** «Un albero rosso-nero con $n$ nodi interni ha altezza al più $2 \lg(n+1)$», dimostrato nelle slide.
**Si parte da:** il lemma precedente, applicato alla radice, e la proprietà 4.

- Per la proprietà 4, almeno la metà dei nodi su ogni percorso dalla radice a una foglia, escludendo la radice, sono neri. Quindi la black-height della radice è almeno $h/2$, dove $h$ è l'altezza dell'albero ($h \le 2\, bh$).
- Il numero di nodi interni $n$ è almeno $2^{bh} - 1$ (lemma sulla radice).

$$
\begin{aligned}
n &\ge 2^{bh} - 1 \ge 2^{h/2} - 1 && \text{lemma, poi } bh \ge h/2 \\
n + 1 &\ge 2^{h/2} && \text{sommo 1 ai due membri} \\
\lg(n+1) &\ge h/2 && \text{logaritmo in base 2 (funzione crescente)} \\
h &\le 2 \lg(n+1) && \text{moltiplico per 2: la tesi}
\end{aligned}
$$

**Sanity check** ([[alberi_rosso_neri.py]], $n$ inserimenti ordinati): $n = 127$: altezza 12 $\le 2 \lg 128 = 14$; $n = 1023$: 18 $\le 20$; $n = 10000$: 24 $\le 26.58$. Un BST con le stesse chiavi inserite in ordine avrebbe altezza $n$.
**Ipotesi:** altezza contata in numero di nodi del percorso più lungo dalla radice a una foglia esterna; logaritmi in base 2.

## Operazioni

> 📄 Le query Minimum, Maximum, Successor e Predecessor richiedono tempo $O(\lg n)$ su un albero rosso-nero ([[11 . Alberi rosso-neri.pdf#page=17|p. 17]]); sono quelle del BST ([[tree-minimum-maximum]], [[tree-successor]], [[tree-search]]) e costano $O(h)$, con $h = O(\lg n)$ per il teorema precedente. Insert e Delete vanno invece **opportunamente riviste** per preservare le proprietà.

| Operazione | Pagina wiki | Costo |
|---|---|---|
| rotazione a sinistra / a destra | [[left-rotate]] | $O(1)$ |
| inserimento | [[rb-insert]] | $O(\lg n)$ |
| cancellazione | [[rb-delete]] | $O(\lg n)$ |
| ricerca, minimo, massimo, successore, predecessore | come nel BST | $O(\lg n)$ |

## Connessioni

- [[albero-binario-di-ricerca]] — la struttura di partenza, con altezza fino a $n$; il rosso-nero ne conserva l'ordine
- [[heap]] — l'altro albero bilanciato della lezione precedente, che però non permette ricerche efficienti
- [[albero]] — altezza e bilanciamento
- [[invariante-di-ciclo]] — la tecnica con cui si dimostrano i Fixup

## Fonti · [[11 . Alberi rosso-neri.pdf#page=2|p. 2]]–[[11 . Alberi rosso-neri.pdf#page=17|17]]

- [[lezione-11-alberi-rosso-neri]]

_Aggiornato: 2026-11-26 — ingest 11 . Alberi rosso-neri.pdf_

<!-- nav:inizio -->
---
**Lezione 11 · pagina 2 di 5** · ← [[lezione-11-alberi-rosso-neri|Lezione 11: introduzione e riepilogo]] · [[lezioni|Indice]] · [[left-rotate|Rotazioni (Left-Rotate e Right-Rotate)]] →
<!-- nav:fine -->
