"""Visite di un grafo (lezione 13): BFS, Print-Path, DFS, Topological-Sort e l'algoritmo di Dijkstra.

Traduzione dello pseudocodice delle slide (13 - Algoritmi di visita di un grafo.pdf, pp. 12, 22, 28, 40, 50). I grafi sono
rappresentati con liste di adiacenza (dict vertice -> lista), l'ordine delle liste e' quello che produce i risultati
mostrati nelle slide (le visite dipendono dall'ordine dei vicini, pp. 11 e 28).
"""
import math
from collections import deque

BIANCO, GRIGIO, NERO = "WHITE", "GRAY", "BLACK"

# ---------------------------------------------------------------- grafi delle slide
# p. 11: grafo non orientato (e' quello della Figura 22.3 del Cormen); l'ordine di ogni lista e' alfabetico
G_BFS = {"r": ["s", "v"], "s": ["r", "w"], "t": ["u", "w", "x"], "u": ["t", "x", "y"],
         "v": ["r"], "w": ["s", "t", "x"], "x": ["t", "u", "w", "y"], "y": ["u", "x"]}

# p. 28: grafo non orientato; le liste sono ordinate in modo da riprodurre i tempi della figura
G_DFS = {"s": ["a", "b", "c", "d", "f"], "a": ["s", "d", "e", "g"], "d": ["a", "g", "h", "s"], "g": ["d", "a"],
         "h": ["d"], "e": ["a"], "b": ["s", "f", "i"], "f": ["b", "i", "s"], "i": ["f", "b"], "c": ["s"]}
TEMPI_DFS = {"s": (1, 20), "a": (2, 11), "d": (3, 8), "g": (4, 5), "h": (6, 7), "e": (9, 10),
             "b": (12, 17), "f": (13, 16), "i": (14, 15), "c": (18, 19)}

# p. 39-40: grafo orientato aciclico (DAG); a ⇢ b ecc. tratteggiati nella figura sono archi come gli altri
DAG = {"a": ["d", "b"], "b": ["e"], "e": ["f"], "f": ["d"], "d": ["h", "c"], "c": ["g"], "g": ["j"], "j": ["i"], "h": ["i"], "i": []}

# p. 52: grafo pesato non orientato per Dijkstra (sorgente A)
ARCHI_DIJKSTRA = [("A", "B", 5), ("A", "D", 7), ("A", "F", 12), ("B", "C", 7), ("B", "D", 9), ("C", "D", 4), ("C", "E", 2),
                  ("C", "G", 5), ("D", "E", 3), ("D", "F", 4), ("E", "F", 7), ("E", "G", 2)]


def pesato(archi):
    g = {}
    for u, v, w in archi:
        g.setdefault(u, []).append((v, w))
        g.setdefault(v, []).append((u, w))
    return g


# ---------------------------------------------------------------- BFS (p. 12)
def bfs(G, s):
    color = {u: BIANCO for u in G}                      # for each vertex u in V[G]-{s}: color[u] <- WHITE
    d = {u: math.inf for u in G}                        # d[u] <- infinito
    pi = {u: None for u in G}                           # pi[u] <- NIL
    color[s], d[s], pi[s] = GRIGIO, 0, None             # color[s] <- GRAY; d[s] <- 0; pi[s] <- NIL
    Q = deque([s])                                      # Q <- vuota; Enqueue (Q,s)
    ordine = []                                         # ordine di estrazione dalla coda
    iterazioni_for = 0                                  # iterazioni del for each v in Adj[u], per l'analisi del costo
    while Q:                                            # while Q != vuota
        u = Q.popleft()                                 # do u <- Dequeue (Q)
        ordine.append(u)
        for v in G[u]:                                  # for each v in Adj[u]
            iterazioni_for += 1
            if color[v] == BIANCO:                      # do if color[v] = WHITE
                color[v] = GRIGIO                       # then color[v] <- GRAY
                d[v] = d[u] + 1                         # d[v] <- d[u]+1
                pi[v] = u                               # pi[v] <- u
                Q.append(v)                             # Enqueue (Q,v)
        color[u] = NERO                                 # color[u] <- BLACK
    return d, pi, ordine, iterazioni_for


def distanze_minime(G, s):
    """delta(s,v) calcolata indipendentemente (per verificare il teorema di p. 19)."""
    dist = {s: 0}
    pila = [s]
    while pila:
        u = pila.pop(0)
        for v in G[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                pila.append(v)
    return {u: dist.get(u, math.inf) for u in G}


def print_path(pi, s, v, out):
    """Print-Path (G,s,v), p. 22 (assume di aver eseguito BFS in precedenza)."""
    if v == s:
        out.append(s)
    elif pi[v] is None:
        out.append("no path from s to v exists")
    else:
        print_path(pi, s, pi[v], out)
        out.append(v)


# ---------------------------------------------------------------- DFS (p. 28)
def dfs(G, ordine_radici=None):
    color = {u: BIANCO for u in G}
    pi = {u: None for u in G}
    d, f = {}, {}
    tempo = [0]
    archi = {}                                          # classificazione degli archi (pp. 35-36)

    def visit(u):
        color[u] = GRIGIO                               # color[u] <- GRAY
        tempo[0] += 1                                   # time <- time+1
        d[u] = tempo[0]                                 # d[u] <- time
        for v in G[u]:                                  # for each v in Adj[u]
            if (u, v) not in archi and (v, u) not in archi:
                if color[v] == BIANCO:
                    archi[(u, v)] = "tree"
                elif color[v] == GRIGIO:
                    archi[(u, v)] = "back"
                else:
                    archi[(u, v)] = "forward" if d[u] < d[v] else "cross"
            if color[v] == BIANCO:                      # do if color[v] = WHITE
                pi[v] = u                               # then pi[v] <- u
                visit(v)                                # DFS-Visit (v)
        color[u] = NERO                                 # color[u] <- BLACK
        tempo[0] += 1
        f[u] = tempo[0]                                 # f[u] <- time <- time+1

    for u in (ordine_radici or list(G)):                # for each vertex u in V[G]
        if color[u] == BIANCO:
            visit(u)
    return d, f, pi, archi


def dfs_orientato(G, radici):
    """DFS su un grafo orientato con classificazione degli archi."""
    color = {u: BIANCO for u in G}
    d, f, archi = {}, {}, {}
    tempo = [0]
    ordine_fine = []

    def visit(u):
        color[u] = GRIGIO
        tempo[0] += 1
        d[u] = tempo[0]
        for v in G[u]:
            if color[v] == BIANCO:
                archi[(u, v)] = "tree"
                visit(v)
            elif color[v] == GRIGIO:
                archi[(u, v)] = "back"
            else:
                archi[(u, v)] = "forward" if d[u] < d[v] else "cross"
        color[u] = NERO
        tempo[0] += 1
        f[u] = tempo[0]
        ordine_fine.append(u)

    for u in radici:
        if color[u] == BIANCO:
            visit(u)
    return d, f, archi, ordine_fine


def topological_sort(G, radici):
    """Topological-Sort (G), p. 40: DFS, poi i vertici in ordine decrescente di tempo di completamento."""
    d, f, archi, fine = dfs_orientato(G, radici)
    lista = list(reversed(fine))                        # ogni vertice terminato va in testa alla lista
    return lista, d, f, archi


# ---------------------------------------------------------------- Dijkstra (p. 50)
def dijkstra(g, s):
    dist = {v: math.inf for v in g}                     # for i = 1 to n, dist[i] = infinito
    dist[s] = 0
    pred = {v: None for v in g}
    known = {s}                                         # known = {s}
    for v, w in g[s]:                                   # for each edge (s,v), dist[v] = d(s,v)
        dist[v] = w
        pred[v] = s
    last = s
    ordine = [s]
    ciclo = 0
    while len(known) < len(g):                          # while (last != t): qui si continua finche' tutti sono noti
        ciclo += 1
        v = min((x for x in g if x not in known), key=lambda x: (dist[x], x))   # select v tale che dist(v) = min_unknown dist(i)
        for x, w in g[v]:                               # for each (v,x): dist[x] = min(dist[x], dist[v] + w(v,x))
            if x not in known and dist[v] + w < dist[x]:
                dist[x] = dist[v] + w
                pred[x] = v
        last = v
        known.add(v)                                    # known = known U {v}
        ordine.append(v)
    return dist, pred, ordine


if __name__ == "__main__":
    # BFS di p. 11-12 (sorgente s)
    d, pi, ordine, it = bfs(G_BFS, "s")
    print("BFS da s: ordine di estrazione", ordine)
    print("  d =", d)
    print("  pi =", pi)
    assert d == {"s": 0, "r": 1, "w": 1, "v": 2, "t": 2, "x": 2, "u": 3, "y": 3}
    assert d == distanze_minime(G_BFS, "s")             # teorema di p. 19: d[v] = delta(s,v)
    n = len(G_BFS)
    m2 = sum(len(l) for l in G_BFS.values())
    print(f"  iterazioni del for interno = {it} = somma delle lunghezze delle liste = 2|E| = {m2}; |V| = {n}")
    assert it == m2
    out = []
    print_path(pi, "s", "y", out)
    print("  Print-Path (G,s,y):", out)
    out = []
    G2 = dict(G_BFS); G2["z"] = []
    d2, pi2, _, _ = bfs(G2, "s")
    print_path(pi2, "s", "z", out)
    print("  Print-Path (G,s,z) con z non raggiungibile:", out)
    # le visite dipendono dall'ordine dei vicini, le distanze no (p. 11)
    for ordine_vic in (sorted, lambda l: sorted(l, reverse=True)):
        Gx = {u: ordine_vic(l) for u, l in G_BFS.items()}
        dx, pix, _, _ = bfs(Gx, "s")
        assert dx == d
        print("  ordine dei vicini diverso: pi =", pix)

    # DFS di p. 28
    df, ff, pif, archi = dfs(G_DFS, ["s"])
    tempi = {u: (df[u], ff[u]) for u in G_DFS}
    print("DFS da s:", tempi)
    assert tempi == TEMPI_DFS
    print("  archi:", archi)
    assert all(df[u] < ff[u] for u in G_DFS)
    # struttura a parentesi (p. 30)
    eventi = sorted([(df[u], "(" + u) for u in G_DFS] + [(ff[u], u + ")") for u in G_DFS])
    print("  parentesi:", " ".join(e for _, e in eventi))
    # nei grafi non orientati ogni arco e' tree o back (p. 37)
    assert set(archi.values()) <= {"tree", "back"}
    print("  tree edges:", sum(1 for v in archi.values() if v == "tree"), "back edges:", sum(1 for v in archi.values() if v == "back"))
    # Teorema 1 (nesting): per ogni coppia gli intervalli sono disgiunti o contenuti
    for u in G_DFS:
        for v in G_DFS:
            if u != v:
                a, b = tempi[u], tempi[v]
                disgiunti = a[1] < b[0] or b[1] < a[0]
                contenuti = (b[0] < a[0] and a[1] < b[1]) or (a[0] < b[0] and b[1] < a[1])
                assert disgiunti or contenuti
    print("  Teorema 1 verificato su tutte le coppie")
    # costo: Theta(V) + Theta(E) con E = somma liste / 2
    print("  |V| =", len(G_DFS), "somma delle liste =", sum(len(l) for l in G_DFS.values()))

    # Ordinamento topologico di p. 39-40
    lista, dt, ft, archi_t = topological_sort(DAG, ["a"])
    print("Topological-Sort:", lista)
    assert lista == ["a", "b", "e", "f", "d", "c", "g", "j", "h", "i"]
    assert all(ft[v] < ft[u] for u in DAG for v in DAG[u])          # Teorema 1 di p. 43: f[v] < f[u] per ogni arco u->v
    assert "back" not in archi_t.values()                            # Lemma 1: DAG <=> nessun back edge
    print("  tempi d/f:", {u: (dt[u], ft[u]) for u in DAG})
    ciclico = {"a": ["b"], "b": ["c"], "c": ["a"]}
    _, _, archi_c, _ = dfs_orientato(ciclico, ["a"])
    print("  grafo con ciclo a->b->c->a: archi", archi_c)
    assert "back" in archi_c.values()

    # Dijkstra di p. 51-52 (sorgente A)
    g = pesato(ARCHI_DIJKSTRA)
    dist, pred, ordine = dijkstra(g, "A")
    print("Dijkstra da A: dist", dist, "ordine", ordine)
    assert dist == {"A": 0, "B": 5, "D": 7, "E": 10, "C": 11, "F": 11, "G": 12}
    print("  predecessori:", pred)
    # confronto con Bellman-Ford semplice (rilassamenti ripetuti)
    ref = {v: math.inf for v in g}
    ref["A"] = 0
    for _ in range(len(g)):
        for u in g:
            for v, w in g[u]:
                ref[v] = min(ref[v], ref[u] + w)
    assert ref == dist
    n = len(g)
    print(f"  n = {n}: selezione del minimo O(n) e aggiornamento O(n) per n volte -> O(n^2) = {n * n} operazioni elementari al piu'")
