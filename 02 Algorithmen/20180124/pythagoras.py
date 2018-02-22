from turtle import *
from math import *
def py(l, n):  
   if n<=0:  
     forward(l)  
   else:
      x = l*sqrt(2)/2
      right(135)
      forward(x)
      left(90)
      py(x,n-1)
      left(90)
      forward(x)
      left(90)
      forward(x)
      right(135)
      forward(l)
      right(135)
      forward(x)
      left(90)
      forward(x)
      left(90)
      py(x,n-1)
      left(90)
      forward(x)
      right(135)

def baum(l,n):
    speed(0)     
    forward(l)
    left(90)
    forward(l)
    left(90)
    py(l,n)
    left(90)
    forward(l)
    

baum(100,10)
