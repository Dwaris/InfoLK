# Eingabe
gewicht = float(input("Gewicht in kg: "))
groesse = float(input("Groesse im m : "))

# Verarbeitung
bmi = gewicht / (groesse * groesse)

# Ausgabe
print("Body-Mass-Index: ", bmi)
if bmi < 19:
   print("Sie haben Untergwicht")
elif bmi >26:
   print("Sie haben Übergewicht")
if bmi > 19 and bmi < 26:
   print("Sie haben Normalgewicht")
    
