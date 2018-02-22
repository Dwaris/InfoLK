from random import *

tipp = []
for i in range(6):
    tipp = tipp + [int(input(str(i + 1) + "-te Zahl: "))]
print("Getippte Zahlen: " + str(tipp))

richtige = 0
n = 0
while (richtige != 6):

    ziehung = []
    n = n + 1
    for i in range(6):
        zahl = randint(1, 49)
        while (zahl in ziehung):
            zahl = randint(1, 49)
        ziehung = ziehung + [zahl]
    
    richtige = 0
    for i in ziehung:
        if i in tipp:
            richtige = richtige + 1
    if n % 10000 == 0:
        print("Ziehungen: " + str(n))

print("Sechs Richtige nach " + str(n) + " Ziehungen!")
