from a3 import*
# Punkte
p1 = Punkt(0, 0)
p2 = Punkt(0, 10)
p3 = Punkt(10, 10)
p4 = Punkt(10, 0)
p5 = Punkt(0, 10)
p6 = Punkt(10, 10)
p7 = Punkt(5, 15)
# Rechtecke und Dreieck (als n-Eck)
rechteck = nEck([p1, p2, p3, p4])
dreieck = nEck([p5, p6, p7])
# Haus des Nikolaus als Figur
haus_nikolaus = Figur()
haus_nikolaus.hinzufuegen(rechteck)
haus_nikolaus.hinzufuegen(dreieck)
# Figur verschieben
haus_nikolaus.verschieben(2, 3)
