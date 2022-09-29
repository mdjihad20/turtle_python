from turtle import *
import time

pensize(0)
color('white')
bgcolor('black')
speed(20)

forw = 1

for i in range(1000):
    forward(forw)
    left(120)
    left(1)
    forw += 1


hideturtle()
time.sleep(10)