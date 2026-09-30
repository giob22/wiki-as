# Overview — Algoritmi e Strutture Dati

Corso della LM in Ingegneria Informatica, UNINA, a.a. 26/27 — parte ASD del corso integrato ASD + ML ([[00-Presentazione.pdf#page=2]]). Docente: Prof. Stefano Marrone ([[00-Presentazione.pdf#page=3]]). Testo: Cormen, Leiserson, Rivest, Stein, *Introduzione agli algoritmi e strutture dati*, 3ª ed. ([[00-Presentazione.pdf#page=7]]); consigliato Skiena, *The Algorithm Design Manual* ([[00-Presentazione.pdf#page=8]]). Esame: opzione A (unica seduta integrata dopo ML) o B (ASD a fine modulo + ML dopo), voto unico 50/50 ([[00-Presentazione.pdf#page=4]]) → [[presentazione-del-corso]].

**Temi principali** ([[00-Presentazione.pdf#page=5]]): tecniche di analisi e strutture dati elementari; divide et impera; ricerca combinatoriale e metodi euristici; tecniche di analisi e strutture dati avanzate; programmazione dinamica; grafi.

Elenco lezioni e percorso di lettura → [[lezioni]] · catalogo → [[index]] · registro → [[log]]

## Argomenti coperti nel wiki

| Area | Pagine | Stato |
|------|--------|-------|
| Fondamenti: algoritmo, correttezza, efficienza | [[algoritmo-e-problema]], [[efficienza-degli-algoritmi]], [[ordinamento]] | completo per la fonte |
| Ordinamento elementare | [[insertion-sort]], [[selection-sort]] | completo per la fonte |
| Crescita delle funzioni: stringhe e logaritmi | [[substring-pattern-matching]], [[findmatch]], [[logaritmi-nell-analisi]], [[potenza-veloce]] | completo per la fonte |
| Progettazione: famiglie di approcci | [[paradigmi-di-progettazione]], [[divide-et-impera]], [[ricerca-combinatoria]], [[metodi-euristici]] | introduttivo (come nelle slide) |
| Problemi d'esempio e loro algoritmi | [[robot-tour-optimization]], [[movie-scheduling]] e 7 algoritmi | completo per la fonte |
| Correttezza | [[ricerca-di-controesempi]], [[invariante-di-ciclo]], [[correttezza-per-induzione]], [[iterazione-e-ricorsione]] | completo per la fonte |
| Analisi di complessità | [[modello-ram]], [[tempo-di-esecuzione]], [[casi-di-complessita]], [[equazioni-di-ricorrenza]], [[somma-iterativa]], [[somma-ricorsiva]] | completo per la fonte |
| Notazione asintotica | [[notazione-asintotica]], [[regole-di-calcolo-asintotico]], [[dominanza-asintotica]] | completo per la fonte |
| Strutture dati elementari | [[tipo-di-dato-astratto]], [[strutture-contigue-e-collegate]], [[array]], [[array-dinamico]], [[lista-concatenata]], [[pila]], [[coda]] | completo per la fonte |
| Pseudocodice | [[pseudocodice]] | completo |

**Filo logico finora.** Un algoritmo è corretto se termina con l'uscita giusta su **ogni** istanza ([[algoritmo-e-problema]]). La lezione 01 mostra quanto sia facile sbagliare: euristiche ragionevoli per il commesso viaggiatore e per lo scheduling cadono su controesempi, la ricerca esaustiva è corretta ma esponenziale, e solo per lo scheduling esiste una regola greedy corretta ed efficiente ([[metodi-euristici]], [[ricerca-combinatoria]], [[optimal-scheduling]]). La lezione 03 fornisce gli strumenti per stabilire la correttezza: controesempi per smentirla, invarianti e induzione per dimostrarla. L'efficienza si misura contando i passi nel [[modello-ram]] ([[tempo-di-esecuzione]]), di norma nel caso peggiore ([[casi-di-complessita]]), e si riassume con $O$, $\Omega$, $\Theta$ ([[notazione-asintotica]]). Ciò che conta è l'ordine di crescita ([[dominanza-asintotica]]): per $n$ grandi un algoritmo $n\log n$ batte qualunque macchina più veloce con un algoritmo $n^2$. La lezione 04 introduce i mattoni: array e liste, e sopra di essi pile e code con operazioni $O(1)$. La lezione 05 applica tutto a un algoritmo vero, insertion sort: correttezza con l'invariante, costo riga per riga, caso migliore lineare e caso peggiore quadratico. Aggiunge selection sort come esercizio e mostra da dove nascono i logaritmi.

## Argomenti mancanti / da ingerire

- Syllabus del corso (link di [[00-Presentazione.pdf#page=5]]) — TODO
- Ricerca binaria (citata in [[05-Insertion sort.pdf#page=32]], pseudocodice non ancora presentato) — lezioni future
- Algoritmi divide et impera concreti (merge sort citato in [[01-Introduzione.pdf#page=11]]) e ricorrenze di tipo $T(n) = aT(n/b) + f(n)$ — lezioni future
- Heap, tabelle hash, alberi (citati in [[04-Strutture dati elementari.pdf#page=5]]), grafi e DFS/BFS ([[04-Strutture dati elementari.pdf#page=29]]), programmazione dinamica — lezioni future

## Fonti ingerite

7 — [[presentazione-del-corso]], [[lezione-01-introduzione]], [[lezione-02-notazione-asintotica]], [[lezione-03-analisi-di-algoritmi]], [[lezione-04-strutture-dati-elementari]], [[lezione-05-insertion-sort]], [[convenzioni-per-lo-pseudocodice]]

_Aggiornato: 2026-09-26 — ingest di tutto il materiale in raw/ tranne 05-Insertion sort.pdf_
_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_
