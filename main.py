import turtle
from paddle import Paddle
from scoreboard import Score
from ball import Ball
import time

# Screen settings
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# middle line
line = turtle.Turtle()
line.color("white")
line.pensize(3)
line.hideturtle()
line.penup()
line.goto(0, 290)
line.setheading(270)
line.pendown()
for i in range(15):
    line.forward(20)
    line.penup()
    line.forward(20)
    line.pendown()


# Variables
GAME_ON = True
paddle_1 = Paddle()
paddle_1.create_paddle(1)
paddle_2 = Paddle()
paddle_2.create_paddle(2)
ball = Ball()
score_1 = Score(1)
score_2 = Score(2)

# Even listeners (controls)
screen.listen()
screen.onkeypress(paddle_1.up, 'w')
screen.onkeypress(paddle_1.down, 's')

screen.onkeypress(paddle_2.up, 'Up')
screen.onkeypress(paddle_2.down, 'Down')

while GAME_ON:
    screen.update()
    ball.move()
    # collisions with walls
    if ball.xcor() < -390:
        ball.reset_ball(1)
        score_2.update_score(2)
    if ball.xcor() > 383:
        # GAME_ON = False
        ball.reset_ball(2)
        score_1.update_score(1)

    # collisions with paddle
    if (ball.distance(paddle_1) < 50 and ball.xcor() < -350) or (ball.distance(paddle_2) < 50 and ball.xcor() > 350):
        ball.xdirection *= -1
        ball.ball_speed += 0.8

    # collision with celing and floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ydirection *= -1


screen.exitonclick()
