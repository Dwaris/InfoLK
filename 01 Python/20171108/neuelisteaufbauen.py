# Initialisierung
xWerte = [-2, -1, 0, 0.5, 1, 1.5, 2]
# Verarbeitung
yWerte = []
for x in xWerte:
    y = x*x - 4
    yWerte = yWerte + [y]
# Ausgabe
print(xWerte)
print(yWerte)
