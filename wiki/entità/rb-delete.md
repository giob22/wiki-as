---
tipo: entità
categoria: algoritmo
paradigma: "cancellazione come in un BST seguita da una correzione locale (fixup)"
fonti_pdf: ["11 . Alberi rosso-neri.pdf#page=42", "11 . Alberi rosso-neri.pdf#page=43", "11 . Alberi rosso-neri.pdf#page=44", "11 . Alberi rosso-neri.pdf#page=48"]
---

# RB-Delete e RB-Delete-Fixup

## Problema risolto · [[11 . Alberi rosso-neri.pdf#page=42|p. 42]]

Eliminare il nodo $z$ da un [[albero-rosso-nero]] mantenendo le cinque proprietà.

## Idea · [[11 . Alberi rosso-neri.pdf#page=42|p. 42]]

La cancellazione si basa sull'algoritmo [[tree-delete]] dei normali BST, con alcune modifiche. Come nell'inserimento, può servire ripristinare le proprietà rosso-nere:
- se il nodo **fisicamente rimosso è rosso**, le proprietà restano valide;
- se è **nero**, si invoca **RB-Delete-Fixup**, che ripristina le proprietà con eventuali ricolorazioni e rotazioni.

> 📄 Le slide non danno lo pseudocodice di RB-Delete né di RB-Delete-Fixup, solo questa descrizione e i tre esempi di pp. 45–47 (nessuno dei quali richiede il fixup). Il pseudocodice della parte strutturale è quello di [[tree-delete]], da cui RB-Delete parte.

> ❓ Salto non ricostruito: i casi di RB-Delete-Fixup (come si ripristina la black-height dopo la rimozione di una foglia nera) non sono nelle slide. Non li ricostruisco qui; lo svolgimento è nel Cormen (📚 Fonte esterna: Cormen et al., *Introduzione agli algoritmi e strutture dati*, 3ª ed., cap. 13 «Alberi rosso-neri», §13.4 «Cancellazione», da verificare sul testo).

## Casi · [[11 . Alberi rosso-neri.pdf#page=43|p. 43]], [[11 . Alberi rosso-neri.pdf#page=44|44]]

La cancellazione segue inizialmente le regole di un BST: si distingue se $z$ ha **zero, uno o due figli**. Le proprietà degli alberi rosso-neri permettono però alcune osservazioni (p. 43):
- un nodo **rosso** può essere una foglia oppure avere due figli, necessariamente neri;
- non può avere un solo figlio, altrimenti sarebbe violata la proprietà 5 (black-height);
- se $z$ ha due figli, si individua il suo **successore**, che ha al massimo un figlio ([[tree-successor]]).

Pertanto **il nodo fisicamente rimosso ha sempre al massimo un figlio**. A questo punto i casi effettivi sono tre (p. 44):
1. si elimina una **foglia rossa**: l'albero resta rosso-nero (non cambia la black-height, non si creano nodi rossi consecutivi, la radice resta nera);
2. si elimina un **nodo nero con un unico figlio rosso**: il figlio prende il suo posto e viene colorato di nero; le proprietà sono preservate;
3. si elimina una **foglia nera**: la black-height diminuisce lungo alcuni cammini, quindi occorre RB-Delete-Fixup.

![[11-alberi-rosso-neri-p43-cancellazione-casi.png]]

> 🧩 Derivazione mia: perché un nodo rosso non può avere un solo figlio. Sia $r$ rosso con un solo figlio $c$ (l'altro è NIL). Per la proprietà 4 $c$ è nero. Il cammino da $r$ attraverso il figlio NIL ha un solo nodo nero (il NIL); quello attraverso $c$ ne ha almeno due ($c$ e il NIL sotto $c$). Per la proprietà 5 devono essere uguali: contraddizione.

## Esempio di esecuzione · [[11 . Alberi rosso-neri.pdf#page=45|p. 45]]–[[11 . Alberi rosso-neri.pdf#page=47|47]]

![[animazione-rb-delete.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) sull'albero rosso-nero di p. 45, eseguendo la modifica dell'albero nei tre casi delle slide. Il caso della foglia nera, che richiede RB-Delete-Fixup, non è sviluppato nelle slide e compare solo come ultimo fotogramma.

Le slide mostrano il primo fotogramma di tre animazioni, sullo stesso albero (15 nero; 6 e 18 rossi; 3, 7, 17 e 20 neri; 2, 4, 13 e 19 rossi), con le didascalie: «Caso I — eliminare una foglia: scegliamo $z = 19$» (p. 45), «Caso II — un solo figlio: scegliamo $z = 20$ (nero)» (p. 46), «Caso III — due figli: scegliamo $z = 18$: ha due figli» (p. 47).

![[11-alberi-rosso-neri-p45-cancellazione-foglia.png]]
![[11-alberi-rosso-neri-p46-cancellazione-un-figlio.png]]
![[11-alberi-rosso-neri-p47-cancellazione-due-figli.png]]

Tracce mie (🧩), verificate con [[alberi_rosso_neri.py]] (nessuna richiede rotazioni):

| Caso | $z$ | Nodo rimosso fisicamente | Azione | Risultato |
|---|---|---|---|---|
| I | 19 (foglia rossa) | 19, rosso | si toglie; nulla da correggere | albero rosso-nero, $bh = 2$ |
| II | 20 (nero, figlio 19 rosso) | 20, nero | 19 prende il posto di 20 e diventa nero | albero rosso-nero, $bh = 2$ |
| III | 18 (rosso, due figli) | successore 19, foglia rossa | si toglie 19 e la sua chiave va nel nodo di 18 (rosso) | albero rosso-nero, il figlio destro di 15 è ora 19 (rosso) |

## Correttezza · [[11 . Alberi rosso-neri.pdf#page=44|p. 44]]

> 🧩 Derivazione mia dei casi 1 e 2 (il caso 3 richiede il fixup, non svolto nelle slide):
> - **Foglia rossa tolta:** nessun percorso perde un nodo nero (il rosso non conta), il padre non può essere rosso con un figlio rosso (non si creano nodi), e la radice non cambia se $z$ è rosso (la radice è nera).
> - **Nero con un figlio rosso:** il figlio $c$ (rosso) prende il posto di $z$ (nero) e viene colorato di nero: i cammini che passavano per $z$ contavano un nero ($z$) e ora ne contano uno ($c$); il padre di $z$ non ha un figlio rosso in più, quindi non si crea una violazione della proprietà 4 (se il padre è rosso, il nuovo figlio nero la rispetta).

## Complessità · [[11 . Alberi rosso-neri.pdf#page=48|p. 48]]

RB-Delete-Fixup è diverso da RB-Insert-Fixup: quest'ultimo corregge principalmente la presenza di **due nodi rossi consecutivi**, RB-Delete-Fixup lo **squilibrio della black-height** provocato dall'eliminazione di un nodo nero. Entrambi usano rotazioni e ricolorazioni, ma gestiscono situazioni diverse.

![[11-alberi-rosso-neri-p48-rb-delete-fixup.png]]

Complessità (slide): la ricerca e l'eliminazione strutturale richiedono $O(h)$; anche RB-Delete-Fixup richiede $O(h)$ nel caso peggiore; poiché un albero rosso-nero ha altezza $h = O(\log n)$, l'intera cancellazione richiede $O(\log n)$.

$$
T(n) = \underbrace{O(h)}_{\text{ricerca e taglio come Tree-Delete}} + \underbrace{O(h)}_{\text{RB-Delete-Fixup}} = O(h) = O(\lg n) \qquad \text{perché } h \le 2\lg(n+1)
$$

**Ipotesi:** costo costante per ricolorazione e rotazione; l'altezza logaritmica dipende dal teorema di [[albero-rosso-nero]].

## Connessioni

- [[tree-delete]] — la parte strutturale (con le modifiche descritte)
- [[tree-successor]] — individua il nodo da tagliare con due figli
- [[rb-insert]] — il fixup dell'inserimento, che corregge due rossi consecutivi
- [[left-rotate]] — le rotazioni del fixup
- [[albero-rosso-nero]] — le proprietà da preservare

## Fonti · [[11 . Alberi rosso-neri.pdf#page=42|p. 42]]–[[11 . Alberi rosso-neri.pdf#page=48|48]]

- [[lezione-11-alberi-rosso-neri]]

_Aggiornato: 2026-11-26 — ingest 11 . Alberi rosso-neri.pdf_

<!-- nav:inizio -->
---
**Lezione 11 · pagina 5 di 5** · ← [[rb-insert|RB-Insert e RB-Insert-Fixup]] · [[lezioni|Indice]] · [[lezione-12-alberi-auto-aggiustanti|Lezione 12: introduzione e riepilogo]] →
<!-- nav:fine -->
