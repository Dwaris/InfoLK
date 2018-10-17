#-----------------------------------------------------------
# GUI-Klasse
#-----------------------------------------------------------

from tkinter import *

class GUIBank():
    def __init__(self, bank):
        # Referenzattribute zum Datenmodell
        self.bank = bank
        # Erzeugung des Fensters
        self.fenster = Tk()
        self.fenster.title("Bank")
        self.fenster.geometry("455x275")


        # Rahmen Kontoerzeugung
        self.rahmenErzeugen = Frame(master=self.fenster, background="#FFCFC9")
        self.rahmenErzeugen.place(x=5, y=5, width=220, height=130)
        # Button Erzeugen
        self.buttonErzeugen = Button(master=self.rahmenErzeugen, text="erzeugen", 
                                command=self.Button_Erzeugen_Click)
        self.buttonErzeugen.place(x=5, y=5, width=145, height=20)
        # Label mit Aufschrift Name
        self.labelName = Label(master=self.rahmenErzeugen, background="white", text="Name")
        self.labelName.place(x=5, y=30, width=145, height=20)
        # Entry für den Namen
        self.entryName = Entry(master=self.rahmenErzeugen)
        self.entryName.place(x=155, y=30, width=60, height=20)
        # Label mit Aufschrift Vorname
        self.labelVorname = Label(master=self.rahmenErzeugen, background="white", text="Vorname")
        self.labelVorname.place(x=5, y=55, width=145, height=20)
        # Entry für den Vornamen
        self.entryVorname = Entry(master=self.rahmenErzeugen)
        self.entryVorname.place(x=155, y=55, width=60, height=20)
        # Label mit Aufschrift Kontonummer
        self.labelAufschriftKontonummer1 = Label(master=self.rahmenErzeugen, background="white", 
                                           text="Kontonummer")
        self.labelAufschriftKontonummer1.place(x=5, y=80, width=145, height=20)
        # Label Kontonummer
        self.labelKontonummer = Label(master=self.rahmenErzeugen, background="white", text=str(bank.naechsteKontoNr))
        self.labelKontonummer.place(x=155, y=80, width=60, height=20)
        # Label mit Aufschrift Kontostand
        self.labelAufschriftKontostandErzeugen = Label(master=self.rahmenErzeugen, background="white", 
                                           text="Kontostand")
        self.labelAufschriftKontostandErzeugen.place(x=5, y=105, width=145, height=20)

        # Label Kontostand
        self.labelKontostandErzeugen = Label(master=self.rahmenErzeugen, background="white", text=str(0.0))
        self.labelKontostandErzeugen.place(x=155, y=105, width=60, height=20)

        # Rahmen Konto
        self.rahmenKonto = Frame(master=self.fenster, background="#D5E88F")
        self.rahmenKonto.place(x=5, y=140, width=220, height=130)
        # Button Anzeigen
        self.buttonAnzeigen = Button(master=self.rahmenKonto, text="anzeigen", 
                                command=self.Button_Anzeigen_Click)
        self.buttonAnzeigen.place(x=5, y=5, width=145, height=20)
        # Label mit Aufschrift Kontonummer
        self.labelAufschriftKontonummer = Label(master=self.rahmenKonto, background="white", 
                                           text="Kontonummer")
        self.labelAufschriftKontonummer.place(x=5, y=30, width=145, height=20)
        # Entry Kontonummer
        self.entryKontonummerAnzeigen = Entry(master=self.rahmenKonto)
        self.entryKontonummerAnzeigen.place(x=155, y=30, width=60, height=20)
        # Label mit Aufschrift Name
        self.labelAufschriftName = Label(master=self.rahmenKonto, background="white", text="Name")
        self.labelAufschriftName.place(x=5, y=55, width=145, height=20)
        # Label Name
        self.labelNameAnzeigen = Label(master=self.rahmenKonto, background="white", text="")
        self.labelNameAnzeigen.place(x=155, y=55, width=60, height=20)
        # Label mit Aufschrift Vorname
        self.labelAufschriftVorname = Label(master=self.rahmenKonto, background="white", text="Vorname")
        self.labelAufschriftVorname.place(x=5, y=80, width=145, height=20)
        # Label Vornme
        self.labelVornameAnzeigen = Label(master=self.rahmenKonto, background="white", text="")
        self.labelVornameAnzeigen.place(x=155, y=80, width=60, height=20)
        # Label mit Aufschrift Kontostand
        self.labelAufschriftKontostand = Label(master=self.rahmenKonto, background="white", text="Kontostand")
        self.labelAufschriftKontostand.place(x=5, y=105, width=145, height=20)
        # Label Kontostand
        self.labelKontostand = Label(master=self.rahmenKonto, background="white", text="")
        self.labelKontostand.place(x=155, y=105, width=60, height=20)

        # Rahmen Transaktion
        self.rahmenTransaktion = Frame(master=self.fenster, background="#FBD975")
        self.rahmenTransaktion.place(x=230, y=5, width=220, height=265)
        # Label mit Aufschrift Kontonummer
        self.labelAufschriftKontonummer2 = Label(master=self.rahmenTransaktion, background="white", 
                                           text="Kontonummer")
        self.labelAufschriftKontonummer2.place(x=5, y=5, width=145, height=20)
        # Entry Kontonummer
        self.entryKontonummer = Entry(master=self.rahmenTransaktion)
        self.entryKontonummer.place(x=155, y=5, width=60, height=20)
        # Button Einzahlen
        self.buttonEinzahlen = Button(master=self.rahmenTransaktion, text="einzahlen", 
                                 command=self.Button_Einzahlen_Click)
        self.buttonEinzahlen.place(x=5, y=55, width=145, height=20)
        # Label mit Aufschrift Betrag
        self.labelAufschriftEinzahlungsbetrag = Label(master=self.rahmenTransaktion, 
                                                 background="white", text="Einzahlungsbetrag")
        self.labelAufschriftEinzahlungsbetrag.place(x=5, y=80, width=145, height=20)
        # Entry Betrag
        self.entryEinzahlungsbetrag = Entry(master=self.rahmenTransaktion)
        self.entryEinzahlungsbetrag.place(x=155, y=80, width=60, height=20)
        # Button Auszahlen
        self.buttonAuszahlen = Button(master=self.rahmenTransaktion, text="auszahlen", 
                                 command=self.Button_Auszahlen_Click)
        self.buttonAuszahlen.place(x=5, y=105, width=145, height=20)
        # Label mit Aufschrift Betrag
        self.labelAufschriftAuszahlungsbetrag = Label(master=self.rahmenTransaktion, 
                                                 background="white", text="Auszahlungsbetrag")
        self.labelAufschriftAuszahlungsbetrag.place(x=5, y=130, width=145, height=20)
        # Entry Betrag
        self.entryAuszahlungsbetrag = Entry(master=self.rahmenTransaktion)
        self.entryAuszahlungsbetrag.place(x=155, y=130, width=60, height=20)
        # Button Überweisen
        self.buttonUeberweisen = Button(master=self.rahmenTransaktion, text="überweisen", 
                                   command=self.Button_Ueberweisen_Click)
        self.buttonUeberweisen.place(x=5, y=190, width=145, height=20)
        # Label mit Aufschrift Zielkontonummer
        self.labelAufschriftZielkontonummer = Label(master=self.rahmenTransaktion, 
                                               background="white", text="Zielkontonummer")
        self.labelAufschriftZielkontonummer.place(x=5, y=215, width=145, height=20)
        # Entry Kontonummer
        self.entryZielkontonummer = Entry(master=self.rahmenTransaktion)
        self.entryZielkontonummer.place(x=155, y=215, width=60, height=20)
        # Label mit Aufschrift Betrag
        self.labelAufschriftBetrag = Label(master=self.rahmenTransaktion, background="white", 
                                      text="Überweisungsbetrag")
        self.labelAufschriftBetrag.place(x=5, y=240, width=145, height=20)
        # Entry Betrag
        self.entryUeberweisungsbetrag = Entry(master=self.rahmenTransaktion)
        self.entryUeberweisungsbetrag.place(x=155, y=240, width=60, height=20)

    def Button_Erzeugen_Click(self):
        name = self.entryName.get()
        vorname = self.entryVorname.get()
        self.bank.kontoEroeffnen(name, vorname)
        self.entryName.delete(0, END)
        self.entryVorname.delete(0, END)
        self.labelKontonummer.config(text=str(self.bank.naechsteKontoNr))
        self.labelKontostandErzeugen.config(text=str(0.0))
           
    def Button_Anzeigen_Click(self):
        kontonummer = int(self.entryKontonummerAnzeigen.get())
        konto = self.bank.getKonto(kontonummer)
        if konto != None:
            self.labelNameAnzeigen.config(text=str(konto.inhaber.name))
            self.labelVornameAnzeigen.config(text=str(konto.inhaber.vorname))
            self.labelKontostand.config(text=str(konto.stand))
        else:
            self.labelNameAnzeigen.config(text='')
            self.labelVornameAnzeigen.config(text='')
            self.labelKontostand.config(text='')

    def Button_Einzahlen_Click(self):
        kontonummer = int(self.entryKontonummer.get())
        betrag = float(self.entryEinzahlungsbetrag.get())
        self.bank.einzahlen(kontonummer, betrag)
        self.entryKontonummer.delete(0, END)
        self.entryEinzahlungsbetrag.delete(0, END)

    def Button_Auszahlen_Click(self):
        kontonummer = int(self.entryKontonummer.get())
        betrag = float(self.entryAuszahlungsbetrag.get())
        self.bank.auszahlen(kontonummer, betrag)
        self.entryKontonummer.delete(0, END)
        self.entryAuszahlungsbetrag.delete(0, END)

    def Button_Ueberweisen_Click(self):
        kontonummer = int(self.entryKontonummer.get())
        zielkontonummer = int(self.entryZielkontonummer.get())
        betrag = float(self.entryUeberweisungsbetrag.get())
        self.bank.ueberweisen(kontonummer, zielkontonummer, betrag)
        self.entryKontonummer.delete(0, END)
        self.entryZielkontonummer.delete(0, END)
        self.entryUeberweisungsbetrag.delete(0, END)

#-----------------------------------------------------------
# Datenmodellobjekte
#-----------------------------------------------------------

from bank import *
bank = Bank()

#-----------------------------------------------------------
# GUI-Objekte
#-----------------------------------------------------------


guibank = GUIBank(bank)
guibank.fenster.mainloop()
