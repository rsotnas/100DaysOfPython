# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Harvest%203&url=worlds%2Ftutorial_en%2Fharvest3.json

flag = True
change_line = False
count = 1
column = 1
while flag:
    if change_line:
        move()
        turn_left()
        if wall_in_front():
            turn_left()
            turn_left()
        count += 1
        change_line = False
    else:
        if wall_in_front():
            while not is_facing_north():
                turn_left()
            change_line = True
            column = 1
        else:
            if (count > 2 and count < 9) and (column > 2 and column < 9):
                while object_here():
                    take()
                put()
            column += 1
            move()
    if count == 9:
        flag = False
