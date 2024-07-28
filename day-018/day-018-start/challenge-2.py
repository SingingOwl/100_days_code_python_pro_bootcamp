from turtle import *

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
loop = 100
while loop > 0:
    timmy_the_turtle.color("red")
    timmy_the_turtle.forward(10)
    timmy_the_turtle.color("white")
    timmy_the_turtle.forward(10)
    loop -= 1


screen = Screen()
screen.exitonclick()