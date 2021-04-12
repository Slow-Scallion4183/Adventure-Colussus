import adventure_colussus.entities as ents
import pytest
from random import randint, seed
from mock import patch, MagicMock, mock_open
import io

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
        response = sample_Entity.add_xp()
        assert response == "Once implemented testing will fail."


class Test_Entity_add_health():

    def test_add_health(self, sample_Entity):
        sample_Entity.add_health(10)
        assert sample_Entity.current_health == 0


class Test_Entity_give():
    def test_give(self, sample_Entity):
        # pass
        response = sample_Entity.give('a', 2)
        assert response == "Once implemented testing will fail."


class Test_Entity_save():

    def test_Entity_save_file(self, sample_Entity):
        open_name = f'{__name__}.open'     
        with patch(open_name, create=True) as mock_open:
            mock_open.return_value = MagicMock(spec=io.IOBase)
            with open('/some/path', 'w') as f:
                f.write('something')
        file_handle = mock_open.return_value.__enter__.return_value
        # assert file_handle == 'something'
        file_handle.write.assert_called_with('something')
'''
<mock.Mock object at 0x...>
>>> file_handle = mock_open.return_value.__enter__.return_value
>>> file_handle.write.assert_called_with('something')
'''


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
        response = sample_Brawler.add_xp()
        assert response == "Once implemented testing will fail."


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


class Test_Ranger_():

    def test_Ranger_generate(self, sample_Ranger):
        assert type(sample_Ranger) == ents.Ranger

    def test_Ranger_name(self, sample_Ranger):
        assert sample_Ranger.name == "Test_Ranger"

    def test_Ranger_current_health(self, sample_Ranger):
        assert sample_Ranger.current_health == 121


class Test_Ranger_str():

    def test_Ranger_base_str(self, sample_Ranger):
        assert sample_Ranger.__str__() == "Test_Ranger the Cunning"

    def test_Ranger_no_name(self, sample_Ranger):
        sample_Ranger.name = ""
        assert sample_Ranger.__str__() == "Ranger the Cunning"

    def test_Ranger_no_name_no_word(self, sample_Ranger):
        sample_Ranger.word = ""
        assert sample_Ranger.__str__() == "Ranger"


class Test_Ranger_repr():

    def test_Ranger_repr(self, sample_Ranger):
        assert sample_Ranger.__repr__() == "<Ranger Test_Ranger hp=136 lvl=1>"

    def test_Ranger_repr_new_stats(self, sample_Ranger):
        sample_Ranger.level = 100
        assert sample_Ranger.__repr__() == "<Ranger Test_Ranger hp=136 lvl=100>"

class Test_Ranger_XP():

    def test_add_xp(self, sample_Ranger):
        response = sample_Ranger.add_xp()
        assert response == "Once implemented testing will fail."


class Test_Ranger_Combat():

    def test_default_weapons_sword(self, sample_Ranger):
        assert sample_Ranger.weapons[0].name == "Sword"
        assert sample_Ranger.weapons[0].damage == 15

    def test_default_weapons_hands(self, sample_Ranger):
        assert sample_Ranger.weapons[1].name == "Hands"
        assert sample_Ranger.weapons[1].damage == 10

    def test_default_weapons_bow(self, sample_Ranger):
        assert sample_Ranger.weapons[2].name == "Bow"
        assert sample_Ranger.weapons[2].damage == 35

    def test_attack(self, sample_Ranger, sample_Defender):
        assert sample_Ranger.attack(0, sample_Defender) == 484

    def test_iattack(self, sample_Ranger, sample_Defender):
        assert sample_Ranger._attack(0, sample_Defender) == False

    def test_deal_damage(self, sample_Defender):
        assert sample_Defender.current_health == 469

    def test_attack_dialogue(self, sample_Ranger, sample_Defender):
        sample_Defender.current_health = 5
        result = sample_Ranger.attack(0, sample_Defender)
        assert result == f"{sample_Defender.__str__()} has died."



class Test_Zombie_():

    def test_Zombie_generate(self, sample_Zombie):
        assert type(sample_Zombie) == ents.Zombie

    def test_Zombie_name(self, sample_Zombie):
        assert sample_Zombie.name == "Test_Zombie"

    def test_Zombie_current_health(self, sample_Zombie):
        assert sample_Zombie.current_health == 295


class Test_Zombie_str():

    def test_Zombie_base_str(self, sample_Zombie):
        assert sample_Zombie.__str__() == "Test_Zombie"

    def test_Zombie_no_name(self, sample_Zombie):
        sample_Zombie.name = ""
        assert sample_Zombie.__str__() == "Zombie"

    def test_Zombie_no_name_no_word(self, sample_Zombie):
        sample_Zombie.word = ""
        assert sample_Zombie.__str__() == "Zombie"


class Test_Zombie_repr():

    def test_Zombie_repr(self, sample_Zombie):
        assert sample_Zombie.__repr__() == "<Zombie Test_Zombie hp=269 lvl=1>"

    def test_Zombie_repr_new_stats(self, sample_Zombie):
        sample_Zombie.level = 100
        assert sample_Zombie.__repr__() == "<Zombie Test_Zombie hp=269 lvl=100>"


class Test_Zombie_Combat():

    def test_default_weapons_hands(self, sample_Zombie):
        assert sample_Zombie.weapons[0].name == "Hands"
        assert sample_Zombie.weapons[0].damage == 60

    def test_attack(self, sample_Zombie, sample_Defender):
        assert sample_Zombie.attack(0, sample_Defender) == 435

    def test_iattack(self, sample_Zombie, sample_Defender):
        assert sample_Zombie._attack(0, sample_Defender) == False

    def test_deal_damage(self, sample_Defender):
        assert sample_Defender.current_health == 368

    def test_attack_dialogue(self, sample_Zombie, sample_Defender):
        sample_Defender.current_health = 5
        result = sample_Zombie.attack(0, sample_Defender)
        assert result == f"{sample_Defender.__str__()} has died."

class Test_Survivor():

    def test_Survivor_generate(self, sample_Survivor):
        assert type(sample_Survivor) == ents.Survivor

    def test_Survivor_name(self, sample_Survivor):
        assert sample_Survivor.name == "Test_Survivor"
