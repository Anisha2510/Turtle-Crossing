import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

COUNT = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
score = Scoreboard()

screen.onkey(player.move, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    random_chance = random.randint(1, 6)
    time.sleep(0.1)
    screen.update()
    if random_chance == 1:
        car_manager.create_car()
    COUNT += 1
    car_manager.move_forward()
    for car in car_manager.cars_list:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
    if player.ycor() == 280:
        player.move_to_start()
        score.incr_level()
        car_manager.level_up()

screen.exitonclick()
