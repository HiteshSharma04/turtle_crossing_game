from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.color("gold")
        self.goto(-300,250)
        self.update()
        

    def update(self):
        self.clear()
        self.write(f"LEVEL : {self.level} ", align="center", font=("Courier",20,"bold"))

    def level_up(self):
        self.level += 1
        self.update()

    def over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER! \n AT LEVEL : {self.level}", align="center" , font=("Courier", 30, "bold"))