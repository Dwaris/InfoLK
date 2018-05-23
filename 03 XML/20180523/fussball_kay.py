from xml.dom.minidom import *


def ausgabeDatum(doc):
    k = document
    ausgabe = "Spielbericht:"    
    heimListe = k.getElementsByTagName("Heim")
    heim = heimListe[0].firstChild.nodeValue
    ausgabe = ausgabe + heim
    gastListe = k.getElementsByTagName("Gast")
    gast = gastListe[0].firstChild.nodeValue
    ausgabe = ausgabe + "-"+ gast
    TagListe = k.getElementsByTagName("Tag")
    tag = TagListe[0].firstChild.nodeValue
    MonatListe = k.getElementsByTagName("Monat")
    monat = MonatListe[0].firstChild.nodeValue
    JahrListe = k.getElementsByTagName("Jahr")
    jahr = JahrListe[0].firstChild.nodeValue
    UhrzeitListe = k.getElementsByTagName("Uhrzeit")
    uhrzeit = UhrzeitListe[0].firstChild.nodeValue
    print(ausgabe + "(" + tag + "."+ monat + "." + jahr +"."+ uhrzeit + "Uhr"+")")


    
document = parse('fussball.xml')
ausgabeDatum(document)

def entstand(doc):
    k = document
    ausgabe = "Das Spiel endete"
    ToreHeimListe = k.getElementsByTagName("ToreHeim")
    toreheim = ToreHeimListe[0].firstChild.nodeValue
    ToreGastListe = k.getElementsByTagName("ToreGast")
    toregast = ToreGastListe[0].firstChild.nodeValue
    print(ausgabe +" "+ toreheim +":"+toregast)

entstand(document)

def ausgabeHTore(doc):
    k = document
    kopf = "Die Tore für die Heimmannschaft erzielten:"
    print(kopf)
    TorHeimListe = k.getElementsByTagName("TorHeim")
    for torHeim in TorHeimListe:
        spielminuteListe = torHeim.getElementsByTagName("Spielminute")
        spielminute = spielminuteListe[0].firstChild.nodeValue
        spielerListe = torHeim.getElementsByTagName("Spieler")
        spieler = spielerListe[0].firstChild.nodeValue
        ausgabe = spieler + "("+ spielminute+ ")"

        
        eigentorListe = torHeim.getElementsByTagName("Eigentor")
        if len(eigentorListe)>0:
            ausgabe = ausgabe + ",Eigentor"
            
        print(ausgabe)

ausgabeHTore(document)

def ausgabeGTore(doc):
    k = document
    print("Die Tore für die Gastmannschaft erzielten:")
    TorGastListe = k.getElementsByTagName("TorGast")
    for TorGast in TorGastListe:
        spielminuteListe = TorGast.getElementsByTagName("Spielminute")
        spielminute = spielminuteListe[0].firstChild.nodeValue
        spielerListe = TorGast.getElementsByTagName("Spieler")
        spieler = spielerListe[0].firstChild.nodeValue
        ausgabe = spieler + "("+ spielminute+ ")"

        
        eigentorListe = TorGast.getElementsByTagName("Eigentor")
        if len(eigentorListe)>0:
            ausgabe = ausgabe + ",Eigentor"
            
        print(ausgabe)

ausgabeGTore(document)


def schiedsrichter(doc):
    k = document
    ausgabe = "Das Spiel wurde von Schiedsrichter "
    vornameListe = k.getElementsByTagName("Vorname")
    vorname = vornameListe[0].firstChild.nodeValue
    nameListe = k.getElementsByTagName("Name")
    name = nameListe[0].firstChild.nodeValue
    ausgabe = ausgabe +" "+ vorname + " "+ name+ " "  + "geleitet"

    print(ausgabe)

schiedsrichter(document)















    
