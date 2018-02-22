gaeste = ['b','b','d','a']

def anzahl(x,gaeste):
    if gaeste == []:
        return 0
    elif x == gaeste[0]:
        return 1 + anzahl(x, gaeste[1:])
    else:
        return anzahl(x,gaeste[1:])