from ma import *
from turtle import *

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

t = Turtle()
# Initialisierung
t.left(90)
zeichneFigur(logo)

