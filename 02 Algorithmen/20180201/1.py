def anzahl(element, liste):
    print("anzahl", element, liste)
    if len(liste) == 0:
        return 0
    else:
        if liste[0] == element:
            print("Element gefunden")
            return (1 + anzahl(element, liste[1:]))
        else:
            return anzahl(element, liste[1:])
