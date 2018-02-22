zahl = int(input("Natürliche Zahl: "))

gefunden = False

# Wiederholt bis gefunden
while not gefunden:

    # Geht eine Zahl weiter
    zahl = zahl + 1

    # Prüft, ob Zahl eine Quadratzahl ist
    for i in range(1, zahl):
        if i * i == zahl:
            gefunden = True
    
print(zahl, "ist die nächste Quadratzahl!")
