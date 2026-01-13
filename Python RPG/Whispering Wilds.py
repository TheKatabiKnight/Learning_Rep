#The Defensive Looter
# def safe_loot(value):
#     try: return int(value)
#     except ValueError: return "Error: This item is corrupted!"
    
# print(safe_loot(100))
# print(safe_loot("Poison Gas"))


#The Totem Stabilizer
# def stabilize_totem(mana, divisor):
    
#     try: division = mana / int(divisor)
#     except ValueError: return "Totem Error: Invalid data!"
#     except ZeroDivisionError: return "Totem Error: Cannot divide by void!"
#     else: return division

# print(stabilize_totem(100, "5"))
# print(stabilize_totem(100, "0"))
# print(stabilize_totem(100, "Unknown"))


#The Fragile Inventory
# def get_item(inventory, index):
#     try: return inventory[index]
#     except IndexError: return "Item not found in that slot!"

# print(get_item(["Potion", "Shield", "Sword"], 5))


# The Alchemist's Error
# def parse_potions(data_list):
#     total_healing = 0
#     for data in data_list:
#         try: 
#             total_healing += int(data)
#         except ValueError:
#             pass
#         finally:
#             print("Item checked.")
#     return total_healing

# print(parse_potions(["10", "Broken", "20", "Corrupted"]))


#The Battle-Log Defender
def execute_command(command_dict):
    try: 
        command_dict["action"]
        attack = int(command_dict["power"]) * 1.5
    except ValueError: 
        return "Invalid power level!"
    except KeyError:
        return "Missing action command!"
    except Exception as e:
        return f"Critical glitch: {e}"
    else:
        return attack
    
print(execute_command({"action": "Slay", "power": "10"}))
print(execute_command({"action": "Slay", "power": "High"}))
print(execute_command({"power": "10"}))

