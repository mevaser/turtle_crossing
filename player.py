STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.shape("turtle")
        self.turtle.penup()
        self.turtle.setheading(90)
        self.turtle.goto(STARTING_POSITION)

    def move(self):
        self.turtle.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.turtle.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.turtle.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
