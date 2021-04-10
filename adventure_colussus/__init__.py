import datetime
import pickle
import platform
import random
import time
import sys

from os import system, name
from typing import Dict, Any
from random import randint, choice


import adventure_colussus.entities as entities

# functions

def get_input(string: str = "", valid_options: list = []) -> str:
    """
    Deals with error checking for inputs

    Returns:
        str: user_input
    """
    while True:
        user_input = input(string)
        if user_input in valid_options:
            return user_input


def session_counter(filename: str ="adventure_colussus_session_counter.dat") -> int:
    """
    Determines the version of the last played game, either in the {VERSION_FILENAME}
    file, or generating a new file if none is found.

    Args:
        filename (str, optional): Defaults to "adventure_colussus_session_counter.dat".

    Returns:
        int: 1 or session_count
    """
    with open(filename, "a+") as sessionfile:
        sessionfile.seek(0)
        val = int(sessionfile.read() or 0) + 1
        sessionfile.seek(0)
        sessionfile.truncate()
        sessionfile.write(str(val))
        return val


session_count = session_counter()

def debug_print(func):
    """
    Overwrites fancy print with fast print for speedier debugging.
    """
    def wrapper(*args, **kwargs):
        value = False
        try:
            if sys.argv[1] in {"-d", "--debug"}:
            # if config_param['debug'] == True:
                print(args[0], end="")
                value = 1
        except:
            pass
        finally:
            if not value:
                return func(*args, **kwargs)
        return value 
    return wrapper

@debug_print
def print_text(text: str = "", sleep_time: float = 0.0) -> None:
    """
    Prints the text to the console character by character, RPG style.

    Args:
        text (str, optional): Defaults to "".
        sleep_time (float, optional): Defaults to 0.0.
    """ 
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.021)
    if sleep_time != 0.0:
        time.sleep(sleep_time)


def print_block(lines: dict = {}) -> None:
    """
    Takes dictionary and prints formatted contents

    Args:
        lines (dict, optional): keys= string to print, values=float wait times. 
                                Defaults to {}.
    """
    for key in lines.keys():
        print_text(key, lines[key])

def character_style_menu() -> tuple:
    """
    Sets character style, health, and damage for character_generate()

    Returns:
        tuple: (string:style, int:health, int:damage)
    """
    character_style_text = {
        "\n > We have reached the first crucial part of your journey: We must choose the path that you will take! The decision\n": 0.5,
        " > is up to you my friend! Whether you choose to be a bloodthirsty warrior or a cunning and strategic fighter,\n": 0.8,
        " > the choice is up to you!\n": 0.5,
        "\n > Now then, lets get right into it!": 0.8,
        " Are you more of a tanky player[1] or a strategic player[2]?": 0.0
    }
    print_block(character_style_text)
    player_t_choice_1 = get_input('\n > ', ['1', '2'])

    if player_t_choice_1 == '1':
        player_style = 'Brawler'
        player_health = 100
        player_damage = 75

    elif player_t_choice_1 == '2':
        player_style = 'Ranger'
        player_health = 75
        player_damage = 50

    return player_style, player_health, player_damage


def attack_style_menu() -> tuple:
    """
    Sets shield and magic for character_generator

    Returns:
        tuple: (int: shield, int: magic)
    """
    attack_style_text = {
        "\n > So, we have that out of the way, Let's carry on! ": 0.8,
        "Oh of course! Sorry to forget! Another quick question: ": 0.5,
        "Do you like \n": 0.5,
        " > to use magic from great distances[1] or run in to the thick of battle wielding a deadly blade[2]?\n": 0.5,
    }
    print_block(attack_style_text)
    player_t_choice_2 = get_input('\n > ', ['1', '2'])

    if player_t_choice_2 == '1':
        player_shield = 50
        player_magic = 75

    elif player_t_choice_2 == '2':
        player_shield = 75
        player_magic = 45
    return player_shield, player_magic


def luck_menu() -> int:
    """
    Sets luck for character_generate()

    Returns:
        int: luck
    """
    luck_text = {
        "\n > Good good! We have decided your play style and your preferred ways of attacking the enemy!\n": 0.5,
        " > Now, we must see what luck we are able to bestow upon you. Be warned: it is entirely random!\n": 0.8
    }
    print_block(luck_text)
    print_text('\n > Press enter to roll a dice...')
    input()
    time.sleep(0.3)
    print_text(' > Rolling dice...\n')
    player_luck = random.randint(0, 10)
    time.sleep(1)
    print_text(f' > Your hero has {player_luck} luck out of 10!\n', 0.8)
    return player_luck

def get_player_name() -> str:
    """
    Sets name for character_generate()

    Returns:
        str: name
    """
    name_text = {
        "\n > At last! We have reached the most important part of creating your character! The naming!\n": 0.0,
        " > Choose wisely my friend. Your hero will be named this for the rest of their lives...\n": 1,
        "\n > What should your hero be named?\n": 0.0
    }
    print_block(name_text)

    player_name = ''
    while not player_name:
        player_name = input(' > ')
    return player_name


def add_player_choices(player_dict: dict = {}) -> entities.Entity:
    """
    Combines previous choices and creates new character

    Args:
        player_dict (dict): values to feed into Entity.generate()

    Returns:
        entities.Entity: character
    """
    # Generate an initial player
    player = entities.Human.generate(name)

    # Update the player
    if player_dict['player_style'] == "Brawler":
        player = entities.Brawler(**(dict(player) | player_dict))
    elif player_dict['player_style'] == "Ranger":
        player = entities.Ranger(**(dict(player) | player_dict))
    else:
        player = entities.Human(**(dict(player) | player_dict))

    return player


def character_generator() -> tuple:
    """
    Generates a character determined by user input and saves it in
    a pydantic database.

    Returns:
        tuple: (Entity:character, string:character_file_name)
    """
    # get player choices
    character_style, total_health, damage = character_style_menu()
    shield, magic = attack_style_menu()
    luck = luck_menu()
    name = get_player_name()

    time.sleep(1)

    character_dict = {'player_style':character_style, 'health': total_health, 'damage': damage,
                      'shield': shield, 'magic': magic, 'luck': luck, 'name': name}
    character = add_player_choices(character_dict)

    menu_wrap = {
        f"\n > Welcome mighty hero! You shall henceforth be known as: {name} !!!\n ": 0.3,
        "> A perfect choice!\n": 0.0,
        " \n > Now then. I guess you should be on your way! You have a journey to start and a belly to fill!\n": 0.5,
        " > I have to say, I have rather enjoyed your company! Feel free to come by at any time!\n": 0.0,
        " > Goodbye and god speed!\n": 1,
        " > Your starting stats are as follows:\n": 0.3,
        f" > [ health: {total_health}, damage: {damage}, shield: {shield}, magic: {magic}, luck: {luck}, name: {name} ]": 0.0,
        "\n > We should now save your character if you want to come back to it later - character file name:\n": 0.0
    }
    print_block(menu_wrap)
    # Ask for the file name
    character_file_name = input('> ')
    # Save the file
    character.save(f"./{character_file_name}.dat")

    return (character, character_file_name)


# ascii art
def mountain_range() -> None:
    print(r"""
                  /\                       /\                        /\                       /\
                 /  \                     /  \                      /  \                     /  \
                /    \   /\      /\      /    \   /\               /    \   /\      /\      /    \   /\
               /      \ /  \    /  \    /      \ /  \             /      \ /  \    /  \    /      \ /  \
              /  /\    /    \  /    \  /  /\    /    \    /\     /  /\    /    \  /    \  /  /\    /    \
             /  /  \  /      \/      \/  /  \  /      \  /  \   /  /  \  /      \/      \/  /  \  /      \
            /  /    \/ /\     \      /  /    \/ /\     \/    \ /  /    \/ /\     \      /  /    \/ /\     \
           /  /      \/  \/\   \    /  /      \/  \/\   \     /  /      \/  \/\   \    /  /      \/  \/\   \
       ___/__/_______/___/__\___\__/__/_______/___/__\___\___/__/_______/___/__\___\__/__/_______/___/__\___\___
    """)


def character_selection_horse_and_knight() -> None:
    print(r"""
                 ,;~;,                                                                ,;;,.
                    /\_                                                              /~\
                   (  /                                                             ([-])
                   (()      //)                                                   ,_.~~~.
                   | \\  ,,;;'\                                                 ()--|   ,\
               __ _(  )m=(((((((((((((================--------               ,_//   |   |>)
              /'  ' '()/~' '.(, |                                         (~'  m''~)(   )/
           ,;(      )||     |  ~                                           \(~||~)/ //~\\
          ,;' \    /-(.;,   )                                                 ||   ()   ()
         ,;'   ) /       ) /                                                  ||   ()   ()
               //         ||                                                  ||   ||   ||
               )_\         )_\                                                || ,;.)   (.;,
        """)


def screen_line() -> None:
    print(' _____________________________________________________________________________________________________________________')


def main_menu(CLEAR_SCREEN: str ='clear') -> str:
    """
    Prints the main menu to the screen so player can choose new game/load game/credits

    Args:
        CLEAR_SCREEN (str, optional): Defaults to 'clear'.

    Returns:
        str: menu option chosen as number
    """
    __version__ = 0.1
    time.sleep(0.5)
    system(CLEAR_SCREEN)
    time.sleep(0.5)
    show_date_and_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    screen_line()
    title1 = "\n  <Adventure Colossus>"
    a = len(title1)
    title2 = f"session: {session_count} | current date: {show_date_and_time} | date of creation: 9.2.2021 | version: {__version__} "
    print(title1 + title2.rjust(118-a, " "))
    screen_line()
    time.sleep(0.5)
    mountain_range()
    screen_line()
    create_load_menu = {
        "> [1] Create new game\n": 0.5,
        "> [2] Load existing game\n": 0.5,
        "> [3] End game\n": 0.5,
        "> [4] Credits\n": 0.5
    }
    print_block(create_load_menu)
    choice = get_input("\n > ", ['1', '2', '3', '4'])
    return choice


def new_character(CLEAR_SCREEN: str ='clear') -> tuple:
    """
    Create new entity object based on player input

    Args:
        CLEAR_SCREEN (str, optional): Defaults to 'clear'.

    Returns:
        tuple: entity:character, string:character_save_file
    """
    print_text(
        "\n > You have chosen to create a new game: Redirecting...", 0.75)
    system(CLEAR_SCREEN)
    screen_line()
    # print('  \n  We will begin with creating your character:                                        Quick tip: Choose wisely')
    line1 = '  \n  We will begin with creating your character:'
    line2 = 'Quick tip: Choose wisely\n'
    print_text(line1 + line2.rjust(118-(len(line1[3:])), " "))
    screen_line()
    time.sleep(0.5)
    character_selection_horse_and_knight()
    screen_line()
    time.sleep(0.3)
    return character_generator()


def load_character(CLEAR_SCREEN: str ='clear') -> tuple:
    """
    Takes input from user and returns pydantic entity object stored
    in the given file

    Args:
        CLEAR_SCREEN (str, optional): [description]. Defaults to 'clear'.

    Returns:
        tuple: entity:character, string:character_save_file
    """
    print_text(
        "\n > You have chosen to load an existing game: Redirecting...", 0.75)
    system(CLEAR_SCREEN)
    time.sleep(0.5)
    screen_line()
    # print('  \n  We will begin with choosing an existing character:                             Quick tip: Make sure it exists!')
    line1 = '  \n  We will begin with choosiNg an existing character:'
    line2 = 'Quick tip: Make sure it exists!\n'
    print_text(line1 + line2.rjust(118-(len(line1[3:])), " "))
    screen_line()
    time.sleep(0.5)
    character_selection_horse_and_knight()
    screen_line()
    character_file_name = input('\n > Character file name: ')
    # The new character load
    character = entities.Human.load(f"./{character_file_name}.dat")
    print(character.__repr__())
    return (character, character_file_name)


if __name__ == '__main__':
    print("I am not supposed to be run directly")
    sys.exit(1)
