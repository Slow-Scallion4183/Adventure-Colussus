from adventure_colussus import *
import time
import random
import adventure_colussus.json_handlers as jh


CLEAR_SCREEN = 'clear'
if platform.system() == 'Windows':
    CLEAR_SCREEN = 'cls'

def main():
    """
    This is where everything to do with the main game is. This includes all functions in one
    way or another. 
    """
    choice = main_menu(CLEAR_SCREEN)

    if choice == '1':
        character, character_file_name = new_character(CLEAR_SCREEN)
    elif choice == '2':
        character, character_file_name = load_character(CLEAR_SCREEN)
    elif choice == '3':
        print_text(' > Ending session...', 0.5)
        print_text(' > Session ended successfully \n', 1)
        sys.exit()
    elif choice == '4':
        print_text("exiting...", 1)
        sys.exit(0)
    else:
        print_text('Invalid response. Please try again')

    print_text(f"{character.name},\n", 0.5)

    quest = jh.load_quest()
    jh.print_question(quest["one"], quest)
    print_text("Congratulations on completing your quest, now rest in the Hall of Heroes.\n", 0.5)
    character.save(f"./{character_file_name}.dat")
    print("SUCESS! EXITING")


    # if choice == '1':
        # print_text(
        #     "\n > You have chosen to create a new game: Redirecting...", 0.75)
        # system(CLEAR_SCREEN)
        # screen_line()
        # print('  \n  We will begin with creating your character:                                        Quick tip: Choose wisely')
        # screen_line()
        # time.sleep(0.5)
        # character_selection_horse_and_knight()
        # screen_line()
        # time.sleep(0.3)
        # character_generator()

    # elif choice == '2':
        # print_text(
        #     "\n > You have chosen to load an existing game: Redirecting...", 0.75)
        # system(CLEAR_SCREEN)
        # time.sleep(0.5)
        # screen_line()
        # print('  \n  We will begin with choosing an existing character:                             Quick tip: Make sure it exists!')
        # screen_line()
        # time.sleep(0.5)
        # character_selection_horse_and_knight()
        # screen_line()
        # character_file_name = input('\n > Character file name: ')
        # #load_character(character_file_name)

        # # The new character load
        # character = entities.Human.load(f"./{character_file_name}.dat")
        # print(character.__repr__())
        # tests
        # bob = entities.Ranger.generate('Bob')
        # jim = entities.Brawler.generate('Jim')
        # print(jim.attack(1, bob))
        # print(bob.attack(1, jim))
        # print(jim.attack(2, bob))
        # print(bob.attack(1, jim))
        # print(jim.attack(1, bob))
        # print(bob.attack(2, jim))

        # z = entities.Zombie.generate()

        # while z.current_health > 0:
        #     print(jim.attack(1, z))
        #     print(bob.attack(2, z))

if __name__ == '__main__':
    main()
