---
tipo: concetto
importanza_esame: alta
prerequisiti: ["tipo-di-dato-astratto"]
fonti_pdf: ["04-Strutture dati elementari.pdf#page=5", "04-Strutture dati elementari.pdf#page=8", "04-Strutture dati elementari.pdf#page=15", "04-Strutture dati elementari.pdf#page=21"]
---

# Strutture dati contigue e collegate (e puntatori)

## Definizione · 04-Strutture dati elementari.pdf [[04-Strutture dati elementari.pdf#page=5|p. 5]], [[04-Strutture dati elementari.pdf#page=15|p. 15]] · Pseudocodice [[a1-indicazioni_psuedocodice.pdf#page=3|p. 3]]

> 📄 Fonte: p. 5 — *Contiguous vs. Linked Data Structures*

Le strutture dati si classificano nettamente come **contigue** o **collegate**, a seconda che siano basate su **array** o su **puntatori**:
- le strutture **allocate in modo contiguo** sono composte da **singoli blocchi di memoria** e comprendono array, matrici, heap e tabelle hash;
- le strutture **collegate** sono composte da **più blocchi distinti** di memoria legati tra loro da **puntatori**, e comprendono liste, alberi e liste di adiacenza dei grafi.

> 📄 Fonte: p. 15 — *Pointers and Linked Structures*

- I **puntatori** rappresentano l'**indirizzo** di una locazione di memoria.
- Un numero di cellulare può essere visto come un puntatore al suo proprietario mentre si sposta per il pianeta.
- In C, `*p` indica l'elemento puntato da `p` e `&x` indica l'indirizzo (cioè il puntatore) di una variabile `x`.
- Un valore speciale `NULL` indica puntatori che terminano una struttura o non assegnati.

Nello [[pseudocodice]] del corso il puntatore nullo si chiama `NIL` e ogni variabile di tipo aggregato è un puntatore alla struttura.

## Spiegazione · [[04-Strutture dati elementari.pdf#page=8|p. 8]], [[04-Strutture dati elementari.pdf#page=10|p. 10]], [[04-Strutture dati elementari.pdf#page=21|p. 21]], [[04-Strutture dati elementari.pdf#page=22|22]]

Confronto tra le due famiglie, ricavato dalle slide:

| Aspetto | Contigue ([[array]]) | Collegate ([[lista-concatenata]]) |
|---|---|---|
| Accesso all'elemento $i$-esimo | tempo costante dato l'indice | scorrimento dalla testa |
| Spazio | solo dati, nessun collegamento | dati + puntatori (il doppio con le liste doppie) |
| Località / cache | continuità fisica → sfrutta la cache | blocchi sparsi |
| Overflow | dimensione fissa (salvo array dinamici) | mai, finché la memoria non è davvero piena |
| Inserimenti/cancellazioni | bisogna spostare gli elementi successivi | più semplici: si ricollegano solo i puntatori (ma dipende dall'operazione, vedi sotto) |
| Record grandi | si spostano i dati | spostare puntatori è più facile e veloce |

> 📄 Fonte: p. 21 — *Advantages of Linked Lists* (rispetto agli array statici)
1. L'overflow sulle strutture collegate non può mai avvenire a meno che la memoria sia effettivamente piena.
2. Nelle liste collegate inserimenti e cancellazioni sono **più semplici** che nelle liste contigue (array). La slide dice «Insertions and deletions are *simpler* than for contiguous (array) lists»: il soggetto sono le liste collegate, quindi il vantaggio è della lista, non dell'array.
3. Con record grandi, spostare puntatori è più facile e veloce che spostare gli elementi stessi.

«Dynamic memory allocation provides us with flexibility on how and where we use our limited storage resources.»

### «Più semplice» dipende dall'operazione · [[04-Strutture dati elementari.pdf#page=11|p. 11]], [[04-Strutture dati elementari.pdf#page=17|p. 17]], [[04-Strutture dati elementari.pdf#page=20|p. 20]], [[04-Strutture dati elementari.pdf#page=22|p. 22]], [[04-Strutture dati elementari.pdf#page=28|p. 28]]

> 🧩 Derivazione mia, a partire dai costi dati nelle slide. La slide afferma il vantaggio in generale, ma quanto è vero dipende dal **tipo** di inserimento o cancellazione e dall'**implementazione** (lista semplice o doppia, con o senza puntatore alla coda, array statico o dinamico).
>
> «Più semplice» nella slide vuol dire che nella lista **non bisogna spostare gli altri elementi**: basta ricollegare due o tre puntatori. Non vuol dire sempre «più veloce»: se prima bisogna **trovare** il punto giusto, lo scorrimento della lista costa $\Theta(n)$.

| Operazione | Array | Lista concatenata | Chi vince |
|---|---|---|---|
| Inserimento **in testa** (push front) | $\Theta(n)$: tutti gli elementi scorrono di un posto | $\Theta(1)$: `insert_list` | lista |
| Inserimento **in coda** (push_back) | array statico: $\Theta(1)$ se c'è spazio, altrimenti overflow; [[array-dinamico]]: $O(1)$ in media, perché $n$ inserimenti costano $O(n)$ in totale | $\Theta(n)$ senza puntatore alla coda (bisogna arrivare in fondo); $\Theta(1)$ con puntatore alla coda, come nella [[coda]] | pari, se la lista tiene il puntatore alla coda |
| Inserimento **in posizione $i$** (insert) | $\Theta(n - i)$ spostamenti | $\Theta(1)$ per ricollegare, **se** si ha già il puntatore al nodo precedente; altrimenti $\Theta(i)$ per raggiungerlo | lista solo se la posizione è già nota |
| **Cancellazione** di un nodo dato | $\Theta(n - i)$ spostamenti per chiudere il buco | lista semplice: $\Theta(n)$ nel caso peggiore, per cercare il predecessore; lista doppia: $\Theta(1)$ | lista doppia |
| Push/Pop di una **pila** | $\Theta(1)$ in fondo all'array | $\Theta(1)$ in testa alla lista | pari |

> Regola pratica: la lista vince quando si inserisce o cancella **dove si ha già un puntatore** (la testa, o un nodo appena trovato). L'array vince quando serve accedere per **indice**, e con il raddoppio regge bene anche gli inserimenti in fondo. La slide si riferisce agli **array statici** (titolo «Advantages of Linked Lists … over static arrays»): contro un array dinamico il vantaggio del punto 1 (overflow) si riduce.

## Perché importa

La scelta contigua/collegata è la prima decisione implementativa per ogni [[tipo-di-dato-astratto]]: determina il costo delle operazioni.

> 🎯 Esame: vantaggi e svantaggi di array e liste; esempi di strutture di ciascuna famiglia.

## Connessioni

- [[array]], [[array-dinamico]], [[lista-concatenata]]
- [[modello-ram]] — il vantaggio di cache degli array è fuori dal modello (niente gerarchie di memoria)
- [[pila]], [[coda]] — implementabili in entrambe le famiglie

## Fonti · [[04-Strutture dati elementari.pdf#page=5|p. 5]], [[04-Strutture dati elementari.pdf#page=14|p. 14]], [[04-Strutture dati elementari.pdf#page=15|15]], [[04-Strutture dati elementari.pdf#page=21|p. 21]]

- [[lezione-04-strutture-dati-elementari]]

_Aggiornato: 2026-09-26 — ingest 04-Strutture dati elementari.pdf_
_Aggiornato: 2026-09-30 — chiarito il punto 2 di p. 21 (vantaggio della lista, non dell'array); aggiunta la tabella dei costi per tipo di inserimento/cancellazione_

<!-- nav:inizio -->
---
**Lezione 04 · pagina 3 di 9** · ← [[tipo-di-dato-astratto|Astrazione dei dati (operazioni astratte vs implementazione)]] · [[lezioni|Indice]] · [[array|Array]] →
<!-- nav:fine -->
