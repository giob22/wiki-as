"""Backtracking (lezione 15): schema generale, sottoinsiemi e permutazioni.

Traduzione del codice C delle slide (15 - Backtracking.pdf, pp. 7, 9-12, 14-18, 20-24). Il vettore a e' indicizzato da 1,
come nelle slide: a[0] non si usa. Le funzioni hanno gli stessi nomi del C (is_a_solution, construct_candidates,
make_move, unmake_move, process_solution).
"""
import math

TRUE, FALSE = True, False


class Problema:
    """Le routine che specializzano lo schema generale per ciascuna applicazione."""
    def is_a_solution(self, a, k, n): raise NotImplementedError
    def construct_candidates(self, a, k, n): raise NotImplementedError
    def process_solution(self, a, k, n, out): out.append(tuple(a[1:k + 1]))
    def make_move(self, a, k, n): pass
    def unmake_move(self, a, k, n): pass


class Sottoinsiemi(Problema):
    """p. 14-18: S_k = (true, false); a e' una soluzione quando k = n."""
    def is_a_solution(self, a, k, n):
        return k == n
    def construct_candidates(self, a, k, n):
        return [TRUE, FALSE]


class Permutazioni(Problema):
    """p. 20-24: S_k = {1..n} - a; a e' una soluzione quando k = n."""
    def is_a_solution(self, a, k, n):
        return k == n
    def construct_candidates(self, a, k, n):
        in_perm = [False] * (n + 1)
        for i in range(1, k):
            in_perm[a[i]] = True
        return [i for i in range(1, n + 1) if not in_perm[i]]


class Esecuzione:
    def __init__(self):
        self.soluzioni, self.stati, self.chiamate = [], [], 0
        self.finished = False


def backtrack(a, k, n, pb, es):
    """void backtrack(int a[], int k, data input), p. 9."""
    es.chiamate += 1
    es.stati.append(tuple(a[1:k + 1]))                  # stato visitato: il vettore parziale (a1..ak)
    if pb.is_a_solution(a, k, n):                       # if (is_a_solution(a, k, input))
        pb.process_solution(a, k, n, es.soluzioni)      #     process_solution(a, k, input);
    else:
        k = k + 1                                       # k = k + 1;
        c = pb.construct_candidates(a, k, n)            # construct_candidates(a, k, input, c, &nc);
        for ci in c:                                    # for (i = 0; i < nc; i++)
            a[k] = ci                                   #     a[k] = c[i];
            pb.make_move(a, k, n)                       #     make_move(a, k, input);
            backtrack(a, k, n, pb, es)                  #     backtrack(a, k, input);
            pb.unmake_move(a, k, n)                     #     unmake_move(a, k, input);
            es.stati.append(tuple(a[1:k]))              # ritorno al vettore parziale (a1..a_{k-1})
            if es.finished:                             #     if (finished) return;
                return


def esegui(pb, n):
    es = Esecuzione()
    backtrack([None] * (n + 2), 0, n, pb, es)
    return es


def nome(v):
    return "−" if v is False else str(v)


def fmt(stato):
    return "(" + ",".join(nome(x) for x in stato) + ")"


def fmt_sub(stato):
    """Come nelle slide (p. 15): l'elemento i incluso si scrive i, escluso si scrive un trattino."""
    return "(" + ",".join(str(i + 1) if v is True else "−" for i, v in enumerate(stato)) + ")"


def insieme(sol):
    return "{" + ",".join(str(i + 1) for i, v in enumerate(sol) if v is True) + "}"


if __name__ == "__main__":
    n = 3
    es = esegui(Sottoinsiemi(), n)
    print("sottoinsiemi di {1,2,3}: soluzioni", [insieme(s) for s in es.soluzioni])
    assert [insieme(s) for s in es.soluzioni] == ["{1,2,3}", "{1,2}", "{1,3}", "{1}", "{2,3}", "{2}", "{3}", "{}"]   # foglie di p. 15
    print("  ordine degli stati:", " -> ".join(fmt_sub(s) if s else "()" for s in es.stati))
    print("  chiamate di backtrack:", es.chiamate, "= 2^(n+1) - 1 =", 2 ** (n + 1) - 1)
    assert es.chiamate == 2 ** (n + 1) - 1

    # sequenza della slide p. 15 (con le tre omissioni delle risalite)
    slide = ["(1)", "(1,2)", "(1,2,3)", "(1,2,−)", "(1,−)", "(1,−,3)", "(1,−,−)", "(1,−)", "(1)", "(−)", "(−,2)", "(−,2,3)", "(−,2,−)",
             "(−,−)", "(−,−,3)", "(−,−,−)", "(−,−)", "(−)", "()"]
    mio = [fmt_sub(s) if s else "()" for s in es.stati]
    it = iter(mio)
    assert all(x in it for x in slide), "la sequenza della slide dovrebbe essere una sottosequenza di quella eseguita"
    print("  la sequenza di p. 15 e' una sottosequenza di quella eseguita (la slide omette alcune risalite)")

    es = esegui(Permutazioni(), n)
    print("permutazioni di {1,2,3}:", ["".join(map(str, s)) for s in es.soluzioni])
    assert ["".join(map(str, s)) for s in es.soluzioni] == ["123", "132", "213", "231", "312", "321"]
    print("  ordine degli stati:", " -> ".join(fmt(s) if s else "()" for s in es.stati))
    assert es.chiamate == 16
    slide = ["(1)", "(1,2)", "(1,2,3)", "(1,2)", "(1)", "(1,3)", "(1,3,2)", "(1,3)", "(1)", "()", "(2)", "(2,1)", "(2,1,3)", "(2,1)", "(2)", "(2,3)",
             "(2,3,1)", "(2,3)", "(2)", "()", "(3)", "(3,1)", "(3,1,2)", "(3,1)", "(3)", "(3,2)", "(3,2,1)", "(3,2)", "(3)", "()"]
    mio = [fmt(s) if s else "()" for s in es.stati]
    it = iter(mio)
    assert all(x in it for x in slide)
    print("  chiamate di backtrack:", es.chiamate, "(1 + 3 + 6 + 6)")

    # conteggi: nodi dell'albero delle chiamate
    for n in range(1, 9):
        e1, e2 = esegui(Sottoinsiemi(), n), esegui(Permutazioni(), n)
        nodi_perm = sum(math.factorial(n) // math.factorial(n - k) for k in range(n + 1))
        assert e1.chiamate == 2 ** (n + 1) - 1 and len(e1.soluzioni) == 2 ** n
        assert e2.chiamate == nodi_perm and len(e2.soluzioni) == math.factorial(n)
        print(f"n = {n}: sottoinsiemi {len(e1.soluzioni):>4} (chiamate {e1.chiamate:>4}) | permutazioni {len(e2.soluzioni):>6} (chiamate {e2.chiamate:>6}, e*n! = {math.e * math.factorial(n):9.1f})")

    # uscita anticipata con finished (p. 9)
    class Primo(Permutazioni):
        def process_solution(self, a, k, n, out):
            out.append(tuple(a[1:k + 1]))
    es = Esecuzione()
    pb = Primo()

    class Fermati(Primo):
        def process_solution(self, a, k, n, out):
            super().process_solution(a, k, n, out)
            es.finished = True
    backtrack([None] * 6, 0, 4, Fermati(), es)
    print("con finished = true alla prima soluzione:", es.soluzioni, "dopo", es.chiamate, "chiamate")
