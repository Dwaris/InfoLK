from time import *

def ggt(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x

def ggt2(x,y):
    while y > 0:
        r = x % y
        x = y
        y = r
    return x
x = 44
y = 8
t1 = clock()
z = ggt2(444444444,8)
t2 = clock()

t = t2 - t1
print('ggt von {} und {} = {}'.format(x,y,z))
print('Rechenzeit: {} '.format(t))


