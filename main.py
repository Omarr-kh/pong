import turtle
from paddle import Paddle
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

# Even listeners (controls)
screen.listen()
screen.onkeypress(paddle_1.up, 'w')
screen.onkeypress(paddle_1.down, 's')

screen.onkeypress(paddle_2.up, 'Up')
screen.onkeypress(paddle_2.down, 'Down')

while GAME_ON:
    screen.update()
    # time.sleep(0.1)

screen.exitonclick()
