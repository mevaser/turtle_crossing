from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    # This class is responsible for keeping score and displaying the level.
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-380, 260)
        self.write(f"level: {self.level}", align="left", font=FONT)
        self.update_scoreboard()
    
    # update the level on the screen 
    def update_scoreboard(self):
        self.clear()
        self.write(f"level: {self.level}", align="left", font=FONT)
    
    # increase the level by 1   
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    # display game over message
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)