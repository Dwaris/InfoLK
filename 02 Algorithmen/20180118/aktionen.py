def ggt(x, y):
    z = 0
    while x != y:
        z += 1
        if x > y:
            x = x - y
        else:
            y = y - x
    return x,z

def ggt2(x,y):
    z = 0
    while y > 0:
        z += 1
        r = x % y
        x = y
        y = r
    return x,z
a = 17
b = 17
(ergebnis, zaehler)  = ggt(a, b)
print('ggt(', a, ',', b, ') =', ergebnis)
print('Schleifendurchläufe: ', zaehler)
