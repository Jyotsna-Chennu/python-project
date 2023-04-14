from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.pos = position
        self.paddle = Turtle(shape='square')
        self.paddle.left(90)
        self.paddle.color('red')
        self.paddle.shapesize(stretch_wid=1.5, stretch_len=5)
        self.paddle.penup()
        self.paddle.goto(self.pos[0], self.pos[1])
        self.paddle.speed('fastest')


    def up(self):
        self.paddle.forward(20)

    def down(self):
        self.paddle.backward(20)

    def paddle_pos(self):
        return self.paddle.pos()
