def kapital(n):
    if n == 0:
        return 1000
    else:
        return kapital(n-1)*1.05
