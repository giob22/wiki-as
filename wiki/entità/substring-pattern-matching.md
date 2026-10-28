---
tipo: entità
categoria: problema
fonti_pdf: ["05-Insertion sort.pdf#page=30", "05-Insertion sort.pdf#page=31"]
---

# Substring Pattern Matching (ricerca di una sottostringa)

## Definizione formale

> 📄 Fonte: [[05-Insertion sort.pdf#page=30]] — «Crescita delle funzioni: ragionare sull'efficienza», *S&T: String Pattern Matching*

- **Problem:** Substring Pattern Matching
- **Input:** una stringa di testo $t$ e una stringa pattern $p$.
- **Output:** $t$ contiene il pattern $p$ come sottostringa? E se sì, **dove**?

Simboli (dal codice di p. 31): $n$ = lunghezza di $t$, $m$ = lunghezza di $p$.

## Esempio della fonte

![[05-insertion-sort-p30-pattern-matching-esempio.png]]
*Ricerca della sottostringa **abba** nel testo **aababba**: ogni riga è un tentativo, spostato di una posizione a destra, con i caratteri del pattern effettivamente confrontati. ([[05-Insertion sort.pdf#page=30]])*

> 🧩 Lettura mia della figura (con $t = a\,a\,b\,a\,b\,b\,a$, posizioni da 0):

| Tentativo (posizione $i$) | Caratteri di $p$ confrontati | Esito |
|---------------------------|------------------------------|-------|
| 0 | `a b` | $t[1] = a \ne b$: fallisce al 2° carattere |
| 1 | `a b b` | $t[3] = a \ne b$: fallisce al 3° carattere |
| 2 | `a` | $t[2] = b \ne a$: fallisce subito |
| 3 | `a b b a` | tutti uguali: **trovato in posizione 3** (4° carattere, contando da 1) |

Totale: $2 + 3 + 1 + 4 = 10$ confronti di caratteri (verificato con [[stringhe_e_logaritmi.py]]).

## Algoritmi che lo risolvono

| Algoritmo | Costo nel caso peggiore | Pagina |
|-----------|-------------------------|--------|
| [[findmatch]] (forza bruta) | $O(nm)$ — 🧩 derivazione nella pagina dell'algoritmo | [[05-Insertion sort.pdf#page=31]] |

La consegna della slide è «**Valutare l'efficienza asintotica**» ([[05-Insertion sort.pdf#page=30]]).

## Connessioni

- [[findmatch]] — l'algoritmo
- [[dominanza-asintotica]] — la sezione della lezione si intitola «Crescita delle funzioni»

## Fonti

- [[lezione-05-insertion-sort]]
- le stesse slide sono riprese nella versione aggiornata della lezione 06 ([[lezione-06-merge-sort]]): [[06-Merge Sort (1).pdf#page=45]], [[06-Merge Sort (1).pdf#page=46]]
- [[05-Insertion sort.pdf#page=30]], [[05-Insertion sort.pdf#page=31]]

_Aggiornato: 2026-09-30 — ingest 05-Insertion sort.pdf_
_Aggiornato: 2026-10-10 — slide riprese nella versione aggiornata della lezione 06_

<!-- nav:inizio -->
---
**Lezione 05 · pagina 4 di 7** · ← [[selection-sort|Selection sort (Esercizio del libro di testo 2.2.2)]] · [[lezioni|Indice]] · [[findmatch|findmatch — pattern matching a forza bruta]] →
<!-- nav:fine -->
