def galton(x, y):
    if x < y:
        return None
    else:
        if (y == 0) or (x == y):
            return 1
        else:
            return (galton(x-1, y-1) + galton(x-1, y))
galton(0, 2)
