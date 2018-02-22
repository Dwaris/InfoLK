from turtle import *
import time
speed(0)
def spiderman(x,n):
    y = float(x)/n
    for i in range(0, n+1):
        goto(x - y*i, 0)
        goto(0, y*i)
        goto(-x + y*i, 0)
        goto(0, -y*i)
    reset()
for i in range(50):
    spiderman(500,50)
