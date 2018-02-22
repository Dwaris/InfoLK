from turtle import *
reset()
speed(0)

def kochkurve(laenge):
    if (laenge > 2):
        kochkurve(laenge/3)
        left(60)
        kochkurve(laenge/3)
        right(120)
        kochkurve(laenge/3)
        left(60)
        kochkurve(laenge/3)
    else:
        forward(laenge)

def kochflocke(laenge):
    for i in range(3):
        kochkurve(laenge)
        right(120)

kochflocke(200)
