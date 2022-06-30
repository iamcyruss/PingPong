from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, "normal")


#teachers solutions
class R_scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(200, 265)
        self.color("white")
        self.update_point()
        self.hideturtle()

    def update_point(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_point()

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.color("Yellow")
        self.write("Right Player WINS!", align=ALIGN, font=FONT)