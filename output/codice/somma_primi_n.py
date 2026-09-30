"""Verifica di 03-Analisi di algoritmi.pdf pp.11-34: somma dei primi n interi.

- somma_iterativa: conta i passi come nella tabella di p.28 (1 + 1 + (n+1) + n + 1 = 2n + 4)
  e controlla l'invariante di p.17 (all'inizio dell'iterazione i, s = sum_{k=1}^{i-1} k)
- somma_ricorsiva: conta il costo con T(0) = 1, T(i) = T(i-1) + c (p.31-33) e la
  profondità massima della pila di chiamate (complessità spaziale, domanda di p.34)

Corrispondenza con lo pseudocodice di p.11 (righe numerate come nel wiki):
  somma_iterativa(n)             somma_ricorsiva(n)
  1  s <- 0                       1  se n = 0
  2  per i da 1 a n               2      ritorna 0
  3      s <- s + i               3  altrimenti
  4  ritorna s                    4      ritorna n + somma_ricorsiva(n - 1)
"""


def somma_iterativa(n):
    passi = 0
    s = 0; passi += 1                       # riga 1: assegnazione -> 1
    i = 1; passi += 1                       # riga 2: inizializzazione del ciclo -> 1
    while True:
        passi += 1                          # riga 2: test i <= n -> eseguito n+1 volte
        if not i <= n:
            break
        assert s == sum(range(1, i)), "invariante violato"   # p.17
        s = s + i; passi += 1               # riga 3: corpo -> n volte (p.26: in realtà somma+assegnazione+incremento)
        i += 1
    assert s == n * (n + 1) // 2            # conclusione: i = n+1 => s = 1 + ... + n
    passi += 1                              # riga 4: return -> 1
    return s, passi


def somma_ricorsiva(n, c=1, profondita=1, stato=None):
    """Restituisce (valore, costo T(n) con costo c per chiamata non base, profondità massima)."""
    if stato is None:
        stato = {"max": 0}
    stato["max"] = max(stato["max"], profondita)
    if n == 0:
        return 0, 1, stato["max"]            # T(0) = 1: un confronto e un return (p.31)
    v, t, _ = somma_ricorsiva(n - 1, c, profondita + 1, stato)
    return n + v, t + c, stato["max"]        # T(i) = T(i-1) + c (p.32)


if __name__ == "__main__":
    print(" n | s_iter | passi | 2n+4 | s_ric | T(n) (c=1) | 1+c*n | chiamate annidate")
    for n in [0, 1, 2, 5, 10, 100]:
        s, passi = somma_iterativa(n)
        v, t, prof = somma_ricorsiva(n)
        print(f"{n:>3} | {s:>6} | {passi:>5} | {2*n+4:>4} | {v:>5} | {t:>10} | {1+n:>5} | {prof}")
