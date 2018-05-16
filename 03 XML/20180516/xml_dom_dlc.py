from xml.dom.minidom import *
# Quelltext in einen DOM-Baum umwandeln
xml_quelltext = """<?xml version="1.0" encoding="iso-8859-1"?>
<Kurs>
  <Fach>Informatik</Fach>
  <Typ>Grundkurs</Typ>
  <Stufe>11</Stufe>
  <Bezeichner>11-in-1</Bezeichner>
  <Unterricht>
    <Einheit>
      <Tag>Montag</Tag>
      <Stunde>7</Stunde>
    </Einheit>
    <Einheit>
      <Tag>Mittwoch</Tag>
      <Stunde>3</Stunde>
    </Einheit>
    <Einheit>
      <Tag>Mittwoch</Tag>
      <Stunde>4</Stunde>
    </Einheit>
  </Unterricht>
</Kurs>"""
document = parseString(xml_quelltext)
# Verarbeitung eines DOM-Baumes

def kursbezeichner(doc):
    k = doc
    kBezeichner = k.getElementsByTagName("Bezeichner")
    b = kBezeichner[0].firstChild.nodeValue
    return b

def unterrichtsstunden(doc):
    ergebnis = []
    k = doc
    kEinheit = k.getElementsByTagName("Einheit")
    for k in kEinheit:
        kTag = k.getElementsByTagName("Tag")
        tag = kTag[0].firstChild.nodeValue
        kStunde = k.getElementsByTagName("Stunde")
        stunde = int(kStunde[0].firstChild.nodeValue)
        ergebnis = ergebnis + [(tag, stunde)]
    return ergebnis

def fach(doc):
    k = doc
    kBezeichner = k.getElementsByTagName("Fach")
    b = kBezeichner[0].firstChild.nodeValue
    return b

def typ(doc):
    k = doc
    kBezeichner = k.getElementsByTagName("Typ")
    b = kBezeichner[0].firstChild.nodeValue
    return b
# Test
print(kursbezeichner(document))
print(unterrichtsstunden(document))
print(fach(document))
print(typ(document))
