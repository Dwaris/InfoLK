


from tkinter import *

class GUIZaehler(object):
    def __init__(self, zaehler):
        self.zaehler = zaehler
        self.fenster = Tk()
        self.fenster.title("Zaehler")
        self.fenster.geometry('120x110')

        self.labelZaehler = Label(master=self.fenster, 
                           text=str(self.zaehler.stand), 
                           background="#FBD975")
        self.labelZaehler.place(x=45, y=40, width=30, height=30)

        self.buttonZaehler = Button(master=self.fenster, 
                               text="weiterzaehlen", 
                               command=self.Button_Zaehler_Click)
        self.buttonZaehler.place(x=10, y=80, width=100, height=20)


    def Button_Zaehler_Click(self):
        self.zaehler.weiterzaehlen()
        self.labelZaehler.config(text=str(self.zaehler.stand))


from zaehler import *
zaehler = Zaehler()

guizaehler = GUIZaehler(zaehler)
guizaehler.fenster.mainloop()
