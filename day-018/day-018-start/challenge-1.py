from turtle import *

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
loop = 4
while loop > 0:
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)
    loop -= 1


screen = Screen()
screen.exitonclick()