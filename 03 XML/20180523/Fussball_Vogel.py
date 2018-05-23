# Spielbericht: 1. FC Kaiserslautern - 1. FSV Mainz 05 (17.9.2011, 15:30 Uhr)
# Das Spiel endete 3:1.
# Die Tore für die Heimmannschaft erzielten:
# Svensson (24, Eigentor),
# Shechter (54),
# Tiffert (73).
# Die Tore für die Gastmannschaft erzielten:
# Choupo-Moting (15).
# Das Spiel wurde von Schiedsrichter Wolfgang Stark (WoSt) geleitet.

from xml.dom.minidom import *

document = parse("Fussball.xml")


def getHeim(document):
    return document.getElementsByTagName("Heim")[0].firstChild.nodeValue


def getGast(document):
    return document.getElementsByTagName("Gast")[0].firstChild.nodeValue


def getDatum(document):
    a = document.getElementsByTagName("Anstoß")[0]
    return (a.getElementsByTagName("Tag")[0].firstChild.nodeValue,
            a.getElementsByTagName("Monat")[0].firstChild.nodeValue,
            a.getElementsByTagName("Jahr")[0].firstChild.nodeValue,
            a.getElementsByTagName("Uhrzeit")[0].firstChild.nodeValue)


def getErgebnis(document):
    e = document.getElementsByTagName("Ergebnis")[0]
    return (e.getElementsByTagName("ToreHeim")[0].firstChild.nodeValue,
            e.getElementsByTagName("ToreGast")[0].firstChild.nodeValue)

# Gibt Tore im Format (Spieler, Minute, Eigentor?) zurück
def getTore(document, heim):
    st = document.getElementsByTagName("Spielverlauf-Tore")[0] # st = Spielverlauftore
    tore = []
    lt = st.getElementsByTagName("TorHeim" if heim else "TorGast")
    for t in lt:
        tore += [(t.getElementsByTagName("Spieler")[0].firstChild.nodeValue,
                  t.getElementsByTagName("Spielminute")[0].firstChild.nodeValue,
                  t.getElementsByTagName("Eigentor")!=[])]
    return tore


def getSchiedsrichter(document):
    s = document.getElementsByTagName("Schiedsrichter")[0]
    return (s.getElementsByTagName("Vorname")[0].firstChild.nodeValue,
            s.getElementsByTagName("Name")[0].firstChild.nodeValue,
            s.getAttribute("kurz"))


def printSpielbericht():
    datum = getDatum(document)
    ergebnis = getErgebnis(document)
    print("""
Spielbericht: {0} - {1} ({2}.{3}.{4}, {5} Uhr)
Das Spiel endete {6}:{7}.
Die Tore für die Heimmannschaft erzielten:
        """.format(getHeim(document), getGast(document), datum[0], datum[1], datum[2], datum[3],
                    ergebnis[0], ergebnis[1]))

    toreHeim = getTore(document, True)
    for t in toreHeim:
        print("{0} ({1}".format(t[0], t[1]) + (", Eigentor)" if t[2] else ")"))

    print("Die Tore für die Gastmannschaft erzielten:")

    toreGast = getTore(document, False)
    for t in toreGast:
        print("{0} ({1}".format(t[0], t[1]) + (", Eigentor)" if t[2] else ")"))

    schiedsrichter = getSchiedsrichter(document)

    print("Das Spiel wurde von Schiedsrichter {0} {1} ({2}) geleitet.".format(schiedsrichter[0], schiedsrichter[1], schiedsrichter[2]))


printSpielbericht()