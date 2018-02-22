from turtle import *
#seitenlaenge = int(input("Seitenlänge: "))
#n = int(input("Anzahl: "))
def stern(seitenlaenge):
    for i in range(5):
        forward(seitenlaenge)
        left(72)
        left(360/5)
stern(50)
