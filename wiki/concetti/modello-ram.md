---
tipo: concetto
importanza_esame: alta
prerequisiti: ["algoritmo-e-problema"]
fonti_pdf: ["02-Notazione asintotica.pdf#page=5", "02-Notazione asintotica.pdf#page=6", "02-Notazione asintotica.pdf#page=2", "03-Analisi di algoritmi.pdf#page=21"]
---

# Modello di calcolo RAM

## Definizione

> 📄 Fonte: [[02-Notazione asintotica.pdf#page=5]], [[02-Notazione asintotica.pdf#page=6]]

Gli algoritmi si possono studiare in modo **indipendente dalla macchina e dal linguaggio** perché tutte le analisi usano il **modello di calcolo RAM** (*Random Access Machine*):

- ogni operazione **«semplice»** ($+$, $-$, $=$, `if`, `call`) richiede **1 passo**;
- **cicli** e **chiamate a sottoprogrammi** *non* sono operazioni semplici: dipendono dalla dimensione dei dati e dal contenuto del sottoprogramma. «Sort» non è un'operazione a passo singolo;
- ogni **accesso alla memoria** richiede esattamente **1 passo**.

Il tempo di esecuzione di un algoritmo si misura **contando il numero di passi**.

> «This model is useful and accurate in the same sense as the flat-earth model (which *is* useful)!» ([[02-Notazione asintotica.pdf#page=6]])

> 📄 Fonte: [[02-Notazione asintotica.pdf#page=2]] = [[03-Analisi di algoritmi.pdf#page=21]] (slide identiche)

Per analizzare un algoritmo occorre definire il **modello del calcolatore**: **singolo processore**, **memoria ad accesso casuale**, **assenza di gerarchie di memoria**. Assunzione: le istruzioni **aritmetiche**, di **accesso alla memoria** e di **controllo** richiedono un **tempo costante**.

## Spiegazione

Il paragone con la «terra piatta» dice due cose: il modello è **falso** in senso stretto (una moltiplicazione costa più di un'addizione, un accesso in cache costa molto meno di uno in RAM, esistono più core) ma è **utile** perché, sulle scale che interessano, gli errori che introduce sono **costanti moltiplicative**, che la [[notazione-asintotica]] ignora comunque.

> 🧩 Derivazione mia: se ogni operazione reale costa tra $a$ e $b$ unità di tempo ($0 < a \le b$ costanti), e il modello conta $f(n)$ passi, il tempo reale $t(n)$ soddisfa $a\,f(n) \le t(n) \le b\,f(n)$, cioè $t(n) = \Theta(f(n))$: l'ordine di crescita calcolato nel modello RAM è quello vero.

> 💡 Connessione: «assenza di gerarchie di memoria» è proprio l'ipotesi che le strutture dati contigue violano a loro vantaggio: la località degli [[array]] sfrutta la cache ([[04-Strutture dati elementari.pdf#page=8]]), effetto invisibile nel modello RAM.

## Perché importa

È l'ipotesi su cui poggiano **tutte** le analisi del corso ([[tempo-di-esecuzione]], [[casi-di-complessita]]). Nello pseudocodice, una chiamata come `sort` non costa 1 ([[02-Notazione asintotica.pdf#page=5]]) — da ricordare quando si usano funzioni di libreria ([[a1-indicazioni_psuedocodice.pdf#page=4]]).

> 🎯 Esame: elencare le ipotesi del modello (costo unitario delle operazioni semplici e degli accessi, cicli/chiamate non elementari, singolo processore, niente gerarchie di memoria).

## Connessioni

- [[tempo-di-esecuzione]] — il conteggio dei passi riga per riga
- [[notazione-asintotica]] — rende irrilevanti le costanti che il modello approssima

## Fonti

- [[lezione-02-notazione-asintotica]], [[lezione-03-analisi-di-algoritmi]]
- [[02-Notazione asintotica.pdf#page=2]], [[02-Notazione asintotica.pdf#page=5]], [[02-Notazione asintotica.pdf#page=6]], [[03-Analisi di algoritmi.pdf#page=21]]

_Aggiornato: 2026-09-26 — ingest 02-Notazione asintotica.pdf e 03-Analisi di algoritmi.pdf_
