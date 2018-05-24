from xml.dom.minidom import *



def listTexte(rootElement):
    """ extrahiert alle Texte des Dokuments in eine Liste"""
    ergebnisListe = []

    # Liste aller Texte (<tspan>)
    textListe = rootElement.getElementsByTagName("tspan")
    for t in textListe:
        meinText = t.firstChild.nodeValue
        ergebnisListe.append(meinText)

    return ergebnisListe



def listTexteZusammenhang(rootElement):
    """ extrahiert alle Texte des Dokuments in eine 2-dimensionale Liste.
        Dabei werden alle Texte zusammengefasst, die mit dem <text>-Element
        zusammengehören."""

    ergebnisListe = []

    # Liste aller Texte
    textListe = rootElement.getElementsByTagName("text")
    for text in textListe:
        tspanListe = text.getElementsByTagName("tspan")
        unterliste = []
        for tspan in tspanListe:
            meinText = tspan.firstChild.nodeValue
            unterliste.append(meinText)
        ergebnisListe.append(unterliste)

    return ergebnisListe



document = parse('limericks.svg')

ersterKnoten = document.documentElement # root-Element
print("Alle Texte")
print("===========")
print(listTexte(ersterKnoten))

print()
print("Alle Texte im Zusammenhang")
print("==========================")
ergebnis = listTexteZusammenhang(ersterKnoten)
for e in ergebnis:
    print(e)

