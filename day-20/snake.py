from turtle import Turtle

my_snake = Turtle(shape='square')
my_snake.color('black')
length_snake = 10.0
my_snake.shapesize(stretch_len=length_snake)
my_snake.penup()


class Snake:
    def to_move_forward(self):
        my_snake.forward(10)

    def turn_left(self):
        my_snake.left(90)

    def turn_right(self):
        my_snake.right(90)

    def to_get_snake_cord(self):
        if my_snake.xcor() >= 290 or my_snake.xcor() <= -290 or my_snake.ycor() >= 290 or my_snake.ycor() <= -290:
            return True
        return False

    def up(self):
        if my_snake.heading() != 270:
            my_snake.setheading(90)

    def down(self):
        if my_snake.heading() != 90:
            my_snake.setheading(270)

    def left(self):
        if my_snake.heading() != 0:
            my_snake.setheading(180)

    def right(self):
        if my_snake.heading() != 180:
            my_snake.setheading(0)

    def snake_dist(self, my_food):
        return int(my_snake.distance(my_food))

    def to_increase_size(self):
        self.length = my_snake.shapesize()[1]
        my_snake.shapesize(stretch_len=self.length + 1)
