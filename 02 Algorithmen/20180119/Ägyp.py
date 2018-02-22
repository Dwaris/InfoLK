def agyp(x, y):
    produkt = 0
    while x > 0:
        if x%2==1:
            produkt = produkt+y
        x= x//2
        y= y//2
    return produkt


            
