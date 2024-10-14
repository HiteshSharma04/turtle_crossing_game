from turtle import Turtle, Screen
from tort import T
from cars import Cars
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.title("TURTLE CROSS")
screen.tracer(0)
screen.listen()


t = T()
cars = Cars()
score = Score()

screen.onkey(t.move, "Up")

game = True
while game:
    time.sleep(0.1)
    screen.update()

    cars.new()
    cars.move()

    for i in cars.all:
        if i.distance(t) < 30:
            game = False
            score.over()
    
    if t.finish():
        t.start()
        cars.level_up()
        score.level_up()

screen.exitonclick()