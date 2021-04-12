"""
    This file contains updated and revised
    classes for all Entities
"""

# We want to import pydantic for the classes
import pydantic

# Get a backwards compatible Dict and List typehints
from typing import Dict, List

# Randomization stuff
from random import randint, choice

# JSON for saving entities
import json


class Item(pydantic.BaseModel):
    """
        This represents an item in an inventory.
    """

    # The item name
    name: str = "item"


class Weapon(pydantic.BaseModel):
    """
        This represents a weapon.
    """

    # The weapon name
    name: str = "weapon"

    # The weapon damage
    damage: int = 0


class Entity(pydantic.BaseModel):
    """
        This is the base class for all entities.
        Entities can all attack, be damaged, be killed, etc.
        Entities can also be saved for loading later.

        All Characters, Monsters, NPCs, etc. are all Entities
    """

    # Entities have a default minimum and maximum health
    # Starting values.
    # NOTE These are default values. Subclasses will define their own values
    min_health: int = 220  # Minimum 220 starting value
    max_health: int = 500  # Maximum of 500

    # NOTE Maybe replace these with a strength system?
    min_damage: int = 10  # Minimum of 10
    max_damage: int = 75  # Maximum of 75

    # This is a multiplier used when generating health
    health_mult_1: int = 1
    health_mult_2: int = 1

    # The name of the entity.
    name: str = "Entity"

    # The current health of the entity defaults to zero.
    current_health: int = 0

    # Luck defaults to zero. Generate at character initialization time.
    luck: int = 0

    # Your characters total health
    total_health: int = 0

    # NOTE Renaming loot to inventory. Keeps consistency with most other games
    #   Loot should be specific to things like rooms, chests, etc.
    inventory: Dict[Item, int] = dict()

    # Weapons is now just a list of weapon classes
    weapons: List[Weapon] = [[]]

    # Starting weapons is the weapons this Entity starts with
    # A random list can be chosen from this
    default_weapons: List[List[Weapon]] = []

    # Entities also have a level, so that their difficulty
    # can be scaled to the player.
    level: int = 1

    # Same with xp
    xp: int = 1

    # We also want our describing word
    word: str = ""

    # And a choice of words
    word_choice: List[str] = [""]

    # Sheild
    shield: int = 0

    # Magic
    magic: int = 0

    # Damage
    # NOTE Keeping this here for now
    damage: int = 0

    def __str__(self):
        """
            Gets the entity as a string.
            This returns the entity name
        """
        return f'{f"The {self.word} " if self.word.strip() != "" else ""}{self.name if self.name.strip() != "" else self.__class__.__name__}'

    def __repr__(self):
        """
            Returns a representation of the entity
        """
        return f"<{self.__class__.__name__} {self.name} hp={self.current_health} lvl={self.level}>"

    def calculate_luck(self, value):
        """
            This function auguments the provided value by the entity's luck
        """

        percent = round(value * (randint(1, self.luck) / 50))

        value += percent

        return value

    def add_xp(self):
        """
            Add xp and level up accordingly. If it has leveled up, add health to total_health
        """
        return "Once implemented testing will fail."

    def attack(self, weapon: int, defender):
        """
            This is the front facing function for _attack
        """
        attk = self._attack(weapon, defender)

        return f"{str(defender)} has died." if attk else defender.current_health

    def _attack(self, weapon: int, defender):
        """
            Internal function
            Attacks another player using this player's weapon.
        """

        # Calculate damage
        round_damage = self.calculate_luck(
            self.weapons[weapon].damage
        )

        print(
            f"{str(defender)}'s current health is {defender.current_health}"
        )

        print(
            f"damage for this round is {round_damage}"
        )

        # Damage the defender
        defender.deal_damage(round_damage)

        # Return True if the attack killed the defender, false if it did not
        return defender.current_health <= 0

    def deal_damage(self, damage):
        """
            Deals damage to this entity.
        """
        # Another cool trick
        self.current_health = max(
            0,
            self.current_health-damage
        )

    def add_health(self, ammount: int):
        """
            Add health to a character with out exceeding total
        """
        # A cool trick to do this fast
        self.current_health = min(
            self.current_health+ammount,
            self.total_health
        )

    def give(self, item: Item, count: int):
        """
            NOTE I assume this is to give items to the entity
            This should add an item to the inventory, I assume
        """
        return "Once implemented testing will fail."

    def save(self, file):
        """
            Saves the entity to the selected file
        """
        with open(file, "w+") as f:
            json.dump(self.dict(), f)

    @classmethod
    def load(cls, file):
        """
            Loads a Entity from a file
        """
        with open(file, "r") as f:
            j = json.load(f)
            return cls(**j)

    @classmethod
    def generate(cls, name=''):
        """
            Generates a default Entity
        """
        # Create the class
        self = cls()

        # Name
        self.name = name

        # Generate luck
        self.luck = randint(1, 10)

        # Total health
        self.total_health = randint(
            (self.max_health * self.health_mult_1),
            (self.max_health * self.health_mult_2)
        )

        # Max our health out
        self.add_health(self.max_health)

        # Add default weapons
        self.weapons = choice(self.default_weapons)

        # Set our describing word
        self.word = choice(self.word_choice)

        # Inventory should be empty
        self.inventory = dict()

        # Level and xp
        self.level = 1
        self.xp = 1

        return self


class Human(Entity):
    """
        A basic human class. All humans are based off of this.
    """
    # NOTE Entity is already modeled around a human
    #   No need to change much
    default_weapons: List[List[Weapon]] = [[
        Weapon(name="Hands", damage=10),
    ]]


class Brawler(Human):
    """
        Brawler human subclass
    """
    default_weapons: List[List[Weapon]] = [[
        Weapon(name="Sword", damage=35),
        Weapon(name="Hands", damage=20),
        Weapon(name="Bow", damage=15)
    ]]

    word_choice: List[str] = [
        "Mighty",
        "Brave",
        "Fierce",
        "Stabby"
    ]

    health_mult_1: int = 0.2
    health_mult_2: int = 0.4


class Ranger(Human):
    """
        Ranger human subclass
    """

    default_weapons: List[List[Weapon]] = [[
        Weapon(name="Sword", damage=15),
        Weapon(name="Hands", damage=10),
        Weapon(name="Bow", damage=35)
    ]]

    word_choice: List[str] = [
        "Cunning",
        "Wise",
        "Resourceful",
        "Shooty"
    ]

    health_mult_1: int = 0.2
    health_mult_2: int = 0.3

    def __str__(self):
        return f'{self.name if self.name.strip() != "" else self.__class__.__name__}{f" the {self.word}" if self.word.strip() != "" else ""}'


class Zombie(Human):
    """
        The zombie human subclass.
    """

    default_weapons: List[List[Weapon]] = [[
        Weapon(name="Hands", damage=60)
    ]]

    health_mult_1: int = 0.5
    health_mult_2: int = 0.6


class Survivor(Human):
    """
        Non combatant humans to trade with or other 
    """
    pass
