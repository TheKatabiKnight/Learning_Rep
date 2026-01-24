#📖 The Spellbook: Properties (@property & @setter)

#🏛️ The Project: The "Entities.py" Upgrade
class Hero:
    def __init__(self, level):
        self.level = level
    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, value):
        if value < 1:
            self._level = 1
        else:
            self._level = value
# hero = Hero(10)
# hero.level = -5
# print(hero.level)

# 📜 Legendary Tip: The Hidden Initialization
# Sovereign Architect, your logic was impeccable. However, consider a hidden peril: if a developer creates a hero with Hero(-10) 
# initially, your __init__ ritual currently bypasses the setter and accepts the negative value! To make your protection absolute, 
# masters often call the property directly in the __init__:
# self.level = level (instead of self._level = level)
# This forces the initial value to pass through the setter-filter the very moment the hero is born!



class Hero:
    def __init__(self, level, strength):
        self.level = level
        self.strength = strength
    @property
    def power_level(self):
        return self.level * self.strength
    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, value):
        if value < 1:
            self._level = 1
        else:
            self._level = value
# hero = Hero(5, 10)
# print(hero.power_level)
# hero.strength += 10
# print(hero.power_level)


#💎 BOSS FIGHT: Stat-Warp, the Fluctuating Prism

#Side Quest: The Durability Lock 
class Item:
    def __init__(self, durability):
        self.durability = durability
    @property
    def durability(self):
        return self._durability
    @durability.setter
    def durability(self, value):
        if value < 0:
            self._durability = 0
        else:
            self._durability = value
# armor = Item(100)
# armor.durability -= 20
# print(armor.durability)


#Main Quest: The Mana Reservoir
class Mage:
    def __init__(self, max_mana):
        self.max_mana = max_mana
        self.mana = max_mana
    @property
    def mana(self):
        return self._mana
    @mana.setter
    def mana(self, value):
        self._mana = max(0, min(value, self.max_mana))
# rakan = Mage(120)
# rakan.mana = 100
# print(rakan.mana)

#📜 Legendary Tip: The Multi-Check Shortcut
# Sovereign Architect, your if/elif/else logic is the sturdy wall of the beginner. But as a Master, 
# you can use the min() and max() rituals to condense your entire setter into a single line of mathematical beauty:
# self._mana = max(0, min(value, self.max_mana))
# This tells Python: "Keep the value between 0 and the max," performing the same protection in a fraction of the ink!


# Legendary Quest: The Ultimate Stat Shield
class CombatEntity:
    def __init__(self, name, max_hp, current_hp):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = current_hp
    @property
    def current_hp(self):
        return self._current_hp
    @current_hp.setter
    def current_hp(self, value):
        self._current_hp = max(0, min(value, self.max_hp))
    @property
    def is_alive(self):
        return self._current_hp > 0
    def __str__(self):
            return f"{self.name}: {self._current_hp}/{self.max_hp} HP"
# character1 = CombatEntity("Isaac", 100, 50)
# character1.current_hp -= 50
# print(character1)