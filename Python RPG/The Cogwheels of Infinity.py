#📖 The Spellbook: Iterators & Generators

#⚔️ Training Grounds: The Endless Mana Well
# def mana_generator(start_mana, max_limit):
#     while start_mana < max_limit:
#         yield start_mana
#         start_mana += 10
# for mana in mana_generator(10, 50):
#     print (mana)

# 📜 Legendary Tip: The Memory Ghost
# Grand Overseer, you have created a 'Memory Ghost.' If you had made a list of 1,000,000 mana points,
# it would have taken up a massive chunk of your spirit's storage (RAM). 
# But this generator, no matter how many millions of points it produces, takes up the same tiny amount of space. 
# It is a portal, not a container!


#⚙️ Training Grounds: The Hero’s Choice
# def loot_generator():
#     yield "Common Sword"
#     yield "Rare Shield"
#     yield "Epic Armor"
        
# bag = loot_generator()
# print(next(bag))
# print(next(bag))

# 📜 Legendary Tip: The Final Breath
# Grand Overseer, you have mastered the next() draw. But beware: if you call next() one too many times—after the "Epic Armor"
# is gone—the generator will let out its final breath: a StopIteration error. In the higher circles, we often wrap our next() calls
# in a try/except block to catch this silent end of the stream!


#⚔️ LEGENDARY QUEST: The Loot Filter
# def loot_generator():
#     yield "Common Sword"
#     yield "Rare Shield"
#     yield "Epic Armor"
#     yield "Broken Hilt"
#     yield "Rare Potion"
# def loot_filter(incoming_stream):
#     for item in incoming_stream:
#         if "Rare" in item or "Epic" in item:
#             yield item
# for item in loot_filter(loot_generator()):
#     print(item)

#📜 Legendary Tip: The Generator Expression
# Grand Overseer, your multi-line generator was structurally perfect. 
# However, if you ever need a simple filter in the heat of battle, you can use a Generator Expression—it's 
# like a list comprehension but with parentheses () instead of brackets []:
# filtered = (item for item in source if "Rare" in item)
# This creates the same memory-efficient sieve in just one line!