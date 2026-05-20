from turtle import Turtle, Screen
import utils
import  time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=utils.SCREEN_WIDTH, height=utils.SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

utils.draw_divider()

paddle_r = Paddle((utils.SCREEN_WIDTH / 2 - 20, 0))
paddle_l = Paddle((-utils.SCREEN_WIDTH / 2 + 20, 0))

scoreboard = Scoreboard()

ball = Ball()

screen.listen()
screen.onkeypress(key="Up", fun=paddle_r.up)
screen.onkeypress(key="Down", fun=paddle_r.down)
screen.onkeypress(key="w", fun=paddle_l.up)
screen.onkeypress(key="s", fun=paddle_l.down)

# Fix on keeping key, still works

while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Check collide upper or bottom
    if ball.check_collide_horizontal():
        ball.bounce_y()

    # Check out of screen
    is_out_of_screen = ball.check_out_of_screen()
    if is_out_of_screen == -1:
        scoreboard.increase_score_r()
    elif is_out_of_screen == 1:
        scoreboard.increase_score_l()

    # Check collide paddle
    if ball.check_collide_paddle(paddle_r) or ball.check_collide_paddle(paddle_l):
        ball.bounce_x()

screen.exitonclick()