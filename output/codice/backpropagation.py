"""Backpropagation su un grafo computazionale (lezione 14).

Traduzione dello pseudocodice della slide (14 - Backpropagation.pdf, p. 22) e verifica dei numeri dell'esempio di
pp. 11-21: C(a,b) = 1/2 (sin(a b) + b - 1)^2 nel punto (2, 3). Il grafo e' un DAG per layer:
    a, b (layer 0) -> c = a*b -> d = sin(c) -> e = d + b -> C = 1/2 (e - 1)^2
"""
import math

# grafo: nodo -> (predecessori, funzione locale f_v, derivate locali df_v/dz_u per ciascun predecessore)
GRAFO = {
    "a": ([], None, None),
    "b": ([], None, None),
    "c": (["a", "b"], lambda x, y: x * y, lambda x, y: [y, x]),                   # c = a * b
    "d": (["c"], lambda x: math.sin(x), lambda x: [math.cos(x)]),                 # d = sin(c)
    "e": (["d", "b"], lambda x, y: x + y, lambda x, y: [1.0, 1.0]),               # e = d + b
    "C": (["e"], lambda x: 0.5 * (x - 1) ** 2, lambda x: [x - 1]),                # C = 1/2 (e - 1)^2
}
ORD = ["a", "b", "c", "d", "e", "C"]                                              # ordine topologico (= ordine dei layer)


def forward(grafo, ordine, ingressi):
    """FORWARD: per v in Ord, value[v] <- input[v] oppure f_v(value[u] per u in pred[v])."""
    value = {}
    for v in ordine:
        pred, f, _ = grafo[v]
        if not pred:                                    # v e' un input
            value[v] = ingressi[v]
        else:
            args = [value[u] for u in pred]
            value[v] = f(*args)
    return value


def backward(grafo, ordine, value, uscita):
    """BACKWARD: delta[v] = dC/dz_v; for v in reverse(Ord), for u in pred[v]: delta[u] += delta[v] * df_v/dz_u."""
    delta = {v: 0.0 for v in grafo}                     # for v in V: delta[v] <- 0
    delta[uscita] = 1.0                                 # delta[C] <- 1
    passi = []
    for v in reversed(ordine):
        pred, _, derivate = grafo[v]
        if not pred:
            continue
        dlocal = derivate(*[value[u] for u in pred])    # derivate locali, valutate con i valori del forward
        for u, dl in zip(pred, dlocal):
            delta[u] += delta[v] * dl
            passi.append((v, u, dl, dict(delta)))
    return delta, passi


if __name__ == "__main__":
    value = forward(GRAFO, ORD, {"a": 2.0, "b": 3.0})
    print("forward:", {k: round(v, 4) for k, v in value.items()})
    assert round(value["c"], 4) == 6.0 and round(value["d"], 4) == -0.2794
    assert round(value["e"], 4) == 2.7206 and round(value["C"], 4) == 1.4802

    delta, passi = backward(GRAFO, ORD, value, "C")
    print("backward:")
    for v, u, dl, d in passi:
        print(f"  da {v} a {u}: derivata locale {dl:.4f} -> delta[{u}] = {d[u]:.4f}")
    print("delta finali:", {k: round(v, 4) for k, v in delta.items()})
    assert round(delta["e"], 4) == 1.7206 and round(delta["d"], 4) == 1.7206
    assert round(delta["c"], 4) == 1.6521
    assert round(delta["a"], 4) == 4.9562 and round(delta["b"], 4) == 5.0247

    # verifica con la regola della catena a mano (p. 21)
    a, b = 2.0, 3.0
    dCda = (math.sin(a * b) + b - 1) * b * math.cos(a * b)
    dCdb = (math.sin(a * b) + b - 1) * (a * math.cos(a * b) + 1)
    print("regola della catena:", round(dCda, 4), round(dCdb, 4))
    assert abs(dCda - delta["a"]) < 1e-12 and abs(dCdb - delta["b"]) < 1e-12

    # verifica con differenze finite
    def C(x, y):
        return forward(GRAFO, ORD, {"a": x, "b": y})["C"]
    h = 1e-6
    num_a = (C(a + h, b) - C(a - h, b)) / (2 * h)
    num_b = (C(a, b + h) - C(a, b - h)) / (2 * h)
    print("differenze finite:", round(num_a, 4), round(num_b, 4))
    assert abs(num_a - delta["a"]) < 1e-5 and abs(num_b - delta["b"]) < 1e-5

    # contributi di b: due cammini, due contributi, una somma (p. 20)
    print("delta[b] = 1.7206 (via e) + 3.3041 (via c) =", round(delta["e"] * 1.0, 4), "+", round(delta["c"] * a, 4), "=", round(delta["e"] + delta["c"] * a, 4))

    # costo: V nodi, E archi (p. 24)
    V = len(GRAFO)
    E = sum(len(p) for p, _, _ in GRAFO.values())
    print(f"V = {V}, E = {E}: il forward legge {E} dipendenze e il backward elabora {E} archi")

    # una rete feedforward 3-4-3-1 a layer (p. 25): V e E
    layer = [3, 4, 3, 1]
    V2 = sum(layer)
    E2 = sum(layer[i] * layer[i + 1] for i in range(len(layer) - 1))
    print(f"rete {layer}: V = {V2}, E = {E2}")
