import turtle


class Score:
    def __init__(self):
        self.score = 0
        turtle.hideturtle()
        turtle.penup()
        turtle.color('blue')
        turtle.goto(0, 270)
        turtle.write(arg=f"Score :{self.score}", font=('Arial', 16, 'normal'))

    def score_update(self):
        self.score += 1
        turtle.clear()
        turtle.write(arg=f"Score :{self.score}", font=('Arial', 16, 'normal'))

    def game_over(self):
        turtle.goto(0,0)
        turtle.write(arg='Game Over', align='center', font=('Arial', 16, 'normal'))
