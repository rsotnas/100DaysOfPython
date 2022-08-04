# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Center%201&url=worlds%2Ftutorial_en%2Fcenter1.json

import math
flag = True
count = 1
while flag:
    if wall_in_front():
        turn_left()
        turn_left()
        steps = math.ceil(count/2)
        for i in range(steps-1):
            move()
        put()
        flag = False
    else:
        count += 1
        move()
