from turtle import *

def spirl(abstand, laenge, faktor):
  if laenge > 1:
    for j in range(5):
      forward(laenge)
      left(90)
    right(abstand)
    spirl(abstand, faktor*laenge, faktor)
    
hideturtle()
speed(0)
spirl(135, 200, 0.80)
