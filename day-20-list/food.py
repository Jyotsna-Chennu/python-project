from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.speed('fastest')
        self.move_food()

    def move_food(self):
        x = randint(-260, 260)
        y = randint(-260, 260)
        self.goto(x, y)
