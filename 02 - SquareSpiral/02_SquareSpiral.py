import turtle
t = turtle.Pen()
t.speed(0)
colors = ["blue", "blue", "blue", "blue"]
for x in range(300):
    t.pencolor(colors[ x % 4] )
    t.forward(1*x)
    t.left(91)
    
