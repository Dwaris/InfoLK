liste = [4,5,2,3,42]

def reverse(liste):
    if len(liste) == 0:
        return []
    return [liste[-1]] + reverse(liste[:-1])

print(reverse(liste))
