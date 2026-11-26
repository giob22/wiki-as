---
tipo: concetto
importanza_esame: alta
prerequisiti: ["modello-ram"]
fonti_pdf: ["02-Notazione asintotica.pdf#page=3", "02-Notazione asintotica.pdf#page=8", "03-Analisi di algoritmi.pdf#page=22", "03-Analisi di algoritmi.pdf#page=28"]
---

# Analisi di un algoritmo: tempo di esecuzione (e spazio)

## Definizione · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=21|p. 21]], [[03-Analisi di algoritmi.pdf#page=22|22]] · 02-Notazione asintotica.pdf [[02-Notazione asintotica.pdf#page=2|p. 2]], [[02-Notazione asintotica.pdf#page=3|3]], [[02-Notazione asintotica.pdf#page=8|p. 8]]

**Analizzare** un algoritmo significa stimare le **risorse** richieste in termini di:
- **occupazione di memoria**,
- **impegno di banda**,
- **tempo di calcolo**.

- Il **tempo di esecuzione** è solitamente espresso **in funzione della dimensione dei valori in ingresso**:
  - per algoritmi di **ordinamento**: lunghezza della sequenza da ordinare;
  - per algoritmi su **grafi**: numero di vertici e numero di archi.
- Il tempo di esecuzione è dato dalla **somma dei tempi di esecuzione di ciascuna linea** dello pseudocodice (assunti **costanti**), ciascuno **moltiplicato per il numero di volte** che la linea viene eseguita.
- Ogni operazione di base (assegnamento, confronto, somma, incremento, chiamata/return) costa una costante.

> 📄 Fonte: p. 8 — *Tempo di esecuzione asintotico*

Caratterizziamo l'efficienza di un algoritmo mediante il suo tempo di esecuzione. Quando la dimensione dei dati in ingresso è tale da rendere rilevante solo l'**ordine di crescita** del tempo di esecuzione, stiamo studiando l'efficienza **asintotica** di un algoritmo.

## Formule · [[03-Analisi di algoritmi.pdf#page=22|p. 22]]

> 🧮 Formula chiave:
$$
T(n) = \sum_{i} c_i \, t_i(n)
$$

- $n$ = dimensione dell'ingresso
- $c_i$ = costo (costante) di un'esecuzione della riga $i$ dello pseudocodice
- $t_i(n)$ = numero di volte che la riga $i$ viene eseguita su un ingresso di dimensione $n$
- $T(n)$ = tempo di esecuzione, in passi del [[modello-ram]]

Prima comparsa: p. 22 (enunciata a parole).

## Derivazioni

### Derivazione — somma iterativa: $T(n) = 2n + 4 = O(n)$ · [[03-Analisi di algoritmi.pdf#page=23|p. 23]], [[03-Analisi di algoritmi.pdf#page=28|p. 28]]
**Fonte:** p. 23–p. 28; svolta passo per passo in [[analisi-del-costo-riga-per-riga]] e nell'entità [[somma-iterativa]].

$$
T(n) = \underbrace{1}_{s \leftarrow 0} + \underbrace{1}_{i \leftarrow 1} + \underbrace{(n+1)}_{\text{test } i \le n} + \underbrace{n}_{\text{corpo}} + \underbrace{1}_{\text{return}} = 2n + 4 = O(n)
$$

## Spiegazione · [[03-Analisi di algoritmi.pdf#page=9|p. 9]], [[03-Analisi di algoritmi.pdf#page=29|p. 29]], [[03-Analisi di algoritmi.pdf#page=35|p. 35]]

**Perché il test del ciclo costa $n+1$ e il corpo $n$:** il test viene valutato una volta per ogni valore $i = 1, \dots, n$ (esito vero) più una volta con $i = n+1$ (esito falso, uscita dal ciclo).

**Complessità spaziale** — la domanda «E la complessità spaziale?» è posta in p. 29 e p. 35 senza risposta.

> 🧩 Derivazione mia:
> - [[somma-iterativa]]: usa solo le variabili $s$ e $i$, indipendentemente da $n$ → spazio aggiuntivo $\Theta(1)$.
> - [[somma-ricorsiva]]: ogni chiamata attiva occupa un record di attivazione sulla pila di sistema (parametro $n$, indirizzo di ritorno); le chiamate annidate sono $n+1$ (per $n, n-1, \dots, 0$) prima che la prima ritorni → spazio $\Theta(n)$. Verificato contando la profondità massima in [[somma_primi_n.py]].
> - Questo è il «rischio di stack overflow» citato in p. 9 → [[iterazione-e-ricorsione]].

## Perché importa

È il metodo standard per ricavare $T(n)$ da uno pseudocodice; il risultato si riassume poi con la [[notazione-asintotica]], normalmente nel caso peggiore ([[casi-di-complessita]]).

> 🎯 Esame: costruire la tabella «riga / costo / numero di esecuzioni» e sommarla; ricordarsi che il test di un `for` viene eseguito una volta in più del corpo.

## Connessioni

- [[modello-ram]] — perché ogni riga ha costo costante
- [[casi-di-complessita]] — $t_i(n)$ può dipendere dall'istanza, non solo da $n$
- [[equazioni-di-ricorrenza]] — l'analogo per algoritmi ricorsivi
- [[analisi-del-costo-riga-per-riga]] — esercizi

## Fonti · 03-Analisi di algoritmi.pdf [[03-Analisi di algoritmi.pdf#page=20|p. 20]]–[[03-Analisi di algoritmi.pdf#page=22|22]] · 02-Notazione asintotica.pdf [[02-Notazione asintotica.pdf#page=3|p. 3]], [[02-Notazione asintotica.pdf#page=8|p. 8]]

- [[lezione-03-analisi-di-algoritmi]], [[lezione-02-notazione-asintotica]]

_Aggiornato: 2026-09-26 — ingest 02-Notazione asintotica.pdf e 03-Analisi di algoritmi.pdf_

<!-- nav:inizio -->
---
**Lezione 02 · pagina 3 di 8** · ← [[modello-ram|Modello di calcolo RAM]] · [[lezioni|Indice]] · [[casi-di-complessita|Caso peggiore, migliore e medio]] →
<!-- nav:fine -->
