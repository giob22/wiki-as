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


# =================================================================== HEAP (lezione 10)
def _heap_scena(A, size, col=None, etich=None, ordinati=0, x0=20, w=470, y_arr=62, y_tree=150, dy=62):
    """Array (in alto) e albero binario completo (sotto) di un heap; A e' una lista 0-based, size = heap-size[A].
    Le celle oltre heap-size sono grigie, o verdi se `ordinati` le dichiara gia' al loro posto (Heap-Sort)."""
    n = len(A)
    col, etich = col or {}, etich or {}
    cw = min(44, w / n)
    s = ""
    for i in range(1, n + 1):
        x = x0 + (i - 1) * cw
        fuori = i > size
        f = ORDINATO if (fuori and i > n - ordinati) else ("#eeeeee" if fuori else col.get(i, "#ffffff"))
        v = A[i - 1]
        s += rect(x, y_arr, cw, 34, fill=f, stroke=TESTO, sw=1.3, rx=0)
        s += t(x + cw / 2, y_arr + 23, "−∞" if v is None else v, 17, GRIGIO if (fuori and not ordinati) else TESTO, "middle", True)
        s += t(x + cw / 2, y_arr - 6, i, 11, GRIGIO, "middle")
    pos = {}
    for i in range(1, size + 1):
        d = i.bit_length() - 1
        k = i - (1 << d)
        pos[i] = (x0 + w * (k + 0.5) / (1 << d), y_tree + d * dy)
    for i in range(2, size + 1):
        (px, py), (cx, cy) = pos[i // 2], pos[i]
        s += line(px, py, cx, cy, GRIGIO, 1.6)
    for i, (px, py) in pos.items():
        v = A[i - 1]
        s += circle(px, py, 17, col.get(i, "#d0e8f7"), TESTO, 1.4)
        s += t(px, py + 5, "−∞" if v is None else v, 14, TESTO, "middle", True)
        s += t(px - 25, py - 13, i, 10, GRIGIO, "middle")
        if i in etich:
            s += t(px + 20, py - 13, etich[i], 13, ROSSO, "start", True)
    return s


def _heapify_eventi(A, size, i, out):
    """Esegue Max-Heapify(A,i) su A (lista 0-based, modificata sul posto) registrando gli eventi con una copia di A."""
    l, r, largest = 2 * i, 2 * i + 1, i
    out.append(("avvio", i, l, r, i, list(A)))
    if l <= size and A[l - 1] > A[largest - 1]:
        largest = l
    if r <= size and A[r - 1] > A[largest - 1]:
        largest = r
    out.append(("scelta", i, l, r, largest, list(A)))
    if largest != i:
        A[i - 1], A[largest - 1] = A[largest - 1], A[i - 1]
        out.append(("scambio", i, l, r, largest, list(A)))
        _heapify_eventi(A, size, largest, out)
    else:
        out.append(("fine", i, l, r, largest, list(A)))


PSEUDO_MAXHEAPIFY = [(0, "Max-Heapify (A,i)"), (1, "l ← Left(i)"), (2, "r ← Right(i)"), (3, "largest ← i"),
                     (4, "if l≤heap-size[A] and A[l]>A[largest]"), (5, "   largest ← l"),
                     (6, "if r≤heap-size[A] and A[r]>A[largest]"), (7, "   largest ← r"),
                     (8, "if largest≠i"), (9, "   exchange A[i]↔A[largest]"), (10, "   Max-Heapify (A,largest)")]


def _scena_heapify(an, ev, size, pseudo, px=520, ordinati=0, base=None):
    tipo, i, l, r, largest, A = ev
    col = dict(base or {})
    col[i] = EVID
    et = {i: "i"}
    if tipo in ("scelta", "scambio", "fine"):
        for k, nome in ((l, "l"), (r, "r")):
            if k <= size:
                et[k] = nome
        if largest != i or tipo == "scelta":
            col[largest] = VERDINO
            et[largest] = "largest" if largest not in (l, r) else et.get(largest, "") + "=largest"
    righe = {"avvio": {1, 2, 3}, "scelta": {4, 5, 6, 7}, "scambio": {8, 9}, "fine": {8}}[tipo]
    s = _heap_scena(A, size, col, et, ordinati)
    s += an.pseudocodice(pseudo, righe, px, 90, 340, 21)
    return s


def max_heapify():
    an = Animazione("Max-Heapify (A,2) sull'heap di 10 p. 7 (heap-size = 10)", 870, 440, 1.1)
    A, size = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1], 10
    eventi = []
    _heapify_eventi(A, size, 2, eventi)
    testi = {"avvio": "righe 1–3: l ← Left(i), r ← Right(i), largest ← i",
             "scelta": "righe 4–7: si confronta A[i] con i due figli; largest è l'indice del massimo fra tre",
             "scambio": "righe 8–9: largest ≠ i, si scambiano A[i] e A[largest]; riga 10: si richiama Max-Heapify sul figlio",
             "fine": "riga 8 falsa: A[i] è già il massimo fra tre, non si scambia e la ricorsione termina"}
    for ev in eventi:
        tipo, i, l, r, largest, Ac = ev
        extra = ""
        if tipo == "scelta":
            vals = [f"A[{k}]={Ac[k - 1]}" for k in (i, l, r) if k <= size]
            extra = " · " + ", ".join(vals) + f" → largest = {largest}"
        s = _scena_heapify(an, ev, size, PSEUDO_MAXHEAPIFY)
        s += t(20, 374, testi[tipo] + extra, 12, TESTO)
        an.frame(s, f"Max-Heapify(A,{i}): {tipo}")
    fin = eventi[-1][5]
    s = _heap_scena(fin, size) + an.pseudocodice(PSEUDO_MAXHEAPIFY, set(), 520, 90, 340, 21)
    s += t(20, 374, "3 chiamate (i = 2, 4, 9): l'elemento 4 è sceso di due livelli fino a diventare foglia", 12, TESTO)
    an.frame(s, "il sottoalbero di radice 2 è di nuovo un max-heap (10 p. 10)", 2.5)
    an.salva("animazione-max-heapify.svg")


PSEUDO_BUILD = [(0, "Build-Max-Heap (A)"), (1, "heap-size[A] ← length[A]"), (2, "for i ← ⌊length[A]/2⌋ downto 1"),
                (3, "   Max-Heapify (A,i)")]


def build_max_heap():
    an = Animazione("Build-Max-Heap sull'array di 10 p. 15", 870, 440, 1.0)
    A, size = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7], 10
    an.frame(_heap_scena(A, size) + an.pseudocodice(PSEUDO_BUILD, set(), 520, 90, 340, 21)
             + t(20, 374, "array arbitrario: i nodi 6..10 sono foglie, cioè heap di un solo elemento (nessun lavoro)", 12, TESTO),
             "array di partenza ⟨4, 1, 3, 2, 16, 9, 10, 14, 8, 7⟩")
    for i in range(size // 2, 0, -1):
        eventi = []
        _heapify_eventi(A, size, i, eventi)
        fatti = {k: ORDINATO for k in range(i, size + 1)}
        s = _heap_scena(eventi[0][5], size, {**fatti, i: EVID}, {i: "i"}) + an.pseudocodice(PSEUDO_BUILD, {2, 3}, 520, 90, 340, 21)
        s += t(20, 374, f"i = {i}: si invoca Max-Heapify (A,{i}); i nodi in verde sono già radici di max-heap (invariante)", 12, TESTO)
        an.frame(s, f"ciclo for: i = {i}")
        for ev in eventi:
            if ev[0] == "scambio":
                _, j, l, r, largest, Ac = ev
                s = _heap_scena(Ac, size, {**fatti, largest: EVID}, {largest: "scambiato"}) + an.pseudocodice(PSEUDO_BUILD, {3}, 520, 90, 340, 21)
                s += t(20, 374, f"dentro Max-Heapify: A[{j}] e A[{largest}] scambiati, la chiave scende di un livello", 12, TESTO)
                an.frame(s, f"scambio dentro Max-Heapify (A,{j})")
    s = _heap_scena(A, size, {k: ORDINATO for k in range(1, size + 1)}) + an.pseudocodice(PSEUDO_BUILD, set(), 520, 90, 340, 21)
    s += t(20, 374, "i = 0: il nodo 1 è radice di max-heap, quindi l'array è un max-heap (10 p. 19)", 12, TESTO)
    an.frame(s, "max-heap ottenuto: ⟨16, 14, 10, 8, 7, 9, 3, 2, 4, 1⟩", 2.5)
    an.salva("animazione-build-max-heap.svg")


PSEUDO_HEAPSORT = [(0, "Heap-Sort (A)"), (1, "Build-Max-Heap (A)"), (2, "for i ← length[A] downto 2"),
                   (3, "   exchange A[1]↔A[i]"), (4, "   heap-size[A] ← heap-size[A]-1"), (5, "   Max-Heapify (A,1)")]


def heapsort():
    an = Animazione("Heap-Sort sull'array di 10 p. 15 (dall'heap di p. 23 in poi come nelle slide)", 870, 440, 1.0)
    A, n = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7], 10
    an.frame(_heap_scena(A, n) + an.pseudocodice(PSEUDO_HEAPSORT, set(), 520, 90, 340, 21)
             + t(20, 374, "array di partenza", 12, TESTO), "array di partenza")
    ev = []
    for i in range(n // 2, 0, -1):
        _heapify_eventi(A, n, i, ev)
    an.frame(_heap_scena(A, n) + an.pseudocodice(PSEUDO_HEAPSORT, {1}, 520, 90, 340, 21)
             + t(20, 374, "riga 1: Build-Max-Heap rende l'array un max-heap; il massimo 16 è in A[1]", 12, TESTO), "dopo Build-Max-Heap (10 p. 23)")
    size = n
    for i in range(n, 1, -1):
        A[0], A[i - 1] = A[i - 1], A[0]
        size -= 1
        an.frame(_heap_scena(A, size, {1: EVID}, {1: "radice"}, ordinati=n - size) + an.pseudocodice(PSEUDO_HEAPSORT, {3, 4}, 520, 90, 340, 21)
                 + t(20, 374, f"righe 3–4: A[1] ↔ A[{i}] → il massimo {A[i - 1]} è al suo posto; heap-size = {size}", 12, TESTO),
                 f"i = {i}: scambio e heap-size = {size}")
        eventi = []
        _heapify_eventi(A, size, 1, eventi)
        A = list(eventi[-1][5])
        an.frame(_heap_scena(A, size, ordinati=n - size) + an.pseudocodice(PSEUDO_HEAPSORT, {5}, 520, 90, 340, 21)
                 + t(20, 374, f"riga 5: Max-Heapify (A,1) fa scendere la radice ({sum(1 for e in eventi if e[0] == 'scambio')} scambi) e ripristina il max-heap", 12, TESTO),
                 f"dopo Max-Heapify (A,1), heap-size = {size}")
    an.frame(_heap_scena(A, 1, {1: ORDINATO}, ordinati=n - 1) + an.pseudocodice(PSEUDO_HEAPSORT, set(), 520, 90, 340, 21)
             + t(20, 374, "rimane un solo elemento: l'algoritmo termina, l'array è ordinato (10 p. 40)", 12, TESTO),
             "array ordinato ⟨1, 2, 3, 4, 7, 8, 9, 10, 14, 16⟩", 2.5)
    an.salva("animazione-heapsort.svg")


PSEUDO_EXTRACT = [(0, "Heap-Extract-Max (A)"), (1, "if heap-size[A]<1"), (2, '   error "heap empty"'), (3, "max ← A[1]"),
                  (4, "A[1] ← A[heap-size[A]]"), (5, "heap-size[A] ← heap-size[A]-1"), (6, "Max-Heapify (A,1)"),
                  (7, "return max")]


def heap_extract_max():
    an = Animazione("Heap-Extract-Max sull'heap di 10 p. 6 (istanza mia)", 870, 440, 1.0)
    A, size = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1], 10
    an.frame(_heap_scena(A, size) + an.pseudocodice(PSEUDO_EXTRACT, set(), 520, 90, 340, 21)
             + t(20, 374, "max-heap di partenza; Heap-Maximum restituirebbe A[1] = 16 in Θ(1)", 12, TESTO), "heap di partenza")
    massimo = A[0]
    an.frame(_heap_scena(A, size, {1: EVID}, {1: "max"}) + an.pseudocodice(PSEUDO_EXTRACT, {3}, 520, 90, 340, 21)
             + t(20, 374, f"riga 3: max ← A[1] = {massimo}", 12, TESTO), "si memorizza il massimo")
    A[0] = A[size - 1]
    size -= 1
    an.frame(_heap_scena(A, size, {1: EVID}, {1: "nuova radice"}) + an.pseudocodice(PSEUDO_EXTRACT, {4, 5}, 520, 90, 340, 21)
             + t(20, 374, f"righe 4–5: l'ultimo elemento ({A[0]}) va al posto della radice, heap-size = {size}: ora la radice viola la proprietà", 12, TESTO),
             "l'ultimo elemento sale in radice")
    eventi = []
    _heapify_eventi(A, size, 1, eventi)
    for ev in eventi:
        if ev[0] == "scambio":
            _, j, l, r, largest, Ac = ev
            an.frame(_heap_scena(Ac, size, {largest: EVID}, {largest: "scambiato"}) + an.pseudocodice(PSEUDO_EXTRACT, {6}, 520, 90, 340, 21)
                     + t(20, 374, f"riga 6: dentro Max-Heapify, A[{j}] ↔ A[{largest}]: la chiave scende di un livello", 12, TESTO),
                     f"scambio A[{j}] ↔ A[{largest}]")
    A = list(eventi[-1][5])
    an.frame(_heap_scena(A, size) + an.pseudocodice(PSEUDO_EXTRACT, {7}, 520, 90, 340, 21)
             + t(20, 374, f"riga 7: return {massimo}; l'heap ha {size} elementi ed è di nuovo un max-heap", 12, TESTO),
             f"restituito {massimo}; una sola invocazione di Max-Heapify: O(lg n)", 2.5)
    an.salva("animazione-heap-extract-max.svg")


PSEUDO_INCKEY = [(0, "Heap-Increase-Key (A,i,key)"), (1, "if key<A[i]"), (2, '   error "new key is smaller"'),
                 (3, "A[i] ← key"), (4, "while i>1 and A[Parent(i)]<A[i]"), (5, "   exchange A[i]↔A[Parent(i)]"),
                 (6, "   i ← Parent(i)")]


def heap_increase_key():
    an = Animazione("Heap-Increase-Key (A,9,15) sull'heap di 10 p. 45", 870, 440, 1.1)
    A, size = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1], 10
    i, key = 9, 15
    an.frame(_heap_scena(A, size, {i: EVID}, {i: "i"}) + an.pseudocodice(PSEUDO_INCKEY, {1}, 520, 90, 340, 21)
             + t(20, 374, f"riga 1: key = {key} ≥ A[{i}] = {A[i - 1]}, l'errore non scatta", 12, TESTO), "max-heap di partenza")
    A[i - 1] = key
    an.frame(_heap_scena(A, size, {i: EVID}, {i: "i"}) + an.pseudocodice(PSEUDO_INCKEY, {3}, 520, 90, 340, 21)
             + t(20, 374, f"riga 3: A[{i}] ← {key} (10 p. 46): il padre {A[i // 2 - 1]} è minore, l'heap non è più valido", 12, TESTO), "la chiave 4 diventa 15")
    while i > 1 and A[i // 2 - 1] < A[i - 1]:
        p = i // 2
        A[i - 1], A[p - 1] = A[p - 1], A[i - 1]
        an.frame(_heap_scena(A, size, {p: EVID}, {p: "i"}) + an.pseudocodice(PSEUDO_INCKEY, {4, 5, 6}, 520, 90, 340, 21)
                 + t(20, 374, f"righe 4–6: A[{i}] ↔ A[{p}] e i ← {p}" + (" (10 p. 47)" if i == 9 else ""), 12, TESTO), f"scambio con il padre: i = {p}")
        i = p
    an.frame(_heap_scena(A, size, {i: ORDINATO}, {i: "i"}) + an.pseudocodice(PSEUDO_INCKEY, {4}, 520, 90, 340, 21)
             + t(20, 374, f"riga 4 falsa: A[Parent({i})] = {A[i // 2 - 1]} ≥ {A[i - 1]}; i scambi ≤ altezza = O(lg n)", 12, TESTO),
             "max-heap ripristinato", 2.5)
    an.salva("animazione-heap-increase-key.svg")


PSEUDO_INSERT = [(0, "Max-Heap-Insert (A,key)"), (1, "heap-size[A] ← heap-size[A]+1"), (2, "A[heap-size[A]] ← −∞"),
                 (3, "Heap-Increase-Key (A,heap-size[A],key)")]


def max_heap_insert():
    an = Animazione("Max-Heap-Insert (A,15) sull'heap di 10 p. 6 (istanza mia)", 870, 440, 1.0)
    A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1, None]
    size = 10
    an.frame(_heap_scena(A[:10], 10) + an.pseudocodice(PSEUDO_INSERT, set(), 520, 90, 340, 21)
             + t(20, 374, "max-heap di partenza con 10 elementi", 12, TESTO), "heap di partenza")
    size = 11
    an.frame(_heap_scena(A, size, {11: EVID}, {11: "nuovo"}) + an.pseudocodice(PSEUDO_INSERT, {1, 2}, 520, 90, 340, 21)
             + t(20, 374, "righe 1–2: heap-size = 11 e A[11] ← −∞ (non viola nulla: −∞ è minore di ogni chiave)", 12, TESTO),
             "si aggiunge una foglia con chiave −∞")
    i, key = 11, 15
    A[i - 1] = key
    an.frame(_heap_scena(A, size, {i: EVID}, {i: "i"}) + an.pseudocodice(PSEUDO_INSERT, {3}, 520, 90, 340, 21)
             + t(20, 374, "riga 3: Heap-Increase-Key (A,11,15) imposta A[11] ← 15", 12, TESTO), "la chiave −∞ viene portata a 15")
    while i > 1 and A[i // 2 - 1] < A[i - 1]:
        p = i // 2
        A[i - 1], A[p - 1] = A[p - 1], A[i - 1]
        an.frame(_heap_scena(A, size, {p: EVID}, {p: "i"}) + an.pseudocodice(PSEUDO_INSERT, {3}, 520, 90, 340, 21)
                 + t(20, 374, f"dentro Heap-Increase-Key: A[{i}] ↔ A[{p}] e i ← {p}", 12, TESTO), f"15 sale al livello del nodo {p}")
        i = p
    an.frame(_heap_scena(A, size, {i: ORDINATO}, {i: "i"}) + an.pseudocodice(PSEUDO_INSERT, set(), 520, 90, 340, 21)
             + t(20, 374, f"A[Parent({i})] = {A[i // 2 - 1]} ≥ 15: il nuovo elemento è a posto; una sola invocazione di Heap-Increase-Key: O(lg n)", 12, TESTO),
             "max-heap con 11 elementi", 2.5)
    an.salva("animazione-max-heap-insert.svg")


# =================================================================== ALBERI ROSSO-NERI (lezione 11)
ROSSO_RB, NERO_RB = "#d9443a", "#1f2d33"


class _R:
    def __init__(self, key, rosso=False, left=None, right=None):
        self.key, self.rosso, self.left, self.right, self.p = key, rosso, left, right, None
        for c in (left, right):
            if c is not None:
                c.p = self


def _rb(spec, padre=None):
    """Costruisce un albero da (chiave, 'R'|'B', sinistro, destro); None = NIL."""
    if spec is None:
        return None
    n = _R(spec[0], spec[1] == "R")
    n.p = padre
    n.left, n.right = _rb(spec[2], n), _rb(spec[3], n)
    return n


def _rb_nodi(x, out=None):
    out = [] if out is None else out
    if x is not None:
        _rb_nodi(x.left, out)
        out.append(x)
        _rb_nodi(x.right, out)
    return out


def _rb_pos(root, x0=25, y0=62, w=470, dy=58):
    """Ascissa = rango nella visita in ordine, ordinata = profondita'."""
    pos = {}

    def visita(x, d, k):
        if x is None:
            return k
        k = visita(x.left, d + 1, k)
        pos[x] = (x0 + (k + 0.5) * w / n, y0 + d * dy)
        return visita(x.right, d + 1, k + 1)

    n = max(len(_rb_nodi(root)), 1)
    visita(root, 0, 0)
    return pos


def _rb_archi(nodi):
    return {(a, a.left) for a in nodi if a.left is not None} | {(a, a.right) for a in nodi if a.right is not None}


def _rb_disegna(nodi, pos, archi, nuovi=(), vecchi=(), evid=None, etich=None, r=16):
    evid, etich = evid or {}, etich or {}
    s = ""
    for (a, b) in vecchi:
        s += line(*pos[a], *pos[b], GRIGIO, 1.4, dash="4,3")
    for (a, b) in archi:
        nuovo = (a, b) in nuovi
        s += line(*pos[a], *pos[b], ROSSO if nuovo else GRIGIO, 3 if nuovo else 1.7)
    for x in nodi:
        px, py = pos[x]
        st = evid.get(x)
        s += circle(px, py, r, ROSSO_RB if x.rosso else NERO_RB, st or "#555", 3.5 if st else 1.3)
        s += t(px, py + 5, x.key, 13, "#ffffff", "middle", True)
        if x in etich:
            s += t(px + r + 2, py - r + 3, etich[x], 13, BLU, "start", True)
    return s


def _rb_ruota_sx(x):
    """Left-Rotate sugli oggetti _R, restituisce y e gli stati (nodi, archi) dopo ciascuna operazione."""
    y = x.right
    stati = []
    x.right = y.left                                   # operazione 1
    if y.left is not None:
        y.left.p = x
    stati.append(1)
    y.p = x.p                                          # operazione 2
    if x.p is None:
        pass
    elif x is x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    stati.append(2)
    y.left = x                                         # operazione 3
    x.p = y
    stati.append(3)
    return y


PSEUDO_LR = [(0, "Left-Rotate (T,x)"), (1, "y ← right[x]"), (0, "// operazione 1."), (2, "right[x] ← left[y]"),
             (3, "if left[y] ≠ nil[T]"), (4, "   then p[left[y]] ← x"), (0, "// operazione 2."), (5, "p[y] ← p[x]"),
             (6, "if p[x] = nil[T]"), (7, "   then root[T] ← y"), (8, "   else if x = left[p[x]]"),
             (9, "      then left[p[x]] ← y"), (10, "      else right[p[x]] ← y"), (0, "// operazione 3."),
             (11, "left[y] ← x"), (12, "p[x] ← y")]


def left_rotate():
    an = Animazione("Left-Rotate (T,11) sull'albero di 11 p. 20", 880, 470, 1.2)
    spec = (7, "B", (4, "B", (3, "B", (2, "B", None, None), None), (6, "B", None, None)),
            (11, "B", (9, "B", None, None), (18, "B", (14, "B", (12, "B", None, None), (17, "B", None, None)),
                                             (19, "B", None, (22, "B", None, None)))))
    root = _rb(spec)
    nodi = _rb_nodi(root)
    pos = _rb_pos(root, w=430)
    x = next(n for n in nodi if n.key == 11)
    y = x.right
    beta = y.left
    note_ev = {x: ARANCIO, y: BLU}
    et = {x: "x", y: "y"}

    def frame(righe, nota, cap, archi_prima, archi_dopo, evid=None, pos_=None):
        nuovi = archi_dopo - archi_prima
        vecchi = archi_prima - archi_dopo
        s = _rb_disegna(nodi, pos_ or pos, archi_dopo, nuovi, vecchi, evid or note_ev, et)
        s += t(20, 394, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO_LR, righe, 510, 80, 360, 21)
        an.frame(s, cap)

    a0 = _rb_archi(nodi)
    frame(set(), "x = 11 e y = right[x] = 18; il sottoalbero β è left[y] (radice 14)", "Left-Rotate (T,x) con x = 11", a0, a0)
    # operazione 1
    x.right = y.left
    if y.left is not None:
        y.left.p = x
    a1 = _rb_archi(nodi)
    frame({2, 3, 4}, "operazione 1: β (radice 14) diventa figlio destro di x", "operazione 1: β diventa figlio destro di x", a0, a1)
    # operazione 2
    y.p = x.p
    if x.p is None:
        pass
    elif x is x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    a2 = _rb_archi(nodi)
    frame({5, 6, 8, 10}, "operazione 2: il padre di x (il nodo 7) diventa il padre di y (riga 10: x è figlio destro)", "operazione 2: p[y] ← p[x]", a1, a2)
    # operazione 3
    y.left = x
    x.p = y
    a3 = _rb_archi(nodi)
    frame({11, 12}, "operazione 3: x diventa figlio sinistro di y", "operazione 3: x diventa figlio sinistro di y", a2, a3)
    nuova_pos = _rb_pos(y.p if y.p else y, w=430)
    # ridisegno con il layout del nuovo albero
    radice = root
    s = _rb_disegna(nodi, _rb_pos(radice, w=430), a3, set(), set(), note_ev, et)
    s += t(20, 394, "Left-Rotate è completata: ordine BST invariato (9 ≤ 11 ≤ 14 ≤ 18), tempo O(1)", 13, TESTO)
    s += an.pseudocodice(PSEUDO_LR, set(), 510, 80, 360, 21)
    an.frame(s, "albero ruotato (11 p. 20, in basso)", 2.5)
    an.salva("animazione-left-rotate.svg")


PSEUDO_RBFIX = [(0, "RB-Insert-Fixup (T,z)"), (1, "while color[p[z]] = RED"), (2, "  do if p[z] = left[p[p[z]]]"),
                (3, "      then y ← right[p[p[z]]]   // zio"), (4, "        if color[y] = RED"),
                (5, "          then color[p[z]] ← BLACK"), (6, "               color[y] ← BLACK"),
                (7, "               color[p[p[z]]] ← RED"), (8, "               z ← p[p[z]]"),
                (9, "          else if z = right[p[z]]"), (10, "                 then z ← p[z]"),
                (11, "                      Left-Rotate (T,z)"), (12, "               color[p[z]] ← BLACK"),
                (13, "               color[p[p[z]]] ← RED"), (14, "               Right-Rotate (T,p[p[z]])"),
                (15, "      else (simmetrico: left ↔ right)"), (16, "color[root[T]] ← BLACK")]

SPEC_P37 = (11, "B", (2, "R", (1, "B", None, None), (7, "B", (5, "R", None, None), (8, "R", None, None))),
            (14, "B", None, (15, "R", None, None)))


def rb_insert():
    an = Animazione("RB-Insert (T,4) sull'albero rosso-nero di 11 p. 37", 880, 480, 1.2)
    radice = _rb(SPEC_P37)

    def scena(righe, nota, evid=None, etich=None, w=440):
        nodi = _rb_nodi(radice)
        s = _rb_disegna(nodi, _rb_pos(radice, w=w, dy=56), _rb_archi(nodi), set(), set(), evid, etich, 15)
        s += t(20, 402, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO_RBFIX, righe, 500, 62, 372, 19)
        return s

    an.frame(scena(set(), "albero di partenza: radice nera, nessun rosso con figli rossi, 2 nodi neri su ogni percorso"),
             "albero rosso-nero iniziale (11 p. 37, senza z)")
    # RB-Insert: inserimento come in Tree-Insert, z rosso
    def nodo(k):
        return next(n for n in _rb_nodi(radice) if n.key == k)
    cinque = nodo(5)
    z = _R(4, True)
    z.p = cinque
    cinque.left = z
    an.frame(scena({0}, "RB-Insert: 4 scende 11 → 2 → 7 → 5, diventa figlio sinistro di 5 ed è colorato di ROSSO: z e p[z] sono rossi (violazione di tipo 4)",
                   {z: ARANCIO}, {z: "z"}), "RB-Insert: z = 4 rosso, figlio di 5 (rosso)")
    # caso 1: zio rosso
    y = cinque.p.right
    assert y.key == 8 and y.rosso
    cinque.rosso = False
    y.rosso = False
    cinque.p.rosso = True
    z = cinque.p
    an.frame(scena({1, 2, 3, 4, 5, 6, 7, 8}, "caso 1: lo zio y = 8 è rosso → p[z] = 5 e y diventano neri, il nonno 7 diventa rosso, z ← 7",
                   {z: ARANCIO, y: BLU}, {z: "z", y: "y"}), "caso 1 (zio rosso): ricolorazione, z sale di due livelli")
    # seconda iterazione: z = 7, p[z] = 2 rosso, zio 14 nero, z figlio destro: caso 2
    zio = z.p.p.right
    assert z.p.rosso and not zio.rosso and z is z.p.right
    an.frame(scena({1, 2, 3, 4, 9}, "iterazione 2: p[z] = 2 è rosso (violazione di tipo 4), lo zio y = 14 è nero e z è figlio destro → caso 2",
                   {z: ARANCIO, zio: BLU}, {z: "z", zio: "y"}), "p[z] rosso: lo zio è nero e z è figlio destro")
    z = z.p
    rad_prima = radice
    # Left-Rotate (T, z=2)
    y_ = z.right
    z.right = y_.left
    if y_.left is not None:
        y_.left.p = z
    y_.p = z.p
    if z.p is None:
        radice = y_
    elif z is z.p.left:
        z.p.left = y_
    else:
        z.p.right = y_
    y_.left = z
    z.p = y_
    an.frame(scena({10, 11}, "caso 2: z ← p[z] = 2 e Left-Rotate su z: 7 sale sopra 2; si passa al caso 3 con z = 2 (figlio sinistro di p[z] = 7)",
                   {z: ARANCIO, zio: BLU}, {z: "z", zio: "y"}), "caso 2: Left-Rotate su z = 2")
    # caso 3
    z.p.rosso = False
    nonno = z.p.p
    nonno.rosso = True
    # Right-Rotate (T, p[p[z]]) = (T, 11)
    x_ = nonno.left
    nonno.left = x_.right
    if x_.right is not None:
        x_.right.p = nonno
    x_.p = nonno.p
    if nonno.p is None:
        radice = x_
    elif nonno is nonno.p.right:
        nonno.p.right = x_
    else:
        nonno.p.left = x_
    x_.right = nonno
    nonno.p = x_
    an.frame(scena({12, 13, 14}, "caso 3: p[z] = 7 diventa nero, il nonno 11 diventa rosso e Right-Rotate su 11: 7 è la nuova radice (11 p. 40)",
                   {z: ARANCIO, zio: BLU}, {z: "z", zio: "y"}), "caso 3: ricolorazione e Right-Rotate su p[p[z]]")
    radice.rosso = False
    an.frame(scena({16}, "p[z] = 7 è nero: il ciclo termina. Riga 16: la radice è già nera. Proprietà 1–5 valide, altezza nera 2, 2 rotazioni, 3 iterazioni",
                   {}, {}), "albero rosso-nero finale", 2.8)
    an.salva("animazione-rb-insert.svg")


PSEUDO_RBDEL = [(1, "Caso I: foglia rossa"), (2, "  si toglie, nulla cambia"), (3, "Caso II: nero con un figlio rosso"),
                (4, "  il figlio lo sostituisce → nero"), (5, "Caso III: due figli"), (6, "  successore tagliato, chiave copiata"),
                (7, "Foglia nera tolta → RB-Delete-Fixup")]

SPEC_P45 = (15, "B", (6, "R", (3, "B", (2, "R", None, None), (4, "R", None, None)), (7, "B", None, (13, "R", None, None))),
            (18, "R", (17, "B", None, None), (20, "B", (19, "R", None, None), None)))


def rb_delete():
    an = Animazione("Cancellazione in un albero rosso-nero: i tre casi di 11 pp. 45–47", 880, 470, 1.3)

    def scena(radice, righe, nota, evid=None, etich=None):
        nodi = _rb_nodi(radice)
        s = _rb_disegna(nodi, _rb_pos(radice, w=450, dy=60), _rb_archi(nodi), set(), set(), evid, etich, 16)
        s += t(20, 398, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO_RBDEL, righe, 520, 80, 340, 22)
        return s

    def cerca(radice, k):
        return next(n for n in _rb_nodi(radice) if n.key == k)

    r = _rb(SPEC_P45)
    an.frame(scena(r, set(), "albero rosso-nero iniziale (11 p. 45): 15 nero; rossi 6, 18, 2, 4, 13, 19"), "albero di partenza")
    # Caso I: z = 19
    r = _rb(SPEC_P45)
    z = cerca(r, 19)
    an.frame(scena(r, {1}, "Caso I: z = 19 è una foglia rossa", {z: ARANCIO}, {z: "z"}), "Caso I: si elimina la foglia rossa 19")
    z.p.left = None
    an.frame(scena(r, {1, 2}, "19 tolta: non cambia la black-height, nessun rosso consecutivo, radice nera → ancora rosso-nero"), "Caso I: albero ancora rosso-nero")
    # Caso II: z = 20 (nero), figlio 19 rosso
    r = _rb(SPEC_P45)
    z = cerca(r, 20)
    an.frame(scena(r, {3}, "Caso II: z = 20 è nero e ha un solo figlio (19, rosso)", {z: ARANCIO, z.left: BLU}, {z: "z", z.left: "figlio"}),
             "Caso II: si elimina il nero 20 con un solo figlio")
    figlio = z.left
    figlio.p = z.p
    z.p.right = figlio
    figlio.rosso = False
    an.frame(scena(r, {3, 4}, "il figlio 19 prende il posto di 20 ed è colorato di nero: la black-height dei cammini è invariata"), "Caso II: 19 diventa nero al posto di 20")
    # Caso III: z = 18 (rosso, due figli): successore 19
    r = _rb(SPEC_P45)
    z = cerca(r, 18)
    y = z.right
    while y.left is not None:
        y = y.left
    an.frame(scena(r, {5}, "Caso III: z = 18 ha due figli; il successore y = 19 (minimo del sottoalbero destro) ha al massimo un figlio",
                   {z: ARANCIO, y: BLU}, {z: "z", y: "y"}), "Caso III: due figli, successore 19")
    y.p.left = None
    z.key = y.key
    an.frame(scena(r, {5, 6}, "si taglia y = 19 (foglia rossa: nulla da correggere) e se ne copia la chiave in z: il nodo rosso in posizione di 18 ora contiene 19",
                   {z: ARANCIO}, {z: "z"}), "Caso III: chiave 19 copiata in z, foglia 19 tolta")
    an.frame(scena(r, {7}, "Rimane il caso di una foglia NERA tolta: la black-height scende sui suoi cammini e serve RB-Delete-Fixup (non sviluppato nelle slide)"),
             "caso della foglia nera: richiede RB-Delete-Fixup, O(h) = O(lg n)", 2.8)
    an.salva("animazione-rb-delete.svg")


# =================================================================== SPLAY TREE (lezione 12)
class _Alb:
    """Contenitore della radice, perche' le rotazioni possono cambiarla."""
    def __init__(self, root):
        self.root = root


def _rot_sx(T, x):
    y = x.right
    x.right = y.left
    if y.left is not None:
        y.left.p = x
    y.p = x.p
    if x.p is None:
        T.root = y
    elif x is x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x
    x.p = y


def _rot_dx(T, y):
    x = y.left
    y.left = x.right
    if x.right is not None:
        x.right.p = y
    x.p = y.p
    if y.p is None:
        T.root = x
    elif y is y.p.left:
        y.p.left = x
    else:
        y.p.right = x
    x.right = y
    y.p = x


def _sali_nodo(T, x):
    """Rotazione su p[x] che porta x sopra il padre; restituisce il nome della rotazione per la didascalia."""
    p = x.p
    if x is p.left:
        nome = f"Right-Rotate (T,{p.key})"
        _rot_dx(T, p)
    else:
        nome = f"Left-Rotate (T,{p.key})"
        _rot_sx(T, p)
    return nome


def _splay_frames(T, x, emetti):
    """Esegue Splay (T,x) e chiama emetti(righe, nota, didascalia) dopo ogni rotazione."""
    rot = 0
    while x.p is not None:
        y = x.p
        z = y.p
        if z is None:
            nome = _sali_nodo(T, x)
            rot += 1
            emetti({2, 3, 4, 5}, f"caso I: x è figlio della radice → {nome}", f"caso I: {nome}")
        elif (x is y.left) == (y is z.left):
            n1 = _sali_nodo(T, y)
            emetti({2, 3, 6, 7}, f"caso II: x e p[x] sono entrambi figli {'sinistri' if x is y.left else 'destri'} → prima la rotazione sul nonno: {n1}",
                   f"caso II, rotazione sul nonno: {n1}")
            n2 = _sali_nodo(T, x)
            rot += 2
            emetti({2, 3, 6, 8}, f"caso II → poi la rotazione sul padre di x: {n2}", f"caso II, rotazione sul padre: {n2}")
        else:
            n1 = _sali_nodo(T, x)
            emetti({2, 3, 9, 10}, f"caso III: uno è figlio sinistro e l'altro destro → prima la rotazione sul padre di x: {n1}",
                   f"caso III, rotazione sul padre: {n1}")
            n2 = _sali_nodo(T, x)
            rot += 2
            emetti({2, 3, 9, 11}, f"caso III → poi la rotazione sul nuovo padre di x (era il nonno): {n2}", f"caso III, rotazione sul nuovo padre: {n2}")
    return rot


PSEUDO_SPLAY = [(1, "Splay (T,x)   ▷ x sale fino alla radice"), (2, "while p[x] ≠ NIL"), (3, "  y ← p[x];  z ← p[y]"),
                (4, "  if z = NIL              ▷ caso I"), (5, "     then rotazione su y: x sale"),
                (6, "  else if stesso lato     ▷ caso II"), (7, "     rotazione sul nonno z (y sale)"),
                (8, "     rotazione sul padre y (x sale)"), (9, "  else                    ▷ caso III"),
                (10, "     rotazione sul padre y (x sale)"), (11, "     rotazione sul nuovo padre z (x sale)")]


def splay():
    an = Animazione("Splay sull'albero di 12 p. 6: Splay(17), poi Splay(13)", 880, 470, 1.2)
    T = _Alb(_bst([15, 6, 18, 3, 7, 17, 20, 2, 4, 13]))

    def trova(k):
        x = T.root
        while x.key != k:
            x = x.left if k < x.key else x.right
        return x

    def scena(righe, x, nota):
        s = _disegna_albero(T.root, x0=20, y0=70, w=450, dy=47, col={x: EVID}, etich={x: "x"}, r=15)
        s += t(20, 400, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO_SPLAY, righe, 500, 80, 360, 22)
        return s

    for k in (17, 13):
        x = trova(k)
        an.frame(scena({1}, x, f"Splay (T,{k}): x = {k} deve salire fino alla radice"), f"Splay({k}): albero di partenza")
        _splay_frames(T, x, lambda righe, nota, cap, x=x: an.frame(scena(righe, x, nota), cap))
    an.frame(scena({1}, x, "x = 13 è la radice; l'ordine delle chiavi è invariato (visita in ordine: 2 3 4 6 7 13 15 17 18 20)"),
             "dopo Splay(13) la visita in ordine non è cambiata", 2.5)
    an.salva("animazione-splay.svg")


PSEUDO_SPLAYOP = {
    "search": [(1, "Splay-Tree-Search (T,k)"), (2, "x ← root[T]"), (3, "while x≠NIL and key[x]≠k"), (4, "  do y ← x"),
               (5, "     if k < key[x]"), (6, "        then x ← left[x]"), (7, "        else x ← right[x]"),
               (8, "if x≠NIL"), (9, "  then Splay (T,x)"), (10, "  else if root[T]≠NIL"), (11, "       then Splay (T,y)"),
               (12, "return x")],
    "insert": [(1, "Splay-Tree-Insert (T,z)"), (2, "Tree-Insert (z)"), (3, "Splay (T,z)")],
    "delete": [(1, "Splay-Tree-Delete (T,z)"), (2, "Tree-Delete (z)"), (3, "if p[z]≠NIL"), (4, "  then Splay (T,p[z])")],
}


def splay_tree_operazioni():
    an = Animazione("Splay-Tree-Search, -Insert e -Delete sull'albero di 12 pp. 6–8", 880, 470, 1.2)
    base = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13]

    def scene(T, tipo, righe, x, nota, evid=None, etich=None):
        col = {x: EVID} if x is not None else {}
        col.update(evid or {})
        s = _disegna_albero(T.root, x0=20, y0=70, w=450, dy=47, col=col, etich=etich if etich is not None else ({x: "x"} if x is not None else {}), r=15)
        s += t(20, 400, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO_SPLAYOP[tipo], righe, 500, 80, 360, 22)
        return s

    # --- ricerca di una chiave assente: 19 (si fa lo splay dell'ultimo nodo visitato, 20)
    T = _Alb(_bst(base))
    an.frame(scene(T, "search", set(), None, "Splay-Tree-Search (T,19): la chiave 19 non c'è nell'albero"), "ricerca di 19 (assente)")
    x, y = T.root, None
    percorso = []
    while x is not None and x.key != 19:
        y = x
        percorso.append(x.key)
        x = x.left if 19 < x.key else x.right
    an.frame(scene(T, "search", {2, 3, 4, 5, 6, 7}, y, f"la discesa tocca {' → '.join(map(str, percorso))} e si ferma su NIL: y = {y.key} è l'ultimo nodo visitato", etich={y: "y"}),
             "la ricerca termina su NIL: y = 20")
    an.frame(scene(T, "search", {8, 10, 11}, y, "x = NIL e l'albero non è vuoto: Splay (T,y) con y = 20", etich={y: "y"}), "x = NIL: Splay (T,y)")
    _splay_frames(T, y, lambda righe, nota, cap: an.frame(scene(T, "search", {11}, y, nota, etich={y: "y"}), cap))
    an.frame(scene(T, "search", {12}, y, "return x = NIL; la radice è ora 20 (il nodo su cui la ricerca è terminata)", etich={y: "y"}), "ricerca terminata: 20 in radice", 2.2)

    # --- inserimento di 19 (p. 7)
    T = _Alb(_bst(base))
    an.frame(scene(T, "insert", set(), None, "Splay-Tree-Insert (T,19): il nodo z = 19 non è ancora nell'albero"), "inserimento di 19 (p. 7)")
    z = _N(19)
    x, y = T.root, None
    while x is not None:
        y = x
        x = x.left if 19 < x.key else x.right
    z.p = y
    if 19 < y.key:
        y.left = z
    else:
        y.right = z
    an.frame(scene(T, "insert", {2}, z, "riga 2: Tree-Insert attacca 19 come figlio sinistro di 20 (foglia)", etich={z: "z"}), "Tree-Insert: 19 è una foglia")
    _splay_frames(T, z, lambda righe, nota, cap: an.frame(scene(T, "insert", {3}, z, nota, etich={z: "z"}), cap))
    an.frame(scene(T, "insert", {3}, z, "19 è la nuova radice: gli elementi appena usati stanno vicino alla radice", etich={z: "z"}), "inserimento completato", 2.2)

    # --- cancellazione di 3 (due figli): si taglia il successore 4 e si fa lo splay del padre di z (6)
    T = _Alb(_bst(base))
    x = T.root
    while x.key != 3:
        x = x.left if 3 < x.key else x.right
    z = x
    an.frame(scene(T, "delete", set(), z, "Splay-Tree-Delete (T,z) con z = 3 (due figli: 2 e 4); il padre di z è 6", etich={z: "z"}), "cancellazione di 3 (istanza mia)")
    padre = z.p
    succ = z.right
    while succ.left is not None:
        succ = succ.left
    figlio = succ.right
    if figlio is not None:
        figlio.p = succ.p
    if succ.p.left is succ:
        succ.p.left = figlio
    else:
        succ.p.right = figlio
    z.key = succ.key
    an.frame(scene(T, "delete", {2}, padre, f"riga 2: Tree-Delete taglia il successore 4 (ha al massimo un figlio) e ne copia la chiave in z; p[z] = 6 resta il padre", evid={padre: EVID}, etich={padre: "p[z]"}),
             "Tree-Delete: la chiave 4 prende il posto di 3")
    _splay_frames(T, padre, lambda righe, nota, cap: an.frame(scene(T, "delete", {3, 4}, padre, nota, etich={padre: "p[z]"}), cap))
    an.frame(scene(T, "delete", {4}, padre, "6 (il padre di z) è la nuova radice", etich={padre: "p[z]"}), "cancellazione completata", 2.2)
    an.salva("animazione-splay-tree-operazioni.svg")


# =================================================================== VISITE DI GRAFI (lezione 13)
NODO_B, NODO_G, NODO_N = "#ffffff", "#b8c2c8", "#26363d"


def _g_scena(pos, archi, stato, tree=(), evid=None, sotto=None, r=16, pesi=False, dash=()):
    """Grafo: archi = [(u,v)] o [(u,v,w)]; stato[u] in 'W','G','B'; tree = insieme di frozenset({u,v}) in blu."""
    evid, sotto = evid or {}, sotto or {}
    s = ""
    for a in archi:
        u, v = a[0], a[1]
        in_tree = frozenset((u, v)) in tree
        s += line(*pos[u], *pos[v], BLU if in_tree else GRIGIO, 3.2 if in_tree else 1.6, dash="5,3" if frozenset((u, v)) in dash else None)
        if pesi and len(a) > 2:
            mx, my = (pos[u][0] + pos[v][0]) / 2, (pos[u][1] + pos[v][1]) / 2
            s += rect(mx - 9, my - 9, 18, 16, fill=SFONDO, stroke="none", rx=3) + t(mx, my + 4, a[2], 11, ARANCIO, "middle", True)
    for u, (x, y) in pos.items():
        st = stato.get(u, "W")
        fill = {"W": NODO_B, "G": NODO_G, "B": NODO_N}[st]
        s += circle(x, y, r, fill, evid.get(u, TESTO), 4 if u in evid else 1.5)
        s += t(x, y + 5, u, 14, "#ffffff" if st == "B" else TESTO, "middle", True)
        if u in sotto:
            s += rect(x - 20, y + r + 2, 40, 14, fill=SFONDO, stroke="none", rx=3) + t(x, y + r + 13, sotto[u], 11, ROSSO, "middle", True)
    return s


PSEUDO_BFS = [(1, "BFS (G,s)"), (2, "for each vertex u ∈ V[G]-{s}"), (3, "  do color[u] ← WHITE"), (4, "     d[u] ← ∞"),
              (5, "     π[u] ← NIL"), (6, "color[s] ← GRAY"), (7, "d[s] ← 0"), (8, "π[s] ← NIL"), (9, "Q ← Ø"),
              (10, "Enqueue (Q,s)"), (11, "while Q ≠ Ø"), (12, "  do u ← Dequeue (Q)"), (13, "     for each v ∈ Adj[u]"),
              (14, "       do if color[v] = WHITE"), (15, "          then color[v] ← GRAY"), (16, "               d[v] ← d[u] + 1"),
              (17, "               π[v] ← u"), (18, "               Enqueue (Q,v)"), (19, "     color[u] ← BLACK")]

POS_BFS = {"r": (50, 100), "s": (140, 100), "t": (260, 100), "u": (350, 100), "v": (50, 200), "w": (140, 200), "x": (260, 200), "y": (350, 200)}
ARCHI_BFS = [("r", "s"), ("r", "v"), ("s", "w"), ("t", "u"), ("t", "w"), ("t", "x"), ("u", "x"), ("u", "y"), ("w", "x"), ("x", "y")]


def bfs_anim():
    from collections import deque
    an = Animazione("BFS sul grafo di 13 p. 11 con sorgente s (liste in ordine alfabetico)", 880, 480, 1.2)
    G = {"r": ["s", "v"], "s": ["r", "w"], "t": ["u", "w", "x"], "u": ["t", "x", "y"], "v": ["r"], "w": ["s", "t", "x"],
         "x": ["t", "u", "w", "y"], "y": ["u", "x"]}
    color = {u: "W" for u in G}
    d = {u: "∞" for u in G}
    pi = {u: None for u in G}
    tree = set()
    Q = deque()

    def scena(righe, nota, evid=None, nuovi=()):
        s = _g_scena(POS_BFS, ARCHI_BFS, color, tree, evid, {u: f"d={d[u]}" for u in G if d[u] != "∞"})
        s += t(20, 300, "coda Q (testa → coda):", 13, TESTO, bold=True)
        for i, q in enumerate(Q):
            s += rect(180 + i * 38, 284, 34, 24, fill=NODO_G, stroke=TESTO, sw=1.2, rx=3) + t(197 + i * 38, 301, q, 14, TESTO, "middle", True)
        if not Q:
            s += t(180, 301, "vuota", 13, GRIGIO)
        s += t(20, 340, "π: " + "  ".join(f"{u}←{pi[u] if pi[u] else 'NIL'}" for u in sorted(G)), 12, TESTO)
        s += t(20, 400, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO_BFS, righe, 500, 62, 360, 19)
        return s

    an.frame(scena(set(), "tutti i vertici bianchi (non scoperti), d = ∞, π = NIL"), "grafo di partenza (13 p. 11)")
    color["s"], d["s"] = "G", 0
    Q.append("s")
    an.frame(scena({6, 7, 8, 9, 10}, "sorgente: s grigio, d[s] = 0, Q = ⟨s⟩ (inizializzazione)", {"s": ARANCIO}), "inizializzazione")
    while Q:
        u = Q.popleft()
        nuovi = []
        for v in G[u]:
            if color[v] == "W":
                color[v], d[v], pi[v] = "G", d[u] + 1, u
                tree.add(frozenset((u, v)))
                Q.append(v)
                nuovi.append(v)
        color[u] = "B"
        an.frame(scena({11, 12, 13, 14, 15, 16, 17, 18, 19},
                       f"u = {u}: Adj[{u}] = {', '.join(G[u])} → " + (f"nuovi grigi: {', '.join(nuovi)}" if nuovi else "nessun vertice bianco") + f"; {u} diventa nero",
                       {u: ARANCIO}), f"si estrae {u}: " + (f"scoperti {', '.join(nuovi)}" if nuovi else "nessun nuovo vertice"))
    an.frame(scena(set(), "Q vuota: BFS termina. Archi blu = breadth-first tree; d[v] = lunghezza dello shortest path da s (13 p. 19)"),
             "visita completata: d = 0, 1, 1, 2, 2, 2, 3, 3", 2.5)
    an.salva("animazione-visita-in-ampiezza.svg")


PSEUDO_PP = [(1, "Print-Path (G,s,v)"), (2, "if v = s"), (3, "  then print s"), (4, "  else if π[v] = NIL"),
             (5, '    then print "no path from s to v exists"'), (6, "    else Print-Path (G,s,π[v])"), (7, "         print v")]


def print_path_anim():
    an = Animazione("Print-Path (G,s,y) dopo la BFS di 13 p. 11", 880, 450, 1.2)
    pi = {"r": "s", "s": None, "t": "w", "u": "t", "v": "r", "w": "s", "x": "w", "y": "x"}
    color = {u: "B" for u in pi}
    tree = {frozenset((v, p)) for v, p in pi.items() if p}
    stato_ev = {}

    def scena(righe, nota, pila, stampa, evid):
        s = _g_scena(POS_BFS, ARCHI_BFS, color, tree, evid)
        s += t(20, 290, "chiamate aperte: " + (" → ".join(f"({v})" for v in pila) if pila else "—"), 13, TESTO, bold=True)
        s += t(20, 318, "stampato: " + (" ".join(stampa) if stampa else "—"), 14, VERDE, bold=True)
        s += t(20, 400, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO_PP, righe, 500, 70, 360, 22)
        return s

    pila, stampa, evid = [], [], {}

    def rec(v):
        pila.append(v)
        evid.clear(); evid[v] = ARANCIO
        if v == "s":
            an.frame(scena({1, 2}, "v = s: caso base, si stampa s", pila, stampa, evid), "Print-Path (G,s,s): v = s")
            stampa.append("s")
            an.frame(scena({3}, "riga 3: print s", pila, stampa, evid), "print s")
        else:
            an.frame(scena({1, 2, 4, 6}, f"v = {v}, π[{v}] = {pi[v]}: prima si stampa il percorso fino a π[{v}] (chiamata ricorsiva)", pila, stampa, evid),
                     f"Print-Path (G,s,{v}): π[{v}] = {pi[v]}")
            rec(pi[v])
            evid.clear(); evid[v] = ARANCIO
            stampa.append(v)
            an.frame(scena({7}, f"ritorno nella chiamata con v = {v}: riga 7, print {v}", pila, stampa, evid), f"print {v}")
        pila.pop()

    an.frame(scena(set(), "BFS già eseguita: π come in figura (sorgente s); si vuole il percorso da s a y", [], [], {}), "BFS già eseguita")
    rec("y")
    an.frame(scena(set(), "stampato s w x y: lo shortest path da s a y, con 3 archi, in tempo lineare nel numero di vertici sul percorso", [], stampa, {}),
             "percorso minimo: s → w → x → y", 2.5)
    an.salva("animazione-print-path.svg")


PSEUDO_DFS = [(1, "DFS (G)"), (2, "for each vertex u ∈ V[G]"), (3, "  do color[u] ← WHITE; π[u] ← NIL"), (4, "time ← 0"),
              (5, "for each vertex u ∈ V[G]"), (6, "  do if color[u] = WHITE"), (7, "     then DFS-Visit (u)"),
              (8, "DFS-Visit (u): color[u] ← GRAY"), (9, "  time ← time+1"), (10, "  d[u] ← time"), (11, "  for each v ∈ Adj[u]"),
              (12, "    do if color[v] = WHITE"), (13, "       then π[v] ← u"), (14, "            DFS-Visit (v)"),
              (15, "  color[u] ← BLACK"), (16, "  f[u] ← time ← time+1")]
POS_DFS = {"h": (40, 120), "d": (110, 120), "g": (60, 200), "a": (180, 200), "s": (280, 200), "e": (195, 290), "c": (285, 290),
           "b": (370, 120), "i": (455, 205), "f": (395, 275)}
ARCHI_DFS = [("h", "d"), ("d", "g"), ("d", "a"), ("g", "a"), ("a", "s"), ("a", "e"), ("d", "s"), ("s", "b"), ("s", "c"), ("s", "f"), ("b", "f"),
             ("f", "i"), ("b", "i")]


def dfs_anim():
    an = Animazione("DFS sul grafo di 13 p. 28 con sorgente s", 880, 480, 1.0)
    G = {"s": ["a", "b", "c", "d", "f"], "a": ["s", "d", "e", "g"], "d": ["a", "g", "h", "s"], "g": ["d", "a"], "h": ["d"],
         "e": ["a"], "b": ["s", "f", "i"], "f": ["b", "i", "s"], "i": ["f", "b"], "c": ["s"]}
    color = {u: "W" for u in G}
    dd, ff = {}, {}
    tree, pila = set(), []
    tempo = [0]

    def scena(righe, nota, evid=None):
        sotto = {u: (f"{dd[u]}/{ff[u]}" if u in ff else f"{dd[u]}/") for u in dd}
        s = _g_scena(POS_DFS, ARCHI_DFS, color, tree, evid, sotto, r=15)
        s += t(20, 345, "pila delle chiamate: " + (" → ".join(pila) if pila else "—"), 13, TESTO, bold=True)
        s += t(20, 400, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO_DFS, righe, 515, 62, 350, 19)
        return s

    def visit(u, padre):
        color[u] = "G"
        tempo[0] += 1
        dd[u] = tempo[0]
        pila.append(u)
        if padre:
            tree.add(frozenset((u, padre)))
        an.frame(scena({8, 9, 10} | ({13, 14} if padre else {6, 7}), f"{u} scoperto: d[{u}] = {tempo[0]}, {u} diventa grigio" + (f" (π[{u}] = {padre})" if padre else ""), {u: ARANCIO}),
                 f"scoperto {u}, d = {tempo[0]}")
        for v in G[u]:
            if color[v] == "W":
                visit(v, u)
        color[u] = "B"
        tempo[0] += 1
        ff[u] = tempo[0]
        an.frame(scena({15, 16}, f"{u}: tutti i vicini esplorati, {u} diventa nero, f[{u}] = {tempo[0]}", {u: ARANCIO}), f"terminato {u}, f = {tempo[0]}")
        pila.pop()

    an.frame(scena(set(), "tutti i vertici bianchi; time = 0"), "grafo di partenza (13 p. 28)")
    visit("s", None)
    an.frame(scena(set(), "DFS termina: depth-first tree (blu); gli altri archi sono back edges. Intervalli annidati: (s (a (d (g g) (h h) d) (e e) a) (b (f (i i) f) b) (c c) s)"),
             "tempi finali d/f come in 13 p. 28", 2.8)
    an.salva("animazione-visita-in-profondita.svg")


POS_DAG = {"a": (30, 180), "b": (70, 250), "c": (95, 85), "d": (135, 175), "e": (160, 260), "f": (230, 235), "g": (180, 55), "h": (215, 130),
           "i": (310, 150), "j": (290, 75)}
ARCHI_DAG = [("a", "d"), ("a", "b"), ("b", "e"), ("e", "f"), ("f", "d"), ("d", "c"), ("c", "g"), ("g", "j"), ("j", "i"), ("d", "h"), ("h", "i")]
PSEUDO_TS = [(1, "Topological-Sort (G)"), (2, "  chiama DFS (G): calcola f[v]"), (3, "  ogni vertice terminato →"),
             (4, "    in testa a una lista"), (5, "  return la lista")]


def topological_sort_anim():
    an = Animazione("Topological-Sort sul DAG di 13 pp. 39–40 (DFS da a)", 880, 480, 1.0)
    G = {"a": ["d", "b"], "b": ["e"], "e": ["f"], "f": ["d"], "d": ["h", "c"], "c": ["g"], "g": ["j"], "j": ["i"], "h": ["i"], "i": []}
    color = {u: "W" for u in G}
    dd, ff = {}, {}
    lista, tempo = [], [0]
    tree = set()

    def scena(righe, nota, evid=None):
        sotto = {u: (f"{dd[u]}/{ff[u]}" if u in ff else f"{dd[u]}/") for u in dd}
        s = ""
        for (u, v) in ARCHI_DAG:
            (x1, y1), (x2, y2) = POS_DAG[u], POS_DAG[v]
            lung = math.hypot(x2 - x1, y2 - y1)
            xa, ya = x1 + (x2 - x1) * 16 / lung, y1 + (y2 - y1) * 16 / lung        # parte dal bordo di u
            xb, yb = x2 - (x2 - x1) * 17 / lung, y2 - (y2 - y1) * 17 / lung        # arriva al bordo di v
            s += line(xa, ya, xb, yb, BLU if frozenset((u, v)) in tree else GRIGIO, 3 if frozenset((u, v)) in tree else 1.6, arrow=True)
        for u, (x, y) in POS_DAG.items():
            st = color[u]
            s += circle(x, y, 15, {"W": NODO_B, "G": NODO_G, "B": NODO_N}[st], (evid or {}).get(u, TESTO), 4 if evid and u in evid else 1.5)
            s += t(x, y + 5, u, 14, "#ffffff" if st == "B" else TESTO, "middle", True)
            if u in sotto:
                s += t(x, y + 29, sotto[u], 11, ROSSO, "middle", True)
        s += t(20, 330, "lista (inserimenti in testa):", 13, TESTO, bold=True)
        for i, v in enumerate(lista):
            s += rect(20 + i * 40, 342, 36, 28, fill=EVID if i == 0 else "#fff", stroke=TESTO, sw=1.2, rx=3) + t(38 + i * 40, 362, v, 15, TESTO, "middle", True)
        s += t(20, 408, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO_TS, righe, 520, 70, 340, 22)
        return s

    def visit(u, padre):
        color[u] = "G"
        tempo[0] += 1
        dd[u] = tempo[0]
        if padre:
            tree.add(frozenset((u, padre)))
        an.frame(scena({2}, f"DFS scopre {u}: d[{u}] = {tempo[0]}", {u: ARANCIO}), f"scoperto {u}, d = {tempo[0]}")
        for v in G[u]:
            if color[v] == "W":
                visit(v, u)
        color[u] = "B"
        tempo[0] += 1
        ff[u] = tempo[0]
        lista.insert(0, u)
        an.frame(scena({2, 3, 4}, f"{u} terminato: f[{u}] = {tempo[0]}; {u} va in testa alla lista", {u: ARANCIO}), f"terminato {u}, f = {tempo[0]}")

    an.frame(scena(set(), "DAG di p. 39: se esiste un arco u → v, u deve precedere v nell'ordinamento"), "DAG di partenza")
    visit("a", None)
    an.frame(scena({5}, "return: a b e f d c g j h i. Per ogni arco u → v vale f[v] < f[u], quindi u precede v; costo Θ(V+E)"),
             "ordinamento topologico: a b e f d c g j h i", 2.8)
    an.salva("animazione-ordinamento-topologico.svg")


PSEUDO_DIJ = [(1, "known = {s}"), (2, "for i = 1 to n, dist[i] = ∞"), (3, "for each edge (s,v), dist[v] = d(s,v)"), (4, "last = s"),
              (5, "while (last ≠ t)"), (6, "  select v: dist(v) = min unknown"), (7, "  for each (v,x):"),
              (8, "    dist[x]=min(dist[x],dist[v]+w(v,x))"), (9, "  last = v"), (10, "  known = known ∪ {v}")]
POS_DIJ = {"A": (40, 250), "B": (40, 140), "C": (150, 70), "D": (160, 190), "E": (270, 120), "F": (260, 260), "G": (375, 70)}
ARCHI_DIJ = [("A", "B", 5), ("A", "D", 7), ("A", "F", 12), ("B", "C", 7), ("B", "D", 9), ("C", "D", 4), ("C", "E", 2), ("C", "G", 5),
             ("D", "E", 3), ("D", "F", 4), ("E", "F", 7), ("E", "G", 2)]


def dijkstra_anim():
    an = Animazione("Algoritmo di Dijkstra sul grafo di 13 pp. 51–52 (sorgente A)", 880, 480, 1.3)
    g = {}
    for u, v, w in ARCHI_DIJ:
        g.setdefault(u, []).append((v, w))
        g.setdefault(v, []).append((u, w))
    INF = float("inf")
    dist = {v: INF for v in g}
    pred = {v: None for v in g}
    known = set()
    tree = set()

    def scena(righe, nota, evid=None, agg=()):
        stato = {v: ("B" if v in known else ("G" if dist[v] < INF else "W")) for v in g}
        s = _g_scena(POS_DIJ, ARCHI_DIJ, stato, tree, evid, None, r=16, pesi=True)
        # tabella delle distanze
        s += t(20, 320, "dist:", 13, TESTO, bold=True)
        for i, v in enumerate(sorted(g)):
            x = 70 + i * 52
            f = NODO_N if v in known else (EVID if v in agg else "#fff")
            s += rect(x, 304, 48, 38, fill=f, stroke=TESTO, sw=1.2, rx=3)
            s += t(x + 24, 319, v, 12, "#fff" if v in known else GRIGIO, "middle")
            s += t(x + 24, 336, "∞" if dist[v] == INF else dist[v], 14, "#fff" if v in known else TESTO, "middle", True)
        s += t(20, 370, "known = {" + ", ".join(sorted(known)) + "}  (blu: albero dei cammini minimi)", 12, TESTO)
        s += t(20, 408, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO_DIJ, righe, 520, 70, 340, 22)
        return s

    an.frame(scena(set(), "grafo pesato non orientato, pesi positivi (non negativi); sorgente A", {"A": ARANCIO}), "grafo di partenza (13 p. 52)")
    dist["A"] = 0
    known.add("A")
    agg = []
    for v, w in g["A"]:
        dist[v] = w
        pred[v] = "A"
        agg.append(v)
    an.frame(scena({1, 2, 3, 4}, "inizializzazione: known = {A}; dist[v] = peso dell'arco (A,v) per i vicini B, D, F", {"A": ARANCIO}, agg), "inizializzazione")
    while len(known) < len(g):
        v = min((x for x in g if x not in known), key=lambda x: (dist[x], x))
        agg = []
        tree.add(frozenset((v, pred[v])))
        an.frame(scena({5, 6}, f"si sceglie v = {v}, il vertice non noto con dist minima ({dist[v]}); l'arco ({pred[v]},{v}) entra nell'albero", {v: ARANCIO}),
                 f"select v = {v} (dist = {dist[v]})")
        known.add(v)
        for x, w in g[v]:
            if x not in known and dist[v] + w < dist[x]:
                dist[x] = dist[v] + w
                pred[x] = v
                agg.append(x)
        an.frame(scena({7, 8, 9, 10}, f"v = {v}: per ogni vicino x, dist[x] = min(dist[x], dist[{v}] + w)" + (f" → migliorati: {', '.join(agg)}" if agg else " → nessun miglioramento"), {v: ARANCIO}, agg),
                 f"aggiornamento dei vicini di {v}")
    an.frame(scena(set(), "tutti i vertici noti: dist = A 0, B 5, D 7, E 10, C 11, F 11, G 12. Costo O(n²): n volte una selezione O(n) e un aggiornamento O(n)", {}),
             "cammini minimi da A", 2.8)
    an.salva("animazione-dijkstra.svg")


# =================================================================== BACKPROPAGATION (lezione 14)
PSEUDO_BP = [(1, "FORWARD:  for v in Ord:"), (2, "  if v è un input:"), (3, "    value[v] ← input[v]"), (4, "  else:"),
             (5, "    args ← [value[u] for u in pred[v]]"), (6, "    value[v] ← f_v(args)"),
             (7, "BACKWARD: for v in V: δ[v] ← 0"), (8, "  δ[C] ← 1"), (9, "  for v in reverse(Ord):"),
             (10, "    for u in pred[v]:"), (11, "      dlocal ← ∂f_v/∂z_u"), (12, "      δ[u] += δ[v] · dlocal")]
POS_BP = {"a": (50, 130), "b": (50, 260), "c": (150, 130), "d": (250, 130), "e": (350, 130), "C": (440, 130)}
ARCHI_BP = [("a", "c"), ("b", "c"), ("c", "d"), ("d", "e"), ("b", "e"), ("e", "C")]
FORMULE_BP = {"c": "c = a·b", "d": "d = sin(c)", "e": "e = d + b", "C": "C = ½(e−1)²"}


def backpropagation_anim():
    import math as _m
    an = Animazione("Backpropagation su C(a,b) = ½(sin(a·b) + b − 1)² nel punto (2, 3) — grafo di 14 pp. 11–21", 880, 470, 1.4)
    a, b = 2.0, 3.0
    val, delta = {"a": a, "b": b}, {}
    attivi = set()

    def scena(righe, nota, nodo_ev=None, archi_ev=(), calc=""):
        s = ""
        for (u, v) in ARCHI_BP:
            ev = (u, v) in archi_ev
            x1, y1 = POS_BP[u]
            x2, y2 = POS_BP[v]
            if u == "b" and v == "e":                  # arco b -> e: percorso a gomito sotto il grafo
                s += line(x1, y1 + 17, x1, 330, ROSSO if ev else GRIGIO, 3 if ev else 1.6)
                s += line(x1, 330, x2, 330, ROSSO if ev else GRIGIO, 3 if ev else 1.6)
                s += line(x2, 330, x2, y2 + 17, ROSSO if ev else GRIGIO, 3 if ev else 1.6, arrow=True)
                continue
            lung = _m.hypot(x2 - x1, y2 - y1)
            xa, ya = x1 + (x2 - x1) * 17 / lung, y1 + (y2 - y1) * 17 / lung
            xb, yb = x2 - (x2 - x1) * 18 / lung, y2 - (y2 - y1) * 18 / lung
            s += line(xa, ya, xb, yb, ROSSO if ev else GRIGIO, 3 if ev else 1.6, arrow=True)
        for v, (x, y) in POS_BP.items():
            fill = ROSA if v == "C" else EVID
            s += circle(x, y, 17, fill, ARANCIO if v == nodo_ev else TESTO, 4 if v == nodo_ev else 1.5)
            s += t(x, y + 5, v, 15, TESTO, "middle", True)
            if v in FORMULE_BP:
                s += t(x, y - 26, FORMULE_BP[v], 11, GRIGIO, "middle")
            if v in val:
                s += rect(x - 36, y + 23, 72, 16, fill=SFONDO, stroke="none", rx=3)
                s += t(x, y + 36, f"val = {val[v]:.4g}" if abs(val[v]) >= 1e-3 else f"val = {val[v]:.2g}", 12, BLU, "middle", True)
            if v in delta:
                s += rect(x - 36, y + 39, 72, 16, fill=SFONDO, stroke="none", rx=3)
                s += t(x, y + 51, f"δ = {delta[v]:.4f}".rstrip("0").rstrip("."), 12, ROSSO, "middle", True)
        s += t(20, 372, calc, 13, TESTO)
        s += t(20, 400, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO_BP, righe, 500, 62, 365, 20)
        return s

    an.frame(scena({1, 2, 3}, "FORWARD 1/5: valori degli input value[a] = 2, value[b] = 3; gli altri nodi non sono ancora calcolati", "a"), "forward: i due input")
    val["c"] = val["a"] * val["b"]
    an.frame(scena({1, 4, 5, 6}, "FORWARD 2/5: c dipende da a e b", "c", calc=f"value[c] = value[a]·value[b] = 2·3 = {val['c']:g}"), "forward: c = a·b = 6")
    val["d"] = _m.sin(val["c"])
    an.frame(scena({1, 4, 5, 6}, "FORWARD 3/5: d usa il valore di c (seno in radianti)", "d", calc=f"value[d] = sin(6) ≈ {val['d']:.4f}"), "forward: d = sin(6)")
    val["e"] = val["d"] + val["b"]
    an.frame(scena({1, 4, 5, 6}, "FORWARD 4/5: e riceve due valori, d e b (anche da un layer non adiacente)", "e", calc=f"value[e] = sin(6) + 3 ≈ {val['e']:.4f}"), "forward: e = d + b")
    val["C"] = 0.5 * (val["e"] - 1) ** 2
    an.frame(scena({1, 4, 5, 6}, "FORWARD 5/5: l'uscita scalare; si conservano tutti i valori per le derivate locali", "C", calc=f"C = ½(e − 1)² ≈ {val['C']:.4f}"), "forward: C ≈ 1,4802")
    for v in val:
        delta[v] = 0.0
    delta["C"] = 1.0
    an.frame(scena({7, 8}, "BACKWARD 1/5: δ[v] = ∂C/∂z_v; δ = 0 per ogni v ≠ C, e δ[C] = ∂C/∂C = 1", "C", calc="le quantità rosse sono accumulatori delle derivate, non valori dei nodi"), "backward: δ[C] = 1")
    dl = val["e"] - 1
    delta["e"] += delta["C"] * dl
    an.frame(scena({9, 10, 11, 12}, "BACKWARD 2/5: C ha un solo predecessore, e", "C", {("e", "C")}, f"∂C/∂e = e − 1 ≈ {dl:.4f}  ⇒  δ[e] += δ[C]·(e − 1) ≈ {delta['e']:.4f}"), "backward: da C a e")
    delta["d"] += delta["e"] * 1.0
    delta["b"] += delta["e"] * 1.0
    an.frame(scena({9, 10, 11, 12}, "BACKWARD 3/5: e = d + b, entrambi i predecessori ricevono il contributo; δ[b] è ancora parziale", "e", {("d", "e"), ("b", "e")},
                   f"∂e/∂d = ∂e/∂b = 1  ⇒  δ[d] += δ[e]·1 ≈ {delta['d']:.4f},  δ[b] += δ[e]·1 ≈ {delta['b']:.4f}"), "backward: da e a d e b")
    dl = _m.cos(val["c"])
    delta["c"] += delta["d"] * dl
    an.frame(scena({9, 10, 11, 12}, "BACKWARD 4/5: d = sin(c): si usa il valore di c memorizzato nel forward", "d", {("c", "d")}, f"∂d/∂c = cos(c) = cos(6) ≈ {dl:.4f}  ⇒  δ[c] += δ[d]·cos(6) ≈ {delta['c']:.4f}"), "backward: da d a c")
    delta["a"] += delta["c"] * val["b"]
    delta["b"] += delta["c"] * val["a"]
    an.frame(scena({9, 10, 11, 12}, "BACKWARD 5/5: c = a·b, il contributo di c va a entrambi gli input; due cammini per b, due contributi, una somma", "c", {("a", "c"), ("b", "c")},
                   f"∂c/∂a = b = 3 ⇒ δ[a] ≈ {delta['a']:.4f};   ∂c/∂b = a = 2 ⇒ δ[b] = 1.7206 + 3.3041 ≈ {delta['b']:.4f}"), "backward: da c ad a e b")
    an.frame(scena(set(), "∇C(2, 3) ≈ (4,9562; 5,0247): coincide con la regola della catena calcolata a mano; tempo O(V+E) per il forward e per il backward", None, calc="∂C/∂a ≈ 4,9562   ∂C/∂b ≈ 5,0247"),
             "gradiente ottenuto con un solo passaggio all'indietro", 3.0)
    an.salva("animazione-backpropagation.svg")


# =================================================================== BACKTRACKING (lezione 15)
PSEUDO_BT = [(1, "Backtrack (a,k)"), (2, "if a is a solution, print (a)"), (3, "else {"), (4, "  k = k + 1"), (5, "  compute S_k"),
             (6, "  while S_k ≠ ∅ do"), (7, "    a_k = an element in S_k"), (8, "    S_k = S_k − a_k"), (9, "    Backtrack (a,k)"), (10, "}")]


def _bt_esegui(n, candidati):
    """Esegue Backtrack (a,0) davvero e restituisce gli eventi (stato, tipo): 'entra' | 'esce' | 'sol'."""
    eventi, a = [], [None] * (n + 2)

    def bt(k):
        stato = tuple(a[1:k + 1])
        if k == n:
            eventi.append((stato, "sol"))
            return
        eventi.append((stato, "entra"))
        for c in candidati(a, k + 1, n):
            a[k + 1] = c
            bt(k + 1)
            eventi.append((tuple(a[1:k + 1]), "esce"))

    bt(0)
    return eventi


def _bt_albero(eventi, n, W=440, x0=20, y0=70, dy=58):
    """Posizioni dei nodi (stati distinti): foglie equidistanti, nodi interni centrati sopra i figli."""
    figli = {}
    for stato, _ in eventi:
        figli.setdefault(stato, [])
    for stato in list(figli):
        if stato:
            padre = stato[:-1]
            if stato not in figli.setdefault(padre, []):
                figli[padre].append(stato)
    foglie = [s for s in figli if not figli[s]]
    pos = {}
    for i, f in enumerate(foglie):
        pos[f] = (x0 + (i + 0.5) * W / len(foglie), y0 + len(f) * dy)

    def posiziona(s):
        if s in pos:
            return pos[s][0]
        xs = [posiziona(c) for c in figli[s]]
        pos[s] = (sum(xs) / len(xs), y0 + len(s) * dy)
        return pos[s][0]

    posiziona(())
    return pos, figli


def _bt_fmt(stato, tipo):
    if tipo == "sub":
        return "(" + ", ".join(str(i + 1) if v is True else "−" for i, v in enumerate(stato)) + ")"
    return "(" + ", ".join(str(v) for v in stato) + ")" if stato else "()"


def _bt_anim(nome_file, titolo, n, candidati, tipo):
    an = Animazione(titolo, 880, 480, 0.8)
    eventi = _bt_esegui(n, candidati)
    pos, figli = _bt_albero(eventi, n)
    visitati, sol = set(), []

    def etichetta(s):
        if not s:
            return "·"
        v = s[-1]
        return "−" if v is False else (str(len(s)) if v is True else str(v))

    def scena(corrente, righe, nota):
        s = ""
        for p, fs in figli.items():
            for c in fs:
                col = BLU if c in visitati else GRIGIO
                s += line(*pos[p], *pos[c], col, 2.4 if c in visitati else 1.2)
        for st, (x, y) in pos.items():
            if st == corrente:
                f, sw, col = EVID, 3.5, ARANCIO
            elif st in sol:
                f, sw, col = ORDINATO, 1.5, TESTO
            elif st in visitati:
                f, sw, col = "#d0e8f7", 1.5, TESTO
            else:
                f, sw, col = "#ffffff", 1, GRIGIO
            s += circle(x, y, 13, f, col, sw)
            s += t(x, y + 5, etichetta(st), 12, TESTO, "middle", True)
        s += t(20, 345, "vettore a = " + _bt_fmt(corrente, tipo) + f"   (k = {len(corrente)})", 14, TESTO, bold=True)
        soluzioni = "  ".join(("{" + ",".join(str(i + 1) for i, v in enumerate(x) if v is True) + "}") if tipo == "sub" else "".join(map(str, x)) for x in sol)
        s += t(20, 370, "soluzioni trovate: " + (soluzioni or "—"), 13, VERDE, bold=True)
        s += t(20, 408, nota, 13, TESTO)
        s += an.pseudocodice(PSEUDO_BT, righe, 520, 70, 330, 22)
        return s

    an.frame(scena((), set(), "albero di tutte le configurazioni: si parte dal vettore vuoto"), "si parte da a = ()")
    visti_una_volta = set()
    for stato, ev in eventi:
        if ev == "sol":
            visitati.add(stato)
            sol.append(stato)
            an.frame(scena(stato, {1, 2}, f"k = n = {n}: a è una soluzione → print {_bt_fmt(stato, tipo)}"), f"soluzione {_bt_fmt(stato, tipo)}")
        elif ev == "entra":
            visitati.add(stato)
            an.frame(scena(stato, {1, 2, 4, 5}, f"a = {_bt_fmt(stato, tipo)} non è una soluzione: k = k + 1, si calcolano i candidati S_k = " +
                           ("(true, false)" if tipo == "sub" else "{1..n} − a")), f"si estende {_bt_fmt(stato, tipo)}")
        else:
            an.frame(scena(stato, {6, 7, 8, 9}, "ritorno dalla chiamata ricorsiva: l'ultimo elemento viene tolto e si prova il candidato successivo (se c'è)"),
                     f"si torna a {_bt_fmt(stato, tipo)}")
    an.frame(scena((), set(), f"tutte le configurazioni sono state visitate esattamente una volta: {len(sol)} soluzioni"), f"{len(sol)} soluzioni", 2.5)
    an.salva(nome_file)


def backtracking_anim():
    _bt_anim("animazione-backtracking.svg", "Backtracking: tutti i sottoinsiemi di {1,2,3} (S_k = (true, false), slide p. 15)", 3,
             lambda a, k, n: [True, False], "sub")


def generazione_di_permutazioni_anim():
    _bt_anim("animazione-generazione-di-permutazioni.svg", "Backtracking: tutte le permutazioni di {1,2,3} (S_k = {1,…,n} − a, slide p. 21)", 3,
             lambda a, k, n: [i for i in range(1, n + 1) if i not in a[1:k]], "perm")


if __name__ == "__main__":
    backtracking_anim()
    generazione_di_permutazioni_anim()
    backpropagation_anim()
    bfs_anim()
    print_path_anim()
    dfs_anim()
    topological_sort_anim()
    dijkstra_anim()
    splay()
    splay_tree_operazioni()
    left_rotate()
    rb_insert()
    rb_delete()
    max_heapify()
    build_max_heap()
    heapsort()
    heap_extract_max()
    heap_increase_key()
    max_heap_insert()
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
