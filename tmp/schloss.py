from random import randint
class Schloss(object):
    def __init__(self):
        self.k = Kombination()
        self.zA = Zahlenrad()
        self.zB = Zahlenrad()
        self.zC = Zahlenrad()
        self.istOffen = False

    def setKombination(self,zA,zB,zC):
        if self.istOffen == True:
            self.zA = zA
            self.zB = zB
            self.zC = zC
        else:
            pass
    def kombinationKorrect(self):
        
class Kombination(object):
    def __init__(self):
        self.zA = randint(0,9) 
        self.zB = randint(0,9)
        self.zC = randint(0,9)

class Zahlenrad(object):
    def __init__(self):
        self.wert = 0

    def drehen(self):
        if self.wert < 10:
            self.wert += 1
        else:
            self.wert = 0
