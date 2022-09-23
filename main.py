from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
turtle = Turtle()
screen.listen()
screen.onkey(l_paddle.move_up, 'Up')
screen.onkey(l_paddle.move_down, 'Down') 
screen.onkey(r_paddle.move_up, 'w')
screen.onkey(r_paddle.move_down, 's') 

game_on = True
while game_on:
    screen.update()




screen.exitonclick()