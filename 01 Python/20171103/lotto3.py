from random import *

tipp = []
for i in range(6):
    tipp = tipp + [int(input(str(i + 1) + "-te Zahl: "))]
print("Getippte Zahlen: " + str(tipp))

ziehung = []
for i in range(6):
    zahl = randint(1, 49)
    while (zahl in ziehung):
        zahl = randint(1, 49)
    ziehung = ziehung + [zahl]
print("Gezogene Zahlen: " + str(ziehung))

print("")
richtige = 0
for i in ziehung:
    if i in tipp:
        print(str(i) + " ist richtig!")
        richtige = richtige + 1

print("")
print(str(richtige) + " Richtige!")
