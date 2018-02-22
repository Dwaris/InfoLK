from random import *

# Wiederhole bis Benutzer aufhört
nochmal = "j"
while nochmal == "j":

    # Bestimme zufällige Zahl
    grenze = 99
    ratezahl = randint(0, grenze)
    print("Ich habe mir eine Zahl zwischen 0 und %g ausgedacht..." % grenze)

    # Wiederhole bis Benutzer Zahl trifft
    gefunden = False
    while not gefunden:

        # Lese Vorschlag ein
        vorschlag = int(input("Vorschlag: "))

        # Werte Vorschlag aus
        if vorschlag < ratezahl:
            print("Zu klein...")
        elif vorschlag > ratezahl:
            print("Zu gross...")
        else:
            print("Treffer!")
            gefunden = True

    nochmal = input("Nochmal (j/n)?")
    print()
