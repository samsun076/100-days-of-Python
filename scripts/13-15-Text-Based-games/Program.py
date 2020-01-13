from actors import Creature

def main():
    print_header()
    game_loop()


def print_header():

    print('----------------------')
    print('     WIZARD GAME')
    print('----------------------')
    pritn()


def game_loop():
    creatures = [
        # TODO: add some creatures
        Creature('Bat', 5),
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)

    ]

    hero = none # TODO: Create our hero
    while True:
        #randomly choose a creature
        # active_creature = none

        print('A {} of level {} has appeared from the dark and foggy forest...'.format(...))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            pass
            #Todo: Attack

        elif cmd == 'r':
            print()
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees: '.format(hero.name))
            # TODO: sho the creatures in the room
        else:
            print('OK, exiting game....bye!')

        if not creatures:
            print('You  have defeated all the creatures, well done!')
            break
    Print("Good Bye")
