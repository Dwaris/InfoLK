#Initalisierung
kapital = float(input("Kapital: "))
zinssatz = float(input("Zinssitz: "))
n = float(input("Jahre der Kapitalverzinsung: "))
ziel = float(input("Zielbetrag: "))
jahr = 0

#Iterierung
while jahr < n:
    zinsen = kapital * (zinssatz/100)
    kapital = kapital + zinsen
    print(kapital)
    jahr =  jahr + 1
    
#Ausgabe
print("Kapital nach ", int(n) ,"Jahren: ")
input('Press ENTER to exit')
