from random import randint

ratezahl = randint(0,99)
gefunden = False

while not gefunden:
    vorschlag = int(input("Vorschlag:"))
    if vorschlag < ratezahl:
        print("Zu klein!")
    elif vorschlag > ratezahl:
        print("Zu groß!")
    else:
        print("Treffer!")
        gefunden = True