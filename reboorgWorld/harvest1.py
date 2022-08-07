# https: // reeborg.ca/reeborg.html?lang = en & mode = python & menu = worlds % 2Fmenus % 2Freeborg_intro_en.json & name = Harvest % 201 & url = worlds % 2Ftutorial_en % 2Fharvest1.json

flag = True
change_line = False
count = 1
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
        else:
            if object_here():
                take()
            move()
    if count == 10:
        while not wall_in_front():
            if object_here():
                take()
            move()
        flag = False
