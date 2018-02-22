def a_Rechteck(a, b):
    flaecheninhalt = a * b
    return flaecheninhalt

def u_Rechteck(a, b):
    umfang = 2 * a + 2 * b
    return umfang

def v_Quader(a, b, c):
    volumen = a * b * c
    return volumen

def f_Quader(a, b, c):
    flaecheninhalt = 2 * a * b + 2 * a * c + 2 * b * c
    return flaecheninhalt

a = 4
b = 2
c = 3


print(a_Rechteck(a,b))
print(u_Rechteck(a,b))
print(v_Quader(a,b, c))
print(f_Quader(a,b,c))
