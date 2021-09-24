from turtle import Turtle , Screen
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
SCREEN = Screen()
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.write(arg=f"Score : {self.score}", align= ALIGNMENT, font=FONT)
        self.hideturtle()


    def score_change(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score : {self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.home()


        self.write(arg="GAME OVER!", align=ALIGNMENT, font=("Arial", 14, "normal"))







