#📖 The Spellbook: Polymorphism & Overriding

#⚔️ Training Grounds: The Shapeshifter’s Strike
class Warrior:
    def strike(self):
        return "Swings a heavy claymore!"
class Mage:
    def strike(self):
        return "Fires a bolt of arcane lightning!"
def execute_attack(hero):
    return hero.strike()
# warrior = Warrior()
# mage = Mage()
# print(execute_attack(warrior))
# print(execute_attack(mage))


#🏛️ The Project: The combat.py Evolution
class BaseWeapon:
    def __init__(self, base_damage):
        self.base_damage = base_damage
    def calculate_damage(self):
        return self.base_damage
class EnchantedWeapon(BaseWeapon):
    def __init__(self, base_damage, bonus_damage):
        super().__init__(base_damage)
        self.bonus_damage = bonus_damage
    def calculate_damage(self):
        return super().calculate_damage() + self.bonus_damage
# BOE = BaseWeapon(50)
# BOE_forged = EnchantedWeapon(50, 25)
# print(BOE.calculate_damage())
# print(BOE_forged.calculate_damage())


#👥 BOSS FIGHT: The Mirror-Stalker

#Side Quest: The Interaction Unification
class Door:
    def interact(self):
        return "You open the Door!"
class Chest:
    def interact(self):
        return "You open the Chest!"
def trigger_interaction(obj):
    return obj.interact()
# dungeon_door = Door()
# treasure_chest = Chest()
# print(trigger_interaction(dungeon_door))
# print(trigger_interaction(treasure_chest))


#Main Quest: The Multi-Tool System
class Weapon:
    def __init__(self, power):
        self.power = power
    def get_damage(self):
        return self.power
class EnchantedWeapon(Weapon):
    def __init__(self, power):
        super().__init__(power)
    def get_damage(self):
        return super().get_damage() * 1.5
# Two_Handed_Sword = Weapon(146)
# Dragon_Slayer = EnchantedWeapon(146)
# print(Two_Handed_Sword.get_damage())
# print(Dragon_Slayer.get_damage())


#Legendary Quest: The Weapon-Master Engine
class Melee:
    def execute(self):
        return 100
class Magic:
    def execute(self):
        return 150
class Ranged:
    def execute(self):
        return 80
def process_combat_queue(queue_list):
    return [damage_type.execute() for damage_type in queue_list]
# print(process_combat_queue([Melee(), Magic(), Ranged()]))