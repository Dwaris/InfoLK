import math
def Leibniz_iterativ(Grenze):
    """ Gibt eine Näherung für pi/4 zurück """
    ergebnis=0
    for i in range(0,Grenze+1):
        ergebnis = ergebnis + (-1)**i/(2*i+1)

    return ergebnis



def Leibniz_rekursiv(Grenze):
    if Grenze>0:
        ergebnis = (-1)**Grenze/(2*Grenze+1) + Leibniz_rekursiv(Grenze-1)
    else:
        ergebnis = (-1)**Grenze/(2*Grenze+1)

    return ergebnis

def Leibniz_test(Stelle):
    if math.pi
