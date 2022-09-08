import colorgram
import turtle
import random


colors = colorgram.extract("image.jpg", 30)

rgb_colors = []
for color in colors:
  r = color.rgb.r
  g = color.rgb.g
  b = color.rgb.b
  rgb_colors.append((r,g,b))


number_of_dots = 100

turtle.colormode(255)
tim = turtle.Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dot_count in range(1, number_of_dots + 1):
  tim.dot(20, random.choice(rgb_colors))
  tim.forward(50)

  if dot_count % 10 == 0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.setheading(500)
    tim.setheading(0)