#input
mass = float(input('Masse (in kg) : '))
age = float(input('Alter : '))
alc_vol = float(input('Alkoholgehalt des Getränks : '))
drink_vol = float(input('Menge des Getränks (in l) : '))

#process
if age < 18:
    factor = 0.6
else:
    factor = 0.7

alc_mass = 10 * drink_vol * alc_vol * 0.8
alc_lvl = round(alc_mass / (mass * factor) ,3)

#output
print('')
print('Die Promille beträgt : ' + str(alc_lvl))
if age < 18 and alc_vol >= 15 :
    print('\n')
    print("""Du kleiner Pi**er, du sollst so etwas noch nicht trinken!!!
Schande über dich und deine ganze Familie.""")
