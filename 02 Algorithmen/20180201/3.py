liste = ['b','c','a','y']
def del_first(x,liste):
    if liste == []:
        return []
    if x == liste[0]:
        return del_first(x, liste[1:])
    else:
        return [liste[0]] + del_first(x, liste[1:])

del_first('a',liste)
