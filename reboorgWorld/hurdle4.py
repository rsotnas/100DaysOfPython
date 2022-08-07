# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    flag = True
    # UP
    while flag:
        if wall_in_front():
            while not is_facing_north():
                turn_left()
            if not wall_in_front():
                move()
                turn_right()
        else:
            flag = False
            move()

    # DOWN
    flag = True
    turn_right()
    while flag:
        while not wall_in_front():
            move()
        turn_left()
        flag = False


def whole_movement():
    if wall_in_front():
        jump()
    else:
        move()


while not at_goal():
    whole_movement()
