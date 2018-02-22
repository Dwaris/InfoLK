# Eingabe
x1 = float(input("Punkt 1 x: "))
y1 = float(input("Punkt 1 y: "))
x2 = float(input("Punkt 2 x: "))
y2 = float(input("Punkt 2 y: "))

# Verarbeitung
if x1 == x2:
    fehler = True
else:
    m = (y2-y1) / (x2-x1)
    b = y1 - m*x1
    fehler = False

# Ausgabe
if fehler == True:
    print("Es gibt keine Funktionsgleichung!")
else:
    print ("Steigung m = ", m)
    print ("y-Achsenabschnitt b = ", b)
    if (m == 1):                # Sonderfall m = 1
        print("y = x +", b)
    elif (m == -1):             # Sonderfall m = -1
        print("y = -x +", b)
    elif (m == 0):              # Sonderfall m = 0
        print("y =", b)
    else:                       # Allgemeiner Fall
        print("y =", m, "* x +", b)

