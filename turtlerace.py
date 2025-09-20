from turtle import Turtle, Screen
import random

# for turtle_index in range(0,6):
#     timmy = Turtle(shape="turtle")
#     timmy.penup()
#     timmy.goto(-230, -100)

# timmy1=Turtle(shape="turtle")
# timmy2=Turtle(shape="turtle")
# timmy3=Turtle(shape="turtle")
# timmy4=Turtle(shape="turtle")
# timmy5=Turtle(shape="turtle")

screen=Screen()
screen.setup(500,400)
is_race_on=False
user_bet=screen.textinput(title="make your bet",prompt="chose a colour")
colors=["red","green","blue","orange","yellow","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)




if user_bet:
    is_race_on=True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"you won ! the {winning_color} turtle is the winner")
            else:
                print(f"you lost ! the {winning_color} turtle is the winner")


        random_d=random.randint(0,10)
        turtle.forward(random_d)














# timmy.penup()
# timmy.color("red")
# timmy1.penup()
# timmy1.color("green")
# timmy2.penup()
# timmy2.color("blue")
# timmy3.penup()
# timmy3.color("cyan")
# timmy4.penup()
# timmy4.color("grey")
# timmy5.penup()
# timmy5.color("beige")

# timmy.goto(-230,-100)

screen.exitonclick()