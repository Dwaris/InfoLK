def ggt(x, y):
    while y > 0:
        h = x % y
        x = y
        y = h
    return x

def addiereBrueche(bruch1, bruch2):
    (zaehler1, nenner1) = bruch1
    (zaehler2, nenner2) = bruch2
    nennerSumme = nenner1 * nenner2
    zaehlerSumme = zaehler1*nenner2 + zaehler2*nenner1
    bruchSumme = (zaehlerSumme, nennerSumme)
    return bruchSumme
