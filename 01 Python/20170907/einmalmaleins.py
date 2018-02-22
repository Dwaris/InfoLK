# Eingabe
basis = int(input("Basis: "))

# Verarbeitung und Ausgabe
for i in range(1, 21):
    print('{0:2d} * {1:2d} = {2:3d}'. format(i, basis, i * basis))
