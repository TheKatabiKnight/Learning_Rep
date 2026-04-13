from progression.utils import get_welcome_message, Training_Grounds, character_creation
from config import NexusConfig
from src.entities.Entities import Warrior, CombatEntity, Stats
from progression.story import training_part1
import asyncio
from ursina import *
import random
from src.core.persistence import load_player_state
from src.entities.player import Player
from src.entities.monster import Monster
from src.core.world import create_environment










app = Ursina()

###Game Start###
if __name__ == "__main__" :
    print(get_welcome_message())
    print(NexusConfig.format_header(NexusConfig.WORLD_NAME))
    #difficulty for later#
    # difficulty = NexusConfig.update_difficulty(input("Please Choose difficulty (Easy/Normal/Hard)"))
    # print(f"{difficulty} difficulty chosen!!")

###Character Creation###
if __name__ == "__main__" :
   character_creation()
###Training Grounds###
if __name__ == "__main__" :
    Training_Grounds()
    asyncio.run(training_part1())
    


environment = create_environment()

data = load_player_state("save_player_data.txt")

my_data = CombatEntity("9tiba", data["player_current_hp"], 100)
player = Player(my_data, data["position"], monster=Monster)

slimes = [
          Monster(CombatEntity("Slime", 60, 60),
          pos=(random.uniform(1, 10), 1.5, random.uniform(1, 10)),
          player=player) for i in range(5)
          ]



app.run()

    
    

    