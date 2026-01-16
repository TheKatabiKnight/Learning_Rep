#📖The Spellbook: APIs & JSON
#JSON scroll (JavaScript Object Notation)
# API (Application Programming Interface)


#⚔️ Training Grounds: The Merchant’s Signal
# import json
# def parse_merchant_signal(json_data):
#     return json.loads(json_data)["item"]
# print(parse_merchant_signal('{"merchant": "Alaric", "item": "Dragon Scale", "price": 500}'))

# 📜 Legendary Tip: The Pretty-Printing Ritual
# Script-Bearer, while json.dumps() creates a string the machine loves, it is often a jumbled mess for human eyes.
# If you ever need to read a complex JSON scroll yourself, use the indent incantation: json.dumps(data, indent=4). 
# This adds spacing and line breaks, turning a chaotic clump of text into a structured work of art.


#🕸️ Training Grounds: The Beacon's Call
# import json
# def serialize_player_stats(stats_dict):
#     return json.dumps(stats_dict, indent=4)
# print(serialize_player_stats({"name": "Script-Bearer", "hp": 121, "level": 8}))


#🕷️ BOSS FIGHT: Pharos-Null, The Weaver of False Echoes

#Side Quest: The High-Score Extraction
# import json
# def get_weapon_power(json_string):
#     return json.loads(json_string)["stats"]["power"]
# print(get_weapon_power('{"item": "Sun-Slayer", "stats": {"power": 150, "durability": 80}}'))



#Main Quest: The Data Purifier
# import json
# def active_status(users_list):
#     return [user for user in json.loads(users_list) if user["status"] == "active"]
# print(active_status('[{"user": "Alice", "status": "active"}, {"user": "Null", "status": "corrupted"}]'))

# 📜 Legendary Tip: The Comprehension Shortcut
# Script-Bearer, your use of the List Comprehension ritual combined with the JSON-parsing spell was masterful. 
# In the lands of the Web, where data lists can be miles long, 
# this one-line filtering ritual is the difference between a quick victory and a timed-out connection!



#Legendary Quest: The Handshake Protocol
# import json
# def secure_handshake(json_input):
#     handshake = json.loads(json_input)
#     handshake["status"] = "verified"
#     handshake["key_bearer"] = "Script-Bearer"
#     return json.dumps(handshake)
# print(secure_handshake('{"session_id": 12345}'))

# 📜 Legendary Tip: The Update Incantation
# Script-Bearer, your logic for adding keys was clean and precise. 
# However, if you ever have a large scroll of metadata to add at once, you can use the .update() ritual:
# handshake.update({"status": "verified", "key_bearer": "Script-Bearer"})
# This merges one dictionary into another in a single, efficient motion!