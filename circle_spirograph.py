from turtle import *
import time

pensize(2)
color('yellow')
bgcolor('black')
speed(20)

penup()
goto(0,0)
pendown()

for i in range(6):
    for colors in ['red','blue','green','magenta','yellow','cyan','orange']:
        color(colors)
        circle(100)
        left(10)

hideturtle()
time.sleep(10)