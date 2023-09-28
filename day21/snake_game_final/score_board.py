from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self): 
        super().__init__()
        self.score = 0
        with open("/media/tilakkndl/New Volume/py/Days/day21/snake_game_final/score.txt") as f:
            self.high_score=int(f.read())
        self.color("white")
        self.hideturtle()
        self.score_board = f"Score: {self.score} High Score: {self.high_score}"
        self.penup()
        self.setposition(0, 270)
        self.write(self.score_board, False, "center", ("Arial", 18, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ("Arial", 18, "normal"))
        # self.update()

    def increase_scoreboard(self):
         self.score+=1
         self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game over", False, "center", ("Arial", 18, "normal"))

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("/media/tilakkndl/New Volume/py/Days/day21/snake_game_final/score.txt", "w") as f:
                f.write(f"{self.score}")
        self.score=0
        self.update_scoreboard()