''' Lab 7: Password Generator
Let's generate a password ten characters long using a loop (while loop or for loop) and random.choice, this will be a string of random characters.

Advanced Version 1
Allow the user to choose how many characters the password will be.

Advanced Version 2
Allow the user to choose how many letters, numbers, and punctuation characters they want in their password. Mix everything up using list(), random.shuffle(), and ''.join().
'''
import random
import string
lowers = string.ascii_lowercase
uppers = string.ascii_uppercase
possible_characters = lowers + uppers
counter = 1
while counter < 11:
    print(f"#{counter}: Here's a random lowercase letter: {random.choice(possible_characters)}")
    counter += 1
