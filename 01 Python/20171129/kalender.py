def schaltjahr(jahr):
    if (jahr % 400 == 0) or ((jahr % 4 == 0) and not (jahr % 100 == 0)):
        return True
    else:
        return False

def anzahlTageImMonat(monat, jahr):
    if monat in [1, 3, 5, 7, 8, 10, 12]:
        anzahl = 31
    elif monat in [4, 6, 9, 11]:
        anzahl = 30
    elif schaltjahr(jahr):
        anzahl = 29
    else:
        anzahl = 28
    return anzahl

def naechstesDatum(datum):
    (tag, monat, jahr) = datum
    if tag < anzahlTageImMonat(monat, jahr):
        tag = tag + 1
    elif monat < 12:
        tag = 1
        monat = monat + 1
    else:
        tag = 1
        monat = 1
        jahr = jahr + 1
    return (tag, monat, jahr)

def datumNachTagen(datumStart, anzahlTage):
    for i in range(anzahlTage):
        datumStart = naechstesDatum(datumStart)
    return datumStart

def anzahlTage(datumStart, datumZiel):
    i = 0
    while datumStart != datumZiel:
        datumStart = naechstesDatum(datumStart)
        i = i + 1
    return i
