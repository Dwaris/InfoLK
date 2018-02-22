# Initialisierung
kapital = float(input("Kapital: "))
zinssatz = float(input("Zinssatz: "))
sparziel = float(input("Sparziel: "))
jahr = 0

# Iterierung und Ausgabe
while kapital < sparziel:
    zinsen = kapital * (zinssatz/100)
    kapital = kapital + zinsen
    jahr = jahr + 1
    print("Kapital nach", jahr, "Jahren:", kapital)