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



def quickerSort(L, anfang, ende):
    if len(L) > 1:
        pivot = L[anfang]
        links = anfang
        rechts = ende
        while links <= rechts:
            while L[links] < pivot:
                links = links+1
            while L[rechts] > pivot:
                rechts = rechts-1
            if links <= rechts:
                if links < rechts:
                    h = L[links]
                    L[links] = L[rechts]
                    L[rechts] = h
                links = links+1
                rechts = rechts-1
                if rechts < anfang:
                    rechts = anfang
        if anfang < rechts:            
            L = quickerSort(L, anfang, rechts)
        if links < ende:
            L = quickerSort(L, links, ende)
    return L
