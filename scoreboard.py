
from turtle import Turtle

FONT = ("Courier New", 15, "bold")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        with open("data.txt", mode="r") as file:
            self.highest_score = int(file.read())
        self.score = 0
        self.position()
        self.color("white")
        self.penup()
        self.show_counter()


    def update_scoreboard(self):
        self.score += 1
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highest_score))
        self.show_counter()

    def position(self):
        self.goto(0, 275)

    def show_counter(self):
        self.clear()
        self.write(arg=f"Score = {self.score} Highest score = {self.highest_score}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.score = 0
        self.show_counter()







