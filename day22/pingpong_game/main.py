from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

right_paddle = Paddle((350, 0))
left_paddle=Paddle((-350,0))
ball = Ball()
score_board = ScoreBoard()


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PingPong Game")
screen.tracer(0)

screen.listen()

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detecting the collision on the top and bottom of the screen
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #Detecting the collisions with the paddle
    if ball.distance(right_paddle) <50 and ball.xcor()>320 or ball.distance(left_paddle)< 50 and ball.xcor()<-320:
        ball.bounce_x()


    #Detecting R paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        score_board.l_increase()
    
    #Detecting L paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        score_board.r_increase()