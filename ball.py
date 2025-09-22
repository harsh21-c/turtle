from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.X_move=10
        self.Y_move=10
        self.move_speed=0.1
        

    def move(self):
        new_x=self.xcor()+self.X_move
        new_y=self.ycor()+self.Y_move
        self.goto(new_x,new_y)

    def bounce_Y(self):
        self.Y_move *= -1


    def bounce_X(self):
        self.X_move*=-1
        self.move_speed*=0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_X()