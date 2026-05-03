import random

#ASCII art
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") -> for printing the ascii art
#● ┌ ─ ┐ │ └ ┘

#we need 5 lines for each face of the die

"┌─────────┐"
"│         │"
"│    ●    │"
"│         │"
"└─────────┘"

#dictionary
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")
}

dice=[]
total=0
num_of_dice=int(input("How many times want to roll the dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

#To print the dice rolls vertically
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

#To print the dice rolls horizontally
for line in range(5): # 5 because there 5 lines in the ascii art for each die roll
    for die in dice:
        print(dice_art.get(die)[line],end="")
    print()

for die in dice:
    total+=die

print(f"Total: {total}")


