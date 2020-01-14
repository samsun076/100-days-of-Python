class Rps():
    def __init__(self, human=True):
        self.human = human
        #self.player = self.create_player()

    def create_player(self):
        if self.human:
            name = input("Please enter your name: ")
            print("You entered: ", name)
            return name


if __name__== "__main__":
    game = Rps()
    game.create_player()
