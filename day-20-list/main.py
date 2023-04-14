from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score

# my screen code
my_scr = Screen()
my_scr.bgcolor('black')
my_scr.title('Snake Game')
my_scr.setup(600, 600)
my_scr.tracer(0)

# object creation for snake, food, score
snake = Snake()
food = Food()
score = Score()
# to make the screen listen
my_scr.listen()
my_scr.onkey(snake.up, "Up")
my_scr.onkey(snake.down, "Down")
my_scr.onkey(snake.left, "Left")
my_scr.onkey(snake.right, "Right")

# variable to start and stop the game
game_start = True

# start of the game
while game_start:
    if snake.to_get_snake_cord():
        score.game_over()
        game_start = False
    if snake.snake_dist(food) < 15:
        snake.to_increase_size()
        score.score_update()
        food.move_food()
    if snake.tail_collision():
        score.game_over()
        game_start = False
    my_scr.update()
    time.sleep(0.1)
    snake.move_forward()

# exit on click
my_scr.exitonclick()
