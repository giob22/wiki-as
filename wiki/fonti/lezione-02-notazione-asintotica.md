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

## Sommario

Slide in inglese di Steven Skiena (Stony Brook) con inserti in italiano del Prof. Marrone ([[02-Notazione asintotica.pdf#page=1]]). La lezione fissa il **modello RAM** (ogni operazione semplice e ogni accesso in memoria costano un passo) e definisce i casi **peggiore, migliore e medio** come funzioni «tempo contro dimensione»; il corso userà di norma il caso peggiore. Poiché l'analisi esatta è difficile, si introducono i limiti superiori e inferiori $O$, $\Omega$, $\Theta$ con definizioni formali (costanti $c$ e soglia $n_0$), esempi su $3n^2 - 100n + 6$, regole per somme, costanti e prodotti e proprietà (transitiva, riflessiva, simmetrica, trasposta). Chiude la **dominanza asintotica** (little-o, test del limite, classifiche di crescita) con la tabella dei tempi a 1 ns per operazione.

## Punti chiave

1. Analisi = stima di memoria, banda, tempo; modello: singolo processore, memoria ad accesso casuale, nessuna gerarchia; operazioni a tempo costante ([[02-Notazione asintotica.pdf#page=2]]) → [[modello-ram]].
2. Tempo in funzione della dimensione dell'input; somma dei costi di riga × esecuzioni ([[02-Notazione asintotica.pdf#page=3]]) → [[tempo-di-esecuzione]].
3. Modello RAM: operazioni semplici e accessi = 1 passo; cicli e chiamate no; «flat-earth model» ([[02-Notazione asintotica.pdf#page=5]], [[02-Notazione asintotica.pdf#page=6]]).
4. Esempi `Base()` e `Base2(n)` per i casi fortunato/sfortunato ([[02-Notazione asintotica.pdf#page=7]], [[02-Notazione asintotica.pdf#page=11]]); efficienza asintotica = conta solo l'ordine di crescita ([[02-Notazione asintotica.pdf#page=8]]).
5. Definizioni dei casi e posizione del corso: caso peggiore salvo indicazione contraria; algoritmi randomizzati → caso medio ([[02-Notazione asintotica.pdf#page=9]]–[[02-Notazione asintotica.pdf#page=12]]) → [[casi-di-complessita]].
6. $O$, $\Omega$, $\Theta$: nomi, figure, definizioni formali ([[02-Notazione asintotica.pdf#page=15]]–[[02-Notazione asintotica.pdf#page=18]]) → [[notazione-asintotica]].
7. Esempi su $3n^2 - 100n + 6$ ([[02-Notazione asintotica.pdf#page=21]]–[[02-Notazione asintotica.pdf#page=23]]) → [[dimostrazioni-notazione-asintotica]].
8. Somma/differenza, costante, prodotto ([[02-Notazione asintotica.pdf#page=24]]–[[02-Notazione asintotica.pdf#page=26]]) → [[regole-di-calcolo-asintotico]].
9. Notazione nelle equazioni e proprietà ([[02-Notazione asintotica.pdf#page=27]]).
10. Dominanza: razzo contro vela solare, implicazioni pratiche, little-o e limite, proprietà, tabella di crescita, classifiche ([[02-Notazione asintotica.pdf#page=30]]–[[02-Notazione asintotica.pdf#page=37]]) → [[dominanza-asintotica]].

## Refusi e note

- p. 16 contro p. 18: $C_1$/$C_2$ con ruoli scambiati (upper/lower) → segnalato in [[notazione-asintotica]].
- p. 21: «$c \cdot n < 3n^2$ when $n > c$» trascura i termini di ordine inferiore; la versione precisa è $n > (100 + c)/3$.
- p. 27: «Anti-simmetrica» = simmetria trasposta del Cormen.
- p. 36: arrotondamenti ($n\lg n$ con $n = 10^4$: 130 µs nella slide, 132.9 µs esatti).
- p. 7 e p. 11 usano uno pseudocodice diverso dalle convenzioni del corso (`SE/ALTRIMENTI/PER`, commenti `//`).
- Pagina del titolo: [[02-Notazione asintotica.pdf#page=1|1]]; pagine di sola intestazione o «Questions?»: [[02-Notazione asintotica.pdf#page=4|4]], [[02-Notazione asintotica.pdf#page=13|13]], [[02-Notazione asintotica.pdf#page=14|14]], [[02-Notazione asintotica.pdf#page=19|19]], [[02-Notazione asintotica.pdf#page=20|20]], [[02-Notazione asintotica.pdf#page=28|28]], [[02-Notazione asintotica.pdf#page=29|29]], [[02-Notazione asintotica.pdf#page=32|32]], [[02-Notazione asintotica.pdf#page=33|33]], [[02-Notazione asintotica.pdf#page=38|38]].

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
