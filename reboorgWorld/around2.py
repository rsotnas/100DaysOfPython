# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Around%202&url=worlds%2Ftutorial_en%2Faround2.json

put()
move()
while not object_here():
    if front_is_clear() and wall_on_right():
        move()
    elif is_facing_north() and front_is_clear():
        move()
    else:
        turn_left()
