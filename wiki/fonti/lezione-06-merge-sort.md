---
tipo: fonte
titolo: "Corso di Algoritmi e Strutture Dati — Progettazione di algoritmi: Divide et Impera (Merge Sort)"
file_raw: "06-Merge Sort (1).pdf"
pagine: "1-48"
data_ingest: 2026-10-10
formato: slide-pdf
argomenti: [divide et impera, torre di hanoi, merge sort, merge, ricorrenze, metodo di sostituzione, albero di ricorrenza, teorema dell'esperto, massimo sottoarray, crescita delle funzioni]
---

# Lezione 06 — Divide et impera: Merge Sort (06-Merge Sort (1).pdf) · [[06-Merge Sort.pdf|Merge Sort (vecchia)]]

> Versione aggiornata delle slide (48 pagine), che sostituisce la precedente (30 pagine, ingerita il 2026-10-01). Tutti i link del wiki puntano alla nuova versione. Le 30 pagine della vecchia sono contenute, identiche nel contenuto, nella nuova; le novità sono elencate sotto in «Cosa cambia rispetto alla versione precedente».

## Sommario · [[06-Merge Sort (1).pdf#page=1|p. 1]]

Slide del Prof. Marrone, a.a. 26/27, intitolate «Progettazione di algoritmi – Divide et Imera». La lezione si apre con lo «Stop & Think» della **Torre di Hanoi**: il problema, la domanda su come ridurlo a problemi più piccoli dello stesso tipo, l'approccio divide et impera e la sequenza di mosse per tre dischi. Presenta poi **merge sort**: idea divide et impera, funzionamento su un esempio di 11 elementi, e la costruzione dello pseudocodice in tappe. Si parte da una prima versione che alloca nuovi vettori $L$ e $R$ (discesa, caso base, risalita); se ne discutono le criticità; si passa agli **indici** su un unico array; si sposta la memoria ausiliaria dentro **Merge**, che è il punto in cui nasce il «non in-place». Seguono il **codice completo** di Merge con sentinelle, la traccia, l'invariante, il costo lineare e lo pseudocodice definitivo di **Merge-Sort**. L'analisi introduce la ricorrenza generale del divide et impera $aT(n/b) + D(n) + C(n)$ (prima come domanda, poi con le risposte) e la risolve per merge sort con l'albero di ricorsione: $\Theta(n\lg n)$. Dopo uno «Stop & Think» sul **massimo sottoarray** (solo rimando al libro), la lezione presenta i tre metodi per risolvere le ricorrenze: **sostituzione** (con il problema dei casi base), **albero di ricorrenza** (esempio $3T(n/4) + cn^2$, costruito un livello per slide e verificato per sostituzione) e **teorema dell'esperto** (tre casi, quattro esempi, uno dei quali cade nel gap). Chiudono lo S&T «Albero di ricorsione?» e quattro slide riprese dalla lezione 05 sulla crescita delle funzioni (pattern matching, logaritmi, split equilibrato).

## Percorso della lezione · [[06-Merge Sort (1).pdf|Merge Sort]]

**PDF:** (pp. 1–52; versione aggiornata delle slide, sostituisce la precedente di 30 pagine)

Pagine del wiki nell'ordine di prima comparsa nelle slide (è l'ordine delle pagine di questa lezione nel libro, dopo questa):
1. [[torre-di-hanoi]] — pp. 2–5 · S&T: problema e domanda (p. 3), approccio divide et impera con fase decrescente e ascendente (p. 4), le 7 mosse per 3 dischi (p. 5); pseudocodice ricorsivo e $2^n - 1$ mosse (🧩)
2. [[merge-sort]] — pp. 6–16 (poi pp. 23–27) · idea divide et impera e «ATTENZIONE» sul non in-place (p. 7), funzionamento su ⟨5, 2, 8, 0, 4, 7, 1, 9, 3, 2, 6⟩ (p. 9), primo pseudocodice con $L$ e $R$ e criticità (pp. 10–13), versione con indici (pp. 14–15), memoria ausiliaria in Merge (p. 16); pseudocodice definitivo (p. 23), ricorrenza $aT(n/b) + D(n) + C(n)$ prima come domanda e poi con le risposte (pp. 24–26), albero di ricorsione e $\Theta(n\lg n)$ (p. 27)
3. [[merge]] — pp. 16–22 · prima versione senza sentinelle (p. 16), codice completo con sentinelle (p. 17), traccia su ⟨2, 4, 5, 7⟩ + ⟨1, 2, 3, 6⟩ (p. 18), invariante (pp. 19–21), costo $\Theta(n)$ (p. 22)
4. [[massimo-sottoarray]] — p. 28 · S&T: solo il titolo e il rimando al libro (cap. 4.1)
5. [[metodo-di-sostituzione]] — pp. 30–32 (poi p. 41) · ipotesi + induzione, $2T(\lfloor n/2 \rfloor) + n \le cn\lg n$ con $c \ge 2$, perché due casi base
6. [[metodo-albero-di-ricorrenza]] — pp. 33–43 (poi p. 48) · $3T(n/4) + cn^2$ costruito un livello per slide (pp. 34–37): livelli, costo per livello, serie geometrica, verifica con $d \ge \frac{16}{13}c$, anche $\Omega(n^2)$; S&T «Albero di ricorsione?» (p. 48)
7. [[teorema-dell-esperto]] — pp. 44–47 · tre casi, gap, esempi $9T(n/3) + n$, $T(2n/3) + 1$, $3T(n/4) + n\lg n$, $2T(n/2) + n\lg n$

Già lette, aggiornate con questa lezione: *divide-et-impera* (pp. 24–26: ricorrenza generale e tabella degli esempi), *equazioni-di-ricorrenza* (p. 29: definizione di ricorrenza e i tre metodi), *invariante-di-ciclo* (p. 20, collegamento a Merge), *ordinamento* (tabella con merge sort), *efficienza-degli-algoritmi* ($n\lg n$ ora dimostrato), *risoluzione-ricorrenze* (casi 2–5 e 7), *dimostrazioni-di-correttezza* (casi 7–8), *correttezza-per-induzione*, *array-dinamico* (annotazione di p. 7), *selection-sort* (perché non dividere per $n$, p. 7).
Già lette nella lezione 05, riprese senza novità alle pp. 49–52: *substring-pattern-matching* e *findmatch* (pp. 49–50), *logaritmi-nell-analisi* e *potenza-veloce* (pp. 51–52).

**Ordine consigliato.**
Le slide spezzano merge sort in due (pp. 6–16 e 22–25) con Merge in mezzo (pp. 16–22); la p. 16 appartiene a entrambi, e il metodo dell'albero compare una prima volta a p. 27 prima di essere spiegato (pp. 33–43). Ordine suggerito:
1. *torre-di-hanoi*, come riscaldamento sulla ricorsione e sulle due fasi (discesa e risalita);
2. *merge-sort* fino alla sezione «Dal primo pseudocodice alla versione con indici» compresa (pp. 6–16): spiega perché Merge deve copiare in $L$ e $R$;
3. *merge* per intero (pp. 16–22): il suo costo $\Theta(n)$ serve nell'analisi;
4. il resto di *merge-sort* (pseudocodice definitivo e complessità, pp. 23–27): la sezione «Soluzione con l'albero di ricorsione» anticipa il metodo che *metodo-albero-di-ricorrenza* spiega in generale;
5. *equazioni-di-ricorrenza* (solo la sezione «Ricorrenze divide et impera»), poi *metodo-di-sostituzione*, *metodo-albero-di-ricorrenza*, *teorema-dell-esperto*, nell'ordine delle slide;
6. *massimo-sottoarray* quando vuoi: è solo un rimando al libro. Le pp. 49–52 sono un ripasso della lezione 05.

## Punti chiave · [[06-Merge Sort (1).pdf#page=2|p. 2]]–[[06-Merge Sort (1).pdf#page=5|5]], [[06-Merge Sort (1).pdf#page=7|p. 7]]–[[06-Merge Sort (1).pdf#page=10|10]], [[06-Merge Sort (1).pdf#page=13|p. 13]]–[[06-Merge Sort (1).pdf#page=19|19]], [[06-Merge Sort (1).pdf#page=21|p. 21]]–[[06-Merge Sort (1).pdf#page=30|30]], [[06-Merge Sort (1).pdf#page=32|p. 32]], [[06-Merge Sort (1).pdf#page=33|33]], [[06-Merge Sort (1).pdf#page=43|p. 43]]–[[06-Merge Sort (1).pdf#page=49|49]], [[06-Merge Sort (1).pdf#page=52|p. 52]]

1. S&T Torre di Hanoi: problema e vincoli, domanda sulla riduzione a problemi più piccoli → [[torre-di-hanoi]].
2. Approccio divide et impera per Hanoi: sotto-torre, caso base di un solo disco, combinazione delle soluzioni; fase decrescente e ascendente; sequenza di 7 mosse per 3 dischi.
3. Merge sort: divide in due metà, ordina ricorsivamente fino a lunghezza 1, combina con Merge; non ordina sul posto (ATTENZIONE!!!) → [[merge-sort]].
4. Funzionamento su ⟨5, 2, 8, 0, 4, 7, 1, 9, 3, 2, 6⟩.
5. Prima versione `MergeSort(A)` con vettori $L$, $R$: discesa, caso base, risalita; criticità (caso base senza lavoro, seconda funzione per fondere, vettori nuovi a ogni chiamata).
6. Miglioramento: un sottoproblema è una porzione dell'array originale; `MergeSort(A, p, r)` con indici.
7. La copia in $L$ e $R$ passa da Merge-Sort a Merge, perché l'inserimento in $A$ è una sovrascrittura: qui nasce il «non in-place» → [[merge]].
8. Merge, codice completo con sentinelle $\infty$; «è una funzione iterativa!!»; non ordina ma inserisce in $A$ in modo ordinato; traccia su ⟨2, 4, 5, 7⟩ + ⟨1, 2, 3, 6⟩.
9. Invariante di Merge: $A[p..k-1]$ contiene i $k - p$ elementi più piccoli di $L$ e $R$, ordinati; $L[i]$, $R[j]$ minimi non ricopiati → [[invariante-di-ciclo]].
10. Merge costa tempo proporzionale a $n = n_1 + n_2$.
11. Pseudocodice definitivo di Merge-Sort, invocato come `Merge-Sort(A,1,n)`.
12. Ricorrenza del divide et impera con $\Theta(1)$, $D(n)$, $C(n)$, $a$, $1/b$; per merge sort $D = \Theta(1)$, $C = \Theta(n)$, $a = b = 2$ → [[divide-et-impera]].
13. Albero di ricorsione di $2T(n/2) + cn$: $\lg n + 1$ livelli da $cn$, totale $cn\lg n + cn = \Theta(n\lg n)$.
14. S&T Problema del massimo sottoarray, capitolo 4.1 del libro → [[massimo-sottoarray]].
15. Ricorrenza: equazione o disequazione che descrive una funzione tramite i suoi valori su ingressi più piccoli; tre metodi → [[equazioni-di-ricorrenza]].
16. Metodo di sostituzione su $2T(\lfloor n/2 \rfloor) + n$: $T(n) \le cn\lg n$ con $c \ge 2$, casi base $T(2) = 4$ e $T(3) = 5$; perché due casi base → [[metodo-di-sostituzione]].
17. Albero di ricorrenza di $3T(n/4) + cn^2$: $\log_4 n$, $3^i$ nodi, somma $< \frac{16}{13}cn^2 + \Theta(n^{\log_4 3})$; verifica con $d \ge \frac{16}{13}c$; anche $\Omega(n^2)$ → [[metodo-albero-di-ricorrenza]].
18. Teorema dell'esperto: tre casi, osservazioni sul gap → [[teorema-dell-esperto]].
19. Esempi: $9T(n/3) + n$ (caso 1), $T(2n/3) + 1$ (caso 2), $3T(n/4) + n\lg n$ (caso 3), $2T(n/2) + n\lg n$ (gap).
20. S&T «Albero di ricorsione?».
21. Crescita delle funzioni: S&T String Pattern Matching e `findmatch`, importanza dei logaritmi, Importance of an Even Split: sono le slide 30–33 della lezione 05 → [[substring-pattern-matching]], [[findmatch]], [[logaritmi-nell-analisi]].

## Cosa cambia rispetto alla versione precedente

| Nuova versione | Vecchia versione | Differenza |
|---|---|---|
| pp. 3–4 | — | **nuove**: enunciato di Hanoi con domanda; approccio divide et impera |
| p. 3 | p. 3 | la figura della torre è ora accompagnata dal testo del problema |
| p. 7 | p. 6 | aggiunto «(ATTENZIONE!!!)» a «non effettua un ordinamento sul posto» |
| p. 9 | p. 7 | titolo «Merge-Sort: funzionamento» |
| pp. 10–16 | — | **nuove**: primo pseudocodice con $L$, $R$, criticità, versione con indici, spostamento delle copie in Merge |
| p. 17 | p. 9 | titolo «Merge: codice completo»; aggiunti «È una funzione iterativa!!» e la precisazione sul «non fa proprio ordinamento» |
| p. 19 | — | **nuova**: solo titolo «Merge: analisi di correttezza», pagina vuota |
| p. 24 | — | **nuova**: ricorrenza del divide et impera con $D(n)$, $C(n)$, $a$, $b$ come domande |
| p. 30 | p. 19 | «Consideriamo $T(1) = 1$ vera ai fini della verifica» (prima: «Utilizziamo…») |
| pp. 34–37 | p. 23 | l'albero di $3T(n/4) + cn^2$ è costruito su quattro slide invece che su una |
| p. 48 | — | **nuova**: S&T «Albero di ricorsione?» |
| pp. 49–52 | — | **nuove** in questo file: riprendono 05 pp. 32–35 (senza lo pseudocodice di `power(a,n)`) |

Tutte le altre pagine sono uguali, spostate in avanti: vecchie pp. 10–32 → nuove pp. 18, 19–22, 24–32, 36–43.

## Annotazioni a mano

Il PDF contiene annotazioni scritte a mano, riportate nelle pagine del wiki accanto alla slide a cui si riferiscono:
- p. 4: fase decrescente e fase ascendente della ricorsione → [[torre-di-hanoi]];
- p. 7: «array dinamico è solo una forma di gestione dell'array»; «perché dividiamo in due? perché non per $n$?» → [[merge-sort]];
- pp. 10, 11: «caso base / fase ascendente», «caso ricorsivo / fase decrescente», «qui L e R arrivano ordinati» → [[merge-sort]];
- p. 16: le copie in $L$, $R$ «facevano parte della fase discendente pre modifiche»; il ciclo è «fase ascendente» → [[merge]];
- p. 23: «Restituisci A ⇒ non operare su A se devi considerare il singolo elemento di A»; «l'ottimizzazione della firma ci ha portato a tutti questi benefici» → [[merge-sort]];
- p. 24: «Ricorrenza: formula matematica», «potrei avere più casi base», $D(n)$ «equivale al costo dell'operazione per ottenere $q$» → [[merge-sort]].

## Refusi e note · [[06-Merge Sort (1).pdf#page=6|p. 6]], [[06-Merge Sort (1).pdf#page=19|p. 19]], [[06-Merge Sort (1).pdf#page=28|p. 28]]

- p. 1: «Divide et **Imera**» per «Impera». Il file si chiama «Merge Sort» ma copre l'intero paradigma divide et impera e i metodi per le ricorrenze.
- Le pagine p. 6 (titolo «Merge Sort») e p. 28 (titolo dello S&T) sono solo titoli; p. 19 ha solo il titolo e la pagina vuota. Le pagine 3, 5, 8, 9, 13, 15, 21, 25, 30 e 32–38 hanno il contenuto soprattutto come figura: è trascritto nelle pagine del wiki, con l'immagine accanto.
- p. 10: la prima versione dello pseudocodice è uno schizzo in italiano, fuori dalle [[pseudocodice|convenzioni del corso]]; la slide stessa la intitola «pseudocodice?».
- p. 14: «un sottovettore di un solo element» (manca la «o»).
- p. 16: la versione semplificata di Merge non ha sentinelle e leggerebbe oltre la fine di $L$ o $R$ (🧩, in [[merge]]); il codice completo di p. 17 le aggiunge.
- p. 17: la parentesi aperta in «(infatti non fa proprio ordinamento, … da L e R.» non viene chiusa.
- pp. 17, 17, 21: pseudocodice in stile Cormen 2ª ed. (`do`, `then`, `//`, assegnamenti multipli), diverso dalle convenzioni del corso: segnalato in [[merge]].
- pp. 14 e 22: due forme del caso base, «se $p = r$ ritorna» e «if $p<r$»: equivalenti (🧩, in [[merge-sort]]).
- p. 31: la slide scrive «assumiamo vero per ⌊n/2⌋», e il testo estratto del PDF mostra parentesi sbagliate (⌊n/2⌊); nella figura sono corrette. Lo stesso a p. 41 per ⌊n/4⌋.
- p. 34: la ricorrenza è data con $\lfloor n/4 \rfloor$, l'albero è costruito senza parti intere (approssimazione dichiarata nella slide).
- p. 41: per $n = 2, 3$ si ha $\lfloor n/4 \rfloor = 0$: oltre a $T(1)$ servono anche questi casi base (🧩, in [[metodo-albero-di-ricorrenza]]).
- p. 46: «$\epsilon \approx 0{,}2$» viene da $1 - \log_4 3 \approx 0.207$.
- p. 52: «≈ 35 chiamate nel caso peggiore» (in 05 p. 35 la stessa slide): vedi la nota sul 35 in [[lezione-05-insertion-sort]].
- Le slide non danno lo pseudocodice della Torre di Hanoi né la correttezza di Merge-Sort: nel wiki sono marcati 🧩.

## Concetti introdotti

[[merge]], [[merge-sort]], [[torre-di-hanoi]], [[massimo-sottoarray]], [[metodo-di-sostituzione]], [[metodo-albero-di-ricorrenza]], [[teorema-dell-esperto]], [[progettazione-divide-et-impera]]; aggiornati [[divide-et-impera]], [[equazioni-di-ricorrenza]], [[ordinamento]], [[invariante-di-ciclo]], [[efficienza-degli-algoritmi]]; ripresi dalla lezione 05 [[substring-pattern-matching]], [[findmatch]], [[logaritmi-nell-analisi]], [[potenza-veloce]].

## Domande aperte

- Il massimo sottoarray è solo annunciato (p. 28): soluzione da cercare nel libro (Cormen §4.1) o in una lezione successiva.
- Lo S&T «Albero di ricorsione?» (p. 48) è solo una domanda: nel wiki c'è uno spunto di risposta 🧩 in [[metodo-albero-di-ricorrenza]].
- La slide di correttezza di p. 19 è vuota: probabilmente svolta a lezione.
- La dimostrazione del teorema dell'esperto non è nelle slide.
- Le slide non quantificano lo spazio di merge sort oltre a «non sul posto»: nel wiki $\Theta(n)$ è una mia derivazione.

## Domande da esame

- Scrivere Merge e Merge-Sort; eseguire la traccia di Merge su due sequenze date.
- Quali sono le criticità della prima versione con i vettori $L$ e $R$, e come le risolve la versione con gli indici? Perché la memoria ausiliaria resta necessaria in Merge?
- Enunciare e dimostrare l'invariante di Merge; a che servono le sentinelle?
- Scrivere la ricorrenza di merge sort ($D$, $C$, $a$, $b$) e risolverla con l'albero di ricorsione.
- Dimostrare per sostituzione che $2T(\lfloor n/2 \rfloor) + n = O(n\lg n)$; perché servono due casi base?
- Risolvere $3T(n/4) + cn^2$ con l'albero e verificare per sostituzione.
- Enunciare il teorema dell'esperto e applicarlo; mostrare una ricorrenza nel gap.
- Torre di Hanoi: approccio divide et impera, algoritmo ricorsivo e numero di mosse.

_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf_
_Aggiornato: 2026-10-10 — ingest della versione aggiornata 06-Merge Sort (1).pdf (48 pagine)_
_Aggiornato: 2026-10-28 — aggiunto il «Percorso della lezione» (spostato dall'indice lezioni.md)_

<!-- nav:inizio -->
---
**Lezione 06 · pagina 1 di 8** · ← [[potenza-veloce|power(a, n) — potenza veloce (fast exponentiation)]] · [[lezioni|Indice]] · [[torre-di-hanoi|Torre di Hanoi · 06-Merge Sort (1).pdf#page=2p. 2]] →
<!-- nav:fine -->
