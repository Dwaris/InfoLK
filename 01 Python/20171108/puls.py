#input
print = 'Ihr optimaler Ausdauer-Puls'
alt = float(input('Ihr Alter: '))
gew = float(input('Ihr Gewicht: '))

#verarbeitung
maxipuls = float(212 - ((0.5 * alt) - (0.11 * gew)))
optimini = float(maxipuls * 0.7)
optimaxi = float(maxipuls * 0.8)

#output
print('Ihre optimale Herzfrequenz-Zone: ' , optimini , '-' , optimaxi , ':D')
