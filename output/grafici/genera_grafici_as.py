"""Grafici di funzione (🧩) per il wiki di Algoritmi e Strutture Dati.

Solo libreria standard: scrive SVG direttamente. Esecuzione (da questa cartella):
    python genera_grafici_as.py

Grafici prodotti:
- grafico-big-oh-esempio.svg          02-Notazione asintotica p.21 (3n^2-100n+6 vs 3n^2 vs 0.01n^3)
- grafico-theta-rapporto.svg          02-Notazione asintotica p.22-23 (f(n)/n^2 -> 3, soglia 2.99)
- grafico-crescita-funzioni.svg       02-Notazione asintotica p.36-37 (scala logaritmica)
- grafico-razzo-vela-solare.svg       02-Notazione asintotica p.30 (dominanza asintotica)
- grafico-array-dinamico.svg          04-Strutture dati elementari p.10-11 (copie totali <= 2n)
- grafico-insertion-sort-casi.svg     05-Insertion sort p.20-22 (test del while: caso migliore e peggiore)
"""
import math

COLORI = ["#268bd2", "#dc322f", "#859900", "#b58900", "#6c71c4", "#2aa198", "#d33682", "#586e75"]
W, H = 640, 400
ML, MR, MT, MB = 70, 190, 40, 50        # margini (a destra la legenda)


class Grafico:
    def __init__(self, titolo, xmin, xmax, ymin, ymax, xlabel, ylabel, logy=False, logx=False):
        self.t, self.logx, self.logy = titolo, logx, logy
        self.xmin, self.xmax = (math.log10(xmin), math.log10(xmax)) if logx else (xmin, xmax)
        self.ymin, self.ymax = (math.log10(ymin), math.log10(ymax)) if logy else (ymin, ymax)
        self.xl, self.yl = xlabel, ylabel
        self.el, self.leg = [], []

    def px(self, x):
        x = math.log10(x) if self.logx else x
        return ML + (x - self.xmin) / (self.xmax - self.xmin) * (W - ML - MR)

    def py(self, y):
        y = math.log10(y) if self.logy else y
        y = min(max(y, self.ymin), self.ymax)
        return H - MB - (y - self.ymin) / (self.ymax - self.ymin) * (H - MT - MB)

    def curva(self, xs, f, nome, colore, tratteggio=False):
        punti = []
        for x in xs:
            y = f(x)
            if y is None or (self.logy and y <= 0):
                continue
            ly = math.log10(y) if self.logy else y
            if not (self.ymin - 1e-9 <= ly <= self.ymax + 1e-9):
                continue                          # fuori scala: il tratto viene tagliato
            punti.append(f"{self.px(x):.1f},{self.py(y):.1f}")
        d = ' stroke-dasharray="6 4"' if tratteggio else ""
        self.el.append(f'<polyline fill="none" stroke="{colore}" stroke-width="2"{d} points="{" ".join(punti)}"/>')
        self.leg.append((nome, colore, tratteggio))

    def vline(self, x, testo):
        X = self.px(x)
        self.el.append(f'<line x1="{X:.1f}" y1="{MT}" x2="{X:.1f}" y2="{H-MB}" stroke="#657b83" stroke-dasharray="3 3"/>')
        vicino_bordo = X > W - MR - 80
        xt, anc = (X - 4, "end") if vicino_bordo else (X + 4, "start")
        self.el.append(f'<text x="{xt:.1f}" y="{MT+14}" font-size="12" fill="#657b83" text-anchor="{anc}">{testo}</text>')

    def assi(self, xticks, yticks, fx=str, fy=str):
        out = [f'<line x1="{ML}" y1="{H-MB}" x2="{W-MR}" y2="{H-MB}" stroke="#333"/>',
               f'<line x1="{ML}" y1="{MT}" x2="{ML}" y2="{H-MB}" stroke="#333"/>']
        for x in xticks:
            X = self.px(x)
            out.append(f'<line x1="{X:.1f}" y1="{H-MB}" x2="{X:.1f}" y2="{H-MB+5}" stroke="#333"/>')
            out.append(f'<text x="{X:.1f}" y="{H-MB+18}" font-size="11" text-anchor="middle">{fx(x)}</text>')
        for y in yticks:
            Y = self.py(y)
            out.append(f'<line x1="{ML-5}" y1="{Y:.1f}" x2="{ML}" y2="{Y:.1f}" stroke="#333"/>')
            out.append(f'<line x1="{ML}" y1="{Y:.1f}" x2="{W-MR}" y2="{Y:.1f}" stroke="#eee8d5"/>')
            out.append(f'<text x="{ML-8}" y="{Y+4:.1f}" font-size="11" text-anchor="end">{fy(y)}</text>')
        out.append(f'<text x="{(ML+W-MR)/2}" y="{H-12}" font-size="12" text-anchor="middle">{self.xl}</text>')
        out.append(f'<text x="16" y="{(MT+H-MB)/2}" font-size="12" text-anchor="middle" '
                   f'transform="rotate(-90 16 {(MT+H-MB)/2})">{self.yl}</text>')
        self.el = out + self.el

    def salva(self, nome_file):
        leg = []
        for i, (nome, col, tr) in enumerate(self.leg):
            y = MT + 10 + i * 22
            d = ' stroke-dasharray="6 4"' if tr else ""
            leg.append(f'<line x1="{W-MR+12}" y1="{y}" x2="{W-MR+36}" y2="{y}" stroke="{col}" stroke-width="2"{d}/>')
            leg.append(f'<text x="{W-MR+42}" y="{y+4}" font-size="12">{nome}</text>')
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
               f'font-family="sans-serif"><rect width="100%" height="100%" fill="white"/>'
               f'<text x="{W/2}" y="22" font-size="14" text-anchor="middle" font-weight="bold">{self.t}</text>'
               + "".join(self.el) + "".join(leg) + "</svg>")
        with open(nome_file, "w", encoding="utf-8") as f:
            f.write(svg)
        print("scritto", nome_file)


def big_oh_esempio():
    g = Grafico("3n² − 100n + 6 = O(n²) e O(n³)", 0, 320, 0, 320000, "n", "passi")
    xs = range(0, 321, 2)
    g.curva(xs, lambda n: 3*n*n - 100*n + 6, "3n² − 100n + 6", COLORI[0])
    g.curva(xs, lambda n: 3*n*n, "3n²", COLORI[3])
    g.curva(xs, lambda n: 0.01*n**3, "0.01n³", COLORI[2])
    g.vline(300, "n = 300")
    g.assi(range(0, 321, 50), range(0, 300001, 50000), fy=lambda y: f"{y//1000}k")
    g.salva("grafico-big-oh-esempio.svg")


def theta_rapporto():
    g = Grafico("f(n)/n² con f(n) = 3n² − 100n + 6", 100, 1e6, 2.0, 3.02, "n (scala log)",
                "f(n) / n²", logx=True)
    xs = [10 ** (k / 50) for k in range(100, 301)]
    g.curva(xs, lambda n: (3*n*n - 100*n + 6) / (n*n), "f(n)/n²", COLORI[0])
    g.curva(xs, lambda n: 3.0, "c₂ = 3 (O)", COLORI[1], True)
    g.curva(xs, lambda n: 2.99, "c₁ = 2.99 (Ω)", COLORI[2], True)
    g.vline(10000, "n₀ = 10⁴")
    g.assi([100, 1000, 1e4, 1e5, 1e6], [2.0, 2.2, 2.4, 2.6, 2.8, 3.0],
           fx=lambda x: f"10^{int(round(math.log10(x)))}", fy=lambda y: f"{y:.2f}")
    g.salva("grafico-theta-rapporto.svg")


def crescita():
    g = Grafico("Crescita delle funzioni (scala log)", 1, 50, 1, 1e20, "n", "f(n)", logy=True)
    xs = [k / 4 for k in range(4, 201)]
    fun = [("lg n", lambda n: max(math.log2(n), 1e-9) if n > 1 else None),
           ("√n", math.sqrt), ("n", lambda n: n), ("n lg n", lambda n: n * math.log2(n) if n > 1 else None),
           ("n²", lambda n: n**2), ("n³", lambda n: n**3), ("2ⁿ", lambda n: 2.0**n),
           ("n!", lambda n: math.gamma(n + 1))]
    for (nome, f), c in zip(fun, COLORI):
        g.curva(xs, f, nome, c)
    g.assi([1, 10, 20, 30, 40, 50], [1, 1e5, 1e10, 1e15, 1e20],
           fy=lambda y: f"10^{int(round(math.log10(y)))}")
    g.salva("grafico-crescita-funzioni.svg")


def razzo_vela():
    # valori illustrativi: razzo accelera forte fino a t=2 poi velocità costante v_r = 10; vela v = a t, a = 0.5
    g = Grafico("Razzo vs vela solare (dominanza asintotica)", 0, 40, 0, 20, "t", "velocità")
    xs = [k / 10 for k in range(0, 401)]
    g.curva(xs, lambda t: 5 * t if t < 2 else 10, "razzo: v_r costante", COLORI[1])
    g.curva(xs, lambda t: 0.5 * t, "vela: v_s = a·t", COLORI[0])
    g.vline(20, "t = v_r / a")
    g.assi(range(0, 41, 10), range(0, 21, 5))
    g.salva("grafico-razzo-vela-solare.svg")


def array_dinamico():
    def copie(n):
        cap, dim, tot = 1, 0, 0
        for _ in range(n):
            if dim == cap:
                tot += dim
                cap *= 2
            dim += 1
        return tot
    g = Grafico("Array dinamico: elementi ricopiati", 1, 140, 0, 280, "n (elementi inseriti)", "copie totali")
    xs = list(range(1, 141))
    g.curva(xs, copie, "copie effettive", COLORI[0])
    g.curva(xs, lambda n: 2 * n, "2n (limite di p.11)", COLORI[1], True)
    g.curva(xs, lambda n: n, "n", COLORI[7], True)
    g.assi([1, 16, 32, 64, 128], range(0, 281, 40))
    g.salva("grafico-array-dinamico.svg")


def insertion_sort_casi():
    # numero totale di test del while (sum t_j) dalle formule di p.20 e p.22
    g = Grafico("Insertion sort: test del while", 1, 60, 0, 1900, "n", "sum t_j")
    xs = list(range(1, 61))
    g.curva(xs, lambda n: n * (n + 1) / 2 - 1, "peggiore: n(n+1)/2 − 1", COLORI[1])
    g.curva(xs, lambda n: n - 1, "migliore: n − 1", COLORI[0])
    g.curva(xs, lambda n: n * n / 2, "n²/2", COLORI[7], True)
    g.assi([1, 10, 20, 30, 40, 50, 60], range(0, 1801, 300))
    g.salva("grafico-insertion-sort-casi.svg")


if __name__ == "__main__":
    big_oh_esempio()
    theta_rapporto()
    crescita()
    razzo_vela()
    array_dinamico()
    insertion_sort_casi()
