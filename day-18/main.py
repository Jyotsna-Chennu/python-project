from turtle import Turtle, Screen

my_turtle = Turtle()
my_screen = Screen()

my_turtle.shape('arrow')
my_turtle.color('green')
my_screen.delay(100)
number_of_turns = 15
# while number_of_turns != 0:
#     my_turtle.forward(100)
#     my_turtle.right(90)
#     number_of_turns -= 1
while number_of_turns != 0:
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()
    number_of_turns -= 1




my_screen.exitonclick()
