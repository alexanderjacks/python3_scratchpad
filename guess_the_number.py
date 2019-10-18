''' Lab 8: Guess_the_Number
Let's play 'Guess the Number':
- the computer will choose a random int between 1 and 10
- the user will then try to guess the number, and the program will tell them whether they're right or wrong

Advanced Features (optional learnings):
#☑️) Keep track of how many guesses the user has made, and tell them at the end.
#☑️) Using a while loop, allow the user to guess 10 times; if they fail to guess the number after 10 tries, the user is told they've lost.
#☑️) Tell the user whether their current guess is closer than their last.
#❌) Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.
#❌) Swap the user with the computer: the user will pick a number, and the computer will guess until they get it right.
'''
import random
game_on = True
# 📝 all the game parameters are vars so they can easily become input()s
lowest_possible_guess = 1
highest_possible_guess = 10
guessing_range = range(lowest_possible_guess, highest_possible_guess)
secret_number = random.choice(guessing_range)
max_allowed_guesses = 10
number_of_times_player_guesses = 0
last_rounds_guess = 0 # optional feature for sending absolute value clues to player
print(f"Welcome to Guess the Number! Please choose an integer from {lowest_possible_guess} to {highest_possible_guess}!")
while game_on == True and number_of_times_player_guesses < max_allowed_guesses:
    print(f"\nYou have {max_allowed_guesses - number_of_times_player_guesses} guesses left, good luck!")
    # print(f"\nPsst... The secret number is:{secret_number}\n") <-- dev mode
    this_player_guess = int(input(f"> > > Guess a number between {lowest_possible_guess} to {highest_possible_guess} ! ! ! ")) # gotta turn the input into integer
    number_of_times_player_guesses += 1
    if this_player_guess == secret_number:
        game_on = False
    else:
        game_on = True
        print(f"😼 You just guessed {this_player_guess}.\nIt's not correct-- guess again! (Or hold down 'Ctrl' & type 'C' to quit.)")
        print(f"We will remember that you guessed {this_player_guess} and give you a clue next time!")
        if (last_rounds_guess == 0): # condition of 1st guess
            print("🛣 That's a great first guess!")
        elif (abs(last_rounds_guess - secret_number) > abs(this_player_guess - secret_number)):
            print("😺 That guess was closer to the secret number than last time!")
        # elif (abs(last_rounds_guess - secret_number) == abs(this_player_guess - secret_number)):
        #     print("⚖️ That guess was just as far from the secret number as your last guess!\n👻 Can you win with your next guess???") # trying to warn player when they've found a guess exactly as far from secret# as last guess. How could this logic work; am I way off???
        else:
            print("🙀 That guess was even farther from the secret number than your last guess!")
        last_rounds_guess = this_player_guess
else:
    if game_on == False:
        print(f"😹 You won in only {number_of_times_player_guesses} guesses!\nGood game! 🏁")
    else:
        print(f"You guessed {number_of_times_player_guesses} times and never guessed {secret_number}!\nFascinating! 👾")
