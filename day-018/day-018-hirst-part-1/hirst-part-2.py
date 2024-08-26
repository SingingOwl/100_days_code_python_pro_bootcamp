from turtle import *
import random

def random_color():
    return (random.random(), random.random(), random.random())


screen = Screen()
screen.setup(width=800, height=800)  # Adjust the width and height as needed

#screen.bgcolor("black")
t = Turtle()
t.shape("turtle")
t.color("green")
#t.speed(10000000000000000000000000000000000000000000000000)

color_list = [(253, 253, 252), (242, 244, 247), (241, 247, 243), (144, 76, 50), (188, 165, 117), (248, 244, 246),
              (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99),
              (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111),
              (165, 99, 131), (91, 122, 172)]

diameter = 20
move_distance = 50

#t.dot(radius, random_color())

# Move the turtle to a specific position (optional)
t.penup()  # Lift the pen so it doesn't draw a line
t.goto(-300, -300)  # Move to the center of the screen

# Define the number of rows and dots
rows = 10
dots_per_row = 10
dot_size = 20
spacing = 50

# Draw the dots
for row in range(rows):
    for i in range(dots_per_row):
        t.dot(dot_size, random_color())  # Change color as needed
        t.forward(spacing)  # Move to the next position
    # Move the turtle up and back to the start of the row
    t.backward(spacing * dots_per_row)
    t.left(90)
    t.forward(50)
    t.right(90)

# Hide the turtle (optional)
t.hideturtle()

# Keep the window open until it is closed by the user
screen.mainloop()
