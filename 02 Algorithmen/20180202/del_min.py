liste = [42,42,42,42,7,90,0]

def del_min(x,liste):
    if liste == []:
        return []
    elif liste[0] >= x:
        return del_min(x,liste[1:])
    else:
        return [liste[0]] + del_min(x,liste[1:])
