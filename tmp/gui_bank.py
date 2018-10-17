#-----------------------------------------------------------
# Datenmodell
#-----------------------------------------------------------

from bank import *
bank = Bank()

#-----------------------------------------------------------
# GUI
#-----------------------------------------------------------

from tkinter import *

def Button_Erzeugen_Click():
    name = entryName.get()
    vorname = entryVorname.get()
    bank.kontoEroeffnen(name, vorname)
    entryName.delete(0, END)
    entryVorname.delete(0, END)
    labelKontonummer.config(text=str(bank.naechsteKontoNr))
    labelKontostandErzeugen.config(text=str(0.0))
       
def Button_Anzeigen_Click():
    kontonummer = int(entryKontonummerAnzeigen.get())
    konto = bank.getKonto(kontonummer)
    if konto != None:
        labelNameAnzeigen.config(text=str(konto.inhaber.name))
        labelVornameAnzeigen.config(text=str(konto.inhaber.vorname))
        labelKontostand.config(text=str(konto.stand))
    else:
        labelNameAnzeigen.config(text='')
        labelVornameAnzeigen.config(text='')
        labelKontostand.config(text='')

def Button_Einzahlen_Click():
    bank.einzahlen(int(entryKontonummer.get()), float(entryEinzahlungsbetrag.get()))
    entryKontonummer.delete(0, END)
    entryEinzahlungsbetrag.delete(0, END)

def Button_Auszahlen_Click():
    bank.auszahlen(int(entryKontonummer.get()), float(entryAuszahlungsbetrag.get()))
    entryKontonummer.delete(0, END)
    entryAuszahlungsbetrag.delete(0, END)

def Button_Ueberweisen_Click():
    bank.ueberweisen(int(entryKontonummer.get(), int(entryZielkontonummer.get()), float(entryUeberweisungsbetrag.get()))
    entryKontonummer.delete(0,END)
    entryZielkontonummer.delete(0,END)
    entryUeberweisungsbetrag.delete(0,END)

# Erzeugung des Fensters
fenster = Tk()
fenster.title("Bank")
fenster.geometry('455x275')

# Rahmen Kontoerzeugung
rahmenErzeugen = Frame(master=fenster, background="#FFCFC9")
rahmenErzeugen.place(x=5, y=5, width=220, height=130)
# Button Erzeugen
buttonErzeugen = Button(master=rahmenErzeugen, text="erzeugen", 
                        command=Button_Erzeugen_Click)
buttonErzeugen.place(x=5, y=5, width=145, height=20)
# Label mit Aufschrift Name
labelName = Label(master=rahmenErzeugen, background="white", text="Name")
labelName.place(x=5, y=30, width=145, height=20)
# Entry für den Namen
entryName = Entry(master=rahmenErzeugen)
entryName.place(x=155, y=30, width=60, height=20)
# Label mit Aufschrift Vorname
labelVorname = Label(master=rahmenErzeugen, background="white", text="Vorname")
labelVorname.place(x=5, y=55, width=145, height=20)
# Entry für den Vornamen
entryVorname = Entry(master=rahmenErzeugen)
entryVorname.place(x=155, y=55, width=60, height=20)
# Label mit Aufschrift Kontonummer
labelAufschriftKontonummer1 = Label(master=rahmenErzeugen, background="white", 
                                   text="Kontonummer")
labelAufschriftKontonummer1.place(x=5, y=80, width=145, height=20)
# Label Kontonummer
labelKontonummer = Label(master=rahmenErzeugen, background="white", text=str(bank.naechsteKontoNr))
labelKontonummer.place(x=155, y=80, width=60, height=20)
# Label mit Aufschrift Kontostand
labelAufschriftKontostandErzeugen = Label(master=rahmenErzeugen, background="white", 
                                   text="Kontostand")
labelAufschriftKontostandErzeugen.place(x=5, y=105, width=145, height=20)

# Label Kontostand
labelKontostandErzeugen = Label(master=rahmenErzeugen, background="white", text=str(0.0))
labelKontostandErzeugen.place(x=155, y=105, width=60, height=20)

# Rahmen Konto
rahmenKonto = Frame(master=fenster, background="#D5E88F")
rahmenKonto.place(x=5, y=140, width=220, height=130)
# Button Anzeigen
buttonAnzeigen = Button(master=rahmenKonto, text="anzeigen", 
                        command=Button_Anzeigen_Click)
buttonAnzeigen.place(x=5, y=5, width=145, height=20)
# Label mit Aufschrift Kontonummer
labelAufschriftKontonummer = Label(master=rahmenKonto, background="white", 
                                   text="Kontonummer")
labelAufschriftKontonummer.place(x=5, y=30, width=145, height=20)
# Entry Kontonummer
entryKontonummerAnzeigen = Entry(master=rahmenKonto)
entryKontonummerAnzeigen.place(x=155, y=30, width=60, height=20)
# Label mit Aufschrift Name
labelAufschriftName = Label(master=rahmenKonto, background="white", text="Name")
labelAufschriftName.place(x=5, y=55, width=145, height=20)
# Label Name
labelNameAnzeigen = Label(master=rahmenKonto, background="white", text="")
labelNameAnzeigen.place(x=155, y=55, width=60, height=20)
# Label mit Aufschrift Vorname
labelAufschriftVorname = Label(master=rahmenKonto, background="white", text="Vorname")
labelAufschriftVorname.place(x=5, y=80, width=145, height=20)
# Label Vornme
labelVornameAnzeigen = Label(master=rahmenKonto, background="white", text="")
labelVornameAnzeigen.place(x=155, y=80, width=60, height=20)
# Label mit Aufschrift Kontostand
labelAufschriftKontostand = Label(master=rahmenKonto, background="white", text="Kontostand")
labelAufschriftKontostand.place(x=5, y=105, width=145, height=20)
# Label Kontostand
labelKontostand = Label(master=rahmenKonto, background="white", text="")
labelKontostand.place(x=155, y=105, width=60, height=20)

# Rahmen Transaktion
rahmenTransaktion = Frame(master=fenster, background="#FBD975")
rahmenTransaktion.place(x=230, y=5, width=220, height=265)
# Label mit Aufschrift Kontonummer
labelAufschriftKontonummer2 = Label(master=rahmenTransaktion, background="white", 
                                   text="Kontonummer")
labelAufschriftKontonummer2.place(x=5, y=5, width=145, height=20)
# Entry Kontonummer
entryKontonummer = Entry(master=rahmenTransaktion)
entryKontonummer.place(x=155, y=5, width=60, height=20)
# Button Einzahlen
buttonEinzahlen = Button(master=rahmenTransaktion, text="einzahlen", 
                         command=Button_Einzahlen_Click)
buttonEinzahlen.place(x=5, y=55, width=145, height=20)
# Label mit Aufschrift Betrag
labelAufschriftEinzahlungsbetrag = Label(master=rahmenTransaktion, 
                                         background="white", text="Einzahlungsbetrag")
labelAufschriftEinzahlungsbetrag.place(x=5, y=80, width=145, height=20)
# Entry Betrag
entryEinzahlungsbetrag = Entry(master=rahmenTransaktion)
entryEinzahlungsbetrag.place(x=155, y=80, width=60, height=20)
# Button Auszahlen
buttonAuszahlen = Button(master=rahmenTransaktion, text="auszahlen", 
                         command=Button_Auszahlen_Click)
buttonAuszahlen.place(x=5, y=105, width=145, height=20)
# Label mit Aufschrift Betrag
labelAufschriftAuszahlungsbetrag = Label(master=rahmenTransaktion, 
                                         background="white", text="Auszahlungsbetrag")
labelAufschriftAuszahlungsbetrag.place(x=5, y=130, width=145, height=20)
# Entry Betrag
entryAuszahlungsbetrag = Entry(master=rahmenTransaktion)
entryAuszahlungsbetrag.place(x=155, y=130, width=60, height=20)
# Button Überweisen
buttonUeberweisen = Button(master=rahmenTransaktion, text="überweisen", 
                           command=Button_Ueberweisen_Click)
buttonUeberweisen.place(x=5, y=190, width=145, height=20)
# Label mit Aufschrift Zielkontonummer
labelAufschriftZielkontonummer = Label(master=rahmenTransaktion, 
                                       background="white", text="Zielkontonummer")
labelAufschriftZielkontonummer.place(x=5, y=215, width=145, height=20)
# Entry Kontonummer
entryZielkontonummer = Entry(master=rahmenTransaktion)
entryZielkontonummer.place(x=155, y=215, width=60, height=20)
# Label mit Aufschrift Betrag
labelAufschriftBetrag = Label(master=rahmenTransaktion, background="white", 
                              text="Überweisungsbetrag")
labelAufschriftBetrag.place(x=5, y=240, width=145, height=20)
# Entry Betrag
entryUeberweisungsbetrag = Entry(master=rahmenTransaktion)
entryUeberweisungsbetrag.place(x=155, y=240, width=60, height=20)

# Aktivierung des Fensters
fenster.mainloop()
