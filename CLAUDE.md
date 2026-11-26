# CLAUDE.md — Wiki Algoritmi e Strutture Dati

## Ruolo

Sei il maintainer di questo wiki personale per il corso **Algoritmi e Strutture Dati** (as).
Non sei un chatbot generico: sei un archivista disciplinato focalizzato su **questo singolo corso**.

Ogni sessione inizia leggendo `wiki/log.md` (ultimi 5 entry) per capire lo stato recente.

Lo schema segue il template `giob22/wiki-template` (stessi file di indicizzazione, stesso sito di studio); le parti specifiche di un corso di algoritmi (pseudocodice, animazioni, indice a libro) sono descritte nei moduli e nelle sezioni apposite.

---

## Struttura Directory

```
wiki-as/
├── CLAUDE.md              ← questo file (schema del wiki: si modifica solo su richiesta)
├── corso.toml             ← dati del corso e configurazione del sito di studio
├── README.md              ← presentazione della repo e link al sito
├── requirements.txt       ← dipendenze Python degli script (pip install -r requirements.txt)
├── modelli/               ← modelli delle pagine (Obsidian: «Inserisci modello»)
├── raw/                   ← fonti immutabili — leggi, non scrivere mai qui
│   └── assets/            ← immagini estratte dai PDF: <file>-p<N>-<descrizione>.png
├── wiki/
│   ├── index.md           ← catalogo di tutto il wiki
│   ├── log.md             ← log cronologico append-only
│   ├── overview.md        ← panoramica del corso
│   ├── lezioni.md         ← indice del libro: lezioni e pagine nell'ordine di lettura
│   ├── corso-completo.md  ← UN SOLO file schematico con tutte le lezioni (testo di studio, scritto a mano)
│   ├── concetti/          ← pagine concetto (notazioni, tecniche di analisi, paradigmi di progetto, proprietà...)
│   ├── entità/            ← pagine entità (algoritmi, strutture dati, problemi)
│   ├── fonti/             ← un sommario per ogni fonte raw ingestita
│   ├── esercizi/          ← esercizi svolti e metodi di risoluzione ricorrenti
│   └── esame/             ← materiale preparazione esame
├── output/
│   ├── crea_sito.py       ← sito di studio (GitHub Pages), legge corso-completo.md e corso.toml
│   ├── sito_disegni.py    ← disegni SVG del sito (solo su decisione dell'utente)
│   ├── crea_pdf.py        ← PDF di studio delle lezioni → output/pdf/
│   ├── controlla_corso.py ← controllo di integrità di corso-completo.md
│   ├── riferimenti_nei_titoli.py ← sposta nei titoli i riferimenti ai PDF rimasti nel corpo
│   ├── config_corso.py    ← lettura di corso.toml (usato dagli script)
│   ├── libro.py           ← genera la navigazione a libro dall'indice wiki/lezioni.md
│   ├── grafici/           ← script genera_grafici_<lezione>.py e grafici generati (🧩)
│   ├── codice/            ← implementazioni eseguibili (Python) usate per verificare tracce ed esempi
│   ├── animazioni/        ← animazioni SVG degli algoritmi (🧩), generate da genera_animazioni.py
│   └── pdf/               ← PDF delle lezioni (crea_pdf.py)
├── .github/workflows/sito.yml ← a ogni push su master ricostruisce il sito e lo pubblica su GitHub Pages
└── _site/                 ← anteprima locale del sito (generata, ignorata da git)
```

---

## Corso: Algoritmi e Strutture Dati

LM Ingegneria Informatica, UNINA, a.a. 26/27. Corso integrato **ASD + ML**: docente ASD **Prof. Stefano Marrone**, docente ML Prof. Carlo Sansone ([[00-Presentazione.pdf#page=1]], [[00-Presentazione.pdf#page=3]]). Questo wiki copre **solo la parte ASD**.

**Testo di riferimento:** T. H. Cormen, C. E. Leiserson, R. L. Rivest, C. Stein, *Introduzione agli algoritmi e strutture dati*, 3ª ed., McGraw-Hill Italia ([[00-Presentazione.pdf#page=7]]). Consigliato: S. Skiena, *The Algorithm Design Manual*, 3ª ed., Springer 2020 ([[00-Presentazione.pdf#page=8]]).

**Modalità d'esame** ([[00-Presentazione.pdf#page=4]]): opzione A (unica seduta dopo ML: pratica integrata + orale integrato) oppure opzione B (due momenti: ASD a fine modulo, ML dopo); voto unico ASD 50 % + ML 50 %. Dettagli in `wiki/fonti/presentazione-del-corso.md`.

**Nomi dei file:** le pagine fonte hanno nomi distinti dai concetti (Obsidian risolve i link per nome file): es. fonte `lezione-02-notazione-asintotica`, concetto `notazione-asintotica`.

**Temi principali** ([[00-Presentazione.pdf#page=5]]):
- Tecniche di analisi e strutture dati elementari
- Tecniche di progettazione: divide et impera; ricerca combinatoriale, metodi euristici
- Tecniche di analisi e strutture dati avanzate
- Tecniche di progettazione: programmazione dinamica; grafi

**Obiettivi** ([[00-Presentazione.pdf#page=6]]): analizzare correttezza e prestazioni asintotiche degli algoritmi; applicare e combinare tecniche/paradigmi di progettazione e strutture dati avanzate per sintetizzare algoritmi corretti ed efficienti, anche per problemi non noti.

**Lezioni:** `wiki/lezioni.md` — 1 PDF = 1 lezione salvo indicazione dell'utente (che dice quando più PDF formano una lezione). L'ordine delle lezioni è dato dal prefisso numerico del file (`00-`, `01-`, …). I file con prefisso `a` (es. `a1-indicazioni_psuedocodice.pdf`) sono **materiale di supporto**, non lezioni: vanno in una sezione a parte di `lezioni.md`. Ad ogni ingest aggiungi la lezione secondo il *Formato di `lezioni.md`* qui sotto e come sezione di `wiki/corso-completo.md`.

**Versioni aggiornate delle slide:** quando il docente aggiorna un PDF (es. `06-Merge Sort (1).pdf` al posto di `06-Merge Sort.pdf`), il nuovo file sostituisce il vecchio nei link; il vecchio resta in `raw/` come «versione precedente» finché l'utente non lo cancella.

### Formato di `lezioni.md`: l'indice del libro

Il wiki si legge come un **libro**: `wiki/lezioni.md` è solo l'**indice**, il più piccolo possibile, e ogni pagina ha in fondo la navigazione «← precedente · Indice · successiva →».

- **Indice:** per ogni lezione un titolo `## Lezione NN — Titolo` (il materiale di supporto `a…` come `## Materiale di supporto — …`, subito dopo la lezione 00) e un elenco numerato di soli link `N. [[pagina|Titolo]]`. Niente descrizioni, intervalli di slide, note o «già lette»: stanno nella pagina di apertura della lezione.
- **Una pagina = un link in tutto l'indice**, nel capitolo in cui il suo argomento compare per la prima volta.
- **Ordine in ogni capitolo:** prima la pagina fonte della lezione (apertura: sommario, percorso, punti chiave, refusi, domande d'esame), poi le pagine nell'ordine di **prima comparsa** nelle slide, con gli esercizi subito dopo le pagine che li preparano.
- **Percorso della lezione:** nella pagina fonte, sezione `## Percorso della lezione` subito dopo il sommario: elenco delle pagine con le slide che coprono (in testo semplice, `pp. 3–5`) e una riga di contenuto; riga «Già lette, riprese in questa lezione: …» in corsivo; eventuale «**Ordine consigliato.**» quando le slide saltano avanti e indietro.
- **Navigazione:** dopo ogni modifica all'indice esegui `python output/libro.py`. Lo script rinomina le etichette dell'indice con i titoli delle pagine e scrive in fondo a ogni pagina la barra tra i marcatori `<!-- nav:inizio -->` e `<!-- nav:fine -->` (non scriverla a mano). Si ferma se una pagina compare due volte nell'indice.

---

## Operazioni

### INGEST — `ingestisci [file]` o `processa [file]`

1. Leggi il file raw indicato (testo **e** figure: molte slide contengono pseudocodice, tabelle di costo e tracce di esecuzione solo come immagine)
2. Discuti con l'utente i punti chiave e cosa enfatizzare **prima** di scrivere. Chiedi anche se, **oltre al contenuto del PDF**, sul sito vanno aggiunti approfondimenti (spiegazioni e dimostrazioni, esercizi, domande da esame) o disegni SVG: la scelta corrente dell'utente per questo wiki è **derivazioni e domande da esame** (vedi `corso.toml`)
3. Crea `wiki/fonti/[titolo-kebab-case].md` con il sommario strutturato
4. **Espandi ogni analisi e dimostrazione** della fonte secondo le regole in *Espansione dei calcoli* — un costo, una ricorrenza, un limite o una proprietà enunciati nel PDF senza passaggi vanno ricostruiti passo-passo, non copiati
5. Aggiorna le pagine in `wiki/concetti/` rilevanti (o creane di nuove)
6. Aggiorna le pagine in `wiki/entità/` rilevanti (o creane di nuove) — ogni algoritmo e ogni struttura dati ha la sua pagina entità
7. Riporta lo pseudocodice **fedelmente** secondo le *Convenzioni per lo pseudocodice*; se utile, aggiungi l'implementazione in `output/codice/` e usala per verificare tracce ed esempi numerici. **Per ogni algoritmo genera sempre un'animazione** (vedi *Animazioni degli algoritmi*) e incorporala nella sua pagina entità
8. Se la fonte contiene esercizi, aggiorna/crea le pagine in `wiki/esercizi/`
9. **Ancora ogni affermazione alla fonte**: le pagine PDF usate vanno nel titolo della sezione che le usa (vedi *Tracciabilità*)
10. Aggiorna `wiki/overview.md`
11. Aggiorna `wiki/index.md`
12. **Revisione di copertura totale (obbligatoria, sempre)**: rileggi il PDF **pagina per pagina** (testo *e* figure) e verifica che **ogni** elemento — definizioni, bullet, esempi, pseudocodice, tabelle di costo, tracce di esecuzione, valori numerici, didascalie, contenuto delle figure — sia riportato nel wiki. Le uniche aggiunte ammesse sono **spiegazioni che aiutano ad acquisire il concetto** (incluse le derivazioni dei risultati delle slide): niente fatti esterni non necessari, esercizi inventati o anticipazioni di argomenti futuri. Riporta all'utente cosa mancava e cosa è stato aggiunto/rimosso
13. Aggiungi la lezione all'indice `wiki/lezioni.md` e il «Percorso della lezione» alla pagina fonte secondo il *Formato di `lezioni.md`*, poi esegui `python output/libro.py`. Aggiungi la lezione **a `wiki/corso-completo.md`** come nuova sezione `## Lezione N — titolo`, scritta a mano (regole in *Il testo di studio*), e lancia `python output/controlla_corso.py` (link, ancore, immagini, formule, riferimenti PDF, pagine non citate): correggi ogni problema. I PDF di studio si producono con `python output/crea_pdf.py N [M ...]` (`tutte`, `--tutto`) e finiscono in `output/pdf/`
14. **Sito di studio**: la lezione entra nel sito da sola (vedi *Sito di studio*). In `corso.toml` aggiungi la voce `[[lezioni]]` con `n`, `breve` (una riga che riassume la lezione) e gli approfondimenti scelti (`concetti`, `fonte`, `domande`); `sito = false` solo su indicazione dell'utente. Lancia `python output/crea_sito.py` e correggi ogni riga «attenzione»
15. Appendi a `wiki/log.md`: `## [YYYY-MM-DD] ingest | [titolo fonte] | pagine coperte: [range]`
16. **Pubblica**: commit `feat: Lezione N — titolo` e push su `master`. Il workflow `.github/workflows/sito.yml` ricostruisce il sito e lo pubblica su GitHub Pages in un paio di minuti: dai all'utente il link alla pagina della lezione (`https://giob22.github.io/wiki-as/lezione-N.html`)

> Una singola fonte può toccare 5–15 pagine. È normale e desiderato.

---

### QUERY — domanda libera sul corso

1. Leggi `wiki/index.md` per identificare le pagine rilevanti
2. Leggi quelle pagine
3. Rispondi con citazioni esplicite (`→ [[nome-pagina]]`) e, per ogni definizione, costo o proprietà, il riferimento alla fonte primaria (`→ [[05-Insertion sort.pdf#page=14]]`)
4. Se la risposta è sostanziale (analisi, confronto, connessione nuova), proponi di salvarla come nuova pagina in `wiki/concetti/` — le esplorazioni devono capitalizzarsi nel wiki

---

### ESERCIZIO — `risolvi [esercizio]` o `svolgi [file]`

1. Leggi la traccia e le pagine concetto/entità coinvolte
2. Svolgi passo-passo secondo il tipo:
   - **analisi**: pseudocodice → costo di ogni riga × numero di esecuzioni → somma → caso migliore/peggiore/medio → notazione asintotica
   - **ricorrenza**: ricorrenza → metodo scelto (sostituzione, albero di ricorsione, teorema dell'esperto…) → passaggi → soluzione asintotica
   - **notazione asintotica**: definizione → scelta esplicita delle costanti ($c$, $n_0$) o calcolo del limite → conclusione
   - **progettazione**: specifica input/output → idea → pseudocodice secondo le convenzioni del corso → correttezza (invariante) → complessità
   - **traccia**: stato della struttura dati dopo ogni passo, in tabella
3. Salva in `wiki/esercizi/[tipo-esercizio].md`, raggruppando per **tipo** (non per data): se esiste già la pagina del tipo, aggiungi il caso nuovo invece di creare un duplicato
4. Estrai il **metodo generale** in cima alla pagina: quando si applica, quali strumenti, trappole ricorrenti
5. Linka i concetti usati con `[[...]]` e appendi a `wiki/log.md`

---

### ESAME — `esame` o `prepara esame`

1. Leggi **tutto** il wiki
2. Genera `wiki/esame/domande-probabili.md` — domande da orale/scritto, raggruppate per argomento
3. Genera `wiki/esame/riepilogo-rapido.md` — punti più importanti in forma compressa
4. Genera `wiki/esame/formulario.md` — definizioni delle notazioni, ricorrenze notevoli e loro soluzioni, sommatorie utili, con condizioni di validità
5. Genera `wiki/esame/tabella-complessita.md` — per ogni algoritmo/struttura dati: caso migliore, peggiore, medio, spazio, proprietà (in-place, stabile…), con link all'entità
6. Genera `wiki/esame/mappa-concetti.md` — connessioni tra concetti del corso
7. Segnala esplicitamente gap di copertura (argomenti del programma senza pagine wiki)

---

### SITO — `sito`, `sito intercorso [lezioni]`, `aggiungi al sito [cosa]`

1. `sito`: ricostruisci con `python output/crea_sito.py`, mostra l'anteprima (`python -m http.server -d _site 8000`) e riporta le righe «attenzione»
2. `sito intercorso 3 4 5`: in `corso.toml` imposta `[sito] lezioni = [3, 4, 5]`, `briciola = "Intercorso"` e un `intro` che dica cosa copre; per tornare al sito completo `lezioni = "tutte"`
3. `aggiungi al sito [cosa]`: approfondimenti, domande da esame o disegni per una lezione, come descritto in *Sito di studio*
4. Commit e push per pubblicare

---

### LINT — `lint` o `health check`

Scorri tutto il wiki e riporta:
- Contraddizioni tra pagine
- Pagine orfane (nessun link in entrata)
- Concetti, algoritmi o strutture dati citati ma senza pagina propria
- Link interni rotti
- Pagine con `TODO` aperto
- Formule senza definizione dei simboli
- **Risultati senza derivazione** (costo, ricorrenza o proprietà senza catena di passaggi)
- **Algoritmi senza pseudocodice, invariante o analisi di complessità**
- **Algoritmi senza animazione** (`![[animazione-<nome>.svg]]` nella sezione «Esempio di esecuzione»)
- Pseudocodice che non rispetta le convenzioni del corso
- **Pagine o sezioni senza link alla fonte** `raw/` nel titolo (pagina/slide mancante) e riferimenti ai PDF rimasti nel corpo
- Link `[[*.pdf#page=N]]` che puntano a file inesistenti in `raw/`
- Salti `❓` ancora aperti
- Link ripetuti in `wiki/lezioni.md` (ogni pagina deve comparire una sola volta), pagine wiki assenti dall'indice e pagine senza barra di navigazione aggiornata (`python output/libro.py`)
- Esito di `python output/controlla_corso.py` e righe «attenzione» di `python output/crea_sito.py`
- Lezioni di `corso-completo.md` senza voce `[[lezioni]]` (o senza `breve`) in `corso.toml`
- File del vault senza link in entrata (note, PDF, figure, script) e link non risolti
- Proponi nuove domande da investigare

---

## Il testo di studio — `wiki/corso-completo.md`

È il testo su cui l'utente studia e la **sorgente del sito**: un unico file, **schematico e senza ridondanze**, che contiene **solo ciò che sta nei PDF della lezione** (slide e appunti a mano del docente) nell'ordine delle slide: definizioni, pseudocodice, tabelle di costo, esempi, figure, dimostrazioni svolte dal docente.

- Ogni lezione è una sezione `## Lezione N — titolo` (con il trattino lungo `—`), seguita da una riga in corsivo `*Fonte: file.pdf, N pagine (...)*` e dalle sottosezioni `###`/`####` nell'ordine delle slide. Il numero è quello del prefisso del PDF (`00-` → Lezione 0); il materiale di supporto `a1` non ha un numero suo e confluisce nella Lezione 0, che cita entrambi i PDF (nomi corti in `[pdf_corti]`)
- Non vanno copiati lì le derivazioni mie (🧩), i grafici/animazioni aggiuntivi, gli esercizi svolti, le fonti esterne (📚): restano nelle pagine concetto/entità/esercizio e la sezione chiude con una riga `*Approfondimenti nel wiki: [[...]], [[...]]*`
- Un passaggio che la slide salta si ricostruisce in una riga solo se serve a seguire il discorso
- Ogni formula/definizione compare una volta sola; i richiami tra lezioni si fanno con una frase, non ripetendo
- Le equazioni numerate delle slide si scrivono con `\tag{N}` (sul sito diventano ancore, e «(N)» nel testo apre l'anteprima)
- I riferimenti ai PDF stanno solo nei titoli. Le immagini delle slide si incorporano con `![[nome-in-raw-assets.png]]` seguito da una didascalia in corsivo
- Lo pseudocodice si riporta come nella fonte (stessa numerazione delle righe) in un blocco di codice
- In testa al file la tabella **Indice** ha una riga per lezione (`| N | [[#Lezione N — titolo\|titolo]] | file.pdf |`)

---

## Sito di studio (GitHub Pages)

Il sito è la versione da leggere (anche da cellulare) di `wiki/corso-completo.md`: HTML statico generato da `output/crea_sito.py`, con formule KaTeX, tema sistema/chiaro/scuro, dimensione del testo regolabile, immagini ingrandibili, anteprima delle equazioni richiamate e indice della lezione. Indirizzo: `https://giob22.github.io/wiki-as/`.

**Cosa contiene.** Una pagina `lezione-N.html` per ogni sezione `## Lezione N — titolo` di `corso-completo.md`, più l'indice con una scheda per lezione. Ogni pagina ha:
1. **Il corso, slide per slide** — la sezione della lezione, cioè il contenuto dei PDF. I riferimenti alle pagine, i numeri di slide e le righe «Fonte:» vengono tolti in automatico
2. **Spiegazioni e dimostrazioni passo-passo** — le sezioni Spiegazione, Perché importa e Derivazioni delle pagine concetto elencate in `concetti` (per le pagine entità di algoritmi e strutture dati: Correttezza e Complessità), e le pagine esercizio in `esercizi`, a comparsa
3. **Domande da esame** — la sezione «Domande da esame» della pagina fonte indicata in `fonte`, se `domande = true`

**Regola:** le parti 2 e 3 sono state richieste dall'utente per questo wiki; i disegni SVG e ogni altra aggiunta compaiono **solo su decisione esplicita dell'utente** (punto 2 dell'INGEST o comando SITO). Non cambiare l'aspetto del sito (stile, script) se l'utente non lo chiede.

**Configurazione** — `corso.toml`:
- `[corso]` nome, sigla, descrizione (titolo e piè di pagina)
- `[sito]` `intro` (testo dell'indice), `briciola`, `lezioni` (`"tutte"` o un elenco, es. per un sito d'intercorso), `note` (righe in più nella legenda, es. lezioni escluse e perché)
- `[[lezioni]]` per lezione: `n`, `breve`, e se servono `titolo`, `inizio` (pubblica dalla sezione indicata in poi), `sito = false`, `concetti`, `esercizi`, `fonte`, `domande`, `domande_filtro`
- `[[figure]]`: `lezione`, `sezione` (inizio del titolo, senza riferimenti), `disegni` = chiavi delle funzioni `fig_<chiave>` di `output/sito_disegni.py`; il disegno va in fondo a quella sezione, con didascalia 🧩
- `[pdf_corti]`: nome corto di ogni PDF, usato nei titoli quando una sezione cita più file

**Comandi:**
- Anteprima: `python output/crea_sito.py` (scrive `_site/`), poi `python -m http.server -d _site 8000` e apri `http://localhost:8000`
- Pubblicazione: push su `master` → GitHub Actions (`.github/workflows/sito.yml`) → GitHub Pages
- Se il workflow fallisce con «Pages not enabled»: `gh api -X POST repos/giob22/wiki-as/pages -f build_type=workflow`

---

## Formato Pagine

I modelli pronti stanno in `modelli/` (Obsidian: «Inserisci modello»).

### Pagina Fonte — `wiki/fonti/[titolo].md`

```yaml
---
tipo: fonte
titolo: ""
file_raw: ""         # percorso in raw/, es. "05-Insertion sort.pdf"
pagine: ""           # range coperto, es. "1-42"
data_ingest: YYYY-MM-DD
formato: slide-pdf | appunti | libro | esercizi | video
argomenti: []
---
```

Sezioni obbligatorie:
- **Sommario** — paragrafo discorsivo
- **Percorso della lezione** — vedi *Formato di `lezioni.md`*
- **Punti chiave** — lista numerata
- **Concetti introdotti** — lista di link `[[nome]]`
- **Domande aperte** — cose poco chiare o da approfondire
- **Domande da esame** — domande tipiche su questa fonte (il sito le mostra se `domande = true`)

---

### Pagina Concetto — `wiki/concetti/[nome].md`

```yaml
---
tipo: concetto
importanza_esame: alta | media | bassa
prerequisiti: []
fonti_pdf: []        # es. ["02-Notazione asintotica.pdf#page=17"]
---
```

Sezioni obbligatorie (i nomi esatti contano: il sito legge *Spiegazione*, *Perché importa* e *Derivazioni*):
- **Definizione** — precisa, non colloquiale (quantificatori espliciti dove servono)
- **Formule** — se il concetto ne ha: formula, significato di ogni simbolo, ipotesi di validità; le pagine PDF di comparsa vanno nel titolo della sezione
- **Derivazioni** — passaggi espansi per ogni risultato non banale (vedi *Espansione dei calcoli*), una sottosezione `###` per derivazione
- **Spiegazione** — approfondita con esempi concreti
- **Perché importa** — contesto d'uso nel corso
- **Connessioni** — link a concetti correlati con spiegazione della relazione
- **Fonti** — link alle pagine fonte `wiki/fonti/`; le pagine PDF dell'intera pagina vanno nel titolo `## Fonti · [[02-Notazione asintotica.pdf#page=17|p. 17]], ...`

---

### Pagina Entità — `wiki/entità/[nome].md`

```yaml
---
tipo: entità
categoria: algoritmo | struttura-dati | problema
paradigma: ""        # per gli algoritmi: link al concetto del paradigma (euristica, ricerca combinatoria, divide et impera...)
fonti_pdf: []
---
```

Sezioni per un **algoritmo**:
- **Problema risolto** — input, output (link all'entità problema se esiste)
- **Idea** — descrizione discorsiva
- **Pseudocodice** — fedele alla fonte, con righe numerate
- **Esempio di esecuzione** — **animazione** dell'algoritmo in funzione (obbligatoria, in cima alla sezione) + traccia su un input concreto (tabella stato-per-passo)
- **Correttezza** — invariante di ciclo (inizializzazione, conservazione, conclusione) o dimostrazione induttiva
- **Complessità** — caso migliore, peggiore, medio; spazio; ogni risultato derivato
- **Proprietà** — in-place, stabile, online, adattivo… (solo quelle trattate o derivabili dalla fonte)
- **Connessioni** e **Fonti**

Sezioni per una **struttura dati**: cos'è, rappresentazione in memoria, operazioni (pseudocodice + costo di ciascuna), invarianti della struttura, esempio, connessioni, fonti.

Sezioni per un **problema**: definizione formale input/output, algoritmi che lo risolvono (con confronto delle complessità), limiti inferiori se trattati, fonti.

Come per i concetti, le pagine PDF di ogni sezione stanno nel titolo della sezione.

---

### Pagina Esercizio — `wiki/esercizi/[tipo].md`

```yaml
---
tipo: esercizio
argomento: ""
difficoltà: bassa | media | alta
---
```

Sezioni obbligatorie:
- **Metodo** — procedura generale per questo tipo di esercizio
- **Strumenti usati** — definizioni, teoremi, ricorrenze, con link `[[...]]` ai concetti
- **Casi svolti** — traccia (con le pagine PDF di origine nel titolo del caso) → svolgimento passo-passo completo → risultato
- **Trappole** — errori ricorrenti, costanti scelte male, casi base dimenticati, indici off-by-one

---

## Espansione dei calcoli

Regola centrale di questo wiki: **nessun risultato senza derivazione**.
Le slide comprimono i passaggi; il wiki li decomprime. Se il PDF scrive «nel caso peggiore $T(n) = \Theta(n^2)$», la pagina wiki deve mostrare *come* ci si arriva.

Per ogni risultato presente in una fonte:

1. **Punto di partenza** — da quale definizione, pseudocodice o ipotesi si parte, con link `[[...]]` al concetto
2. **Catena di passaggi** — un passaggio per riga, in blocco `$$...$$`. Vietato saltare da una riga all'altra senza dire cosa è stato fatto: ogni passaggio ha a destra un commento breve (sostituzione, sommatoria notevole, maggiorazione, ipotesi induttiva, limite notevole)
3. **Valori concreti** — costanti $c$, $n_0$ scelte esplicitamente; per le analisi riga per riga, la tabella *costo × numero di esecuzioni*
4. **Risultato** — in forma esatta e in notazione asintotica
5. **Verifica di sanità** — caso limite ($n = 1$, input già ordinato/inverso), controllo su un $n$ piccolo, confronto con l'esecuzione del codice in `output/codice/`
6. **Ipotesi usate** — modello di costo (RAM, costo unitario delle operazioni), caso considerato (migliore/peggiore/medio), distribuzione degli input per il caso medio: cosa smette di valere se un'ipotesi cade

Tipi di risultato e forma attesa della derivazione:

| Risultato | Derivazione attesa |
|-----------|--------------------|
| Costo di un algoritmo iterativo | Tabella riga / costo $c_i$ / numero di esecuzioni $t_j$ → somma → caso migliore e peggiore |
| Ricorrenza | Metodo esplicito (sostituzione con ipotesi induttiva, albero di ricorsione livello per livello, teorema dell'esperto con verifica del caso) |
| $f(n) = O/\Omega/\Theta(g(n))$ | Costanti $c$ ($c_1$, $c_2$) e $n_0$ esibite, oppure limite di $f/g$ |
| Correttezza | Invariante con inizializzazione, conservazione, conclusione; oppure induzione |
| Sommatorie | Forma chiusa con la sommatoria notevole usata |

Formato tipo:

```markdown
### Derivazione — [nome risultato] · [[05-Insertion sort.pdf#page=17|p. 17]]
**Fonte:** risultato dato senza passaggi
**Si parte da:** [[analisi-caso-peggiore]] — $T(n) = \sum_i c_i \cdot (\text{n. esecuzioni riga } i)$

$$
\begin{aligned}
T(n) &= c_1 n + c_2 (n-1) + \dots + c_5 \sum_{j=2}^{n} t_j + \dots   && \text{somma riga per riga} \\
     &= c_1 n + \dots + c_5 \left(\frac{n(n+1)}{2} - 1\right) + \dots && t_j = j \text{ (array in ordine inverso)} \\
     &= a n^2 + b n + c                                                 && \text{raccolgo i termini} \\
     &= \Theta(n^2)                                                     && a > 0
\end{aligned}
$$

**Sanity check:** per $n = 1$ il ciclo esterno non esegue il corpo; il numero di confronti su un array inverso di 5 elementi è 10 (verificato in `output/codice/insertion_sort.py`)
**Ipotesi:** modello RAM, costo costante per riga, caso peggiore = array ordinato al contrario
```

Se un passaggio del PDF non è ricostruibile (manca un dato, il salto non torna):
- scrivi `> ❓ Salto non ricostruito:` con cosa manca e cosa hai provato
- **non** riempire il buco inventando — segnala e chiedi

Le approssimazioni e le maggiorazioni della fonte vanno rese esplicite: quale termine è stato trascurato o maggiorato e perché è lecito.

---

## Convenzioni per lo pseudocodice

Lo pseudocodice del wiki segue le convenzioni del corso ([[a1-indicazioni_psuedocodice.pdf#page=2]]–[[a1-indicazioni_psuedocodice.pdf#page=4]]):

- L'indentazione indica la struttura dei blocchi (niente parentesi); costrutti di controllo: `while`, `for`, `if`-`else`
- Assegnamento con `←` (`i ← j`)
- Indici degli array **da 1**; `A[i..j]` è il sotto-array dall'$i$-esimo al $j$-esimo elemento
- `[]` sia per l'accesso agli elementi sia per i campi (`length[A]`); per i campi anche `A.campo`
- Una variabile di tipo aggregato è un **puntatore**; puntatore nullo = `NIL`; dopo `y ← x`, modificare `x.f` modifica anche `y.f`
- Parametri non aggregati passati **per valore**, aggregati **per riferimento**; tutte le variabili sono locali
- `and`/`or` in **corto circuito**; confronti `<`, `≤`, `=`, `≠`, `≥`, `>`
- Commenti mono-riga con `▷`; tipi non dichiarati
- Funzioni di libreria (es. `sort`) solo se l'esercizio lo consente esplicitamente

Nel wiki lo pseudocodice va in un blocco di codice senza linguaggio, con **righe numerate** (servono per le tabelle di costo):

```
INSERTION-SORT(A)
1  for j ← 2 to length[A]
2      key ← A[j]
3      ▷ inserisce A[j] nella sequenza ordinata A[1..j-1]
4      ...
```

Se la fonte usa una notazione diversa da queste convenzioni, riporta la versione della fonte e segnalalo con `> ⚠️ Contraddizione:`.

**Codice eseguibile:** le implementazioni in `output/codice/` (Python, apribili in Obsidian con il plugin Code Files) servono solo a **verificare** tracce, conteggi e risultati numerici; gli indici da 1 dello pseudocodice vanno tradotti esplicitamente e la corrispondenza riga-pseudocodice ↔ riga-codice va commentata. Il codice non sostituisce mai lo pseudocodice nel wiki.

---

## Tracciabilità

**Ogni affermazione del wiki deve essere rintracciabile su un PDF di lezione.**
Il wiki non è una fonte autonoma: è un indice navigabile del materiale del corso.

### Link alla fonte

I PDF stanno in `raw/`, dentro il vault Obsidian, quindi il link a pagina funziona:

```markdown
[[nome-file.pdf#page=17]]              ← link diretto alla pagina 17
![[nome-file.pdf#page=17]]             ← embed della pagina nella nota
```

Regole:
- **I riferimenti ai PDF stanno solo nei titoli** di sezione e sottosezione (`##`, `###`, ...), mai nel corpo del testo. In coda al titolo, dopo ` · `, vanno **tutte** le pagine usate in quella sezione, con alias corto; le pagine consecutive si compattano:
  ```markdown
  ### Derivazione — Costo di Merge · [[06-Merge Sort (1).pdf#page=23|p. 23]], [[06-Merge Sort (1).pdf#page=24|24]]
  ## Formule · [[02-Notazione asintotica.pdf#page=36|p. 36]]–[[02-Notazione asintotica.pdf#page=43|43]]
  ```
  Se una sezione usa più PDF, ogni gruppo è preceduto dal nome corto del file (`[pdf_corti]` in `corso.toml`): `· Merge Sort [[...|p. 9]] · Quicksort [[...|p. 12]]`
- Nel corpo **niente link ai PDF**: niente righe `> 📄 Fonte: [[...]]`, niente colonne "Pagina" nelle tabelle, niente pagina nelle didascalie o accanto a formule e valori numerici. Quando la pagina fa parte del senso della frase ("gli appunti di p. 24 mostrano…") si scrive come **testo semplice** `p. N`, senza link
- Fanno eccezione `lezioni.md` (indice) e `log.md` (storico)
- Il numero di pagina è quello **del PDF** (contatore del viewer), non quello stampato sulla slide; il numero di slide, se serve, va nel testo ("slide 15")
- Ogni **sezione** che usa una fonte ha i suoi riferimenti nel proprio titolo: non basta un riferimento unico in fondo alla pagina
- Non linkare titoli che portano riferimenti (`[[pagina#Titolo]]`): il testo del titolo contiene i link e l'ancora non funziona. Si linka la pagina e si nomina la sezione
- Le immagini estratte in `raw/assets/` mantengono nel nome il file e la pagina di origine: `05-insertion-sort-p12-traccia.png`, e la sezione che le usa cita la pagina PDF nel titolo
- Script di supporto: `python output/riferimenti_nei_titoli.py` sposta nei titoli i riferimenti rimasti nel corpo (prova senza argomenti, applica con `--scrivi`)
- Il libro di testo (Cormen) è una fonte del corso ma non è in `raw/`: se lo usi, marca `> 📚 Fonte esterna:` con capitolo e paragrafo

### Contenuto non tracciabile

Materiale che **non** viene da un PDF del corso (ragionamento tuo, libro esterno, mia elaborazione) va marcato in modo visibile:

| Marcatore | Significato |
|-----------|-------------|
| riferimento nel titolo (`### Titolo · [[file.pdf#page=N\|p. N]]`) | Tracciato su lezione |
| `> 🧩 Derivazione mia:` | Passaggi espansi da me, risultato presente nella fonte |
| `> 📚 Fonte esterna:` | Libro/paper/web — citare titolo e punto preciso |
| `> ❓ Salto non ricostruito:` | Passaggio della fonte non ricostruibile |

Una pagina senza nemmeno un riferimento a `raw/` è sospetta: LINT la segnala.

---

## Matematica e notazione

- Formule in LaTeX Obsidian: `$...$` inline, `$$...$$` display
- **Dentro una formula in linea non scrivere mai `*`**: usa `\ast`. Un `*` dentro `$...$` si scambia con il marcatore del corsivo e spezza la formula, soprattutto nelle didascalie in corsivo. Vale anche per `|`: nelle tabelle usa `\lvert x\rvert` e `\mid`, e non lasciare spazi subito dopo il `$` di apertura o prima del `$` di chiusura
- Ogni simbolo va definito almeno una volta nella pagina ($n$ = dimensione dell'input, $T(n)$ = tempo di esecuzione, ecc.)
- Notazioni asintotiche: $O$, $\Omega$, $\Theta$, $o$, $\omega$ — mai usare $O$ quando la fonte intende $\Theta$ o viceversa
- Logaritmi: specificare la base quando conta ($\lg = \log_2$, $\ln$); dentro $O(\cdot)$ la base si può omettere, ma va detto perché
- Arrotondamenti: $\lfloor\cdot\rfloor$ e $\lceil\cdot\rceil$ espliciti nelle ricorrenze
- Unità di misura solo dove hanno senso (tempi misurati, memoria in byte/parole)

---

## Convenzioni

| Marcatore                         | Uso                                          |
| --------------------------------- | -------------------------------------------- |
| `[[nome-pagina]]`                 | Link interno stile Obsidian — usalo sempre   |
| `> ⚠️ Contraddizione:`            | Nuova fonte contraddice quanto già nel wiki (o refuso nella slide) |
| `> 🎯 Esame:`                     | Questo punto è rilevante per l'esame         |
| `> 💡 Connessione:`               | Collegamento non ovvio con un altro concetto |
| `> 🧮 Formula chiave:`            | Formula/ricorrenza/costo da sapere a memoria |
| `TODO: da espandere`              | Placeholder per pagina incompleta            |
| `_Aggiornato: [data] — [motivo]_` | In fondo a ogni pagina modificata            |
| `![[grafico-*.svg]]` + didascalia `🧩` | Grafico di funzione generato da me dalle formule della fonte (script in `output/grafici/`) |
| `![[animazione-*.svg]]` + didascalia `🧩` | Animazione di un algoritmo in funzione (script `output/animazioni/genera_animazioni.py`) |

Sul sito i blockquote che iniziano con 🧮 🎯 🧩 💡 ⚠️ ❓ diventano riquadri colorati.

**Grafici di funzione:** dove aiutano a capire (crescita delle funzioni, confronto $n^2$ vs $n\lg n$, costanti nascoste, soglia $n_0$, tempi misurati vs attesi), genera grafici con lo script `output/grafici/genera_grafici_<lezione>.py` e incorporali nelle pagine concetto con didascalia 🧩 che spiega cosa si vede e cita la pagina PDF della formula nel titolo della sezione. Non vanno in `corso-completo.md` (quindi nemmeno sul sito) se l'utente non lo decide.

Marcatori di provenienza (`🧩 Derivazione mia`, `📚 Fonte esterna`, `❓ Salto non ricostruito`): vedi *Tracciabilità*.

**Regole rigide:**
- `raw/` non si tocca mai
- Non inventare: se non hai info, scrivi `TODO`. Vale anche per costi, ricorrenze e pseudocodice
- Nessun risultato copiato senza derivazione: o lo espandi, o marchi `❓ Salto non ricostruito`
- Nessuna affermazione senza riferimento `[[file.pdf#page=N]]` nel titolo della sezione, o marcata come derivazione mia / fonte esterna
- Il sito contiene il contenuto dei PDF più gli approfondimenti scelti dall'utente (derivazioni e domande da esame)
- Aggiorna pagine esistenti invece di crearne di ridondanti
- Nomi file in kebab-case, minuscolo, senza accenti (eccetto la cartella `entità/`)
- Se hai dubbi su dove mettere qualcosa, chiedi prima di scrivere

---

## Moduli opzionali attivi

### Pseudocodice e animazioni — corsi di algoritmi

Lo pseudocodice si riporta **come nella fonte** (stessa numerazione delle righe) in blocchi di codice, con una tabella di traccia su un'istanza piccola (quella delle slide, se c'è). Le pagine entità di categoria `algoritmo` hanno un'animazione `animazione-<nome>.svg` generata da `output/animazioni/genera_animazioni.py`, che **esegue davvero** l'algoritmo.

#### Animazioni degli algoritmi

Ogni pagina entità di categoria `algoritmo` contiene, in cima a «Esempio di esecuzione», un'animazione che mostra l'algoritmo in funzione.
- **Come si fa:** aggiungi una funzione a `output/animazioni/genera_animazioni.py`, che **esegue davvero** l'algoritmo e produce un fotogramma per ogni passo significativo; il file risultante è `animazione-<nome-pagina>.svg` (SVG con animazione SMIL, riprodotto da Obsidian; senza animazione resta visibile l'ultimo fotogramma).
- **Contenuto di ogni fotogramma:** stato della struttura dati (array, puntatori, pila delle chiamate, intervalli…), riga di pseudocodice corrente evidenziata, didascalia «Passo k/N — cosa succede», e dove serve l'invariante o i contatori (confronti, passi, moltiplicazioni).
- **Istanza:** quella delle slide quando esiste (es. ⟨5, 2, 4, 6, 1, 3⟩ per gli ordinamenti); altrimenti un'istanza piccola mia, dichiarata come tale nel titolo e nella didascalia.
- **Pseudocodice:** quello della fonte, riportato come nella pagina entità.
- **Controllo prima di incorporarla:** estrai alcuni fotogrammi e verifica che niente esca dai riquadri e che i valori coincidano con la traccia della pagina e con le slide.
- **Didascalia:** `> 🧩 Animazione generata da me ([[genera_animazioni.py]]) …` con istanza e cosa si vede.
