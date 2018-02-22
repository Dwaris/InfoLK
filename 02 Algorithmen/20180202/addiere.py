liste = [4,5,6,7,8,9,42]

def addiere(x,liste):
    if liste == []:
        return []
    else:
        return [liste[0]+x] + addiere(x,liste[1:])
