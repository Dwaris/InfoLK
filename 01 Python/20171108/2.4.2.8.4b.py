# Initialisierung
primfaktoren = [2, 2, 3, 7]
gesucht = int(input(" Gesuchte Primzahl: "))
zaehler = 0

# Verarbeitung
for i in range(len(primfaktoren)):
    if gesucht == primfaktoren[i]:
        zaehler = zaehler + 1

# Ausgabe
print('Primfaktoren:', primfaktoren)
print("Die Primzahl", gesucht, "ist", str(zaehler) + "-mal vorgekommen")
