''' Lab 09: Make Change
Let the user enter how many pennies they have, and convert their pennies into larger coins and leftover pennies.

Version 1 ✔️
Convert the user's pennies into the maximum number of quarters. For example, if the user enters 136, break that 136 into quarters (5) and pennies (11).

Version 2 ✔️
Convert the user's pennies into the maximum number of quarters, then the maximum number of dimes, then the maximum number of nickels. Have the user enter the total number in pennies. For example, break 136 into quarters (5), dimes (1), nickles (0) and pennies (1).

Bonus Feature 1 ✔️
Have the user enter a dollar amount (1.36), convert this to the total in pennies, and proceed as before. Do this with float() and round().

Bonus Feature 2 Ⓧ
In a while loop, let the user add or subtract a dollar amount to the current coin value, and then convert the resulting value into the smallest number of coins possible.

>>> You have 5 quarters, 1 dimes, 0 nickles, 1 pennies
>>> Choose (add), (subtract), or (done) >subtract
>>> How much? >.37
>>> You have 3 quarters, 2 dimes, 0 nickles, 4 pennies
>>> Choose (add), (subtract), or (done) >done

Super Advanced Version 1 Ⓧ
Let the user add their own custom coins!

Hint: Use a list and sort
>>> def get_index_two(in_tuple):
... return in_tuple[2]
>>> student_tuples = [
... ('john', 'A', 15),
... ('jane', 'B', 12),
... ('dave', 'B', 10),
... ]
>>> sorted(student_tuples, key=get_index_two) # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
>>> sorted(student_tuples, key=get_index_two, reverse=True) # sort by age, reversed
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)
'''
print('''
++++++++++++++++++++++++++
| LET'S PLAY MAKE CHANGE |
| 🔪 💰 🔪 💰 🔪 💰 🔪   |
++++++++++++++++++++++++++
Please enter an amount in US dollars (don't type "$") and this script will tell you:
- how many quarters
- how many dimes
- how many nickels
- how many pennies
your amount totals.\n
It calculates the fewest number of coins, b/c no one likes pennies, even virtual ones.
''')
player_amount = input("How much do you want to make into change? Enter a dollar amount using number keys. If you don't add a decimal we'll just assume you're telling us how many pennies you have...  ")

if '.' in player_amount: # player inputs a decimal character, we have a str() type that oughta be a float()
    working_number = float(player_amount)
else: # they're entering the amount in pennies
    working_number = float(player_amount)/100 # converts player input into number, then into pennies 1/100th units

print(f"Thanks! You entered ${working_number}.")
working_number = working_number * 100 # to allow for dollar-based math, not penny-
quarters_number = int(working_number / 25)
working_number -= quarters_number * 25
dimes_number = int(working_number / 10)
working_number -= dimes_number * 10
nickels_number = int(working_number / 5)
working_number -= nickels_number * 5
remainder = int(working_number / 1)
print(f"That's {quarters_number} quarters")
print(f"... {dimes_number} dimes")
print(f"... {nickels_number} nickels")
print(f"and {remainder} pennies")
print("Thanks for playing! Hope you found this game programmatically interesting.")
