from random import randint

class Spiel(object):
    def __init__(self):
        self.k = Konto(100)
        self.s = Spielzahl()
        self.wA = Wuerfel()
        self.wB = Wuerfel()
        self.wC = Wuerfel()

    def einsatzZahlen(self):
        self.k.auszahlen(1)

    def spielzahlSetzen(self, zahl):
        self.s.setzen(zahl)

    def wuerfelWerfen(self):
        self.wA.werfen()
        self.wB.werfen()
        self.wC.werfen()

    def gewinnAuszahlen(self):
        x = 0
        if self.wA.augen == self.s.zahl:
            x = x + 1
        if self.wB.augen == self.s.zahl:
            x = x + 1
        if self.wC.augen == self.s.zahl:
            x = x + 1
        if x > 0:
            x = x + 1
        self.k.einzahlen(x)

    def spielen(self, zahl):
        self.einsatzZahlen()
        print("Konto = " + str(self.k.stand))
        self.spielzahlSetzen(zahl)
        print("Zahl = " + str(self.s.zahl))
        self.wuerfelWerfen()
        print("Würfel = " + str(self.wA.augen) + ", " + str(self.wB.augen) + ", " + str(self.wC.augen))
        self.gewinnAuszahlen()
        print("Konto = " + str(self.k.stand))

class Konto(object):
    def __init__(self, betrag):
        self.stand = betrag

    def einzahlen(self, betrag):
        self.stand += betrag

    def auszahlen(self, betrag):
        self.stand -= betrag

class Spielzahl(object):
    def __init__(self):
        self.zahl = 0

    def setzen(self, wert):
        self.zahl = wert


class Wuerfel(object):
    def __init__(self):
        self.augen = randint(1, 6)

    def werfen(self):
        self.augen = randint(1, 6)
