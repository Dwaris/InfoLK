from random import randint

class Wuerfel(object):

    __slots__ = ('augen')

    def __init__(self):
        self.augen = randint(1, 6)

    def werfen(self):
        self.augen = randint(1, 6)
        #print(self.augen)

    def getAugen(self):
        return self.augen

class Kasse(object):

    __slots__ = ('stand')

    def __init__(self):
        self.stand = 0

    def auszahlen(self, pBetrag):
        self.stand = self.stand - pBetrag

    def einzahlen(self, pBetrag):
        self.stand = self.stand + pBetrag

    def getStand(self):
        return self.stand

class Spieler(object):

    __slots__ = ('name', 'marken', 'rWuerfel1', 'rWuerfel2', 'rKasse')

    def __init__(self, pName, pMarken, pWuerfel1, pWuerfel2, pKasse):
        self.name = pName
        self.marken = pMarken
        self.rWuerfel1 = pWuerfel1
        self.rWuerfel2 = pWuerfel2
        self.rKasse = pKasse

    def spielen(self):
        self.rWuerfel1.werfen()
        self.rWuerfel2.werfen()
        augenGesamt = self.rWuerfel1.getAugen() + self.rWuerfel2.getAugen()
        if augenGesamt == 12:
            self.marken = self.marken - 12
            self.rKasse.einzahlen(12)
        elif augenGesamt == 11:
            anzahlMarken = self.rKasse.getStand()
            self.rKasse.auszahlen(anzahlMarken)
            self.marken = self.marken + anzahlMarken
        else:
            differenzBetrag = 11 - augenGesamt
            self.marken = self.marken - differenzBetrag
            self.rKasse.einzahlen(differenzBetrag)

    def getName(self):
        return self.name

    def getMarken(self):
        return self.marken

class Spielmanager(object):

    __slots__ = ('rSpieler1', 'rSpieler2', 'rSpieler3')

    def __init__(self, pSpieler1, pSpieler2, pSpieler3):
        self.rSpieler1 = pSpieler1
        self.rSpieler2 = pSpieler2
        self.rSpieler3 = pSpieler3

    def spielrundeDurchfuehren(self):
        self.rSpieler1.spielen()
        self.rSpieler2.spielen()
        self.rSpieler3.spielen()

                

w1 = Wuerfel()                          
w2 = Wuerfel()
k = Kasse()
sp1 = Spieler('Winner', 100, w1, w2, k)
sp2 = Spieler('Looser', 100, w1, w2, k)
sp3 = Spieler('Zitterhand', 100, w1, w2, k)
m = Spielmanager(sp1, sp2, sp3)

m.spielrundeDurchfuehren()
print(sp1.getMarken(), sp2.getMarken(), sp3.getMarken())
