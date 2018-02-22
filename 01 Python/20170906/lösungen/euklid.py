# Eingabe
x = int(input("x = "))
y = int(input("y = "))

# Verarbeitung
while y > 0:
    h = x % y
    x = y
    y = h

# Ausgabe
print(x)

