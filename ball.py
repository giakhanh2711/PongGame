from turtle import Turtle
import random
import utils

OFFSET_COLLIDE = 5
SCALE_MOVE_SPEED = 0.9

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.color("white")
        self.xmove = utils.BALL_STEP
        self.ymove = utils.BALL_STEP
        self.move_speed = 0.1


    def move(self):
        self.goto(self.xcor() + self.xmove, self.ycor() + self.ymove)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self): # Use when colliding paddle
        self.xmove *= -1
        self.move_speed *= SCALE_MOVE_SPEED

    def check_collide_horizontal(self):
        if abs(self.ycor() - (-utils.SCREEN_HEIGHT / 2)) <= OFFSET_COLLIDE or \
            abs(self.ycor() - utils.SCREEN_HEIGHT / 2) <= OFFSET_COLLIDE:
            return True
        return False


    def check_collide_paddle(self, paddle):
        return abs(self.xcor() - paddle.xcor()) <= 21 and abs(self.ycor() - paddle.ycor()) <= 50


    def check_out_of_screen(self):
        if abs(self.xcor() - (-utils.SCREEN_WIDTH / 2)) <= OFFSET_COLLIDE or \
            abs(self.xcor() - (utils.SCREEN_WIDTH / 2)) <= OFFSET_COLLIDE:
            self.reset_position()
            return -1 if self.xcor() < 0 else 1
        return False

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1

