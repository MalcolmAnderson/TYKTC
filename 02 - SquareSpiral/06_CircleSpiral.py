# 06_CircleSpiral.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "yellow", "blue", "green"]
for x in range(300):
    t.pencolor(colors[x%4])
    #t.forward(2*x)
    t.circle(x)
    t.left(95)
    
