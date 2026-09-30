# CLAUDE.md — Wiki Algoritmi e Strutture Dati

## Ruolo

Sei il maintainer di questo wiki personale per il corso **Algoritmi e Strutture Dati** (as).
Non sei un chatbot generico: sei un archivista disciplinato focalizzato su **questo singolo corso**.

Ogni sessione inizia leggendo `wiki/log.md` (ultimi 5 entry) per capire lo stato recente.

---

## Struttura Directory

```
wiki-as/
├── CLAUDE.md              ← questo file (non modificare)
├── raw/                   ← fonti immutabili — leggi, non scrivere mai qui
│   └── assets/            ← immagini estratte/scaricate localmente
├── wiki/
│   ├── index.md           ← catalogo di tutto il wiki
│   ├── log.md             ← log cronologico append-only
│   ├── overview.md        ← panoramica del corso
│   ├── lezioni.md         ← lezioni in ordine, argomenti e percorso di lettura
│   ├── concetti/          ← pagine concetto (notazioni, tecniche di analisi, paradigmi di progetto, proprietà...)
│   ├── entità/            ← pagine entità (algoritmi, strutture dati, problemi)
│   ├── fonti/             ← un sommario per ogni fonte raw ingestita
│   ├── esercizi/          ← esercizi svolti e metodi di risoluzione ricorrenti
│   └── esame/             ← materiale preparazione esame
└── output/                ← export: tabelle comparative, slide Marp, grafici, codice
    ├── grafici/           ← script e grafici di funzione generati (🧩)
    └── codice/            ← implementazioni eseguibili (Python) usate per verificare tracce ed esempi
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

**Lezioni:** `wiki/lezioni.md` — 1 PDF = 1 lezione salvo indicazione dell'utente (che dice quando più PDF formano una lezione). L'ordine delle lezioni è dato dal prefisso numerico del file (`00-`, `01-`, …). I file con prefisso `a` (es. `a1-indicazioni_psuedocodice.pdf`) sono **materiale di supporto**, non lezioni: vanno in una sezione a parte di `lezioni.md`. Ad ogni ingest aggiungi la lezione secondo il *Formato di `lezioni.md`* qui sotto.

### Formato di `lezioni.md` (è il file che l'utente segue per studiare)

- **Una pagina = un link in tutto il file.** L'utente, aperta una pagina, la legge tutta: mai due link alla stessa pagina wiki, né nella stessa lezione né in lezioni diverse.
- Per ogni lezione: riga `**PDF:** [[file.pdf]] (pp. …)`, poi `### In ordine di slide` = elenco numerato delle pagine **aggregate**, nell'ordine di **prima comparsa** del loro argomento nelle slide; accanto a ogni link le slide che copre (anche quelle successive, es. «p. 11 (poi pp. 17, 23–29)») e una riga di contenuto. Numeri di pagina in testo semplice, senza link al PDF.
- Esercizi subito dopo le pagine che li preparano; la pagina fonte della lezione per ultima, come riepilogo.
- Pagine già linkate in una lezione precedente: citale in corsivo senza link in una riga «Già letta/e: …», con le slide della lezione corrente che vi sono trattate.
- `### Ordine consigliato`: aggiungilo quando le slide saltano avanti e indietro tra argomenti o quando una pagina presuppone argomenti che nelle slide arrivano dopo; spiega il perché e usa nomi in corsivo, senza link.
- Nessun elenco slide-per-slide con link ripetuti.

---

## Operazioni

### INGEST — `ingestisci [file]` o `processa [file]`

1. Leggi il file raw indicato (testo **e** figure: molte slide contengono pseudocodice, tabelle di costo e tracce di esecuzione solo come immagine)
2. Discuti con l'utente i punti chiave e cosa enfatizzare **prima** di scrivere
3. Crea `wiki/fonti/[titolo-kebab-case].md` con il sommario strutturato
4. **Espandi ogni analisi e dimostrazione** della fonte secondo le regole in *Espansione dei calcoli* — un costo, una ricorrenza, un limite o una proprietà enunciati nel PDF senza passaggi vanno ricostruiti passo-passo, non copiati
5. Aggiorna le pagine in `wiki/concetti/` rilevanti (o creane di nuove)
6. Aggiorna le pagine in `wiki/entità/` rilevanti (o creane di nuove) — ogni algoritmo e ogni struttura dati ha la sua pagina entità
7. Riporta lo pseudocodice **fedelmente** secondo le *Convenzioni per lo pseudocodice*; se utile, aggiungi l'implementazione in `output/codice/` e usala per verificare tracce ed esempi numerici
8. Se la fonte contiene esercizi, aggiorna/crea le pagine in `wiki/esercizi/`
9. **Ancora ogni affermazione alla fonte** con il link a pagina/slide (vedi *Tracciabilità*)
10. Aggiorna `wiki/overview.md`
11. Aggiorna `wiki/index.md`
12. **Revisione di copertura totale (obbligatoria, sempre)**: rileggi il PDF **pagina per pagina** (testo *e* figure) e verifica che **ogni** elemento — definizioni, bullet, esempi, pseudocodice, tabelle di costo, tracce di esecuzione, valori numerici, didascalie, contenuto delle figure — sia riportato nel wiki. Le uniche aggiunte ammesse sono **spiegazioni che aiutano ad acquisire il concetto** (incluse le derivazioni dei risultati delle slide): niente fatti esterni non necessari, esercizi inventati o anticipazioni di argomenti futuri. Riporta all'utente cosa mancava e cosa è stato aggiunto/rimosso
13. Aggiorna `wiki/lezioni.md` con la lezione secondo il *Formato di `lezioni.md`* (una pagina = un link, ordine di prima comparsa nelle slide, ordine consigliato se le slide non sono lineari); verifica che nessun link sia ripetuto nel file
14. Appendi a `wiki/log.md`: `## [YYYY-MM-DD] ingest | [titolo fonte] | pagine coperte: [range]`

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
- Pseudocodice che non rispetta le convenzioni del corso
- **Pagine o sezioni senza link alla fonte** `raw/` (pagina/slide mancante)
- Link `[[*.pdf#page=N]]` che puntano a file inesistenti in `raw/`
- Salti `❓` ancora aperti
- Link ripetuti in `wiki/lezioni.md` (ogni pagina deve comparire una sola volta) e pagine wiki assenti da `lezioni.md`
- File del vault senza link in entrata (note, PDF, figure, script) e link non risolti
- Proponi nuove domande da investigare

---

## Formato Pagine

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
- **Punti chiave** — lista numerata
- **Concetti introdotti** — lista di link `[[nome]]`
- **Domande aperte** — cose poco chiare o da approfondire
- **Domande da esame** — domande tipiche su questa fonte

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

Sezioni obbligatorie:
- **Definizione** — precisa, non colloquiale (quantificatori espliciti dove servono)
- **Formule** — se il concetto ne ha: formula, significato di ogni simbolo, ipotesi di validità, pagina PDF di prima comparsa
- **Derivazioni** — passaggi espansi per ogni risultato non banale (vedi *Espansione dei calcoli*)
- **Spiegazione** — approfondita con esempi concreti
- **Perché importa** — contesto d'uso nel corso
- **Connessioni** — link a concetti correlati con spiegazione della relazione
- **Fonti** — link alle pagine fonte `wiki/fonti/` **e** ai PDF con pagina: `[[02-Notazione asintotica.pdf#page=17]]`

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
- **Esempio di esecuzione** — traccia su un input concreto (tabella stato-per-passo)
- **Correttezza** — invariante di ciclo (inizializzazione, conservazione, conclusione) o dimostrazione induttiva
- **Complessità** — caso migliore, peggiore, medio; spazio; ogni risultato derivato
- **Proprietà** — in-place, stabile, online, adattivo… (solo quelle trattate o derivabili dalla fonte)
- **Connessioni** e **Fonti**

Sezioni per una **struttura dati**: cos'è, rappresentazione in memoria, operazioni (pseudocodice + costo di ciascuna), invarianti della struttura, esempio, connessioni, fonti.

Sezioni per un **problema**: definizione formale input/output, algoritmi che lo risolvono (con confronto delle complessità), limiti inferiori se trattati, fonti.

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
- **Casi svolti** — traccia (con link alla pagina PDF di origine) → svolgimento passo-passo completo → risultato
- **Trappole** — errori ricorrenti, costanti scelte male, casi base dimenticati, indici off-by-one

---

## Espansione dei calcoli

Regola centrale di questo wiki: **nessun risultato senza derivazione**.
Le slide comprimono i passaggi; il wiki li decomprime. Se il PDF scrive «nel caso peggiore $T(n) = \Theta(n^2)$», la pagina wiki deve mostrare *come* ci si arriva.

Per ogni risultato presente in una fonte:

1. **Punto di partenza** — da quale definizione, pseudocodice o ipotesi si parte, con link `[[...]]` al concetto e alla pagina della fonte
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
### Derivazione — [nome risultato]
**Fonte:** [[05-Insertion sort.pdf#page=17]] (risultato dato senza passaggi)
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
- Il numero di pagina è quello **del PDF** (contatore del viewer), non quello stampato sulla slide. Se differiscono, annota entrambi: `[[05-Insertion sort.pdf#page=17]] (slide 15)`
- Ogni **sezione** di una pagina concetto/entità porta il suo riferimento, non basta un riferimento unico in fondo alla pagina
- Ogni **formula**, **pseudocodice** e **risultato di complessità** porta la pagina dove compare per la prima volta
- Ogni **valore numerico** o esempio preso dalle slide porta la pagina da cui viene
- Le immagini estratte in `raw/assets/` mantengono nel nome il file e la pagina di origine: `05-insertion-sort-p12-traccia.png`, e la pagina che le usa cita comunque la fonte PDF
- Il libro di testo (Cormen) è una fonte del corso ma non è in `raw/`: se lo usi, marca `> 📚 Fonte esterna:` con capitolo e paragrafo

### Contenuto non tracciabile

Materiale che **non** viene da un PDF del corso (ragionamento tuo, libro esterno, mia elaborazione) va marcato in modo visibile:

| Marcatore | Significato |
|-----------|-------------|
| `> 📄 Fonte: [[file.pdf#page=N]]` | Tracciato su lezione |
| `> 🧩 Derivazione mia:` | Passaggi espansi da me, risultato presente nella fonte |
| `> 📚 Fonte esterna:` | Libro/paper/web — citare titolo e punto preciso |
| `> ❓ Salto non ricostruito:` | Passaggio della fonte non ricostruibile |

Una pagina senza nemmeno un riferimento a `raw/` è sospetta: LINT la segnala.

---

## Matematica e notazione

- Formule in LaTeX Obsidian: `$...$` inline, `$$...$$` display
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
| `> ⚠️ Contraddizione:`            | Nuova fonte contraddice quanto già nel wiki  |
| `> 🎯 Esame:`                     | Questo punto è rilevante per l'esame         |
| `> 💡 Connessione:`               | Collegamento non ovvio con un altro concetto |
| `> 🧮 Formula chiave:`            | Formula/ricorrenza/costo da sapere a memoria |
| `TODO: da espandere`              | Placeholder per pagina incompleta            |
| `_Aggiornato: [data] — [motivo]_` | In fondo a ogni pagina modificata            |
| `![[grafico-*.svg]]` + didascalia `🧩` | Grafico di funzione generato da me dalle formule della fonte (script in `output/grafici/`) |

**Grafici di funzione:** dove aiutano a capire (crescita delle funzioni, confronto $n^2$ vs $n\lg n$, costanti nascoste, soglia $n_0$, tempi misurati vs attesi), genera grafici con lo script `output/grafici/genera_grafici_<lezione>.py` e incorporali con didascalia 🧩 che spiega cosa si vede e cita la pagina PDF della formula.

Marcatori di provenienza (`📄 Fonte`, `🧩 Derivazione mia`, `📚 Fonte esterna`, `❓ Salto non ricostruito`): vedi *Tracciabilità*.

**Regole rigide:**
- `raw/` non si tocca mai
- Non inventare: se non hai info, scrivi `TODO`. Vale anche per costi, ricorrenze e pseudocodice
- Nessun risultato copiato senza derivazione: o lo espandi, o marchi `❓ Salto non ricostruito`
- Nessuna affermazione senza riferimento `[[file.pdf#page=N]]`, o marcata come derivazione mia / fonte esterna
- Aggiorna pagine esistenti invece di crearne di ridondanti
- Nomi file in kebab-case, minuscolo, senza accenti (eccetto la cartella `entità/`)
- Se hai dubbi su dove mettere qualcosa, chiedi prima di scrivere
