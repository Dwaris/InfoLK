L = [8, 5, 3, 7, 1, 4]



def quickSort(L):

    # Rekursionsanfang
    if L != []:

        # Zerlegt die Liste in zwei Teile in Abhängigkeit des nullten Elements
        pivot = L[0]
        kleinerPivot = []
        groessergleichPivot = []
        for e in L[1:]:
            if e < pivot:
                kleinerPivot = kleinerPivot + [e]
            else:
                groessergleichPivot = groessergleichPivot + [e]

        # Liefert sortierte Liste
        return quickSort(kleinerPivot) + [pivot] + quickSort(groessergleichPivot)

    else:
        return []
