from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
my_scr = Screen()
my_scr.bgcolor('black')
my_scr.title('Welcome to Pong Game')
my_scr.setup(width=800, height=800)

# creating objects
right = Paddle((350, 0))
left = Paddle((-350, 0))
ball = Ball()
score_right = Score()
score_left = Score()
score_right.right(-1)
score_left.left(-1)
# my screen related code
my_scr.tracer(0)
my_scr.listen()
my_scr.onkeypress(key='Up', fun=right.up)
my_scr.onkeypress(key='Down', fun=right.down)
my_scr.onkeypress(key='n', fun=left.up)
my_scr.onkeypress(key='m', fun=left.down)

# variable to initialize the game
game_play = True

# start the game
while game_play:
    ball.move()
    time.sleep(ball.move_speed)
    my_scr.update()
    if ball.on_hit_boundaries():
        ball.bounce_y()
    point_1 = ball.collision_paddle(right.paddle_pos())
    point_2 = ball.collision_paddle(left.paddle_pos())
    if point_2 == 'r' or point_1 == 'r':
        score_right.update_right()
    elif point_2 == 'l' or point_1 == 'l':
        score_left.update_left()


my_scr.exitonclick()
