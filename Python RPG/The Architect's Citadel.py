#Training Grounds: The Hero's Forge

# class NPC:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role

#     def introduce(self):
#         return f"I am {self.name}, the {self.role}."
# introduction = NPC("Elara", "Blacksmith")
# print(introduction.introduce())

#Training Grounds: The Living Blueprint
# class Hero:
#     def __init__(self, name, max_hp):
#         self.name = name
#         self.max_hp = max_hp
#         self.current_hp = max_hp

#     def take_damage(self, amount):
#         self.current_hp -= amount
#         if self.current_hp < 0:
#             self.current_hp = 0
#         print(self.current_hp)
    
#     def is_conscious(self):
#         if self.current_hp > 0:
#             return True
#         else:
#             return False
        
# Hero_name = Hero("Arthur", 100)
# Hero_name.take_damage(30)
# print(Hero_name.is_conscious())

#BOSS FIGHT: The Monolith of Measurement
class Vault:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.items = []
        self.sum_of_weights = 0

    def get_total_weight(self):
        return sum(item["weight"] for item in self.items)
    
    def add_item(self, item_name, weight):
        if sum(item["weight"] for item in self.items) + weight > 500:
            return "Vault full!"
        else:
            self.items.append({"name": item_name, "weight": weight})
            
Owner = Vault("Master Raven")
Owner.add_item("Golden Statue", 300)
Owner.add_item("Iron Chest", 150)
print(Owner.add_item("Giant Anchor", 100))
print(Owner.get_total_weight())


