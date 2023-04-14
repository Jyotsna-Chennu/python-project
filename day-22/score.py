from turtle import Turtle


class Score:
    def __init__(self):
        self.score = Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.color('white')
        self.score.point_r = 0
        self.score.point_l = 0

    def right(self, score):
        self.score.goto(170, 350)
        self.score.write(f'Score :{self.score.point_r}', font=('Arial', 16, 'normal'))

    def left(self, score):
        self.score.goto(-250, 350)
        self.score.write(f'Score :{self.score.point_l}', font=('Arial', 16, 'normal'))

    def update_right(self):
        self.score.clear()
        self.score.point_r += 1

        self.score.write(f'Score :{self.score.point_r}', font=('Arial', 16, 'normal'))

    def update_left(self):
        self.score.clear()
        self.score.point_l += 1
        self.score.goto(-250, 350)
        self.score.write(f'Score :{self.score.point_l}', font=('Arial', 16, 'normal'))


