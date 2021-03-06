import adventure_colussus.entities as ents
import pytest
from random import randint, seed


"""
Item Tests: I'm not sure how necessary these are, but I need to practice
testing and having 100% coverage is never a bad idea, so here they are.
"""


@pytest.fixture(scope="module")
def sample_Item():
    item = ents.Item()
    yield item


def test_Item(sample_Item):
    assert type(sample_Item) == ents.Item


def test_Item_name(sample_Item):
    assert sample_Item.name == 'item'


"""
Weapons Tests: I'm not sure how necessary these are, but I need to practice
testing and having 100% coverage is never a bad idea, so here they are.
"""


@pytest.fixture(scope="module")
def sample_Weapon():
    weapon = ents.Weapon()
    yield weapon


def test_Weapon(sample_Weapon):
    assert type(sample_Weapon) == ents.Weapon


def test_Weapon_name(sample_Weapon):
    assert sample_Weapon.name == 'weapon'


def test_Weapon_damage(sample_Weapon):
    assert sample_Weapon.damage == 0


"""
Entity Attribute Tests: I'm not sure how necessary these are, but I need to practice
testing and having 100% coverage is never a bad idea, so here they are.
"""


@pytest.fixture(scope="module")
def sample_Entity():
    entity = ents.Entity()
    yield entity


def test_Entity(sample_Entity):
    assert type(sample_Entity) == ents.Entity


def test_Entity_name(sample_Entity):
    assert sample_Entity.name == 'Ent'


def test_Entity_current_health(sample_Entity):
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


# __str__


def test_Entity_base_str(sample_Entity):
    assert sample_Entity.__str__() == "Ent"


def test_Entity_no_name(sample_Entity):
    sample_Entity.name = ""
    assert sample_Entity.__str__() == "Entity"


def test_Entity_new_name(sample_Entity):
    sample_Entity.name = "Bob"
    assert sample_Entity.__str__() == "Bob"


def test_Entity_new_word(sample_Entity):
    sample_Entity.word = "Mighty"
    assert sample_Entity.__str__() == "The Mighty Bob"


# __repr__


def test_Entity_repr(sample_Entity):
    assert sample_Entity.__repr__() == "<Bob hp=0 lvl=1>"


def test_Entity_repr_new_stats(sample_Entity):
    sample_Entity.current_health = 100
    sample_Entity.level = 100
    assert sample_Entity.__repr__() == "<Bob hp=100 lvl=100>"


# calculate_luck

def test_calc_luck(sample_Entity):
    seed(20)
    sample_Entity.damage = 10
    sample_Entity.luck = 10
    amount = sample_Entity.calculate_luck(sample_Entity.damage)
    assert amount == 11

# add_xp


def test_add_xp(sample_Entity):
    pass


def test_attack(sample_Entity):
    pass


def test_iattack(sample_Entity):
    pass


# spacer


# spacer
