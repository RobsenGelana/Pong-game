from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')

screen.tracer(0)

#Creating object for the paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

#creating a ball object
ball = Ball()
#Listening for keyboard keys
screen.listen()
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down') 
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's') 

scoreboard = ScoreBoard()
#creating a while loop to update the screen
game_on = True
while game_on:
    #Slowing down the pace of the ball
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detecting ball collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y() 

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    if ball.xcor()  < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()