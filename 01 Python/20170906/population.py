# Eingabe
population = float(input("Population zu Beginn: "))

# Verarbeitung
jahr = 2010
while jahr < 2020:
    population = population * 1.05
    jahr += 1

# Ausgabe
print("Population am Ende:", population)
