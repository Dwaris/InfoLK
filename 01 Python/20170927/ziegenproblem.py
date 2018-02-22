from random import *

userDoor = int(input("Wähle eine Tür: (1,2,3): "))

ziege = 1

while not ziege != userDoor:
    ziege = randint(1, 3)


if randint(0, 1) == 1:
    auto = userDoor
else:
    for i in range(3):
        if i!=ziege and i!=userDoor:
            auto = i+1

antwort = input("Hinter Tür " + str(ziege) + " befindet sich eine Ziege! Möchtest du wechseln (w/B)")
if antwort == "W" or antwort == "w":
    if userDoor == auto:
        print("Du hast das Auto gewonnen!")
    else:
        print("Du hast die Ziege erwischt")
else:
    if userDoor != auto:
        print("Du hast das Auto gewonnen!")
    else:
        print("Du hast die Ziege erwischt")