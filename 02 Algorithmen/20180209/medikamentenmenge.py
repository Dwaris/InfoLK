def medikamentenmenge(n):
    if n == 0:
        return 5
    else:
        return 5 + medikamentenmenge(n-1) * 0.6

print(medikamentenmenge((9)))
