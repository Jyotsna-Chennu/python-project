from turtle import Turtle
from random import randint, choice

COLORS =['red', 'yellow', 'green', 'blue', 'pink']
class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.setheading(180)
        self.goto(370, randint(-350, 350))
        self.shapesize(stretch_len=3.5)
        self.color(choice(COLORS))
        self.move_speed = 0.1

    def move_blocks(self):
        self.forward(5)