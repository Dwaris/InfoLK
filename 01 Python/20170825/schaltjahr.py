# Eingabe
jahr = int(input("Jahr: "))

# Verarbeitung
if jahr % 4 == 0:
    if jahr % 100 == 0:
        if jahr % 400 == 0:
            schaltjahr = True
        else:
             schaltjahr = False
    else:
         schaltjahr = True
else:
     schaltjahr = False
#Ausgabe
if schaltjahr == True:
    print(jahr, "ist ein Schaltjahr")
else:
    print(jahr, "ist kein Schaltjahr")
