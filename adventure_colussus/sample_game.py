from sys import exit
import json
import entities as ents
import utils as ac
import typing
import time

def main():
    with open("../plots_json/all_quests.json") as jsonfile:
        quests = json.load(jsonfile)

    # ac.print_text("What quest would you like to endeavor today?" + "\n")
    print("What quest would you like to endeavor today?" + "\n")
    filenames = []
    for index, option in enumerate(quests):
        # ac.print_text("\t" + str(index + 1) + ") " + quests[quest]["name"] + " | " + quests[quest]["description"] + "\n")
        print("\t" + str(index + 1) + ") " +
              quests[option]["name"] + " | " + quests[option]["description"] + "\n")
        filenames.append(quests[option]["filename"])
    responses = [str(i) for i in range(1, len(quests) + 1)]
    answer = ac.get_input(">", responses)
    quest_file = filenames[int(answer)-1]
    # quest_file = "../plots_json/" + quest_file
    # print(quest_file + "\n" + str(type(quest_file)))
    with open(quest_file) as qf:
        quest = json.load(qf)
    userchoice = print_question(quest["one"], quest)
    # while userchoice != "Null":
    #     print_question(quest[userchoice], quest)


def print_question(question, quest):
    print(question["ask"])
    for index, option in enumerate(question["options"]):
        print(f"{index}: {option}")
    test = input(">")
    user_choice = [int(test)]
    # user_choice = quest[question]["options"][int(test)]
    # user_choice = quest[question]["next"][(quest[question]["options"][int(test)])]
    print(f"{quest[question]}")
    # while test != "Null":
    #     return print_question(quest[test], quest)
    # return "You have reached the end of your quest."
    # return "twoa"


def print_block(lines: dict) -> None:
    """ takes dictionary where
    keys: string to print
    values: float wait time"""
    for key in lines.keys():
        ac.print_text(key, lines[key])

def character_generator():
    """
    Generates a character determined by user input and saves it in
    a pickle database.
    """
    character_style_menu = {
        "\n > We have reached the first crucial part of your journey: We must choose the path that you will take! The decision\n": 0.5,
        " > is up to you my friend! Whether you choose to be a bloodthirsty warrior or a cunning and strategic fighter,\n" : 0.8,
        " > the choice is up to you!\n": 0.5,
        "\n > Now then, lets get right into it!": 0.8,
        " Are you more of a tanky player[1] or a strategic player[2]?": 0.0
    }
    print_block(character_style_menu)
    player_t_choice_1 = ac.get_input('\n > ', ['1', '2'])
    # player_t_choice_1 = get_input('\n > ', ['1', '2'])

    if player_t_choice_1 == '1':
        health = 100
        damage = 75

    elif player_t_choice_1 == '2':
        health = 75
        damage = 50

    attack_style_menu = {
        "\n > So, we have that out of the way, Let's carry on! ": 0.8,
        "Oh of course! Sorry to forget! Another quick question: ": 0.5,
        "Do you like \n": 0.5,
        " > to use magic from great distances[1] or run in to the thick of battle wielding a deadly blade[2]?\n": 0.5,
    }
    print_block(attack_style_menu)
    player_t_choice_2 = ac.get_input('\n > ', ['1', '2'])
    # player_t_choice_2 = get_input('\n > ', ['1', '2'])

    if player_t_choice_2 == '1':
        player = ents.Brawler.generate()
        # shield = 50
        # magic = 75

    elif player_t_choice_2 == '2':
        player = ents.Ranger.generate()
        # shield = 75
        # magic = 45

    #luck
    luck_menu = {
        "\n > Good good! We have decided your play style and your preferred ways of attacking the enemy!\n": 0.5,
        " > Now, we must see what luck we are able to bestow upon you. Be warned: it is entirely random!\n": 0.8
    }
    print_block(luck_menu)


    # Do we keep this now that luck is part of Entity.generate()
    input('\n > Press enter to roll a dice...')
    time.sleep(0.3)
    ac.print_text(' > Rolling dice...\n')
    # print_text(' > Rolling dice...\n')
    time.sleep(1)
    ac.print_text(f' > Your hero has {player.luck} luck out of 10!\n', 0.8)
    # print_text(f' > Your hero has {player.luck} luck out of 10!\n', 0.8)
    
    #name
    name_menu = {
        "\n > At last! We have reached the most important part of creating your character! The naming!\n": 0.0,
        " > Choose wisely my friend. Your hero will be named this for the rest of their lives...\n": 1,
        "\n > What should your hero be named?\n": 0.0
    }
    print_block(name_menu)

    name = ''
    while not name:
        name = input(' > ')
    player.name = name

    time.sleep(1)
    menu_wrap = {
        f"\n > Welcome mighty hero! You shall henceforth be known as: {player.name} !!!\n ": 0.3,
        "> A perfect choice!\n": 0.0,
        " \n > Now then. I guess you should be on your way! You have a journey to start and a belly to fill!\n": 0.0
    }
    print_block(menu_wrap)

    return player

'''
    # Should Implement The Script And Story From Here.

    # Generate an initial character
    character = entities.Human.generate(name)

    # Update the character
    character = entities.Human(**(dict(character) | character_dict))

    # Ask for the file name
    character_file_name = input('> ')
    # Save the file
    character.save(f"./{character_file_name}.dat")

character_dict = {'health': health, 'damage': damage,
                    'shield': shield, 'magic': magic, 'luck': luck, 'name': name}

'''

def end_game(player=None) -> None:
    if player == None:
        ac.print_text("Thanks for playing", 0.5)
        exit(0)

    health = player.current_health
    #return most powerful weapon
    damage = max([arm.damage for arm in player.weapons])
    shield =  player.shield
    magic = player.magic
    luck = player.luck
    name = player.name
    end_text = {
        " > I have to say, I have rather enjoyed your company! Feel free to come by at any time!\n": 0.0,
        " > Goodbye and god speed!\n": 1,
        " > Your final stats are as follows:\n": 0.3,
        f" > [ health: {health}, damage: {damage}, shield: {shield}, magic: {magic}, luck: {luck}, name: {name} ]": 0.0,
        "\n > We should now save your character if you want to come back to it later - character file name:\n": 0.0
    }
    print_block(end_text)


if __name__ == "__main__":
    player = character_generator()   
    print("ending game" + ("\n" * 5))
    end_game(player)


#new branch edit 