from turtle import Screen
from paddle import Paddle
from table import Table
from score_board import ScoreBoard
from ball import Ball
import time


#Create background
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("PONG GAME")
screen.tracer(0)

#Create paddle+Paddle move
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

score = Table()

score_board = ScoreBoard()

#Create Ball
ball = Ball()


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        ball.change_move_speed()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.go_to_start()
        ball.bounce_x()
        score_board.grow_score_l()

    #Detect L paddle misses
    if ball.xcor() < -380:
        ball.go_to_start()
        ball.bounce_x()
        score_board.grow_score_r()

screen.exitonclick()