from turtle import Screen
from tim_tur import Timmy
from car_blocks import Blocks
from score import Score
import time
# screen specification
scr = Screen()
scr.setup(width=800, height=800)
scr.tracer(0)

# creating objects
tim = Timmy()
block = Blocks()
score = Score()
# to make the screen listen
scr.listen()
scr.onkeypress(key='Up', fun=tim.up)

game_play = True
while game_play:
    scr.update()
    time.sleep(0.1)
    block = Blocks()
    block.move_blocks()
    if tim.ycor() >= 360:
        tim.set_turtle_position()
        score.level += 1
        block.move_speed *= 0.01
    if tim.distance(block) < 50:
        score.game_over()
        game_play = False
scr.exitonclick()
