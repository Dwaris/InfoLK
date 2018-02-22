# Initialisierung
kapital = float(input("Kapital: "))
zinssatz = float(input("Zinssatz: "))
jahre = int(input("Jahre: "))
jahr = 0

# Iterierung und Ausgabe
while jahr < jahre:
    zinsen = kapital * (zinssatz/100)
    kapital = kapital + zinsen
    jahr = jahr + 1
    print("Kapital nach", jahr, "Jahren:", kapital)

    
    