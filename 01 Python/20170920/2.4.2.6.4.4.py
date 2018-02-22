#input
n = int(input("natürliche Zahl: "))
prim = True
k=2
quad = 1
gefunden = False
hlp = n + 1
#process
while not gefunden:
    k=2
    prim = True
    while k*k <=n and prim == True:
        if n % k == 0:
            prim = False
        k = k+1
    gefunden = prim
    hlp += 1

gefunden = False
while not gefunden:
    if quad**2 <= n:
        gefunden = False
        quad += 1
    else:
        gefunden = True
#output
print("Die nächste Quadratzahl ist {} und die nächste Primzahl ist {}".format(quad**2,hlp-1))
