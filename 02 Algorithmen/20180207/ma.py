from turtle import *
t = Turtle()
def del_all(x,liste):
    if liste == []:
        return []
    if x == liste[0]:
        return del_all(x, liste[1:])
    else:
        return [liste[0]] + del_all(x, liste[1:])

def addiere(x,liste):
    if liste == []:
        return []
    else:
        return [liste[0]+x] + addiere(x,liste[1:])

def del_min(x,liste):
    if liste == []:
        return []
    elif liste[0] >= x:
        return del_min(x,liste[1:])
    else:
        return [liste[0]] + del_min(x,liste[1:])

def reverse(liste):
    if len(liste) == 0:
        return []
    return [liste[-1]] + reverse(liste[:-1])

def flacheListe(liste):
    if len(liste) == 0:
        return []
    if len(liste) == 1:
        if type(liste[0]) == list:
            liste_neu = flacheListe(liste[0])
        else:
            liste_neu = liste
    elif type(liste[0]) == list:
        liste_neu = flacheListe(liste[0]) + flacheListe(liste[1:])
    else:
        liste_neu = [liste[0]] + flacheListe(liste[1:])
    return liste_neu

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
def yVerschiebenPunkt(punkt, y):
    if istPunkt(punkt):
        return [punkt[0], punkt[1]+y]
def xyVerschiebenPunkt(punkt, x, y):
    if istPunkt(punkt):
        return [punkt[0] + x, punkt[1] + y]
def xVerschiebenStreckenzug(streckenzug, x):
    if istStreckenzug(streckenzug):
        if streckenzug == []:
            return []
        else:
            punkt = streckenzug[0]
            restStreckenzug = streckenzug[1:]
            return [xVerschiebenPunkt(punkt, x)] + xVerschiebenStreckenzug(restStreckenzug, x)
def yVerschiebenStreckenzug(streckenzug, y):
    if istStreckenzug(streckenzug):
        if streckenzug == []:
            return []
        else:
            punkt = streckenzug[0]
            restStreckenzug = streckenzug[1:]
            return [yVerschiebenPunkt(punkt, y)] + yVerschiebenStreckenzug(restStreckenzug, y)
def xyVerschiebenStreckenzug(streckenzug, x, y):
    if istStreckenzug(streckenzug):
        if streckenzug == []:
            return []
        else:
            punkt = streckenzug[0]
            restStreckenzug = streckenzug[1:]
            return [xVerschiebenPunkt(punkt, x)] + xVerschiebenStreckenzug(restStreckenzug, x) + [yVerschiebenPunkt(punkt, y)] + yVerschiebenStreckenzug(restStreckenzug, y)
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
def yVerschiebenFigur(figur, y):
    if istFigur(figur):
        if figur == []:
            return []
        else:
            erstesElement = figur[0]
            restFigur = figur[1:]
            if istStreckenzug(erstesElement):
                return [yVerschiebenStreckenzug(erstesElement, y)] + yVerschiebenFigur(restFigur, y)
            else:
                return [yVerschiebenFigur(erstesElement, y)] + yVerschiebenFigur(restFigur, y)
def xyVerschiebenFigur(figur, x, y):
    if istFigur(figur):
        if figur == []:
            return []
        else:
            erstesElement = figur[0]
            restFigur = figur[1:]
            if istStreckenzug(erstesElement):
                return [xVerschiebenStreckenzug(erstesElement, x)] + xVerschiebenFigur(restFigur, x) + [yVerschiebenStreckenzug(erstesElement, y)] + yVerschiebenFigur(restFigur, y)
            else:
                return [xVerschiebenFigur(erstesElement, x)] + xVerschiebenFigur(restFigur, x) + [yVerschiebenFigur(erstesElement, y)] + yVerschiebenFigur(restFigur, y)
def xSpiegelnPunkt(punkt):
    return [-x for x in punkt]
