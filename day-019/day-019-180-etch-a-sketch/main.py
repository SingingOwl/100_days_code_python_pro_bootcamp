from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed(0)

def move_up():
    tim.setheading(90)
    tim.forward(10)

def move_down():
    tim.setheading(270)
    tim.forward(10)

def move_left():
    tim.setheading(180)
    tim.forward(10)

def move_right():
    tim.setheading(0)
    tim.forward(10)

def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

def curve_left():
    for _ in range(10):
        tim.left(1)
        tim.forward(1)

def curve_right():
    for _ in range(10):
        tim.right(1)
        tim.forward(1)


# Set up the event listeners once
screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear_screen, "c")

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(curve_left, "Left")
screen.onkey(curve_right, "Right")

screen.exitonclick()



