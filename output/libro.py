"""Navigazione «a libro» del wiki (wiki/lezioni.md = indice).

L'indice wiki/lezioni.md elenca, capitolo per capitolo, le pagine nell'ordine di lettura.
Questo script legge l'indice e scrive in fondo a ogni pagina elencata una barra
«← precedente · Indice · successiva →», racchiusa tra i marcatori
<!-- nav:inizio --> e <!-- nav:fine -->, sostituendo quella vecchia se c'è.

Va rieseguito ogni volta che si aggiunge una pagina all'indice:
    python output/libro.py            (dalla cartella del vault)
"""
import os
import re
import sys

WIKI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "wiki")
INIZIO, FINE = "<!-- nav:inizio -->", "<!-- nav:fine -->"


def file_di(pagina):
    for radice, _, files in os.walk(WIKI):
        if pagina + ".md" in files:
            return os.path.join(radice, pagina + ".md")
    sys.exit(f"pagina non trovata: {pagina}")


SIMBOLI = {r"\Omega": "Ω", r"\Theta": "Θ", r"\lg": "lg", "$": ""}


def titolo(pagina, apertura=False):
    """Titolo H1 della pagina, ripulito per l'etichetta di un link; «Introduzione e riepilogo» per l'apertura."""
    if apertura:
        return "Introduzione e riepilogo"
    for riga in open(file_di(pagina), encoding="utf-8"):
        if riga.startswith("# "):
            t = riga[2:].strip()
            for k, v in SIMBOLI.items():
                t = t.replace(k, v)
            return re.sub(r"[\[\]|]", "", t)
    return pagina


def leggi_indice():
    capitoli, corrente = [], None
    for riga in open(os.path.join(WIKI, "lezioni.md"), encoding="utf-8"):
        riga = riga.rstrip("\n").rstrip("\r")
        if riga.startswith("## "):
            corrente = (riga[3:].split(" — ")[0], [])
            capitoli.append(corrente)
        m = re.match(r"^\d+\. \[\[([^\]|#]+)", riga)
        if m and corrente:
            corrente[1].append(m.group(1))
    return capitoli


def etichetta(pagina, aperture):
    """Nella barra la pagina d'apertura porta anche il nome del capitolo, per i salti tra lezioni."""
    return f"{aperture[pagina]}: introduzione e riepilogo" if pagina in aperture else titolo(pagina)


def barra(cap, k, tot, prec, succ, aperture):
    parti = [f"**{cap} · pagina {k} di {tot}**"]
    parti.append(f"← [[{prec}|{etichetta(prec, aperture)}]]" if prec else "← inizio del libro")
    parti.append("[[lezioni|Indice]]")
    parti.append(f"[[{succ}|{etichetta(succ, aperture)}]] →" if succ else "fine del libro →")
    return f"{INIZIO}\n---\n" + " · ".join(parti) + f"\n{FINE}\n"


def riscrivi_indice(aperture):
    """Aggiorna le etichette dei link dell'indice con i titoli correnti delle pagine (l'ordine non cambia)."""
    f = os.path.join(WIKI, "lezioni.md")
    s = open(f, encoding="utf-8").read()
    s = re.sub(r"^(\d+)\. \[\[([^\]|#]+)(\|[^\]]*)?\]\]",
               lambda m: f"{m.group(1)}. [[{m.group(2)}|{titolo(m.group(2), m.group(2) in aperture)}]]", s, flags=re.M)
    open(f, "w", encoding="utf-8").write(s)


def main():
    capitoli = leggi_indice()
    sequenza = [(cap, k + 1, len(pag), p) for cap, pag in capitoli for k, p in enumerate(pag)]
    viste = [p for *_, p in sequenza]
    doppie = {p for p in viste if viste.count(p) > 1}
    if doppie:
        sys.exit(f"pagine ripetute nell'indice: {sorted(doppie)}")
    aperture = {pag[0]: cap for cap, pag in capitoli if pag}
    riscrivi_indice(aperture)
    for i, (cap, k, tot, p) in enumerate(sequenza):
        prec = sequenza[i - 1][3] if i > 0 else None
        succ = sequenza[i + 1][3] if i + 1 < len(sequenza) else None
        f = file_di(p)
        s = open(f, encoding="utf-8", newline="").read()
        nl = "\r\n" if "\r\n" in s else "\n"
        s = s.replace("\r\n", "\n")
        s = re.sub(r"\n*" + re.escape(INIZIO) + r".*?" + re.escape(FINE) + r"\n*", "\n", s, flags=re.S)
        s = s.rstrip("\n") + "\n\n" + barra(cap, k, tot, prec, succ, aperture)
        open(f, "w", encoding="utf-8", newline="").write(s.replace("\n", nl))
    print(f"barra di navigazione scritta in {len(sequenza)} pagine ({len(capitoli)} capitoli)")


if __name__ == "__main__":
    main()
