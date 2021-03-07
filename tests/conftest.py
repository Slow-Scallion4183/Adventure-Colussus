import pytest
import adventure_colussus.entities as ents
from random import seed


seed(20)


@pytest.fixture(scope="class")
def sample_Item():
    item = ents.Item()
    yield item


@pytest.fixture(scope="class")
def sample_Weapon():
    weapon = ents.Weapon()
    yield weapon


@pytest.fixture(scope="class")
def sample_Entity():
    entity = ents.Entity()
    yield entity


@pytest.fixture(scope="class")
def sample_Attacker():
    attacker = ents.Human().generate("Attacker")
    attacker.word = "Basic"
    attacker.weapons.append(ents.Weapon(name="Sword", damage=25))
    yield attacker


@pytest.fixture(scope="class")
def sample_Defender():
    defender = ents.Human().generate("Defender")
    defender.word = "Also Basic"
    yield defender

# delete
