def umfang(n,m):
    if n > 1:
        return umfang(n-1,m)+2*m
    return m*4
def flaecheninhalt(n,m):
    if n > 1:
        return 1/3*flaecheninhalt(n-1, m)+m
    return m**2

print(flaecheninhalt(2,1))
print(umfang(2,1))
