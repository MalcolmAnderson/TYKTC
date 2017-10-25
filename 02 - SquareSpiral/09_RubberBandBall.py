# 09_RubberBandBall.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = eval(input('Enter a number of sides between 2 and 8 : '))
#offset = 91
offset = 46
colors = ["red", "yellow", "blue", "orange", "green", "purple", "salmon", "dark orange"]
for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + offset)
    t.width(x * sides / 100)
    
