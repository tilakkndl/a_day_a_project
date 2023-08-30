import turtle
tim = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    # tim.setheading()
    # tim.setheading(0)
    tim.forward(10)

def move_backward():
    # tim.setheading()
    # tim.setheading(180)
    tim.backward(10)

def move_upward():
    # tim.setheading()
    heading = tim.heading()+10
    tim.setheading(heading)
    # tim.forward(10)


def move_downward():
    # tim.setheading(270)
    heading = tim.heading()-10
    tim.setheading(heading)
    # tim.forward(10)

def clear_sketch():
    tim.clear()  
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
#here onkey is higher order function which is taking function as an argument
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_downward, key="a")
screen.onkey(fun=move_upward, key="d")
screen.onkey(fun=clear_sketch, key="c")

screen.exitonclick()
