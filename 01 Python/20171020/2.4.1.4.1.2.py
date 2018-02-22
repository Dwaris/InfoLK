# Initialisierung
ziehung = [25, 40, 44, 1, 45, 21]
tipp = [1, 12, 21, 31, 37, 46]
# Verarbeitung
richtige = 0
for z in ziehung:
    for t in tipp:
        print('vergleiche: ', z, t)
        if z == t:
            richtige +=1
# Ausgabe
print(richtige)
print()
richtige = 0
for z in ziehung:
    if z in tipp:
        richtige = richtige + 1
# Ausgabe
print(richtige)