from random import *
liste = []
for i in range(20):
    liste += [randint(0, 50)]

def swap(liste, a, b):
    va = liste[a]
    liste[a] = liste[b]
    liste[b] = va
    return liste

def bubble_sort(liste):
    for j in range(len(liste)):
        for i in range(len(liste)-1-j):
            if liste[i] > liste[i+1]:
                liste = swap(liste, i, i+1)#
    return liste

print(bubble_sort(liste))
