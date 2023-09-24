from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def move_left():
    t.left(10)

def move_right():
    t.right(10)

def clear_screen():
      t.clear()
      t.penup()
      t.home()
      t.pendown()


s.listen()
s.onkey(key="w", fun=move_forward)
s.onkey(key="a", fun=move_left)
s.onkey(key="s", fun=move_backward)
s.onkey(key="d", fun=move_right)
s.onkey(clear_screen, "c")








s.exitonclick()