from turtle import Turtle

class Table(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(0, 0)
        self.color("#8B0A50")
        self.shapesize(stretch_wid=80, stretch_len=0.1)

