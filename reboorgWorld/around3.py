# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Around%203&url=worlds%2Ftutorial_en%2Faround3.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_right()
    move()
    move()


def whole_movement():
    turn_left()
    move()
    jump()
    turn_right()
    move()


put()
flag = True
count = 1
whole_movement()
while flag:
    if wall_on_right() and not wall_in_front():
        if front_is_clear() and not wall_in_front():
            move()
        elif is_facing_north() and front_is_clear() and not wall_in_front():
            move()
    else:
        turn_left()
    if object_here() and not count:
        flag = False
    if count:
        count -= 1
    if not count and is_facing_north() and front_is_clear():
        move()
