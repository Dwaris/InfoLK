L = [8, 5, 3, 7, 1, 4]



def bubbleSort(L):

    # ende läuft von Listenlänge bis 1
    ende = len(L)
    while ende > 0:

        # i läuft von 0 bis ende - 2
        i = 0
        while i < ende - 1:
            
            # Tauscht L[i] mit L[i + 1] falls notwendig
            if L[i + 1] < L[i]:
                h = L[i]
                L[i] = L[i + 1]
                L[i + 1] = h
            
            i = i + 1
        
        ende = ende - 1

    # Liefert sortierte Liste
    return L
