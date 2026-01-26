#📖 The Spellbook: Collection Properties

#⚔️ Training Grounds: The Skill-Slot Guardian
class SkillManager:
    def __init__(self, max_slots):
        self._skills = []
        self._max_slots = max_slots
    @property
    def skills(self):
        return self._skills
    @skills.setter
    def skills(self, skills):
        if len(skills) > self._max_slots:
            self._skills = skills[:self._max_slots]
        else:
            self._skills = skills
# Mage_skills = SkillManager(3)
# Mage_skills.skills = (["Fireball", "Teleport", "Ice Shield", "Magic Missile", "Flight"])
# print(Mage_skills.skills)


#The Project: The entities.py Skill System
class SkillManager:
    def __init__(self, max_slots):
        self._skills = []
        self._max_slots = max_slots
    @property
    def skills(self):
        return self._skills[:]
    @skills.setter
    def skills(self, skills):
        if len(skills) > self._max_slots:
            self._skills = skills[:self._max_slots]
        else:
            self._skills = skills
    def add_skill(self, new_skill):
        if new_skill in self._skills:
            return "Skill already learned!"
        else:
            if len(self._skills) < self._max_slots:
                self._skills.append(new_skill)
                return "Skill added!"
            else:
                return "No more slots available!"
# slots = SkillManager(2)
# print(slots.add_skill("Meditation"))
# print(slots.add_skill("Meditation"))
# print(slots.add_skill("Shield Slam"))
# print(slots.add_skill("Fireball"))

#📜 Legendary Tip: The Shield of the Copy
#To be truly invincible, masters often return a copy of the list in @property:
# return self._skills[:]


#🐍 BOSS FIGHT: The Hydra of Overlapping Data

#⚔️ SIDE QUEST: The Type Guard
class Item:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name[:]
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
# item1 = Item("Unknown")
# item1.name = 777
# item1.name = "Excalibur"
# print(item1.name)


#Main Quest: The Inventory Sieve
class InventoryManager:
    def __init__(self, max_size):
        self._max_size = max_size
        self._items = []
    @property
    def items(self):
        return self._items[:]
    @items.setter
    def items(self, items):
        if len(self._items) > self._max_size:
            self._items = items[:self._max_size]
        else:
            self._items = items
    def add_item(self, name):
        if name in self._items:
            return "Duplicate"
        else:
            if len(self._items) < self._max_size:
                self._items.append(name)
                return "Added"
            else:
                return "Full"
# my_inventory = InventoryManager(3)
# my_inventory.add_item("Candy_stick")
# my_inventory.add_item("Sugar")
# print(my_inventory.add_item("Rusty_sword"))
# print(my_inventory.add_item("Rusty_sword"))
# print(my_inventory.add_item("Grey_Staff"))
# print(my_inventory.items)


#Legendary Quest: The Skill-Tree Architect
class SkillSystem:
    def __init__(self, max_slots):
        self._max_slots = max_slots
        self._skills = []
    @property
    def skills(self):
        return self._skills[:]
    def learn_skill(self, name, rank):
        skill_des = f"{name} (Rank {rank})"
        if skill_des not in self._skills:
            if len(self._skills) < self._max_slots:
                self._skills.append(skill_des)
                return "Learned"
            else:
                return "Failed"
        else:
            return "Failed"
    def forget_skill(self, name_with_rank):
        if name_with_rank in self._skills:
            self._skills.remove(name_with_rank)
# skill = SkillSystem(max_slots=2)
# print(skill.learn_skill("Fireball", 1))
# print(skill.learn_skill("Fireball", 1))
# print(skill.learn_skill("Heal", 2))
# print(skill.learn_skill("Teleport", 1))
# print(skill.skills)
# print(skill.forget_skill("Fireball (Rank 1)"))
# print(skill.skills)











