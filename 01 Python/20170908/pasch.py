#import
from random import *

#process
w1 = randint(1,6)
w2 = randint(1,6)
w3 = randint(1,6)
w4 = randint(1,6)

versuche = 1

while (w1!=w2)or(w1!=w3):
    w1 = randint(1,6)
    w2 = randint(1,6)
    w3 = randint(1,6)
    w4 = randint(1,6)
    versuche += 1

#output
print("42")
