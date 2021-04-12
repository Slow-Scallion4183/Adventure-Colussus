import pytest
import adventure_colussus.entities as ents
from random import seed
import adventure_colussus as ac

seed(20)

collect_ignore = ["setup.py", "tox.ini", "pytest.ini", "tests/",]


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
    yield brawler

@pytest.fixture(scope="class")
def sample_Ranger():
    '''Distance specialist character class'''
    ranger = ents.Ranger.generate("Test_Ranger")
    yield ranger

@pytest.fixture(scope="class")
def sample_Zombie():
    '''Main enemy'''
    zombie = ents.Zombie.generate("Test_Zombie")
    yield zombie

@pytest.fixture(scope="class")
def sample_Survivor():
    '''Neutral? NPC'''
    survivor = ents.Survivor.generate("Test_Survivor")
    yield survivor

@pytest.fixture(scope="module")
def sample_Dict_Brawler():
    character_dict = {'player_style':"Brawler", 'health': 100, 'damage': 50,
                      'shield': 25, 'magic': 30, 'luck': 10, 'name': "dict_Brawler"}
    person_traits = ac.add_player_choices(character_dict)
    yield person_traits

@pytest.fixture(scope="module")
def sample_Dict_Ranger():
    character_dict = {'player_style':"Ranger", 'health': 100, 'damage': 50,
                      'shield': 25, 'magic': 30, 'luck': 10, 'name': "dict_Ranger"}
    person_traits = ac.add_player_choices(character_dict)
    yield person_traits

@pytest.fixture(scope="module")
def sample_Dict_Human():
    character_dict = {'player_style':"Human", 'health': 100, 'damage': 50,
                      'shield': 25, 'magic': 30, 'luck': 10, 'name': "dict_Human"}
    person_traits = ac.add_player_choices(character_dict)
    yield person_traits
    
'''
@ TODO
# make test save file fixure for saving/loading
# make test_session file for get_session_count
'''