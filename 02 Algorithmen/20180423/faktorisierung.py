from time import *
from random import randint
def primfaktoren(n):
    faktoren = []
    z = n
    while z > 1:
        i = 2
        gefunden = False
        while i*i <= z and not gefunden:
            if z % i == 0:
                gefunden = True
                p = i
            else:
                i = i + 1
        if not gefunden:
            p = z
        faktoren = faktoren + [p]
        z = z // p
    return faktoren
#primfaktoren(56576543432454321679739)
#primfaktoren(484639526894037745950720)
for i in range (10000000000000,1000000000000000000000,randint(1,9)):
    t1 = clock()
    primfaktoren(i)
    t2 = clock()
    print(i,t2 -t1)
