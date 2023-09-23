from turtle import Turtle, Screen
trishan_turtle = Turtle()

for _ in range(20):
    trishan_turtle.forward(10)
    trishan_turtle.penup()
    trishan_turtle.forward(10)
    trishan_turtle.pendown()
    
screen = Screen()
screen.exitonclick()