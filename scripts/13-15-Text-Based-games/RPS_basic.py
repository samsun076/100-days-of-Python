import random

options = ["rock", "paper", "scissors"]


comp = random.choice(options)
user_choice = None
while user_choice not in options:
    user_choice= input("Please choose rock, paper, or scissors: ")

print("you: ", user_choice
      , "VS", comp)