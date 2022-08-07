# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

import random


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def whole_movement(_move):
    if front_is_clear():
        move()
    else:
        if _move == 'left':
            turn_left()
        else:
            turn_right()


while not at_goal():
    choices = ['left', 'right']
    _move = random.choice(choices)
    whole_movement(_move)
