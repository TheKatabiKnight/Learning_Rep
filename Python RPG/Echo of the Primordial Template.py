#📖 The Spellbook: Abstract Base Classes (ABCs)

#⚔️ Training Grounds: The Mandatory Maneuver
from abc import ABC, abstractmethod
class Creature(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Slime(Creature):
    def make_sound(self):
        return "Bloop!"
# slime = Slime()
# print(slime.make_sound())

#📜 Legendary Tip: The Partial Blueprint
# Grand Sovereign, your abstract method was a perfect "Mandate of Silence" (using pass). 
# But remember: an Abstract Method can actually contain code! If there is a "Default Behavior" that most creatures share, 
# you can write it inside the abstract method and then call it using super().make_sound() inside the child class. 
# It is the art of the Shared Foundation.

#🏛️ The Project: The entities.py Foundation
class BaseEntity(ABC):
    @abstractmethod
    def perform_action(self):
        pass
class NPC(BaseEntity):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def perform_action(self):
        return f"{self.name} waves at you."
# elara = NPC("Elara")
# print(elara.perform_action())

#🌌 BOSS FIGHT: Logos, the Formless Primordial

#Side Quest: The Law of the Cry 
class Combatant(ABC):
    @abstractmethod
    def battle_cry(self):
        pass
class Warrior(Combatant):
    def battle_cry(self):
        return "For the Nexus!"
# Alex = Warrior()
# print(Alex.battle_cry())


#Main Quest: The Gear Mandate
class Equippable(ABC):
    @abstractmethod
    def get_defense(self):
        pass
    @abstractmethod
    def get_weight(self):
        pass
class Shield(Equippable):
    def get_defense(self):
        return 20
    def get_weight(self):
        return 15
    

#Legendary Quest: The Heroic Prototype
class BaseHero(ABC):
    @abstractmethod
    def unique_ability(self):
        pass
    @abstractmethod
    def get_role(self):
        pass
    def introduce(self):
        return f"I am {self.name}, the {self.get_role()}."
class Mage(BaseHero):
    def __init__(self, name):
        self.name = name
    def unique_ability(self):
        return "Casts Fireball"
    def get_role(self):
        return "Mage"
# Gandalf = Mage("Gandalf")
# print(Gandalf.introduce())
# print(Gandalf.unique_ability())
    