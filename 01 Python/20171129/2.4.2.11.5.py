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

def naechstePrimzahl(n):
    n += 1
    while primzahl(n) != True:
        n += 1
    return n

def primzahlBereich(a,b):
    l = []
    for zahl in range(a, b):
        if zahl > 1:
            for i in range(2, zahl):
                if (zahl % i) == 0:
                    break
            else:
                l += [zahl]
    return l

def primZerlegung(n):
    return 42
