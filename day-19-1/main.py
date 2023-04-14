from turtle import Turtle, Screen
from random import randint

my_scr = Screen()
my_scr.setup(500, 500)
user_choice = my_scr.textinput(title='On which color turtle would like ti bet on?',
                               prompt='Which turtle do you think will win the race? Enter a color')
colors = ['red', 'yellow', 'green', 'blue', 'pink', 'orange']
my_turtles = []

y_axis = -190
for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, y_axis)
    y_axis += 60
    my_turtles.append(new_turtle)

start_rase = False
if user_choice:
    start_rase = True

while start_rase:
    for turtle in my_turtles:
        distance = randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() >= 250:
            winner = turtle.color()
            start_rase = False
            break

        # if turtle.xcor() > 250:
        #     winner = turtle.color()
        #     start_rase = False
        #     break
        # else:
        #     distance = randint(0, 10)
        #     turtle.forward(distance)
if user_choice == winner:
    print("Yu Win")
else:
    print("You loose")

my_scr.exitonclick()
