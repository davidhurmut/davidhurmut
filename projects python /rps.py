import random

choices = ["rock", "paper", "scissors"]

player = input("rock paper scissors: ").lower()
computer = random.choice(choices)
print("system:", computer)

if player == computer:
    print("Draw")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("You win")
else:
    print("You lose")
