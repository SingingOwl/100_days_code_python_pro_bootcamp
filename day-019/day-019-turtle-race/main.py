import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# List to hold the turtle objects
turtles = []

# Start y-coordinate
start_y = 130

# Create 6 turtles
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_y - index * 50)  # Adjust y-coordinate for each turtle
    turtles.append(new_turtle)

# Your code for the race logic will go here
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() + rand_distance >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()  # Get the winning turtle's color
            print(f"The winner is the {winning_color} turtle!")
            screen.textinput(title="Race Over",
                             prompt=f"The winner is the {winning_color} turtle!\nPress Enter to exit.")
            screen.textinput(title="Race Over",
                             prompt=f"The winner is the {winning_color} turtle!\nPress Enter to exit.")
            #break

screen.exitonclick()
