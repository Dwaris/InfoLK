# Initialisierung
L = ['Meier', 'Bauer', 'Moser','Schmitt', 'Molitor', 'Ludwig', 'Schmitt']
name = 'Schmitt'
# Verarbeitung
n = -1
i = 0
while (i < len(L)) and (n < 0):
    if L[i] == name:
        n = i
    i = i + 1
# Ausgabe
print(n)
