class Zahlenrad(object):
    
    def __init__(self, stand, korrekt):
        self.stand = 0
        self.setStand(stand)
        self.korrekt = 0
        self.setKorrekt(korrekt)

    def setStand(self, stand):
        if (stand >= 0 and stand <= 9):
            self.stand = stand
        else:
            self.stand = 0

    def setKorrekt(self, korrekt):
        if (korrekt >= 0 and korrekt <= 9):
            self.korrekt = korrekt
        else:
            self.korrekt = 0

    def getStand(self):
        return self.stand

    def getKorrekt(self):
        return self.korrekt

    def istOffen(self):
        if self.stand == self.korrekt:
            return True
        else:
            return False



class Zahlenschloss(object):

    def __init__(self, korrekt):
        self.raeder = []
        self.offen = False
        for k in korrekt:
            self.raeder = self.raeder + [Zahlenrad(0, k)]

    def oeffnen(self):
        offen = True
        for r in self.raeder:
            if not r.istOffen():
                offen = False
        if offen == True:
            self.offen = True

    def schliessen(self):
        self.offen = False

    def setStand(self, index, wert):
        self.raeder[index].setStand(wert)

    def getStand(self):
        stand = []
        for r in self.raeder:
            stand = stand + [r.stand]
        return stand

    def getOffen(self):
        return self.offen

z = Zahlenschloss([2, 3, 4])
