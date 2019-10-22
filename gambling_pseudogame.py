'''
filename: gambling-pseudogame.py
purpose: store a score, play more and more
concepts:
    - module: random
    - lists[]
    - conditional 'elif' is so cute
user story:
    - greet user, ask for 2 numbers
    - display result
    - randomly select an operator from a list
    - keep score
'''
import random

stars = "*" * 3
operator_list = ["+","-","x","/"]
operator = random.choice(operator_list)
first_number = input("\nGimme a number! ")
second_number = input("\nGimme anudda number! ")

# valdation
if first_number.isdigit() and second_number.isdigit():
    first_number = int(first_number)
    second_number = int(second_number)
    # intended user path
    print(f"Your random equation 📝 {first_number} {operator} {second_number}")
    if operator > "+":
        outcome = first_number + second_number
    elif operator == "-":
        outcome = first_number - second_number
    elif operator == "x":
        outcome = first_number * second_number
    else:
        outcome = first_number / second_number
    print(f"Your computation results in {outcome} . . .\n Thank you for using personal computers! 💻🧠")
else:
    print("Please enter numbers... You know, like integers. Or digits. Or a thing that you can type but that doesn't fit into the Alphabet Song. Take it from the top, sunshine. 🙌☀️")
