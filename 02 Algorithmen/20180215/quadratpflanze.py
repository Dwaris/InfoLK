def flaeche(n, basis):
    if n == 0:
        return basis**2
    else:
        return 3 * flaeche(n-1, basis/3) + basis**2
    
def umfang(n, basis):
    if n == 0:
        return 4*basis
    else:
        return 3 * umfang(n-1, basis/3) + 2 * basis
