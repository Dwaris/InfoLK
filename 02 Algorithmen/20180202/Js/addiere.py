def addiere(wert, liste):
    if liste == []:
        return []
    else:
        return [liste[0] + wert] + addiere(wert, liste[1:])
