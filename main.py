import turtle
from paddle import Paddle
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
    if ball.xcor() < -390 or ball.xcor() > 383:
        GAME_ON = False

    # collisions with paddle
    if (ball.xcor() < paddle_1.xcor() + 30 and paddle_1.ycor() + 60 > ball.ycor() > paddle_1.ycor() - 60) or (ball.xcor() > paddle_2.xcor() - 30 and paddle_2.ycor() + 60 > ball.ycor() > paddle_2.ycor() - 60):
        ball.xdirection *= -1
        ball.ball_speed += 0.7

    # collision with celing and floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ydirection *= -1


screen.exitonclick()
