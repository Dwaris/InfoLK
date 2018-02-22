liste = [[3, 5], 6, [], [4, [2, 9]]]
def flacheListe(liste):
    if len(liste) == 0:
        return []
    if len(liste) == 1:
        if type(liste[0]) == list:
            liste_neu = flacheListe(liste[0])
        else:
            liste_neu = liste
    elif type(liste[0]) == list:
        liste_neu = flacheListe(liste[0]) + flacheListe(liste[1:])
    else:
        liste_neu = [liste[0]] + flacheListe(liste[1:])
    return liste_neu
print(flacheListe(liste))