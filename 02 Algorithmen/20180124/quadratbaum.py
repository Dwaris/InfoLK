from turtle import *

def quadratbaum(l):
    if l > 5:
        left(90)
        forward(l/2)
        right(90)
        forward(l)
        left(45)
        quadratbaum(l/2)
        right(135)
        forward(l)
        left(45)
        quadratbaum(l/2)
        right(135)
        forward(l)
        right(90)
        forward(l/2)
        right(90)

left(90) # Damit der Baum nach oben wächst
speed(0)
quadratbaum(100)
