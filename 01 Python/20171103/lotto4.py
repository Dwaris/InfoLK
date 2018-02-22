from random import *

tipp = []
for i in range(6):
    tipp = tipp + [int(input(str(i + 1) + "-te Zahl: "))]
print("Getippte Zahlen: " + str(tipp))

anzahl = int(input("Anzahl der Ziehungen: "))
for n in range(anzahl):

    ziehung = []
    for i in range(6):
        zahl = randint(1, 49)
        while (zahl in ziehung):
            zahl = randint(1, 49)
        ziehung = ziehung + [zahl]
    print("")
    print("Gezogene Zahlen: " + str(ziehung))
    
    richtige = 0
    for i in ziehung:
        if i in tipp:
            print(str(i) + " ist richtig!")
            richtige = richtige + 1
    print("")
    print(str(richtige) + " Richtige!")
