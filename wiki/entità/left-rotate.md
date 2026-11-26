---
tipo: entità
categoria: algoritmo
paradigma: "ristrutturazione locale di puntatori"
fonti_pdf: ["11 . Alberi rosso-neri.pdf#page=18", "11 . Alberi rosso-neri.pdf#page=19", "11 . Alberi rosso-neri.pdf#page=20"]
---

# Rotazioni (Left-Rotate e Right-Rotate)

## Problema risolto · [[11 . Alberi rosso-neri.pdf#page=18|p. 18]]

Per preservare le proprietà di un [[albero-rosso-nero]] dopo un inserimento o una cancellazione si effettuano **rotazioni**: operazioni che cambiano la forma dell'albero in modo locale **preservando le proprietà di un albero di ricerca** (l'ordine delle chiavi).
- **Input:** un albero $T$ e un nodo $x$ il cui figlio destro non è NIL (presupposto di Left-Rotate).
- **Output:** $T$ in cui $x$ è sceso a sinistra del suo vecchio figlio destro $y$, che prende il suo posto.

## Idea · [[11 . Alberi rosso-neri.pdf#page=18|p. 18]], [[11 . Alberi rosso-neri.pdf#page=19|19]]

Nella figura, il nodo $A$ ($= x$) ha il figlio sinistro $\alpha$ e il figlio destro $B$ ($= y$); $B$ ha i sottoalberi $\beta$ e $\gamma$. Left-Rotate su $x$ fa tre cose, nell'ordine:
1. $\beta$ diventa **figlio destro** di $A$;
2. il **padre di $A$ diventa il padre di $B$** (B prende il posto di A);
3. $A$ diventa il **figlio sinistro** di $B$.

In maniera equivalente si definisce la **rotazione a destra** (Right-Rotate sul nodo $y$), l'operazione inversa, scambiando destra e sinistra.

![[11-alberi-rosso-neri-p18-rotazione-sinistra.png]]

## Pseudocodice · [[11 . Alberi rosso-neri.pdf#page=19|p. 19]]

```
Left-Rotate (T,x)
1  y ← right[x]
   ▷ operazione 1.
2  right[x] ← left[y]
3  if left[y] ≠ nil[T]
4      then p[left[y]] ← x
   ▷ operazione 2.
5  p[y] ← p[x]
6  if p[x] = nil[T]
7      then root[T] ← y
8      else if x = left[p[x]]
9          then left[p[x]] ← y
10         else right[p[x]] ← y
   ▷ operazione 3.
11 left[y] ← x
12 p[x] ← y
```

Il tempo di esecuzione è $O(1)$. I numeri di riga sono miei; nella slide i commenti sono nello stile `//`.

![[11-alberi-rosso-neri-p19-left-rotate-codice.png]]

## Esempio di esecuzione · [[11 . Alberi rosso-neri.pdf#page=20|p. 20]]

![[animazione-left-rotate.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero Left-Rotate sull'albero di p. 20 con $x = 11$ e $y = 18$: ogni operazione è un fotogramma, con in rosso i puntatori che cambiano e tratteggiati quelli che spariscono. Il fotogramma finale è l'albero ruotato della slide.

La figura della slide mostra, con $x = 11$ e $y = 18$ (in giallo): **Left-Rotate (T,x)** porta dall'albero in alto a quello in basso, **Right-Rotate (T,y)** dal basso verso l'alto. Prima della rotazione 18 ha figli 14 (con 12, 17) e 19 (con il figlio destro 22) e 11 ha il figlio sinistro 9; dopo, 11 ha figli 9 e 14, e 18 ha figli 11 e 19.

![[11-alberi-rosso-neri-p20-rotazioni-esempio.png]]

Traccia (verificata con [[alberi_rosso_neri.py]]):

| Operazione | Puntatori modificati |
|---|---|
| 1 | $right[11] \leftarrow 14$; $p[14] \leftarrow 11$ |
| 2 | $p[18] \leftarrow p[11] = 7$; $right[7] \leftarrow 18$ |
| 3 | $left[18] \leftarrow 11$; $p[11] \leftarrow 18$ |

## Correttezza · [[11 . Alberi rosso-neri.pdf#page=18|p. 18]]

> 🧩 Derivazione mia. La rotazione non cambia la sequenza della visita in ordine ([[inorder-tree-walk]]): prima, $A$ con sottoalberi $\alpha$ e $B(\beta, \gamma)$ dà $\alpha, A, \beta, B, \gamma$; dopo, $B$ con sottoalberi $A(\alpha, \beta)$ e $\gamma$ dà ancora $\alpha, A, \beta, B, \gamma$. Dunque la proprietà del BST (sinistra $\le$ nodo $\le$ destra) vale ancora in tutto l'albero: nei nodi sopra $A$ nulla è cambiato, perché il sottoalbero ha le stesse chiavi. Le righe 6–10 aggiornano il padre di $A$ distinguendo i tre casi (era la radice, figlio sinistro, figlio destro). I **colori** non vengono toccati: le proprietà rosso-nere dopo la rotazione dipendono da come si ricolora ([[rb-insert]]).

## Complessità · [[11 . Alberi rosso-neri.pdf#page=19|p. 19]]

$O(1)$ (slide). 🧩 Il corpo non ha cicli né ricorsione e fa un numero costante di assegnamenti di puntatori (al più 12 righe eseguite), quindi $T = \Theta(1)$.

## Connessioni

- [[albero-rosso-nero]] — la struttura che usa le rotazioni
- [[rb-insert]], [[rb-delete]] — le operazioni che le chiamano
- [[albero-binario-di-ricerca]] — l'ordine delle chiavi che la rotazione preserva
- [[lista-concatenata]] — le tre operazioni sono assegnamenti di puntatori come negli inserimenti di lista

## Fonti · [[11 . Alberi rosso-neri.pdf#page=18|p. 18]]–[[11 . Alberi rosso-neri.pdf#page=20|20]]

- [[lezione-11-alberi-rosso-neri]]

_Aggiornato: 2026-11-26 — ingest 11 . Alberi rosso-neri.pdf_

<!-- nav:inizio -->
---
**Lezione 11 · pagina 3 di 5** · ← [[albero-rosso-nero|Albero rosso-nero]] · [[lezioni|Indice]] · [[rb-insert|RB-Insert e RB-Insert-Fixup]] →
<!-- nav:fine -->
