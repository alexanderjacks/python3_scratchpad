'''
filename: random_opinions.py
purpose: display random opinion
concepts:
    - module: random
    - lists[]
'''
# modules
import random

# variables
opinions = ["straight trash","awful","despicable","awesome","beautiful"]

# app begins here
first_name = input("What's your name? ✍️: ")
fave_movie = input("Because you have to choose for this prompt, what's your favorite movie? 🎞 : ")

# outcome of code
print(f"\nThanks, {first_name}! {fave_movie} was totes {random.choice(opinions)}...")
