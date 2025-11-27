# Before running this script run this in the terminal:
#   pip install english-words
#

import random
from english_words import get_english_words_set

print("Please refrain from entering multiple letters.")
web2lowerset = get_english_words_set(['web2'], lower=True)
word_bank = list(web2lowerset)

word = random.choice(word_bank)
guessed_word = ["_"] * len(word)
attempts = 10

vowels = ['a', 'e', 'i', 'o', 'u']
for vowel in vowels:
    if vowel in word:
        for x in range(len(word)):
            if vowel == word[x]:
                guessed_word[x] = vowel

tried = ['a','e','i','o','u']

while attempts > 0:
    print("\nCurrent word: " +  "".join(guessed_word))
    guess = input("Guess a letter: ").lower()
    if guess in tried:
        print("You already entered this character before.")
        attempts -= 1
        print(f"Attempts left: {attempts}")
    elif guess in word and 2 > len(guess) > 0:
        for x in range(len(word)):
            if guess == word[x]:
                guessed_word[x] = guess
        print("Great Guess!")
    else:
        attempts -= 1
        print(f"Wrong Guess! Attempts left: {attempts}")
    tried += guess

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word!")
        break
if attempts == 0 and "_" in guessed_word:
    print('\nYou\'ve run out of attempts! The word was: ' + word)