import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(player.move, "Up")



game_is_on = True
while game_is_on:
    counter = 0
    time.sleep(0.1)
    screen.update()
    if counter % 10 == 0:
        car_manager.create_car()
    counter += 1
    car_manager.move_cars()
    
    if car_manager.all_cars:  # Make sure the list isn't empty
        random.choice(car_manager.all_cars).forward(car_manager.car_speed)
