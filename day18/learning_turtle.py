from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
import random

# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
import heroes

# print(heroes.gen())

#Challenge 1
# for _ in range(4):
    # timmy_the_turtle.backward(100)
    # timmy_the_turtle.left(90)

# timmy_the_turtle.up()
# timmy_the_turtle.setpos(-300, 0)
# timmy_the_turtle.down()

# #Challenge 2
# for _ in range(50):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.up()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.down()

#challenge 3
# def makingShape(side, angle, color):
#     for _ in range(side):
#         timmy_the_turtle.color(color)
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)

# makingShape(3, 120, "red")
# makingShape(4, 90, "green")
# makingShape(5, 180-108, "blue")
# makingShape(6, 180-120, "purple")
# makingShape(7, 180-128.57, "black")
# makingShape(8, 180-135, "yellow")
# makingShape(9, 180-140, "orange")
# makingShape(10, 180-18*8, "black")


# #challenge 4

# color_options=["red", "green", "yellow", "blue"]

# def random_color():
#     r=random.randint(0, 255)
#     g=random.randint(0, 255)
#     b=random.randint(0, 255)
#     rand_color=(r, g, b)
#     return rand_color

# def generate_shape(width, length):
#     timmy_the_turtle.pensize(width)
#     timmy_the_turtle.speed(10)
#     i=0
#     while(i==0):
#         random_number = random.randint(0,3)
#         if random_number==0:
#             timmy_the_turtle.forward(length)
#             # timmy_the_turtle.color(random_color())
#             # timmy_the_turtle.pencolor(random_color())
#             # timmy_the_turtle.color((1, 3, 77))
#         elif random_number==1:
#             timmy_the_turtle.backward(length)
#             # timmy_the_turtle.color(random_color())
#         elif random_number==2:
#             timmy_the_turtle.right(90)
#             timmy_the_turtle.forward(length)
#             # timmy_the_turtle.color(random_color())
#         else:
#             timmy_the_turtle.left(90)
#             timmy_the_turtle.forward(length)
#             # timmy_the_turtle.color(random_color())
#generate_shape(7, 17)
# timmy_the_turtle.home()
timmy_the_turtle.speed(10)
def make_shape(radius, angle):
    while(angle<=360):
        previous_angle = angle
        angle+=20
        timmy_the_turtle.right(angle-previous_angle)
        timmy_the_turtle.color("red")
        timmy_the_turtle.circle(radius)


make_shape(100, 0)
screen = Screen()
screen.exitonclick()