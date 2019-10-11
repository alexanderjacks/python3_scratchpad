# in "bash" aka Terminal in Linux/macOS
# touch makes empty files
# mkdir makes empty directories

# Slack
# paperclip OR create new in DM in Slack for homework

# Python3
# print function is built-in to python, prints right to the Terminal (or the Console in Chrome!)
# input() asks for user input, it works very much opposite to print() function
# comment liness are ignored when compiling code
# notes and team communication
# triple single quotes
'''
works for multi-line comments and can
easily get bumped below or above
to make code experimental
'''

'''
filename: hello.py
purpose: say hello
author: Alex Jacks
'''

print("Halo Whirled. 🚀")

# variables hold data for laters
greeting = "HALO"
planet = "Mercury"
spaceholder = " " # get it?

# print('a single variable is easy to print')
print(greeting)

# print('now printing many variables of text, spacing of which gets old fast')
print(greeting + spaceholder + planet) # concatenating works much like in JS

# print(fstrings are new in python3: format strings interpolate variables smoothly)
# add f to declare a normal string "" as a format string f""
print(f"{greeting}! I'm from {planet}.")
