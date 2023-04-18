from turtle import Screen
from tim_tur import Timmy
from car_blocks import Blocks
import time
# screen specification
scr = Screen()
scr.setup(width=800, height=800)
scr.tracer(0)

# creating objects
tim = Timmy()
block = Blocks()
# to make the screen listen
scr.listen()
scr.onkeypress(key='Up', fun=tim.up)

game_play = True
while game_play:
    scr.update()
    time.sleep(0.1)
    block.move_blocks()
    if tim.ycor() >= 360:
        tim.set_turtle_position()
        block.move_speed *= 0.01
scr.exitonclick()
