import turtle
import time
t = turtle.Turtle()
t.screen.bgcolor('black')
t.pencolor('white')
t.speed(15)
t.penup()
t.setpos(0,-50)
t.pendown()

for i in range(12):
    t.left(30)
        
    for i in range(12):
        t.left(30)
        t.circle(45)
    t.forward(60)

    
t.hideturtle()
time.sleep(5)