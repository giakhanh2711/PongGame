from turtle import Turtle
import utils


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)
        self.x = self.xcor()

    def up(self):
        self.goto(self.x, utils.PADDLE_MOVE_LENGTH + self.ycor())

    def down(self):
        self.goto(self.x, self.ycor() - utils.PADDLE_MOVE_LENGTH)