from time import *
from random import randint
import sort

# Initialisierung der Anzahl der Listenelemente
anzahl = 1000
while anzahl <= 10000:
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
