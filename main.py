from turtle import Screen
from l_scoreboards import L_scoreboard
from r_scoreboard import R_scoreboard
from paddles import Paddles
from ball import Ball
import time

sleepy = 0.1
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_scoreboards = L_scoreboard()
r_scoreboard = R_scoreboard()

r_paddle = Paddles((350, 0))
l_paddle = Paddles((-350, 0))
ball = Ball()

screen.listen()

screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(sleepy)
    screen.update()
    ball.move_ball()

    if ball.ycor() >= 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()
        sleepy -= 0.01
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
        sleepy -= 0.01

    if ball.xcor() > 380:
        l_scoreboards.add_point()
        ball.ball_reset()
        sleepy -= 0.01
        if l_scoreboards.score == 10:
            l_scoreboards.game_over()
            game_is_on = False
    elif ball.xcor() < -380:
        r_scoreboard.add_point()
        ball.ball_reset()
        sleepy -= 0.01
        if r_scoreboard.score == 10:
            r_scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
