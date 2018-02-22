def bmi(gewicht, größe):
    return gewicht/(größe)**2

def puls(alter):
    return 165-0.75*alter

gewicht = float(input("Gewicht in kg: "))
größe = float(input("Größe in m: "))
alter = int(input("Alter in Jahren: "))

print("Dein BMI beträgt: {}".format(bmi(gewicht, größe)))
print("""
Dein Alter: {}
Dein optimaler Puls: {}
""".format(alter,puls(alter)))
