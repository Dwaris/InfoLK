fac = 0.65
puls = float(input('Ruhepuls : '))
age = float(input('Alter :'))

trpuls = puls + (220 - 2/3 * age - puls)*fac

print('Dein optimaler Trainingspuls ist : ', trpuls)
