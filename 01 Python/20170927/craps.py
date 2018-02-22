from random import randint

# Gewinne zählen
anzahlGewinne = 0

# anzahl mal spielen
anzahl = 100
for i in range(anzahl):
    
    # Wuerfel werfen
    wuerfel1 = randint(1, 6)
    wuerfel2 = randint(1, 6)
    print("Würfeln... ", wuerfel1, wuerfel2)

    # Erste Runde auswerten
    fertig = False
    augensumme = wuerfel1 + wuerfel2
    if (augensumme == 7) or (augensumme == 11):
        gewonnen = True
        fertig = True
        print("Gewonnen!")
    elif (augensumme == 2) or (augensumme == 3) or (augensumme == 12):
        gewonnen = False
        fertig = True

    # Spielen bis fertig
    while not fertig:
        
        # Wuerfel werfen
        wuerfel1 = randint(1, 6)
        wuerfel2 = randint(1, 6)
        print("Würfeln... ", wuerfel1, wuerfel2)
        
        # Naechste Runde auswerten
        augensummeNeu = wuerfel1 + wuerfel2
        
        if (augensummeNeu == 7):
            gewonnen = False
            fertig = True
        elif (augensummeNeu == augensumme):
            gewonnen = True
            fertig = True

    # Ergebnis ausgeben
    if gewonnen:
        print('Gewonnen!')
        anzahlGewinne = anzahlGewinne + 1
    else:
        print('Verloren!')
    print("---------------")

# Gewinnwahrscheinlichkeit ausgeben
gewinnwahrscheinlichkeit = anzahlGewinne / anzahl * 100
print("Die Gewinnwahrscheinlichkeit beträgt", gewinnwahrscheinlichkeit, "%!")
