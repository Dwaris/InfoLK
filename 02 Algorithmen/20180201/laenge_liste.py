def laenge(liste):
    if liste == []:
        return 0
    else:
        return 1 + laenge(liste[1:]) 
