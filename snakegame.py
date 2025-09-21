from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food

import time
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()


screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    #detect the collision with food. using the distance coming from turtle()

    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

########detect collision with the wall.
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()

        #detect collision with the tail
    for segment in snake.segments:
        if segment==snake.head:#that is why we are going to consider a if statement
            pass
        elif snake.head.distance(segment) <10:
            game_is_on=False
            scoreboard.game_over()## if we run this now the game is going to show thw game over signal as the out of every segment the head is the first segment
        #if head collide with any segment in tail game over to do this we are going to loop through


















screen.exitonclick()