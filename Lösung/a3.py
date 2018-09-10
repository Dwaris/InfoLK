class Punkt(object):

    def __init__(self, posX, posY):
        self.x = posX
        self.y = posY
        
    def verschieben(self, dX, dY):
        self.x += dX
        self.y += dY

class nEck(object):

    def __init__(self, punkte):
        self.punkte = punkte

    def hinzufuegen(self, punkt):
        self.punkte += [punkt]

    def verschieben(self, dX, dY):
        for punkt in self.punkte:
            punkt.verschieben(dX, dY)
        
class Figur(object):

    def __init__(self):
        self.nEcke = []

    def hinzufuegen(self, nEck):
        self.nEcke += [nEck]
        
    def verschieben(self, dX, dY):
        for nEck in self.nEcke:
            nEck.verschieben(dX, dY)
