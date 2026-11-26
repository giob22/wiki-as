"""Heap, Max-Heapify, Build-Max-Heap, Heap-Sort e operazioni della coda a priorita' (lezione 10).

Traduzione 1:1 dello pseudocodice delle slide (10 - Heap - Heapsort.pdf, pp. 5-49). Gli indici dello
pseudocodice partono da 1: l'array Python ha un elemento in piu' in testa (A[0] non si usa), cosi'
A[i] corrisponde esattamente ad A[i] delle slide. Il codice serve solo a verificare tracce e conteggi.
"""
import math


def parent(i): return i // 2          # Parent(i) = floor(i/2)
def left(i): return 2 * i             # Left(i) = 2*i
def right(i): return 2 * i + 1        # Right(i) = 2*i + 1


class Heap:
    def __init__(self, valori):
        self.A = [None] + list(valori)           # A[1..length]
        self.size = len(valori)                  # heap-size[A]
        self.scambi = 0
        self.chiamate = 0                        # chiamate di Max-Heapify

    length = property(lambda self: len(self.A) - 1)

    def lista(self):
        return self.A[1:]

    def exchange(self, i, j):
        self.A[i], self.A[j] = self.A[j], self.A[i]
        self.scambi += 1


def max_heapify(H, i):
    """Max-Heapify (A,i), p. 11: righe 1-10 dello pseudocodice."""
    H.chiamate += 1
    l = left(i)                                          # 1  l <- Left(i)
    r = right(i)                                         # 2  r <- Right(i)
    largest = i                                          # 3
    if l <= H.size and H.A[l] > H.A[largest]:            # 4
        largest = l                                      # 5
    if r <= H.size and H.A[r] > H.A[largest]:            # 6
        largest = r                                      # 7
    if largest != i:                                     # 8
        H.exchange(i, largest)                           # 9
        max_heapify(H, largest)                          # 10


def build_max_heap(H):
    """Build-Max-Heap (A), p. 20."""
    H.size = H.length                                    # 1
    for i in range(H.length // 2, 0, -1):                # 2  for i <- floor(length/2) downto 1
        max_heapify(H, i)                                # 3


def heap_sort(H, passi=None):
    """Heap-Sort (A), p. 41."""
    build_max_heap(H)                                    # 1
    for i in range(H.length, 1, -1):                     # 2  for i <- length[A] downto 2
        H.exchange(1, i)                                 # 3
        H.size -= 1                                      # 4
        max_heapify(H, 1)                                # 5
        if passi is not None:
            passi.append((i, H.lista()))


def heap_maximum(H):
    return H.A[1]                                        # p. 43


def heap_extract_max(H):
    """Heap-Extract-Max (A), p. 44."""
    if H.size < 1:
        raise ValueError("heap empty")                   # 1-2
    massimo = H.A[1]                                     # 3
    H.A[1] = H.A[H.size]                                 # 4
    H.size -= 1                                          # 5
    max_heapify(H, 1)                                    # 6
    return massimo                                       # 7


def heap_increase_key(H, i, key):
    """Heap-Increase-Key (A,i,key), p. 48."""
    if key < H.A[i]:
        raise ValueError("new key is smaller")           # 1-2
    H.A[i] = key                                         # 3
    while i > 1 and H.A[parent(i)] < H.A[i]:             # 4
        H.exchange(i, parent(i))                         # 5
        i = parent(i)                                    # 6


def max_heap_insert(H, key):
    """Max-Heap-Insert (A,key), p. 49."""
    H.size += 1                                          # 1
    if H.size >= len(H.A):
        H.A.append(None)
    H.A[H.size] = -math.inf                              # 2
    heap_increase_key(H, H.size, key)                    # 3


def altezza(n):
    return n.bit_length() - 1                            # floor(lg n)


def e_max_heap(A, size):
    return all(A[parent(i)] >= A[i] for i in range(2, size + 1))


if __name__ == "__main__":
    # Build-Max-Heap sull'array di p. 15
    H = Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    build_max_heap(H)
    print("Build-Max-Heap:", H.lista(), "chiamate Max-Heapify:", H.chiamate, "scambi:", H.scambi)
    assert H.lista() == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1] and e_max_heap(H.A, H.size)

    # Heap-Sort a partire dall'heap di p. 23
    passi = []
    H = Heap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
    H.size = 10
    for i in range(10, 1, -1):
        H.exchange(1, i)
        H.size -= 1
        max_heapify(H, 1)
        passi.append((i, H.lista()))
    for i, A in passi:
        print(f"  dopo i={i}:", A)
    assert H.lista() == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]

    # Heap-Sort completo, con il conteggio degli scambi
    H = Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    heap_sort(H)
    print("Heap-Sort:", H.lista(), "scambi:", H.scambi, "chiamate di Max-Heapify:", H.chiamate)

    # Heap-Increase-Key: p. 45-48 (la chiave 4, in posizione 9, diventa 15)
    H = Heap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
    heap_increase_key(H, 9, 15)
    print("Increase-Key(9, 15):", H.lista())
    assert H.lista() == [16, 15, 10, 14, 7, 9, 3, 2, 8, 1]

    # Heap-Extract-Max, Max-Heap-Insert
    H = Heap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
    print("Extract-Max:", heap_extract_max(H), H.lista()[:H.size])
    H = Heap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
    max_heap_insert(H, 15)
    print("Insert(15):", H.lista()[:H.size])

    # altezza e nodi per altezza (p. 21)
    for n in (1, 2, 3, 7, 10, 15, 16):
        print(f"n={n}: altezza floor(lg n) = {altezza(n)}")
    n = 10
    for h in range(altezza(n) + 1):
        conta = sum(1 for i in range(1, n + 1) if altezza(n // i) == h)
        print(f"  n={n}: nodi di altezza {h} = {conta}  (limite ceil(n/2^(h+1)) = {math.ceil(n / 2 ** (h + 1))})")

    # somma dei costi di Build-Max-Heap: sum_h ceil(n/2^(h+1)) * h  <= 2n
    for n in (10, 100, 1000):
        s = sum(math.ceil(n / 2 ** (h + 1)) * h for h in range(altezza(n) + 1))
        print(f"n={n}: sum ceil(n/2^(h+1)) h = {s} <= 2n = {2 * n}")

    # Esercizio di p. 50: Heap-Sort da zero su <6, 5, 3, 1, 8, 7, 2, 4>
    H = Heap([6, 5, 3, 1, 8, 7, 2, 4])
    print("p. 50 array:", H.lista())
    build_max_heap(H)
    print("  Build-Max-Heap:", H.lista(), "scambi:", H.scambi)
    for i in range(H.length, 1, -1):
        H.exchange(1, i)
        H.size -= 1
        max_heapify(H, 1)
        print(f"  i={i}:", H.lista(), "heap-size =", H.size)
    assert H.lista() == [1, 2, 3, 4, 5, 6, 7, 8]
