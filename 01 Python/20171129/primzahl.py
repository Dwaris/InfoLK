def primzahl(n):
    prim = True
    if n == 1:
        prim = False
    else:
        i = 2
        while i <= n-1:
            if n % i == 0:
                prim = False
            i = i+1
    return prim

def naechstGroesserePrimzahl(n):
    n = n + 1
    while primzahl(n) == False:
        n = n + 1
    return n

def primzahlenZwischen(a, b):
    primzahlen = []
    i = a
    while i <= b:
        if primzahl(i):
            primzahlen = primzahlen + [i]
        i = i + 1
    return primzahlen

def primfaktoren(n):
    zahl = n
    faktoren = []
    i = 2
    while i <= n:
        if primzahl(i):
            while zahl % i == 0:
                zahl = zahl // i
                faktoren = faktoren + [i]
        i = i + 1
    return faktoren
