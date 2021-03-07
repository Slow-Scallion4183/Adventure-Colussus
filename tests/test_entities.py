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
        assert sample_Entity.__repr__() == "<Entity hp=0 lvl=1>"

    def test_Entity_repr_new_stats(self, sample_Entity):
        sample_Entity.current_health = 100
        sample_Entity.level = 100
        assert sample_Entity.__repr__() == "<Entity hp=100 lvl=100>"


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


class Test_Human_Combat():

    def test_attack(self, sample_Attacker, sample_Defender):
        assert sample_Attacker.attack(0, sample_Defender) == 490

    def test_iattack(self, sample_Attacker, sample_Defender):
        assert sample_Attacker._attack(0, sample_Defender) == False

    def test_deal_damage(self, sample_Defender):
        assert sample_Defender.current_health == 480

# spacer


# spacer
