import datetime
import pickle
import platform
import random
import time
import sys

from os import system, name
from typing import Dict, Any

from ascii_art_functions import character_selection_horse_and_knight
from ascii_art_functions import mountain_range
from ascii_art_functions import screen_line

from subprocess import call

CLEAR_SCREEN = 'clear'
if platform.system() == 'Windows':
    CLEAR_SCREEN = 'cls'

def get_input(string: str, valid_options: list) -> str:
    """
    Deals with error checking for inputs
    """
    while True:
        user_input = input(string)
        if user_input in valid_options:
            return user_input


def version_counter(filename="adventure_colussus_version_counter.dat"):
    """
    Determines the version of the last played game, either in the {VERSION_FILENAME}
    file, or generating a new file if none is found.
    """
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val


counter = version_counter()


def print_text(text: str, sleep_time: float = 0.0) -> None:
    """
    Prints the text to the console character by character. RPG style.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.021)
    if sleep_time != 0.0:
        time.sleep(sleep_time)


def save_character(save_name: str, character: Dict[str, Any]) -> None:
    """
    Saves the current character to a pickle database.
    """
    save_name_pickle = save_name + '.pickle'
    print_text(' > Saving character\n', 1)
    with open(save_name_pickle, 'wb') as f:
        pickle.dump(character, f)
        print_text(' > Character saved successfully')


def load_character(load_name):
    """
    Loads the selected character from a pickle database.
    """
    load_name_pickle = load_name + '.pickle'
    print_text(' > Loading character...\n', 1)
    pickle_in = open(load_name_pickle, "rb")
    character = pickle.load(pickle_in)
    print_text(' > Character loaded successfully\n')
    print_text(f"\n > Welcome back {character['name']}!!!\n", 0.5)
    print_text('\n > Here are your stats from last time: \n', 0.5)
    print(f' > {character} ')


def character_generator():
    """
    Generates a character determined by user input and saves it in
    a pickle database.
    """
    print_text('\n > We have reached the first crucial part of your journey: We must choose the path that you will take! The decision\n', 0.5)
    print_text(' > is up to you my friend! Whether you choose to be a bloodthirsty warrior or a cunning and strategic fighter,\n', 0.8)
    print_text(' > the choice is up to you!\n', 0.5)
    print_text('\n > Now then, lets get right into it!', 0.8)
    print_text(' Are you more of a tanky player[1] or a strategic player[2]?')

    player_t_choice_1 = get_input('\n > ', ['1', '2'])

    if player_t_choice_1 == '1':
        health = 100
        damage = 75

    elif player_t_choice_1 == '2':
        health = 75
        damage = 50

    print_text('\n > So, we have that out of the way, Let\'s carry on!', 0.8)
    print_text(' Oh of course! Sorry to forget! Another quick question: ', 0.5)
    print_text('Do you like \n')
    print_text(
        ' > to use magic from great distances[1] or run in to the thick of battle wielding a deadly blade[2]? ')

    player_t_choice_2 = get_input('\n > ', ['1', '2'])

    if player_t_choice_2 == '1':
        shield = 50
        magic = 75

    elif player_t_choice_2 == '2':
        shield = 75
        magic = 45

    print_text(
        '\n > Good good! We have decided your play style and your preferred ways of attacking the enemy!\n', 0.5)
    print_text(
        ' > Now, we must see what luck we are able to bestow upon you. Be warned: it is entirely random!\n', 0.8)
    random_luck = input('\n > Press enter to roll a dice...')
    time.sleep(0.3)
    print_text(' > Rolling dice...\n')
    luck = random.randint(0, 10)
    time.sleep(1)
    print_text(f' > Your hero has {luck} luck out of 10!\n', 0.8)
    print_text(
        '\n > At last! We have reached the most important part of creating your character! The naming!\n')
    print_text(
        ' > Choose wisely my friend. Your hero will be named this for the rest of their lives...\n', 1)

    print_text('\n > What should your hero be named?\n ')

    name = ''
    while not name:
        name = input(' > ')

    time.sleep(1)
    print_text(
        f'\n > Welcome mighty hero! You shall henceforth be known as: {name} !!!\n ', 0.3)
    print_text('> A perfect choice!')
    print_text('\n')

    print_text(
        ' \n > Now then. I guess you should be on your way! You have a journey to start and a belly to fill!\n')
               
    #Should Implement The Script And Story From Here.
               
    print_text(
        ' > I have to say, I have rather enjoyed your company! Feel free to come by at any time!\n ')
    print_text('> Goodbye and god speed!', 1)
    print('\n')
    print_text(' > Your final stats are as follows: \n', 0.3)
    print(
        f" > [ health: {health}, damage: {damage}, shield: {shield}, magic: {magic}, luck: {luck}, name: {name} ]")

    print_text(
        '\n > We should now save your character if you want to come back to it later - character file name: \n ')
    character = {'health': health, 'damage': damage,
                 'shield': shield, 'magic': magic, 'luck': luck, 'name': name}
    character_file_name = input('> ')
    save_character(character_file_name, character)

# non player characters


def Louis_NPC(joke, mood):
    '''
    A function that creates our 1st NPC called Louis
    '''
    existence = True
    print(joke)
    print(f'I am feeling {mood} today')


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
