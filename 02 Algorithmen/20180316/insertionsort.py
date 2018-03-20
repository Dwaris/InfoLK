L = [8, 5, 3, 7, 1, 4]



def insertionSort(L):

    # einfuegen läuft von 1 bis Listenlänge - 1
    einfuegen = 1
    while einfuegen < len(L):

        # i läuft von einfuegen rückwärts bis L[i - 1] nicht größer ist als das einzufügende Element
        einfuegenElement = L[einfuegen]
        i = einfuegen
        while(i > 0) and (L[i - 1] > einfuegenElement):

            # L[i - 1] rückt eins nach rechts
            L[i] = L[i - 1]
            i = i - 1

        # Das einzufügende Element wird an i eingefügt
        L[i] = einfuegenElement

        einfuegen = einfuegen + 1

    # Liefert sortierte Liste
    return L
