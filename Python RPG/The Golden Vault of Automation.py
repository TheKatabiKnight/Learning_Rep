#The Automated Discount
# def apply_discount(price_list):
#     return [discount for price in price_list if (discount:=price * 0.8 )> 50]
# print(apply_discount([100, 40, 200, 60]))


#The Hall of the Gilded Key-Value
# def map_rarity(item_data):
#     return {item_name: "Legendary" if power_level > 75 else "Common" for item_name, power_level in item_data}

# print(map_rarity([("Excalibur", 90), ("Rusty Sword", 10), ("Aegis", 80), ("Wooden Club", 5)]))


#SIDE QUEST: The Loot Compressor
# def compress_loot(loot_list):
#     return [item for compressed in loot_list if (item:= compressed.strip()) != "junk"]

# print(compress_loot([" Sword ", "Potion", " Shield ", "junk", " Bow "]))


#MAIN QUEST: The Stat Multiplier
# def boost_stats(stats_dict):
#     return {stat: value * 2 if value >= 10 else value * 5 for stat, value in stats_dict.items()}

# print(boost_stats({"Strength": 10, "Agility": 5, "Luck": 2, "Intellect": 20}))


#LEGENDARY QUEST: The Matrix Decipher
# def flatten_and_filter(matrix):
#     return [ num for part in matrix for num in part if num > 40]

# print(flatten_and_filter([[10, 50, 20], [80, 5, 90], [30, 100, 15]]))