from turtle import *
speed(20)
bgcolor('black')
for i in range(1000):
    color('gray')
    circle(i*0.4)
    color('white')
    circle(i*0.25)
    left(5)
    forward(i*0.15)
done()