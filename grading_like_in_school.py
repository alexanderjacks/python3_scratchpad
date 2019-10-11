'''
filename: grading_like_in_school.py
purpose/MVP:
    - return a letter grade
user story:
    - greet user, ask for 2 numbers
concepts:
    - lists[]
    - problem solve on ranges
    - conditionals, elif vs else
    - = vs ==
grading rubric:
    95-100: A+
    90-94: A
    85-89: B+
    80-84: B
    75-79: C+
    70-74: C
    60-69: D
    0-59: F
'''

# optional sauce, not MVP feature
import random
rival_score = random.randint(60,100)

# MVP code
user_score = int(input("What was your score on that last exam? Be honest, I'm a computer and I don't do lies. "))
if 95 <= user_score <= 100:
    outcome = "A+"
elif 90 <= user_score <= 94:
    outcome = "A"
elif 85 <= user_score <= 89:
    outcome = "B+"
elif 80 <= user_score <= 84:
    outcome = "B"
elif 75 <= user_score <= 79:
    outcome = "C+"
elif 70 <= user_score <= 74:
    outcome = "C"
elif 60 <= user_score <= 69:
    outcome = "D"
else:
    outcome = "F"

print(f"You scored {user_score}.\nYour score alphabetizes to the letter grade {outcome}, for what it's worth.")

''' optional fun: comment out for MVP demo ⬇️
'''
if rival_score > user_score:
    print(f"Your rival scored {rival_score} and beat you! 🤓☠️")
elif rival_score == user_score:
    print(f"You scored exactly the same as your hated rival! You need to study more! 🤦‍")
else:
    print(f"Your rival scored {rival_score}, and needs to study more. 🎒📚")
