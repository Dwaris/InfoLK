tipp = []
for i in range(6):
    eingabe = input(str(i + 1) +  "-te Zahl: ")
    
    tipp = tipp + [int(eingabe)]
print("Getippte Zahlen: " + str(tipp))

ziehung = [3, 6, 10, 28, 30, 47]
print("Gezogene Zahlen: " + str(ziehung))

print("")
richtige = 0
for i in ziehung:
    if i in tipp:
        print(str(i) + " ist richtig!")
        richtige = richtige + 1

print("")
print(str(richtige) + " Richtige!")
