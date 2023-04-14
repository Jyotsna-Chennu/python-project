from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
snake = Turtle()


class Snake:
    def __init__(self):
        self.part = None
        self.snake_parts = []
        self.head = None
        self.create_snake()

    def create_snake(self):
        for i in range(0, 3):
            self.part = Turtle(shape='circle')
            self.part.penup()
            self.part.goto(positions[i])
            self.part.color('red')
            self.snake_parts.append(self.part)
        self.head = self.snake_parts[0]
        self.head.color('blue')

    def move_forward(self):
        for part in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part - 1].xcor()
            new_y = self.snake_parts[part - 1].ycor()
            self.snake_parts[part].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def to_get_snake_cord(self):
        if self.head.xcor() >= 290 or self.head.xcor() <= -290 or self.head.ycor() >= 290 or self.head.ycor() <= -290:
            return True
        return False

    def snake_dist(self, my_food):
        return int(self.head.distance(my_food))

    def to_increase_size(self):
        self.part = Turtle(shape='circle')
        self.part.penup()
        self.part.goto(self.snake_parts[-1].position())
        self.part.color('red')
        self.snake_parts.append(self.part)

    def tail_collision(self):
        for i in self.snake_parts[1:]:
            if self.head.distance(i) < 15:
                return True
        return False
