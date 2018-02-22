#Es gibt zwei zufällige Zahlen aus, die man multiplizieren soll. Gibt je nach Antwort richtig oder falsch aus und fragt ob man weiter spielen will

from random import randint

print("Teste deine Kopfrechenfähigkeiten!")
maximum = 20
genug = False
richtig = True
counter = 0
while richtig and (not genug):
    print("Noch ein Test?")
    antwort = input("Antwort(j/n): ")
    if antwort == "j":
        zahl1 = randint(1,maximum)
        zahl2 = randint(2,maximum   )
        produkt = zahl1 * zahl2
        print(zahl1, " * ",zahl2)
        ergebnis = int(input("Ergebnis: "))
        if ergebnis == produkt:
            print("richtig!")
            counter += 1
        else:
            print("falsch!")
            richtig = False
    else:
        genug = True

print("Du hast {} Fragen richtig beantwortet".format(counter))
