"""Verifiche numeriche per le lezioni 08 (Grafi e alberi) e 09 (Alberi binari di ricerca).

Grafi (08 pp.26-35): liste di adiacenza con insert_edge in testa, gradi, spazio m+n contro n^2.
Alberi (08 pp.37-44): archi n-1, altezza dell'albero k-ario perfetto, bilanciato contro degenere.
BST (09 pp.6-21): traduzione 1:1 dello pseudocodice (left, right, p, key; NIL = None).

Esecuzione: python grafi_e_alberi.py
"""
import math
import random


# ------------------------------------------------------------------ GRAFI (08 pp.28-35)
class Grafo:
    """Liste di adiacenza come nel codice C di 08 pp.31-35 (vertici 1..n, inserimento in testa)."""

    def __init__(self, n, diretto):           # initialize_graph (p.33)
        self.nvertices, self.nedges, self.directed = n, 0, diretto
        self.edges = {i: [] for i in range(1, n + 1)}   # lista: indice 0 = testa
        self.degree = {i: 0 for i in range(1, n + 1)}

    def insert_edge(self, x, y, diretto):     # insert_edge (p.35)
        self.edges[x].insert(0, y)            # p->next = g->edges[x]; g->edges[x] = p
        self.degree[x] += 1
        if not diretto:
            self.insert_edge(y, x, True)      # la seconda copia dell'arco non orientato
        else:
            self.nedges += 1


def matrice(g):
    n = g.nvertices
    M = [[0] * (n + 1) for _ in range(n + 1)]
    for x in g.edges:
        for y in g.edges[x]:
            M[x][y] = 1
    return M


# ------------------------------------------------------------------ BST (09)
class Nodo:
    def __init__(self, key):
        self.key, self.left, self.right, self.p = key, None, None, None


class Albero:
    def __init__(self):
        self.root = None


passi = {"chiamate": 0}


def inorder_tree_walk(x, out):               # 09 p.8
    passi["chiamate"] += 1
    if x is not None:
        inorder_tree_walk(x.left, out)
        out.append(x.key)
        inorder_tree_walk(x.right, out)


def tree_search(x, k):                       # 09 p.10
    if x is None or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left, k)
    return tree_search(x.right, k)


def iterative_tree_search(x, k):             # 09 p.11
    while x is not None and k != x.key:
        x = x.left if k < x.key else x.right
    return x


def tree_minimum(x):                         # 09 p.12
    while x.left is not None:
        x = x.left
    return x


def tree_maximum(x):
    while x.right is not None:
        x = x.right
    return x


def tree_successor(x):                       # 09 p.14
    if x.right is not None:
        return tree_minimum(x.right)
    y = x.p
    while y is not None and x is y.right:
        x, y = y, y.p
    return y


def tree_insert(T, z):                       # 09 p.16
    y, x = None, T.root
    while x is not None:
        y = x
        x = x.left if z.key < x.key else x.right
    z.p = y
    if y is None:
        T.root = z                           # albero vuoto
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z


def tree_delete(T, z):                       # 09 p.20 (versione con copia della chiave)
    y = z if (z.left is None or z.right is None) else tree_successor(z)
    x = y.left if y.left is not None else y.right
    if x is not None:                        # y non e' foglia
        x.p = y.p
    if y.p is None:                          # y e' radice
        T.root = x
    elif y is y.p.left:
        y.p.left = x
    else:
        y.p.right = x
    if y is not z:                           # terzo caso
        z.key = y.key
    return y


def costruisci(chiavi):
    T = Albero()
    for k in chiavi:
        tree_insert(T, Nodo(k))
    return T


def altezza(x):
    return -1 if x is None else 1 + max(altezza(x.left), altezza(x.right))


def forma(x):
    if x is None:
        return "-"
    if x.left is None and x.right is None:
        return str(x.key)
    return f"{x.key}({forma(x.left)},{forma(x.right)})"


def verifica_bst(x, lo=-math.inf, hi=math.inf):
    return x is None or (lo <= x.key <= hi and verifica_bst(x.left, lo, x.key) and verifica_bst(x.right, x.key, hi))


if __name__ == "__main__":
    print("== 08 p.28: liste di adiacenza del grafo a 5 vertici ==")
    g = Grafo(5, False)
    for x, y in [(1, 2), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5)]:
        g.insert_edge(x, y, False)
    for v in g.edges:
        print(f"  {v}: {g.edges[v]}  (grado {g.degree[v]})")
    print(f"  m = {g.nedges}, somma dei gradi = {sum(g.degree.values())} = 2m; nodi di lista = {sum(len(l) for l in g.edges.values())}")
    M = matrice(g)
    print("  matrice simmetrica:", all(M[i][j] == M[j][i] for i in range(1, 6) for j in range(1, 6)))
    for n, m in [(5, 7), (1000, 3000), (1000, 499500)]:
        print(f"  n={n}, m={m}: liste n+2m = {n + 2 * m}, matrice n^2 = {n * n}")

    print("\n== 08 pp.39-43: alberi ==")
    print("  archi = n - 1 per n = 7:", 7 - 1)
    for k in [2, 3]:
        for h in [2, 3]:
            n = (k ** (h + 1) - 1) // (k - 1)
            hh = math.log(n * (k - 1) + 1, k) - 1
            print(f"  k={k}, h={h}: n = {n} nodi, log_k(n(k-1)+1) - 1 = {hh:.0f}")
    bil = costruisci([4, 2, 6, 1, 3, 5, 7]); deg = costruisci([1, 2, 3, 4, 5, 6, 7])
    print(f"  7 nodi: bilanciato h = {altezza(bil.root)}, degenere h = {altezza(deg.root)}")

    print("\n== 09 p.7-9: BST e visita in ordine ==")
    T = costruisci([5, 3, 7, 2, 5, 8])
    out = []; passi["chiamate"] = 0
    inorder_tree_walk(T.root, out)
    print("  albero:", forma(T.root), " visita in ordine:", out, " chiamate:", passi["chiamate"], "= 2n+1 =", 2 * 6 + 1)
    for n in [10, 100, 1000]:
        R = costruisci(random.Random(n).sample(range(10 * n), n)); out = []; passi["chiamate"] = 0
        inorder_tree_walk(R.root, out)
        assert out == sorted(out)
        print(f"  n={n}: chiamate {passi['chiamate']} = 2n+1 = {2 * n + 1}")

    print("\n== 09 pp.13-14: successore (albero 15,6,18,3,7,17,20,2,4,13,9) ==")
    S = costruisci([15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9])
    print("  albero:", forma(S.root))
    for k in [6, 13, 9, 20]:
        s = tree_successor(tree_search(S.root, k))
        print(f"  successore di {k}: {s.key if s else 'NIL'}")
    print("  minimo:", tree_minimum(S.root).key, " massimo:", tree_maximum(S.root).key,
          " ricerca 13 (ric/iter):", tree_search(S.root, 13).key, iterative_tree_search(S.root, 13).key,
          " ricerca 11:", tree_search(S.root, 11))

    print("\n== 09 pp.16-18: inserimento ==")
    I = costruisci([15, 6, 18, 3, 7, 17, 20, 2, 4, 13])
    tree_insert(I, Nodo(19))
    print("  dopo Insert(19):", forma(I.root), " BST:", verifica_bst(I.root))
    J = costruisci([15, 6, 18, 3, 7, 17, 19, 2, 4, 13, 20])
    tree_insert(J, Nodo(10))
    print("  albero di p.18 + Insert(10):", forma(J.root), " BST:", verifica_bst(J.root))

    print("\n== 09 pp.19-21: eliminazione (albero 15,6,18,3,10,17,20,2,8,13,9) ==")
    for k, caso in [(20, "z' nessun figlio"), (3, "z'' un figlio"), (6, "z''' due figli")]:
        D = costruisci([15, 6, 18, 3, 10, 17, 20, 2, 8, 13, 9])
        y = tree_delete(D, tree_search(D.root, k))
        print(f"  Delete({k}) [{caso}]: nodo tagliato y = {y.key}; albero = {forma(D.root)}; BST: {verifica_bst(D.root)}")
