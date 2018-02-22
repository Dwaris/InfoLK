from random import randint
wins = 0
anzahl = 10000
#Wuerfel werfen
def wuerfel():
    wuerfel1 = randint(1,6)
    wuerfel2 = randint(1,6)
    summe = wuerfel1 + wuerfel2
    return summe;
#erste Runde auswerten
for i in range(anzahl):
    fertig = False
    augensumme = wuerfel()
    if augensumme == 7 or augensumme == 11:
        gewonnen = True
        fertig = True
    elif augensumme == 2 or augensumme == 3 or augensumme == 2:
        gewonnen = False
        fertig = True
    while not fertig:
        #Wuerfel werfen; naechste Runde auswerten
        augensummeNeu = wuerfel()
        if augensummeNeu == 7:
            gewonnen = False
            fertig = True
        elif augensumme == augensummeNeu:
            gewonnen = True
            fertig = True
    if gewonnen == True:
            wins += 1
counter = (wins / anzahl) * 100
#Ausgabe
print("Du hast eine {} % Chance zu gewinnen".format(round(counter,3)))
