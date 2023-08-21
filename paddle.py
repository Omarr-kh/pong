import turtle

class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1.2, stretch_wid=5)

    def create_paddle(self, player):
        if player == 1:
            self.goto(-380, 0)
        elif player == 2:
            self.goto(373, 0)

    def up(self):
        if self.ycor() < 242:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)
