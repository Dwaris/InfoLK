L = [1,6,3]

import random


def monkeysort(L):
    while not sort(L):
        random.shuffle(L)
    return L


def sort(L):
    if not L:
        return True
    last = L[0]
    for i in L[1:]:
        if i < last:
            return False
        last = i
    return True

print(monkeysort(L))
