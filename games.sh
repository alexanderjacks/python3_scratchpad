#!/bin/bash
# Please run this script with `source games.sh`
echo "Here's an anagram game."
python3 anagramalyzer.py
echo "Now for an oracle game."
python3 magic_8_ball.py
echo "Now a High-Low guessing game."
python3 guess_the_number.py
echo "Finally, play as much Rock-Paper-Scissors as you want!"
echo "(Type 'python3 RPS.py' to play this game by itself)"
python3 RPS.py
