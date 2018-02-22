def quadratzahl(n):
    i = 1
    while i+i+1 < n:
        i = i + 1
    if i+i+1 == n:
        ergebnis = True
    else:
        ergebnis = False
    return ergebnis
print(quadratzahl(8))