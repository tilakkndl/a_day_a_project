from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self): 
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.score_board = f"Score: {self.score}"
        self.penup()
        self.setposition(0, 270)
        self.write(self.score_board, False, "center", ("Arial", 18, "normal"))

    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score}", False, "center", ("Arial", 18, "normal"))
        # self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over", False, "center", ("Arial", 18, "normal"))