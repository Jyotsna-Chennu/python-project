from turtle import Turtle



class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.penup()
        self.left(90)
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.set_turtle_position()

    def up(self):
        self.forward(10)

    def set_turtle_position(self):
        #self.goto(0, -360)
        self.goto(0, 300)

