## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test in your script (unit test) and see your results.

# Experimentation.
# 'a', 'e', 'i', 'o', 'u'

testword1 = "California" # 5 vowels, all lowercase.
testword2 = "cAlIfOrNiA" # 5 vowels, 4 uppercase.
notword1 = 5
notword2 = "5"

def count_vowels(word):
    # Raise error if `word` is integer.
    if isinstance(word, int):
        return "Input is an integer. Please enter a word!"
    # Raise error is `word` contains non-letters passed as strings.
    nonletters = []
    for letter in word:
        nonletters.append(not letter.isalpha())
    if any(nonletters):
        return "Input contains non-letters. Please enter a word!"
    # Make all letters lowercase.
    word = word.lower()
    # Separate letters in list.
    word = [letter for letter in word]
    # Count number of vowels.
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_num = 0
    for letter in word:
        if letter in vowels:
            vowel_num += 1
    return(vowel_num)

# Try different cases to make sure it works right.
count_vowels(testword1)
count_vowels(testword2)
count_vowels(notword1)
count_vowels(notword2)

# Make unit tests.
import unittest

class()