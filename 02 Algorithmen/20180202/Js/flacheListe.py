def flacheListe(liste):
    if liste == []:
        return []
    elif type(liste[0]) != list:
        return [liste[0]] + flacheListe(liste[1:])
    else:
        return flacheListe(liste[0]) + flacheListe(liste[1:])
