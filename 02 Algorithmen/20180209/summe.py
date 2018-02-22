def summe(n):
    if n == 0:
        return 0
    return n + summe(n-1)

print(summe(3))