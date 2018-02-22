breite  = int(input("Breite = "))
hoehe   = int(input("Höhe   = "))

zeile = ""
hilf = 1
for i in range(breite):
    if hilf == 4:
        zeile = zeile + "+"
        hilf = 1
    else:
        zeile = zeile + "*"
        hilf = hilf + 1

for i in range(hoehe):
    print(zeile)
