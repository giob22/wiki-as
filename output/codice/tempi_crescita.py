"""Verifica dei numeri sui tempi di esecuzione presenti nelle slide.

- 01-Introduzione.pdf p.11: insertion sort vs merge sort su 10^6 elementi a 10^9 op/s
- 01-Introduzione.pdf p.12: n massimo risolvibile in un tempo t se l'algoritmo impiega f(n) microsecondi
- 01-Introduzione.pdf p.33-34: 20! e 1000!
- 01-Introduzione.pdf p.59: 2^20 e 2^100
- 02-Notazione asintotica.pdf p.36: tabella della crescita delle funzioni (1 operazione = 1 ns)

Solo libreria standard. Esecuzione: python tempi_crescita.py
"""
import math

SEC = 1.0
MIN = 60 * SEC
ORA = 60 * MIN
GIORNO = 24 * ORA
MESE = 30 * GIORNO          # convenzione: mese di 30 giorni
ANNO = 365 * GIORNO         # convenzione: anno di 365 giorni
SECOLO = 100 * ANNO


def fmt_tempo(s):
    """Formatta una durata in secondi con l'unità più leggibile (come nella tabella di p.36)."""
    if s < 1e-3:
        return f"{s * 1e6:.3g} µs"
    if s < 1:
        return f"{s * 1e3:.3g} ms"
    if s < MIN:
        return f"{s:.3g} sec"
    if s < ORA:
        return f"{s / MIN:.3g} min"
    if s < GIORNO:
        return f"{s / ORA:.3g} h"
    if s < ANNO:
        return f"{s / GIORNO:.3g} days"
    return f"{s / ANNO:.3g} years"


def p11():
    print("== 01-Introduzione p.11 (10^9 operazioni al secondo) ==")
    n = 10**6
    ins = n**2 / 1e9
    mer = n * math.log2(n) / 1e9
    print(f"insertion sort: n^2 / 1e9 = {ins:.0f} s = {ins / 60:.1f} min")
    print(f"merge sort:     n lg n / 1e9 = {mer:.4f} s  (lg 10^6 = {math.log2(n):.2f})")


def p36():
    print("\n== 02-Notazione asintotica p.36 (1 operazione = 1 ns) ==")
    funzioni = {
        "lg n": lambda n: math.log2(n),
        "n": lambda n: n,
        "n lg n": lambda n: n * math.log2(n),
        "n^2": lambda n: n**2,
        "2^n": lambda n: 2.0**n,
        "n!": lambda n: float(math.factorial(n)),
    }
    righe = [10, 20, 30, 40, 50, 100, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9]
    print("n".ljust(14) + "".join(k.ljust(14) for k in funzioni))
    for n in righe:
        cella = []
        for k, f in funzioni.items():
            if k == "2^n" and n > 100 or k == "n!" and n > 30:
                cella.append("-")      # celle vuote nella slide
                continue
            cella.append(fmt_tempo(f(n) * 1e-9))
        print(str(n).ljust(14) + "".join(c.ljust(14) for c in cella))


def n_max(f, t_us, crescente_rapida=False):
    """Massimo n intero con f(n) <= t_us (f in microsecondi), per ricerca esponenziale + binaria."""
    lo, hi = 1, 2
    while f(hi) <= t_us:
        lo, hi = hi, hi * 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if f(mid) <= t_us:
            lo = mid
        else:
            hi = mid
    return lo


def p12():
    print("\n== 01-Introduzione p.12: n massimo con f(n) microsecondi <= t ==")
    tempi = {"1 second": SEC, "1 minute": MIN, "1 hour": ORA, "1 day": GIORNO,
             "1 month": MESE, "1 year": ANNO, "1 century": SECOLO}
    funzioni = {
        "sqrt n": lambda n: math.sqrt(n),
        "n": lambda n: n,
        "n lg n": lambda n: n * math.log2(n),
        "n^2": lambda n: n**2,
        "n^3": lambda n: n**3,
        "2^n": lambda n: 2.0**n,
        "n!": lambda n: float(math.factorial(n)),
    }
    print("f(n)".ljust(9) + "".join(k.ljust(12) for k in tempi))
    # lg n: n = 2^(t in µs), numero astronomico -> si scrive in forma chiusa
    print("lg n".ljust(9) + "".join(f"2^{t * 1e6:.2e}".ljust(12) for t in tempi.values()))
    for nome, f in funzioni.items():
        riga = []
        for t in tempi.values():
            t_us = t * 1e6
            if nome == "sqrt n":
                riga.append(f"{t_us**2:.2e}")   # n = t^2 esatto
            elif nome == "n":
                riga.append(f"{t_us:.2e}")
            else:
                riga.append(f"{n_max(f, t_us):.3g}" if n_max(f, t_us) < 1e6 else f"{n_max(f, t_us):.2e}")
        print(nome.ljust(9) + "".join(c.ljust(12) for c in riga))


def p33_p59():
    print("\n== 01-Introduzione p.33 e p.59 ==")
    print(f"20!   = {math.factorial(20):,}")
    f1000 = math.factorial(1000)
    print(f"1000! ≈ 10^{math.log10(f1000):.1f}  ({len(str(f1000))} cifre)")
    print(f"20! ns = {math.factorial(20) * 1e-9 / ANNO:.1f} anni (confronto con p.36: 77.1 years)")
    print(f"2^20  = {2**20:,}")
    print(f"2^100 = {2**100:.4e}")


if __name__ == "__main__":
    p11()
    p36()
    p12()
    p33_p59()
