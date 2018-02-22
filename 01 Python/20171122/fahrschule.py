def reaktionsweg(speed):
    return (speed/10)*3

def bremsweg(speed):
    return (speed/10)**2

def anhalteweg(speed):
    return reaktionsweg(speed)+bremsweg(speed)

speed = int(input("Geschwindigkeit in km/h: "))

print("""
Dein Reaktionsweg beträgt {}
Dein Bremsweg beträgt {}
Dein Anhalteweg beträgt {}
""".format(reaktionsweg(speed),bremsweg(speed),anhalteweg(speed)))
