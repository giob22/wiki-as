"""Animazioni (🧩) degli algoritmi del wiki di Algoritmi e Strutture Dati.

Ogni animazione e' un SVG a fotogrammi (animazione SMIL, riprodotta da Obsidian quando il file
e' incorporato con ![[...]]). I fotogrammi NON sono disegnati a mano: ogni algoritmo viene
eseguito davvero sull'istanza delle slide e ogni passo produce un fotogramma, con la riga di
pseudocodice corrente evidenziata. Se un visualizzatore non supporta l'animazione, si vede
l'ultimo fotogramma (lo stato finale).

Solo libreria standard. Esecuzione (da questa cartella):
    python genera_animazioni.py
"""
import itertools
import math
from xml.sax.saxutils import escape

# ------------------------------------------------------------------ colori (tema chiaro Solarized)
SFONDO = "#fdf6e3"
TESTO = "#073642"
GRIGIO = "#93a1a1"
BLU = "#268bd2"
ROSSO = "#dc322f"
VERDE = "#859900"
GIALLO = "#b58900"
VIOLA = "#6c71c4"
CIANO = "#2aa198"
ARANCIO = "#cb4b16"
EVID = "#fce9a8"          # evidenziazione riga di pseudocodice
ORDINATO = "#d7ecc2"      # parte gia' sistemata (invariante)


def t(x, y, s, size=15, col=TESTO, anchor="start", bold=False, mono=False):
    fam = "monospace" if mono else "sans-serif"
    w = ' font-weight="bold"' if bold else ""
    testo = escape(str(s)).replace(" ", " ") if mono else escape(str(s))   # spazi non comprimibili
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{col}" font-family="{fam}"'
            f' text-anchor="{anchor}"{w}>{testo}</text>')


def rect(x, y, w, h, fill="none", stroke=TESTO, sw=1.5, rx=4, extra=""):
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}"'
            f' stroke="{stroke}" stroke-width="{sw}"{extra}/>')


def line(x1, y1, x2, y2, col=TESTO, sw=2, dash=None, arrow=False):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    out = f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{sw}"{d}/>'
    if arrow:                                   # punta disegnata come triangolo (i marker non sono supportati ovunque)
        ang = math.atan2(y2 - y1, x2 - x1)
        a1, a2 = ang + math.radians(150), ang - math.radians(150)
        pts = [(x2, y2), (x2 + 9 * math.cos(a1), y2 + 9 * math.sin(a1)), (x2 + 9 * math.cos(a2), y2 + 9 * math.sin(a2))]
        out += '<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f'" fill="{col}"/>'
    return out


def circle(x, y, r, fill=TESTO, stroke="none", sw=1):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def freccia_su(x, y, label, col=BLU):
    """Puntatore sotto una cella: freccia verso l'alto con etichetta."""
    return (line(x, y + 26, x, y + 4, col=col, sw=2, arrow=True) + t(x, y + 42, label, 14, col, "middle", True))


class Animazione:
    def __init__(self, titolo, W=760, H=400, durata=1.1):
        self.titolo, self.W, self.H, self.durata = titolo, W, H, durata
        self.frames = []

    def frame(self, contenuto, didascalia, durata=None):
        self.frames.append((contenuto, didascalia, durata or self.durata))

    def pseudocodice(self, righe, attive, x, y, larghezza=330, passo=21):
        """Pannello di pseudocodice; `attive` = insieme dei numeri di riga da evidenziare."""
        out = [rect(x - 8, y - 18, larghezza, passo * len(righe) + 14, fill="#ffffff", stroke=GRIGIO, sw=1)]
        for k, (num, testo) in enumerate(righe):
            yy = y + k * passo
            if num in attive:
                out.append(rect(x - 6, yy - 15, larghezza - 4, passo, fill=EVID, stroke="none", rx=2))
            out.append(t(x, yy, f"{num:>2}  {testo}" if num else f"    {testo}", 13, TESTO, mono=True))
        return "".join(out)

    def salva(self, nome_file):
        T = sum(d for _, _, d in self.frames) + 2.0          # pausa finale sull'ultimo fotogramma
        parti, inizio = [], 0.0
        n = len(self.frames)
        for k, (contenuto, didascalia, d) in enumerate(self.frames):
            a, b = inizio / T, (inizio + d) / T
            if k == n - 1:
                b = 1.0
            if k == 0:
                valori, tempi = "1;0", f"0;{b:.5f}"
            elif k == n - 1:
                valori, tempi = "0;1", f"0;{a:.5f}"
            else:
                valori, tempi = "0;1;0", f"0;{a:.5f};{b:.5f}"
            opac = "1" if k == n - 1 else "0"                  # senza SMIL resta visibile lo stato finale
            barra = (rect(20, self.H - 14, (self.W - 40) * (k + 1) / n, 5, fill=BLU, stroke="none", rx=2))
            cap = (t(20, self.H - 26, f"Passo {k + 1}/{n} — {didascalia}", 14, TESTO))
            parti.append(f'<g opacity="{opac}"><animate attributeName="opacity" values="{valori}" '
                         f'keyTimes="{tempi}" dur="{T:.2f}s" calcMode="discrete" repeatCount="indefinite"/>'
                         f'{contenuto}{cap}{barra}</g>')
            inizio += d
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.W}" height="{self.H}" '
               f'viewBox="0 0 {self.W} {self.H}">'
               '<defs><marker id="freccia" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" '
               'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/>'
               '</marker></defs>'
               f'{rect(0, 0, self.W, self.H, fill=SFONDO, stroke="none", rx=0)}'
               f'{t(self.W / 2, 26, self.titolo, 17, TESTO, "middle", True)}'
               + "".join(parti) + "</svg>")
        with open(nome_file, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"scritto {nome_file} ({n} fotogrammi, {T:.0f} s)")


def array(A, x0, y0, cw=52, ch=46, colori=None, indici=True, base=1, testi_col=None):
    """Disegna A come fila di celle; colori/testi_col: dizionari indice -> colore."""
    colori, testi_col = colori or {}, testi_col or {}
    out = []
    for k, v in enumerate(A):
        idx = k + base
        x = x0 + k * cw
        out.append(rect(x, y0, cw, ch, fill=colori.get(idx, "#ffffff"), stroke=TESTO, sw=1.5, rx=0))
        out.append(t(x + cw / 2, y0 + ch / 2 + 7, "" if v is None else v, 22, testi_col.get(idx, TESTO), "middle", True))
        if indici:
            out.append(t(x + cw / 2, y0 - 8, idx, 12, GRIGIO, "middle"))
    return "".join(out)


# =================================================================== ORDINAMENTO
def insertion_sort():
    PSEUDO = [(1, "for j ← 2 to length[A]"), (2, "    do key ← A[j]"),
              (3, "       // Insert A[j] into A[1..j-1]"), (4, "       i ← j-1"),
              (5, "       while i>0 and A[i]>key"), (6, "           do A[i+1] ← A[i]"),
              (7, "              i ← i-1"), (8, "       A[i+1] ← key")]
    an = Animazione("Insertion sort su ⟨5, 2, 4, 6, 1, 3⟩ (slide 05 pp. 5–15)", 800, 400, 1.0)
    A = [5, 2, 4, 6, 1, 3]
    n = len(A)
    X0, Y0 = 40, 110

    def scena(righe, j=None, i=None, key=None, conf=None, ordinati=0, nota=""):
        col = {k: ORDINATO for k in range(1, ordinati + 1)}
        tcol = {}
        if conf:
            col[conf[0]] = "#fbd0cc" if conf[1] else "#d9ecf7"
        s = array(A, X0, Y0, colori=col, testi_col=tcol)
        s += t(X0, Y0 - 38, "A", 16, TESTO, bold=True)
        s += rect(X0, Y0 + 125, 60, 46, fill="#ffffff", stroke=ROSSO, sw=2, rx=0)
        s += t(X0 + 30, Y0 + 155, "" if key is None else key, 22, ROSSO, "middle", True)
        s += t(X0, Y0 + 117, "key", 14, ROSSO, bold=True)
        if j is not None and j <= n:
            s += freccia_su(X0 + (j - 1) * 52 + 26, Y0 + 48, "j", ROSSO)
        if i is not None and i >= 1:
            s += freccia_su(X0 + (i - 1) * 52 + 20, Y0 + 48, "i", BLU)
        elif i == 0:
            s += t(X0 - 4, Y0 + 90, "i = 0", 14, BLU, "end", True)
        if ordinati:
            s += t(X0, Y0 + 205, f"invariante: A[1..{ordinati}] ordinato", 14, VERDE, bold=True)
        if nota:
            s += t(X0 + 80, Y0 + 155, nota, 14, TESTO)
        s += an.pseudocodice(PSEUDO, righe, 400, 95)
        return s

    an.frame(scena(set()), "stato iniziale")
    for j in range(2, n + 1):
        an.frame(scena({1}, j=j, ordinati=j - 1), f"j = {j}: all'inizio A[1..{j - 1}] è ordinato (invariante)")
        key = A[j - 1]
        an.frame(scena({2}, j=j, key=key, ordinati=j - 1), f"key ← A[{j}] = {key}")
        i = j - 1
        an.frame(scena({4}, j=j, i=i, key=key, ordinati=j - 1), f"i ← j−1 = {i}")
        while True:
            if i > 0:
                vero = A[i - 1] > key
                an.frame(scena({5}, j=j, i=i, key=key, conf=(i, vero), ordinati=j - 1),
                         f"test: A[{i}] = {A[i - 1]} > key = {key}? {'sì → sposto' if vero else 'no → esco dal while'}")
            else:
                vero = False
                an.frame(scena({5}, j=j, i=0, key=key, ordinati=j - 1), "test: i = 0 → esco dal while")
            if not vero:
                break
            A[i] = A[i - 1]
            i -= 1
            an.frame(scena({6, 7}, j=j, i=i, key=key, ordinati=j - 1),
                     f"A[{i + 2}] ← A[{i + 1}] (il valore scorre a destra), i ← {i}")
        A[i] = key
        an.frame(scena({8}, j=j, i=i if i >= 1 else None, ordinati=j), f"A[{i + 1}] ← key = {key}: ora A[1..{j}] è ordinato")
    an.frame(scena(set(), ordinati=n), "j = 7 > n: il for termina, A[1..6] = ⟨1, 2, 3, 4, 5, 6⟩ ordinato", 2.0)
    an.salva("animazione-insertion-sort.svg")


def selection_sort():
    PSEUDO = [(1, "n ← length[A]"), (2, "for i ← 1 to n − 1"), (3, "    min ← i"),
              (4, "    for j ← i + 1 to n"), (5, "        if A[j] < A[min]"), (6, "            min ← j"),
              (7, "    scambia A[i] con A[min]")]
    an = Animazione("Selection sort su ⟨5, 2, 4, 6, 1, 3⟩ (esercizio 2.2.2, slide 05 pp. 24–29)", 800, 400, 0.9)
    A = [5, 2, 4, 6, 1, 3]
    n = len(A)
    X0, Y0 = 40, 110
    confronti = 0

    def scena(righe, i=None, j=None, m=None, fissati=0, evid=None):
        col = {k: ORDINATO for k in range(1, fissati + 1)}
        if evid:
            for k, c in evid.items():
                col[k] = c
        s = array(A, X0, Y0, colori=col) + t(X0, Y0 - 38, "A", 16, TESTO, bold=True)
        if i:
            s += freccia_su(X0 + (i - 1) * 52 + 14, Y0 + 48, "i", ROSSO)
        if m:
            s += freccia_su(X0 + (m - 1) * 52 + 38, Y0 + 48, "min", VIOLA)
        if j:
            s += freccia_su(X0 + (j - 1) * 52 + 26, Y0 + 100, "j", BLU)
        s += t(X0, Y0 + 205, f"confronti eseguiti: {confronti}", 14, TESTO)
        if fissati:
            s += t(X0, Y0 + 228, f"invariante: A[1..{fissati}] = i {fissati} più piccoli, ordinati", 14, VERDE, bold=True)
        s += an.pseudocodice(PSEUDO, righe, 420, 95, 350)
        return s

    an.frame(scena(set()), "stato iniziale")
    for i in range(1, n):
        m = i
        an.frame(scena({2, 3}, i=i, m=m, fissati=i - 1), f"i = {i}: cerco il minimo di A[{i}..{n}], parto da min = {i}")
        for j in range(i + 1, n + 1):
            confronti += 1
            minore = A[j - 1] < A[m - 1]
            an.frame(scena({4, 5}, i=i, j=j, m=m, fissati=i - 1, evid={j: "#d9ecf7", m: "#eadcf5"}),
                     f"A[{j}] = {A[j - 1]} < A[min] = {A[m - 1]}? {'sì' if minore else 'no'}")
            if minore:
                m = j
                an.frame(scena({6}, i=i, j=j, m=m, fissati=i - 1, evid={m: "#eadcf5"}), f"min ← {j}")
        A[i - 1], A[m - 1] = A[m - 1], A[i - 1]
        an.frame(scena({7}, i=i, m=m, fissati=i, evid={i: ORDINATO}),
                 f"scambio A[{i}] e A[{m}]: il minimo {A[i - 1]} va in posizione {i}" if m != i
                 else f"il minimo è già in posizione {i}: scambio con sé stesso")
    an.frame(scena(set(), fissati=n), f"fatto dopo n−1 = 5 iterazioni: {confronti} = n(n−1)/2 confronti", 2.0)
    an.salva("animazione-selection-sort.svg")


# =================================================================== PATTERN MATCHING
def findmatch():
    PSEUDO = [(5, "for (i=0; i<=(n-m); i=i+1) {"), (6, "    j=0;"),
              (7, "    while ((j<m) && (t[i+j]==p[j]))"), (8, "        j = j+1;"),
              (9, "    if (j == m) return(i);"), (10, "}"), (11, "return(-1);")]
    an = Animazione("findmatch: cercare p = abba in t = aababba (slide 05 pp. 30–31)", 800, 400, 1.0)
    T_, P = "aababba", "abba"
    n, m = len(T_), len(P)
    X0, Y0 = 40, 90
    cw = 46
    confronti = 0

    def scena(righe, i, j=None, esito=None, trovato=False):
        s = t(X0 - 10, Y0 + 30, "t", 16, TESTO, "end", True)
        s += array(list(T_), X0, Y0, cw=cw, base=0)
        s += t(X0 - 10, Y0 + 110, "p", 16, TESTO, "end", True)
        col = {}
        for k in range(m):
            if j is not None and k < j:
                col[k] = ORDINATO
        if esito is not None:
            col[j] = ORDINATO if esito else "#fbd0cc"
        if trovato:
            col = {k: ORDINATO for k in range(m)}
        s += array(list(P), X0 + i * cw, Y0 + 80, cw=cw, base=0, indici=False, colori=col)
        s += t(X0 + i * cw, Y0 + 150, f"i = {i}", 14, BLU, bold=True)
        s += t(X0, Y0 + 215, f"confronti di caratteri: {confronti}", 14, TESTO)
        s += an.pseudocodice(PSEUDO, righe, 420, 80, 360)
        return s

    for i in range(0, n - m + 1):
        an.frame(scena({5, 6}, i), f"i = {i}: allineo p sotto t[{i}..{i + m - 1}], j ← 0")
        j = 0
        while j < m:
            confronti += 1
            uguale = T_[i + j] == P[j]
            an.frame(scena({7}, i, j, uguale), f"t[{i + j}] = {T_[i + j]} == p[{j}] = {P[j]}? {'sì' if uguale else 'no → tentativo fallito'}")
            if not uguale:
                break
            j += 1
            if j < m:
                an.frame(scena({8}, i, j), f"j ← {j}")
        if j == m:
            an.frame(scena({9}, i, trovato=True), f"j == m = 4: trovato, return({i}) — {confronti} confronti in tutto", 2.0)
            break
    an.salva("animazione-findmatch.svg")


# =================================================================== LOGARITMI
def potenza_veloce():
    PSEUDO = [(1, "if (n = 0) return(1)"), (2, "x = power(a, ⌊n/2⌋)"),
              (3, "if (n is even) then return(x²)"), (4, "    else return(a * x²)")]
    an = Animazione("power(a, n): calcolo di 2¹³ (slide 05 p. 32)", 800, 400, 1.2)
    a, N = 2, 13
    chiamate = []
    n = N
    while True:
        chiamate.append(n)
        if n == 0:
            break
        n //= 2
    X0, Y0, h = 40, 60, 46
    risultati = {}
    molt = [0]

    def scena(righe, attiva, nota):
        s = ""
        for k, nn in enumerate(chiamate):
            y = Y0 + k * (h + 6)
            if k > len(chiamate) - 1:
                continue
            aperta = nn in risultati or k <= chiamate.index(attiva)
            if not aperta:
                continue
            col = EVID if nn == attiva else "#ffffff"
            s += rect(X0 + k * 18, y, 300, h, fill=col, stroke=BLU, sw=1.5)
            s += t(X0 + k * 18 + 12, y + 29, f"power({a}, {nn})", 16, TESTO, mono=True)
            if nn in risultati:
                s += t(X0 + k * 18 + 290, y + 29, f"= {risultati[nn]}", 16, VERDE, "end", True)
        s += t(X0, 336, f"moltiplicazioni finora: {molt[0]}", 14, TESTO)
        s += t(X0 + 330, 336, nota, 14, TESTO)
        s += an.pseudocodice(PSEUDO, righe, 430, 90, 330)
        s += t(430, 205, "pila delle chiamate: n si dimezza a ogni livello", 13, GRIGIO)
        s += t(430, 225, f"13 → 6 → 3 → 1 → 0: {len(chiamate)} chiamate = ⌊lg 13⌋ + 2", 13, GRIGIO)
        return s

    for nn in chiamate:
        if nn == 0:
            an.frame(scena({1}, nn, ""), "power(2, 0): caso base, restituisce 1")
        else:
            an.frame(scena({2}, nn, ""), f"power(2, {nn}): chiamo power(2, ⌊{nn}/2⌋) = power(2, {nn // 2})")
    risultati[0] = 1
    an.frame(scena({1}, 0, ""), "power(2, 0) = 1 torna al chiamante")
    for nn in reversed(chiamate[:-1]):
        x = risultati[nn // 2]
        if nn % 2 == 0:
            molt[0] += 1
            risultati[nn] = x * x
            an.frame(scena({3}, nn, f"x = {x}, n pari"), f"n = {nn} pari: x² = {x}² = {x * x}")
        else:
            molt[0] += 2
            risultati[nn] = a * x * x
            an.frame(scena({4}, nn, f"x = {x}, n dispari"), f"n = {nn} dispari: a·x² = 2·{x}² = {a * x * x}")
    an.frame(scena(set(), N, "8192 = 2¹³"), f"risultato 8192 con {molt[0]} moltiplicazioni (invece di 12)", 2.0)
    an.salva("animazione-potenza-veloce.svg")


# =================================================================== SOMMA 1..n
def somma_iterativa():
    PSEUDO = [(1, "s ← 0"), (2, "per i da 1 a n"), (3, "    s ← s + i"), (4, "ritorna s")]
    an = Animazione("somma_iterativa(4): 1 + 2 + 3 + 4 (slide 03 pp. 11, 17, 23–28)", 800, 360, 1.1)
    n = 4
    passi = [0]

    def scena(righe, i, s, nota=""):
        out = t(60, 90, "n = 4", 18, TESTO, bold=True, mono=True)
        out += rect(60, 110, 110, 50, fill="#ffffff", stroke=BLU, sw=2) + t(70, 142, f"i = {i if i is not None else '–'}", 18, BLU, bold=True, mono=True)
        out += rect(190, 110, 110, 50, fill="#ffffff", stroke=ROSSO, sw=2) + t(200, 142, f"s = {s if s is not None else '–'}", 18, ROSSO, bold=True, mono=True)
        if i is not None and i <= n + 1 and s is not None:
            somma = " + ".join(str(k) for k in range(1, i)) or "somma vuota"
            out += t(60, 200, f"invariante all'inizio dell'iterazione i: s = Σ_(k=1..i−1) k", 14, VERDE, bold=True)
            out += t(60, 222, f"   i = {i}: s = {somma} = {sum(range(1, i))}", 14, VERDE)
        out += t(60, 262, f"passi contati finora: {passi[0]}   (totale atteso 2n + 4 = 12)", 14, TESTO)
        out += an.pseudocodice(PSEUDO, righe, 470, 110, 260)
        return out

    passi[0] += 1
    an.frame(scena({1}, None, 0), "s ← 0 (1 passo)")
    passi[0] += 1
    s = 0
    for i in range(1, n + 2):
        passi[0] += 1
        if i > n:
            an.frame(scena({2}, i, s), f"test i ≤ n con i = {i}: falso, esco dal ciclo")
            break
        an.frame(scena({2}, i, s), f"test i ≤ n con i = {i}: vero")
        s += i
        passi[0] += 1
        an.frame(scena({3}, i, s), f"s ← s + {i} = {s}")
    passi[0] += 1
    an.frame(scena({4}, n + 1, s, ""), f"ritorna s = {s}; passi totali = {passi[0]} = 2·4 + 4", 2.0)
    an.salva("animazione-somma-iterativa.svg")


def somma_ricorsiva():
    PSEUDO = [(1, "se n = 0"), (2, "    ritorna 0"), (3, "altrimenti"), (4, "    ritorna n + somma_ricorsiva(n − 1)")]
    an = Animazione("somma_ricorsiva(3): la pila delle chiamate (slide 03 pp. 11, 19, 30–33)", 800, 380, 1.2)
    risultati = {}
    X0, Y0, h = 40, 70, 48

    def scena(righe, aperte, attiva):
        s = ""
        for k, nn in enumerate(aperte):
            y = Y0 + k * (h + 8)
            col = EVID if nn == attiva else "#ffffff"
            s += rect(X0 + k * 20, y, 330, h, fill=col, stroke=BLU, sw=1.5)
            s += t(X0 + k * 20 + 12, y + 30, f"somma_ricorsiva({nn})", 16, TESTO, mono=True)
            if nn in risultati:
                s += t(X0 + k * 20 + 320, y + 30, f"= {risultati[nn]}", 16, VERDE, "end", True)
        s += t(X0, 330, f"record di attivazione sulla pila: {len(aperte)}", 14, TESTO)
        s += an.pseudocodice(PSEUDO, righe, 420, 100, 370)
        s += t(420, 215, "correttezza per induzione: S(n) = n + S(n−1)", 13, GRIGIO)
        s += t(420, 235, "costo T(n) = T(n−1) + c, spazio Θ(n)", 13, GRIGIO)
        return s

    ordine = [3, 2, 1, 0]
    for k, nn in enumerate(ordine):
        aperte = ordine[:k + 1]
        if nn == 0:
            an.frame(scena({1, 2}, aperte, nn), "n = 0: caso base, ritorna 0")
        else:
            an.frame(scena({3, 4}, aperte, nn), f"n = {nn} > 0: serve somma_ricorsiva({nn - 1}) prima di sommare {nn}")
    risultati[0] = 0
    for k in range(len(ordine) - 2, -1, -1):
        nn = ordine[k]
        risultati[nn] = nn + risultati[nn - 1]
        an.frame(scena({4}, ordine[:k + 2], nn), f"torna {risultati[nn - 1]}: somma_ricorsiva({nn}) = {nn} + {risultati[nn - 1]} = {risultati[nn]}")
        an.frame(scena({4}, ordine[:k + 1], nn), f"il record di somma_ricorsiva({nn - 1}) viene tolto dalla pila")
    an.frame(scena(set(), [3], 3), "risultato 6 = 3·4/2; al massimo 4 = n+1 chiamate aperte insieme", 2.0)
    an.salva("animazione-somma-ricorsiva.svg")


# =================================================================== TSP
def nearest_neighbor():
    PSEUDO = [(1, "Pick and visit an initial point p0 from P"), (2, "p = p0"), (3, "i = 0"),
              (4, "While there are still unvisited points"), (5, "    i = i + 1"),
              (6, "    Select pi closest unvisited to p(i-1)"), (7, "    Visit pi"), (8, "Return to p0 from p(n-1)")]
    an = Animazione("NearestNeighbor sui punti −21, −5, −1, 0, 1, 3, 11 (slide 01 pp. 18–24)", 800, 540, 1.4)
    P = [-21, -5, -1, 0, 1, 3, 11]
    ordine_figura = {1: 0, -1: 1, 3: 2, -5: 3, 11: 4, -21: 5}     # parita' rotte come nella figura di p.24

    def X(v):
        return 50 + (v + 21) * (700 / 32)

    Y = 170

    def scena(righe, giro, corrente=None, candidati=(), chiuso=False):
        s = line(30, Y, 770, Y, GRIGIO, 1)
        for k in range(len(giro) - 1):
            a, b = giro[k], giro[k + 1]
            r = abs(X(b) - X(a)) / 2
            ry = min(r * 0.45, 95)
            sopra = k % 2 == 0
            sweep = (1 if X(b) > X(a) else 0) if sopra else (0 if X(b) > X(a) else 1)
            s += (f'<path d="M{X(a):.1f},{Y} A{r:.1f},{ry:.1f} 0 0,{sweep} {X(b):.1f},{Y}" '
                  f'fill="none" stroke="{BLU}" stroke-width="2"/>')
        if chiuso:
            a, b = giro[-1], giro[0]
            r = abs(X(b) - X(a)) / 2
            s += (f'<path d="M{X(a):.1f},{Y} A{r:.1f},{min(r * 0.45, 95):.1f} 0 0,0 {X(b):.1f},{Y}" fill="none" '
                  f'stroke="{ARANCIO}" stroke-width="2" stroke-dasharray="6 4"/>')
        for v in P:
            col = ROSSO if v == corrente else (VERDE if v in candidati else (TESTO if v in giro else GRIGIO))
            s += circle(X(v), Y, 7, col) + t(X(v), Y + 30, v, 14, col, "middle", True)
        L = sum(abs(giro[k + 1] - giro[k]) for k in range(len(giro) - 1)) + (abs(giro[-1] - giro[0]) if chiuso else 0)
        s += t(50, 300, f"giro finora: {' → '.join(str(v) for v in giro)}{' → 0' if chiuso else ''}", 14, TESTO, mono=True)
        s += t(50, 323, f"lunghezza finora: {L}", 14, TESTO, bold=True)
        s += an.pseudocodice(PSEUDO, righe, 50, 360, 420, 17)
        s += t(500, 370, "in verde: i candidati più vicini", 13, GRIGIO)
        s += t(500, 390, "(a ogni passo due punti equidistanti:", 13, GRIGIO)
        s += t(500, 410, " la figura sceglie quello peggiore)", 13, GRIGIO)
        return s

    giro = [0]
    an.frame(scena({1, 2, 3}, giro, 0), "parto da p0 = 0")
    rimasti = [v for v in P if v != 0]
    while rimasti:
        cur = giro[-1]
        dmin = min(abs(v - cur) for v in rimasti)
        cand = [v for v in rimasti if abs(v - cur) == dmin]
        scelto = min(cand, key=lambda v: ordine_figura[v])
        an.frame(scena({4, 5, 6}, giro, cur, cand), f"da {cur}: i più vicini non visitati sono {cand} (distanza {dmin})")
        giro.append(scelto)
        rimasti.remove(scelto)
        an.frame(scena({7}, giro, scelto), f"visito {scelto}")
    an.frame(scena({8}, giro, giro[-1], chiuso=True), "torno a 0 da −21 (distanza 21)")
    an.frame(scena(set(), giro, chiuso=True), "giro di NearestNeighbor = 84, ma l'ottimo (−21 … 11 e ritorno) è 64: sbagliato", 2.5)
    an.salva("animazione-nearest-neighbor.svg")


def closest_pair():
    PSEUDO = [(1, "Let n be the number of points in set P."), (2, "For i = 1 to n − 1 do"), (3, "    d = ∞"),
              (4, "    For each pair of endpoints (s,t)"), (0, "        from distinct vertex chains"),
              (5, "        if dist(s,t) ≤ d then"), (0, "            sm = s, tm = t, d = dist(s,t)"),
              (6, "    Connect (sm, tm) by an edge"), (7, "Connect the two endpoints by an edge")]
    an = Animazione("ClosestPair su due file di punti (slide 01 pp. 26–28)", 800, 440, 1.6)
    h, v = 1.12, 0.88
    PT = {"A": (0, v), "B": (h, v), "C": (2 * h, v), "D": (0, 0), "E": (h, 0), "F": (2 * h, 0)}

    def XY(p):
        x, y = PT[p]
        return 90 + x * 110, 200 - y * 110

    def dist(a, b):
        return math.dist(PT[a], PT[b])

    def scena(righe, archi, nuovo=None, chiusura=None, ottimo=False):
        s = ""
        if ottimo:
            giro = ["A", "B", "C", "F", "E", "D", "A"]
            for k in range(6):
                (x1, y1), (x2, y2) = XY(giro[k]), XY(giro[k + 1])
                s += line(x1, y1, x2, y2, VERDE, 3, "7 5")
        for a, b in archi:
            (x1, y1), (x2, y2) = XY(a), XY(b)
            s += line(x1, y1, x2, y2, ROSSO if (a, b) == nuovo else BLU, 3)
        if chiusura:
            (x1, y1), (x2, y2) = XY(chiusura[0]), XY(chiusura[1])
            s += line(x1, y1, x2, y2, ARANCIO, 3)
        for p in PT:
            x, y = XY(p)
            s += circle(x, y, 8, TESTO) + t(x, y - 14, p, 15, TESTO, "middle", True)
        L = sum(dist(a, b) for a, b in archi) + (dist(*chiusura) if chiusura else 0)
        s += t(40, 270, "distanza verticale 0.88 < orizzontale 1.12 (coordinate lette dal grafico)", 13, GRIGIO)
        s += t(40, 295, f"lunghezza finora: {L:.2f}", 15, TESTO, bold=True)
        if ottimo:
            s += t(40, 318, "tratteggio verde: giro ottimo A-B-C-F-E-D-A = 6.24", 14, VERDE, bold=True)
        s += an.pseudocodice(PSEUDO, righe, 370, 70, 420, 19)
        return s

    archi = []
    an.frame(scena({1}, archi), "ogni punto è una catena da solo")
    sequenza = [("A", "D"), ("B", "E"), ("C", "F"), ("A", "B"), ("E", "F")]
    for k, (a, b) in enumerate(sequenza, 1):
        an.frame(scena({2, 3, 4, 5}, archi), f"iterazione {k}: cerco la coppia di estremi più vicina tra catene distinte")
        archi.append((a, b))
        an.frame(scena({6}, archi, (a, b)), f"unisco {a}{b} (distanza {dist(a, b):.2f})")
    an.frame(scena({7}, archi, chiusura=("D", "C")), f"chiudo il ciclo unendo gli estremi D e C (diagonale {dist('D', 'C'):.2f})")
    an.frame(scena(set(), archi, chiusura=("D", "C"), ottimo=True), "ClosestPair = 7.29 contro l'ottimo 6.24: sbagliato", 2.5)
    an.salva("animazione-closest-pair.svg")


def optimal_tsp():
    PSEUDO = [(1, "d = ∞"), (2, "For each of the n! permutations Pi of P"),
              (3, "    If (cost(Pi) ≤ d)"), (0, "        then d = cost(Pi) and Pmin = Pi"), (4, "Return Pmin")]
    an = Animazione("OptimalTSP: prova tutte le 4! = 24 permutazioni (istanza di esempio mia)", 800, 400, 0.7)
    PT = {"A": (0, 0), "B": (4, 0), "C": (1, 3), "D": (4, 4)}

    def XY(p):
        return 70 + PT[p][0] * 55, 290 - PT[p][1] * 55

    def cost(perm):
        return sum(math.dist(PT[perm[k]], PT[perm[(k + 1) % len(perm)]]) for k in range(len(perm)))

    def disegna(perm, col, w, dash=None):
        s = ""
        for k in range(len(perm)):
            (x1, y1), (x2, y2) = XY(perm[k]), XY(perm[(k + 1) % len(perm)])
            s += line(x1, y1, x2, y2, col, w, dash)
        return s

    def scena(righe, perm, d, best, k):
        s = ""
        if best:
            s += disegna(best, VERDE, 6)
        if perm:
            s += disegna(perm, BLU, 2, "6 4")
        for p in PT:
            x, y = XY(p)
            s += circle(x, y, 8, TESTO) + t(x - 12, y - 10, p, 15, TESTO, "end", True)
        s += t(360, 250, f"permutazione {k}/24: {''.join(perm) if perm else '–'}", 15, BLU, bold=True, mono=True)
        if perm:
            s += t(360, 275, f"cost = {cost(perm):.2f}", 15, BLU, mono=True)
        s += t(360, 305, f"d = {'∞' if d == math.inf else f'{d:.2f}'}   Pmin = {''.join(best) if best else '–'}", 15, VERDE, bold=True, mono=True)
        s += t(360, 330, "blu tratteggiato: permutazione corrente; verde: la migliore finora", 12, GRIGIO)
        s += an.pseudocodice(PSEUDO, righe, 360, 80, 420)
        return s

    d, best = math.inf, None
    an.frame(scena({1}, None, d, None, 0), "d = ∞: nessuna permutazione ancora esaminata")
    for k, perm in enumerate(itertools.permutations("ABCD"), 1):
        c = cost(perm)
        migliore = c <= d
        if migliore:
            d, best = c, perm
        an.frame(scena({2, 3}, perm, d, best, k),
                 f"cost({''.join(perm)}) = {c:.2f} {'≤ d: nuova migliore' if migliore else '> d: scartata'}")
    an.frame(scena({4}, None, d, best, 24), f"Return Pmin = {''.join(best)} (cost {d:.2f}): corretto, ma ha esaminato n! = 24 giri", 2.5)
    an.salva("animazione-optimal-tsp.svg")


# =================================================================== MOVIE SCHEDULING
FILM = [("Tarjan of the Jungle", 96.8, 303.1, BLU), ("The Four Volume Problem", 380.2, 628.9, VIOLA),
        ("The President's Algorist", 4.7, 241.6, GIALLO), ("Steiner's Tree", 274.0, 402.1, VERDE),
        ("Process Terminated", 550.4, 770.4, ARANCIO), ("Halting State", 231.5, 359.6, ROSSO),
        ("Programming Challenges", 423.0, 600.5, ROSSO), ('"Discrete" Mathematics', 33.1, 182.2, ROSSO),
        ("Calculated Bets", 613.8, 784.8, ROSSO)]
RIGA = {"Tarjan of the Jungle": 0, "The Four Volume Problem": 0, "Steiner's Tree": 1, "Process Terminated": 1,
        "The President's Algorist": 2, "Halting State": 3, "Programming Challenges": 3,
        '"Discrete" Mathematics': 4, "Calculated Bets": 5}


def sovrapposti(a, b):
    return a[1] < b[2] and b[1] < a[2]


def scena_film(stato, evidenzia=None, extra=""):
    """stato: nome -> 'ok' | 'no' | None. Intervalli come nella figura di p.37 (coordinate estratte)."""
    s = ""
    for nome, x0, x1, col in FILM:
        y = 70 + RIGA[nome] * 38
        X0, X1 = 20 + x0 * 0.95, 20 + x1 * 0.95
        st = stato.get(nome)
        opac = "0.35" if st == "no" else "1"
        s += f'<g opacity="{opac}">'
        if nome == evidenzia:
            s += rect(X0 - 4, y - 18, X1 - X0 + 8, 30, fill=EVID, stroke="none", rx=3)
        s += line(X0, y + 6, X1, y + 6, col, 3)
        s += t((X0 + X1) / 2, y, nome, 13, col, "middle", True)
        s += "</g>"
        if st == "ok":
            s += circle((X0 + X1) / 2, y + 6, 9, "none", BLU, 3)
        elif st == "no":
            s += t((X0 + X1) / 2, y + 12, "✘", 20, ROSSO, "middle", True)
    return s + extra


def movie_greedy(nome_file, titolo, scegli, criterio, pseudo, righe_scelta, righe_elimina):
    an = Animazione(titolo, 800, 450, 1.3)
    stato = {}
    S = list(FILM)

    def scena(righe, ev=None):
        acc = [n for n, st in stato.items() if st == "ok"]
        extra = t(20, 300, f"accettati: {len(acc)}", 14, BLU, bold=True)
        extra += an.pseudocodice(pseudo, righe, 380, 300, 410, 19)
        extra += t(20, 322, criterio, 13, GRIGIO)
        return scena_film(stato, ev, extra)

    an.frame(scena(set()), "istanza di p. 37: 9 film (intervalli)")
    while S:
        j = scegli(S)
        an.frame(scena(righe_scelta, j[0]), f"scelgo «{j[0]}»")
        stato[j[0]] = "ok"
        tolti = [x for x in S if x is not j and sovrapposti(x, j)]
        for x in tolti:
            stato[x[0]] = "no"
        S = [x for x in S if x is not j and not sovrapposti(x, j)]
        an.frame(scena(righe_elimina, j[0]),
                 f"accetto «{j[0]}»" + (f"; escludo: {', '.join(x[0] for x in tolti)}" if tolti else ""))
    acc = [n for n, st in stato.items() if st == "ok"]
    an.frame(scena(set()), f"risultato: {len(acc)} film", 2.5)
    an.salva(nome_file)


def earliest_job_first():
    PSEUDO = [(1, "Accept the earliest starting job j from S"), (0, "  which does not overlap any previously"),
              (0, "  accepted job, and repeat until no more"), (0, "  such jobs remain.")]
    movie_greedy("animazione-earliest-job-first.svg",
                 "EarliestJobFirst sui 9 film (slide 01 pp. 38–46)",
                 lambda S: min(S, key=lambda x: x[1]),
                 "criterio: il job che INIZIA prima tra quelli rimasti",
                 PSEUDO, {1}, {1})


def shortest_job_first():
    PSEUDO = [(1, "While (S ≠ ∅) do"), (2, "    Accept the shortest possible job j from S."),
              (3, "    Delete j, and any interval which"), (0, "    intersects j from S.")]
    movie_greedy("animazione-shortest-job-first.svg",
                 "ShortestJobFirst sui 9 film (slide 01 pp. 47–55)",
                 lambda S: min(S, key=lambda x: x[2] - x[1]),
                 "criterio: il job più CORTO tra quelli rimasti",
                 PSEUDO, {1, 2}, {3})


def optimal_scheduling():
    PSEUDO = [(1, "While (S ≠ ∅) do"), (2, "    Accept the job j from S with the"), (0, "    earliest completion date."),
              (3, "    Delete j, and any interval which"), (0, "    intersects j from S.")]
    movie_greedy("animazione-optimal-scheduling.svg",
                 "OptimalScheduling sui 9 film della slide 01 p. 37 (regola di p. 60)",
                 lambda S: min(S, key=lambda x: x[2]),
                 "criterio: il job che FINISCE prima tra quelli rimasti",
                 PSEUDO, {1, 2}, {3})


def exhaustive_scheduling():
    PSEUDO = [(1, "j = 0, Smax = ∅"), (2, "For each of the 2^n subsets Si"), (0, "    of intervals S"),
              (3, "    If (Si is mutually non-overlapping)"), (0, "       and (size(Si) > j)"),
              (4, "        then j = size(Si) and Smax = Si."), (5, "Return Smax")]
    an = Animazione("ExhaustiveScheduling: tutti i 2⁴ = 16 sottoinsiemi (istanza di esempio mia)", 800, 420, 0.9)
    I = [("a", 0, 10), ("b", 1, 2), ("c", 3, 4), ("d", 5, 6)]

    def X(v):
        return 60 + v * 30

    def scena(righe, Si, ok, jbest, Smax, k):
        s = ""
        for r, (nome, a, b) in enumerate(I):
            y = 80 + r * 36
            dentro = nome in Si
            col = (VERDE if ok else ROSSO) if dentro else GRIGIO
            s += line(X(a), y, X(b), y, col, 6 if dentro else 2)
            s += t(X(a) - 8, y + 5, f"{nome} [{a},{b})", 13, col, "end", True)
            if nome in Smax:
                s += circle(X(b) + 14, y, 6, BLU)
        s += t(60, 250, f"sottoinsieme {k}/16: {{{', '.join(Si)}}}", 15, TESTO, bold=True, mono=True)
        if k:
            s += t(60, 275, "senza sovrapposizioni" if ok else "ha sovrapposizioni: scartato", 14, VERDE if ok else ROSSO)
        s += t(60, 300, f"j = {jbest}, Smax = {{{', '.join(Smax)}}}  (pallino blu)", 14, BLU, bold=True, mono=True)
        s += an.pseudocodice(PSEUDO, righe, 400, 80, 390, 19)
        return s

    jbest, Smax = 0, ()
    an.frame(scena({1}, (), True, 0, (), 0), "j = 0, Smax = ∅")
    k = 0
    for r in range(len(I) + 1):
        for Si in itertools.combinations(I, r):
            k += 1
            nomi = tuple(x[0] for x in Si)
            ok = all(not (x[1] < y[2] and y[1] < x[2]) for x, y in itertools.combinations(Si, 2))
            migliore = ok and len(Si) > jbest
            if migliore:
                jbest, Smax = len(Si), nomi
            an.frame(scena({2, 3, 4} if migliore else {2, 3}, nomi, ok, jbest, Smax, k),
                     f"{{{', '.join(nomi)}}}: " + ("nuovo migliore" if migliore else ("valido ma non più grande" if ok else "sovrapposto")))
    an.frame(scena({5}, Smax, True, jbest, Smax, 16), f"Return Smax = {{{', '.join(Smax)}}} dopo aver visto tutti i 16 sottoinsiemi", 2.5)
    an.salva("animazione-exhaustive-scheduling.svg")


# =================================================================== DIVIDE ET IMPERA (lezioni 06-07)
PSEUDO_MERGE = [(1, "n1 ← q-p+1"), (2, "n2 ← r-q"), (3, "// create L[1..n1+1] and R[1..n2+1]"),
                (4, "for i ← 1 to n1"), (5, "    do L[i] ← A[p+i-1]"), (6, "for j ← 1 to n2"),
                (7, "    do R[j] ← A[q+j]"), (8, "L[n1+1] ← R[n2+1] ← ∞"), (9, "i ← j ← 1"),
                (10, "for k ← p to r"), (11, "    do if L[i] ≤ R[j]"), (12, "        then A[k] ← L[i]"),
                (13, "             i ← i+1"), (14, "        else A[k] ← R[j]"), (15, "             j ← j+1")]


def merge():
    an = Animazione("Merge(A, p, q, r) su A[p..r] = ⟨2, 4, 5, 7, 1, 2, 3, 6⟩ (slide 06 p. 17)", 820, 470, 1.1)
    A = [None, 2, 4, 5, 7, 1, 2, 3, 6]
    p, q, r = 1, 4, 8
    L = [None] + A[p:q + 1] + ["∞"]
    R = [None] + A[q + 1:r + 1] + ["∞"]
    X0 = 30

    def scena(righe, k=None, i=None, j=None, copiati=False, scelto=None, nota=""):
        col = {kk: ORDINATO for kk in range(p, k)} if k else {}
        s = t(X0, 72, "A", 16, TESTO, bold=True) + array(A[1:], X0 + 20, 80, cw=46, ch=40, colori=col)
        s += t(X0 + 20 + 23, 66, "p", 12, BLU, "middle", True) + t(X0 + 20 + 3 * 46 + 23, 66, "q", 12, BLU, "middle", True)
        s += t(X0 + 20 + 7 * 46 + 23, 66, "r", 12, BLU, "middle", True)
        if k and k <= r:
            s += freccia_su(X0 + 20 + (k - 1) * 46 + 23, 122, "k", ROSSO)
        if copiati:
            cl = {i: ("#d9ecf7" if scelto == "L" else "#ffffff")} if i else {}
            cr = {j: ("#d9ecf7" if scelto == "R" else "#ffffff")} if j else {}
            s += t(X0, 222, "L", 16, TESTO, bold=True) + array(L[1:], X0 + 20, 200, cw=40, ch=36, colori=cl)
            s += t(X0, 302, "R", 16, TESTO, bold=True) + array(R[1:], X0 + 20, 280, cw=40, ch=36, colori=cr)
            if i:
                s += t(X0 + 20 + (i - 1) * 40 + 20, 252, "i", 14, BLU, "middle", True)
            if j:
                s += t(X0 + 20 + (j - 1) * 40 + 20, 332, "j", 14, BLU, "middle", True)
        if k:
            s += t(X0, 372, f"invariante: A[p..k−1] = i {k - p} elementi più piccoli di L e R, ordinati", 13, VERDE, bold=True)
        if nota:
            s += t(X0, 395, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO_MERGE, righe, 470, 60, 340, 18)
        return s

    an.frame(scena(set()), "le due metà A[p..q] e A[q+1..r] sono già ordinate")
    an.frame(scena({1, 2, 3, 4, 5, 6, 7}, copiati=True), "n1 = 4, n2 = 4: copio A[p..q] in L e A[q+1..r] in R")
    an.frame(scena({8, 9}, copiati=True, i=1, j=1), "metto le sentinelle ∞ in fondo a L e R; i ← j ← 1")
    i = j = 1
    for k in range(p, r + 1):
        if L[i] != "∞" and (R[j] == "∞" or L[i] <= R[j]):
            an.frame(scena({10, 11}, k, i, j, True, "L"), f"k = {k}: L[{i}] = {L[i]} ≤ R[{j}] = {R[j]}? sì")
            A[k] = L[i]; i += 1
            an.frame(scena({12, 13}, k + 1, i, j, True), f"A[{k}] ← {A[k]}, i ← {i}")
        else:
            an.frame(scena({10, 11}, k, i, j, True, "R"), f"k = {k}: L[{i}] = {L[i]} ≤ R[{j}] = {R[j]}? no")
            A[k] = R[j]; j += 1
            an.frame(scena({14, 15}, k + 1, i, j, True), f"A[{k}] ← {A[k]}, j ← {j}")
    an.frame(scena(set(), r + 1, i, j, True, nota="in L e R restano solo le due sentinelle ∞ (slide 06 p. 20)"),
             "k = r + 1: A[p..r] = ⟨1, 2, 2, 3, 4, 5, 6, 7⟩ ordinato; n = 8 iterazioni → Θ(n)", 2.5)
    an.salva("animazione-merge.svg")


def merge_sort():
    PSEUDO = [(1, "if p<r"), (2, "    q ← ⌊(p+r)/2⌋"), (3, "    Merge-Sort (A,p,q)"),
              (4, "    Merge-Sort (A,q+1,r)"), (5, "    Merge (A,p,q,r)")]
    an = Animazione("Merge-Sort(A, 1, 11) su ⟨5, 2, 8, 0, 4, 7, 1, 9, 3, 2, 6⟩ (slide 06 p. 8)", 820, 520, 0.9)
    A = [None, 5, 2, 8, 0, 4, 7, 1, 9, 3, 2, 6]
    n = 11
    cw, X0, Y0, DY = 66, 48, 70, 62
    nodi = {}                    # (p, r) -> (profondita', valori, stato)

    def scena(righe, attivo=None, nota=""):
        s = ""
        for (pp, rr), (prof, val, stato) in sorted(nodi.items()):
            x = X0 + (pp - 1) * cw
            y = Y0 + prof * DY
            w = (rr - pp + 1) * cw - 6
            fill = ORDINATO if stato == "ordinato" else "#ffffff"
            bordo = ROSSO if (pp, rr) == attivo else (VERDE if stato == "ordinato" else GRIGIO)
            s += rect(x, y, w, 40, fill=fill, stroke=bordo, sw=2.5 if (pp, rr) == attivo else 1.5)
            s += t(x + w / 2, y + 27, "  ".join(str(v) for v in val), 17, TESTO, "middle", True, mono=True)
            s += t(x + 2, y - 4, f"[{pp}..{rr}]", 10, GRIGIO)
        s += t(X0, 400, "bianco: da ordinare · verde: ordinato (dopo Merge) · rosso: chiamata attiva", 12, GRIGIO)
        if nota:
            s += t(X0, 422, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO, righe, 560, 400, 240, 15)
        return s

    def ms(pp, rr, prof):
        nodi[(pp, rr)] = (prof, A[pp:rr + 1], "da ordinare")
        if pp < rr:
            q = (pp + rr) // 2
            an.frame(scena({1, 2}, (pp, rr)), f"Merge-Sort(A, {pp}, {rr}): q = ⌊({pp}+{rr})/2⌋ = {q}, divido in [{pp}..{q}] e [{q + 1}..{rr}]")
            ms(pp, q, prof + 1)
            ms(q + 1, rr, prof + 1)
            A[pp:rr + 1] = sorted(A[pp:rr + 1])
            nodi[(pp, rr)] = (prof, A[pp:rr + 1], "ordinato")
            an.frame(scena({5}, (pp, rr)), f"Merge(A, {pp}, {q}, {rr}): fondo le due metà ordinate → {A[pp:rr + 1]}")
        else:
            nodi[(pp, rr)] = (prof, A[pp:rr + 1], "ordinato")
            an.frame(scena({1}, (pp, rr)), f"Merge-Sort(A, {pp}, {rr}): p = r, un solo elemento, già ordinato")

    an.frame(scena(set()), "si invoca Merge-Sort(A, 1, n) con n = 11")
    ms(1, n, 0)
    an.frame(scena(set(), nota="non sul posto: Merge usa gli array ausiliari L e R (slide 06 p. 7)"),
             "risultato ⟨0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9⟩: albero di ⌈lg 11⌉ + 1 = 5 livelli", 2.5)
    an.salva("animazione-merge-sort.svg")


PSEUDO_PARTITION = [(1, "x ← A[r]"), (2, "i ← p-1"), (3, "for j ← p to r-1"), (4, "    if A[j] ≤ x"),
                    (5, "        i ← i+1"), (6, "        exchange A[i] ↔ A[j]"), (7, "exchange A[i+1] ↔ A[r]"),
                    (8, "return i+1")]


def scena_partition(an, A, p, r, i, j, righe, x0=40, y0=110, cw=56, extra="", finale=None):
    """Quattro aree di slide 07 p.5: p..i giallo (<= x), i+1..j-1 rosso (> x), j..r-1 bianco, r pivot."""
    col, tcol = {}, {}
    for k in range(p, r + 1):
        if finale is not None:
            col[k] = "#d0e8f7" if k == finale else ("#fff3b0" if k < finale else "#fbc8c3")
        elif k == r:
            col[k] = "#d0e8f7"
        elif k <= i:
            col[k] = "#fff3b0"
        elif j is not None and i + 1 <= k <= j - 1:
            col[k] = "#fbc8c3"
    s = array(A[1:], x0, y0, cw=cw, ch=48, colori=col)
    s += t(x0 + (p - 1) * cw + cw / 2, y0 - 26, "p", 13, BLU, "middle", True)
    s += t(x0 + (r - 1) * cw + cw / 2, y0 - 26, "r", 13, BLU, "middle", True)
    if finale is None:
        if i >= p:
            s += freccia_su(x0 + (i - 1) * cw + cw / 2 - 8, y0 + 50, "i", VERDE)
        else:
            s += t(x0 + (p - 1) * cw - 6, y0 + 92, f"i = {i}", 13, VERDE, "end", True)
        if j is not None and j <= r:
            s += freccia_su(x0 + (j - 1) * cw + cw / 2 + 8, y0 + 50, "j", ROSSO)
    s += t(x0, y0 + 130, "giallo: ≤ pivot · rosso: > pivot · bianco: non ancora analizzati · azzurro: pivot", 12, GRIGIO)
    s += extra
    return s


def partition():
    an = Animazione("Partition(A, 1, 8) su ⟨2, 8, 7, 1, 3, 5, 6, 4⟩, pivot x = A[r] = 4 (slide 07 pp. 5–12)", 820, 420, 1.2)
    A = [None, 2, 8, 7, 1, 3, 5, 6, 4]
    p, r = 1, 8
    x = A[r]
    pse = lambda righe: an.pseudocodice(PSEUDO_PARTITION, righe, 520, 90, 280)
    an.frame(scena_partition(an, A, p, r, p - 1, p, set(), extra=pse({1, 2})), "x ← A[r] = 4, i ← p − 1 = 0: le prime due aree sono vuote")
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            an.frame(scena_partition(an, A, p, r, i, j, set(), extra=pse({3, 4})), f"j = {j}: A[{j}] = {A[j]} ≤ 4? sì")
            i += 1
            A[i], A[j] = A[j], A[i]
            an.frame(scena_partition(an, A, p, r, i, j + 1, set(), extra=pse({5, 6})),
                     f"i ← {i}, scambio A[{i}] ↔ A[{j}]: l'elemento entra nell'area gialla")
        else:
            an.frame(scena_partition(an, A, p, r, i, j, set(), extra=pse({3, 4})), f"j = {j}: A[{j}] = {A[j]} ≤ 4? no")
            an.frame(scena_partition(an, A, p, r, i, j + 1, set(), extra=pse({3})), f"basta far avanzare j: {A[j]} resta nell'area rossa")
    A[i + 1], A[r] = A[r], A[i + 1]
    an.frame(scena_partition(an, A, p, r, i, None, set(), extra=pse({7, 8}), finale=i + 1),
             f"fine del ciclo: scambio A[{i + 1}] ↔ A[r], il pivot va in posizione q = {i + 1}; return {i + 1}", 2.5)
    an.salva("animazione-partition.svg")


def _quicksort_frames(an, A, pse, scegli=None, titolo_chiamata="Quicksort"):
    n = len(A) - 1
    fissati = set()

    def colori(p, r):
        c = {k: ORDINATO for k in fissati}
        for k in range(p, r + 1):
            if k not in fissati:
                c[k] = "#fdf0c4"
        return c

    def scena(righe, p, r, nota=""):
        s = array(A[1:], 40, 110, cw=56, ch=48, colori=colori(p, r))
        if p == r:
            s += t(40 + (p - 1) * 56 + 28, 84, "p,r", 13, BLU, "middle", True)
        elif p < r:
            s += t(40 + (p - 1) * 56 + 28, 84, "p", 13, BLU, "middle", True)
            s += t(40 + (r - 1) * 56 + 28, 84, "r", 13, BLU, "middle", True)
        s += t(40, 200, "giallo: chiamata attiva · verde: pivot al suo posto", 12, GRIGIO)
        if nota:
            s += t(40, 225, nota, 13, TESTO)
        s += pse(righe)
        return s

    def qs(p, r, prof):
        if p < r:
            nota = ""
            if scegli:
                k = scegli(p, r)
                A[r], A[k] = A[k], A[r]
                nota = f"Random({p}, {r}) = {k}: scambio A[r] ↔ A[{k}], il pivot è {A[r]}"
                an.frame(scena({2, 5, 6}, p, r, nota),
                         f"{titolo_chiamata}(A, {p}, {r}) — profondità {prof}: pivot scelto a caso")
            q = _partition_semplice(A, p, r)
            fissati.add(q)
            an.frame(scena({2} if titolo_chiamata == "Quicksort" else {7}, p, r, f"pivot {A[q]} in posizione q = {q}"),
                     f"{titolo_chiamata}(A, {p}, {r}) — profondità {prof}: Partition → q = {q}")
            qs(p, q - 1, prof + 1)
            qs(q + 1, r, prof + 1)
        elif p == r:
            fissati.add(p)
            an.frame(scena({1}, p, r),
                     f"{titolo_chiamata}(A, {p}, {r}): un solo elemento, niente da fare")

    an.frame(scena(set(), 1, n), f"si invoca {titolo_chiamata}(A, 1, {n})")
    qs(1, n, 0)
    fissati.update(range(1, n + 1))
    return scena


def _partition_semplice(A, p, r):
    x, i = A[r], p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort():
    PSEUDO = [(1, "if p<r"), (2, "    q ← Partition (A,p,r)"), (3, "    Quicksort (A,p,q-1)"), (4, "    Quicksort (A,q+1,r)")]
    an = Animazione("Quicksort(A, 1, 8) su ⟨2, 8, 7, 1, 3, 5, 6, 4⟩ (slide 07 pp. 4–12)", 820, 400, 1.3)
    A = [None, 2, 8, 7, 1, 3, 5, 6, 4]
    pse = lambda righe: an.pseudocodice(PSEUDO, righe, 520, 260, 280)
    scena = _quicksort_frames(an, A, pse)
    an.frame(scena(set(), 1, 0), "ordinato sul posto: ⟨1, 2, 3, 4, 5, 6, 7, 8⟩ (Combine: niente da fare)", 2.5)
    an.salva("animazione-quicksort.svg")


def quicksort_randomizzato():
    import random as _r
    PSEUDO = [(0, "Randomized-Quicksort (A,p,r)"), (1, "  if p<r"), (2, "    q ← Randomized-Partition (A,p,r)"),
              (3, "    Randomized-Quicksort (A,p,q-1)"), (4, "    Randomized-Quicksort (A,q+1,r)"),
              (0, "Randomized-Partition (A,p,r)"), (5, "  i ← Random (p,r)"),
              (6, "  exchange A[r] ↔ A[i]"), (7, "  return Partition (A,p,r)")]
    an = Animazione("Randomized-Quicksort su ⟨1, 2, …, 8⟩ già ordinato (istanza mia; slide 07 p. 20)", 820, 440, 1.3)
    A = [None, 1, 2, 3, 4, 5, 6, 7, 8]
    rng = _r.Random(4)
    pse = lambda righe: an.pseudocodice(PSEUDO, righe, 425, 205, 385, 19)
    scena = _quicksort_frames(an, A, pse, scegli=lambda p, r: rng.randint(p, r), titolo_chiamata="Randomized-Quicksort")
    an.frame(scena(set(), 1, 0, "con pivot fisso A[r] la profondità sarebbe 7"),
             "ordinato: il pivot casuale evita le partizioni n−1 / 0 dell'array ordinato", 2.5)
    an.salva("animazione-quicksort-randomizzato.svg")


def torre_di_hanoi():
    PSEUDO = [(0, "HANOI(n, da, a, via)"), (1, "  if n > 0"), (2, "    HANOI(n−1, da, via, a)"),
              (3, "    sposta disco n: da → a"), (4, "    HANOI(n−1, via, a, da)")]
    an = Animazione("Torre di Hanoi con 3 dischi da A a C (slide 06 pp. 2–5; pseudocodice mio)", 820, 420, 1.4)
    pioli = {"A": [3, 2, 1], "B": [], "C": []}
    colori_disco = {1: ARANCIO, 2: "#c8c8c8", 3: VERDE}
    PX = {"A": 110, "B": 260, "C": 410}

    def scena(righe, k, nota, chiamata=""):
        s = ""
        for nome, x in PX.items():
            s += rect(x - 4, 110, 8, 170, fill=BLU, stroke="none", rx=2) + t(x, 100, nome, 16, TESTO, "middle", True)
            for liv, d in enumerate(pioli[nome]):
                w = 40 + d * 34
                s += rect(x - w / 2, 262 - liv * 22, w, 20, fill=colori_disco[d], stroke=TESTO, sw=1, rx=6)
                s += t(x, 277 - liv * 22, d, 12, TESTO, "middle", True)
        s += line(30, 283, 520, 283, TESTO, 3)
        s += t(40, 315, f"mosse eseguite: {k} / 7 = 2³ − 1", 14, TESTO, bold=True)
        if chiamata:
            s += t(40, 338, chiamata, 13, VIOLA, mono=True)
        s += an.pseudocodice(PSEUDO, righe, 548, 110, 268, 19)
        return s

    mosse = []

    def hanoi(n, da, a, via, prof):
        if n == 0:
            return
        hanoi(n - 1, da, via, a, prof + 1)
        mosse.append((n, da, a, f"{'  ' * prof}HANOI({n}, {da}, {a}, {via})"))
        hanoi(n - 1, via, a, da, prof + 1)

    hanoi(3, "A", "C", "B", 0)
    an.frame(scena(set(), 0, ""), "stato iniziale: tre dischi su A, il più grande in basso (slide 06 p. 5)")
    for k, (d, da, a, chiamata) in enumerate(mosse, 1):
        pioli[a].append(pioli[da].pop())
        an.frame(scena({3}, k, "", "chiamata attiva: " + chiamata.strip()), f"mossa {k}: disco {d} da {da} a {a}")
    an.frame(scena(set(), 7, ""), "tutti i dischi su C: 7 mosse, come nella sequenza di p. 5", 2.5)
    an.salva("animazione-torre-di-hanoi.svg")


def nuts_and_bolts():
    import random as _r
    PSEUDO = [(0, "NUTS-BOLTS(D, B)"), (1, "  if D = ∅ return"), (2, "  d ← dado scelto a caso in D"),
              (3, "  dividi B con d: B<, b, B>"), (4, "  dividi D con b: D<, D>"),
              (5, "  accoppia d con b"), (6, "  NUTS-BOLTS(D<, B<)"), (7, "  NUTS-BOLTS(D>, B>)")]
    an = Animazione("Nuts and Bolts randomizzato su 6 coppie (istanza mia; slide 07 pp. 24–25)", 820, 440, 1.5)
    rng = _r.Random(3)
    dadi = [4, 1, 6, 3, 5, 2]
    bulloni = [3, 6, 2, 5, 1, 4]
    coppie = []
    test = [0]

    def riga(vals, y, etichetta, evid=None, forma="dado"):
        s = t(30, y + 26, etichetta, 14, TESTO, bold=True)
        for k, v in enumerate(vals):
            x = 110 + k * 56
            col = EVID if v == evid else "#ffffff"
            if forma == "dado":
                s += circle(x + 22, y + 20, 20, col, TESTO, 1.5)
            else:
                s += rect(x + 4, y, 36, 40, fill=col, stroke=TESTO, sw=1.5, rx=2)
            s += t(x + 22, y + 26, v, 16, TESTO, "middle", True)
        return s

    def scena(righe, D, B, nota="", evid=None):
        s = riga(D, 70, "dadi", evid, "dado") + riga(B, 140, "bulloni", evid, "bullone")
        s += t(30, 225, "coppie trovate: " + (", ".join(f"{d}↔{b}" for d, b in coppie) or "nessuna"), 14, VERDE, bold=True)
        s += t(30, 250, f"test dado–bullone eseguiti: {test[0]}", 14, TESTO)
        if nota:
            s += t(30, 275, nota, 13, TESTO)
        s += t(30, 300, "(i numeri sono le larghezze, che si possono solo confrontare dado contro bullone)", 12, GRIGIO)
        s += an.pseudocodice(PSEUDO, righe, 480, 70, 330, 19)
        return s

    def ricorri(D, B):
        if not D:
            return
        d = rng.choice(D)
        an.frame(scena({1, 2}, D, B, f"sottoproblema con {len(D)} coppie: scelgo a caso il dado {d}", d), f"dado pivot {d}")
        Bm = [b for b in B if b < d]; BM = [b for b in B if b > d]
        test[0] += len(B)
        an.frame(scena({3}, D, B, f"bulloni più stretti {Bm}, gemello {d}, più larghi {BM}", d),
                 f"{len(B)} test: divido i bulloni con il dado {d}")
        Dm = [x for x in D if x < d]; DM = [x for x in D if x > d]
        test[0] += len(D) - 1
        coppie.append((d, d))
        an.frame(scena({4, 5}, D, B, f"dadi più stretti {Dm}, più larghi {DM}; accoppio {d}↔{d}", d),
                 f"{len(D) - 1} test: divido i dadi con il bullone gemello")
        ricorri(Dm, Bm)
        ricorri(DM, BM)

    an.frame(scena(set(), dadi, bulloni), "n = 6 dadi e 6 bulloni da accoppiare")
    ricorri(dadi, bulloni)
    an.frame(scena(set(), dadi, bulloni, "è Partition di quicksort applicata due volte: tempo atteso O(n log n)"),
             f"tutte le 6 coppie trovate con {test[0]} test (il metodo quadratico ne fa fino a n(n+1)/2 = 21)", 2.5)
    an.salva("animazione-nuts-and-bolts.svg")


def nuts_and_bolts_quadratico():
    PSEUDO = [(0, "NUTS-BOLTS-QUADRATICO(D, B)"), (1, "for i ← 1 to n"), (2, "    j ← i"),
              (3, "    while D[j] non combacia con B[i]"), (4, "        j ← j+1"),
              (5, "    exchange D[i] ↔ D[j]")]
    an = Animazione("Nuts and Bolts quadratico su 6 coppie (istanza mia; slide 07 p. 25)", 820, 400, 0.9)
    D = [None, 4, 1, 6, 3, 5, 2]
    B = [None, 3, 6, 2, 5, 1, 4]
    n = 6
    test = [0]

    def scena(righe, i=None, j=None, esito=None, nota=""):
        s = t(30, 96, "bulloni B", 14, TESTO, bold=True) + t(30, 176, "dadi D", 14, TESTO, bold=True)
        for k in range(1, n + 1):
            x = 120 + (k - 1) * 56
            s += t(x + 22, 62, k, 11, GRIGIO, "middle")
            fatto = i is not None and k < i
            colB = ORDINATO if fatto else (EVID if k == i else "#ffffff")
            s += rect(x + 4, 70, 36, 40, fill=colB, stroke=TESTO, sw=1.5, rx=2) + t(x + 22, 96, B[k], 16, TESTO, "middle", True)
            colD = ORDINATO if fatto else "#ffffff"
            if k == j and esito is not None:
                colD = "#d0e8f7" if esito else "#fbc8c3"
            s += circle(x + 22, 170, 20, colD, TESTO, 1.5) + t(x + 22, 176, D[k], 16, TESTO, "middle", True)
        if i is not None and i <= n:
            s += t(120 + (i - 1) * 56 + 22, 132, "i", 14, BLU, "middle", True)
        if j is not None and j <= n:
            s += freccia_su(120 + (j - 1) * 56 + 22, 192, "j", ROSSO)
        s += t(30, 268, f"test dado–bullone eseguiti: {test[0]}", 14, TESTO, bold=True)
        s += t(30, 292, "verde: coppie già formate (D[1..i−1] combacia con B[1..i−1])", 12, GRIGIO)
        if nota:
            s += t(30, 316, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO, righe, 468, 70, 345, 21)
        return s

    an.frame(scena(set()), "n = 6: per ogni bullone si cercano i dadi uno alla volta")
    for i in range(1, n + 1):
        j = i
        while True:
            test[0] += 1
            ok = D[j] == B[i]
            an.frame(scena({3} if ok else {3, 4}, i, j, ok, f"D[{j}] = {D[j]} contro B[{i}] = {B[i]}: " + ("combaciano" if ok else "non combaciano")),
                     f"i = {i}, j = {j}: test n. {test[0]}")
            if ok:
                break
            j += 1
        D[i], D[j] = D[j], D[i]
        an.frame(scena({5}, i + 1, None, None, f"exchange D[{i}] ↔ D[{j}]: il dado {D[i]} va accanto al suo bullone"),
                 f"coppia {i} formata dopo {j - i + 1} test")
    an.frame(scena(set(), n + 1, None, None, "nel caso peggiore n + (n−1) + … + 1 = n(n+1)/2 = 21 test"),
             f"tutte le coppie formate con {test[0]} test: O(n²)", 2.5)
    an.salva("animazione-nuts-and-bolts-quadratico.svg")



# =================================================================== GRAFI E ALBERI (lezioni 08-09)
class _N:
    def __init__(self, key, left=None, right=None):
        self.key, self.left, self.right, self.p = key, left, right, None
        for c in (left, right):
            if c is not None:
                c.p = self


def _bst(chiavi):
    root = None
    for k in chiavi:
        z, y, x = _N(k), None, root
        while x is not None:
            y = x
            x = x.left if k < x.key else x.right
        z.p = y
        if y is None:
            root = z
        elif k < y.key:
            y.left = z
        else:
            y.right = z
    return root


def _disegna_albero(root, x0=25, y0=80, w=420, dy=62, col=None, etich=None, r=17):
    """Nodi in ascissa per rango nella visita in ordine, in ordinata per profondita'."""
    col, etich = col or {}, etich or {}
    pos, ordine = {}, []

    def visita(x, d):
        if x is None:
            return
        visita(x.left, d + 1)
        ordine.append((x, d))
        visita(x.right, d + 1)

    visita(root, 0)
    n = max(len(ordine), 1)
    dx = w / n
    for k, (x, d) in enumerate(ordine):
        pos[x] = (x0 + dx * (k + 0.5), y0 + d * dy)
    s = ""
    for x, (px, py) in pos.items():
        for c in (x.left, x.right):
            if c is not None:
                cx, cy = pos[c]
                s += line(px, py, cx, cy, GRIGIO, 1.6)
    for x, (px, py) in pos.items():
        s += circle(px, py, r, col.get(x, "#fff7c2"), TESTO, 1.4)
        s += t(px, py + 5, x.key, 14, TESTO, "middle", True)
        if x in etich:
            s += t(px + r + 3, py - r + 2, etich[x], 13, ROSSO, "start", True)
    return s


AZZ, VERDINO, ROSA = "#d0e8f7", "#cfe8b8", "#fbc8c3"


def inorder_tree_walk():
    PSEUDO = [(0, "Inorder-Tree-Walk (x)"), (1, "if x≠NIL"), (2, "  then Inorder-Tree-Walk (left[x])"),
              (3, "       print key[x]"), (4, "       Inorder-Tree-Walk (right[x])")]
    an = Animazione("Inorder-Tree-Walk sull'albero di 09 p. 7", 820, 400, 0.9)
    radice = _N(5, _N(3, _N(2), _N(5)), _N(7, None, _N(8)))
    stampate, chiamate, pila = [], [0], []

    def scena(righe, x, nota):
        col = {y: ORDINATO for y in fatti}
        if x is not None:
            col[x] = EVID
        s = _disegna_albero(radice, col=col, etich={x: "x"} if x is not None else {})
        s += t(30, 300, "chiavi stampate: " + (" ".join(str(k) for k in stampate) or "—"), 15, VERDE, bold=True)
        s += t(30, 324, f"chiamate eseguite: {chiamate[0]}  ·  pila: " + (" → ".join(pila) or "—"), 13, TESTO)
        if nota:
            s += t(30, 346, nota, 13, GRIGIO)
        s += an.pseudocodice(PSEUDO, righe, 505, 90, 300, 21)
        return s

    fatti = set()

    def walk(x):
        chiamate[0] += 1
        if x is None:
            an.frame(scena({1}, None, "x = NIL: il test della riga 1 è falso, la chiamata termina"), f"chiamata n. {chiamate[0]} su NIL")
            return
        pila.append(str(x.key))
        an.frame(scena({1, 2}, x, f"x = {x.key}: prima tutto il sottoalbero sinistro"), f"chiamata n. {chiamate[0]} sul nodo {x.key}")
        walk(x.left)
        stampate.append(x.key)
        fatti.add(x)
        an.frame(scena({3}, x, f"sinistra finita: stampo {x.key}"), f"print {x.key}")
        walk(x.right)
        pila.pop()

    an.frame(scena(set(), None, "si invoca Inorder-Tree-Walk(root)"), "visita in ordine: sinistra → nodo → destra")
    walk(radice)
    an.frame(scena(set(), None, f"n = 6 nodi: {chiamate[0]} chiamate = 2n + 1 (una per nodo, una per ogni figlio NIL)"),
             "chiavi in ordine crescente: 2 3 5 5 7 8", 2.5)
    an.salva("animazione-inorder-tree-walk.svg")


ALBERO_SLIDE = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]


def tree_search():
    PSEUDO = [(0, "Tree-Search (x,k)"), (1, "if x=NIL or key[x]=k"), (2, "  then return x"),
              (3, "if k < key[x]"), (4, "  then return Tree-Search (left[x],k)"),
              (5, "  else return Tree-Search (right[x],k)")]
    an = Animazione("Tree-Search sull'albero di 09 p. 13: ricerca di 13 e di 11", 820, 440, 1.0)
    radice = _bst(ALBERO_SLIDE)

    def scena(righe, x, visti, k, nota, esito=None):
        col = {y: AZZ for y in visti}
        if x is not None:
            col[x] = VERDINO if esito == "trovato" else EVID
        s = _disegna_albero(radice, col=col, etich={x: "x"} if x is not None else {})
        s += t(30, 372, f"chiave cercata k = {k}  ·  nodi visitati: {len(visti) + (1 if x is not None else 0)}", 14, TESTO, bold=True)
        s += t(30, 394, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO, righe, 470, 90, 340, 21)
        return s

    for k in (13, 11):
        x, visti = radice, []
        an.frame(scena(set(), None, [], k, "si parte dalla radice"), f"Tree-Search(root, {k})")
        while True:
            if x is None:
                an.frame(scena({1, 2}, None, visti, k, "x = NIL: la chiave non c'è, si restituisce NIL"), f"{k} non trovato: return NIL", 1.8)
                break
            if x.key == k:
                an.frame(scena({1, 2}, x, visti, k, f"key[x] = {k}: trovato", "trovato"), f"{k} trovato dopo {len(visti) + 1} nodi", 1.8)
                break
            if k < x.key:
                an.frame(scena({1, 3, 4}, x, visti, k, f"{k} < {x.key}: si scende a sinistra"), f"x = {x.key}")
                visti.append(x); x = x.left
            else:
                an.frame(scena({1, 3, 5}, x, visti, k, f"{k} > {x.key}: si scende a destra"), f"x = {x.key}")
                visti.append(x); x = x.right
    an.salva("animazione-tree-search.svg")


def tree_minimum_maximum():
    PSEUDO = [(0, "Tree-Minimum (x)"), (1, "while left[x]≠NIL"), (2, "    do x ← left[x]"), (3, "return x"),
              (0, ""), (0, "Tree-Maximum (x)"), (4, "while right[x]≠NIL"), (5, "    do x ← right[x]"), (6, "return x")]
    an = Animazione("Tree-Minimum e Tree-Maximum sull'albero di 09 p. 13", 820, 430, 1.0)
    radice = _bst(ALBERO_SLIDE)

    def scena(righe, x, visti, nota, fine=False):
        col = {y: AZZ for y in visti}
        col[x] = VERDINO if fine else EVID
        s = _disegna_albero(radice, col=col, etich={x: "x"})
        s += t(30, 380, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO, righe, 500, 80, 300, 21)
        return s

    for nome, figlio, r_test, r_passo, r_ret in (("minimo", "left", 1, 2, 3), ("massimo", "right", 4, 5, 6)):
        x, visti = radice, []
        while getattr(x, figlio) is not None:
            an.frame(scena({r_test, r_passo}, x, visti, f"{figlio}[x] ≠ NIL: si scende"), f"{nome}: x = {x.key}")
            visti.append(x); x = getattr(x, figlio)
        an.frame(scena({r_test, r_ret}, x, visti, f"{figlio}[x] = NIL: x è il {nome}", True), f"{nome} = {x.key} dopo {len(visti)} passi", 1.8)
    an.salva("animazione-tree-minimum-maximum.svg")


def tree_successor():
    PSEUDO = [(0, "Tree-Successor (x)"), (1, "if right[x]≠NIL"), (2, "  then return Tree-Minimum(right[x])"),
              (3, "y ← p[x]"), (4, "while y≠NIL and x=right[y]"), (5, "    do x ← y"), (6, "       y ← p[y]"), (7, "return y")]
    an = Animazione("Tree-Successor sull'albero di 09 pp. 13–14: successori di 6 e di 13", 820, 430, 1.1)
    radice = _bst(ALBERO_SLIDE)

    def trova(k):
        x = radice
        while x.key != k:
            x = x.left if k < x.key else x.right
        return x

    def scena(righe, x, y, nota, ris=None, partenza=None):
        col, et = {}, {}
        if partenza is not None:
            col[partenza] = ROSA; et[partenza] = "nodo dato"
        if x is not None:
            col.setdefault(x, EVID); et[x] = "x" if x is not partenza else "nodo dato, x"
        if y is not None:
            col[y] = AZZ; et[y] = "y"
        if ris is not None:
            col[ris] = VERDINO; et[ris] = "successore"
        s = _disegna_albero(radice, col=col, etich=et)
        s += t(30, 380, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO, righe, 475, 90, 335, 21)
        return s

    z = trova(6)
    an.frame(scena({1}, z, None, "right[6] = 7 ≠ NIL: caso 1", partenza=z), "successore di 6")
    m = z.right
    while m.left is not None:
        m = m.left
    an.frame(scena({1, 2}, None, None, "il successore è il minimo del sottoalbero destro: 7", ris=m, partenza=z), "successore di 6 = 7 (slide p. 13)", 1.8)
    z = trova(13)
    x, y = z, z.p
    an.frame(scena({1, 3}, x, y, "right[13] = NIL: caso 2, si risale; y ← p[x] = 7", partenza=z), "successore di 13")
    while y is not None and x is y.right:
        an.frame(scena({4, 5, 6}, x, y, f"x = {x.key} è figlio destro di y = {y.key}: si sale ancora", partenza=z), f"x = {x.key}, y = {y.key}")
        x, y = y, y.p
    an.frame(scena({4, 7}, x, y, f"x = {x.key} è figlio sinistro di y = {y.key}: il ciclo si ferma", ris=y, partenza=z),
             "successore di 13 = 15 (slide p. 13)", 2.0)
    an.salva("animazione-tree-successor.svg")


def tree_insert():
    PSEUDO = [(0, "Tree-Insert (T,z)"), (1, "y ← NIL"), (2, "x ← root[T]"), (3, "while x≠NIL"), (4, "    do y ← x"),
              (5, "       if key[z] < key[x]"), (6, "          then x ← left[x]"), (7, "          else x ← right[x]"),
              (8, "p[z] ← y"), (9, "if y = NIL"), (10, "   then root[T] ← z"), (11, "   else if key[z] < key[y]"),
              (12, "      then left[y] ← z"), (13, "      else right[y] ← z")]
    an = Animazione("Tree-Insert: inserimento di 19 e poi di 10 (09 pp. 16–18)", 820, 460, 1.0)
    radice = _bst([15, 6, 18, 3, 7, 17, 20, 2, 4, 13])

    def scena(righe, x, y, k, nota, nuovo=None):
        col, et = {}, {}
        if y is not None:
            col[y] = AZZ; et[y] = "y"
        if x is not None:
            col[x] = EVID; et[x] = "x" if x is not y else "x, y"
        if nuovo is not None:
            col[nuovo] = VERDINO; et[nuovo] = "z"
        s = _disegna_albero(radice, col=col, etich=et, dy=58)
        s += t(30, 340, f"chiave da inserire: key[z] = {k}", 14, TESTO, bold=True)
        s += t(30, 362, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO, righe, 505, 62, 305, 20)
        return s

    for k in (19, 10):
        y, x = None, radice
        an.frame(scena({1, 2}, x, y, k, "y ← NIL, x ← radice"), f"Tree-Insert(T, {k})")
        while x is not None:
            y = x
            if k < x.key:
                an.frame(scena({3, 4, 5, 6}, x, y, k, f"{k} < {x.key}: x scende a sinistra"), f"y = {y.key}")
                x = x.left
            else:
                an.frame(scena({3, 4, 5, 7}, x, y, k, f"{k} ≥ {x.key}: x scende a destra"), f"y = {y.key}")
                x = x.right
        z = _N(k); z.p = y
        if k < y.key:
            y.left = z; lato, riga = "sinistro", 12
        else:
            y.right = z; lato, riga = "destro", 13
        an.frame(scena({3, 8, 9, 11, riga}, None, y, k, f"x = NIL: z diventa figlio {lato} di y = {y.key}", z),
                 f"{k} inserito come figlio {lato} di {y.key}", 1.8)
    an.salva("animazione-tree-insert.svg")


def tree_delete():
    PSEUDO = [(0, "Tree-Delete (T,z)"), (1, "if left[z]=NIL or right[z]=NIL"), (2, "  then y ← z"),
              (3, "  else y ← Tree-Successor (z)"), (4, "if left[y] ≠NIL"), (5, "  then x ← left[y]"),
              (6, "  else x ← right[y]"), (7, "if x ≠NIL"), (8, "  then p[x] ← p[y]"), (9, "if p[y] = NIL"),
              (10, "  then root[T] ← x"), (11, "  else if y = left[p[y]]"), (12, "     then left[p[y]] ← x"),
              (13, "     else right[p[y]] ← x"), (14, "if y ≠z"), (15, "  then key[z] ← key[y]"),
              (16, "  (copia i dati satellite di y in z)"), (17, "return y")]
    an = Animazione("Tree-Delete: i tre casi sull'albero di 09 pp. 19–21", 820, 500, 1.2)
    radice = [_bst([15, 6, 18, 3, 10, 17, 20, 2, 8, 13, 9])]

    def trova(k):
        x = radice[0]
        while x.key != k:
            x = x.left if k < x.key else x.right
        return x

    def scena(righe, z, y, x, nota):
        col, et = {}, {}
        for nodo, c, e in ((z, ROSA, "z"), (y, AZZ, "y"), (x, EVID, "x")):
            if nodo is not None:
                col.setdefault(nodo, c); et[nodo] = (et[nodo] + ", " + e) if nodo in et else e
        s = _disegna_albero(radice[0], col=col, etich=et, dy=60)
        s += t(30, 380, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO, righe, 505, 62, 305, 19)
        return s

    for k, caso in ((20, "caso z′: nessun figlio"), (3, "caso z″: un solo figlio"), (6, "caso z‴: due figli")):
        z = trova(k)
        an.frame(scena(set(), z, None, None, caso), f"Tree-Delete(T, {k})")
        if z.left is None or z.right is None:
            y = z
            an.frame(scena({1, 2}, z, y, None, "z ha al più un figlio: si taglia fuori z stesso (y ← z)"), f"{caso}: y = {y.key}")
        else:
            y = z.right
            while y.left is not None:
                y = y.left
            an.frame(scena({1, 3}, z, y, None, f"z ha due figli: y ← successore di z = {y.key}, che non ha figlio sinistro"), f"{caso}: y = {y.key}")
        x = y.left if y.left is not None else y.right
        an.frame(scena({4, 5} if y.left is not None else {4, 6}, z, y, x,
                       f"x ← l'unico figlio di y: {x.key if x else 'NIL'}"), "x = " + (str(x.key) if x else "NIL"))
        righe = {7, 9} | ({8} if x is not None else set())
        if y.p is None:
            righe |= {10}
        else:
            righe |= {11, 12 if y is y.p.left else 13}
        if x is not None:
            x.p = y.p
        if y.p is None:
            radice[0] = x
        elif y is y.p.left:
            y.p.left = x
        else:
            y.p.right = x
        if y is not z:
            z.key = y.key
            an.frame(scena(righe | {14, 15, 16, 17}, z, None, x, f"y tagliato fuori; key[z] ← key[y]: il nodo z ora contiene {z.key}"),
                     f"Delete({k}) completato: al posto di {k} c'è {z.key}", 2.0)
        else:
            an.frame(scena(righe | {14, 17}, None, None, x, f"y = z tagliato fuori: il padre punta a x = {x.key if x else 'NIL'}"),
                     f"Delete({k}) completato", 1.8)
    an.salva("animazione-tree-delete.svg")


def liste_di_adiacenza():
    an = Animazione("Costruzione delle liste di adiacenza con insert_edge (grafo di 08 p. 28)", 820, 420, 1.0)
    archi = [(1, 2), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5)]
    pos = {1: (90, 110), 2: (230, 110), 3: (300, 190), 4: (230, 260), 5: (90, 260)}
    liste = {v: [] for v in pos}
    grado = {v: 0 for v in pos}
    fatti = []

    def scena(nuovo, nota):
        s = ""
        for (a, b) in fatti:
            c = ROSSO if (a, b) == nuovo else GRIGIO
            s += line(*pos[a], *pos[b], c, 3 if (a, b) == nuovo else 1.8)
        for v, (x, y) in pos.items():
            s += circle(x, y, 17, "#ffffff", TESTO, 1.5) + t(x, y + 5, v, 14, TESTO, "middle", True)
        for i, v in enumerate(sorted(pos)):
            yy = 80 + i * 46
            s += rect(400, yy, 34, 30, fill="#ffffff", stroke=TESTO, sw=1.2, rx=2) + t(417, yy + 20, v, 13, TESTO, "middle", True)
            s += t(392, yy + 20, f"grado {grado[v]}", 11, GRIGIO, "end")
            xx = 450
            for k, w in enumerate(liste[v]):
                testa = nuovo is not None and k == 0 and v in nuovo
                s += line(xx - 16, yy + 15, xx, yy + 15, GRIGIO, 1.2, arrow=True)
                s += rect(xx, yy + 2, 30, 26, fill=EVID if testa else "#fdfdfd", stroke=TESTO, sw=1, rx=2)
                s += t(xx + 15, yy + 20, w, 13, TESTO, "middle")
                xx += 46
            s += t(xx - 8, yy + 20, "/", 13, GRIGIO)
        s += t(30, 330, f"archi inseriti: {len(fatti)}  ·  nodi di lista: {sum(len(l) for l in liste.values())} = 2m", 14, TESTO, bold=True)
        s += t(30, 352, nota, 13, TESTO)
        return s

    an.frame(scena(None, "initialize_graph: tutte le liste vuote, tutti i gradi a 0"), "grafo vuoto")
    for (a, b) in archi:
        fatti.append((a, b))
        liste[a].insert(0, b); grado[a] += 1
        liste[b].insert(0, a); grado[b] += 1
        an.frame(scena((a, b), f"insert_edge({a},{b}): {b} in testa alla lista di {a} e, non orientato, {a} in testa a quella di {b}"),
                 f"arco ({a},{b})")
    an.frame(scena(None, "spazio: n celle dell'array + 2m nodi di lista = Θ(n + m)"), "7 archi, 14 nodi di lista", 2.5)
    an.salva("animazione-liste-di-adiacenza.svg")

if __name__ == "__main__":
    inorder_tree_walk()
    tree_search()
    tree_minimum_maximum()
    tree_successor()
    tree_insert()
    tree_delete()
    liste_di_adiacenza()
    merge()
    merge_sort()
    partition()
    quicksort()
    quicksort_randomizzato()
    torre_di_hanoi()
    nuts_and_bolts()
    nuts_and_bolts_quadratico()
    insertion_sort()
    selection_sort()
    findmatch()
    potenza_veloce()
    somma_iterativa()
    somma_ricorsiva()
    nearest_neighbor()
    closest_pair()
    optimal_tsp()
    earliest_job_first()
    shortest_job_first()
    optimal_scheduling()
    exhaustive_scheduling()
