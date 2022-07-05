import turtle 

turtle.speed(1)
turtle.bgcolor("white")
turtle.pensize(6)

def mycurve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
turtle.color("darkred", "red")
turtle.begin_fill()

turtle.left(140)
turtle.forward(111.65)
mycurve()

turtle.left(120)
mycurve()
turtle.forward(111.65)
turtle.end_fill()

turtle.hideturtle()
turtle.done()
