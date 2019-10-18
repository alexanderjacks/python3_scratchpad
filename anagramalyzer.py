''' Lab 10: Anagram Checker
Two words are anagrams of each other if the letters of one can be rearranged to fit the other. e.g. `dormitory` and `dirty room`.

Let's write an anagram checker; at its most simple this is a program that lets the user enter two strings, and reports if they are anagrams of each other.
1. Convert the strings into lists (`list`)
2. Sort the letters of each word (`sort`)
3. Check if the two are equal
```
>>> enter the first word: dormitory
>>> enter the second word: dirtyroom
>>> 'dormitory' and 'dirtyroom' are anagrams
```
# Advanced Features
X Convert each word to lower case (`lower`)
- Remove all the spaces from each word by replacing them with empty strings (`replace`)
- Make your program ignore punctuation when checking anagrams.
- Let the user enter as many words as they choose. If every word is an anagram of every other word, let the user know.
'''
def word_to_letters(word):
    return [letter for letter in word]

print("Two words are anagrams if their letters can be scrambled to spell each other, like `battle` and `tablet`.\nCan you please input 2 words, so Python can anagramalyze them?")
word_1 = input("Please enter a word: ")
word_1 = word_1.lower()
word_2 = input("Please enter another word: ")
word_2 = word_2.lower()
if len(word_1) == len(word_2):
    letter_list_1 = word_to_letters(word_1) # making str into list
    letter_list_1.sort() # alphabetizing list of letters
    letter_list_2 = word_to_letters(word_2)
    letter_list_2.sort()

    how_many_letters = len(letter_list_1)
    # print(letter_list_1,letter_list_2,how_many_letters) # <- devmode
    while (how_many_letters > 0):
        if (letter_list_1[how_many_letters-1] == letter_list_2[how_many_letters-1]):
            looks_anagrammy = True
            # print("TRUE") # <- devmode
            how_many_letters -= 1
        else:
            looks_anagrammy = False
            # print("FALSE") # <- devmode
            break
    if looks_anagrammy == True:
        print(f"🏆🔃  Congratulations, {word_1} & {word_2} are anagramatical! 🏆🔃")
    else:
        print(f"Sorry, {word_1} & {word_2} don't count as anagrams!")
else: # main logic above, jumps here if the 2 words don't have the same number of letters
    print("✋ Please run this script again (↑ , ⏎ ) and input 2 words of equal length.")
