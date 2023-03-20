from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(position)
        self.color("#8B0A50")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), y=new_y)
