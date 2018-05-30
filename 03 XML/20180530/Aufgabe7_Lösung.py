from xml.dom.minidom import *



# Unterprogramme
def ausgabeLebensdaten(wurzel):
    philosophen = wurzel.getElementsByTagName("Philosoph")
    for philosoph in philosophen:
        name = philosoph.firstChild.nextSibling.firstChild.nodeValue
        
        geboren = philosoph.getElementsByTagName("Geboren")
        geboren = geboren[0].firstChild.nodeValue
        
        gestorben = philosoph.getElementsByTagName("Gestorben")
        gestorben = gestorben[0].firstChild.nodeValue

        print(name, "lebte von", geboren, "bis", gestorben)

def ausgabeAlter(wurzel):
    philosophen = wurzel.getElementsByTagName("Philosoph")
    for philosoph in philosophen:
        name = philosoph.firstChild.nextSibling.firstChild.nodeValue
        
        geboren = philosoph.getElementsByTagName("Geboren")
        exaktgeboren = geboren[0].getAttribute("exakt")
        geboren = geboren[0].firstChild.nodeValue
        
        gestorben = philosoph.getElementsByTagName("Gestorben")
        exaktgestorben = gestorben[0].getAttribute("exakt")
        gestorben = gestorben[0].firstChild.nodeValue

        alter = int(gestorben) - int(geboren)

        if exaktgeboren == "nein" or exaktgestorben == "nein":
            print(name, "wurde ca.", str(alter), "Jahre alt.")
        else:
            print(name, "wurde", str(alter), "Jahre alt.")

def ausgabeThemen(wurzel):
    ausgabe = []

    philosophen = wurzel.getElementsByTagName("Philosoph")
    for philosoph in philosophen:
        themen = philosoph.getElementsByTagName("Thema")
        for thema in themen:
            name = thema.firstChild.nodeValue
            if not(name in ausgabe):
                ausgabe = ausgabe + [name]
    
    for name in ausgabe:
        print(name)



# Hauptprogramm
document = parse('WeisheitsLiebende.xml')

print()
ausgabeLebensdaten(document)

print()
ausgabeAlter(document)

print()
ausgabeThemen(document)

