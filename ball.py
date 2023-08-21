import turtle
import time


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.ball_speed = 6
        self.xdirection = 1
        self.ydirection = 1
        self.create_ball()

    def create_ball(self):
        self.shape("square")
        self.penup()
        self.color("white")
        self.move()

    def move(self):
        self.goto(self.xcor() + (self.ball_speed * self.xdirection),
                  self.ycor() + (self.ball_speed * self.ydirection))
        time.sleep(0.05)
