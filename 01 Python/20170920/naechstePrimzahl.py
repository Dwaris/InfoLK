zahl = int(input("Natürliche Zahl: "))

gefunden = False

# Wiederholt bis gefunden
while not gefunden:

    # Geht eine Zahl weiter
    zahl = zahl + 1

    # Prüft, ob Zahl eine Primzahl ist
    anzahlTeiler = 0
    
    for i in range(1, zahl + 1):
        if zahl % i == 0:
            anzahlTeiler = anzahlTeiler + 1
    
    if anzahlTeiler == 2:
        gefunden = True

print(zahl, "ist die nächste Primzahl!")
