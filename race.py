from turtle import Turtle, Screen
import random
import tkinter

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Turtle Race", prompt="Which color turtle is win.")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.pensize(25)
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                tkinter.messagebox.showinfo(title="Result", message=f"You've won! The {winning_color} turtle is the winner")
            else:
                tkinter.messagebox.showinfo(title="Result", message=f"You've loss! The {winning_color} turtle is the winner")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()