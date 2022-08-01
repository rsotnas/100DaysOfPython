import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


options = [rock, paper, scissors]

your_choice = int(input(
    'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
if your_choice > 2:
    print('You selected a wrong option, you lose!')
else:
    print(options[your_choice])
    print('Computer chose:')
    computer_choice = random.randint(0, 2)
    print(options[computer_choice])
    if (your_choice == computer_choice):
        print('Draw')
    elif (your_choice == 0 and computer_choice == 2):
        print('You won')
    elif (your_choice == 2 and computer_choice == 0):
        print('You lose')
    elif your_choice > computer_choice:
        print("You won")
    else:
        print('You lose')
