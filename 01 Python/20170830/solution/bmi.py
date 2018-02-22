# Eingabe
gewicht = float(input("Gewicht in kg: "))
groesse = float(input("Groesse im m : "))

# Verarbeitung
bmi = gewicht / (groesse * groesse)

# Ausgabe
print("Body-Mass-Index: ", bmi)
if bmi < 19:
    print("Du hast Untergewicht...")
else:
    if bmi <= 26:
        print("Du hast Normalgewicht...")
    else:
        print("Du hast Übergewicht...")
