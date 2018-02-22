liste = [32, 12, 4, 9, 11, 200, 87, 23]



def selectionSort(L):

    # Gehe Liste durch
    aktPos = 0
    while aktPos < len(L) - 1:

        # Suche kleinstes Element im unsortierten Bereich
        minPos = aktPos
        suchPos = aktPos + 1
        while suchPos < len(L):
            if L[suchPos] < L[minPos]:
                minPos = suchPos
            suchPos = suchPos + 1

        # Tausche kleinstes Element mit aktuellem Element
        h = L[aktPos]
        L[aktPos] = L[minPos]
        L[minPos] = h

        aktPos = aktPos + 1

    # Liefere sortiere Liste zurück
    return L



def insertionSort(L):

    # Gehe Liste durch
    aktPos = 1
    while aktPos < len(L):

        # Füge aktuelles Element ein
        akt = L[aktPos]
        einPos = aktPos
        while (einPos > 0) and (L[einPos - 1] > akt):
            L[einPos] = L[einPos - 1]
            einPos = einPos - 1
        L[einPos] = akt

        aktPos = aktPos + 1

    # Liefere sortierte Liste zurück
    return L



def bubbleSort(L):

    # Gehe Liste durch
    ende = len(L)
    while ende > 0:

        # Lässt Element aufsteigen
        aktPos = 0
        while aktPos < ende - 1:
            if L[aktPos + 1] < L[aktPos]:
                h = L[aktPos]
                L[aktPos] = L[aktPos + 1]
                L[aktPos + 1] = h
            aktPos = aktPos + 1

        ende = ende - 1

    # Liefere sortierte Liste zurück
    return L



def quickSort(L):

    # Rekursionsanfang
    if L != []:

        # Zerlege Liste in zwei Teile
        pivot = L[0]
        kleinerPivot = []
        groessergleichPivot = []
        for e in L[1:]:
            if e < pivot:
                kleinerPivot = kleinerPivot + [e]
            else:
                groessergleichPivot = groessergleichPivot + [e]

        # Rekursionsschritt
        kleinergPivotSortiert = quickSort(kleinerPivot)
        groessergleichPivotSortiert = quickSort(groessergleichPivot)
        LSortiert = kleinergPivotSortiert + [pivot] + groessergleichPivotSortiert

    else:
        LSortiert = []

    # Liefere sortierte Liste zurück
    return LSortiert
