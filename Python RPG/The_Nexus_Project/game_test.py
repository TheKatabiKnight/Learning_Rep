from src.entities.Entities import CombatEntity
from ursina import *
import random
from src.core.persistence import load_player_state
from src.entities.player import Player
from src.entities.monster import Monster
from src.core.world import create_environment


app = Ursina()

environment = create_environment()

data = load_player_state("save_player_data.txt")

my_data = CombatEntity("9tiba", data["player_current_hp"], 100)
player = Player(my_data, data["position"], monster=Monster)

slimes = [
          Monster(CombatEntity("Slime", 60, 60),
          pos=(random.uniform(1, 9), 1.5, random.uniform(1, 9)),
          player=player) for i in range(5)
          ]

EditorCamera() #todebug

app.run()