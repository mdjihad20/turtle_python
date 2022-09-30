from turtle import *
import time

pensize(3)
color('yellow')
bgcolor('black')
speed(5)

penup()
goto(0,0)
pendown()

for i in range(8):
    left(45)
    for i in range(8):
        forward(100)
        left(45)

hideturtle()
time.sleep(10)