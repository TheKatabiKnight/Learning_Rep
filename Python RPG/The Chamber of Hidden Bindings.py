#📖 The Spellbook: Closures

#⚔️ Training Grounds: The Power Multiplier
def create_buff(multiplier):
    def apply_buff(base_damage):
        return base_damage * multiplier
    return apply_buff
double_damage = create_buff(2)
triple_damage = create_buff(3)
# print(double_damage(50))
# print(triple_damage(50))
# print(triple_damage.__closure__[0].cell_contents)


#🌫️ Training Grounds: The State-Shifter
def create_cooldown(start_time):
    def tick():
        nonlocal start_time
        start_time -= 1
        return start_time
    return tick
my_timer = create_cooldown(3)
# print(my_timer())
# print(my_timer())
# print(my_timer())
# print(my_timer())


#👥 BOSS FIGHT: Mnemonic, the Corrupted Memory

#Side Quest: The Session Chronometer
def creat_tracker(count):
    def track():
        nonlocal count
        count += 1
        return count
    return track
tracker = creat_tracker(0)
# print(tracker())
# print(tracker())
# print(tracker())
# print(tracker.__closure__[0].cell_contents)



#Main Quest: The Buff Decay
def create_decaying_buff(multiplier):
    def apply(damage):
        nonlocal multiplier
        buff_damage = damage * multiplier
        multiplier -= 0.5
        return buff_damage
    return apply
buff = create_decaying_buff(2.0)
# print(buff(100))
# print(buff(100))
# print(buff(100))



#Legendary Quest: The Mana Regulator
def create_mana_pool(max_mana):
    def spend_mana(amount):
        nonlocal max_mana
        if amount <= max_mana:
            max_mana -= amount
            return max_mana
        else:
            return "Insufficient Mana!"
    return spend_mana
caster = create_mana_pool(100)
# print(caster(40))
# print(caster(60))
# print(caster(15))
