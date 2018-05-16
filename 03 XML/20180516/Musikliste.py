from xml.dom.minidom import *
doc = parse("Musikliste.xml")

def Titel(doc):
    ergebnis = []
    k = doc
    kMedium = k.getElementsByTagName("Medium")
    for k in kMedium:
        kTitel = k.getElementsByTagName("Titel")
        titel = kTitel[0].firstChild.nodeValue
        typ = k.getAttribute("typ")
       # typ = ktyp[0].firstChild.nodeValue
        ergebnis = ergebnis + [(titel, typ)]
    return ergebnis
print(Titel(doc))

def Interpreten(doc):
    Interpret = "The Beatles"
    k = doc
    kMedium = k.getElementsByTagName("Medium")
    for k in kMedium:
        kInterpret = k.getElementsByTagName("Interpret")
        for i in kInterpret:
            print(i)
            if i.firstChild.nodeValue == Interpret:
                return(k.getElementsByTagName("Titel")[0].firstChild.nodeValue)
print(Interpreten(doc))

def unterschiedliche_Interpreten(doc):
    ergebnis = []
    k = doc
    kMedium = k.getElementsByTagName("Medium")
    for k in kMedium:
        kInterpret = k.getElementsByTagName("Interpret")
        for i in kInterpret:
            ergebnis = ergebnis + [i.firstChild.nodeValue]
    return set(ergebnis)
print(unterschiedliche_Interpreten(doc))

def laufzeit(doc):
    ergebnis = []
    typ = "CD"
    k = doc
    kMedium = k.getElementsByTagName("Medium")
    for k in kMedium:
       if k.getAttribute("typ") == typ:
            ergebnis += [k.getElementsByTagName("Laufzeit")[0].firstChild.nodeValue]
       return ergebnis
print(laufzeit(doc))