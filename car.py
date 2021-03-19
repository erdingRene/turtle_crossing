from turtle import Turtle
import random


class Car(Turtle):

    def random_color(self):
        hex_number = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        return hex_number

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, random.randint(1, 5))
        self.penup()
        self.color(self.random_color(), self.random_color())
        self.setheading(180)
