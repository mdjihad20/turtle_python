from turtle import *
speed(15)
bgcolor('black')
color('cyan')
penup()
setpos(0,-160)
pendown()
a = 0
b = 0
for i in range(200):
    forward(a)
    left(b)
    a += 3
    b += 1
hideturtle()
done()