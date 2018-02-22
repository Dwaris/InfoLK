def kapital(n):
    if n == 0:
        return 1000
    else:
        return kapital(n-1) + kapital(n-1)*0.05

print(kapital(1))
