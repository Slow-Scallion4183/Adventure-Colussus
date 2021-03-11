import json
import entities as ents
import utils as ac


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


if __name__ == "__main__":
    main()
