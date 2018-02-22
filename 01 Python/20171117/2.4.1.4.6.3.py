mag_quadrat = [
    (16, 3, 2, 13),
    (5, 10, 11, 8),
    (9, 6, 7 ,12),
    (4, 15, 14, 1)
]
x = len(mag_quadrat)
q = 0
l = 0
erfüllt = False
summe_spalten = [0] * x
summe_zeilen = [0] * x
summe_diagonal = [0] * int(x/2)
while q <= 3:
    for i in mag_quadrat:
        summe_spalten[q] += mag_quadrat[q][l]
        summe_zeilen[q] += mag_quadrat[l][q]
        if q == 0:
            summe_diagonal[0] += mag_quadrat[l][l]
            summe_diagonal[1] += mag_quadrat[l][abs(3 - l)]
        l += 1
        if l == 4:
            q += 1
            l = 0
print(summe_spalten, summe_zeilen, summe_diagonal)
if (all(s==summe_diagonal[0] for s in summe_diagonal)) and (all(s==summe_spalten[0] for s in summe_spalten)) and (all(s==summe_spalten[0] for s in summe_zeilen)) == True:
    print("Es ist ein magisches Quadrat")
else:
    print("Es ist KEIN magisches Quadrat")