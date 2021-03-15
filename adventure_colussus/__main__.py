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

    # pick a character
    choice = main_menu(CLEAR_SCREEN)

    if choice == '1':
        character, character_file_name = new_character(CLEAR_SCREEN)
    elif choice == '2':
        character, character_file_name = load_character(CLEAR_SCREEN)
    elif choice == '3':
        print_text(' > Ending session...', 0.5)
        print_text(' > Session ended successfully \n', 1)
        sys.exit(0)
    elif choice == '4':
        print_text("exiting...", 1)
        sys.exit(0)
    else:
        print_text('Invalid response. Please try again')

    # pick a quest
    system(CLEAR_SCREEN)
    print_text(("_" * 117 + "\n"), 0.3)  # length of screen_line
    print_text(f"{character.name},\n", 0.5)
    quest = jh.load_quest()

    # game loop
    system(CLEAR_SCREEN)
    print_text(("_" * 117 + "\n"), 0.3)  # length of screen_line
    jh.print_question(quest["one"], quest)

    # exit program with save
    print_text(
        "Congratulations on completing your quest, now rest in the Hall of Heroes.\n", 0.5)
    character.save(f"./{character_file_name}.dat")
    print_text("SUCESS! EXITING", 1)


if __name__ == '__main__':
    main()
