quadrat = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]
    ]

summen = []

# Summen der Zeilen
for i in range(4):
    summe = 0
    for j in range(4):
        summe = summe + quadrat[i][j]
    summen = summen + [summe]

# Summen der Spalten
for i in range(4):
    summe = 0
    for j in range(4):
        summe = summe + quadrat[j][i]
    summen = summen + [summe]

# Summe der ersten Diagonalen
summe = 0
for i in range(4):
    summe = summe + quadrat[i][i]
summen = summen + [summe]

# Summe der zweiten Diagonalen
summe = 0
for i in range(4):
    summe = summe + quadrat[i][3-i]
summen = summen + [summe]

# Magie-Prüfung
summe = summen[0]
magisch = True
for i in summen:
    if i != summe:
        magisch = False

# Ausgabe
for zeile in quadrat:
    print(zeile)

if magisch:
    print("Das Quadrat ist magisch!")
else:
    print("Das Quadrat besitzt keine Magie!")
