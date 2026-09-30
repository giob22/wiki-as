"""Verifica di 05-Insertion sort.pdf pp.30-33.

- findmatch (p.31): confronti di caratteri sull'esempio di p.30 e nel caso peggiore
- power (p.32): numero di moltiplicazioni = O(lg n)
- altezza di un albero d-ario, bit necessari, numeri armonici (p.32)
- p.33: log_{3/2}(10^6) e log_2(10^6)

Esecuzione: python stringhe_e_logaritmi.py
"""
import math


def findmatch(p, t):
    """Codice C di p.31 (indici da 0). Restituisce (posizione o -1, confronti di caratteri, righe di confronto)."""
    m, n = len(p), len(t)
    confronti, righe = 0, []
    for i in range(0, n - m + 1):            # for (i=0; i<=(n-m); i=i+1)
        j = 0
        riga = ""
        while j < m:                         # while ((j<m) && (t[i+j]==p[j]))
            confronti += 1
            riga += p[j]
            if t[i + j] != p[j]:
                break
            j += 1
        righe.append((i, riga))
        if j == m:
            return i, confronti, righe
    return -1, confronti, righe


moltiplicazioni = 0


def power(a, n):
    """Pseudocodice di p.32; conta le moltiplicazioni."""
    global moltiplicazioni
    if n == 0:
        return 1
    x = power(a, n // 2)                     # x = power(a, floor(n/2))
    if n % 2 == 0:
        moltiplicazioni += 1                 # x^2
        return x * x
    moltiplicazioni += 2                     # a * x^2
    return a * x * x


if __name__ == "__main__":
    print("== findmatch: p = abba, t = aababba (p.30) ==")
    pos, c, righe = findmatch("abba", "aababba")
    for i, r in righe:
        print("  " + "  " * i + " ".join(r), f"   (i={i})")
    print(f"  posizione = {pos} (da 0), confronti = {c}")

    print("\n== findmatch: caso peggiore t = a^n, p = a^(m-1) b ==")
    print("   n    m | confronti | (n-m+1)*m")
    for n, m in [(10, 3), (100, 10), (100, 50), (1000, 500)]:
        _, c, _ = findmatch("a" * (m - 1) + "b", "a" * n)
        print(f"{n:>5} {m:>4} | {c:>9} | {(n - m + 1) * m:>9}")

    print("\n== power(a, n): moltiplicazioni contro 2(floor(lg n)+1) ==")
    for n in [1, 2, 3, 7, 8, 15, 16, 1000, 10**6]:
        moltiplicazioni = 0
        v = power(2, n)
        assert v == 2 ** n
        print(f"  n={n:>8}: {moltiplicazioni:>3} moltiplicazioni, limite {2 * (int(math.log2(n)) + 1)}")

    print("\n== p.32: alberi, bit, numeri armonici ==")
    for d, n in [(2, 8), (3, 9), (10, 10**6)]:
        print(f"  albero con d={d}, n={n} foglie: h = log_d n = {math.log(n, d):.2f}")
    for n in [2, 5, 256, 1000, 10**6]:
        print(f"  n={n}: bit necessari = ceil(lg n) = {math.ceil(math.log2(n))}")
    for n in [10, 100, 10**4, 10**6]:
        H = sum(1 / i for i in range(1, n + 1))
        print(f"  H({n}) = {H:.4f}, ln n = {math.log(n):.4f}, differenza = {H - math.log(n):.4f}")

    print("\n== p.33: ricerca binaria con split 1/3-2/3 contro 1/2-1/2 ==")
    print(f"  log_(3/2)(10^6) = {math.log(10**6, 1.5):.2f}  -> ceil = {math.ceil(math.log(10**6, 1.5))}")
    print(f"  log_2(10^6)     = {math.log2(10**6):.2f}  -> ceil = {math.ceil(math.log2(10**6))}")
    print(f"  rapporto = 1/lg(3/2) = {1 / math.log2(1.5):.3f}")
    # simulazione: ogni domanda confronta con l'elemento a 1/3 (o 1/2) dei candidati rimasti;
    # nel caso peggiore si prosegue sempre nella parte piu' grande, finche' non restano candidati
    for divisore, nome in [(3, "1/3-2/3"), (2, "1/2-1/2")]:
        n, domande = 10**6, 0
        while n > 0:
            domande += 1
            sinistra = (n - 1) // divisore       # elementi prima di quello interrogato
            n = max(sinistra, n - 1 - sinistra)  # si continua nella parte piu' grande
        print(f"  split {nome}: {domande} domande nel caso peggiore (simulazione)")
