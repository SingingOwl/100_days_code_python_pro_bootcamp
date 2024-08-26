from turtle import *
import random

screen = Screen()
screen.bgcolor("black")
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
timmy_the_turtle.speed(10000000000000000000000000000000000000000000000000)

timmy_the_turtle.goto(-50,-150)
loop = 100
# while loop > 0:
#     t.color("red")
#     t.forward(10)
#     t.color("white")
#     t.forward(10)
#     loop -= 1

# Define a function to generate a random color
def random_color():
    return (random.random(), random.random(), random.random())

for sides in range(3,100):

    screen.bgcolor(random_color())
    for iteration in range (1,sides+1):
        timmy_the_turtle.forward(20)
        timmy_the_turtle.left(360/sides)
        timmy_the_turtle.color(random_color())


screen.exitonclick()