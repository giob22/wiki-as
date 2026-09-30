"""Verifica di 05-Insertion sort.pdf: insertion sort (pp.5-22) e selection sort (esercizio 2.2.2, pp.24-29).

Insertion sort: traduzione 1:1 dello pseudocodice di p.5 con array indicizzato da 1 (cella 0 inutilizzata).
Numerazione delle righe come nella tabella dei costi di p.17 (la riga 3 e' il commento):
  1 for j <- 2 to length[A]                 c1   n
  2     do key <- A[j]                      c2   n-1
  3     // Insert A[j] into A[1..j-1]       -    -
  4     i <- j-1                            c4   n-1
  5     while i>0 and A[i]>key              c5   sum t_j
  6         do A[i+1] <- A[i]               c6   sum (t_j - 1)
  7         i <- i-1                        c7   sum (t_j - 1)
  8     A[i+1] <- key                       c8   n-1

Esecuzione: python ordinamento.py
"""
import random


def insertion_sort(valori, traccia=False):
    """Ordina una copia di `valori`; restituisce (array ordinato, lista dei t_j per j = 2..n, conteggi per riga)."""
    A = [None] + list(valori)            # A[1..n]
    n = len(valori)
    conta = {r: 0 for r in (1, 2, 4, 5, 6, 7, 8)}
    t = []
    j = 2
    while True:
        conta[1] += 1                    # riga 1: test del for (n volte in tutto)
        if not j <= n:
            break
        key = A[j]; conta[2] += 1        # riga 2
        i = j - 1; conta[4] += 1         # riga 4
        tj = 0
        while True:
            tj += 1; conta[5] += 1       # riga 5: test del while
            if not (i > 0 and A[i] > key):   # corto circuito: A[0] non viene letto
                break
            A[i + 1] = A[i]; conta[6] += 1   # riga 6
            i = i - 1; conta[7] += 1         # riga 7
        A[i + 1] = key; conta[8] += 1    # riga 8
        # invariante di p.16 all'inizio dell'iterazione successiva (j+1):
        assert A[1:j + 1] == sorted(valori[:j]), "invariante violato"
        t.append(tj)
        if traccia:
            print(f"  j={j} key={key} t_j={tj} -> A = {A[1:]}")
        j += 1
    return A[1:], t, conta


def selection_sort(s):
    """Codice C di p.25 (indici da 0). Restituisce (array, confronti, swap)."""
    s = list(s)
    n = len(s)
    confronti = scambi = 0
    for i in range(n):                   # for (i=0; i<n; i++)
        minimo = i
        for j in range(i + 1, n):        # for (j=i+1; j<n; j++)
            confronti += 1
            if s[j] < s[minimo]:
                minimo = j
        s[i], s[minimo] = s[minimo], s[i]   # swap(s[i], s[min])
        scambi += 1
        # invariante (mio): s[0..i] contiene gli i+1 elementi piu' piccoli, ordinati
        assert s[:i + 1] == sorted(s)[:i + 1]
    return s, confronti, scambi


if __name__ == "__main__":
    print("== Traccia di p.5-15 su <5, 2, 4, 6, 1, 3> ==")
    A, t, conta = insertion_sort([5, 2, 4, 6, 1, 3], traccia=True)
    print("  risultato:", A, "| t_j:", t, "| conteggi per riga:", conta)

    print("\n== Caso migliore (gia' ordinato) e peggiore (decrescente), p.20-22 ==")
    print("   n | best: sum t_j  (n-1) | worst: sum t_j  n(n+1)/2-1 | worst: sum(t_j-1)  n(n-1)/2")
    for n in [1, 2, 3, 5, 10, 100]:
        _, tb, _ = insertion_sort(range(n))
        _, tw, _ = insertion_sort(range(n, 0, -1))
        print(f"{n:>4} | {sum(tb):>13} {n-1:>6} | {sum(tw):>14} {n*(n+1)//2-1:>11} |"
              f" {sum(x-1 for x in tw):>16} {n*(n-1)//2:>9}")

    print("\n== Stabilita' (A[i] > key stretto): chiavi uguali mantengono l'ordine ==")
    coppie = [(3, 'a'), (1, 'b'), (3, 'c'), (2, 'd'), (1, 'e')]

    class K:  # confronta solo la chiave numerica
        def __init__(self, c): self.c = c
        def __gt__(self, o): return self.c[0] > o.c[0]
        def __lt__(self, o): return self.c[0] < o.c[0]
        def __eq__(self, o): return self.c[0] == o.c[0]
        def __repr__(self): return f"{self.c[0]}{self.c[1]}"
    ordinato = [None] + [K(c) for c in coppie]
    n = len(coppie)
    for j in range(2, n + 1):
        key = ordinato[j]; i = j - 1
        while i > 0 and ordinato[i] > key:
            ordinato[i + 1] = ordinato[i]; i -= 1
        ordinato[i + 1] = key
    print("  ", ordinato[1:])

    print("\n== Selection sort (p.25-29): confronti = n(n-1)/2 per ogni input ==")
    print("   n | ordinato | decrescente | casuale | n(n-1)/2 | swap")
    for n in [1, 2, 5, 10, 100]:
        c1 = selection_sort(range(n))[1]
        c2 = selection_sort(range(n, 0, -1))[1]
        c3, sw = selection_sort(random.sample(range(n), n))[1:]
        print(f"{n:>4} | {c1:>8} | {c2:>11} | {c3:>7} | {n*(n-1)//2:>8} | {sw}")
