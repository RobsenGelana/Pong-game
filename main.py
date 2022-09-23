from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')

screen.tracer(0)

#Creating object for the paddle
l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))

#creating a ball object
ball = Ball()
#Listening for keyboard keys
screen.listen()
screen.onkey(l_paddle.move_up, 'Up')
screen.onkey(l_paddle.move_down, 'Down') 
screen.onkey(r_paddle.move_up, 'w')
screen.onkey(r_paddle.move_down, 's') 


#creating a while loop to update the screen
game_on = True
while game_on:
    #Slowing down the pace of the ball
    time.sleep(0.1)
    screen.update()
    ball.move()



screen.exitonclick()