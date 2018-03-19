L = [8, 5, 3, 7, 1, 4]



def selectionSort(L):

    # unsortiert läuft von 0 bis zur Listenlänge - 2
    unsortiert = 0
    while unsortiert < len(L) - 1:

        # Sucht kleinstes Element ab unsortiert
        kleinstes = unsortiert
        i = kleinstes + 1
        while i < len(L):
            if L[i] < L[kleinstes]:
                kleinstes = i
            i = i + 1

        # Tauscht kleinstes Element mit erstem unsortierten
        h = L[unsortiert]
        L[unsortiert] = L[kleinstes]
        L[kleinstes] = h

        unsortiert = unsortiert + 1

    # Liefert sortierte Liste
    return L
