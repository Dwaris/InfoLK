from random import *
liste = [1588,52,42,23,12]
#for i in range(20):
 #   liste += [randint(0, 50)]

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
            print(liste)
        #print(liste)
    return liste

print(liste)
print()
print(bubble_sort(liste))
