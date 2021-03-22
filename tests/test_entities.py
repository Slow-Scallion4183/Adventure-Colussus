import adventure_colussus.entities as ents
import pytest
from random import randint, seed

"""
Item Tests: I'm not sure how necessary these are, but I need to practice
testing and having 100% coverage is never a bad idea, so here they are.
"""


class Test_Item():

    def test_Item_generate(self, sample_Item):
        assert type(sample_Item) == ents.Item

    def test_Item_name(self, sample_Item):
        assert sample_Item.name == 'item'


"""
Weapons Tests: I'm not sure how necessary these are, but I need to practice
testing and having 100% coverage is never a bad idea, so here they are.
"""


class Test_Weapon():

    def test_Weapon_generate(self, sample_Weapon):
        assert type(sample_Weapon) == ents.Weapon

    def test_Weapon_name(self, sample_Weapon):
        assert sample_Weapon.name == 'weapon'

    def test_Weapon_damage(self, sample_Weapon):
        assert sample_Weapon.damage == 0


"""
Entity Attribute Tests: I'm not sure how necessary these are, but I need to practice
testing and having 100% coverage is never a bad idea, so here they are.
"""


class Test_Entity_base():

    def test_Entity_generate(self, sample_Entity):
        assert type(sample_Entity) == ents.Entity

    def test_Entity_name(self, sample_Entity):
        assert sample_Entity.name == 'Entity'

    def test_Entity_current_health(self, sample_Entity):
        assert sample_Entity.damage == 0


""" 
Should I keep going like this, or would it be smarter to test all attributes
at once since it's just testing object generation? Most of the tutorials
I've seen suggest to limit your tests to one assert, but this seems excessive, 
especially for a base class.
"""


"""
Entity Method Tests: This is where it starts to get interesting.
"""


class Test_Entity_str():

    def test_Entity_base_str(self, sample_Entity):
        assert sample_Entity.__str__() == "Entity"

    def test_Entity_no_name(self, sample_Entity):
        sample_Entity.name = ""
        assert sample_Entity.__str__() == "Entity"

    def test_Entity_new_name(self, sample_Entity):
        sample_Entity.name = "Bob"
        assert sample_Entity.__str__() == "Bob"

    def test_Entity_new_word(self, sample_Entity):
        sample_Entity.word = "Mighty"
        assert sample_Entity.__str__() == "The Mighty Bob"


class Test_Entity_repr():

    def test_Entity_repr(self, sample_Entity):
        assert sample_Entity.__repr__() == "<Entity Entity hp=0 lvl=1>"

    def test_Entity_repr_new_stats(self, sample_Entity):
        sample_Entity.current_health = 100
        sample_Entity.level = 100
        assert sample_Entity.__repr__() == "<Entity Entity hp=100 lvl=100>"


class Test_Entity_Calculate_Luck():

    def test_calc_luck(self, sample_Entity):
        seed(20)
        sample_Entity.damage = 10
        sample_Entity.luck = 10
        amount = sample_Entity.calculate_luck(sample_Entity.damage)
        assert amount == 11


class Test_Entity_XP():

    def test_add_xp(self, sample_Entity):
        pass


class Test_Entity_add_health():

    def test_add_health(self, sample_Entity):
        sample_Entity.add_health(10)
        assert sample_Entity.current_health == 0


""" 
Human tests 
"""


class Test_Human_Combat():

    def test_default_weapons_hands(self, sample_Attacker):
        assert sample_Attacker.weapons[0].name == "Hands"
        assert sample_Attacker.weapons[0].damage == 10

    def test_default_weapons_sword(self, sample_Attacker):
        assert sample_Attacker.weapons[1].name == "Sword"
        assert sample_Attacker.weapons[1].damage == 25

    def test_attack(self, sample_Attacker, sample_Defender):
        assert sample_Attacker.attack(0, sample_Defender) == 490

    def test_iattack(self, sample_Attacker, sample_Defender):
        assert sample_Attacker._attack(0, sample_Defender) == False

    def test_deal_damage(self, sample_Defender):
        assert sample_Defender.current_health == 480

    def test_attack_dialogue(self, sample_Attacker, sample_Defender):
        sample_Defender.current_health = 5
        result = sample_Attacker.attack(0, sample_Defender)
        assert result == f"{sample_Defender.__str__()} has died."


class Test_Brawler_():

    def test_Brawler_generate(self, sample_Brawler):
        assert type(sample_Brawler) == ents.Brawler

    def test_Brawler_name(self, sample_Brawler):
        assert sample_Brawler.name == "Test_Brawler"

    def test_Brawler_current_health(self, sample_Brawler):
        assert sample_Brawler.current_health == 174


"""
Brawler Method Tests: This is where it starts to get interesting.
"""


class Test_Brawler_str():

    def test_Brawler_base_str(self, sample_Brawler):
        assert sample_Brawler.__str__() == "The Fierce Test_Brawler"

    def test_Brawler_no_name(self, sample_Brawler):
        sample_Brawler.name = ""
        assert sample_Brawler.__str__() == "The Fierce Brawler"

    def test_Brawler_no_name_no_word(self, sample_Brawler):
        sample_Brawler.word = ""
        assert sample_Brawler.__str__() == "Brawler"


class Test_Brawler_repr():

    def test_Brawler_repr(self, sample_Brawler):
        assert sample_Brawler.__repr__() == "<Brawler Test_Brawler hp=154 lvl=1>"

    def test_Brawler_repr_new_stats(self, sample_Brawler):
        # sample_Brawler.current_health = 100
        sample_Brawler.level = 100
        assert sample_Brawler.__repr__() == "<Brawler Test_Brawler hp=154 lvl=100>"


class Test_Brawler_Calculate_Luck():

    def test_calc_luck(self, sample_Brawler):
        seed(20)
        sample_Brawler.damage = 10
        sample_Brawler.luck = 10
        amount = sample_Brawler.calculate_luck(sample_Brawler.damage)
        assert amount == 11


class Test_Brawler_XP():

    def test_add_xp(self, sample_Brawler):
        pass


class Test_Brawler_add_health():

    def test_add_health(self, sample_Brawler):
        sample_Brawler.add_health(10)
        assert sample_Brawler.current_health == 121


""" 
Brawler Combat tests 
"""


class Test_Brawler_Combat():

    def test_default_weapons_sword(self, sample_Brawler):
        assert sample_Brawler.weapons[0].name == "Sword"
        assert sample_Brawler.weapons[0].damage == 35

    def test_default_weapons_hands(self, sample_Brawler):
        assert sample_Brawler.weapons[1].name == "Hands"
        assert sample_Brawler.weapons[1].damage == 20

    def test_default_weapons_bow(self, sample_Brawler):
        assert sample_Brawler.weapons[2].name == "Bow"
        assert sample_Brawler.weapons[2].damage == 15

    def test_attack(self, sample_Brawler, sample_Defender):
        assert sample_Brawler.attack(0, sample_Defender) == 464

    def test_iattack(self, sample_Brawler, sample_Defender):
        assert sample_Brawler._attack(0, sample_Defender) == False

    def test_deal_damage(self, sample_Defender):
        assert sample_Defender.current_health == 428

    def test_attack_dialogue(self, sample_Brawler, sample_Defender):
        sample_Defender.current_health = 5
        result = sample_Brawler.attack(0, sample_Defender)
        assert result == f"{sample_Defender.__str__()} has died."


class Test_Ranger():
    pass


class Test_Zombie():
    pass


# spacer


# spacer
