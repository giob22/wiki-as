---
tipo: concetto
importanza_esame: alta
prerequisiti: ["equazioni-di-ricorrenza", "logaritmi-nell-analisi"]
fonti_pdf: ["06-Merge Sort (1).pdf#page=25", "06-Merge Sort (1).pdf#page=31", "06-Merge Sort (1).pdf#page=32", "06-Merge Sort (1).pdf#page=35", "06-Merge Sort (1).pdf#page=36", "06-Merge Sort (1).pdf#page=37", "06-Merge Sort (1).pdf#page=38", "06-Merge Sort (1).pdf#page=39", "06-Merge Sort (1).pdf#page=40", "06-Merge Sort (1).pdf#page=44", "07-Quicksort 1.pdf#page=17", "07-Quicksort 1.pdf#page=18"]
---

# Metodo dell'albero di ricorrenza

## Definizione

> 📄 Fonte: [[06-Merge Sort (1).pdf#page=31]]

- Il metodo dell'albero di ricorrenza può essere usato per **generare delle buone soluzioni di tentativo**, da verificare con il [[metodo-di-sostituzione]] se sono state fatte ipotesi semplificative per derivare le soluzioni.
- I **nodi** dell'albero di ricorrenza riportano il **costo per risolvere un dato (sotto)problema**.

> 🧩 Procedura (ricavata dagli esempi delle slide):
> 1. la radice è il costo «locale» della chiamata su $n$ (il termine non ricorsivo della ricorrenza); i figli sono le chiamate ricorsive;
> 2. si espande ogni nodo allo stesso modo, fino ai sottoproblemi di dimensione 1;
> 3. si calcolano il **numero di livelli** e il **costo di ciascun livello**;
> 4. si **somma** sui livelli, spesso con una serie geometrica;
> 5. se si sono fatte approssimazioni (parti intere ignorate, $n$ potenza esatta), si verifica il risultato per sostituzione.

## Formule

> 🧮 Formula chiave — per $T(n) = aT(n/b) + f(n)$ con $n$ potenza di $b$ (🧩 forma generale degli esempi di pp. 25 e 32–38):
$$
T(n) = \sum_{i=0}^{\log_b n - 1} a^i f\!\left(\frac{n}{b^i}\right) + a^{\log_b n}\, T(1), \qquad a^{\log_b n} = n^{\log_b a}
$$
Simboli: $i$ = livello (radice = 0); $a^i$ = nodi al livello $i$; $n/b^i$ = dimensione di un sottoproblema al livello $i$; $\log_b n$ = livello delle foglie; $a^{\log_b n}$ = numero di foglie.

> 🧩 Derivazione mia dell'identità $a^{\log_b n} = n^{\log_b a}$: $\log_b\left(a^{\log_b n}\right) = \log_b n \cdot \log_b a = \log_b\left(n^{\log_b a}\right)$, e $\log_b$ è iniettivo. Serve a scrivere il numero di foglie come potenza di $n$.

## Derivazioni

### Esempio 1 — merge sort, $T(n) = 2T(n/2) + cn$
> 📄 Fonte: [[06-Merge Sort (1).pdf#page=25]]

L'albero ha $\lg n + 1$ livelli, ciascuno di costo $cn$: totale $cn(\lg n + 1) = \Theta(n\lg n)$. Derivazione livello per livello in [[merge-sort]] § Soluzione con l'albero di ricorsione.

### Esempio 2 — $T(n) = 3T(\lfloor n/4 \rfloor) + \Theta(n^2)$
> 📄 Fonte: [[06-Merge Sort (1).pdf#page=32]]–[[06-Merge Sort (1).pdf#page=35]] (l'albero è costruito un passo per slide: a p. 32 c'è solo $T(n)$, a [[06-Merge Sort (1).pdf#page=33|p. 33]] e [[06-Merge Sort (1).pdf#page=34|p. 34]] si espandono i livelli, a p. 35 l'albero è completo)

Consideriamo $T(n) = 3T(\lfloor n/4 \rfloor) + \Theta(n^2)$. Costruiamo l'albero di ricorrenza per $T(n) = 3T(n/4) + cn^2$:
- ignoriamo l'arrotondamento per difetto (approssimazione);
- supponiamo che $n$ sia una potenza di 4 (approssimazione);
- esplicitiamo il coefficiente costante $c$.

![[06-merge-sort-p35-albero-3t-n4.png]]
*Espansione: la radice $cn^2$ ha tre figli $T(n/4)$; espandendo, ogni $c(n/4)^2$ ha tre figli $T(n/16)$. ([[06-Merge Sort (1).pdf#page=35]])*

**Quanti livelli ha l'albero?** ([[06-Merge Sort (1).pdf#page=36]]) Per un nodo a livello $i$ (il livello della radice è zero), la dimensione dei (sotto)problemi è $n/4^i$. La dimensione 1 si raggiunge per $n/4^i = 1$, ovvero $i = \log_4 n$. L'albero ha quindi $\log_4 n + 1$ livelli.

**Qual è il costo a ciascun livello?** ([[06-Merge Sort (1).pdf#page=37]]) Ogni livello ha il triplo dei nodi del livello precedente, quindi il numero di nodi a livello $i$ è $3^i$. Al livello $i$, il costo di un singolo nodo è $c(n/4^i)^2$.

![[06-merge-sort-p37-albero-costo-livelli.png]]

**Somma** ([[06-Merge Sort (1).pdf#page=38]]):
$$
\begin{aligned}
T(n) &= \sum_{i=0}^{\log_4 n - 1} 3^i c\left(\frac{n}{4^i}\right)^2 + 3^{\log_4 n}\, T(1) = \sum_{i=0}^{\log_4 n - 1}\left(\frac{3}{16}\right)^i cn^2 + \Theta\!\left(n^{\log_4 3}\right) \\
     &< \sum_{i=0}^{\infty}\left(\frac{3}{16}\right)^i cn^2 + \Theta\!\left(n^{\log_4 3}\right) = \frac{1}{1 - (3/16)}\, cn^2 + \Theta\!\left(n^{\log_4 3}\right) = \frac{16}{13}\, cn^2 + \Theta\!\left(n^{\log_4 3}\right) \\
     &\Rightarrow\ T(n) = O(n^2)
\end{aligned}
$$

![[06-merge-sort-p38-albero-somma.png]]

> 🧩 Derivazione mia — i passaggi della somma, uno per riga:
$$
\begin{aligned}
\text{livelli interni } (0 \le i \le \log_4 n - 1):\ \ 3^i \cdot c\frac{n^2}{16^i} &= \left(\tfrac{3}{16}\right)^i cn^2 && (4^i)^2 = 16^i \\
\text{foglie } (i = \log_4 n):\ \ 3^{\log_4 n} \cdot T(1) &= n^{\log_4 3}\, T(1) = \Theta\!\left(n^{\log_4 3}\right) && \text{identità sopra, } T(1) \text{ costante} \\
\sum_{i=0}^{\log_4 n - 1}\left(\tfrac{3}{16}\right)^i &< \sum_{i=0}^{\infty}\left(\tfrac{3}{16}\right)^i && \text{termini positivi: aggiungerne aumenta la somma} \\
\sum_{i=0}^{\infty} x^i &= \frac{1}{1-x}\ \ (|x| < 1) && \text{serie geometrica, } x = \tfrac{3}{16} \\
\frac{1}{1 - 3/16} &= \frac{1}{13/16} = \frac{16}{13} \approx 1.23 \\
\log_4 3 &\approx 0.79 < 2 \ \Rightarrow\ \Theta\!\left(n^{\log_4 3}\right) = O(n^2) && \text{le foglie sono trascurabili}
\end{aligned}
$$
> Il costo è **dominato dalla radice**: i livelli decrescono geometricamente (ognuno costa $3/16$ del precedente) e la somma è un multiplo costante del primo termine $cn^2$.

### Verifica per sostituzione
> 📄 Fonte: [[06-Merge Sort (1).pdf#page=39]]

Verifichiamo con il [[metodo-di-sostituzione]] che $T(n) = O(n^2)$, ovvero $\exists\, d > 0 : T(n) \le dn^2$. Passo induttivo (assumiamo vero per $\lfloor n/4 \rfloor$, dimostriamo per $n$), con i commenti miei (🧩):

$$
\begin{aligned}
T(n) &= 3T(\lfloor n/4 \rfloor) + \Theta(n^2) && \text{ricorrenza originale, con le parti intere} \\
     &\le 3T(\lfloor n/4 \rfloor) + cn^2 && c \text{ = costante superiore del } \Theta(n^2) \\
     &\le 3d\lfloor n/4 \rfloor^2 + cn^2 && \text{ipotesi induttiva} \\
     &\le 3d(n/4)^2 + cn^2 && \lfloor n/4 \rfloor \le n/4 \\
     &= (3/16)dn^2 + cn^2 && \\
     &\le dn^2 && \text{se } d \ge (16/13)c
\end{aligned}
$$

Per $n = 1$ (caso base), $T(1) \le d$: verificato quindi per $d \ge T(1)$.

![[06-merge-sort-p39-verifica-sostituzione.png]]

> 🧩 Derivazione mia — l'ultima riga: $\frac{3}{16}dn^2 + cn^2 \le dn^2 \iff cn^2 \le \frac{13}{16}dn^2 \iff d \ge \frac{16}{13}c$. È la stessa costante $\frac{16}{13}$ della somma dell'albero: la soluzione di tentativo e la verifica coincidono.
>
> **Sanity check** ([[divide_et_impera.py]], con $c = 1$ e $T$ calcolata esattamente con le parti intere): $\max_{1 \le n \le 10^5} T(n)/n^2 = 1.2308 \approx 16/13$, e anche per la potenza di 4 $n = 4^8$ il rapporto è $1.2308$.
>
> Precisazione (🧩): per $n = 2, 3$ si ha $\lfloor n/4 \rfloor = 0$, fuori dal dominio dell'induzione; anche $n = 2$ e $n = 3$ vanno trattati come casi base, scegliendo $d \ge \max(T(1), T(2)/4, T(3)/9)$.

### Anche limite inferiore
> 📄 Fonte: [[06-Merge Sort (1).pdf#page=40]]

Con il metodo di sostituzione abbiamo verificato che $T(n) = O(n^2)$. In realtà è anche $T(n) = \Omega(n^2)$: la prima chiamata ricorsiva contribuisce con un costo $\Theta(n^2)$ e quindi $\Omega(n^2)$ è un limite inferiore per la ricorrenza. Quindi $T(n) = \Theta(n^2)$.

> 🧩 In formula: $T(n) \ge cn^2$ perché il termine non ricorsivo della radice, da solo, vale già $cn^2$ e gli altri termini sono non negativi.

### Esempio 3 — quicksort con partizione 9:1
> 📄 Fonte: [[07-Quicksort 1.pdf#page=16]], [[07-Quicksort 1.pdf#page=17]]

$T(n) \le T(9n/10) + T(n/10) + cn$: l'albero non è bilanciato, ma ogni livello costa al più $cn$ e la profondità è $\log_{10/9} n = \Theta(\lg n)$, quindi $O(n\lg n)$. Derivazione in [[quicksort]] § Partizionamento con rapporto costante. Lo stesso metodo spiega il caso medio con partizioni alternate ([[07-Quicksort 1.pdf#page=18]]).

## Spiegazione

L'albero rende visibile **dove** sta il costo:
- costo uguale su ogni livello (merge sort, $cn$ per $\lg n + 1$ livelli) ⇒ costo per livello × numero di livelli: $\Theta(n\lg n)$;
- costo che decresce geometricamente dalla radice (esempio 2) ⇒ domina la radice: $\Theta(f(n))$;
- costo che cresce verso le foglie ⇒ dominano le foglie: $\Theta(n^{\log_b a})$.

> 💡 Connessione: sono esattamente i casi 2, 3 e 1 del [[teorema-dell-esperto]], che confronta $f(n)$ (radice) con $n^{\log_b a}$ (foglie).

### S&T: «Albero di ricorsione?»
> 📄 Fonte: [[06-Merge Sort (1).pdf#page=44]]

Dopo il teorema dell'esperto la lezione chiude la parte sulle ricorrenze con uno «Stop & Think» che contiene solo la domanda **«Albero di ricorsione?»**, senza altro testo.

> 🧩 Spunto mio per rispondere. L'**albero di ricorsione** è l'albero delle **chiamate**: ogni nodo è una chiamata con il suo input, i figli sono le chiamate ricorsive che fa. Per merge sort è la figura di [[06-Merge Sort (1).pdf#page=8]], con le sotto-sequenze nei nodi. L'**albero di ricorrenza** di questa pagina ha la stessa forma, ma in ogni nodo scrive il **costo** locale della chiamata invece del suo input (p. 25: $cn$, $cn/2$, …). Si passa dall'uno all'altro sostituendo a ogni nodo il termine non ricorsivo della ricorrenza calcolato sulla sua dimensione.

## Perché importa

> 🎯 Esame: disegnare l'albero di una ricorrenza, contare livelli e costo per livello, sommare con la serie geometrica; poi verificare per sostituzione con la costante esplicita ($d \ge \frac{16}{13}c$).

## Connessioni

- [[metodo-di-sostituzione]] — verifica le soluzioni di tentativo dell'albero
- [[teorema-dell-esperto]] — generalizza i tre comportamenti dell'albero
- [[merge-sort]], [[quicksort]] — gli alberi delle lezioni 06 e 07
- [[logaritmi-nell-analisi]] — il numero di livelli è un logaritmo nella base del fattore di riduzione
- [[risoluzione-ricorrenze]] — esercizi
- [[albero]] — gli alberi di ricorsione come caso degli alberi, insieme a cartelle ed espressioni ([[08-Grafi e alberi.pdf#page=44]])

## Fonti

- [[lezione-06-merge-sort]], [[lezione-07-quicksort]]
- [[06-Merge Sort (1).pdf#page=25]], [[06-Merge Sort (1).pdf#page=31]]–[[06-Merge Sort (1).pdf#page=40]], [[07-Quicksort 1.pdf#page=16]]–[[07-Quicksort 1.pdf#page=18]]

_Aggiornato: 2026-10-01 — ingest 06-Merge Sort.pdf e 07-Quicksort.pdf_
_Aggiornato: 2026-10-10 — nuova versione delle slide (06-Merge Sort (1).pdf): numeri di pagina aggiornati_
_Aggiornato: 2026-10-14 — link ripuntati alla versione aggiornata delle slide 07-Quicksort 1.pdf_
_Aggiornato: 2026-10-28 — collegamenti alle lezioni 08–09_

<!-- nav:inizio -->
---
**Lezione 06 · pagina 7 di 8** · ← [[metodo-di-sostituzione|Metodo di sostituzione]] · [[lezioni|Indice]] · [[teorema-dell-esperto|Teorema dell'esperto (metodo dell'esperto)]] →
<!-- nav:fine -->
