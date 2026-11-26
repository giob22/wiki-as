---
tipo: entità
categoria: algoritmo
paradigma: "inserimento come in un BST seguito da una correzione locale (fixup)"
fonti_pdf: ["11 . Alberi rosso-neri.pdf#page=21", "11 . Alberi rosso-neri.pdf#page=22", "11 . Alberi rosso-neri.pdf#page=24", "11 . Alberi rosso-neri.pdf#page=32", "11 . Alberi rosso-neri.pdf#page=36", "11 . Alberi rosso-neri.pdf#page=37"]
---

# RB-Insert e RB-Insert-Fixup

## Problema risolto · [[11 . Alberi rosso-neri.pdf#page=21|p. 21]]

Inserire il nodo $z$ in un [[albero-rosso-nero]] $T$ mantenendo le cinque proprietà (colori, radice nera, foglie NIL nere, niente rosso con figlio rosso, stessa black-height).

## Idea · [[11 . Alberi rosso-neri.pdf#page=21|p. 21]]

Strategia delle slide:
1. si inserisce il nodo come in un normale albero di ricerca, con **RB-Insert**, una versione (leggermente) modificata di [[tree-insert]];
2. si colora il nodo di **rosso**;
3. si invoca una funzione ausiliaria, **RB-Insert-Fixup**, per ripristinare le proprietà degli alberi rosso-neri.

Il tempo di esecuzione sarà $O(\lg n)$ (vedi sotto).

## Pseudocodice · [[11 . Alberi rosso-neri.pdf#page=22|p. 22]], [[11 . Alberi rosso-neri.pdf#page=32|32]], [[11 . Alberi rosso-neri.pdf#page=34|34]]

**RB-Insert** (p. 22). Rispetto a Tree-Insert (le righe che cambiano sono in rosso nella slide) usa la sentinella $nil[T]$ al posto di NIL (righe 1, 3, 9), imposta $left[z]$ e $right[z]$ a $nil[T]$ (righe 14–15), colora $z$ di rosso (riga 16) e chiama il fixup (riga 17). Il tempo di esecuzione è $O(h)$.

```
RB-Insert (T,z)
1  y ← nil[T]
2  x ← root[T]
3  while x ≠ nil[T]
4      do y ← x
5         if key[z] < key[x]
6             then x ← left[x]
7             else x ← right[x]
8  p[z] ← y
9  if y = nil[T]
10     then root[T] ← z        // albero vuoto
11     else if key[z] < key[y]
12         then left[y] ← z
13         else right[y] ← z
14 left[z] ← nil[T]
15 right[z] ← nil[T]
16 color[z] ← RED
17 RB-Insert-Fixup (T,z)
```

**RB-Insert-Fixup** (pp. 32 e 34):

```
RB-Insert-Fixup (T,z)
1  while color[p[z]] = RED
2      do if p[z] = left[p[p[z]]]
3            then y ← right[p[p[z]]]            // zio
4                 if color[y] = RED
5                    then color[p[z]] ← BLACK
6                         color[y] ← BLACK
7                         color[p[p[z]]] ← RED
8                         z ← p[p[z]]
9                    else if z = right[p[z]]
10                          then z ← p[z]
11                               Left-Rotate (T,z)
12                        color[p[z]] ← BLACK
13                        color[p[p[z]]] ← RED
14                        Right-Rotate (T,p[p[z]])
15           else (stesso codice di then con right e left scambiati)
16 color[root[T]] ← BLACK
```

> ⚠️ Contraddizione (refuso): le slide scrivono `y ← right[p[p[z]]` e `color[p[p[z]]←RED` con una parentesi quadra mancante; nel wiki sono completate. I numeri di riga sono miei.

![[11-alberi-rosso-neri-p22-rb-insert-codice.png]]
![[11-alberi-rosso-neri-p32-rb-insert-fixup-codice.png]]

## Quali proprietà si possono violare · [[11 . Alberi rosso-neri.pdf#page=23|p. 23]]

Dopo l'inserimento di $z$ rosso (slide, con etichette «vale» e «non vale»):
1. ogni nodo è rosso o nero: **vale**;
2. la radice è nera: **non vale se l'albero era vuoto** ($z$ è la nuova radice, rossa);
3. ogni foglia NIL è nera: **vale**;
4. se un nodo è rosso entrambi i figli sono neri: **non vale se il padre di $z$ è rosso**;
5. stessa black-height su tutti i percorsi: **vale**.

![[11-alberi-rosso-neri-p23-proprieta-violabili.png]]

> 🧩 Perché la 5 vale: $z$ prende il posto di una foglia esterna nera e ha due foglie esterne nere come figli; ogni cammino che passava per la vecchia foglia nera ora passa per $z$ (rosso, non conta) e per una nuova foglia nera: lo stesso numero di nodi neri.

## Invariante del ciclo · [[11 . Alberi rosso-neri.pdf#page=24|p. 24]]–[[11 . Alberi rosso-neri.pdf#page=26|26]]

RB-Insert-Fixup è un ciclo `while` eseguito finché il padre di $z$ resta rosso, costruito per mantenere l'invariante. All'inizio di ogni iterazione:
- **a)** il nodo $z$ è rosso;
- **b)** se $p[z]$ è la radice, allora $p[z]$ è nero;
- **c)** in tutto l'albero c'è **al massimo una violazione** delle proprietà rosso-nere, ed è di tipo 2 o di tipo 4:
  1. se è di tipo 2, si presenta perché $z$ è la radice ed è rossa;
  2. se è di tipo 4, si presenta perché sia $z$ sia $p[z]$ sono rossi.

![[11-alberi-rosso-neri-p24-rb-insert-fixup-invariante.png]]

**Inizializzazione** (p. 25; $z$ è il nodo appena inserito):
- a) vera perché il nodo inserito è rosso;
- b) se $p[z]$ è la radice non è stata modificata da RB-Insert, quindi è rimasta nera;
- c) le proprietà 1, 3 e 5 non sono violate da RB-Insert. Se l'albero era vuoto e $z$ è la nuova radice c'è una violazione di tipo 2 e nessuna di tipo 4 (le foglie sono nere); se l'albero non era vuoto e $z$ è figlio di un nodo rosso c'è una violazione di tipo 4 e nessuna di tipo 2.

**Conclusione** (p. 26): il ciclo termina quando il padre di $z$ è nero. L'invariante (c.2) garantisce che non ci sono violazioni di tipo 4; in base a c.1) ci potrebbe essere una violazione di tipo 2, con $z$ radice rossa: basta **ricolorare di nero la radice** (riga 16). Se $z$ è il primo nodo inserito il ciclo termina subito, perché il padre di $z$ è la sentinella, che è nera.

## Il corpo del ciclo · [[11 . Alberi rosso-neri.pdf#page=27|p. 27]]–[[11 . Alberi rosso-neri.pdf#page=36|36]]

Se si entra nel ciclo (p. 27):
- il padre di $z$ è rosso; per b) non può essere la radice, quindi il padre di $p[z]$ non è la sentinella ma un nodo interno: il **nonno** $p[p[z]]$ esiste;
- il nonno è **nero**: se fosse rosso, con $p[z]$ rosso ci sarebbe una violazione di tipo 4 fra $p[z]$ e $p[p[z]]$, contro c.2);
- non ci sono violazioni di tipo 2: altrimenti $z$ sarebbe la radice e il padre di $z$ (la sentinella) sarebbe nero, assurdo perché $p[z]$ è rosso.

Si distingue se il padre è figlio **sinistro** o **destro** del nonno (p. 28): i due casi sono simmetrici (si scambiano left e right); le slide trattano il caso in cui $p[z]$ è figlio sinistro. Si sa quindi che $z$ è rosso, $p[z]$ è rosso, $p[p[z]]$ è nero, e si distingue sul colore dello **zio** $y$ (p. 29).

![[11-alberi-rosso-neri-p29-caso-1.png]]

| Caso | Condizione | Azione | Dopo |
|---|---|---|---|
| **1** (pp. 29–30) | lo zio $y$ è **rosso** | $p[z]$ e $y$ diventano neri, $p[p[z]]$ diventa rosso, $z \leftarrow p[p[z]]$ (ricolorazione) | $z$ sale di due livelli, il ciclo può ripetersi |
| **2** (pp. 31–32) | $y$ è **nero** e $z$ è figlio **destro** | $z \leftarrow p[z]$ e Left-Rotate su $z$ | ci si riconduce al caso 3 |
| **3** (pp. 33–34) | $y$ è **nero** e $z$ è figlio **sinistro** | $p[z]$ diventa nero, $p[p[z]]$ rosso, Right-Rotate su $p[p[z]]$ | il ciclo termina (ora $p[z]$ è nero) |

![[11-alberi-rosso-neri-p31-caso-2.png]]
![[11-alberi-rosso-neri-p33-caso-3.png]]

**Caso 1** (figura di p. 29: $C$ nonno nero, $A = p[z]$ e $D = y$ rossi, $B = z$): ricolorazione e nuovo $z$ = il nonno $C$, che è rosso. Verifica dell'invariante (p. 30), con $z'$ il valore di $z$ nella nuova iterazione:
- a) $z'$ è $p[p[z]]$, colorato di rosso;
- b) $p[z']$ non è modificato in questa iterazione, quindi se è la radice allora è nero;
- c) non si introducono violazioni di tipo 5 (né 1 e 3); se $z'$ è la radice si è risolta la violazione di tipo 4 e resta una sola violazione, di tipo 2 ($z'$ radice rossa); se $z'$ non è la radice non si è introdotta una violazione di tipo 2, e ci può essere una violazione di tipo 4 fra $z'$ e $p[z']$ se $p[z']$ è rosso.

**Caso 2** (p. 31): dato che $z$ e $p[z]$ sono rossi, la rotazione non viola la proprietà 5 né la black-height. Ci si riconduce al caso 3.

**Caso 3** (p. 33): $p[z]$ diventa nero, $p[p[z]]$ rosso e Right-Rotate su $p[p[z]]$; ciò **preserva la proprietà 5** e il ciclo termina perché $p[z]$ è nero (le figure: $C$ è il nonno, $B = p[z]$, $A = z$, $y = D$; dopo, $B$ è la radice del sottoalbero, nero, con figli $A$ e $C$ rossi).

Verifica dell'invariante per i casi 2 e 3 (p. 35): a) nel caso 2 $z$ diventa $p[z]$, che è rosso, e poi $z$ non si modifica più; b) il caso 3 colora $p[z]$ di nero; c) non si introducono violazioni di tipo 5 (né 1 e 3): $z$ (rosso) non è la radice e quindi non viola 2; non ci sono altre violazioni di 2 perché l'unico nodo che diventa rosso diventa figlio di un nodo nero (e quindi non può essere la radice); i casi 2 e 3 correggono una violazione di tipo 4 senza introdurne altre.

> 🧩 Perché la proprietà 5 si conserva nel caso 1: prima della ricolorazione ogni cammino dal nonno $C$ (nero) in giù passa per $C$ e poi per $A$ o per $D$ (rossi) e conta un nero ($C$); dopo, $C$ è rosso e $A$, $D$ sono neri: ancora un nodo nero per ciascun cammino, e nulla cambia sopra $C$. Nel caso 3, prima della rotazione i cammini del sottoalbero passavano per $C$ nero e $B$ rosso (un nero); dopo, la radice $B$ è nera e i suoi figli $A$ e $C$ sono rossi: un nero per cammino. Le rotazioni non cambiano l'ordine, quindi le proprietà del BST restano.

## Esempio di esecuzione · [[11 . Alberi rosso-neri.pdf#page=37|p. 37]]–[[11 . Alberi rosso-neri.pdf#page=41|41]]

![[animazione-rb-insert.svg]]
> 🧩 Animazione generata da me ([[genera_animazioni.py]]) eseguendo davvero RB-Insert sull'albero rosso-nero di p. 37, inserendo la chiave 4: caso 1, poi caso 2, poi caso 3, con le righe di RB-Insert-Fixup evidenziate. Il risultato è l'albero di p. 40.

Le slide (pp. 37–40) mostrano i tre casi sull'albero con radice 11 (nero), 2 e 14, 1 e 7, 15, 5 e 8, e $z = 4$ figlio sinistro di 5: **caso 1** (p. 37: violazione della proprietà 4, lo zio $y = 8$ è rosso; i nodi sono ricolorati e $z$ diventa il nonno 7), **caso 2** (p. 38: lo zio $y = 14$ è nero e $z = 7$ è figlio destro di 2; rotazione a sinistra), **caso 3** (pp. 39–40: lo zio è nero e $z = 2$ è figlio sinistro di 7; rotazione a destra e ricolorazione dei nodi 7 e 11). A p. 41 c'è una schermata del visualizzatore «Red/Black Tree Visualization» (cs.usfca.edu), con un albero di 9 nodi.

![[11-alberi-rosso-neri-p37-inserimento-caso-1-esempio.png]]
![[11-alberi-rosso-neri-p38-inserimento-caso-2-esempio.png]]
![[11-alberi-rosso-neri-p39-inserimento-caso-3-esempio.png]]
![[11-alberi-rosso-neri-p40-inserimento-caso-3-ricolorazione.png]]
![[11-alberi-rosso-neri-p41-visualizzatore.png]]

Traccia (verificata con [[alberi_rosso_neri.py]]):

| Passo | $z$ | $p[z]$ | zio $y$ | Caso | Azione | Albero dopo |
|---|---|---|---|---|---|---|
| RB-Insert | 4 (rosso) | 5 (rosso) | — | — | 4 figlio sinistro di 5, violazione 4 | radice 11 |
| iterazione 1 | 4 | 5 | 8 (rosso) | 1 | 5 e 8 neri, 7 rosso, $z \leftarrow 7$ | 7 rosso, figli 5 e 8 neri |
| iterazione 2 | 7 | 2 (rosso) | 14 (nero) | 2 | $z \leftarrow 2$, Left-Rotate (T,2) | 7 sopra 2; 2 ha figli 1 e 5 |
| iterazione 2 | 2 | 7 (rosso) | 14 (nero) | 3 | 7 nero, 11 rosso, Right-Rotate (T,11) | radice 7 (nero), figli 2 (rosso) e 11 (rosso) |
| fine | 2 | 7 (nero) | | | il ciclo termina; radice già nera | albero di p. 40 |

Albero finale: 7 (nero) con figli 2 (rosso) e 11 (rosso); 2 ha figli 1 (nero) e 5 (nero), 5 ha il figlio sinistro 4 (rosso); 11 ha figli 8 (nero) e 14 (nero), 14 ha il figlio destro 15 (rosso). Tre iterazioni, due rotazioni, black-height 2.

## Complessità · [[11 . Alberi rosso-neri.pdf#page=22|p. 22]], [[11 . Alberi rosso-neri.pdf#page=36|36]]

### Derivazione — $T(n) = O(\lg n)$ · [[11 . Alberi rosso-neri.pdf#page=36|p. 36]]
**Fonte:** «Il tempo di esecuzione di RB-Insert-Fixup è $O(\lg n)$. Il ciclo si ripete solo se siamo nel caso 1, durante il quale $z$ sale di due livelli. Il ciclo viene ripetuto $O(\lg n)$ volte. Vengono eseguite al più due rotazioni. Il ciclo termina quando entriamo nel caso 2 o 3».
**Si parte da:** il costo $O(h)$ di RB-Insert (p. 22) e l'altezza $h \le 2\lg(n+1)$ ([[albero-rosso-nero]]).

$$
\begin{aligned}
T_{\text{RB-Insert}}(n) &= \underbrace{O(h)}_{\text{discesa, righe 1–13}} + \underbrace{O(1)}_{\text{righe 14–16}} + T_{\text{Fixup}}(n) && \text{somma delle parti} \\
T_{\text{Fixup}}(n) &\le \underbrace{\tfrac{h}{2} \cdot O(1)}_{\text{iterazioni del caso 1}} + \underbrace{O(1)}_{\text{casi 2–3 (una volta)}} + O(1) && \text{ogni caso 1 sposta } z \text{ di 2 livelli} \\
&= O(h) = O(\lg n) && h \le 2\lg(n+1)
\end{aligned}
$$

Quindi RB-Insert costa $O(\lg n)$ in totale. Le **rotazioni** sono al più due, per inserimento: il caso 2 fa una rotazione e porta al caso 3 (che ne fa un'altra e termina); il caso 1 non ruota.

**Sanity check** ([[alberi_rosso_neri.py]]): su 200 sequenze casuali di 60 inserimenti il numero di rotazioni non supera mai $2 \times 60$ e le proprietà 1–5 valgono dopo ogni inserimento; nell'esempio di p. 37 ci sono 3 iterazioni e 2 rotazioni.
**Ipotesi:** modello RAM; costo costante per ricolorazione e per [[left-rotate|rotazione]].

## Connessioni

- [[albero-rosso-nero]] — la struttura e il teorema sull'altezza
- [[tree-insert]] — RB-Insert ne è una versione modificata
- [[left-rotate]] — usata nei casi 2 e 3
- [[rb-delete]] — la cancellazione, con un fixup diverso
- [[invariante-di-ciclo]] — il metodo con cui si dimostra il fixup

## Fonti · [[11 . Alberi rosso-neri.pdf#page=21|p. 21]]–[[11 . Alberi rosso-neri.pdf#page=41|41]]

- [[lezione-11-alberi-rosso-neri]]

_Aggiornato: 2026-11-26 — ingest 11 . Alberi rosso-neri.pdf_

<!-- nav:inizio -->
---
**Lezione 11 · pagina 4 di 5** · ← [[left-rotate|Rotazioni (Left-Rotate e Right-Rotate)]] · [[lezioni|Indice]] · [[rb-delete|RB-Delete e RB-Delete-Fixup]] →
<!-- nav:fine -->
