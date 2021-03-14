from sys import exit
import json
# import entities as ents
# import utils as ac
import typing
import time

from adventure_colussus import print_text, get_input

def load_quest():
    with open("./plots_json/all_quests.json") as jsonfile:
        quests = json.load(jsonfile)

    # ac.print_text("What quest would you like to endeavor today?" + "\n")
    print("What quest would you like to endeavor today?" + "\n")
    filenames = []
    for index, option in enumerate(quests):
        print_text("\t" + str(index + 1) + ") " +
                      quests[option]["name"] + " | " + quests[option]["description"] + "\n")
        # print("\t" + str(index + 1) + ") " +
        #   quests[option]["name"] + " | " + quests[option]["description"] + "\n")
        filenames.append(quests[option]["filename"])
    responses = [str(i) for i in range(1, len(quests) + 1)]
    answer = get_input(">", responses)
    quest_file = filenames[int(answer)-1]
    with open(quest_file) as qf:
        quest = json.load(qf)
    # print_question(quest["one"], quest)
    return quest


def print_question(question, quest):
    # print(question["ask"])
    print_text(question["ask"] + "\n")
    for index, option in enumerate(question["options"]):
        print_text(f"{index + 1}: {option}\n")
    responses = [str(i) for i in range(1, len(question["options"]) + 1)]
    # answer = input(">")
    answer = get_input(">", responses)
    user_choice = question["next"][(question["options"][int(answer) - 1])]
    while user_choice != "Null":
        return print_question(quest[user_choice], quest)
    # print("You have reached the end of your quest.")
    print_text("You have reached the end of your quest.\n")
    return 0



if __name__ == "__main__":
    load_quest()