---
tipo: fonte
titolo: "Corso di Algoritmi e Strutture Dati — Analisi di correttezza e di complessità degli algoritmi"
file_raw: "03-Analisi di algoritmi.pdf"
pagine: "1-34"
data_ingest: 2026-09-26
formato: slide-pdf
argomenti: [paradigmi di progettazione, iterazione e ricorsione, correttezza, controesempi, invariante di ciclo, induzione, analisi di complessità, ricorrenze]
---

# Lezione 03 — Analisi di correttezza e di complessità (03-Analisi di algoritmi.pdf)

## Sommario

La lezione ha quattro parti. **Classificazione dei problemi**: tre famiglie di approcci (divide et impera, ricerca combinatoria, metodi euristici) che bilanciano tempo, qualità e scalabilità. **Caratterizzazione degli algoritmi**: iterazione contro ricorsione, con l'esempio della somma dei primi $n$ numeri in entrambe le forme. **Correttezza**: controesempi e testing per dimostrare l'incorrettezza (con cinque suggerimenti pratici), invariante di ciclo per gli algoritmi iterativi, induzione per quelli ricorsivi, applicati alla somma. **Analisi di complessità**: il costo riga per riga della somma iterativa ($2n + 4 = O(n)$) e la ricorrenza $T(n) = T(n-1) + c$ della somma ricorsiva ($1 + cn = O(n)$), con la domanda aperta sulla complessità spaziale.

## Percorso della lezione · [[03-Analisi di algoritmi.pdf|03-Analisi di algoritmi.pdf]]

**PDF:** (pp. 1–35)

Pagine del wiki nell'ordine di prima comparsa nelle slide (è l'ordine delle pagine di questa lezione nel libro, dopo questa):
1. [[paradigmi-di-progettazione]] — pp. 2–3 · tre famiglie di approcci
2. [[divide-et-impera]] — p. 4
3. [[iterazione-e-ricorsione]] — pp. 7–11 · confronto dei due stili
4. [[somma-iterativa]] — p. 11 (poi pp. 17, 23–29) · pseudocodice, invariante, costo $2n+4$
5. [[somma-ricorsiva]] — p. 11 (poi pp. 19, 30–34) · pseudocodice, induzione, ricorrenza
6. [[correttezza-parziale-e-totale]] — p. 16 (con la definizione di 01 p. 9) · parziale = «se termina, è giusto»; totale = parziale + terminazione; quale strumento dimostra cosa
7. [[invariante-di-ciclo]] — pp. 16–17
8. [[correttezza-per-induzione]] — pp. 18–19
9. [[dimostrazioni-di-correttezza]] — esercizio su invariante e induzione
10. [[analisi-del-costo-riga-per-riga]] — esercizio sulle pp. 23–29 (e su Base/Base2 della lezione 02)
11. [[equazioni-di-ricorrenza]] — pp. 30–35
12. [[risoluzione-ricorrenze]] — esercizio sulle pp. 30–33

Già lette: *ricerca-combinatoria* (p. 5), *metodi-euristici* (p. 6), *ricerca-di-controesempi* (pp. 12–15) nella lezione 01; *modello-ram* e *tempo-di-esecuzione* (pp. 20–22, identiche alle pp. 2–3 della lezione 02) nella lezione 02.

**Ordine consigliato.**
Qui le slide non sono lineari rispetto alle pagine: la somma $1..n$ compare a p. 11, ma la sua correttezza (pp. 17–19) e la sua complessità (pp. 23–35) arrivano molto dopo, e le pagine delle due somme contengono già tutto. Conviene prima la **teoria** e poi gli **esempi**:

1. *paradigmi-di-progettazione* → *divide-et-impera* → *iterazione-e-ricorsione*
2. *correttezza-parziale-e-totale* (il quadro) → *invariante-di-ciclo* → *correttezza-per-induzione* (gli strumenti)
3. *equazioni-di-ricorrenza* (complessità ricorsiva; la parte iterativa è in *tempo-di-esecuzione*, già letta)
4. *somma-iterativa* → *somma-ricorsiva* (gli esempi completi, come sintesi)
5. esercizi: *dimostrazioni-di-correttezza* → *analisi-del-costo-riga-per-riga* → *risoluzione-ricorrenze*

## Punti chiave · [[03-Analisi di algoritmi.pdf#page=3|p. 3]], [[03-Analisi di algoritmi.pdf#page=6|p. 6]], [[03-Analisi di algoritmi.pdf#page=8|p. 8]]–[[03-Analisi di algoritmi.pdf#page=11|11]], [[03-Analisi di algoritmi.pdf#page=13|p. 13]], [[03-Analisi di algoritmi.pdf#page=15|p. 15]]–[[03-Analisi di algoritmi.pdf#page=19|19]], [[03-Analisi di algoritmi.pdf#page=21|p. 21]]–[[03-Analisi di algoritmi.pdf#page=23|23]], [[03-Analisi di algoritmi.pdf#page=29|p. 29]], [[03-Analisi di algoritmi.pdf#page=30|30]], [[03-Analisi di algoritmi.pdf#page=35|p. 35]]

1. Tre famiglie di progettazione → [[paradigmi-di-progettazione]], [[divide-et-impera]], [[ricerca-combinatoria]], [[metodi-euristici]].
2. Iterazione contro ricorsione: stesso potere espressivo, costi e chiarezza diversi → [[iterazione-e-ricorsione]].
3. Esempio: somma di $1..n$ iterativa e ricorsiva → [[somma-iterativa]], [[somma-ricorsiva]].
4. Incorrettezza: controesempi, testing, tips (think small, think exhaustively, hunt for the weakness, go for a tie, seek extremes); nessun controesempio ≠ correttezza → [[ricerca-di-controesempi]].
5. Invariante di ciclo: inizializzazione, conservazione, conclusione + terminazione con funzione variante → [[invariante-di-ciclo]].
6. Ricorsione: specifiche, misura ben fondata, casi base, passo induttivo, terminazione → [[correttezza-per-induzione]].
7. Analisi: risorse, modello, dimensione dell'input, costo riga × esecuzioni → [[tempo-di-esecuzione]], [[modello-ram]].
8. Somma iterativa: $1 + 1 + (n+1) + n + 1 = 2n + 4 = O(n)$ → [[analisi-del-costo-riga-per-riga]].
9. Somma ricorsiva: $T(0) = 1$, $T(i) = T(i-1) + c$, $T(n) = 1 + cn = O(n)$ → [[equazioni-di-ricorrenza]], [[risoluzione-ricorrenze]].

## Refusi e note · [[03-Analisi di algoritmi.pdf#page=1|p. 1]], [[03-Analisi di algoritmi.pdf#page=2|2]], [[03-Analisi di algoritmi.pdf#page=7|p. 7]], [[03-Analisi di algoritmi.pdf#page=12|p. 12]], [[03-Analisi di algoritmi.pdf#page=20|p. 20]]

- p. 5: il punto «Spesso efficienti se la partizione è bilanciata» nella ricerca combinatoria sembra copiato dalla slide su divide et impera (p. 4) e contrasta con «complessità tipicamente esponenziale».
- p. 17: «Inizializzazione: $i = 0$» → dovrebbe essere $i = 1$ (il ciclo parte da 1).
- pp. 29 e 34: «E la complessità spaziale?» senza risposta → nel wiki: $\Theta(1)$ iterativa, $\Theta(n)$ ricorsiva (🧩).
- p. 28: il risultato è dato come $O(n)$; vale anche $\Theta(n)$.
- Pseudocodice in italiano (`funzione`, `per … da … a`, `ritorna`), diverso dalle convenzioni di a1.
- Pagina del titolo: p. 1; pagine di intestazione: p. 2, p. 7, p. 12, p. 20.

## Concetti introdotti

[[paradigmi-di-progettazione]], [[divide-et-impera]], [[ricerca-combinatoria]], [[metodi-euristici]], [[iterazione-e-ricorsione]], [[ricerca-di-controesempi]], [[invariante-di-ciclo]], [[correttezza-per-induzione]], [[tempo-di-esecuzione]], [[equazioni-di-ricorrenza]], [[somma-iterativa]], [[somma-ricorsiva]]

## Domande aperte

- Complessità spaziale: la risposta attesa dal docente è quella della profondità della ricorsione?
- Gli esempi concreti di divide et impera arriveranno nelle prossime lezioni.

## Domande da esame

- Confronta divide et impera, ricerca combinatoria ed euristiche (garanzie, costo, quando usarle).
- Pro e contro di iterazione e ricorsione.
- Come si dimostra l'incorrettezza di un algoritmo? Elenca i tips per trovare controesempi.
- Enuncia i passi di una prova con invariante di ciclo e applicali a `somma_iterativa`.
- Dimostra per induzione la correttezza di `somma_ricorsiva`.
- Calcola il costo di `somma_iterativa` riga per riga e risolvi la ricorrenza di `somma_ricorsiva`; confronta anche lo spazio.

_Aggiornato: 2026-09-26 — ingest 03-Analisi di algoritmi.pdf_
_Aggiornato: 2026-10-28 — aggiunto il «Percorso della lezione» (spostato dall'indice lezioni.md)_

<!-- nav:inizio -->
---
**Lezione 03 · pagina 1 di 13** · ← [[dominanza-asintotica|Dominanza asintotica, little-o e crescita delle funzioni]] · [[lezioni|Indice]] · [[paradigmi-di-progettazione|Paradigmi (famiglie) di progettazione degli algoritmi]] →
<!-- nav:fine -->
