liste = ['b','c','a','y','b']
def del_all(x,liste):
    if liste == []:
        return []
    if x == liste[0]:
        return del_all(x, liste[1:])
    else:
        return [liste[0]] + del_all(x, liste[1:])

del_all('a',liste)
