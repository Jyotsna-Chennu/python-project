from turtle import Turtle, Screen

my_tur = Turtle()
my_scr = Screen()


def move_forward():
    my_tur.forward(20)


def move_backward():
    my_tur.backward(20)


def turn_left():
    my_tur.left(10)


def turn_right():
    my_tur.right(10)


def clear_scr():
    # my_scr.clearscreen()
    my_tur.reset()
    # my_scr.resetscreen()


# my_scr.delay(50)
my_scr.listen()
my_scr.onkey(key="w", fun=move_forward)
my_scr.onkey(key="s", fun=move_backward)
my_scr.onkey(key="a", fun=turn_left)
my_scr.onkey(key="d", fun=turn_right)
my_scr.onkey(key="c", fun=clear_scr)
my_scr.exitonclick()
