# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Rain%200&url=worlds%2Ftutorial_en%2Frain0.json

count = 0
flag = True
while flag:

    if front_is_clear():
        count += 1
        move()
    if count == 6:
        flag = False
        # put()
        build_wall()

turn_left()
turn_left()

for _ in range(5):
    move()
