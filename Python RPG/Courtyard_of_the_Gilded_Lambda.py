# def sort_players(player_list):
#     return sorted(player_list, key=lambda player: -player["score"])
# sorted = sort_players([
#     {"name": "Alice", "score": 88},
#     {"name": "Bob", "score": 95},
#     {"name": "Charlie", "score": 70},
#     {"name": "Diana", "score": 99}
# ])
# print(sorted)

#Boss Fight : Syntax Serpent
# def prioritize_threats(enemies):
#     full_health_enemies = list(filter(lambda enemy: enemy["health"] > 0 , enemies))
#     threat_level = sorted(full_health_enemies, key=lambda full_health_enemy: -(full_health_enemy["damage"]*full_health_enemy["speed"]))
#     return threat_level
# enemy_priority = prioritize_threats([
#     {"name": "Shadow Stalker", "damage": 10, "speed": 5, "health": 50},
#     {"name": "Void Reaver", "damage": 20, "speed": 10, "health": 0},
#     {"name": "Null Sprite", "damage": 5, "speed": 2, "health": 10},
#     {"name": "Syntax Wraith", "damage": 15, "speed": 8, "health": 100}
# ])
# print(enemy_priority)
# Note: "Void Reaver" is vanished into the void because its health was 0.