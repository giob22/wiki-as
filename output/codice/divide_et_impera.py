"""Verifica di 06-Merge Sort.pdf e 07-Quicksort.pdf.

Merge e Merge-Sort (06 pp.7-25, slide aggiornate): traduzione 1:1 dello pseudocodice con array indicizzati da 1.
Ricorrenze (06 pp.27-43): verifiche numeriche dei limiti ottenuti con sostituzione, albero, esperto.
Partition e Quicksort (07 pp.4-23): traccia di pp.5-11, casi peggiore/migliore, versione randomizzata.
Torre di Hanoi (06 pp.2-5) e Nuts and Bolts (07 pp.24-25): soluzioni (mie) verificate.

Esecuzione: python divide_et_impera.py
"""
import math
import random
from functools import lru_cache

INF = math.inf
CONTROLLA = {"attivo": True}   # verifica degli invarianti a ogni iterazione: solo sulle tracce piccole


# ------------------------------------------------------------------ MERGE (06 p.16)
def merge(A, p, q, r, conta=None):
    """A e' una lista con A[0] inutilizzato (indici da 1)."""
    n1 = q - p + 1                          # n1 <- q-p+1
    n2 = r - q                              # n2 <- r-q
    L = [None] * (n1 + 2)                   # L[1..n1+1]
    R = [None] * (n2 + 2)                   # R[1..n2+1]
    for i in range(1, n1 + 1):
        L[i] = A[p + i - 1]                 # L[i] <- A[p+i-1]
    for j in range(1, n2 + 1):
        R[j] = A[q + j]                     # R[j] <- A[q+j]
    L[n1 + 1] = R[n2 + 1] = INF             # sentinelle
    i = j = 1
    for k in range(p, r + 1):               # for k <- p to r
        # invariante (06 p.19): A[p..k-1] = i k-p elementi piu' piccoli di L e R, ordinati
        if CONTROLLA["attivo"]:
            assert A[p:k] == sorted(L[1:n1 + 1] + R[1:n2 + 1])[:k - p]
        if conta is not None:
            conta[0] += 1
        if L[i] <= R[j]:
            A[k] = L[i]; i += 1
        else:
            A[k] = R[j]; j += 1
    return L, R


def merge_sort(A, p, r, conta=None, livelli=None, prof=0):
    if p < r:
        q = (p + r) // 2                    # q <- floor((p+r)/2)
        merge_sort(A, p, q, conta, livelli, prof + 1)
        merge_sort(A, q + 1, r, conta, livelli, prof + 1)
        merge(A, p, q, r, conta)
        if livelli is not None:
            livelli.setdefault(prof, []).append(A[p:r + 1])


# ------------------------------------------------------------------ PARTITION / QUICKSORT (07 p.12, p.4, p.20)
def partition(A, p, r, traccia=None, conta=None):
    x = A[r]                                # x <- A[r]
    i = p - 1                               # i <- p-1
    for j in range(p, r):                   # for j <- p to r-1
        # invariante (07 p.13)
        if CONTROLLA["attivo"]:
            assert all(A[k] <= x for k in range(p, i + 1))
            assert all(A[k] > x for k in range(i + 1, j))
        if conta is not None:
            conta[0] += 1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
        if traccia is not None:
            traccia.append((j, i, A[1:]))
    A[i + 1], A[r] = A[r], A[i + 1]         # exchange A[i+1] <-> A[r]
    return i + 1


def quicksort(A, p, r, conta=None, prof=0, maxprof=None):
    if maxprof is not None:
        maxprof[0] = max(maxprof[0], prof)
    if p < r:
        q = partition(A, p, r, conta=conta)
        quicksort(A, p, q - 1, conta, prof + 1, maxprof)
        quicksort(A, q + 1, r, conta, prof + 1, maxprof)


def randomized_quicksort(A, p, r, rng, conta=None):
    if p < r:
        i = rng.randint(p, r)               # i <- Random(p,r)
        A[r], A[i] = A[i], A[r]             # exchange A[r] <-> A[i]
        q = partition(A, p, r, conta=conta)
        randomized_quicksort(A, p, q - 1, rng, conta)
        randomized_quicksort(A, q + 1, r, rng, conta)


# ------------------------------------------------------------------ TORRE DI HANOI (06 pp.2-5)
def hanoi(n, da, a, via, mosse):
    if n == 0:
        return
    hanoi(n - 1, da, via, a, mosse)
    mosse.append((n, da, a))
    hanoi(n - 1, via, a, da, mosse)


# ------------------------------------------------------------------ NUTS AND BOLTS (07 pp.24-25)
def nuts_bolts_quadratico(dadi, bulloni):
    """NUTS-BOLTS-QUADRATICO(D, B) della pagina nuts-and-bolts (indici da 1 -> da 0)."""
    D, B = list(dadi), list(bulloni)
    n, test = len(D), 0
    for i in range(n):                    # riga 1: for i <- 1 to n
        j = i                             # riga 2: j <- i
        test += 1
        while D[j] != B[i]:               # riga 3: while D[j] non combacia con B[i]
            j += 1                        # riga 4
            test += 1
        D[i], D[j] = D[j], D[i]           # riga 5: exchange D[i] <-> D[j]
        assert all(D[k] == B[k] for k in range(i + 1))   # invariante: D[1..i] accoppiati
    return list(zip(D, B)), test


def nuts_bolts_randomizzato(dadi, bulloni, rng, test):
    if not dadi:
        return []
    perno = rng.choice(dadi)                          # dado scelto a caso
    bm, bM, bx = [], [], None
    for b in bulloni:                                 # confronto dado-bullone: n test
        test[0] += 1
        if b < perno: bm.append(b)
        elif b > perno: bM.append(b)
        else: bx = b
    dm, dM = [], []
    for d in dadi:                                    # confronto con il bullone gemello: n-1 test
        if d is perno: continue
        test[0] += 1
        (dm if d < bx else dM).append(d)
    return (nuts_bolts_randomizzato(dm, bm, rng, test) + [(perno, bx)]
            + nuts_bolts_randomizzato(dM, bM, rng, test))


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(20000)               # quicksort su input ordinato: profondita' n-1
    print("== Merge, traccia di 06 p.17: A[p..r] = <2,4,5,7,1,2,3,6> ==")
    A = [None, 2, 4, 5, 7, 1, 2, 3, 6]
    L, R = merge(A, 1, 4, 8)
    print("  L =", L[1:], " R =", R[1:], " ->  A =", A[1:])

    print("\n== Merge-Sort su <5,2,8,0,4,7,1,9,3,2,6> (06 p.8), sequenze prodotte per profondita' ==")
    A = [None, 5, 2, 8, 0, 4, 7, 1, 9, 3, 2, 6]
    livelli = {}
    merge_sort(A, 1, 11, livelli=livelli)
    for k in sorted(livelli, reverse=True):
        print(f"  profondita' {k}: {livelli[k]}")
    print("  risultato:", A[1:])

    CONTROLLA["attivo"] = False
    print("\n== Merge-Sort: confronti nel ciclo for di Merge contro n lg n (n potenza di 2) ==")
    for n in [2, 8, 64, 1024]:
        c = [0]; A = [None] + random.sample(range(n), n); merge_sort(A, 1, n, conta=c)
        print(f"  n={n:5d}: iterazioni del for di Merge = {c[0]:6d}, n lg n = {n * int(math.log2(n)):6d}")

    print("\n== 06 pp.28-29: T(n) = 2T(floor(n/2)) + n, T(1) = 1 ==")
    @lru_cache(None)
    def T1(n): return 1 if n == 1 else 2 * T1(n // 2) + n
    print(f"  T(1)={T1(1)}, T(2)={T1(2)}, T(3)={T1(3)}")
    peggio = max(T1(n) / (n * math.log2(n)) for n in range(2, 100001))
    print(f"  max_(2<=n<=10^5) T(n)/(n lg n) = {peggio:.4f}  (deve essere <= c = 2)")

    print("\n== 06 pp.32-39: T(n) = 3T(floor(n/4)) + n^2 (c = 1), limite d >= 16c/13 = 1.2308 ==")
    @lru_cache(None)
    def T2(n): return 1 if n < 4 else 3 * T2(n // 4) + n * n
    print(f"  max_(1<=n<=10^5) T(n)/n^2 = {max(T2(n) / (n * n) for n in range(1, 100001)):.4f}")
    print(f"  T(4^8)/(4^8)^2 = {T2(4 ** 8) / (4 ** 8) ** 2:.4f}  -> 16/13 = {16 / 13:.4f}")

    print("\n== 06 pp.42-43: esempi del teorema dell'esperto (n potenza della base) ==")
    @lru_cache(None)
    def T3(n): return 1 if n <= 1 else 9 * T3(n // 3) + n
    @lru_cache(None)
    def T4(n): return 1 if n <= 1 else T4(2 * n // 3) + 1
    @lru_cache(None)
    def T5(n): return 1 if n <= 1 else 3 * T5(n // 4) + n * math.log2(n)
    @lru_cache(None)
    def T6(n): return 1 if n <= 1 else 2 * T6(n // 2) + n * math.log2(n)
    for k in [5, 8, 11]:
        n = 3 ** k
        print(f"  9T(n/3)+n,     n=3^{k:<2}: T/n^2      = {T3(n) / n ** 2:.4f}")
    for n in [10 ** 3, 10 ** 6, 10 ** 9]:
        print(f"  T(2n/3)+1,     n=10^{int(math.log10(n))}: T/lg n     = {T4(n) / math.log2(n):.4f}  (-> 1/lg(3/2) = {1 / math.log2(1.5):.4f})")
    for k in [5, 8, 11]:
        n = 4 ** k
        print(f"  3T(n/4)+nlgn,  n=4^{k:<2}: T/(n lg n) = {T5(n) / (n * math.log2(n)):.4f}")
    for k in [10, 20, 40]:
        n = 2 ** k
        print(f"  2T(n/2)+nlgn,  n=2^{k:<2}: T/(n lg n) = {T6(n) / (n * math.log2(n)):.3f},  T/(n lg^2 n) = {T6(n) / (n * math.log2(n) ** 2):.4f}")

    CONTROLLA["attivo"] = True
    print("\n== Partition, traccia di 07 pp.5-11 su <2,8,7,1,3,5,6,4> ==")
    A = [None, 2, 8, 7, 1, 3, 5, 6, 4]
    tr = []
    q = partition(A, 1, 8, traccia=tr)
    for j, i, s in tr:
        print(f"  j={j} i={i}: {s}")
    print(f"  dopo lo scambio finale: {A[1:]}, return q = {q}")

    CONTROLLA["attivo"] = False
    print("\n== Quicksort: array gia' ordinato (caso peggiore, 07 p.14) e casuale ==")
    for n in [10, 100, 1000]:
        c = [0]; mp = [0]; A = [None] + list(range(1, n + 1)); quicksort(A, 1, n, c, 0, mp)
        c2 = [0]; mp2 = [0]; B = [None] + random.sample(range(n), n); quicksort(B, 1, n, c2, 0, mp2)
        print(f"  n={n:5d}: ordinato -> confronti {c[0]:7d} = n(n-1)/2 = {n * (n - 1) // 2:7d}, profondita' {mp[0]};"
              f" casuale -> confronti {c2[0]:6d}, profondita' {mp2[0]}")

    print("\n== Quicksort randomizzato su input ordinato (media di 20 esecuzioni) ==")
    rng = random.Random(1)
    for n in [100, 1000, 10000]:
        tot = 0
        for _ in range(20):
            c = [0]; A = [None] + list(range(n)); randomized_quicksort(A, 1, n, rng, c); tot += c[0]
            assert A[1:] == sorted(A[1:])
        print(f"  n={n:6d}: confronti medi {tot / 20:10.0f};  2 n ln n = {2 * n * math.log(n):10.0f};  n(n-1)/2 = {n * (n - 1) // 2}")

    print("\n== 07 p.17: split 9:1, profondita' del ramo piu' lungo = log_(10/9) n ==")
    for n in [10 ** 3, 10 ** 6]:
        m, livelli = n, 0
        while m > 1:
            m = m * 9 / 10; livelli += 1
        print(f"  n=10^{int(math.log10(n))}: livelli {livelli}, log_(10/9) n = {math.log(n, 10 / 9):.1f}, log_10 n = {math.log10(n):.0f}")

    print("\n== Torre di Hanoi (06 pp.2-5) ==")
    mosse = []
    hanoi(3, "A", "C", "B", mosse)
    print("  3 dischi:", ", ".join(f"disco {d}: {x}->{y}" for d, x, y in mosse))
    for n in [1, 2, 3, 4, 10]:
        m = []; hanoi(n, "A", "C", "B", m)
        print(f"  n={n:2d}: {len(m)} mosse = 2^n - 1 = {2 ** n - 1}")

    print("\n== Nuts and Bolts (07 pp.24-25) ==")
    print("  istanza delle animazioni, quadratico:", nuts_bolts_quadratico([4, 1, 6, 3, 5, 2], [3, 6, 2, 5, 1, 4])[1], "test")
    for n in [6, 10]:
        peggiore = nuts_bolts_quadratico(list(range(2, n + 1)) + [1], list(range(1, n + 1)))[1]
        print(f"  quadratico, dadi <2..n,1> e bulloni <1..n>, n={n}: {peggiore} test = n(n+1)/2 = {n * (n + 1) // 2}")
    rng = random.Random(7)
    for n in [10, 100, 1000]:
        dadi = rng.sample(range(n * 10), n); bulloni = dadi[:]; rng.shuffle(bulloni)
        cq, tq = nuts_bolts_quadratico(dadi, bulloni)
        tot = 0
        for _ in range(20):
            t = [0]; cr = nuts_bolts_randomizzato(dadi, bulloni, rng, t); tot += t[0]
            assert all(d == b for d, b in cr) and len(cr) == n
        print(f"  n={n:5d}: quadratico {tq:7d} test (<= n(n+1)/2 = {n * (n + 1) // 2});"
              f" randomizzato {tot / 20:8.0f} test in media (4 n ln n = {4 * n * math.log(n):8.0f})")
