geschwindigkeit = float(input('Geschwindigkeit (in km/h) : '))
reaktionsweg = (geschwindigkeit/10)*3
bremsweg = (geschwindigkeit/10) * (geschwindigkeit/10)
anhalteweg = reaktionsweg + bremsweg
print('Reaktionsweg (in m)    :', reaktionsweg)
print('Bremsweg (in m)        :', bremsweg)
print('Anhaltewegweg (in m)   :', anhalteweg)
