from chuckaluck import *
# Erzeugung der Objekte
spiel = Spiel()
# Durchführung eines Spiels
spiel.einsatzZahlen()
spiel.spielzahlSetzen(5)
spiel.wuerfelWerfen()
spiel.gewinnAuszahlen()
# Ausgabe der Spiel
print("Würfel A:", spiel.wuerfelA.augen)
