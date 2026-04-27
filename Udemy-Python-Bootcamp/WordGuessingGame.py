"""
Word Guessing Game (Python)

This is a simple command-line word guessing game.

How it works:
- The program randomly selects a word from a predefined list.
- The user tries to guess the word one letter at a time.
- Each correct guess reveals the position(s) of the letter in the word.
- Each wrong guess reduces the number of remaining attempts.
- The player wins if they guess all letters before running out of attempts.
- The player loses if all attempts are used up before guessing the word.

Features:
- Random word selection using the 'random' module
- Tracks guessed letters
- Displays progress after each guess
- Limited number of attempts (12)

Concepts Used:
- Loops (while, for)
- Conditional statements (if-else)
- Strings and lists
- User input handling
- Basic game logic

Author: [Your Name]
"""

import random

print("Welcome to WordGuessingGame")

# Declare the set of words from which the user has to guess the characters
words=["rainbow","mountain","ocean","programming","dream","muruga","python","projects","consistency","concentration","focus","practise","determination","reverse","computer",
       "science","alien","scientist","engineer","pilot","space","rocket"]

# Randomly choose a word
word=random.choice(words)

print("Guess the characters, the word has",len(word),"letters")

guesses=""
attempts=12

while attempts>0:
    # Step 1 - Ask for user input
    guess=input("\nGuess enter a character : ")
    guesses+=guess

    # Step 2 - Check if guess is correct or wrong
    if guess not in word:
        attempts-=1
        print("Wrong! you have ",attempts," more guesses left")
    else:
        print("Correct!")

    # Step 3 - Show the word progress
    failed=0
    for letter in word:
        if letter in guesses:
            print(letter,end=" ")
        else:
            print("_",end=" ")
            failed+=1
    print("\n")

    # Step 4 - Check win condition
    if failed==0:
        print("\nYou win!")
        print("The word is: ",word)
        break

    # Step 5 - Check lose condition
    if attempts==0:
        print("\nYou Loose")
        print("the word was: ",word)
