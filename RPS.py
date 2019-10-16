''' 🏔📋✂️ Lab 6: Let's play rock-paper-scissors with the computer!!!
☑ The computer will ask the user for their choice (rock, paper, scissors)
☑ The computer will randomly choose rock, paper or scissors
☑ Determine who won and tell the user
> Let's list all the cases:
    rock vs rock (tie)
    rock vs paper
    rock vs scissors
    paper vs rock
    paper vs paper (tie)
    paper vs scissors
    scissors vs rock
    scissors vs paper
    scissors vs scissors (tie)
☑ Advanced Version 1
    Catch all tie conditions using a *single if conditional*.
☑ Advanced Version 2
    Ask the user if they want to play again, using a while loop.
☑ Extra Sauce
    Keeps score
_ Advanced Version 3
    Use a dictionary where each key is one of the choices, and the value associated with the key is a list containing the two other choices.
'''
'''
Alex Jacks (j4cks)
Software Features:
    Plays Rock-Paper-Scissors in the terminal.
    Displays results (declares winner).
    Asks if human wishes to play again.
Code Mechanics:
    if
    advanced.feature(if optimization)
    advanced.feature(while loop, boolean as event toggle)
    advanced.feature(dictionary, keys (to set up all results?))
Fun fact:
    Janken is Rock-Paper-Scissors in Japan. It's exactly the same but vastly more common!
'''
import random
moves = ["🏔","📋","✂️"]
game_on = True
player_score = 0
python_score = 0

while game_on == True:
    print("Let's play Rock-Paper-Scissors! 🏔📋✂️\nHere's your input code:\n1 or 'R' or 'r' for ROCK 🏔 \n3 or 'P' or 'p' for PAPER 📋 \n5 or 'S' or 's' for SCISSORS ✂️ \n")

    player_choice = input("Choose your move. . .\n(　｀_ゝ´)  ").lower()
    if player_choice in ["r", "1"]:
        player_move = "🏔"
    elif player_choice in ["p", "3"]:
        player_move = "📋"
    elif player_choice in ["s", "5"]:
        player_move = "✂️"
    else:
        print("You gave a weird input. Please run this script again! (↑ , ⏎ )")
        break

    python_move = random.choice(moves) # more dramatic to have script choose after player, seems rigged otherwise

    result_is = "It looks like a DRAW ಠ_ಠ"

    if player_move == python_move: # refactored all 3 ties into 1 condition
        result_is = result_is
    elif player_move == "🏔" and python_move == "✂️":
        result_is = "Player wins!"
        player_score += 1
    elif player_move == "✂️" and python_move == "🏔":
        result_is = "Computer wins!"
        python_score +=1
    elif player_move == "✂️" and python_move == "📋":
        result_is = "Player wins!"
        player_score += 1
    elif player_move == "📋" and python_move == "✂️":
        result_is = "Computer wins!"
        python_score +=1
    elif player_move == "🏔" and python_move == "📋":
        result_is = "Computer wins!"
        python_score +=1
    else: # player_move == "📋" and python_move == "🏔":
        result_is = "Player wins!"
        player_score += 1

    print(f"\nYou chose {player_move}")
    print(f"Computer randomly selected {python_move}")
    print(result_is)
    if input("\nWould you like to play again???\nType 'y', 'Y', 'YES', 'Yes', 'yEs', 'yES', 'yeS', 'YEs' or 'yes'\nto play again. . . ").lower() in ["y","yes"]:
        game_on = True
        print(f"\nCurrent score is:\nPlayer: {player_score} > vs < Computer: {python_score}\n")
    else:
        game_on = False
else:
    print("Thanks for playing against a computer opponent!")
    print(f"\nF I N A L  S C O R E --> \nPlayer: {player_score}\nComputer: {python_score}\n")
    if player_score > python_score:
        print("Great job defeating a computer! 👾")
    else:
        print("Guess today will be lucky for you in other ways! ☘️")
