from turtle import Turtle
import turtle

class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=350, y=0)
    
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)