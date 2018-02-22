def entferneErstes(element, liste):
    if liste == []:
        return []
    elif liste[0] == element:
        return liste[1:]
    else:
        return liste[:1] + entferneErstes(element, liste[1:])
