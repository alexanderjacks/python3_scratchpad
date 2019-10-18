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
# Advanced Version 1
1. Convert each word to lower case (`lower`)
2. Remove all the spaces from each word by replacing them with empty strings (`replace`)
# Advanced Version 2
Make your program ignore punctuation when checking anagrams.
# Advanced Version 3
Let the user enter as many words as they choose. If every word is an anagram of every other word, let the user know.
'''
def word_to_letters(word):
    return [letter for letter in word]

word_1 = input("Plz enter a word.: ")
word_2 = input("Plz enter another word.: ")
letter_list_1 = word_to_letters(word_1) # making str into list
letter_list_1.sort() # alphabetizing list of letters
letter_list_2 = word_to_letters(word_2)
letter_list_2.sort()

# for x in letter_list_1:
#     print(x)
# print("\n")
# for y in letter_list_2:
#     print(y)
anagram_length = len(letter_list_1)
# print(anagram_length)
while (anagram_length > 0):
    print(letter_list_1[anagram_length-1])
    anagram_length -= 1

anagram_length = len(letter_list_2)
# print(anagram_length)
while (anagram_length > 0):
    print(letter_list_2[anagram_length-1])
    anagram_length -= 1
