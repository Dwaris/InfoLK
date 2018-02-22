def primzahl(n):
    k = 2
    prim = True
    while k * k <=n:
        if n % k == 0:
            prim = False
        k +=1
    hlp +=1
    if n == hlp:
        primzahl = True
    return primzahl
#input
n = int(input("natürliche Zahl: "))
prim = True
k=2
gefunden = False
hlp = n
#process
while not gefunden:
    k=2
    prim = True
    while k*k <=n and prim == True:
        if n % k == 0:
            prim = False
        k += 1
    gefunden = prim
    hlp += 1
print(hlp-1)
