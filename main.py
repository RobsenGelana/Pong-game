from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle = Paddle()
turtle = Turtle()
screen.listen()
screen.onkey(paddle.move_up, 'Up')
screen.onkey(paddle.move_down, 'Down') 

game_on = True
while game_on:
    screen.update()




screen.exitonclick()