from turtle import Turtle
START = (0,-270)
FINISH = 250
STEP = 10

class T(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.start()
        self.setheading(90)
        self.shapesize(stretch_len=2,stretch_wid=2)
        
    def move(self):
        self.goto(self.xcor() , self.ycor() + STEP)

    def start(self):
        self.goto(START)

    def finish(self):
        if self.ycor() > FINISH:
            return True
        else:
            return False
