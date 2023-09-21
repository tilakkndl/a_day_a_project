from turtle import Turtle,Screen
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.paddle_position=position
        # turtle = Turtle()
        # screen = Screen()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(self.paddle_position)

      

    def go_up(self):

        new_y = self.ycor()+20
        
        self.goto(self.xcor(), new_y)

    def go_down(self):
        
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)