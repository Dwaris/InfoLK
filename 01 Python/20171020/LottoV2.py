ziehung = [1, 3, 10, 30, 46, 49]
tipp = [0] * 6
richtige = 0
counter = 0
for t in tipp:
    tipp[counter] = int(input("Zahl von 1-49"))
    t+=1
    counter+=1
counter = 0
for z in ziehung:
    if z in tipp:
        richtige+=1
        print("{} ist Richtig".format(ziehung[counter]))
    counter +=1
# Ausgabe
print("{} Richtige".format(richtige))