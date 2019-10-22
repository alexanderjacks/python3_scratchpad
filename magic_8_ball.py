'''
filename: magic-8-ball.py
purpose: emulate the infamous toy w/o intent to infrige upon copyrights
concepts:
    - module: random
    - lists[]
research: https://en.wikipedia.org/wiki/Magic_8-Ball
'''
# modules
import random

# variables,
eightball_isms = [
"It is certain. 🍀",
"It is decidedly so. ☘️",
"Without a doubt. 💚",
"Yes - definitely. 💚",
"You may rely on it. ✅",
"As I see it, yes. ✅",
"Most likely. ✅",
"Outlook good. ✅",
"Yes. ✅",
"Signs point to yes. ✅",
"Reply hazy, try again. 💛",
"Ask again later. 💛",
"Better not tell you now. 💛",
"Cannot predict now. 💛",
"Concentrate and ask again. 💛",
"Don't count on it. 🔴",
"My reply is no. 🔴",
"My sources say no. 🔴",
"Outlook not so good. 🔴",
"Very doubtful. 🔴"
]

# app begins here
'''
for x in eightball_isms
    print(x)
    '''
player_name = input("What's your name? ✍️: ")
your_question = input("🎱 Thank you for seeking answers of the Magic 8 Ball™️. What is your question? 🎱 ")

# outcome of code
print(f"\nHello, {player_name}! In answer to {your_question}...\n {random.choice(eightball_isms)}")
