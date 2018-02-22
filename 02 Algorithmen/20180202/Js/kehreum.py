def kehreum(liste):
    if liste == []:
        return []
    else:
        return kehreum(liste[1:]) + liste[:1]
