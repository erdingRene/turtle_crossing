from turtle import Turtle


class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()

    def create_turtle(self):
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def create_text(self, text):
        self.color("black")
        self.hideturtle()
        self.penup()
        self.write(text, align="center", font=("Arial", 30, "normal"))

    def move_forward(self):
        self.forward(10)


