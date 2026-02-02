#📖 The Spellbook: *args and **kwargs

#⚔️ Training Grounds: The Infinite Loot-Bag
def pack_satchel(*args):
    count = len(args)
    print(f"Packing {count} items...")
    return count
# print(pack_satchel("Sword", "Shield", "Potion"))
# print(pack_satchel("Map", "Compass"))

#📜 Legendary Tip: The Unpacking Ritual
# Grand Master, you have learned to Pack arguments into a tuple. But did you know you can use the same * to Unpack them? 
# If you have a list of items my_loot = ["Gold", "Silver"] and you call pack_satchel(*my_loot), 
# Python will explode the list into individual items before they enter the function. It is the art of the Shattered Container!



#🌫️ Training Grounds: The Attribute Infuser
def describe_merchant(**kwargs):
    kwargs.get("discount", 0)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    return "Profile Complete"
# print(describe_merchant(name="Alaric", shop="The Gilded Lily", discount=0.1))



#🌀 BOSS FIGHT: Apeiron, the Anomaly

#Side Quest: The Mass Loot Processor
def sum_gold(*args):
    return sum(args)
# print(sum_gold(10, 20, 30))

#Main Quest: The Character Customizer
class Hero:
    def __init__(self, name, **kwargs):
        self.name = name
        self.traits = kwargs
    def get_trait(self, key):
        for key, value in self.traits.items():
            return value
# print(Hero("Aris", str=10).get_trait("str"))


#Legendary Quest: The Universal Event Handler
def log_event(event_name, *tags, **details):
    print(f"Event: {event_name}")
    for tag in tags:
        print(f"Tag: {tag}")
    for key, value in details.items():
        print(f"{key} -> {value}")
    return len(tags) + len(details)
print(log_event("LevelUp", "Hero", "NewSkill", level=22, xp=5000))
        

