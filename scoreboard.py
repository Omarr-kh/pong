import turtle


class Score(turtle.Turtle):
    def __init__(self, player):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.show_score(player)

    def show_score(self, player):
        if player == 1:
            self.goto(-150, 270)
        elif player == 2:
            self.goto(150, 270)
        self.write(f"{self.score}", align="center",
                font=('Arial', 22, 'normal'))

    def update_score(self, player):
        self.score += 1
        self.clear()
        self.show_score(player)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center",
                font=('Arial', 18, 'normal'))