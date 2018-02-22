def fakultät(n):
    if n == 1:
        return 1
    else:
        return n * fakultät(n-1)

n = int(input("Gib eine Zahl n an: "))

print("""
{}! = {}
""".format(n,fakultät(n)))
