from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "yellow", "purple", "orange", "black"]
names = ["Tim", "Tom", "Bob", "Mars", "kiwi"]
speeds = ["fastest", "fast", "normal", "slow", "slowest"]

turtle_racers = []



def play_race():
    x = -230
    y = -100

    for turtle_index in range(0, 6):
        new_turtle = Turtle()
        new_turtle.shape("turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x, y)
        y += 50
        turtle_racers.append(new_turtle)
        # generate_speed = new_turtle.speed(random.randint(0,10))

    is_on = True

    while is_on:

        for turtle in turtle_racers:
            win_color = turtle.pencolor()
            if turtle.xcor() > 50:
                is_on = False
                if user_bet == win_color:
                    screen.textinput(title="Race results", prompt="You won!")
                else:
                    screen.textinput(title="Race results", prompt="You lost!")
            ran_distance = random.randint(0,10)
            ran_speed = turtle.speed(random.randint(0,10))
            turtle.forward(ran_distance)









play_race()

print(turtle_racers)
screen.exitonclick()
