import pytest
import adventure_colussus.entities as ents
from random import seed

def pytest_addoption(parser):
    print('conftest method')
    parser.addoption("--mydebug", action = "store_true", help ="change print function")

@pytest.fixture
def get_param(request):
    config_param = {}
    config_param["debug"] = request.config.getoption("--mydebug")
    return config_param

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

'''
@ TODO
# make test save file fixure for saving/loading
# make test_session file for get_session_count
'''