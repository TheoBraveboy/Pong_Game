from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
speed = 0


game_is_on = True

# paddle input
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

#x = 400 , y = 300

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.movement()

    #ball bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    if ball.xcor() > 380:
        #want to reset the game and move opposite direction
        ball.reset()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

        #ball collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
        ball.speed(speed + 5)








screen.exitonclick()
