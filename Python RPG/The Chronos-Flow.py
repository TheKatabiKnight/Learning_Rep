import asyncio
#📖 The Spellbook: Asynchronous Rituals

#⚔️ Training Grounds: The Parallel Potion Brew
# async def brew_potion(name, time):
#     print(f"Starting {name} brew...")
#     await asyncio.sleep(time)
#     print(f"{name} is ready!")
# async def main():
#     await asyncio.gather(brew_potion("Health", 2), brew_potion("Mana", 1))
# asyncio.run(main())


#🏛️ The Project: The server.py Foundation
# async def listen_for_players():
#     while True:
#         print("Listening for new heroes...")
#         await asyncio.sleep(3)
# async def update_world():
#     while True:
#         print("Updating monster positions...")
#         await asyncio.sleep(1)
# async def main():
#     await asyncio.gather(
#         listen_for_players(),
#         update_world()
#     )
# asyncio.run(main())


#🌀 BOSS FIGHT: Temporal-Meld, the Paradox Weaver

# Side Quest: The Quick-Cast Trigger 
# async def cast_spell(name):
#     print(f"Chanting {name}...")
#     await asyncio.sleep(1)
#     print(f"{name} cast!")
# asyncio.run(cast_spell("FireBolt"))

#Main Quest: The Loot Dispatcher 
# async def send_loot(player_name):
#     print(f"Sending loot to {player_name}...")
#     await asyncio.sleep(1)
#     print(f"Loot delivered to {player_name}!")
# async def dispatch_all_loot(players):
#         await asyncio.gather(*(send_loot(p) for p in players))
# asyncio.run(dispatch_all_loot(["Aris", "Cid", "Elara"]))


#Legendary Quest: The Combat Cooldown Engine
async def cooldown_timer(skill_name, seconds):
    print(f"{skill_name} on cooldown...")
    await asyncio.sleep(seconds)
    print(f"{skill_name} is ready!")
async def main_combat_loop():
    await asyncio.gather(cooldown_timer("FireBall", 3), cooldown_timer("Heal", 5), cooldown_timer("Shield", 2))
asyncio.run(main_combat_loop())