from turtle import Turtle, position

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.goto(position)
