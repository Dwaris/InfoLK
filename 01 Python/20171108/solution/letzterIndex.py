# Initialisierung
L = ['Meier', 'Bauer', 'Moser', 'Molitor', 'Schmitt', 'Ludwig', 'Schmitt']
name = 'Schmitt'

# Verarbeitung
n = -1
i = 0
while i < len(L):
    if L[i] == name:
        n = i
    i = i + 1

# Ausgabe
print(n)
