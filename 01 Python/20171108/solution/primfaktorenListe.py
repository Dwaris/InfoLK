# Initialisierung
primfaktoren = [2, 2, 3, 7]

# Verarbeitung
produkt = 1
for element in primfaktoren:
    produktNeu = produkt * element
    print(produkt, "*", element, "=", produktNeu)
    produkt = produktNeu

# Ausgabe
print('Primfaktoren:', primfaktoren)
print('Zahl:', produkt)
