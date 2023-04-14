import turtle
from turtle import Screen,Turtle
from snake import Snake
from food import Food
from score import Score
# code for my screen to work
my_scr = Screen()
my_scr.title('Snake Game')
my_scr.setup(600, 600)
my_scr.delay(30)

# object creation for my snake,food
my_snake = Snake()
my_food = Food()
my_score = Score()
my_tur = Turtle()
my_tur.hideturtle()
# to make my snake to turn to the directions it should
my_scr.listen()
my_scr.onkey(my_snake.up, "Up")
my_scr.onkey(my_snake.down, "Down")
my_scr.onkey(my_snake.left, "Left")
my_scr.onkey(my_snake.right, "Right")

# parameter which decides when the game to stop
game_end = False

# start of the game
while not game_end:
    if my_snake.to_get_snake_cord():
        my_tur.write(arg="Game Over", align='center', font=('Arial', 16, 'normal'))
        game_end = True
    else:
        if my_snake.snake_dist(my_food) < 20:
            my_score.score_update()
            my_snake.to_increase_size()
            my_food.move_food()

        my_snake.to_move_forward()

my_scr.exitonclick()
