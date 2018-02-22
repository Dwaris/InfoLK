# Eingabe
zahl = int(input("Gib eine Zahl ein: "))

# Verarbeitung
anzahl_teiler = 0
i = 1
while i <= zahl:
    if zahl % i == 0:
        #print(i, "ist ein Teiler von", zahl)
        anzahl_teiler = anzahl_teiler + 1
    i = i + 1

# Ausgabe
if anzahl_teiler == 2:
    print(zahl, "ist eine Primzahl :-D")
else:
    print(zahl, "ist keine Primzahl :-|")
