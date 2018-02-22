# Eingabe
x1 = float(input("x-Koordinate des ersten Punktes: "))
y1 = float(input("y-Koordinate des ersten Punktes: "))
x2 = float(input("x-Koordinate des zweiten Punktes: "))
y2 = float(input("y-Koordinate des zweiten Punktes: "))

# Verarbeitung
steigung = (y2 - y1) / (x2 - x1)
abschnitt = y1 - steigung * x1

# Ausgabe
print ("f(x) = " + str(steigung) + "*x + " + str(abschnitt))