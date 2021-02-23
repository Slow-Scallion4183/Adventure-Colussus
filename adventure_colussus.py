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
    print_text(' > saving character\n', 1)
    with open(save_name_pickle, 'wb') as f:
        pickle.dump(character, f)
        print_text(' > character saved successfully')


def load_character(load_name):
    """
    Loads the selected character from a pickle database.
    """
    load_name_pickle = load_name + '.pickle'
    print_text(' > loading character...\n', 1)
    pickle_in = open(load_name_pickle, "rb")
    character = pickle.load(pickle_in)
    print_text(' > character loaded successfully\n')
    print_text(f"\n > welcome back {character['name']}!!!\n", 0.5)
    print_text('\n > here are your stats from last time: \n', 0.5)
    print(f' > {character} ')


def character_generator():
    """
    Generates a character determined by user input and saves it in
    a pickle database.
    """
    print_text('\n > we have reached the first crucial part of your journey: we must choose the path that you will take! the decision\n', 0.5)
    print_text(' > is up to you my friend! Whether you choose to be a bloodthirsty warrior or a cunning and strategic fighter,\n', 0.8)
    print_text(' > the choice is up to you!\n', 0.5)
    print_text('\n > now then, lets get right into it!', 0.8)
    print_text(' are you more of a tanky player[1] or a strategic player[2]?')

    player_t_choice_1 = get_input('\n > ', ['1', '2'])

    if player_t_choice_1 == '1':
        health = 100
        damage = 75

    elif player_t_choice_1 == '2':
        health = 75
        damage = 50

    print_text('\n > so, we have that out of the way, lets carry on!', 0.8)
    print_text(' oh of course! sorry to forget! another quick question: ', 0.5)
    print_text('do you like \n')
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
        '\n > good good! we have decided your play style and your preferred ways of attacking the enemy!\n', 0.5)
    print_text(
        ' > now, we must see what luck we are able to bestow upon you. be warned: it is entirely random!\n', 0.8)
    random_luck = input('\n > press enter to roll a dice...')
    time.sleep(0.3)
    print_text(' > rolling dice...\n')
    luck = random.randint(0, 10)
    time.sleep(1)
    print_text(f' > your hero has {luck} luck out of 10!\n', 0.8)
    print_text(
        '\n > at last! we have reached the most important part of creating your character! The naming!\n')
    print_text(
        ' > choose wisely my friend. your hero will be named this for the rest of their lives...\n', 1)

    print_text('\n > what should your hero be named?\n ')

    name = ''
    while not name:
        name = input(' > ')

    time.sleep(1)
    print_text(
        f'\n > welcome mighty hero! you shall be named: {name} !!!\n ', 0.3)
    print_text('> a fine choice')
    print_text('\n')

    print_text(
        ' \n > now then. i guess you be on your way! you have a journey to start and a belly to fill!\n')
    print_text(
        ' > i have to say, i have rather enjoyed your company! feel free to come by at any time!\n ')
    print_text('> goodbye and god speed!', 1)
    print('\n')
    print_text(' > your final stats are as follows: \n', 0.3)
    print(
        f" > [ health: {health}, damage: {damage}, shield: {shield}, magic: {magic}, luck: {luck}, name: {name} ]")

    print_text(
        '\n > we should now save your character if you want to come back to it later - character file name: \n ')
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
    print('\n > [1] create new game')
    print(' > [2] load existing game')
    print(' > [3] end game')
    print(' > [4] credits')
    choice = get_input("\n > ", ['1', '2', '3', '4'])

    if choice == '1':
        print_text(
            "\n > you have chosen to create a new game: redirecting...", 0.75)
        system(CLEAR_SCREEN)
        screen_line()
        print('  \n  we will begin with creating your character:                                        quick tip: choose wisely')
        screen_line()
        time.sleep(0.5)
        character_selection_horse_and_knight()
        screen_line()
        time.sleep(0.3)
        character_generator()

    elif choice == '2':
        print_text(
            "\n > you have chosen to load an existing game: redirecting...", 0.75)
        system(CLEAR_SCREEN)
        time.sleep(0.5)
        screen_line()
        print('  \n  we will begin with choosing an existing character:                             quick tip: make sure it exists!')
        screen_line()
        time.sleep(0.5)
        character_selection_horse_and_knight()
        screen_line()
        character_file_name = input('\n > character file name: ')
        load_character(character_file_name)

    elif choice == '3':
        print_text(' > ending session...', 0.5)
        print_text(' > session ended successfully \n', 1)
        sys.exit()

    elif choice == '4':
        pass

    else:
        print_text('incorrect response. please try again')


if __name__ == '__main__':
    main()
