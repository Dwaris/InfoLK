L = [54,26,93,17,77,31,2,44,55,20]

def bubblesort(L):
    ende = len(L)-1
    while ende > 0:
        i = 0
        while i < ende:
            if L[i] > L[i+1]:
                h = L[i]
                L[i] = L[i+1]
                L[i+1] = h
            i += 1
        ende -= 1
bubblesort(L)
print(L)
