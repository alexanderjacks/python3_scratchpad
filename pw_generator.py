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
punctuation = ["!","@","#","$","%","^","&","*","(",")","~","+"]
possible_characters = lowers + uppers + ''.join(punctuation)
inprogress_password = []

counter = int(input("How long of a password do you want? Enter a number between 10 and 256."))
if 10 <= counter <= 256:
    while counter > 0:
        inprogress_password.append(random.choice(possible_characters))
        counter -= 1
    finalized_password = ''.join(inprogress_password)
    print(f"Here's a randomized, 10-character password (do not use after 1998): {finalized_password}")
else:
    print("Please try this script again, and enter a number bigger than 10 and smaller than 2^8 + 1")
