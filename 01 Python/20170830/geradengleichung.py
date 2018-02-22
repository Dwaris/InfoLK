import sys
#input
x1 = float(input('X1-Koordinate : '))
y1 = float(input('Y1-Koordinate : '))
x2 = float(input('X2-Koordinate : '))
y2 = float(input('Y2-Koordinate : '))

#process
if x2 - x1 != 0:
    m = (y2 - y1) / (x2 - x1)
    n = y1
else:
    sys.exit("error")

#output
print ("Steigung m = ",m)
print ("y-Achsenabschnitt n = ",n)
