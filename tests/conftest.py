import pytest
import sys, os


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import adventure_colussus.entities as ents
from random import seed


seed(20)

collect_ignore = ["setup.py", "mechanics_test.py", "utils.py"]


@pytest.fixture(scope="class")
def sample_Item():
    ''' base class for loot objects'''
    item = ents.Item()
    yield item


@pytest.fixture(scope="class")
def sample_Weapon():
    '''base class for player weapons'''
    weapon = ents.Weapon()
    yield weapon


@pytest.fixture(scope="class")
def sample_Entity():
    '''player/enemy base'''
    entity = ents.Entity()
    yield entity


@pytest.fixture(scope="class")
def sample_Attacker():
    '''Human subclass, not actual character'''
    attacker = ents.Human().generate("Attacker")
    attacker.word = "Basic"
    attacker.weapons.append(ents.Weapon(name="Sword", damage=25))
    yield attacker


@pytest.fixture(scope="class")
def sample_Defender():
    '''Human subclass, not actual character'''
    defender = ents.Human().generate("Defender")
    defender.word = "Also Basic"
    yield defender


@pytest.fixture(scope="class")
def sample_Brawler():
    '''Melee specialist character class'''
    brawler = ents.Brawler.generate("Test_Brawler")
    return brawler

@pytest.fixture(scope="class")
def sample_Ranger():
    '''Distance specialist character class'''
    ranger = ents.Ranger.generate("Test_Ranger")
    return ranger

@pytest.fixture(scope="class")
def sample_Zombie():
    '''Main enemy'''
    zombie = ents.Zombie.generate("Test_Zombie")
    return zombie

