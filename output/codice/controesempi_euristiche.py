"""Verifica dei controesempi della lezione 01-Introduzione.pdf.

Robot Tour Optimization (TSP), pp.14-35:
  - NearestNeighbor sui punti della retta di p.22-24: -21, -5, -1, 0, 1, 3, 11 partendo da 0
  - ClosestPair sui 6 punti di p.28 (coordinate lette dal grafico, approssimate)
  - OptimalTSP (forza bruta sulle permutazioni) come riferimento
Movie Scheduling, pp.37-60:
  - EarliestJobFirst, ShortestJobFirst, ExhaustiveScheduling, OptimalScheduling
  - controesempi minimi per le frasi di p.46 e p.55

Solo libreria standard. Esecuzione: python controesempi_euristiche.py
"""
import itertools
import math


# --------------------------------------------------------------------------- TSP
def dist(p, q):
    return math.dist(p, q)


def lunghezza_tour(tour):
    """Lunghezza del ciclo che visita i punti nell'ordine dato e torna al primo."""
    return sum(dist(tour[i], tour[(i + 1) % len(tour)]) for i in range(len(tour)))


def nearest_neighbor(P, p0, rompi_parita=None):
    """NearestNeighbor(P) di p.18. `rompi_parita` sceglie tra punti equidistanti
    (la slide non specifica la regola: la figura di p.24 li rompe nel modo peggiore)."""
    tour, restanti = [p0], [p for p in P if p != p0]
    while restanti:
        ultimo = tour[-1]
        dmin = min(dist(ultimo, q) for q in restanti)
        candidati = [q for q in restanti if math.isclose(dist(ultimo, q), dmin)]
        scelto = rompi_parita(candidati) if rompi_parita else candidati[0]
        tour.append(scelto)
        restanti.remove(scelto)
    return tour


def closest_pair(P):
    """ClosestPair(P) di p.26: n-1 volte unisce la coppia di estremi più vicina
    appartenente a catene distinte, poi chiude il ciclo unendo i due estremi finali."""
    catene = [[p] for p in P]
    archi = []
    for _ in range(len(P) - 1):
        d, sm, tm, ci, cj = math.inf, None, None, None, None
        for i, j in itertools.combinations(range(len(catene)), 2):
            for s in {catene[i][0], catene[i][-1]}:
                for t in {catene[j][0], catene[j][-1]}:
                    if dist(s, t) <= d - 1e-12:          # prima coppia minima trovata
                        d, sm, tm, ci, cj = dist(s, t), s, t, i, j
        archi.append((sm, tm))
        a, b = catene[ci], catene[cj]
        if a[0] == sm:
            a = a[::-1]                                  # sm in coda ad a
        if b[-1] == tm:
            b = b[::-1]                                  # tm in testa a b
        catene[ci] = a + b
        del catene[cj]
    tour = catene[0]
    return tour, archi


def optimal_tsp(P):
    """OptimalTSP(P) di p.29: prova tutte le n! permutazioni."""
    migliore, d = None, math.inf
    for perm in itertools.permutations(P):
        c = lunghezza_tour(perm)
        if c <= d:
            d, migliore = c, perm
    return list(migliore), d


def demo_tsp():
    print("== TSP: punti sulla retta (p.22-24), partenza da 0 ==")
    P = [(-21, 0), (-5, 0), (-1, 0), (0, 0), (1, 0), (3, 0), (11, 0)]
    # parità rotte come nella figura di p.24: 0 -> 1 -> -1 -> 3 -> -5 -> 11 -> -21 -> 0
    ordine_figura = {(1, 0): 0, (-1, 0): 1, (3, 0): 2, (-5, 0): 3, (11, 0): 4, (-21, 0): 5}
    nn = nearest_neighbor(P, (0, 0), lambda c: min(c, key=lambda q: ordine_figura.get(q, 9)))
    print("NearestNeighbor:", [p[0] for p in nn], "lunghezza =", lunghezza_tour(nn))
    opt, d = optimal_tsp(P)
    print("OptimalTSP:     ", [p[0] for p in opt], "lunghezza =", d)

    print("\n== TSP: ClosestPair sui 6 punti di p.28 (coordinate approssimate dal grafico) ==")
    h, v = 1.12, 0.88                 # passo orizzontale e verticale letti dalla figura
    nomi = {(0, v): "A", (h, v): "B", (2 * h, v): "C", (0, 0): "D", (h, 0): "E", (2 * h, 0): "F"}
    P = list(nomi)
    tour, archi = closest_pair(P)
    print("archi scelti in ordine:", [nomi[s] + nomi[t] for s, t in archi], "+ chiusura",
          nomi[tour[0]] + nomi[tour[-1]])
    print("ClosestPair: ", "".join(nomi[p] for p in tour), f"lunghezza = {lunghezza_tour(tour):.3f}")
    opt, d = optimal_tsp(P)
    print("OptimalTSP:  ", "".join(nomi[p] for p in opt), f"lunghezza = {d:.3f}")


# --------------------------------------------------------------- Movie Scheduling
def si_sovrappongono(a, b):
    return a[0] < b[1] and b[0] < a[1]


def earliest_job_first(S):
    """p.38: accetta il job che inizia prima tra quelli compatibili, ripeti."""
    accettati = []
    for j in sorted(S, key=lambda x: x[0]):
        if all(not si_sovrappongono(j, a) for a in accettati):
            accettati.append(j)
    return accettati


def shortest_job_first(S):
    """p.47: accetta il job più corto, elimina lui e quelli che lo intersecano."""
    S, accettati = list(S), []
    while S:
        j = min(S, key=lambda x: x[1] - x[0])
        accettati.append(j)
        S = [x for x in S if x != j and not si_sovrappongono(x, j)]
    return accettati


def exhaustive_scheduling(S):
    """p.58: prova tutti i 2^n sottoinsiemi."""
    migliore = []
    for k in range(len(S) + 1):
        for Si in itertools.combinations(S, k):
            if all(not si_sovrappongono(a, b) for a, b in itertools.combinations(Si, 2)) \
                    and len(Si) > len(migliore):
                migliore = list(Si)
    return migliore


def optimal_scheduling(S):
    """p.60: accetta il job che termina prima, elimina quelli che lo intersecano."""
    S, accettati = list(S), []
    while S:
        j = min(S, key=lambda x: x[1])
        accettati.append(j)
        S = [x for x in S if x != j and not si_sovrappongono(x, j)]
    return accettati


def demo_scheduling():
    print("\n== Movie Scheduling: controesempio per EarliestJobFirst (frase di p.46) ==")
    S = [(0, 10), (1, 2), (3, 4), (5, 6)]          # un job lungo che inizia per primo
    print("EJF:", earliest_job_first(S), "| ottimo:", exhaustive_scheduling(S),
          "| OptimalScheduling:", optimal_scheduling(S))

    print("\n== Movie Scheduling: controesempio per ShortestJobFirst (frase di p.55) ==")
    S = [(0, 5), (4, 7), (6, 11)]                  # il più corto blocca gli altri due
    print("SJF:", shortest_job_first(S), "| ottimo:", exhaustive_scheduling(S),
          "| OptimalScheduling:", optimal_scheduling(S))

    print("\n== OptimalScheduling = ottimo su tutte le istanze piccole (verifica esaustiva) ==")
    fallimenti = 0
    punti = range(6)
    tutti = [(a, b) for a in punti for b in punti if a < b]
    for k in range(1, 5):
        for S in itertools.combinations(tutti, k):
            if len(optimal_scheduling(S)) != len(exhaustive_scheduling(S)):
                fallimenti += 1
    print("istanze con fino a 4 intervalli su [0,5]: fallimenti =", fallimenti)


if __name__ == "__main__":
    demo_tsp()
    demo_scheduling()
