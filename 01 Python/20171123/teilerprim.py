def Teilerzahl(n):
    zaehler = 0
    i = 1
    while i<=n:
        if (n % i) == 0:
            zaehler = zaehler + 1
        i = i+1
    return zaehler

def istPrimzahl(n):
    if Teilerzahl(n) == 2:
        return True
    else:
        return False

def findeNaechstePrimzahl(n):
    zahl = n+1
    while not istPrimzahl(zahl):
        zahl += 1
    return zahl
