from turtle import *
import random

screen = Screen()
screen.setup(width=800, height=800)  # Adjust the width and height as needed

#screen.bgcolor("black")
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
timmy_the_turtle.speed(10000000000000000000000000000000000000000000000000)



# Define a function to generate a random color
def random_color():
    return (random.random(), random.random(), random.random())

def random_angle():
    angles = [0, 90, 180, 270]
    return random.choice(angles)

timmy_the_turtle.width(8)

while True:
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.left(random_angle())
    timmy_the_turtle.forward(20)

    # code to keep turtle within screen boundaries
    # Check if the turtle is near the edge of the canvas
    x, y = timmy_the_turtle.position()
    screen_width = screen.window_width() // 2
    screen_height = screen.window_height() // 2

    if x < -screen_width or x > screen_width or y < -screen_height or y > screen_height:
        timmy_the_turtle.undo()  # Undo the last movement
        timmy_the_turtle.left(random_angle())  # Turn left to change direction
        timmy_the_turtle.forward(20)

screen.exitonclick()