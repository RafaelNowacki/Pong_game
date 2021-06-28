from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

whate = 0.02


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(whate)
    ball.move()
    if ball.ycor() == 300 or ball.ycor() == -300:
        ball.bounce("wall")

    if ball.distance(r_paddle) < 50 and ball.xcor() == 320 or\
            ball.distance(l_paddle) < 50 and ball.xcor() == -320:
        ball.bounce("paddle")
        whate *= 0.2

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    elif ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

# screen.exitonclick()