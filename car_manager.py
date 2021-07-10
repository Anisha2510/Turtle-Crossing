from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        car.setheading(180)
        car.penup()
        position = random.randint(-240, 240)
        car.goto(280, position)
        self.cars_list.append(car)

    def move_forward(self):
        for car in range(len(self.cars_list)):
            self.cars_list[car].forward(self.car_speed)
            # self.cars_list[car].speed(0.1)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
