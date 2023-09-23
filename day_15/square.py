from turtle import Turtle, Screen

trishan_turtle = Turtle()

for _ in range(4):
    trishan_turtle.forward(100)
    trishan_turtle.left(90)

screen = Screen()
screen.exitonclick()