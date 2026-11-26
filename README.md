# wiki-as — Algoritmi e Strutture Dati

Wiki del corso di **Algoritmi e Strutture Dati** (LM Ingegneria Informatica, UNINA, a.a. 2026/27, Prof. Stefano Marrone): LLM wiki mantenuto da Claude Code, vault Obsidian e sito di studio su GitHub Pages. Schema ricavato dal template [`wiki-template`](https://github.com/giob22/wiki-template).

**Sito di studio:** <https://giob22.github.io/wiki-as/>

## Cosa c'è dentro

| Percorso | A cosa serve |
|---|---|
| `CLAUDE.md` | schema del wiki: ruolo, operazioni (INGEST, QUERY, ESERCIZIO, ESAME, SITO, LINT), formato delle pagine, espansione dei calcoli, tracciabilità sui PDF, convenzioni, pseudocodice e animazioni |
| `raw/` | slide del corso (PDF) e figure estratte in `raw/assets/` — immutabili |
| `wiki/index.md`, `log.md`, `overview.md`, `lezioni.md`, `corso-completo.md` | file di indicizzazione e testo di studio |
| `wiki/concetti/`, `entità/`, `fonti/`, `esercizi/`, `esame/` | cartelle delle pagine |
| `modelli/` | modelli delle pagine per Obsidian («Inserisci modello») |
| `corso.toml` | dati del corso e configurazione del sito |
| `output/crea_sito.py`, `sito_disegni.py` | sito di studio (stile, tema chiaro/scuro, KaTeX, anteprima delle equazioni) |
| `output/crea_pdf.py` | PDF di studio delle lezioni (Chrome/Edge headless) |
| `output/controlla_corso.py`, `riferimenti_nei_titoli.py` | controlli di integrità e riferimenti ai PDF nei titoli |
| `output/libro.py` | navigazione a libro («← precedente · Indice · successiva →») generata da `wiki/lezioni.md` |
| `output/animazioni/`, `output/codice/`, `output/grafici/` | animazioni SVG degli algoritmi, codice di verifica, grafici di funzione |
| `.github/workflows/sito.yml` | a ogni push su `master` ricostruisce il sito e lo pubblica su Pages |

## Il sito

Una pagina per ogni sezione `## Lezione N — titolo` di `wiki/corso-completo.md`: il contenuto dei PDF nell'ordine delle slide, poi (a comparsa) spiegazioni e dimostrazioni passo-passo e le domande da esame della lezione.

```bash
pip install -r requirements.txt
python output/crea_sito.py               # genera _site/
python -m http.server -d _site 8000      # anteprima su http://localhost:8000
```

## Lavorare sul wiki

- Per ogni lezione nuova: `ingestisci raw/<file>.pdf`. Claude aggiorna il wiki, aggiunge la lezione a `wiki/corso-completo.md` e a `corso.toml` e, al push, il sito si aggiorna da solo.
- Dopo ogni modifica a `wiki/lezioni.md`: `python output/libro.py` (aggiorna la navigazione in fondo alle pagine).
- Controlli: `python output/controlla_corso.py` (corso completo) e le righe «attenzione» di `python output/crea_sito.py`.
