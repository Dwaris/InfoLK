# Eingabe
zahl = int(input("Gib eine Zahl ein: "))

# Verarbeitung
binaer = ""
while zahl > 0:

    # Bestimmt Ergebnis der Division durch 2 mit Rest
    division = zahl // 2
    rest = zahl % 2

    # Ergänzt beim Ergebnis 0 oder 1
    if rest == 0:
        binaer = "0" + binaer
    else:
        binaer = "1" + binaer

    # Ersetzt Zahl durch Ergebnis der Division durch 2
    zahl = division

# Ausgabe
print(binaer)
