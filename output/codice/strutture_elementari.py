"""Verifica di 04-Strutture dati elementari.pdf.

- pp.10-11: array dinamico che raddoppia -> numero di raddoppi = ceil(lg n), spostamenti totali <= 2n
- p.26 (Figura 10.1 del Cormen): pila su array S[1..7] con S.top
- p.27 (Figura 10.2 del Cormen): coda circolare su array Q[1..12] con Q.head, Q.tail

Gli array sono indicizzati da 1 come nello pseudocodice del corso: la cella 0 non è usata.
"""
import math


# ------------------------------------------------------------------ array dinamico
def array_dinamico(n):
    """Inserisce n elementi partendo da capacità 1 e raddoppiando quando è pieno.
    Restituisce (numero di raddoppi, numero totale di elementi ricopiati)."""
    capacita, dimensione, raddoppi, copie = 1, 0, 0, 0
    for _ in range(n):
        if dimensione == capacita:
            copie += dimensione          # ricopio tutti gli elementi nel nuovo array di 2m celle
            capacita *= 2
            raddoppi += 1
        dimensione += 1
    return raddoppi, copie


# ------------------------------------------------------------------ pila (p.26)
class Pila:
    def __init__(self, contenuto, capacita):
        self.S = [None] + list(contenuto) + [None] * (capacita - len(contenuto))
        self.top = len(contenuto)

    def push(self, x):
        self.top += 1
        self.S[self.top] = x

    def pop(self):
        self.top -= 1
        return self.S[self.top + 1]      # l'elemento resta nell'array ma non è più nella pila

    def __str__(self):
        return f"S[1..top] = {self.S[1:self.top + 1]}, S.top = {self.top}"


# ------------------------------------------------------------------ coda (p.27)
class Coda:
    """Coda circolare: head = primo elemento, tail = prima cella libera (convenzione del Cormen)."""

    def __init__(self, n, head, elementi):
        self.n, self.Q = n, [None] * (n + 1)
        self.head = self.tail = head
        for x in elementi:
            self.enqueue(x)

    def enqueue(self, x):
        self.Q[self.tail] = x
        self.tail = 1 if self.tail == self.n else self.tail + 1

    def dequeue(self):
        x = self.Q[self.head]
        self.head = 1 if self.head == self.n else self.head + 1
        return x

    def contenuto(self):
        out, i = [], self.head
        while i != self.tail:
            out.append(self.Q[i])
            i = 1 if i == self.n else i + 1
        return out

    def __str__(self):
        return f"coda = {self.contenuto()}, Q.head = {self.head}, Q.tail = {self.tail}"


if __name__ == "__main__":
    print("== Array dinamico (pp.10-11) ==")
    print("      n | raddoppi | ceil(lg n) | copie | 2n")
    for n in [1, 2, 3, 4, 5, 8, 9, 1000, 1024, 1025, 10**6]:
        r, c = array_dinamico(n)
        print(f"{n:>7} | {r:>8} | {math.ceil(math.log2(n)):>10} | {c:>5} | {2*n}")

    print("\n== Pila su array (p.26) ==")
    s = Pila([15, 6, 2, 9], 7); print("(a)", s)
    s.push(17); s.push(3); print("(b) dopo PUSH(S,17), PUSH(S,3):", s)
    x = s.pop(); print(f"(c) POP(S) restituisce {x}:", s, "| cella S[6] contiene ancora", s.S[6])

    print("\n== Coda su array (p.27) ==")
    q = Coda(12, 7, [15, 6, 9, 8, 4]); print("(a)", q)
    for x in (17, 3, 5):
        q.enqueue(x)
    print("(b) dopo ENQUEUE 17, 3, 5:", q)
    x = q.dequeue(); print(f"(c) DEQUEUE restituisce {x}:", q)
