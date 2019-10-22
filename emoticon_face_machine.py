''' Lab 5: Random Emoticon Generator
Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth.
☑ Define a list of eyes
☑ Define a list of noses
☑ Define a list of mouths
☑ Randomly pick a set of eyes
☑ Randomly pick a nose
☑ Randomly pick a mouth
☑ Assemble and display the emoticon!
import random
fruits = ['apple', 'banana', 'pineapple']
fruit = random.choice(fruits)
print(fruit)
Advanced Version 1
    Use a for loop to generate 5 emoticons.
Advanced Version 2
    In a while loop, ask the user if they want another emoticon
Advanced Version 3
    Ask the user if they want to choose each part of the face. If they do, let the user choose that part of the face. If they don't, randomly generate that part.
Advanced Version 4
Let the user choose if they want to make one-line horizontal faces like :-), one-line vertical faces like o_O, or multi-line vertical faces like:
O O
 |
 ~
'''
'''
emoticon-face-machine.py
Alex Jacks (j4cks)
Software Features:
    Builds faces out of emojis
    Random choice from options
Code Mechanics:
    random.choice()
    advanced.feature(while & for loops)
    advanced.feature(complex user input paths)
Human factoids:
    The face cortex is the most advanced visual-perceptual part of the brain, coming after color and motion. Faces are gestalts --they are always collections of parts-- so faces get 'seen' after everything else is processed...
 '''

import random
eyes_1 = ["👁‍🗨","👁","🔹","🔴","⚫️","🌀","♻️","⽬"]
noses_1 = ["👃🏽","🥕","🔻","🐽","🚪","🥦","🍡","🥔"]
mouths_1 = ["👄","⬯","⬭","🌀","〰","🏑","💋","⼝"]

random_eye_left = random.choice(eyes_1)
random_eye_right = random.choice(eyes_1)
random_nose = random.choice(noses_1)
random_mouth = random.choice(mouths_1)
ascii_padding = " " # declaring this now makes more sense than earlier imho

print(random_eye_left + ascii_padding + random_eye_right)
print(ascii_padding + random_nose)
print(ascii_padding + random_mouth)

# neat idea: add an input() that asks if you want to see another face
# advanced features 1-4 under development
