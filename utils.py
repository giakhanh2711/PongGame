from turtle import Turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DASHED_LINE_DISTANCE = 20
DASHED_LINE_LENGTH = 60

PADDLE_MOVE_LENGTH = 30

BALL_STEP = 10

def draw_divider():
    t = Turtle(shape="square")
    t.color("white")
    t.pensize(width=10)
    t.hideturtle()
    t.penup()
    t.goto(0, -SCREEN_WIDTH / 2 + 20)
    t.setheading(90)

    for i in range(10):
        t.pendown()
        t.forward(DASHED_LINE_LENGTH)
        t.penup()
        t.forward(DASHED_LINE_DISTANCE)
