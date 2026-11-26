---
tipo: fonte
titolo: "Lecture 2: Asymptotic Notation (Skiena, integrata dal Prof. Marrone)"
file_raw: "02-Notazione asintotica.pdf"
pagine: "1-38"
data_ingest: 2026-09-26
formato: slide-pdf
argomenti: [modello RAM, analisi di un algoritmo, casi peggiore/migliore/medio, O, Omega, Theta, regole di calcolo, dominanza, crescita delle funzioni]
---

# Lezione 02 — Notazione asintotica (02-Notazione asintotica.pdf)

## Sommario · [[02-Notazione asintotica.pdf#page=1|p. 1]]

Slide in inglese di Steven Skiena (Stony Brook) con inserti in italiano del Prof. Marrone. La lezione fissa il **modello RAM** (ogni operazione semplice e ogni accesso in memoria costano un passo) e definisce i casi **peggiore, migliore e medio** come funzioni «tempo contro dimensione»; il corso userà di norma il caso peggiore. Poiché l'analisi esatta è difficile, si introducono i limiti superiori e inferiori $O$, $\Omega$, $\Theta$ con definizioni formali (costanti $c$ e soglia $n_0$), esempi su $3n^2 - 100n + 6$, regole per somme, costanti e prodotti e proprietà (transitiva, riflessiva, simmetrica, trasposta). Chiude la **dominanza asintotica** (little-o, test del limite, classifiche di crescita) con la tabella dei tempi a 1 ns per operazione.

## Percorso della lezione · [[02-Notazione asintotica.pdf|02-Notazione asintotica.pdf]]

**PDF:** (pp. 1–38)

Pagine del wiki nell'ordine di prima comparsa nelle slide (è l'ordine delle pagine di questa lezione nel libro, dopo questa):
1. [[modello-ram]] — pp. 2, 5–6 · ipotesi del modello, «flat-earth model»
2. [[tempo-di-esecuzione]] — pp. 3, 8 · $T(n) = \sum c_i t_i(n)$, efficienza asintotica, complessità spaziale
3. [[casi-di-complessita]] — pp. 7, 9–12 · Base(), Base2(n), peggiore/migliore/medio, lotteria
4. [[notazione-asintotica]] — pp. 15–18, 21–23, 27 · $O$, $\Omega$, $\Theta$, esempi su $3n^2-100n+6$, proprietà
5. [[dimostrazioni-notazione-asintotica]] — esercizio sugli esempi di pp. 21–24
6. [[regole-di-calcolo-asintotico]] — pp. 24–26 · somma, differenza, costante, prodotto
7. [[dominanza-asintotica]] — pp. 30–37 · razzo e vela, little-o, limite, tabella di crescita, classifiche

Già letta: *stima-dei-tempi-di-esecuzione* (lezione 01) — il caso 4 ricalcola la tabella di p. 36.

**Ordine consigliato.**
Le slide alternano argomenti: modello RAM (p. 2) → tempo (p. 3) → modello RAM (pp. 5–6) → casi (p. 7) → tempo (p. 8) → casi (pp. 9–12), e le proprietà di $O$/$\Omega$/$\Theta$ (p. 27) arrivano dopo le regole di calcolo (pp. 24–26). Aggregando per pagina, l'ordine sopra è già quello consigliato: prima il modello, poi come si conta, poi quale caso, poi la notazione **completa** (proprietà incluse) e solo dopo le regole di calcolo, che la usano.

## Punti chiave · [[02-Notazione asintotica.pdf#page=2|p. 2]], [[02-Notazione asintotica.pdf#page=3|3]], [[02-Notazione asintotica.pdf#page=5|p. 5]]–[[02-Notazione asintotica.pdf#page=9|9]], [[02-Notazione asintotica.pdf#page=11|p. 11]], [[02-Notazione asintotica.pdf#page=12|12]], [[02-Notazione asintotica.pdf#page=15|p. 15]], [[02-Notazione asintotica.pdf#page=18|p. 18]], [[02-Notazione asintotica.pdf#page=21|p. 21]], [[02-Notazione asintotica.pdf#page=23|p. 23]], [[02-Notazione asintotica.pdf#page=24|24]], [[02-Notazione asintotica.pdf#page=26|p. 26]], [[02-Notazione asintotica.pdf#page=27|27]], [[02-Notazione asintotica.pdf#page=30|p. 30]], [[02-Notazione asintotica.pdf#page=37|p. 37]]

1. Analisi = stima di memoria, banda, tempo; modello: singolo processore, memoria ad accesso casuale, nessuna gerarchia; operazioni a tempo costante → [[modello-ram]].
2. Tempo in funzione della dimensione dell'input; somma dei costi di riga × esecuzioni → [[tempo-di-esecuzione]].
3. Modello RAM: operazioni semplici e accessi = 1 passo; cicli e chiamate no; «flat-earth model».
4. Esempi `Base` e `Base2(n)` per i casi fortunato/sfortunato; efficienza asintotica = conta solo l'ordine di crescita.
5. Definizioni dei casi e posizione del corso: caso peggiore salvo indicazione contraria; algoritmi randomizzati → caso medio → [[casi-di-complessita]].
6. $O$, $\Omega$, $\Theta$: nomi, figure, definizioni formali → [[notazione-asintotica]].
7. Esempi su $3n^2 - 100n + 6$ → [[dimostrazioni-notazione-asintotica]].
8. Somma/differenza, costante, prodotto → [[regole-di-calcolo-asintotico]].
9. Notazione nelle equazioni e proprietà.
10. Dominanza: razzo contro vela solare, implicazioni pratiche, little-o e limite, proprietà, tabella di crescita, classifiche → [[dominanza-asintotica]].

## Refusi e note · [[02-Notazione asintotica.pdf#page=1|p. 1]], [[02-Notazione asintotica.pdf#page=4|p. 4]], [[02-Notazione asintotica.pdf#page=13|p. 13]], [[02-Notazione asintotica.pdf#page=14|14]], [[02-Notazione asintotica.pdf#page=19|p. 19]], [[02-Notazione asintotica.pdf#page=20|20]], [[02-Notazione asintotica.pdf#page=28|p. 28]], [[02-Notazione asintotica.pdf#page=29|29]], [[02-Notazione asintotica.pdf#page=32|p. 32]], [[02-Notazione asintotica.pdf#page=33|33]], [[02-Notazione asintotica.pdf#page=38|p. 38]]

- p. 16 contro p. 18: $C_1$/$C_2$ con ruoli scambiati (upper/lower) → segnalato in [[notazione-asintotica]].
- p. 21: «$c \cdot n < 3n^2$ when $n > c$» trascura i termini di ordine inferiore; la versione precisa è $n > (100 + c)/3$.
- p. 27: «Anti-simmetrica» = simmetria trasposta del Cormen.
- p. 36: arrotondamenti ($n\lg n$ con $n = 10^4$: 130 µs nella slide, 132.9 µs esatti).
- p. 7 e p. 11 usano uno pseudocodice diverso dalle convenzioni del corso (`SE/ALTRIMENTI/PER`, commenti `//`).
- Pagina del titolo: p. 1; pagine di sola intestazione o «Questions?»: p. 4, p. 13, p. 14, p. 19, p. 20, p. 28, p. 29, p. 32, p. 33, p. 38.

## Concetti introdotti

[[modello-ram]], [[tempo-di-esecuzione]], [[casi-di-complessita]], [[notazione-asintotica]], [[regole-di-calcolo-asintotico]], [[dominanza-asintotica]]

## Domande aperte

- Il caso medio richiede una distribuzione sugli input: quale si userà per gli algoritmi randomizzati? (non trattato)
- La classifica «avanzata» di p. 37 ($\alpha(n)$, $\log n/\log\log n$) è dichiarata fuori dal corso.

## Domande da esame

- Definizione formale di $O$, $\Omega$, $\Theta$; figura con $n_0$.
- Dimostrare che $3n^2 - 100n + 6 = \Theta(n^2)$ e $\ne O(n)$ esibendo le costanti.
- Perché si preferisce il caso peggiore? Esempio in cui caso migliore e peggiore hanno ordini diversi.
- Cosa si può dire di $f + g$ e $f - g$ sapendo solo che entrambe sono $O(n^2)$?
- Quando $f$ domina $g$? Ordinare per crescita $n!, 2^n, n^3, n^2, n\log n, n, \log n, 1$.
- Ipotesi del modello RAM e perché è «utile come la terra piatta».

_Aggiornato: 2026-09-26 — ingest 02-Notazione asintotica.pdf_
_Aggiornato: 2026-10-28 — aggiunto il «Percorso della lezione» (spostato dall'indice lezioni.md)_

<!-- nav:inizio -->
---
**Lezione 02 · pagina 1 di 8** · ← [[controesempi-per-euristiche|Trovare controesempi per euristiche (greedy)]] · [[lezioni|Indice]] · [[modello-ram|Modello di calcolo RAM]] →
<!-- nav:fine -->
