"""Alberi auto-aggiustanti, splay tree (lezione 12): Splay e le operazioni Splay-Tree-Search, Insert e Delete.

Traduzione dello pseudocodice delle slide (12 - Alberi auto-aggiustanti.pdf, pp. 3-8). Le slide descrivono Splay solo
con i tre casi di rotazioni (pp. 3-5): la funzione splay() qui sotto e' la loro traduzione in codice (mia).
Tree-Insert e Tree-Delete sono quelli della lezione 09 (Cormen, 2a ed.): vedi grafi_e_alberi.py.
"""


class Nodo:
    def __init__(self, key):
        self.key, self.left, self.right, self.p = key, None, None, None


class Splay:
    def __init__(self):
        self.root = None
        self.rotazioni = 0
        self.casi = []

    # --- rotazioni (lezione 11, senza sentinella: NIL = None)
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
        self.rotazioni += 1

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.p = y
        x.p = y.p
        if y.p is None:
            self.root = x
        elif y is y.p.left:
            y.p.left = x
        else:
            y.p.right = x
        x.right = y
        y.p = x
        self.rotazioni += 1

    def sali(self, x):
        """x sale sopra il padre con una rotazione sul padre."""
        if x is x.p.left:
            self.right_rotate(x.p)
        else:
            self.left_rotate(x.p)

    # --- Splay (pp. 3-5)
    def splay(self, x):
        while x.p is not None:
            y = x.p
            z = y.p
            if z is None:                                  # caso I: x e' figlio della radice
                self.casi.append("I")
                self.sali(x)
            elif (x is y.left) == (y is z.left):           # caso II: x e il padre sono entrambi figli sinistri (o destri)
                self.casi.append("II")
                self.sali(y)                               # rotazione sul nonno di x
                self.sali(x)                               # rotazione sul padre di x
            else:                                          # caso III: uno sinistro e l'altro destro
                self.casi.append("III")
                self.sali(x)                               # rotazione sul padre di x
                self.sali(x)                               # rotazione sul nuovo padre di x (era il nonno)

    # --- Tree-Insert / Tree-Delete / ricerca (BST della lezione 09)
    def tree_insert(self, z):
        y, x = None, self.root
        while x is not None:
            y = x
            x = x.left if z.key < x.key else x.right
        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def minimo(self, x):
        while x.left is not None:
            x = x.left
        return x

    def successore(self, x):
        if x.right is not None:
            return self.minimo(x.right)
        y = x.p
        while y is not None and x is y.right:
            x, y = y, y.p
        return y

    def tree_delete(self, z):
        y = z if z.left is None or z.right is None else self.successore(z)
        x = y.left if y.left is not None else y.right
        if x is not None:
            x.p = y.p
        if y.p is None:
            self.root = x
        elif y is y.p.left:
            y.p.left = x
        else:
            y.p.right = x
        if y is not z:
            z.key = y.key
        return y

    def search(self, k):
        """Splay-Tree-Search (T,k), p. 6."""
        x = self.root                                      # 1
        y = None
        while x is not None and x.key != k:                # 2
            y = x                                          # 3
            x = x.left if k < x.key else x.right           # 4-7
        if x is not None:                                  # 8
            self.splay(x)                                  # 9
        elif self.root is not None:                        # 10
            self.splay(y)                                  # 11
        return x                                           # 12

    def insert(self, z):
        """Splay-Tree-Insert (T,z), p. 7: Tree-Insert (z), poi Splay (T,z)."""
        self.tree_insert(z)
        self.splay(z)

    def delete(self, z):
        """Splay-Tree-Delete (T,z), p. 8: Tree-Delete (z); se p[z] != NIL, Splay (T,p[z])."""
        padre = z.p
        self.tree_delete(z)
        if padre is not None:
            self.splay(padre)

    # --- utilita'
    def inorder(self, x="r"):
        x = self.root if x == "r" else x
        return [] if x is None else self.inorder(x.left) + [x.key] + self.inorder(x.right)

    def forma(self, x="r"):
        x = self.root if x == "r" else x
        return None if x is None else (x.key, self.forma(x.left), self.forma(x.right))

    def trova(self, k):
        x = self.root
        while x is not None and x.key != k:
            x = x.left if k < x.key else x.right
        return x

    def altezza(self, x="r"):
        x = self.root if x == "r" else x
        return 0 if x is None else 1 + max(self.altezza(x.left), self.altezza(x.right))


def costruisci(chiavi):
    t = Splay()
    for k in chiavi:
        t.tree_insert(Nodo(k))
    return t


ALBERO_SLIDE = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13]       # albero di p. 6: 15; 6, 18; 3, 7, 17, 20; 2, 4, 13

if __name__ == "__main__":
    t = costruisci(ALBERO_SLIDE)
    print("albero di p. 6:", t.forma())
    # p. 11: cercare 17 lo porta in radice con un caso III (zig-zag)
    r = t.search(17)
    print("Splay(17): casi", t.casi, "rotazioni", t.rotazioni, "->", t.forma())
    assert t.casi == ["III"] and t.rotazioni == 2
    assert t.forma() == (17, (15, (6, (3, (2, None, None), (4, None, None)), (7, None, (13, None, None))), None), (18, None, (20, None, None)))
    assert t.inorder() == sorted(ALBERO_SLIDE)
    # cercare di nuovo 17: e' gia' la radice, 0 rotazioni (p. 11: O(1))
    t.rotazioni = 0
    t.search(17)
    print("seconda ricerca di 17: rotazioni =", t.rotazioni)
    assert t.rotazioni == 0
    # Splay(13) sull'albero risultante
    t.casi, t.rotazioni = [], 0
    t.search(13)
    print("Splay(13): casi", t.casi, "rotazioni", t.rotazioni, "->", t.forma())
    # ricerca di una chiave assente: si fa lo splay dell'ultimo nodo visitato (p. 6)
    t2 = costruisci(ALBERO_SLIDE)
    assert t2.search(19) is None
    print("ricerca di 19 (assente): radice dopo lo splay =", t2.root.key, "(ultimo nodo visitato: 20)")
    # p. 7: inserimento di 19
    t3 = costruisci(ALBERO_SLIDE)
    t3.insert(Nodo(19))
    print("Insert(19): radice", t3.root.key, "casi", t3.casi, "rotazioni", t3.rotazioni, "->", t3.forma())
    assert t3.root.key == 19 and t3.inorder() == sorted(ALBERO_SLIDE + [19])
    # p. 8: cancellazione (z = 3, due figli: si taglia il successore 4 e si fa lo splay del padre 6)
    t4 = costruisci(ALBERO_SLIDE)
    t4.delete(t4.trova(3))
    print("Delete(3): radice", t4.root.key, "casi", t4.casi, "rotazioni", t4.rotazioni, "->", t4.forma())
    assert t4.inorder() == sorted(set(ALBERO_SLIDE) - {3})
    # costo: accessi in ordine crescente a chiavi inserite in ordine (BST degenere, altezza n)
    n = 200
    t5 = Splay()
    for k in range(1, n + 1):
        t5.tree_insert(Nodo(k))
    print(f"BST degenere di {n} nodi: altezza", t5.altezza())
    t5.rotazioni = 0
    t5.search(n)
    print("  una ricerca di", n, "costa", t5.rotazioni, "rotazioni e l'altezza scende a", t5.altezza())
    t5.rotazioni = 0
    for k in range(1, n + 1):
        t5.search(k)
    print("  poi", n, "ricerche in ordine crescente: rotazioni totali", t5.rotazioni, "(circa", round(t5.rotazioni / n, 2), "per ricerca)")
    # working set (p. 13): A B C A A D A, un solo elemento distinto (D) prima dell'ultimo A
    t6 = costruisci([10, 5, 15, 3, 7, 12, 18])
    nomi = {"A": 7, "B": 3, "C": 18, "D": 12}
    t6.rotazioni = 0
    costi = []
    for a in "ABCAADA":
        prima = t6.rotazioni
        t6.search(nomi[a])
        costi.append((a, t6.rotazioni - prima))
    print("sequenza A B C A A D A (chiavi 7 3 18 7 7 12 7): rotazioni per accesso", costi)
    # vari invarianti: l'ordine delle chiavi resta identico
    import random
    random.seed(0)
    for _ in range(200):
        t7 = costruisci(random.sample(range(100), 30))
        base = t7.inorder()
        for _ in range(40):
            t7.search(random.randrange(100))
            assert t7.inorder() == base
    print("200 alberi casuali, 40 ricerche ciascuno: la visita in ordine non cambia mai")
