from random import randint

class Wuerfel(object):
    def __init__(self):
        self.augen = randint(1, 6)

    def werfen(self):
        self.augen = randint(1, 6)

    def getAugen(self):
        return self.augen

class Spieler(object):
    def __init__(self, pName):
        self.name = pName
        self.rWuerfel = None
        self.punkte = 0

    def setWuerfel(self, pWuerfel):
        self.rWuerfel = pWuerfel
        
    def wuerfeln(self):
        self.rWuerfel.werfen()
        self.punkte = self.punkte + self.rWuerfel.getAugen()

    def getName(self):
        return self.name

    def getPunkte(self):
        return self.punkte

# Test
#----------------------------------------

wuerfel = Wuerfel()

spieler1 = Spieler('Zauberhand')
spieler1.setWuerfel(wuerfel)

spieler2 = Spieler('Looser')
spieler2.setWuerfel(wuerfel)

spieler3 = Spieler('Spider')
spieler3.setWuerfel(wuerfel)

for i in range(5):
    spieler1.wuerfeln()
    spieler2.wuerfeln()
    spieler3.wuerfeln()
    print('Punktestand', spieler1.getName(), ':', spieler1.getPunkte())
    print('Punktestand', spieler2.getName(), ':', spieler2.getPunkte())
    print('Punktestand', spieler3.getName(), ':', spieler3.getPunkte())
    print()
