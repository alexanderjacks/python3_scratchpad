''' Lab 8: Guess_the_Number
Let's play 'Guess the Number':
- the computer will choose a random int between 1 and 10
- the user will then try to guess the number, and the program will tell them whether they're right or wrong

Advanced Features (optional learnings):
#1) Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.
#2) Keep track of how many guesses the user has made, and tell them at the end.
#3) Using a while loop, allow the user to guess 10 times; if they fail to guess the number after 10 tries, the user is told they've lost.
#4) Tell the user whether their current guess is closer than their last.
#9) Swap the user with the computer: the user will pick a number, and the computer will guess until they get it right.
'''
import random
game_on = True
lowest_possible_guess = 1
highest_possible_guess = 10
guessing_range = range(lowest_possible_guess, highest_possible_guess)
secret_number = random.choice(guessing_range)
while game_on == True:
    print(f"Welcome to Guess the Number! Please choose an integer from {lowest_possible_guess} to {highest_possible_guess}!")
    print(f"\nYou have infinite tries, so keep track of your guesses! ♺\nPsst... The secret number is:{secret_number}\n")
    user_guess = int(input(f"> > > Guess a number between {lowest_possible_guess} to {highest_possible_guess} ! ! ! ")) # gotta turn the input into integer
    if user_guess == secret_number:
        game_on = False
    else:
        game_on = True
        print("Not correct-- guess again! (Or hold down 'Ctrl' & type 'C' to quit.)")
else:
    print("You got it! Good game! 🏁")
