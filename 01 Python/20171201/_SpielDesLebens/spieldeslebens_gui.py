from spieldeslebens import *
from tkinter import *

# Spiel des Lebens
welt1 = [[0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0]
        ]

spiel = SpielDesLebens(42)
#spiel.setWelt(welt1)

# Ereignis
def buttonCountdownClick():
    for i in range(len(zellen)):
        for j in range(len(zellen)):
            if spiel.getZelle(i, j) == 0:
                canvas.itemconfigure(zellen[i][j], fill = 'white')
            else:
                canvas.itemconfigure(zellen[i][j], fill = 'black')
    spiel.neueWelt()
    tkFenster.after(1, buttonCountdownClick)

# Fenster
breite = 500
hoehe  = 500

tkFenster = Tk()
tkFenster.title('Spiel des Lebens')
tkFenster.geometry(str(breite) + 'x' + str(hoehe + 50))

# Button
buttonCountdown = Button(master = tkFenster, text = 'Start', bg = '#FBD975', command = buttonCountdownClick)
buttonCountdown.place(x = 0, y = hoehe, width = breite, height = 50)

# Zellen
canvas = Canvas(master = tkFenster, bg = 'white')
canvas.place(x = 5, y = 5, width = breite, height = hoehe)

zellen = spiel.kopieWelt()
zbreite = breite // spiel.getGroesse()
zhoehe  = hoehe  // spiel.getGroesse()

for i in range(spiel.getGroesse()):
    for j in range(spiel.getGroesse()):
        if spiel.getZelle(i, j) == 0:
            zellen[i][j] = canvas.create_rectangle(j * zbreite, i * zhoehe, j * zbreite + breite, i * zhoehe + hoehe, fill = 'white')
        else:
            zellen[i][j] = canvas.create_rectangle(j * zbreite, i * zhoehe, j * zbreite + breite, i * zhoehe + hoehe, fill = 'black')

# Aktivierung des Fensters
tkFenster.mainloop()
