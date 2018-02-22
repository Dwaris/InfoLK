# Initialisierung
primfaktoren = [[2, 2], [3, 1], [5, 0], [7, 1]]

# Verarbeitung
produkt = 1
for element in primfaktoren:
    produkt = produkt * (element[0] ** element[1])

# Ausgabe
print('Primfaktoren:', primfaktoren)
print('Zahl:', produkt)
