import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Set up the turtle
t = turtle.Turtle()
t.pensize(1)
t.speed(0)  # Fastest speed

# Function to draw a square
def draw_square():
    for _ in range(4):
        t.forward(20)  # Adjust size as needed
        t.right(90)

# Function to draw a heart
def draw_heart():
    t.begin_fill()
    t.left(50)
    t.forward(10)  # Adjust size to fit more hearts on screen
    t.circle(5, 200)  # Adjust size to fit more hearts on screen
    t.right(140)
    t.circle(5, 200)  # Adjust size to fit more hearts on screen
    t.forward(10)  # Adjust size to fit more hearts on screen
    t.end_fill()

# Draw 500 squares and 500 hearts at random positions
for _ in range(500):
    t.color("blue")
    t.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.goto(x, y)
    t.pendown()
    draw_square()

for _ in range(500):
    t.color("red")
    t.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
