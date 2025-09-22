from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")


screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()
paddle=Turtle()
# paddle.shape("square")
# paddle.color("White")
# paddle.shapesize(stretch_wid=5,stretch_len=1)
# paddle.penup()
# paddle.goto(350,0)
# def go_up():
#     new_y=paddle.ycor()+20
#     paddle.goto(paddle.xcor(),new_y)
# def go_down():
#     new_y=paddle.ycor()-20
#     paddle.goto(paddle.xcor(),new_y)


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect the collision when the ball is at 300 above then goint to pass the wall already hit the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_Y()
    # to detect collision with right paddle

    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_X()




    #detect when right paddle misses

    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()


    #detect when the left paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()










screen.exitonclick()

















