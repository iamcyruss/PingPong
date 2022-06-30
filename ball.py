from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        #print(f"new_x - move_ball: {new_x}")
        #print(f"new_y - move_ball: {new_y}")
        self.goto(new_x, new_y)

    def bounce(self):
        #need to invert the xcor and ycor?
        self.y_move *= -1
        #print(f"---WTF---: {self.y_move}")

    def paddle_bounce(self):
        self.x_move *= -1

    def ball_reset(self):
        self.goto(0, 0)
        self.x_move *= -1
