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
            if i.firstChild.nodeValue == Interpret:
                print(k.getElementsByTagName("Titel")[0].firstChild.nodeValue)

def unterschiedliche_Interpreten(doc):



            #print(k.firstChild.nodeValue)

print(Interpreten(doc))