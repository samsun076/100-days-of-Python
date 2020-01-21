# PyBite 102: https://codechalleng.es/bites/102/


VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check:
       - if 'quit' was entered for color, print 'bye' and break.
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:
        user_input = input("please guess a color, or quit: ").lower()
        if user_input == "quit":
            print("bye")
            break
        elif user_input in VALID_COLORS:
            print(user_input)
        else:
            print("Not a valid color")


#PyBites Solution
def print_colors_solution():
    while True:
        color = input("Enter a color: ").lower()
        if color == "quit":
            print("bye")
            break

        if color not in VALID_COLORS:
            print('Not a valid color')

        print(color)

#Another intersting user solution
def print_colors02():
    while True:
        color = input('Enter a color ==>  ').lower()
        if color == 'quit':
            print('bye')
            break
        print(color if color in VALID_COLORS else "Not a valid color!")


print_colors()
print()
print_colors_solution()
print()
print_colors02()