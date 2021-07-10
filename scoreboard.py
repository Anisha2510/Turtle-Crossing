from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.goto(-260, 260)
        self.hideturtle()
        self.level = 0
        self.display_level()

    def display_level(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def incr_level(self):
        self.level += 1
        self.clear()
        self.display_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
