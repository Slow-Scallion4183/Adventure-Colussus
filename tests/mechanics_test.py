import json
import adventure_colussus.entities as ents


def main():
    with open("../plots_json/all_quests.json") as jsonfile:
        quests = json.load(jsonfile)

    bob = ents.Brawler("Bob")
    print(bob)
    # ac.print_text("What quest would you like to endeavor today?")
    # for quest in quests:
    #     print("\t" + quests[quest]["name"])

if __name__ == "__main__":
    main()