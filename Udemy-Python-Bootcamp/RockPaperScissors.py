import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def play_game():
    art_options = [rock, paper, scissors]
    text_options=["rock","paper","scissors"]
    print("Welcome to the Rock Paper Scissors game!")

    while True:
        user_choice=input("Enter your choice (rock, paper, or scissors) else 'quit' to stop:").lower()

        if user_choice=='quit':
            print("Thank you for playing!")
            break
        if user_choice not in text_options:
            print("Invalid Choice!, Please retry")
            continue

        computer_choice=random.choice(text_options)
        user_index=text_options.index(user_choice)
        computer_index=text_options.index(computer_choice)
        print(f"You Chose:\n{art_options[user_index]}\nComputer Chose:\n{art_options[computer_index]}")

        if(user_choice==computer_choice):
            print("It's a tie!")

        elif(user_choice=='rock' and computer_choice=='scissors') or \
            (user_choice=='paper' and computer_choice=='rock') or \
            (user_choice=='scissors' and computer_choice=='paper'):
            print("You Win")
        else:
            print("You Lose")

if __name__ == "__main__":
    play_game()

