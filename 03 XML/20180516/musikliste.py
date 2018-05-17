from xml.dom.minidom import *

document = parse('musikliste.xml')



def ausgabeMedium(rootElement):
    """ gibt alle Titel aus und die Art des Mediums (BluRay, MP3), sofern vorhanden"""

    # Liste aller Medien
    medienListe = rootElement.getElementsByTagName("Medium")
    for medium in medienListe:
        titelListe = medium.getElementsByTagName("Titel")
        titel = titelListe[0].firstChild.nodeValue # genau ein Titel pro Medium lt. DTD
        ausgabe = titel

        bluRayListe = medium.getElementsByTagName("BluRay")
        if len(bluRayListe)>0:
            ausgabe = ausgabe + " - BluRay"
        MP3Liste = medium.getElementsByTagName("MP3")
        if len(MP3Liste)>0:
            ausgabe = ausgabe + " - MP3"

        print(ausgabe)



def sucheInterpret(rootElement, suchInterpret="Pink Floyd"):
    """ gibt alle Titel aus, bei denen der gesuchte Interpret dabei ist. """
    # Liste aller Medien
    medienListe = rootElement.getElementsByTagName("Medium")
    for medium in medienListe:
        titelListe = medium.getElementsByTagName("Titel")
        titel = titelListe[0].firstChild.nodeValue # genau ein Titel pro Medium lt. DTD

        gefunden = False
        interpretListe = medium.getElementsByTagName("Interpret")
        for interpret in interpretListe:
            if interpret.firstChild.nodeValue == suchInterpret:
                gefunden = True
        if gefunden:
            print(titel)



def alleInterpreten(rootElement):
    """ gibt eine Liste aller unterschiedlichen (!) Interpreten an """
    interpretListe = rootElement.getElementsByTagName("Interpret")
    meineInterpreten = []
    for interpret in interpretListe:
        name = interpret.firstChild.nodeValue
        if name not in meineInterpreten:
            meineInterpreten.append(name)
            
    return meineInterpreten



def laufzeitTyp(rootElement, suchTyp="CD"):
    """ gibt die Laufzeit aller Medium vom suchTyp an """
    # Liste aller Medien
    medienListe = rootElement.getElementsByTagName("Medium")
    Laufzeit = 0
    for medium in medienListe:
        if medium.getAttribute('typ')==suchTyp:
            laufzeitListe = medium.getElementsByTagName('Laufzeit')
            if len(laufzeitListe)>0:
                zeit = int(laufzeitListe[0].firstChild.nodeValue)
                Laufzeit = Laufzeit + zeit
    return Laufzeit



ersterKnoten = document # root-Element
print("Alle Medien")
print("===========")
ausgabeMedium(ersterKnoten)

print()
print("Suche Interpret")
print("===============")
sucheInterpret(ersterKnoten, "Pink Floyd")

print()
print("Alle Interpreten")
print("================")
print(alleInterpreten(ersterKnoten))

print()
print("Laufzeit CD")
print("================")
print(laufzeitTyp(ersterKnoten, "CD"))

print()
print("Laufzeit DVD")
print("================")
print(laufzeitTyp(ersterKnoten, "DVD"))
