import turtle
import random
import time


wn = turtle.Screen()
wn.title("Catch the Ball Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)


paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)


ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(random.randint(-250, 250), 250)


score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 18, "normal"))

def go_left():
    x = paddle.xcor()
    if x > -250:
        x -= 40
    paddle.setx(x)

def go_right():
    x = paddle.xcor()
    if x < 250:
        x += 40
    paddle.setx(x)

wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Game loop
fall_speed = 0.05
while True:
    wn.update()
    
    # Move the ball down
    ball.sety(ball.ycor() - 4)

    # If ball goes off screen
    if ball.ycor() < -300:
        ball.goto(random.randint(-250, 250), 250)

    # Check for collision
    if (ball.ycor() < -230 and ball.ycor() > -250) and (abs(ball.xcor() - paddle.xcor()) < 50):
        score += 1
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Courier", 18, "normal"))
        ball.goto(random.randint(-250, 250), 250)

    time.sleep(fall_speed)
