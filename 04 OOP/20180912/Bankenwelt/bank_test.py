from bank import *
bank = Bank()

# Konto eröffnen
print("Neues Konto")
name = input("Name: ")
vorname = input("Vorname: ")
bank.kontoEroeffnen(name, vorname)
print()

# Konto eröffnen
print("Neues Konto")
name = input("Name: ")
vorname = input("Vorname: ")
bank.kontoEroeffnen(name, vorname)
print()

# Konto eröffnen
print("Neues Konto")
name = input("Name: ")
vorname = input("Vorname: ")
bank.kontoEroeffnen(name, vorname)
print()

# Ausgabe der Kunden und Konten
for kunde in bank.kunden:
    print("Kunde:")
    print("Name:", kunde.name)
    print("Vorname:", kunde.vorname)
    print("Kontonummer:", kunde.konto.nr)
    print("Kontostand:", kunde.konto.stand)
    print()

# Transaktion
print("Einzahlung")
kontonummer = int(input("Kontonummer: "))
betrag = float(input("Betrag: "))
bank.einzahlen(kontonummer, betrag)
print()

# Transaktion
print("Auszahlung")
kontonummer = int(input("Kontonummer: "))
betrag = float(input("Betrag: "))
bank.auszahlen(kontonummer, betrag)
print()

# Transaktion
print("Überweisung")
vonKontonummer = int(input("Von Kontonummer: "))
nachKontonummer = int(input("Nach Kontonummer: "))
betrag = float(input("Betrag: "))
bank.ueberweisen(vonKontonummer, nachKontonummer, betrag)
print()

# Ausgabe der konten
for kunde in bank.kunden:
    print("Kunde:")
    print("Name:", kunde.name)
    print("Vorname:", kunde.vorname)
    print("Kontonummer:", kunde.konto.nr)
    print("Kontostand:", kunde.konto.stand)

