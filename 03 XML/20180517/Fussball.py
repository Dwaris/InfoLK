from xml.dom.minidom import *

doc = parse("Fussball.xml")
k = doc

print("Spielbericht:", k.getElementsByTagName("Heim")[0].firstChild.nodeValue, "-",
      k.getElementsByTagName("Gast")[0].firstChild.nodeValue, "(",
      k.getElementsByTagName("Tag")[0].firstChild.nodeValue, ".",
      k.getElementsByTagName("Monat")[0].firstChild.nodeValue, ".",
      k.getElementsByTagName("Jahr")[0].firstChild.nodeValue, k.getElementsByTagName("Uhrzeit")[0].firstChild.nodeValue,
      ")")
print("Das Spiel endete:", k.getElementsByTagName("ToreHeim")[0].firstChild.nodeValue, ":",
      k.getElementsByTagName("ToreGast")[0].firstChild.nodeValue)

kTorHeim = k.getElementsByTagName("TorHeim")
kTorGast = k.getElementsByTagName("TorGast")
kSchiedsrichter = k.getElementsByTagName("Schiedsrichter")
print("Die Tore für die Heimmannschaft erzielten: ")
for k in kTorHeim:
    print(k.getElementsByTagName("Spieler")[0].firstChild.nodeValue, "(",
          k.getElementsByTagName("Spielminute")[0].firstChild.nodeValue,
          ("Eigentor" if k.getElementsByTagName("Eigentor") != [] else ""), ")")
print("Die Tore für die Gastmanschaft erzielten: ")
for k in kTorGast:
    print(k.getElementsByTagName("Spieler")[0].firstChild.nodeValue, "(",
          k.getElementsByTagName("Spielminute")[0].firstChild.nodeValue,
          ("Eigentor" if k.getElementsByTagName("Eigentor") != [] else ""), ")")
for k in kSchiedsrichter:
    print("Das Spiel wurde von Schiedsrichter", k.getElementsByTagName("Vorname")[0].firstChild.nodeValue,
          k.getElementsByTagName("Name")[0].firstChild.nodeValue, "(", k.getAttribute("kurz"), ")", "geleitet")
