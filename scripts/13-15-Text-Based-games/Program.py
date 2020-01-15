from actors import Creature, Wizard, Dragon
import random

def main():
    print_header()
    game_loop()


def print_header():

    print('----------------------')
    print('     WIZARD GAME')
    print('----------------------')
    print()


def game_loop():
    creatures = [
        Creature('Bat', 5),
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Dragon('Black Dragon', 50, scaliness=2, breaths_fire=False),
        Wizard('Evil Wizard', 1000)

    ]

    hero = Wizard('Gandalf', 75)

    while True:
        # randomly choose a creature

        active_creature = random.choice(creatures)

        print('A {} of level {} has appeared from the dark and foggy forest...'.format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                print('The Wizard {} has eliminated the {}'.format(hero.name, active_creature.name))
                print('There are {} creatures to defeat.'.format(len(creatures)))
            else:
                print('The wizard has been defeated by a powerful a {}.'.format(active_creature.name))
        elif cmd == 'r':
            print('The wizard {} has become unsure of his powers and flees...'.format(hero.name))
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees: '.format(hero.name))
            for c in creatures:
                print('* {} of level {}.'.format(c.name, c.level))
            print('--\n')
        else:
            print('OK, exiting game....bye!')

        if not creatures:
            print('You  have defeated all the creatures, well done!')
            break


if __name__ == '__main__':
    main()
