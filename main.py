from turtle import Screen
import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

WIDTH = 800
HEIGHT = 600


screen = Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"W")
screen.onkey(l_paddle.go_down,"S")
print(ball.xcor(),ball.ycor())

game_on=True
while game_on:
    time.sleep(ball.move_speed )
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320  and  ball.distance(r_paddle) < 50 or ball.xcor() < -320  and ball.distance(l_paddle) < 50 :
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

turtle.done()