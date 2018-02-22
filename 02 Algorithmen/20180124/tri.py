from turtle import *

def tri(l,n):
    if n == 0:
        for i in range (3):
            forward(l)
            left(120)
    else:
        tri(l/2,n-1)
        forward(l/2)
        tri(l/2,n-1)
        left(120)
        forward(l/2)
        right(120)
        tri(l/2,n-1)
        right(120)
        forward(l/2)
        left(120)
hideturtle()
setheading(-30)
speed(0)
tri(300,5)

