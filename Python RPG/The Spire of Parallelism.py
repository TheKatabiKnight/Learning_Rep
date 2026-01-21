#📖 The Spellbook: First-Class Functions

#⚔️ Training Grounds: The Spell Infuser
# def double_damage(value):
#     return value * 2
# def add_fire_damage(value):
#     return value + 10
# def apply_combat_effect(effect_func, base_dmg):
#     return effect_func(base_dmg)
# print(apply_combat_effect(double_damage, 50))
# print(apply_combat_effect(add_fire_damage, 50))

#📜 Legendary Tip: The Anonymous Conduit
# Script-Bearer, you passed named functions with great skill. But remember the Lambda ritual you mastered in the valley!
#  You can pass an "anonymous" spell directly into the conduit without naming it first:
# apply_combat_effect(lambda x: x * 3, 50)
# This is the way of the high-speed Shadow-Casters who have no time for formal naming.



#⚔️ Training Grounds: The Battle Logger
# def battle_log(func):
#     def wrapper(*args, **kwargs):
#         print("Executing combat maneuver...")
#         return func(*args, **kwargs)
#     return wrapper
# @battle_log
# def strike(damage):
#     return f"Strike dealt {damage} damage!"
# print(strike(50))

# 📜 Legendary Tip: The Universal Wrapper
# Script-Bearer, your use of *args was perfect for this maneuver. 
# However, in the highest levels of the Spire, masters always pair it with **kwargs. 
# This ensures your decorator can wrap any function, even those with named "Keyword Arguments." 
#     A truly universal wrapper looks like this:
# def wrapper(*args, **kwargs): return func(*args, **kwargs)



#⚔️ SIDE QUEST: The Mana Monitor
# def monitor_mana(func):
#     def wrapper(*args, **kwargs):
#         print("Subtracting mana from pool...")
#         return func(*args, **kwargs)
#     return wrapper
# @monitor_mana
# def cast_fireball():
#     return "Fireball launched!"
# print(cast_fireball())


#Main Quest: The Critical Enchantment
# def critical_boost(func):
#     def wrapper(*args, **kwargs):
#         print("BOOM!! CRITICAL!!")
#         return func(*args, **kwargs) * 2
#     return wrapper
# @critical_boost
# def base_attack(damage):
#     return damage
# print(base_attack(50))


#⚔️ LEGENDARY QUEST: The Shield of Persistence
# def safe_execution(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except ValueError:
#             return f"Shield Active: Cores Overloaded intercepted."
#     return wrapper
# @safe_execution
# def unstable_spell():
#     raise ValueError("Cores Overloaded")
# print(unstable_spell())

#📜 Legendary Tip: The Generic Catch
# Grand Weaver, your shield was perfectly tuned to the ValueError. However, in the wildest lands, 
# you may not know what demon is coming. Using except Exception: (the "Grand Net") is safer for a generic safe_execution decorator,
# as it ensures that any error—be it a KeyError, TypeError, or ValueError—is caught by the shield!

