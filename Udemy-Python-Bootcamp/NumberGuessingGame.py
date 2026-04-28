"""
Number Guessing Game 🎯

This is a simple command-line game where the user tries to guess
a randomly generated number within a given range.

How it works:
- The user inputs a lower and upper limit.
- The program generates a random number within that range.
- The user gets 6 chances to guess the correct number.
- After each guess, the program gives hints:
  • "Too low" if the guess is smaller than the number
  • "Too high" if the guess is larger than the number
- The game ends when:
  • The user guesses correctly, OR
  • All attempts are used

Concepts used:
- Python loops (while)
- Conditional statements (if-elif-else)
- User input handling
- Random number generation
"""

import random

print("Welcome to the Number Guessing Game, You can guess the number within the range you have provided."
      "\n You have 6 chances to guess the number.")

low=int(input("Enter lower limit: \n"))
high=int(input("Enter higher limit: \n"))

num=random.randint(low,high)
chances=6
guess_counter=0

while guess_counter<=chances:
    guess_counter=guess_counter+1
    guess=int(input("Enter your guess: "))

    if guess==num:
        print("You guessed the number")
        break
    elif guess_counter>=chances and guess!=num:
        print(f"Sorry, better luck next time. The number was {num}")
    elif guess<num:
        print("Sorry, your guess is too low")
    elif guess>num:
        print("Sorry, your guess is too high")

