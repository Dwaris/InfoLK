from random import *

class SpielDesLebens(object):
    
    def __init__(self, groesse):
        self.welt = []
        for i in range(groesse):
            zeile = []
            for j in range(groesse):
                zelle = choice([0, 1])
                zeile = zeile + [zelle]
            self.welt = self.welt + [zeile]
    
    def kopieWelt(self):
        kopie = []
        for zeile in self.welt:
            kopie = kopie + [zeile[:]]
        return kopie
    
    def anzahlLebendeNachbarn(self, x, y):
        nachbarn = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                posX = x + i
                posY = y + j
                if not(i == 0 and j == 0) and posX >= 0 and posY >= 0 and posX < len(self.welt) and posY < len(self.welt):
                    nachbarn = nachbarn + [self.welt[posX][posY]]
        anzahlLebend = 0
        for zelle in nachbarn:
            if zelle == 1:
                anzahlLebend = anzahlLebend + 1
        return anzahlLebend

    def neueWelt(self):
        kopie = self.kopieWelt()
        for i in range(len(self.welt)):
            for j in range(len(self.welt)):
                anzahl = self.anzahlLebendeNachbarn(i, j)
                if self.welt[i][j] == 0 and anzahl == 3:
                    kopie[i][j] = 1
                elif self.welt[i][j] == 1 and anzahl < 2:
                    kopie[i][j] = 0
                elif self.welt[i][j] == 1 and anzahl in [2, 3]:
                    kopie[i][j] = 1
                elif self.welt[i][j] == 1 and anzahl > 3:
                    kopie[i][j] = 0
        self.welt = kopie

    def getGroesse(self):
        return len(self.welt)

    def getZelle(self, x, y):
        return self.welt[x][y]

    def setWelt(self, welt):
        self.welt = welt
