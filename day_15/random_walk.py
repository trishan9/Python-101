import turtle as t
import random

direction = [0, 90, 180, 270]

trishan_turtle = t.Turtle()
t.colormode(255)

trishan_turtle.pensize(15)
trishan_turtle.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

for _ in range(150):
    trishan_turtle.pencolor(random_color())
    trishan_turtle.forward(30)
    trishan_turtle.setheading(random.choice(direction))


screen = t.Screen()
screen.exitonclick()