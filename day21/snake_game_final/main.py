from turtle import Turtle, Screen
import time

from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detecting collision with food
    if(snake.head.distance(food))<15:
        food.refresh()
        score_board.increase_score()
        snake.extend()

    #Detecting collision with food
    if(snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280):
        game_is_on=False
        score_board.game_over()


    #Detecting collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            score_board.game_over()











screen.exitonclick()