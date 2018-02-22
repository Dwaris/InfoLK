x = int(input("natütrliche Zahle größer 1: ", ))
y = int(input("natütrliche Zahle größer 1: ", ))
h = 0
while y > 0:
    h = x % y
    x = y
    y = h
print(x)
