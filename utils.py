from random import randint, choice


class Human:

    # min/max starting values for all classes based Human
    min_health = 220
    max_health = 500
    min_damage = 10
    max_damage = 75

    def __init__(self, name=''):

        # Human should never be instantiated, only inherited.
        # Human starting values zeroed out so they won't interfere with game play.
        self.name = name
        self.current_health = 0
        # self.damage could be a level based multiplier, but it might be unnecessary
        # I added it before I realized there was more than one weapon
        self.damage = 0
        self.luck = randint(1, 10)
        self.total_health = 0
        # items stored in dictionary where key is item and value is quantity
        self.loot = {}
        # weapons stored in dict where key is type and value is damage
        self.weapons = {'Hands': 10}
        self.level = 1
        self.xp = 1

    def __str__(self):
        return self.name

    def add_luck(self, attribute):
        ''' 
        returns character attibute augmented by a percent of character luck as int 
        '''
        percent = round(attribute * (randint(1, self.luck) / 50))
        attribute += percent
        return attribute

    def add_xp(self):
        ''' 
        add xp and check if character has leveled up if leveled_up, add 
        heath to total_health 
        '''
        pass

    def attack(self, weapon, defender):
        ''' 
        reduces another character's health by this character's damage 
        '''
        round_damage = self.add_luck(self.weapons[weapon])
        print(f"{defender.__str__()}'s current health is {defender.current_health}")
        print(f'round damage is {round_damage}')
        if defender.current_health - round_damage <= 0:
            defender.current_health = 0
            # uncomment after method implemented
            # self.add_xp()
            return f"{defender.__str__()} has died."
        else:
            defender.current_health -= round_damage
            return defender.current_health

    def add_health(self, amount):
        ''' 
        restore character health without exceeding current maximum 
        '''
        if self.current_health + amount <= self.total_health:
            self.current_health += amount
        else:
            self.current_health = self.total_health

    def list_items(self):
        print(f'{self.__str__()} has these items:')
        for k, v in self.loot.items():
            print(f'{k.capitalize()}: {v}')

    def add_loot(self, stuff):
        # @TODO dict.setdefault to check if item in self.loot
        pass


class Brawler(Human):

    def __init__(self, name):
        Human.__init__(self, name)  # do brawlers start with bows?
        self.luck = randint(1, 10)
        # start player off with low health so they can level up
        self.total_health = randint(
            (Human.max_health * 0.2), (Human.max_health * 0.4))
        self.add_health(Human.max_health)
        self.weapons['Sword'] = 35
        self.weapons['Hands'] = 20
        self.weapons['Bow'] = 15
        self.word = choice(['Mighty', 'Brave', 'Fierce', 'Stabby'])

    def __str__(self):
        return f'The {self.word} {self.name}'


class Ranger(Human):

    def __init__(self, name):
        Human.__init__(self, name)  # do rangers start with swords?
        self.luck = randint(1, 10)
        # start player off with low health so they can level up
        self.total_health = randint(
            (Human.max_health * 0.2), (Human.max_health * 0.3))
        self.add_health(Human.max_health)
        self.weapons['Sword'] = 15
        self.weapons['Hands'] = 10
        self.weapons['Bow'] = 35
        self.word = choice(['Cunning', 'Wise', 'Resourceful', 'Shooty'])

    def __str__(self):
        return f'{self.name} the {self.word}'


class Zombie(Human):

    def __init__(self):
        Human.__init__(self)
        # give the zombie lots of health
        # @TODO rewrite Zombie init so health is generated based on player level
        self.current_health = randint(
            (Human.max_health * 0.5), (Human.max_health * 0.6))
        self.weapons['Hands'] = 60

    def __str__(self):
        return "A zombie"

    def attack(self):
        ''' 
        @TODO add functionality for zombie attack to be scaled by player level 
        '''
        pass


class Loot():
    pass


class Survivor(Human):
    ''' 
    non combatant humans to trade with or other 
    '''
    pass


# tests
bob = Ranger('Bob')
jim = Brawler('Jim')
print(jim.attack('Hands', bob))
print(bob.attack('Hands', jim))
print(jim.attack('Bow', bob))
print(bob.attack('Sword', jim))
print(jim.attack('Sword', bob))
print(bob.attack('Bow', jim))

z = Zombie()

while z.current_health > 0:
    print(jim.attack('Sword', z))
    print(bob.attack('Bow', z))
