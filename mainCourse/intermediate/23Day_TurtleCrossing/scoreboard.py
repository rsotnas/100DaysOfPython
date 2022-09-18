from msilib.schema import Font
from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
  
  
  def __init__(self):
    super().__init__()
    self.level = 0
    self.hideturtle()
    self.penup()
    self.goto(-280, 250)
    self.increase_level()

  def increase_level(self):
    self.level += 1
    self.clear()
    self.write(f"Level: {self.level}", align="left", font=Font)

  def game_over(self):
    self.goto(0, 0)
    self.write(f"GAME OVER", align="center", font=Font)

