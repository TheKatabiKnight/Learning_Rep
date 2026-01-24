#📖 The Spellbook: Dunder Methods

#⚔️ Training Grounds: The Forged Description
# class Item():
#     def __init__(self, name, rarity):
#         self.name = name
#         self.rarity = rarity
#     def __str__(self):
#         return f"{self.rarity} {self.name}"
# new_item = Item("Dragon-Slayer", "Legendary")
# print(new_item)

#🌋 Training Grounds: The Measuring Scale
# class SoulGem():
#     def __init__(self, souls):
#         self.souls = souls
#     def __len__(self):
#         return len(self.souls)
# num_souls = SoulGem(("Ancient Dragon", "Goblin King", "Shadow Wraith"))
# print(len(num_souls))

#🌋 Training Grounds: The Fusion Ritual
# class GoldPouch():
#     def __init__(self, amount):
#         self.amount = amount
#     def __add__(self, other):
#        return GoldPouch(self.amount + other.amount)       
#     def __str__(self):
#         return f"Pouch with {self.amount} gold"
# pouch1 = GoldPouch(50)
# pouch2 = GoldPouch(30)
# total_pouch = pouch1 + pouch2
# print(total_pouch)


#🛡️ BOSS FIGHT: Vulcanos, the Sentinel of the Core

#Main Quest: The Alloy Smelter
# class Metal():
#     def __init__(self, name, purity):
#         self.name = name
#         self.purity = purity
#     def __add__(self, other):
#         return Metal((self.name + other.name), ((self.purity + other.purity)//2))
#     def __str__(self):
#         return f"{self.name} Alloy - Purity: {self.purity}%"
    
# metal1 = Metal("Iron", 80)
# metal2 = Metal("Steel", 90)
# result = metal1 + metal2
# print(result)

# 📜 Legendary Tip: The Average of Integers
# Grand Architect, your calculation of (self.purity + other.purity)/2 resulted in a Float (85.0). 
# In the world of the Under-Forge, if you wish to keep the purity as a solid, whole number, 
# you can use the Floor Division operator //. (80 + 90) // 2 would have returned a sturdy 85 integer!



# Legendary Quest: The Soul-Bound Armor

# class Armor():
#     def __init__(self, part_name, defense_value):
#         self.part_name = part_name
#         self.defense_value = defense_value
#     def __add__(self, second_part):
#         return Armor(f"{self.part_name} & {second_part.part_name} Shell", self.defense_value + second_part.defense_value)
#     def __len__(self):
#         return self.defense_value
#     def __str__(self):
#         return f"Artifact: {self.part_name} (Protection: {self.defense_value})"
    
# armor1 = Armor("Chestplate", 50)
# armor2 = Armor("Pauldrons", 20)
# fused_armor = armor1 + armor2
# print(fused_armor)
# print(len(fused_armor))