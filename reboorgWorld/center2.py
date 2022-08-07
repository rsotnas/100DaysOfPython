import math
flag1 = True
flag2 = True
count = 1
while flag1:
    if wall_in_front():
        turn_left()
        turn_left()
        steps = math.ceil(count/2)
        for i in range(steps-1):
            move()
        # put()
        flag1 = False
        while not is_facing_north():
            turn_left()
        count = 0
        while flag2:
            if wall_in_front():
                turn_left()
                turn_left()
                steps = math.ceil(count/2)
                for i in range(steps):
                    move()
                put()
                flag2 = False
            else:
                count += 1
                move()
    else:
        count += 1
        move()
