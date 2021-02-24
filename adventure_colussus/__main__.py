from adventure_colussus import *
import time
import random


CLEAR_SCREEN = 'clear'
if platform.system() == 'Windows':
    CLEAR_SCREEN = 'cls'

def main():
    """
    This is where everything to do with the main game is. This includes all functions in one
    way or another. 
    """
    time.sleep(0.5)
    system(CLEAR_SCREEN)
    time.sleep(0.5)
    show_date_and_time = datetime.datetime.now()
    screen_line()
    print('\n  <Adventure Colossus>         version: v', counter,
          '| current date: ', show_date_and_time, '| date of creation: 9.2.2021')
    screen_line()
    time.sleep(0.5)
    mountain_range()
    screen_line()
    print('\n > [1] Create new game')
    print(' > [2] Load existing game')
    print(' > [3] End game')
    print(' > [4] Credits')
    choice = get_input("\n > ", ['1', '2', '3', '4'])

    if choice == '1':
        print_text(
            "\n > You have chosen to create a new game: Redirecting...", 0.75)
        system(CLEAR_SCREEN)
        screen_line()
        print('  \n  We will begin with creating your character:                                        Quick tip: Choose wisely')
        screen_line()
        time.sleep(0.5)
        character_selection_horse_and_knight()
        screen_line()
        time.sleep(0.3)
        character_generator()

    elif choice == '2':
        print_text(
            "\n > You have chosen to load an existing game: Redirecting...", 0.75)
        system(CLEAR_SCREEN)
        time.sleep(0.5)
        screen_line()
        print('  \n  We will begin with choosing an existing character:                             Quick tip: Make sure it exists!')
        screen_line()
        time.sleep(0.5)
        character_selection_horse_and_knight()
        screen_line()
        character_file_name = input('\n > Character file name: ')
        load_character(character_file_name)
        # tests
        bob = Ranger('Bob')
        jim = Brawler('Jim')
        print(jim.attack('Hands', bob))
        print(bob.attack('Hands', jim))
        print(jim.attack('Bow', bob))
        print(bob.attack('Sword', jim))
        print(jim.attack('Sword', bob))
        print(bob.attack('Bow', jim))

        z = Zombie()

        while z.current_health > 0:
            print(jim.attack('Sword', z))
            print(bob.attack('Bow', z))

    elif choice == '3':
        print_text(' > Ending session...', 0.5)
        print_text(' > Session ended successfully \n', 1)
        sys.exit()

    elif choice == '4':
        pass

    else:
        print_text('Invalid response. Please try again')


if __name__ == '__main__':
    main()
