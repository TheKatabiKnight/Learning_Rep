#📖 The Spellbook: The Game Loop

#⚔️ Training Grounds: The Echo Heartbeat
# while True:
#     action = input("Enter command: ").lower()
#     if action == "attack":
#         print("You swing your blade!")
#     elif action == "heal":
#         print("You consume a potion.")
#     elif action == "exit":
#         print("Leaving the Nexus...")
#         break
#     else:
#         print("Unknown command.")


#🏛️ The Project: The engine.py Prototype
# hero_hp = 50
# while True:
#     print(f"Hero HP: {hero_hp}")
#     action = input("Action (rest/hazard/quit): ").lower()
#     if action == "rest":
#         hero_hp += 10
#     elif action == "hazard":
#         hero_hp -= 20
#     elif action == "quit":
#         print("Game Over.")
#         break
#     else:
#         print("Unknown command.")
#     if hero_hp <= 0:
#         print("The Hero has fallen...")
#         break

    
#🌀 BOSS FIGHT: Synchronos, the Overlord

#Main Quest: The Resource Heartbeat
# mana = 30
# while True:
#     spell = input("Type 'cast' to cast a spell: ").lower()
#     if spell == "cast":
#         if mana < 10:
#             print("Out of mana!")
#             break
#         mana -= 10
#     else:
#         print("Unknown command.")
#     if mana < 30:
#             mana += 5


#⚔️ LEGENDARY QUEST: The Saga Engine Alpha
hp = 100
inventory = []
max_inv = 2

while True:
    print(f"HP: {hp} | Bag: {inventory}")
    action = input("Action (take/hazard/exit): ").lower()
    if action == "take":
        if len(inventory) < max_inv:
            inventory.append("Relic")
        else:
            print("Bag full!")
    elif action == "hazard":
        hp -= 50
    elif action == "exit":
        print("Exiting...")
        break
    else:
        print("Unknown command!")
    if hp <= 0:
        print("Game Over")
        break
        
