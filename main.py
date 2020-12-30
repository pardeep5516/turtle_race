from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()

screen.listen()
screen.onkey(fun=move_forward, key="d")
screen.onkey(fun=move_backward, key="a")
screen.onkey(fun=turn_left, key="w")
screen.onkey(fun=turn_right, key="s")
screen.onkey(fun=clear, key='c')

screen.exitonclick()
