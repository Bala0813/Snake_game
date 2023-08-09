from turtle import Turtle

class FoodScore(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_score = 0
        self.high_score = 0
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
        with open("score.txt", "r") as score_sheet:
            self.high_score = int(score_sheet.read())
            dum = self.high_score
            if self.snake_score > dum:
                self.high_score = self.snake_score
                with open("score.txt", "w") as score_sheet:
                    score_sheet.write(str(self.high_score))
        self.write("Game Over!", move=False, align="center", font=("arial", 30, "normal"))

    def score_writer(self):
        with open("score.txt", "r") as score_sheet:
            self.high_score = score_sheet.read()
        self.write(f"High Score: {self.high_score}\n Score: {self.snake_score}", move=False, align="center", font=("arial", 30, "normal"))
