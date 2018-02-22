# Initialisierung
primfaktoren = [2, 2, 3, 7]
primfaktor = int(input("Welcher Primfaktor von " + str(primfaktoren) + "?"))

# Verarbeitung
anzahl = 0
for element in primfaktoren:
    if element == primfaktor:
        anzahl = anzahl + 1

# Ausgabe
print(primfaktor, "kommt", anzahl, "mal vor!")
