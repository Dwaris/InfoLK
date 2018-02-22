from random import *

ziehung = [1, 2, randint(1,49), randint(1,49), randint(1,49), randint(1,49)]
counter = 0
richtige = []
tipp = [0] * 6

for t in tipp:
    tipp[counter] = int(input("Zahl von 1-49: "))
    t+=1
    counter+=1
counter = 0
for z in ziehung:
    if z in tipp:
        richtige = richtige + [ziehung[counter]]
    counter +=1
# Ausgabe
if len(richtige) > 0:
    sarr = [str(a) for a in richtige]
    if len(richtige) == 1:
        print(", ".join(sarr), "ist richtig")
    else:
        print(", ".join(sarr), "sind richtig")
else:
    print("Keine richtigen Zahlen")
