from time import *
def pot1(x, n):
    p = 1
    i = 0
    c = 0
    while i < n:
        c += 1
        p = p * x
        i = i + 1
    return (p, c)
def pot2(x, y):
    p = 1
    c = 0
    while y > 0:
        c += 1
        if y % 2 == 1:
            p = p * x
        x = x * x
        y = y // 2
    return (p, c)
from time import *

a = 9
b = 10

t1 = clock()
(z,c) = pot2(a, b)
t2 = clock()

t = t2 - t1
print('pot(', a, ',', b, ') =', z)
print('Rechenzeit: ', t)
print('Schleifendurchläufe: ', c)
#erhöht 2 bei jedem durchlauf um 1 bei großen zahlen dauert es deshalb etwas länger
#eine andere möglichlkeit finden, die die große zahl von anfang an sehr stark verkleinert
