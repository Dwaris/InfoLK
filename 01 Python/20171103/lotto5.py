from random import *

tipp = []
for i in range(6):
    tipp = tipp + [int(input(str(i + 1) + "-te Zahl: "))]
print("Getippte Zahlen: " + str(tipp))

erfolge = [0, 0, 0, 0, 0, 0, 0]
anzahl = int(input("Anzahl der Ziehungen: "))
for n in range(anzahl):

    ziehung = []
    for i in range(6):
        zahl = randint(1, 49)
        while (zahl in ziehung):
            zahl = randint(1, 49)
        ziehung = ziehung + [zahl]
    
    richtige = 0
    for i in ziehung:
        if i in tipp:
            richtige = richtige + 1
    
    erfolge[richtige] = erfolge[richtige] + 1

print("")
print("Ergebnis:")
for i in range(7):
    print(str(i) + " Richtige: " + str(erfolge[i]) + " mal! (" + str(100 * float(erfolge[i] / float(anzahl))) + "%)")
