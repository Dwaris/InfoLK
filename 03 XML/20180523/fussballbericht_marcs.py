from xml.dom.minidom import *

def bericht(doc):
    k = doc
    
    kHeim = k.getElementsByTagName('Heim')
    heim = kHeim[0].lastChild.nodeValue
    kGast = k.getElementsByTagName('Gast')
    gast = kGast[0].lastChild.nodeValue
    print('Es spielte ', heim, '(Heim) gegen ',gast, '(Gast)')

    anstoss = []
    kAnstoss = k.getElementsByTagName('Anstoß')
    kAnstoss = kAnstoss[0].firstChild.nextSibling.firstChild
    anstoss += [kAnstoss.nodeValue]
    for i in range (3):
        kAnstoss = kAnstoss.parentNode.nextSibling.nextSibling.firstChild
        anstoss += [kAnstoss.nodeValue]
    anstoss = str(anstoss[0]) + '.' + str(anstoss[1]) + '.' + str(anstoss[2]) + ' um ' + str(anstoss[3])
    print('Der Anstoß war am', anstoss)

    kSR = k.getElementsByTagName('Schiedsrichter')
    print('Das Spiel lief unter der Leitung des Schiedsrichters', kSR[0].firstChild.nextSibling.firstChild.nodeValue, kSR[0].lastChild.previousSibling.firstChild.nodeValue, str('(' + kSR[0].getAttribute('kurz') + ')'))

    print('Spielverlauf:')
    kSpielverlauf = k.getElementsByTagName('Spielverlauf-Tore')
    kTor = kSpielverlauf[0].firstChild.nextSibling
    while kTor != kSpielverlauf[0].lastChild:
        if kTor.nodeName != '#text':
            if kTor.lastChild.previousSibling.nodeName == 'Eigentor':
                eigen = '(Eigentor)'
            else:
                eigen = ''
            if kTor.nodeName == 'TorHeim':
                hg = '(Heim)'
            else:
                hg = '(Gast)'
            kSpieler = kTor.getElementsByTagName('Spieler')
            print('', kSpieler[0].firstChild.nodeValue, 'in Minute', kTor.firstChild.nextSibling.firstChild.nodeValue, hg, eigen)
        kTor = kTor.nextSibling

    kErgebnis = k.getElementsByTagName('Ergebnis')
    print('Somit endete das Spiel', kErgebnis[0].firstChild.nextSibling.firstChild.nodeValue, 'zu', kErgebnis[0].lastChild.previousSibling.firstChild.nodeValue)


document = parse('fussballspiel.xml')
print(bericht(document))
