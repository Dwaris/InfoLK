def entferneKleiner(wert, liste):
    if liste == []:
        return []
    elif liste[0] < wert:
        return entferneKleiner(wert, liste[1:])
    else:
        return liste[:1] + entferneKleiner(wert, liste[1:])
