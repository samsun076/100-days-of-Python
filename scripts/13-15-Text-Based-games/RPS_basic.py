# RPS game at its most basic level.
# Made TODOs for future tinkering once complete with 100days.


import random

# TODO: Make more efficient
# TODO: add classes
# TODO: add function to add help and/or rule set
# TODO: add function to keep track of score and print out on screen after game over
# TODO: add function to give player choice to pick best of number in series.




def main():
    options = ["rock", "paper", "scissors"]
    comp = None
    user_choice = None
    for game in range(15):
        while user_choice not in options:
            user_choice= input("Please choose rock, paper, or scissors: ")
        comp = random.choice(options)
        print("you: ", user_choice, "VS", comp)

        if user_choice == comp:
            print("Tie")
            user_choice = None
        elif (user_choice == "paper") and (comp == "rock"):
            print("win")
            user_choice = None
        elif (user_choice == "scissors") and (comp == "paper"):
            print("win")
            user_choice = None
        elif (user_choice == "rock") and (comp == "scissors"):
            print("win")
            user_choice = None
        else:
            print("Loss")
            user_choice = None

if __name__ == "__main__":
    main()