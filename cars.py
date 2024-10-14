from turtle import Turtle
import random

START = 5
STEPS = 10
COLORS = ["red", "blue", "brown", "gold", "silver", "pink", "violet"]
class Cars():
    def __init__(self):
        self.speed = START
        self.all = []
        
    def new(self):
        ran = random.randint(1,6)
        if ran == 6:

            new1 = Turtle("square")
            new1.shapesize(stretch_len=2,stretch_wid=1)
            new1.penup()
            new1.color(random.choice(COLORS))
            y1 = random.randint(-220,220)
            new1.goto(500,y1)
            self.all.append(new1)

    def move(self):
        for i in self.all:
            i.backward(self.speed)

    def level_up(self):
        self.speed += START