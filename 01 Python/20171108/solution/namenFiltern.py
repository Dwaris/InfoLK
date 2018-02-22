# Initialisierung
namen = ['Meier', 'Bauer', 'Moser', 'Molitor', 'Martin']

# Verarbeitung
namenNeu = []
for name in namen:
    if name[0] == 'M':
        namenNeu = namenNeu + [name]

# Ausgabe
print(namen)
print(namenNeu)
