###Weapon Creation###
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
    
###Combat Queue###
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