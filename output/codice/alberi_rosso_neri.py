"""Alberi rosso-neri (lezione 11): rotazioni, RB-Insert, RB-Insert-Fixup e cancellazione.

Traduzione dello pseudocodice delle slide (11 . Alberi rosso-neri.pdf, pp. 19, 22, 29-34). Come nelle slide ci
sono una sentinella unica NIL (nera) al posto dei puntatori a NIL e gli attributi color e p. La cancellazione
(RB-Delete con RB-Delete-Fixup) non ha pseudocodice nelle slide: e' qui solo per verificare, sugli alberi di
pp. 45-47, che le tre situazioni descritte a p. 44 lascino un albero rosso-nero (implementazione mia).
"""
import math
import random

RED, BLACK = "R", "B"


class Nodo:
    def __init__(self, key=None, color=BLACK):
        self.key, self.color = key, color
        self.left = self.right = self.p = None


class RBTree:
    def __init__(self):
        self.nil = Nodo(None, BLACK)                       # sentinella nil[T]
        self.nil.left = self.nil.right = self.nil.p = self.nil
        self.root = self.nil
        self.rotazioni = 0
        self.casi = []                                     # casi di RB-Insert-Fixup eseguiti: 1, 2, 3

    # ---------------------------------------------------------------- rotazioni (pp. 18-20)
    def left_rotate(self, x):
        y = x.right                                        # y <- right[x]
        x.right = y.left                                   # operazione 1: right[x] <- left[y]
        if y.left is not self.nil:
            y.left.p = x
        y.p = x.p                                          # operazione 2: p[y] <- p[x]
        if x.p is self.nil:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x                                         # operazione 3: left[y] <- x
        x.p = y
        self.rotazioni += 1

    def right_rotate(self, y):                             # simmetrica
        x = y.left
        y.left = x.right
        if x.right is not self.nil:
            x.right.p = y
        x.p = y.p
        if y.p is self.nil:
            self.root = x
        elif y is y.p.right:
            y.p.right = x
        else:
            y.p.left = x
        x.right = y
        y.p = x
        self.rotazioni += 1

    # ---------------------------------------------------------------- inserimento (pp. 21-41)
    def insert(self, key):
        z = Nodo(key, RED)
        y, x = self.nil, self.root                         # RB-Insert (p. 22)
        while x is not self.nil:
            y = x
            x = x.left if z.key < x.key else x.right
        z.p = y
        if y is self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = z.right = self.nil
        z.color = RED
        self.insert_fixup(z)
        return z

    def insert_fixup(self, z):                             # RB-Insert-Fixup (pp. 29-34)
        while z.p.color == RED:
            if z.p is z.p.p.left:
                y = z.p.p.right                            # zio
                if y.color == RED:                         # caso 1
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                    self.casi.append(1)
                else:
                    if z is z.p.right:                     # caso 2
                        z = z.p
                        self.left_rotate(z)
                        self.casi.append(2)
                    z.p.color = BLACK                      # caso 3
                    z.p.p.color = RED
                    self.right_rotate(z.p.p)
                    self.casi.append(3)
            else:                                          # stesso codice con left e right scambiati
                y = z.p.p.left
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                    self.casi.append(1)
                else:
                    if z is z.p.left:
                        z = z.p
                        self.right_rotate(z)
                        self.casi.append(2)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.left_rotate(z.p.p)
                    self.casi.append(3)
        self.root.color = BLACK

    # ---------------------------------------------------------------- cancellazione (pp. 42-48, versione mia)
    def minimum(self, x):
        while x.left is not self.nil:
            x = x.left
        return x

    def cerca(self, key):
        x = self.root
        while x is not self.nil and x.key != key:
            x = x.left if key < x.key else x.right
        return x

    def _trapianta(self, u, v):
        if u.p is self.nil:
            self.root = v
        elif u is u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def delete(self, z):
        """Come Tree-Delete: si toglie z (al piu' un figlio) oppure il suo successore y, copiandone la chiave in z."""
        y = z
        colore_y = y.color
        if z.left is self.nil:
            x = z.right
            self._trapianta(z, z.right)
        elif z.right is self.nil:
            x = z.left
            self._trapianta(z, z.left)
        else:
            y = self.minimum(z.right)                      # successore: al massimo un figlio
            colore_y = y.color
            x = y.right
            if y.p is z:
                x.p = y
            else:
                self._trapianta(y, y.right)
                y.right = z.right
                y.right.p = y
            self._trapianta(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if colore_y == BLACK:                              # nodo nero tolto: serve il fixup
            self.delete_fixup(x)
        return colore_y

    def delete_fixup(self, x):
        while x is not self.root and x.color == BLACK:
            if x is x.p.left:
                w = x.p.right
                if w.color == RED:
                    w.color = BLACK; x.p.color = RED
                    self.left_rotate(x.p); w = x.p.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED; x = x.p
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK; w.color = RED
                        self.right_rotate(w); w = x.p.right
                    w.color = x.p.color; x.p.color = BLACK; w.right.color = BLACK
                    self.left_rotate(x.p); x = self.root
            else:
                w = x.p.left
                if w.color == RED:
                    w.color = BLACK; x.p.color = RED
                    self.right_rotate(x.p); w = x.p.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED; x = x.p
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK; w.color = RED
                        self.left_rotate(w); w = x.p.left
                    w.color = x.p.color; x.p.color = BLACK; w.left.color = BLACK
                    self.right_rotate(x.p); x = self.root
        x.color = BLACK

    # ---------------------------------------------------------------- verifiche
    def altezza(self, x=None):
        x = self.root if x is None else x
        return 0 if x is self.nil else 1 + max(self.altezza(x.left), self.altezza(x.right))   # in nodi interni

    def n_interni(self, x=None):
        x = self.root if x is None else x
        return 0 if x is self.nil else 1 + self.n_interni(x.left) + self.n_interni(x.right)

    def verifica(self):
        """Controlla le proprieta' 1-5 e l'ordine BST; restituisce bh(radice) (nodi neri da un cammino, radice inclusa, NIL esclusa:
        uguale a bh della slide, che esclude la radice e include la foglia esterna)."""
        assert self.root.color == BLACK, "proprieta' 2"
        assert self.nil.color == BLACK, "proprieta' 3"

        def visita(x, lo, hi):
            if x is self.nil:
                return 0
            assert x.color in (RED, BLACK), "proprieta' 1"
            assert (lo is None or x.key >= lo) and (hi is None or x.key <= hi), "ordine BST"
            if x.color == RED:
                assert x.left.color == BLACK and x.right.color == BLACK, "proprieta' 4"
            a = visita(x.left, lo, x.key)
            b = visita(x.right, x.key, hi)
            assert a == b, "proprieta' 5"
            return a + (1 if x.color == BLACK else 0)
        return visita(self.root, None, None)

    def fotografia(self, x=None):
        """Albero come tupla (chiave, colore, sinistro, destro) per i confronti con le slide."""
        x = self.root if x is None else x
        if x is self.nil:
            return None
        return (x.key, x.color, self.fotografia(x.left), self.fotografia(x.right))


def costruisci(t, spec):
    """Costruisce un albero da una specifica annidata (chiave, colore, sinistro, destro) senza passare da insert."""
    def rec(s, padre):
        if s is None:
            return t.nil
        n = Nodo(s[0], s[1])
        n.p = padre
        n.left = rec(s[2], n)
        n.right = rec(s[3], n)
        return n
    t.root = rec(spec, t.nil)
    return t


# alberi delle slide ---------------------------------------------------------------------------------------
# p. 37: albero in cui si inserisce z = 4
P37 = (11, BLACK,
       (2, RED, (1, BLACK, None, None), (7, BLACK, (5, RED, None, None), (8, RED, None, None))),
       (14, BLACK, None, (15, RED, None, None)))
# p. 45-47: albero delle cancellazioni
P45 = (15, BLACK,
       (6, RED, (3, BLACK, (2, RED, None, None), (4, RED, None, None)), (7, BLACK, None, (13, RED, None, None))),
       (18, RED, (17, BLACK, None, None), (20, BLACK, (19, RED, None, None), None)))
# p. 20: albero delle rotazioni (i colori non contano: solo la struttura)
P20 = (7, BLACK, (4, BLACK, (3, BLACK, (2, BLACK, None, None), None), (6, BLACK, None, None)),
       (11, BLACK, (9, BLACK, None, None), (18, BLACK, (14, BLACK, (12, BLACK, None, None), (17, BLACK, None, None)),
                                            (19, BLACK, None, (22, BLACK, None, None)))))

if __name__ == "__main__":
    # 1. L'albero di p. 37 e' rosso-nero, bh = 2 (radice nera, due nodi neri su ogni cammino: 11 e 1/7/14)
    t = costruisci(RBTree(), P37)
    print("p. 37: n. interni", t.n_interni(), "altezza", t.altezza(), "bh(radice)", t.verifica())
    z = t.insert(4)
    print("inserimento di 4: casi di RB-Insert-Fixup", t.casi, "rotazioni", t.rotazioni)
    atteso = (7, BLACK, (2, RED, (1, BLACK, None, None), (5, BLACK, (4, RED, None, None), None)),
              (11, RED, (8, BLACK, None, None), (14, BLACK, None, (15, RED, None, None))))
    print("albero finale (p. 40):", t.fotografia())
    assert t.fotografia() == atteso and t.casi == [1, 2, 3] and t.rotazioni == 2
    print("  proprieta' 1-5 verificate, bh(radice) =", t.verifica())

    # 2. Rotazioni su p. 20: Left-Rotate (T, 11) e poi Right-Rotate (T, 18) riportano l'albero iniziale
    r = costruisci(RBTree(), P20)
    x = r.cerca(11)
    r.left_rotate(x)
    print("dopo Left-Rotate(T,11):", r.fotografia()[3][:2], "figli di 18:", r.cerca(18).left.key, r.cerca(18).right.key,
          "| figli di 11:", r.cerca(11).left.key, r.cerca(11).right.key, "| figli di 14:", r.cerca(14).left.key, r.cerca(14).right.key)
    assert (r.cerca(18).left.key, r.cerca(18).right.key) == (11, 19)
    assert (r.cerca(11).left.key, r.cerca(11).right.key) == (9, 14)
    r.right_rotate(r.cerca(18))
    assert r.fotografia() == costruisci(RBTree(), P20).fotografia()
    print("Right-Rotate(T,18) ripristina l'albero iniziale")

    # 3. Cancellazioni di p. 45-47
    for k, descr in ((19, "foglia rossa"), (20, "nero con un solo figlio (rosso)"), (18, "due figli")):
        d = costruisci(RBTree(), P45)
        d.verifica()
        z = d.cerca(k)
        colore = d.delete(z)
        print(f"Delete({k}) [{descr}]: colore del nodo tolto fisicamente = {colore}; albero ancora rosso-nero, bh =", d.verifica(),
              "| rotazioni:", d.rotazioni)
        if k == 18:
            print("   figli di 15 dopo l'eliminazione:", d.root.left.key, d.root.right.key, "-> nodo che ha preso il posto di 18:",
                  d.root.right.key, d.root.right.color)

    # 4. Altezza: n inserimenti ordinati (caso peggiore di un BST) e casuali
    for n in (7, 31, 127, 1023, 10000):
        t = RBTree()
        for k in range(1, n + 1):
            t.insert(k)
        bh = t.verifica()
        h = t.altezza()
        print(f"n = {n:>5}: altezza {h:>3} <= 2 lg(n+1) = {2 * math.log2(n + 1):6.2f}  | bh = {bh:>2}, 2^bh - 1 = {2 ** bh - 1} <= n  | rotazioni {t.rotazioni}")
        assert h <= 2 * math.log2(n + 1) and 2 ** bh - 1 <= n
    random.seed(1)
    for _ in range(200):
        t = RBTree()
        chiavi = random.sample(range(1000), 60)
        for k in chiavi:
            t.insert(k)
            t.verifica()
        assert t.rotazioni <= 2 * len(chiavi)
        for k in random.sample(chiavi, 30):
            t.delete(t.cerca(k))
            t.verifica()
    print("200 sequenze casuali di inserimenti e cancellazioni: proprieta' 1-5 sempre valide, al piu' 2 rotazioni per inserimento")
