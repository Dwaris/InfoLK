# Initialisierung
L = [10, 17, 3, 19, 2]
#L = [10, -17, 3, -19, 2]

# Verarbeitung
trifftzu = True
for e in L:
    if e[0] < 0:
        trifftzu = False

# Ausgabe
if trifftzu == True:
    print(L, 'enthält nur positive Zahlen.')
else:
    print(L, 'enthält auch negative Zahlen.')
