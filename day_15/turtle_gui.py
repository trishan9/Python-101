from turtle import Turtle, Screen
import random

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
trishan_turtle = Turtle()

def draw_shape(sides, color):
    for _ in range(sides):
        angle = 360/sides
        trishan_turtle.color(color)
        trishan_turtle.forward(100)
        trishan_turtle.right(angle)

for num_sides in range(3, 11):
    random_color = random.choice(colors)
    draw_shape(num_sides, random_color)


screen = Screen()
screen.exitonclick()