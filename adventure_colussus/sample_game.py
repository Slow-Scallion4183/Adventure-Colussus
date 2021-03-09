import json
import entities as ents
import utils as ac

def main():
    with open("../plots_json/all_quests.json") as jsonfile:
        quests = json.load(jsonfile)

    # ac.print_text("What quest would you like to endeavor today?"+ "\n")
    print("What quest would you like to endeavor today?"+ "\n")
    filenames = []
    for index, quest in enumerate(quests):
        # ac.print_text("\t" + str(index + 1) + ") " + quests[quest]["name"] + " | " + quests[quest]["description"] + "\n")
        print("\t" + str(index + 1) + ") " + quests[quest]["name"] + " | " + quests[quest]["description"] + "\n")
        filenames.append(quests[quest]["filename"])
    responses = [str(i) for i in range(1, len(quests) +1)]
    answer = ac.get_input(">", responses)
    quest_file = filenames[int(answer)-1]
    print(quest_file)
if __name__ == "__main__":
    main()