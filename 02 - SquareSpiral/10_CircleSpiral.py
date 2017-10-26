# 10_CircleSpiral.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = 10 #eval(input('Enter a number of sides between 2 and 8 : '))
offset = 1
colors = ["red", "yellow", "blue", "white", "orange", "green", "purple", "salmon", "light blue", "dark orange"]
for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + offset)
    t.width(x * sides / 100)
    
