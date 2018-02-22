from random import randint
import sys
tuerAuto = randint(1,3)
tuerKanidat = int(input("Waehle eine Tuer (1, 2, 3):"))
def Kanidat():
    if tuerKanidat == 1:
        muenze = randint(0,1)
        if muenze == 0:
            tuerZiege = (2)
        else:
            tuerZiege = (3)
    if tuerKanidat == 2:
        muenze = randint(0, 1)
        if muenze == 0:
            tuerZiege = (1)
        else:
            tuerZiege = (3)
    if tuerKanidat == 3:
        muenze = randint(0, 1)
        if muenze == 0:
            tuerZiege = (1)
        else:
            tuerZiege = (2)
    return(tuerZiege);
if tuerKanidat > (3):
    sys.exit()
Kanidat = Kanidat()
print("Hinter Tuer {} befindet sich eine Ziege.".format(Kanidat))
print("Willst du bei deiner Wahl bleiben?")
if str(input("ja oder nein ")) == "ja":
    weiter = True
else:
    weiter = False
    if weiter == False:
        if tuerKanidat == 1 or tuerKanidat == 2 and Kanidat == 1 or Kanidat == 2:
          tuerKanidat = 3
        else:
            abs(tuerKanidat - Kanidat)
if tuerAuto == tuerKanidat:
    print("Du hast ein Auto gewonnen")
else:
    print("Du hast verloren")

