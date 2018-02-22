def kopieWelt(welt):
    kopie = []
    for zeile in welt:
        kopie = kopie + [zeile[:]]
    return kopie
def anzahlLebendeNachbarn(x, y, welt):
    counter = 0
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if not(i == x and j == y):
                if welt[i][j] != -1:
                    counter += welt[i][j]

    return counter
welt = [[0,0,0,0,0],
        [0,1,1,1,0],
        [0,0,1,0,0],
        [0,0,1,1,0],
        [0,0,0,0,0]]

#print(kopieWelt(welt))
print(anzahlLebendeNachbarn(4,4,welt))
