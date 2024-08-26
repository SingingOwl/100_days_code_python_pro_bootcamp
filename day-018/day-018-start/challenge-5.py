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

#t.width(8)

radius = 100
angle = 0

for i in range(1, 360):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.setheading(angle)
    angle += 1
    #t.forward(20)
    timmy_the_turtle.circle(radius)

    # code to keep turtle within screen boundaries
    # Check if the turtle is near the edge of the canvas
    # x, y = t.position()
    # screen_width = screen.window_width() // 2
    # screen_height = screen.window_height() // 2
    #
    # if x < -screen_width or x > screen_width or y < -screen_height or y > screen_height:
    #     t.undo()  # Undo the last movement
    #     t.left(random_angle())  # Turn left to change direction
    #     t.forward(20)

screen.exitonclick()