import turtle
import random
import time

# Screen setup
wn = turtle.Screen()
wn.title("Dodge the Falling Balls")
wn.bgcolor("lightblue")
wn.setup(width=600, height=600)
wn.tracer(0)

# Player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(0, -250)
player.speed(0)

# Score
score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Falling balls
balls = []

for _ in range(5):
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("red")
    ball.penup()
    ball.speed(0)
    ball.goto(random.randint(-290, 290), random.randint(100, 400))
    balls.append(ball)

# Move functions
def move_left():
    x = player.xcor()
    x -= 20
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    if x > 280:
        x = 280
    player.setx(x)

wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")

# Main game loop
while True:
    wn.update()
    time.sleep(0.05)
    score += 1
    pen.clear()
    pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    for ball in balls:
        y = ball.ycor()
        y -= 10
        ball.sety(y)

        # Reset ball if it falls below
        if y < -300:
            ball.goto(random.randint(-290, 290), random.randint(300, 400))

        # Collision check
        if player.distance(ball) < 20:
            pen.clear()
            pen.write(f"Game Over! Final Score: {score}", align="center", font=("Courier", 24, "normal"))
            time.sleep(2)
            wn.bye()
