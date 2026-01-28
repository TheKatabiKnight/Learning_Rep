#📖 The Spellbook: Static & Class Methods

#⚔️ Training Grounds: The Version Validator
class GameSystem:
    VERSION = "1.5"
    @staticmethod
    def is_valid_version(version_string):
        if version_string == GameSystem.VERSION:
            return True
        else:
            return False
# print(GameSystem.is_valid_version("1.5"))


#🏛️ The Project: The "Hero Factory"
class Hero:
    def __init__(self, name, level, hp):
        self._name = name
        self._level = level
        self._hp = hp
    @classmethod
    def spawn_beginner(cls, name):
        return cls(name, level=1, hp=100)
    def __str__(self):
        return f"{self._name} Level: {self._level}"
# print(Hero("ClownStar", 10, 500))        
# print(Hero.spawn_beginner("TheKatabiKnight"))


#🗿 BOSS FIGHT: The Monolith of Immutable Laws
#Side Quest: The Combat Calculator
class CombatMath:
    @staticmethod
    def calculate_crit(damage, multiplier):
        return damage * multiplier
# print(CombatMath.calculate_crit(100, 2))


#Main Quest: The Enemy Forge
class Enemy:
    def __init__(self, type, level):
        self._type = type
        self._level = level
    @classmethod
    def spawn_boss(cls, boss_type):
        return cls(boss_type, level=50)
    def __str__(self):
        return f"{self._type} Level: {self._level}"
# print(Enemy.spawn_boss("Behimoth"))
# print(Enemy("Goblin", 2))


# Legendary Quest: The World Configuration
class NexusConfig:
    WORLD_NAME = "The Nexus"
    DIFFICULTY = "Normal"
    @classmethod
    def update_difficulty(cls, new_diff):
        cls.DIFFICULTY = new_diff
        return cls.DIFFICULTY
    @staticmethod
    def format_header(title):
        return f"--- {title} ---"
# NexusConfig.update_difficulty("Easy")
# print(NexusConfig.format_header(NexusConfig.WORLD_NAME))
# NexusConfig.update_difficulty("Hard")
# print(NexusConfig.DIFFICULTY)











