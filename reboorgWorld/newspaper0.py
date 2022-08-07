# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Newspaper%200&url=worlds%2Ftutorial_en%2Fnewspaper0.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()


flag = True
count = 0
while flag:
    if object_here():
        take()
    if front_is_clear():
        count += 1
        move()
    else:
        if is_facing_north():
            turn_right()
        else:
            turn_left()

    if count == 9:
        flag = False
        put()
turn_left()
turn_left()
flag = True
count = 0
while flag:

    if front_is_clear():
        count += 1
        move()
    else:
        if count % 3:
            turn_left()
        else:
            turn_right()
    if count == 9:
        flag = False
