L = [8, 5, 3, 7, 1, 4]



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
