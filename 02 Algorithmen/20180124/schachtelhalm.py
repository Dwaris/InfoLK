from turtle import *

def schachtelhalm(l):
    if l > 2:
        forward(l)
        left(30)
        schachtelhalm(l/2)
        right(30)
        forward(l)
        schachtelhalm(l/2)
        backward(l)
        right(30)
        schachtelhalm(l/2)
        left(30)
        backward(l)

penup()
goto(0,-150)
pendown()
left(90)
speed(0)
schachtelhalm(100)
