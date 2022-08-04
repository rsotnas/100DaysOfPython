# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Home%204&url=worlds%2Ftutorial_en%2Fhome4.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def walk():
    move()
    move()
    move()


def cross():
    turn_right()
    move()
    turn_right()


def whole():
    walk()
    turn_left()
    walk()
    cross()


for i in range(3):
    whole()
walk()
turn_left()
walk()
