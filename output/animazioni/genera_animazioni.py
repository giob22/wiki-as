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


if __name__ == "__main__":
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
