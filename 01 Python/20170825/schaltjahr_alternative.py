# Eingabe
jahr  = int(input('Jahr: '))
# Verarbeitung und Ausgabe
if jahr % 4 == 0 and jahr % 100 != 0 and jahr % 400 == 0:
    istSchaltjahr = True
else:
    istSchaltjahr = False
# Ausgabe
if istSchaltjahr == True:
    print(jahr, 'ist ein Schaltjahr.')
else:
    print(jahr, 'ist kein Schaltjahr.')
