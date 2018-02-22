from turtle import *
#seitenlaenge = int(input("Seitenlänge: "))
#n = int(input("Anzahl: "))
def fuenfeck(seitenlaenge,n):
    reset
    for i in range(n):
        for i in range(5):
            forward(seitenlaenge)
            left(72)
        left(360/n)
fuenfeck(50,20)
