from turtle import *

# Deklaration der Zeichenprozedur
def baum(stamm):
    if stamm >= 2:
        forward(stamm)
        right(45)
        baum(stamm // 2)
        left(90)
        baum(stamm // 2)
        right(45)
        backward(stamm)

# Test der Zeichenprozedur
left(90)
baum(200)
