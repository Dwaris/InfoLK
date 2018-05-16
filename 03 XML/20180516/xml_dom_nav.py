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
# Navigation im DOM-Baum
aktuellerKnoten = document
print(aktuellerKnoten.nodeName)
aktuellerKnoten = aktuellerKnoten.firstChild
print(aktuellerKnoten.nodeName)
aktuellerKnoten = aktuellerKnoten.firstChild
print(aktuellerKnoten.nodeName)
aktuellerKnoten = aktuellerKnoten.nextSibling
print(aktuellerKnoten.nodeName)
aktuellerKnoten = aktuellerKnoten.nextSibling
print(aktuellerKnoten.nodeName)
aktuellerKnoten = aktuellerKnoten.nextSibling
print(aktuellerKnoten.nodeName)
aktuellerKnoten = aktuellerKnoten.nextSibling
print(aktuellerKnoten.nodeName)
aktuellerKnoten = aktuellerKnoten.nextSibling
print(aktuellerKnoten.nodeName)
aktuellerKnoten = aktuellerKnoten.nextSibling
print(aktuellerKnoten.nodeName)
aktuellerKnoten = aktuellerKnoten.nextSibling
print(aktuellerKnoten.nodeName)
aktuellerKnoten = aktuellerKnoten.firstChild
print(aktuellerKnoten.nodeName)
print(aktuellerKnoten.nodeValue)
