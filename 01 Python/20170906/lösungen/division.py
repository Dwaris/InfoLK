# Eingabe
a = int(input("Erste Zahl: "))
b = int(input("zweite Zahl: "))

# Verarbeitung
zaehler = 0
while a >= b:
    a = a - b
    zaehler = zaehler + 1

# Ausgabe
print("Zähler:", zaehler)
