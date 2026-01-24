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
hero = Hero(5, 10)
print(hero.power_level)
hero.strength += 10
print(hero.power_level)