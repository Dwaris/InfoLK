ziehung = [1, 3, 10, 30, 46, 49]
tipp = [3, 6, 10, 28, 31, 10]
richtige = 0
counter = 0
for z in ziehung:
    if z in tipp:
        richtige+=1
        print("{} ist richtig".format(ziehung[counter]))
    counter +=1
# Ausgabe
print("{} richtige".format(richtige))