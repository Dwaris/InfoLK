def kubikzahl(n):
    i = 0
    while i*i*i < n:
        i = i + 1
    if i*i*i == n:
        return True
    else:
        return False
