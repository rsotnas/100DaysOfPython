# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Around%201%20-%20apple&url=worlds%2Ftutorial_en%2Faround1c.json

def whole():
    if front_is_clear():
        move()
        if object_here():
            take()
    else:
        turn_left()


whole()
while not at_goal():
    whole()
