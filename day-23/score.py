from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.goto(-350, 350)
        self.hideturtle()
        self.write(f'Level :{self.level}', font=('Arial', 16, 'normal'))

    def game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write('Game Over', font=('Arial', 16, 'normal'))

    def level_incr(self):
        self.clear()
        self.write(f'Level :{self.level}', font=('Arial', 16, 'normal'))
