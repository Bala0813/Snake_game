from turtle import Turtle

class FoodScore(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.score_writer()

    def increase_score(self):
        self.snake_score += 1
        self.clear()
        self.score_writer()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", move=False, align="center", font=("arial", 30, "normal"))

    def score_writer(self):
        self.write(f"Score: {self.snake_score}", move=False, align="center", font=("arial", 30, "normal"))

