from turtle import *

def quadratpflanze(l):
    if l > 5:
        left(90)
        forward(l/2)
        right(90)
        forward(l/2)
        left(90)
        quadratpflanze(l/3)
        right(90)
        forward(l/2)
        right(90)
        forward(l/2)
        left(90)
        quadratpflanze(l/3)
        right(90)
        forward(l/2)
        right(90)
        forward(l/2)
        left(90)
        quadratpflanze(l/3)
        right(90)
        forward(l/2)
        right(90)
        forward(l/2)
        right(90)

left(90)
speed(0)
quadratpflanze(200)
