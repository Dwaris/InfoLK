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
    F = []
    while n%2 == 0:
        F.append(2)
        n = n/2
    while n%3 == 0:
        F.append(3)
        n = n/3
    t = 5
    diff = 2
    while t*t <= n:
        while n%t == 0:
            F.append(t)
            n = n/t
        t = t + diff
        diff = 6 - diff
    if n > 1:
        F.append(n)
    return F
