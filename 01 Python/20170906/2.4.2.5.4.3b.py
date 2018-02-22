# Eingabe
kapital = float(input("Kapital zu Beginn: "))
jahr = 2010
# Verarbeitung
while jahr < 2020:
    kapital = kapital * 1.05
    jahr = jahr + 1

# Ausgabe
print("Kapital am Ende:", kapital)
