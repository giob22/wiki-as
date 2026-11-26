---
tipo: concetto
importanza_esame: alta
prerequisiti: ["paradigmi-di-progettazione"]
fonti_pdf: ["03-Analisi di algoritmi.pdf#page=5", "01-Introduzione.pdf#page=29", "01-Introduzione.pdf#page=58"]
---

# Ricerca combinatoria (ricerca esaustiva)

## Definizione · [[03-Analisi di algoritmi.pdf#page=4|p. 4]], [[03-Analisi di algoritmi.pdf#page=5|5]]

Gli algoritmi di ricerca combinatoria **esplorano uno spazio di soluzioni discrete** (spesso enorme) in modo **sistematico**, con **potature** basate su vincoli o limiti. Mirano all'**ottimo garantito**, ma il costo può crescere **esponenzialmente**.

Esempi classici: **commesso viaggiatore**, **zaino**, «…».

Caratteristiche della soluzione:
- **completezza e ottimalità** (se non si tronca la ricerca);
- «spesso efficienti se la partizione è bilanciata»;
- **complessità tipicamente esponenziale**;
- adatti a istanze **piccole/medie** o quando serve **certificare l'ottimo**.

> ⚠️ Contraddizione: il punto «spesso efficienti se la partizione è bilanciata» è identico a quello della slide su [[divide-et-impera]] e contrasta con «complessità tipicamente esponenziale» della stessa slide: probabile residuo di copia-incolla. Da chiedere al docente.

## Formule · [[01-Introduzione.pdf#page=29|p. 29]], [[01-Introduzione.pdf#page=58|p. 58]]

Le due ricerche esaustive viste nella lezione 01:

| Algoritmo | Spazio esplorato | Dimensione |
|---|---|---|
| [[optimal-tsp]] | permutazioni di $n$ punti | $n!$ |
| [[exhaustive-scheduling]] | sottoinsiemi di $n$ intervalli | $2^n$ |

## Derivazioni

### Derivazione — perché $n!$ permutazioni e $2^n$ sottoinsiemi · [[01-Introduzione.pdf#page=29|p. 29]], [[01-Introduzione.pdf#page=33|p. 33]], [[01-Introduzione.pdf#page=58|p. 58]], [[01-Introduzione.pdf#page=59|59]]

> 🧩 Derivazione mia:
- **Permutazioni:** il primo punto del giro si sceglie in $n$ modi, il secondo tra gli $n-1$ rimasti, …, l'ultimo in 1 modo: $n\cdot(n-1)\cdots 1 = n!$.
- **Sottoinsiemi:** ogni intervallo è dentro o fuori dal sottoinsieme, 2 scelte indipendenti per ciascuno degli $n$ intervalli: $2\cdot 2\cdots 2 = 2^n$.

Nel movie scheduling l'ordine dei film scelti non conta («Non ci interessa delle permutazioni!! (l'ordine non è importante)»): per questo basta enumerare i sottoinsiemi, e $2^n \ll n!$.

**Numeri:** $2^{20} = 1\,048\,576 \approx 1\text{M}$, $2^{100} \approx 1.27 \cdot 10^{30}$ (la slide scrive $1.26\cdot10^{30}$, troncamento di $1.2677\cdot10^{30}$); $20! = 2\,432\,902\,008\,176\,640\,000 \approx 2.4\cdot 10^{18}$. Verificati con [[tempi_crescita.py]].

## Spiegazione · [[02-Notazione asintotica.pdf#page=36|p. 36]]

La ricerca esaustiva è il modo più semplice di ottenere un algoritmo **corretto**: considera tutte le possibilità e sceglie la migliore. Il prezzo è il tempo: già per $n = 20$ punti le $20!$ permutazioni richiederebbero circa 77 anni a $10^9$ permutazioni al secondo (cfr. riga $n = 20$, colonna $n!$ della tabella di p. 36).

## Perché importa · [[00-Presentazione.pdf#page=5|p. 5]]

Fa parte del programma («Ricerca combinatoriale, Metodi euristici») ed è il riferimento esatto con cui si misurano le euristiche.

## Connessioni

- [[backtracking]] — il modo sistematico di implementare una ricerca esaustiva con potatura (lezione 15)

- [[metodi-euristici]] — l'alternativa veloce senza garanzie
- [[dominanza-asintotica]] — $n! \gg 2^n$: spiega perché l'esaustivo sui sottoinsiemi è «meglio» ma resta proibitivo
- [[paradigmi-di-progettazione]]

## Fonti · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=5|p. 5]] · 01-Introduzione.pdf [[01-Introduzione.pdf#page=29|p. 29]], [[01-Introduzione.pdf#page=58|p. 58]], [[01-Introduzione.pdf#page=59|59]]

- [[lezione-03-analisi-di-algoritmi]], [[lezione-01-introduzione]]

_Aggiornato: 2026-09-26 — ingest 01-Introduzione.pdf e 03-Analisi di algoritmi.pdf_

<!-- nav:inizio -->
---
**Lezione 01 · pagina 10 di 18** · ← [[optimal-tsp|OptimalTSP (Soluzione 3 del Robot Tour)]] · [[lezioni|Indice]] · [[metodi-euristici|Metodi euristici (e differenza tra algoritmi ed euristiche)]] →
<!-- nav:fine -->
