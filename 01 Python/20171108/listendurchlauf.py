# Initialisierung
primfaktoren = [[2, 2], [3, 1], [5, 0], [7, 1]]
# Verarbeitung
produkt = 1
for i in range(len(primfaktoren)):
    produkt = produkt * (primfaktoren[i][0] ** primfaktoren[i][1])
# Ausgabe
print('Primfaktoren:', primfaktoren)
print('Zahl:', produkt)
