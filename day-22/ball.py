from turtle import Turtle
from score import Score
score = Score()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball = Turtle(shape='circle')
        self.ball.color('white')
        self.ball.goto(0,0)
        self.ball.shapesize(stretch_wid=1.8)
        self.ball.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1
       # self.speed('fastest')
        #self.ball.speed('slowest')
        #self.ball.goto(350, 350)

    def move(self):
        new_x = self.ball.xcor() + self.move_x
        new_y = self.ball.ycor() + self.move_y
        self.ball.goto(new_x, new_y)

    def on_hit_boundaries(self):
        if self.ball.ycor() >= 350 or self.ball.ycor() <= -350:
            return True
            # self.move_reverse()
        return False

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
        #self.move_speed *= 0.00001

    def collision_paddle(self, paddle):
        if self.ball.distance(paddle) < 60 and (self.ball.xcor() < -300 or self.ball.xcor() > 300):
            self.bounce_x()
        elif self.ball.xcor() > 350:
            self.ball.goto(0, 0)
            #self.move_speed = 0.1
            self.bounce_x()
            #self.move_speed = 0.1
            return 'l'
        elif self.ball.xcor() < -350:
            self.ball.goto(0, 0)
            #self.move_speed = 0.1
            self.bounce_x()
            #self.move_speed = 0.1
            return 'r'
        return -1


