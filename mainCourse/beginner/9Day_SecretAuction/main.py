import os
import art

print(art.logo)
print("Welcome to the secret auction program.")

players = {}
other_players = True

while other_players:
  name = input("What is your name?: ")
  bid = input("What's your bid?: $")
  players[name] = float(bid)
  another = input("Are there any other bidders? Type 'yes' or 'no'.")
  if another == "no":
    other_players = False
  else:
    os.system('cls||clear')

os.system('cls||clear')
winner_name = ''
winner_value = 0.0
for key, value in players.items():
  if value > winner_value:
    winner_value = value
    winner_name = key
  

print(f"The highest value was offered by {winner_name}, which was ${winner_value}")