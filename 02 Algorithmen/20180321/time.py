from time import *
from random import randint
from sys import *
import sort

setrecursionlimit(100000)
# Initialisierung der Anzahl der Listenelemente
anzahl = 10000
while anzahl <= 100001:
    # Erzeugung der Liste
    L = []
    for i in range(anzahl):
        L = L + [randint(1, 10*anzahl)]
    # Bestimmung der Rechenzeit beim Sortieren
    t1 = clock()
   #L_sortiert = sort.bubbleSort(L)
   #L_sortiert = sort.selectionSort(L)
   # L_sortiert = sort.insertionSort(L)
    L_sortiert = sort.quickerSort(L,0,len(L)-1)

    t2 = clock()
    t = t2 - t1
    # Ausgabe des Messergebnisses
    print("Anzahl der Listenelemente: ", anzahl, "Rechenzeit: ", t)
    # Erhoehung der Anzahl der Listenelemente
    anzahl = anzahl + 1000
