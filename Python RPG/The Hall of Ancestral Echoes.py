#Training Grounds: The Hero’s Lineage
# class Character:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

#     def get_status(self):
#         return f"{self.name} has {self.hp} health."
    
# class Mage(Character):
#     def __init__(self, name, hp, mana):
#         super().__init__(name, hp)
#         self.mana = mana

#     def get_status(self):
#         return f"{self.name} has {self.hp} health and {self.mana} mana points."
    
# New_character = Mage("Gandalf", 100, 50)
# print(New_character.get_status())


#Side Quest: The Guard’s Promotion
# class NPC:
#     def __init__(self, name):
#         self.name = name

# class Guard(NPC):
#     def __init__(self, name, rank):
#         super().__init__(name)
#         self.rank = rank

#     def salute(self):
#         return f"I am {self.rank} {self.name}, at your service!"
    
# print(Guard("Valerius", "Commander").salute())


#Main Quest: The Relic Hierarchy
# class Relic:
#     def __init__(self, name, value):
#         self.name = name
#         self.value = value

#     def identify(self):
#         return f"This is the {self.name}, worth {self.value} gold."


# class EnchantedRelic(Relic):
#     def __init__(self, name, value, spell_effect):
#         super().__init__(name, value)
#         self.spell_effect = spell_effect
    
#     def identify(self):
#         return f"This is the {self.name}, worth {self.value} gold. It glows with {self.spell_effect}."
    
# print(EnchantedRelic("Sun-Slayer", 5000, "Holy Fire").identify())


#Side Quest: The Potion Refiner
# class Potion:
#     def __init__(self, heal_amount):
#         self.heal_amount = heal_amount

# class SuperPotion(Potion):
#     def __init__(self, heal_amount, multiplier):
#         super().__init__(heal_amount)
#         self.multiplier = multiplier

#     def get_effective_heal(self):
#         return self.heal_amount * self.multiplier
    
# print(SuperPotion(50, 2).get_effective_heal())


#FINAL BOSS STRIKE: The Combat Simulation
class Ability:
    def __init__(self, name, mana_cost):
        self.name = name
        self.mana_cost = mana_cost

    def can_cast(self, mana_pool):
        if mana_pool >= self.mana_cost:
            return True
        else:
            return False

class HealingSpell(Ability):
    def __init__(self, name, mana_cost, heal_amount):
        super().__init__(name, mana_cost)
        self.heal_amount = heal_amount

    def cast(self, mana_pool):
        if self.can_cast(mana_pool):
            return self.heal_amount
        else:
            return "Not enough mana!"
        
spell = HealingSpell("Greater Heal", 40, 100)
print(spell.cast(50))
print(spell.cast(30))
