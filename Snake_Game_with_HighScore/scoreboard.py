from turtle import Turtle
from typing import TextIO

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
file = open("data.txt", "w")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            contents = data.read()
            if contents == "":
                self.high_score = 0
            else:
                self.high_score = int(contents)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
