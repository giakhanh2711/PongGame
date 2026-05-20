from turtle import Turtle
import utils

FIXED_POSITION_L = (-20, utils.SCREEN_HEIGHT / 2 - 70)
FIXED_POSITION_R = (20, utils.SCREEN_HEIGHT / 2 - 70)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.penup()
        self.hideturtle()
        self.pencolor("white")

        self.update()

    def increase_score_l(self):
        self.score_l += 1
        self.update()

    def increase_score_r(self):
        self.score_r += 1
        self.update()

    def update(self):
        self.clear()
        self.goto(FIXED_POSITION_L)
        self.write(self.score_l, align="center", font=("Courier", 50, "bold"))
        self.goto(FIXED_POSITION_R)
        self.write(self.score_r, align="center", font=("Courier", 50, "bold"))