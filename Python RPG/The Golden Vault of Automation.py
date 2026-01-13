#The Automated Discount
# def apply_discount(price_list):
#     return [discount for price in price_list if (discount:=price * 0.8 )> 50]
# print(apply_discount([100, 40, 200, 60]))


#The Hall of the Gilded Key-Value
def map_rarity(item_data):
    return {item_name: "Legendary" if power_level > 75 else "Common" for item_name, power_level in item_data}

print(map_rarity([("Excalibur", 90), ("Rusty Sword", 10), ("Aegis", 80), ("Wooden Club", 5)]))