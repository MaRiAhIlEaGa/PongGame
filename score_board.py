from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("#8B0A50")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-95, 220)
        self.write(f"{self.l_score}", font=("Arial", 50, "normal"))
        self.goto(40, 220)
        self.write(f"{self.r_score}", font=("Arial", 50, "normal"))

    def grow_score_l(self):
        self.l_score += 1
        self.update_scoreboard()

    def grow_score_r(self):
        self.r_score += 1
        self.update_scoreboard()