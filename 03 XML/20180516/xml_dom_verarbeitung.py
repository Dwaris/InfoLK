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
    k = k.firstChild  # Kurs
    k = k.firstChild  # \..
    k = k.nextSibling  # Fach
    k = k.nextSibling  # \..
    k = k.nextSibling  # Typ
    k = k.nextSibling  # \..
    k = k.nextSibling  # Stufe
    k = k.nextSibling  # \..
    k = k.nextSibling  # Bezeichner
    k = k.firstChild  # #text
    b = k.nodeValue  # '11-in-1'
    return b

def fach(doc):
    k = doc
    k = k.firstChild
    k = k.firstChild
    k = k.nextSibling
    k = k.firstChild
    b = k.nodeValue
    return b
def typ(doc):
    k = doc
    k = k.firstChild
    k = k.firstChild
    k = k.nextSibling
    k = k.nextSibling
    k = k.nextSibling
    k = k.firstChild
    b = k.nodeValue
    return b
# Test
print(kursbezeichner(document))
print(fach(document))
print(typ(document))