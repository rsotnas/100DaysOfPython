print("Welcome to the tip calculator.")
total = float(input('What was the total bill? $'))
percentage = float(
    input('What percentage tip would you like to give? 10, 12 or 15?'))
people = int(input("How many people to split the bill?"))
total_amount = ((total * (1 + percentage / 100)) / people)
total_amount_str = "{:.2f}".format(total_amount)
print(
    f"Each person should pay $ {total_amount_str}.")
