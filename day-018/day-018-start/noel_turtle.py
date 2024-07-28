import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")  # Change the background color

# Set up the turtle
t = turtle.Turtle()
t.speed(1000)  # Fastest speed

# Define a function to generate a random color
def random_color():
    return (random.random(), random.random(), random.random())

# Draw the pattern
for i in range(36):
    t.color(random_color())
    for j in range(36):
        t.forward(200)
        t.left(170)
    t.left(10)

# Keep the window open
turtle.done()