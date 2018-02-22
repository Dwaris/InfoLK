from turtle import *

def sierpinski(grundseite):
    if grundseite > 5:
        for i in range(3):
            forward(grundseite)
            left(120)
            sierpinski(grundseite/2)

speed(0)
sierpinski(200)
input()
