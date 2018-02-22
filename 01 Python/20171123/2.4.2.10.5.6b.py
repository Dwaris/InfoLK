def zahlen_quad(anfang, ende):
    zahl = anfang
    while zahl <= ende:
        print(zahl**2)
        zahl = zahl + 1
        if zahl**2 >= ende:
            break

def primzahl(anfang,ende):
    for zahl in range(anfang, ende):
        if zahl > 1:
            for i in range(2, zahl):
                if (zahl % i) == 0:
                    break
            else:
                print(zahl)
