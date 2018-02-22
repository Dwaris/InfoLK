# Turtle
from turtle import *
t = Turtle()
t.speed(0)
t.left(90)

# Funktionen
def istPunkt(L):
    if type(L) == list:
        if len(L) == 2:
            if (type(L[0]) == int) and (type(L[1]) == int):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def istStreckenzug(L):
    if type(L) == list:
        if len(L) == 0:
            return True
        else:
            if istPunkt(L[0]):
                return istStreckenzug(L[1:])
            else:
                return False
    else:
        return False

def istFigur(L):
    if type(L) == list:
        if len(L) == 0:
            return True
        else:
            if istStreckenzug(L[0]) or istFigur(L[0]):
                return istFigur(L[1:])
            else:
                return False
    else:
        return False

def zeichnePunktListe(punktListe):
    if punktListe != []:
        punkt = punktListe[0]
        t.goto(punkt)
        zeichnePunktListe(punktListe[1:])

def zeichneStreckenzug(streckenzug):
    if istStreckenzug(streckenzug):        
        if streckenzug != []:
            punkt = streckenzug[0]
            t.up()
            t.goto(punkt)
            t.down()
            zeichnePunktListe(streckenzug[1:])

def zeichneFigur(figur):
    if istFigur(figur):
        if figur != []:
            objekt = figur[0]
            if istStreckenzug(objekt):
                zeichneStreckenzug(objekt)
            else:
                zeichneFigur(objekt)
            zeichneFigur(figur[1:])

def xVerschiebenPunkt(punkt, x):
    if istPunkt(punkt):
        return [punkt[0]+x, punkt[1]]

def xVerschiebenStreckenzug(streckenzug, x):
    if istStreckenzug(streckenzug):
        if streckenzug == []:
            return []
        else:
            punkt = streckenzug[0]
            restStreckenzug = streckenzug[1:]
            return [xVerschiebenPunkt(punkt, x)] + xVerschiebenStreckenzug(restStreckenzug, x)

def xVerschiebenFigur(figur, x):
    if istFigur(figur):
        if figur == []:
            return []
        else:
            erstesElement = figur[0]
            restFigur = figur[1:]
            if istStreckenzug(erstesElement):
                return [xVerschiebenStreckenzug(erstesElement, x)] + xVerschiebenFigur(restFigur, x)
            else:
                return [xVerschiebenFigur(erstesElement, x)] + xVerschiebenFigur(restFigur, x)

#def yVerschiebenPunkt(punkt, y):
#def yVerschiebenStreckenzug(streckenzug, y):
#def yVerschiebenFigur(figur, y):
#def xyVerschiebenPunkt(punkt, x, y):
#def xyVerschiebenStreckenzug(streckenzug, x, y):
#def xyVerschiebenFigur(figur, x, y):
#def xSpiegelnPunkt(punkt)
#def xSpiegelnStreckenzug(streckenzug)
#def xSpiegelnFigur(figur)

# Beispiel
stuetzelinks = [[0, 0],[20, 0],[50, 100],[30, 100],[0, 0]]
blockunten = [[90, 10],[110, 10],[110, 30],[90, 30],[90, 10]]
blockoben = [[90, 70],[110, 70],[110, 90],[90, 90],[90, 70]]
raute = [[80, 50],[100, 40],[120, 50],[100, 60],[80, 50]]
verbindung1 = [[100, 110], [100, 90]]
verbindung2 = [[100, 70], [100, 60]]
verbindung3 = [[100, 40], [100, 30]]
verbindung4 = [[100, 10], [100, 0]]
verbindung5 = [[80, 50], [70, 50], [70, 100], [100, 100]]
stuetzerechts = [verbindung1, blockoben, verbindung2, raute, \
                 verbindung5, verbindung3, blockunten, verbindung4]
dach = [[10, 110],[130, 110],[130, 125],[70, 140],[10, 125],[10, 110]]
tor = [stuetzelinks, stuetzerechts, dach]
rahmen = [[0, 0],[140, 0],[140, 140],[0, 140],[0, 0]]
logo = [tor, rahmen]

zeichneFigur(logo)

logoNeu = xyVerschiebenFigur(logo, -50, 100)

zeichneFigur(logoNeu)
