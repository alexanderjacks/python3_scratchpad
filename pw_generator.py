''' Lab 7: Password Generator
Let's generate a password ten characters long using a loop (while loop or for loop) and random.choice, this will be a string of random characters.

Advanced Version 1
Allow the user to choose how many characters the password will be.

Advanced Version 2
Allow the user to choose how many letters, numbers, and punctuation characters they want in their password. Mix everything up using list(), random.shuffle(), and ''.join().
'''
# To use the nifty copy/paste feature, please first run:
# $ sudo pip3 install pyperclip
# in your Terminal
import random
import string
# import pyperclip
lowers = string.ascii_lowercase
uppers = string.ascii_uppercase
punctuation = ["!","@","#","$","%","^","&","*","(",")","~","+","{","}","[","]","-","|","`","="]
possible_characters = lowers + uppers + ''.join(punctuation)
inprogress_password = [] # imho variable names can substitute for comments/notes

counter = int(input("How long of a password do you want? Enter a number between 10 and 256."))
remember_their_choice = counter
if 10 <= counter <= 256:
    while counter > 0:
        inprogress_password.append(random.choice(possible_characters))
        counter -= 1
    finalized_password = ''.join(inprogress_password)
# plz uncomment for nifty feature where it copies pw to your clipboard automatically. Plz install pyperclip 1st!
    # pyperclip.copy(finalized_password)

    print(f"Here's a randomized, {remember_their_choice}-character password: {finalized_password}")
    # ditto on uncomment below for autocopy
    # print("\nWe've copied it (ya know, Ctrl+C'd it) to your clipboard, so Paste it somewhere safe!\nOr go ahead and drag over the password and copy/paste it yourself, we know it's tough to trust open source software. 🤖💦")
else:
    print("Please try this script again, and enter a number bigger than 10 and smaller than 2^8")
