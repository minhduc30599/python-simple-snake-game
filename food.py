from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.refresh_location()

    def refresh_location(self):
        x_location = random.randint(-270, 270)
        y_location = random.randint(-270, 270)
        self.goto(x_location, y_location)
