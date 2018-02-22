# Initialisierung
L = [-1, 23, 3, 42, 5]
# Verarbeitung
trifftzu = True
for e in L:
    if e < 0:
        trifftzu = False
# Ausgabe
if trifftzu == True:
    print('Alle Zahlen sind Positiv.')
else:
    print('Nicht alle Zahlen sind Positiv.')
