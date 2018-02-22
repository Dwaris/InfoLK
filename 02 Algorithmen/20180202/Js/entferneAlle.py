def entferneAlle(element, liste):
    if liste == []:
        return []
    elif liste[0] == element:
        return entferneAlle(element, liste[1:])
    else:
        return liste[:1] + entferneAlle(element, liste[1:])
